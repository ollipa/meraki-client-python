"""Session for the SDK."""

import io
import logging
import random
import time
import urllib.parse
from collections.abc import Callable, Iterator
from datetime import UTC, datetime
from typing import Any, Generic, Literal, Self, TypeVar

import requests
from requests.compat import basestring, urlencode
from requests.utils import to_key_val_list

from .common import (
    handle_3xx,
    sanitize_base_url,
    validate_base_url,
    validate_user_agent,
)
from .exceptions import MerakiConnectionError, MerakiHTTPError, raise_http_error

log = logging.getLogger(__name__)

T = TypeVar("T")


class PaginatedResponse(Iterator[T], Generic[T]):
    """Lazy paginated response that can be iterated or collected."""

    def __init__(self, page_fetcher: Callable[[], Iterator[T]]) -> None:
        self._page_fetcher = page_fetcher
        self._iterator: Iterator[T] | None = None
        self._exhausted = False

    def _ensure_iterator(self) -> Iterator[T]:
        if self._iterator is None:
            self._iterator = self._page_fetcher()
        return self._iterator

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> T:
        if self._exhausted:
            raise StopIteration
        try:
            return next(self._ensure_iterator())
        except StopIteration:
            self._exhausted = True
            raise

    def collect(self) -> list[T]:
        """Collect all remaining items into a list."""
        return list(self)


def encode_params(_, data: dict | list | str | bytes | io.BytesIO) -> str:  # noqa: ANN001
    """Encode parameters in a piece of data.

    Will successfully encode parameters when passed as a dict or a list of
    2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
    if parameters are supplied as a dict.

    MERAKI OVERRIDE:
    By default, when parameters are supplied as a dict, only the object keys
    are encoded.

    Ex. {"param": [{"key_1":"value_1"}, {"key_2":"value_2"}]} => ?param[]=key_1&param[]=key_2

    Now when parameters are supplied as a dict, dict keys will be appended to
    parameter names. This adds support for the "array of objects" query parameter type.

    Ex. {"param": [{"key_1":"value_1"}, {"key_2":"value_2"}]} => ?param[]key_1=value_1&param[]key_2=value_2
    """
    if isinstance(data, (str, bytes)) or hasattr(data, "read"):
        return data
    if hasattr(data, "__iter__"):
        result = []
        # Get each query parameter key value pair
        for k, vs in to_key_val_list(data):
            """
            Turn value into list/iterable if it is not already.
            Ex. {"param": "value"} => {"param": ["value"]}
            """
            if isinstance(vs, basestring) or not hasattr(vs, "__iter__"):
                vs = [vs]  # noqa: PLW2901
            for v in vs:
                # List params
                if v is not None and not isinstance(v, dict):
                    """
                    Add a query parameter key-value pair for each value to the list of results.
                    Ex. {"param": ["value_1", "value_2"]} => [(param, value_1), (param, value_2)]
                    """
                    result.append(
                        (
                            k.encode("utf-8") if isinstance(k, str) else k,
                            v.encode("utf-8") if isinstance(v, str) else v,
                        )
                    )
                # Dict params
                else:
                    """
                    Append each dict key to the parameter name.
                    Add a query parameter key-value pair for each value to the list of results.
                    {"param": [{"key_1": "value_1"}, {"key_2": "value_2"}]} =>
                      [(param + key_1, value1), (param + key_2, value2)]
                    """
                    for k_1, v_1 in v.items():
                        result.append(
                            (
                                ((k + k_1).encode("utf-8") if isinstance(k, str) else k_1),
                                ((v + v_1).encode("utf-8") if isinstance(v, str) else v_1),
                            )
                        )
        # Return URL encoded string
        return urlencode(result, doseq=True)
    return data


# Monkey patch the _encode_params from the requests library with the encode_params function above
requests.models.RequestEncodingMixin._encode_params = encode_params  # noqa: SLF001


def user_agent_extended(be_geo_id: str, caller: str) -> str:
    """Generate the extended portion of the User-Agent."""
    user_agent = {}

    if caller:
        user_agent["caller"] = caller
    elif be_geo_id:
        user_agent["caller"] = be_geo_id
    else:
        user_agent["caller"] = "unidentified"

    return f"Caller/({user_agent['caller']})"


class RestSession:
    """Main module interface."""

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        single_request_timeout: int,
        certificate_path: str,
        requests_proxy: str,
        wait_on_rate_limit: bool,
        maximum_retries: int,
        be_geo_id: str | None,
        caller: str | None,
        version: str,
    ) -> None:
        # Initialize attributes and properties
        self._version = version
        self._api_key = str(api_key)
        self._base_url = str(base_url)
        self._single_request_timeout = single_request_timeout
        self._certificate_path = certificate_path
        self._requests_proxy = requests_proxy
        self._wait_on_rate_limit = wait_on_rate_limit
        self._maximum_retries = maximum_retries
        self._be_geo_id = be_geo_id
        self._caller = caller

        # Initialize a new `requests` session
        self._req_session: requests.Session = requests.session()
        self._req_session.encoding = "utf-8"

        # Check base URL
        self._base_url = sanitize_base_url(self._base_url)

        # Update the headers for the session
        self._req_session.headers = {
            "Authorization": "Bearer " + self._api_key,
            "Content-Type": "application/json",
            "User-Agent": f"python-meraki/{self._version} "
            + validate_user_agent(self._be_geo_id, self._caller),
        }

    def _request(  # noqa: PLR0912, PLR0915
        self,
        *,
        operation: str,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        current_page: int | None = None,
    ) -> requests.Response:
        """Make an HTTP request to the API endpoint."""
        # Ensure proper base URL
        abs_url = validate_base_url(self._base_url, path)

        # Set the maximum number of retries
        retries = self._maximum_retries
        redirects = 0

        response: requests.Response
        while retries >= 0:
            if current_page is not None:
                log.debug(f"{operation} - {method} {abs_url} (page={current_page})")
            else:
                log.debug(f"{operation} - {method} {abs_url}")
            try:
                response = self._req_session.request(
                    method, abs_url, allow_redirects=False, params=params, json=json
                )
            except requests.exceptions.RequestException as e:
                if retries == 0:
                    raise MerakiConnectionError(cause=e) from e
                retries -= 1
                log.warning(f"{operation} - {e}, retrying in 1 second")
                time.sleep(1)
                continue

            reason = response.reason or "ERROR"
            status = response.status_code

            # Handle 3xx redirects automatically
            if 300 <= status < 400:
                if redirects >= 3:
                    raise MerakiHTTPError(
                        f"Maximum number of redirects reached: {redirects}",
                        cause=response,
                        response=response,
                    )
                abs_url, base_url = handle_3xx(self._base_url, response)
                self._base_url = base_url
                redirects += 1
                continue

            # Handle 2xx success
            if 200 <= status < 300:
                return response

            # Handle rate limiting
            if status == 429 and self._wait_on_rate_limit and retries > 0:
                wait = int(response.headers.get("Retry-After", random.randint(2, 5)))
                log.warning(f"{operation} - {status} {reason}, retrying in {wait} seconds")
                time.sleep(wait)
                retries -= 1
            else:
                raise raise_http_error(response)

            # Handle 4xx errors
            if 400 <= status < 500:
                raise raise_http_error(response)

            # Handle 5xx errors
            if status >= 500:
                if retries == 0:
                    raise raise_http_error(response)
                retries -= 1
                log.warning(f"{operation} - {status} {reason}, retrying in 1 second")
                time.sleep(1)
                continue
        raise RuntimeError(
            f"Maximum number of retries reached: {retries}. This should never happen."
        )

    def get(
        self, *, scope: str, operation_id: str, path: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Make a GET request to the API endpoint."""
        response = self._request(
            operation=f"{scope}.{operation_id}", method="GET", path=path, params=params
        )
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def get_pages(
        self,
        *,
        scope: str,
        operation_id: str,
        path: str,
        params: dict[str, Any] | None = None,
        total_pages: int | Literal["all"] = -1,
        direction: str = "next",
        event_log_end_time: str | None = None,
    ) -> PaginatedResponse[Any]:
        """Make a GET request to the API endpoint with pagination.

        Returns a PaginatedResponse that can be iterated for individual items
        or collected with .collect() to get all results as a list.
        """
        if isinstance(total_pages, str) and total_pages.lower() == "all":
            total_pages = -1
        elif isinstance(total_pages, str) and total_pages.isnumeric():
            total_pages = int(total_pages)
        elif isinstance(total_pages, int):
            pass
        else:
            raise ValueError(
                f"total_pages must be either an integer or 'all' as a string. Got {total_pages}",
            )

        def fetch_pages() -> Iterator[Any]:
            current_page = 1
            operation = f"{scope}.{operation_id}"
            next_url: str | None = path
            remaining_pages = total_pages

            while next_url and remaining_pages != 0:
                response = self._request(
                    operation=operation,
                    method="GET",
                    path=next_url,
                    params=params if current_page == 1 else None,
                    current_page=current_page,
                )
                results = response.json()
                links = response.links
                response.close()

                # Extract items from response
                if isinstance(results, list):
                    items = results
                elif isinstance(results, dict) and "items" in results:
                    items = results["items"]
                elif isinstance(results, dict):
                    # For event log endpoint
                    items = results["events"][::-1] if direction == "next" else results["events"]
                else:
                    items = []

                yield from items

                remaining_pages -= 1
                next_url = None

                # Determine next page URL
                if direction == "next" and "next" in links:
                    if operation_id == "getNetworkEvents":
                        starting_after = urllib.parse.unquote(
                            str(links["next"]["url"]).split("startingAfter=")[1]
                        )
                        delta = datetime.now(tz=UTC) - datetime.fromisoformat(starting_after)
                        # Break out of loop if startingAfter returned from next link is within 5 minutes of current time
                        if delta.total_seconds() < 300 or (
                            event_log_end_time and starting_after > event_log_end_time
                        ):
                            break
                    next_url = links["next"]["url"]
                    current_page += 1
                elif direction == "prev" and "prev" in links:
                    # Prevent getNetworkEvents from infinite loop as time goes backward (to epoch 0)
                    if operation_id == "getNetworkEvents":
                        ending_before = urllib.parse.unquote(
                            str(links["prev"]["url"]).split("endingBefore=")[1]
                        )
                        if ending_before < "2014-01-01":
                            break
                    next_url = links["prev"]["url"]
                    current_page += 1

        return PaginatedResponse(fetch_pages)

    def post(
        self, *, scope: str, operation_id: str, path: str, json: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Make a POST request to the API endpoint."""
        response = self._request(
            operation=f"{scope}.{operation_id}", method="POST", path=path, json=json
        )
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def put(
        self, *, scope: str, operation_id: str, path: str, json: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Make a PUT request to the API endpoint."""
        response = self._request(
            operation=f"{scope}.{operation_id}", method="PUT", path=path, json=json
        )
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def delete(
        self, *, scope: str, operation_id: str, path: str, json: dict[str, Any] | None = None
    ) -> None:
        """Make a DELETE request to the API endpoint."""
        response = self._request(
            operation=f"{scope}.{operation_id}", method="DELETE", path=path, json=json
        )
        if response:
            response.close()
