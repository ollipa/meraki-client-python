"""Asynchronous REST session for the SDK."""

import asyncio
import json
import logging
import random
import ssl
import urllib.parse
from collections.abc import Generator
from datetime import datetime, timezone
from typing import Any, Literal

import aiohttp

from meraki_dashboard_sdk.__init__ import __version__
from meraki_dashboard_sdk.common import BaseURL, reject_v0_base_url, validate_user_agent
from meraki_dashboard_sdk.config import (
    ACTION_BATCH_RETRY_WAIT_TIME,
    AIO_MAXIMUM_CONCURRENT_REQUESTS,
    BE_GEO_ID,
    CERTIFICATE_PATH,
    DEFAULT_BASE_URL,
    MAXIMUM_RETRIES,
    MERAKI_PYTHON_SDK_CALLER,
    NETWORK_DELETE_RETRY_WAIT_TIME,
    NGINX_429_RETRY_WAIT_TIME,
    REQUESTS_PROXY,
    RETRY_4XX_ERROR,
    RETRY_4XX_ERROR_WAIT_TIME,
    SIMULATE_API_CALLS,
    SINGLE_REQUEST_TIMEOUT,
    USE_ITERATOR_FOR_GET_PAGES,
    WAIT_ON_RATE_LIMIT,
)
from meraki_dashboard_sdk.exceptions import APIError, AsyncAPIError


class Session:
    """Main module interface."""

    def __init__(
        self,
        *,
        api_key: str,
        base_url: BaseURL,
        single_request_timeout: int,
        certificate_path: str | None,
        proxy: str | None,
        wait_on_rate_limit: bool,
        maximum_retries: int,
        caller: str | None,
        version: str,
        maximum_concurrent_requests: int = AIO_MAXIMUM_CONCURRENT_REQUESTS,
    ) -> None:
        super().__init__()

        # Initialize attributes and properties
        self._version = __version__
        self._api_key = str(api_key)
        self._base_url = str(base_url)
        self._single_request_timeout = single_request_timeout
        self._certificate_path = certificate_path
        self._requests_proxy = requests_proxy
        self._wait_on_rate_limit = wait_on_rate_limit
        self._nginx_429_retry_wait_time = nginx_429_retry_wait_time
        self._action_batch_retry_wait_time = action_batch_retry_wait_time
        self._network_delete_retry_wait_time = network_delete_retry_wait_time
        self._retry_4xx_error = retry_4xx_error
        self._retry_4xx_error_wait_time = retry_4xx_error_wait_time
        self._maximum_retries = maximum_retries
        self._simulate = simulate
        self._concurrent_requests_semaphore = asyncio.Semaphore(maximum_concurrent_requests)
        self._be_geo_id = be_geo_id
        self._caller = caller
        self.use_iterator_for_get_pages = use_iterator_for_get_pages

        # Check base URL
        reject_v0_base_url(self)

        # Update the headers for the session
        self._headers = {
            "Authorization": "Bearer " + self._api_key,
            "Content-Type": "application/json",
            "User-Agent": f"python-meraki/aio-{self._version} "
            + validate_user_agent(self._be_geo_id, self._caller),
        }
        if self._certificate_path:
            self._sslcontext = ssl.create_default_context()
            self._sslcontext.load_verify_locations(certificate_path)

        # Initialize a new `aiohttp` session
        self._req_session = aiohttp.ClientSession(
            headers=self._headers,
            timeout=aiohttp.ClientTimeout(total=single_request_timeout),
        )

        # Log API calls
        self._logger = logger
        self._parameters = {"version": self._version}
        self._parameters.update(locals())
        self._parameters.pop("self")
        self._parameters.pop("logger")
        self._parameters.pop("__class__")
        self._parameters["api_key"] = "*" * 36 + self._api_key[-4:]
        if self._logger:
            self._logger.info(
                f"Meraki dashboard API session initialized with these parameters: {self._parameters}"
            )

    @property
    def use_iterator_for_get_pages(self):  # noqa: ANN201, D102
        return self._use_iterator_for_get_pages

    @use_iterator_for_get_pages.setter
    def use_iterator_for_get_pages(self, value):  # noqa: ANN001, ANN202
        if value:
            self.get_pages = self._get_pages_iterator
        else:
            self.get_pages = self._get_pages_legacy

        self._use_iterator_for_get_pages = value

    async def request(
        self, metadata: dict[str, str], method: str, url: str, **kwargs: dict[str, Any]
    ) -> aiohttp.ClientResponse | None:
        """Make an HTTP request to the API endpoint."""
        async with self._concurrent_requests_semaphore:
            return await self._request(metadata, method, url, allow_redirects=False, **kwargs)

    async def _request(  # noqa: PLR0912, PLR0915
        self, metadata: dict[str, str], method: str, url: str, **kwargs: dict[str, Any]
    ) -> aiohttp.ClientResponse | None:
        # Metadata on endpoint
        tag = metadata["tags"][0]
        operation = metadata["operation"]

        # Update request kwargs with session defaults
        if self._certificate_path:
            kwargs.setdefault("ssl", self._sslcontext)
        if self._requests_proxy:
            kwargs.setdefault("proxy", self._requests_proxy)
        kwargs.setdefault("timeout", self._single_request_timeout)

        # Ensure proper base URL
        allowed_domains = ["meraki.com", "meraki.cn"]

        # aiohttp manipulates URLs as instances of the yarl.URL class
        if not isinstance(url, str):
            url = str(url)

        parsed_url = urllib.parse.urlparse(url)

        abs_url = (
            url
            if any(domain in parsed_url.netloc for domain in allowed_domains)
            else self._base_url + url
        )

        # Set maximum number of retries
        retries = self._maximum_retries

        # Option to simulate non-safe API calls without actually sending them
        if self._logger:
            self._logger.debug(metadata)
        if self._simulate and method != "GET":
            if self._logger:
                self._logger.info(f"{tag}, {operation} > {abs_url} - SIMULATED")
            return None
        response = None
        message = None
        for _ in range(retries):
            # Make sure that the response object gets closed during retries
            if response:
                response.release()
                response = None

            # Make the HTTP request to the API endpoint
            try:
                if self._logger:
                    self._logger.info(f"{method} {abs_url}")
                response = await self._req_session.request(method, abs_url, **kwargs)
                reason = response.reason if response.reason else None
                status = response.status
            except aiohttp.client_exceptions.ClientError as e:
                if self._logger:
                    self._logger.warning(
                        f"{tag}, {operation} > {abs_url} - {e}, retrying in 1 second"
                    )
                await asyncio.sleep(1)
                continue

            if 200 <= status < 300:
                if "page" in metadata:
                    counter = metadata["page"]
                    if self._logger:
                        self._logger.info(
                            f"{tag}, {operation}; page {counter} > {abs_url} - {status} {reason}"
                        )
                elif self._logger:
                    self._logger.info(f"{tag}, {operation} > {abs_url} - {status} {reason}")
                # For non-empty response to GET, ensure valid JSON
                try:
                    if method == "GET":
                        await response.json(content_type=None)
                except (
                    json.decoder.JSONDecodeError,
                    aiohttp.client_exceptions.ContentTypeError,
                ) as e:
                    if self._logger:
                        self._logger.warning(
                            f"{tag}, {operation} > {abs_url} - {e}, retrying in 1 second"
                        )
                    await asyncio.sleep(1)
                else:
                    return response
            # Handle 3XX redirects automatically
            elif 300 <= status < 400:
                abs_url = response.headers["Location"]
                substring = "meraki.com/api/v"
                if substring not in abs_url:
                    substring = "meraki.cn/api/v"
                self._base_url = abs_url[: abs_url.find(substring) + len(substring) + 1]
            # Rate limit 429 errors
            elif status == 429:
                if "Retry-After" in response.headers:
                    wait = int(response.headers["Retry-After"])
                else:
                    wait = random.randint(1, self._nginx_429_retry_wait_time)
                if self._logger:
                    self._logger.warning(
                        f"{tag}, {operation} > {abs_url} - {status} {reason}, retrying in {wait} seconds"
                    )
                await asyncio.sleep(wait)
            # 5XX errors
            elif status >= 500:
                if self._logger:
                    self._logger.warning(
                        f"{tag}, {operation} > {abs_url} - {status} {reason}, retrying in 1 second"
                    )
                await asyncio.sleep(1)
            # 4XX errors
            else:
                try:
                    message = await response.json(content_type=None)
                    message_is_dict = bool(isinstance(message, dict))
                except aiohttp.client_exceptions.ContentTypeError:
                    message_is_dict = False
                    try:
                        message = (await response.text())[:100]
                    except Exception:  # noqa: BLE001
                        message = None

                # Check for specific concurrency errors
                network_delete_concurrency_error_text = (
                    "This may be due to concurrent requests to delete networks."
                )
                action_batch_concurrency_error = {
                    "errors": [
                        "Too many concurrently executing batches. Maximum is 5 confirmed but not yet executed batches."
                    ]
                }
                # Check specifically for network delete concurrency error
                if (
                    message_is_dict
                    and "errors" in message
                    and network_delete_concurrency_error_text in message["errors"][0]
                ):
                    wait = random.randint(15, self._network_delete_retry_wait_time)
                    if self._logger:
                        self._logger.warning(
                            f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds"
                        )
                    await asyncio.sleep(wait)
                    retries -= 1
                    if retries == 0:
                        raise APIError(metadata, response)
                # Check specifically for action batch concurrency error
                elif message == action_batch_concurrency_error:
                    wait = self._action_batch_retry_wait_time
                    if self._logger:
                        self._logger.warning(
                            f"{tag}, {operation} > {abs_url} - {status} {reason}, retrying in {wait} seconds"
                        )
                    await asyncio.sleep(wait)

                elif self._retry_4xx_error:
                    wait = random.randint(1, self._retry_4xx_error_wait_time)
                    if self._logger:
                        self._logger.warning(
                            f"{tag}, {operation} > {abs_url} - {status} {reason}, retrying in {wait} seconds"
                        )
                    await asyncio.sleep(wait)

                # All other client-side errors
                else:
                    if self._logger:
                        self._logger.error(
                            f"{tag}, {operation} > {abs_url} - {status} {reason}, {message}"
                        )
                    raise AsyncAPIError(metadata, response, message)
        raise AsyncAPIError(metadata, response, "Reached retry limit: " + str(message))

    async def get(
        self, metadata: dict[str, str], url: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Make a GET request to the API endpoint."""
        metadata["method"] = "GET"
        metadata["url"] = url
        metadata["params"] = params
        async with await self.request(metadata, "GET", url, params=params) as response:
            return await response.json(content_type=None)

    async def get_pages(
        self,
        metadata: dict[str, str],
        url: str,
        params: dict[str, Any] | None = None,
        total_pages: int = -1,
        direction: str = "next",
        event_log_end_time: str | None = None,
    ) -> Generator[Any, None, None]:
        """Make a GET request to the API endpoint with pagination."""

    async def _download_page(
        self, request: aiohttp.ClientResponse
    ) -> tuple[aiohttp.ClientResponse, Any]:
        response = await request
        result = await response.json(content_type=None)
        return response, result

    async def _get_pages_iterator(  # noqa: PLR0912
        self,
        metadata: dict[str, str],
        url: str,
        params: dict[str, Any] | None = None,
        total_pages: int | Literal["all"] = -1,
        direction: str = "next",
        event_log_end_time: str | None = None,
    ) -> Generator[Any, None, None]:
        if isinstance(total_pages, str) and total_pages.lower() == "all":
            total_pages = -1
        elif isinstance(total_pages, str) and total_pages.isnumeric():
            total_pages = int(total_pages)
        metadata["page"] = 1

        request_task = asyncio.create_task(
            self._download_page(self.request(metadata, "GET", url, params=params))
        )

        # Get additional pages if more than one requested
        while total_pages != 0:
            response, results = await request_task
            links = response.links

            # GET the subsequent page
            if direction == "next" and "next" in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata["operation"] == "getNetworkEvents":
                    starting_after = urllib.parse.unquote(
                        str(links["next"]["url"]).split("startingAfter=")[1]
                    )
                    delta = datetime.now(tz=timezone.utc) - datetime.fromisoformat(
                        starting_after[:-1]
                    )
                    # Break out of loop if startingAfter returned from next link is within 5 minutes of current time
                    if delta.total_seconds() < 300 or (
                        event_log_end_time and starting_after > event_log_end_time
                    ):
                        break

                metadata["page"] += 1
                nextlink = links["next"]["url"]
            elif direction == "prev" and "prev" in links:
                # Prevent getNetworkEvents from infinite loop as time goes backward (to epoch 0)
                if metadata["operation"] == "getNetworkEvents":
                    ending_before = urllib.parse.unquote(
                        str(links["prev"]["url"]).split("endingBefore=")[1]
                    )
                    # Break out of loop if endingBefore returned from prev link is before 2014
                    if ending_before < "2014-01-01":
                        break

                metadata["page"] += 1
                nextlink = links["prev"]["url"]
            else:
                total_pages = 1

            response.release()

            total_pages = total_pages - 1

            if total_pages != 0:
                request_task = asyncio.create_task(
                    self._download_page(self.request(metadata, "GET", nextlink))
                )

            return_items = []
            # just prepare the list
            if isinstance(results, list):
                return_items = results
            elif isinstance(results, dict) and "items" in results:
                return_items = results["items"]
            # For event log endpoint
            elif isinstance(results, dict):
                return_items = results["events"][::-1] if direction == "next" else results["events"]

            for item in return_items:
                yield item

    async def _get_pages_legacy(  # noqa: PLR0912
        self,
        metadata: dict[str, str],
        url: str,
        params: dict[str, Any] | None = None,
        total_pages: int | Literal["all"] = -1,
        direction: str = "next",
        event_log_end_time: str | None = None,
    ) -> dict[str, Any] | None:
        if isinstance(total_pages, str) and total_pages.lower() == "all":
            total_pages = -1
        elif isinstance(total_pages, str) and total_pages.isnumeric():
            total_pages = int(total_pages)
        metadata["page"] = 1

        async with await self.request(metadata, "GET", url, params=params) as response:
            results = await response.json(content_type=None)

            # For event log endpoint when using 'next' direction, so results/events are sorted chronologically
            if (
                isinstance(results, dict)
                and metadata["operation"] == "getNetworkEvents"
                and direction == "next"
            ):
                results["events"] = results["events"][::-1]

            links = response.links

        # Get additional pages if more than one requested
        while total_pages != 1:
            # GET the subsequent page
            if direction == "next" and "next" in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata["operation"] == "getNetworkEvents":
                    starting_after = urllib.parse.unquote(
                        str(links["next"]["url"]).split("startingAfter=")[1]
                    )
                    delta = datetime.now(tz=timezone.utc) - datetime.fromisoformat(
                        starting_after[:-1]
                    )
                    # Break out of loop if startingAfter returned from next link is within 5 minutes of current time
                    if delta.total_seconds() < 300 or (
                        event_log_end_time and starting_after > event_log_end_time
                    ):
                        break

                metadata["page"] += 1
                nextlink = links["next"]["url"]
            elif direction == "prev" and "prev" in links:
                # Prevent getNetworkEvents from infinite loop as time goes backward (to epoch 0)
                if metadata["operation"] == "getNetworkEvents":
                    ending_before = urllib.parse.unquote(
                        str(links["prev"]["url"]).split("endingBefore=")[1]
                    )
                    # Break out of loop if endingBefore returned from prev link is before 2014
                    if ending_before < "2014-01-01":
                        break

                metadata["page"] += 1
                nextlink = links["prev"]["url"]
            else:
                break

            async with await self.request(metadata, "GET", nextlink) as response:
                links = response.links
                # Append that page's results, depending on the endpoint
                if isinstance(results, list):
                    results.extend(await response.json(content_type=None))
                elif isinstance(results, dict) and "items" in results:
                    json_response = await response.json(content_type=None)
                    results.extend(json_response["items"])
                    if "meta" in results:
                        results["meta"]["counts"]["items"]["remaining"] = json_response["meta"][
                            "counts"
                        ]["items"]["remaining"]
                # For event log endpoint
                elif isinstance(results, dict):
                    json_response = await response.json(content_type=None)
                    start = json_response["pageStartAt"]
                    end = json_response["pageEndAt"]
                    events = json_response["events"]
                    if direction == "next":
                        events = events[::-1]
                    results["pageStartAt"] = min(results["pageStartAt"], start)
                    results["pageEndAt"] = max(results["pageEndAt"], end)
                    results["events"].extend(events)

            total_pages = total_pages - 1

        return results

    async def post(
        self, metadata: dict[str, str], url: str, json: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Make a POST request to the API endpoint."""
        metadata["method"] = "POST"
        metadata["url"] = url
        metadata["json"] = json
        async with await self.request(metadata, "POST", url, json=json) as response:
            return await response.json(content_type=None)

    async def put(
        self, metadata: dict[str, str], url: str, json: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Make a PUT request to the API endpoint."""
        metadata["method"] = "PUT"
        metadata["url"] = url
        metadata["json"] = json
        async with await self.request(metadata, "PUT", url, json=json) as response:
            return await response.json(content_type=None)

    async def delete(self, metadata: dict[str, str], url: str) -> None:
        """Make a DELETE request to the API endpoint."""
        metadata["method"] = "DELETE"
        metadata["url"] = url
        async with await self.request(metadata, "DELETE", url):
            return

    async def close(self) -> None:
        """Close the session."""
        await self._req_session.close()
