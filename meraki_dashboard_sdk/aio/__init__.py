"""Asynchronous Meraki dashboard API SDK."""

import logging
import os
from datetime import datetime, timezone
from types import TracebackType

from meraki_dashboard_sdk.api.batch import Batch
from meraki_dashboard_sdk.config import (
    ACTION_BATCH_RETRY_WAIT_TIME,
    AIO_MAXIMUM_CONCURRENT_REQUESTS,
    API_KEY_ENVIRONMENT_VARIABLE,
    BE_GEO_ID,
    CERTIFICATE_PATH,
    DEFAULT_BASE_URL,
    INHERIT_LOGGING_CONFIG,
    LOG_FILE_PREFIX,
    LOG_PATH,
    MAXIMUM_RETRIES,
    MERAKI_PYTHON_SDK_CALLER,
    NETWORK_DELETE_RETRY_WAIT_TIME,
    NGINX_429_RETRY_WAIT_TIME,
    OUTPUT_LOG,
    PRINT_TO_CONSOLE,
    REQUESTS_PROXY,
    RETRY_4XX_ERROR,
    RETRY_4XX_ERROR_WAIT_TIME,
    SIMULATE_API_CALLS,
    SINGLE_REQUEST_TIMEOUT,
    SUPPRESS_LOGGING,
    USE_ITERATOR_FOR_GET_PAGES,
    WAIT_ON_RATE_LIMIT,
)
from meraki_dashboard_sdk.exceptions import APIKeyError

from .api.administered import AsyncAdministered
from .api.appliance import AsyncAppliance
from .api.camera import AsyncCamera
from .api.campus_gateway import AsyncCampusGateway
from .api.cellular_gateway import AsyncCellularGateway
from .api.devices import AsyncDevices
from .api.insight import AsyncInsight
from .api.licensing import AsyncLicensing
from .api.networks import AsyncNetworks
from .api.organizations import AsyncOrganizations
from .api.sensor import AsyncSensor
from .api.sm import AsyncSm
from .api.spaces import AsyncSpaces
from .api.switch import AsyncSwitch
from .api.wireless import AsyncWireless
from .api.wireless_controller import AsyncWirelessController
from .rest_session import AsyncRestSession


class MerakiClient:
    """Creates a persistent Meraki dashboard API session.

    Args:
        api_key: API key generated in dashboard; can also be set as an environment variable
          MERAKI_DASHBOARD_API_KEY.
        base_url: Base URL preceding all endpoint resources.
        single_request_timeout: Maximum number of seconds for each API call.
        certificate_path: Path for TLS/SSL certificate verification if behind local proxy.
        requests_proxy: Proxy server and port, if needed, for HTTPS.
        wait_on_rate_limit: Retry if 429 rate limit error encountered?
        nginx_429_retry_wait_time: Nginx 429 retry wait time.
        action_batch_retry_wait_time: Action batch concurrency error retry wait time.
        network_delete_retry_wait_time: Network deletion concurrency error retry wait time.
        retry_4xx_error: Whether to retry if encountering other 4XX error (besides 429).
        retry_4xx_error_wait_time: Other 4XX error retry wait time.
        maximum_retries: Retry up to this many times when encountering 429s or other server-side
          errors.
        output_log: Whether to create an output log file.
        log_path: Path to output log; by default, working directory of script if not specified.
        log_file_prefix: Log file name appended with date and timestamp.
        print_console: Whether to print logging output to console.
        suppress_logging: Whether to disable all logging.
        inherit_logging_config: Inherits your own logger instance.
        simulate: Enable to simulate POST/PUT/DELETE calls to prevent changes.
        be_geo_id: Optional partner identifier for API usage tracking; can also be set as an
          environment variable BE_GEO_ID.
        caller: Optional identifier for API usage tracking; can also be set as an environment
          variable MERAKI_PYTHON_SDK_CALLER.
        use_iterator_for_get_pages: List methods will return an iterator with each object instead
          of a complete list with all items.
        maximum_concurrent_requests: Number of concurrent API requests for asynchronous class.

    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        single_request_timeout: int = SINGLE_REQUEST_TIMEOUT,
        certificate_path: str = CERTIFICATE_PATH,
        requests_proxy: str = REQUESTS_PROXY,
        wait_on_rate_limit: bool = WAIT_ON_RATE_LIMIT,
        nginx_429_retry_wait_time: int = NGINX_429_RETRY_WAIT_TIME,
        action_batch_retry_wait_time: int = ACTION_BATCH_RETRY_WAIT_TIME,
        network_delete_retry_wait_time: int = NETWORK_DELETE_RETRY_WAIT_TIME,
        retry_4xx_error: bool = RETRY_4XX_ERROR,
        retry_4xx_error_wait_time: int = RETRY_4XX_ERROR_WAIT_TIME,
        maximum_retries: int = MAXIMUM_RETRIES,
        output_log: bool = OUTPUT_LOG,
        log_path: str = LOG_PATH,
        log_file_prefix: str = LOG_FILE_PREFIX,
        print_console: bool = PRINT_TO_CONSOLE,
        suppress_logging: bool = SUPPRESS_LOGGING,
        simulate: bool = SIMULATE_API_CALLS,
        be_geo_id: str | None = BE_GEO_ID,
        caller: str | None = MERAKI_PYTHON_SDK_CALLER,
        use_iterator_for_get_pages: bool = USE_ITERATOR_FOR_GET_PAGES,
        inherit_logging_config: bool = INHERIT_LOGGING_CONFIG,
        maximum_concurrent_requests: int = AIO_MAXIMUM_CONCURRENT_REQUESTS,
    ) -> None:
        # Check API key
        api_key = api_key or os.environ.get(API_KEY_ENVIRONMENT_VARIABLE)
        if not api_key:
            raise APIKeyError

        # Pull the BE GEO ID from an environment variable if present
        be_geo_id = be_geo_id or os.environ.get("BE_GEO_ID")

        # Pull the caller from an environment variable if present
        caller = caller or os.environ.get("MERAKI_PYTHON_SDK_CALLER")

        # Configure logging
        if not suppress_logging:
            self._logger = logging.getLogger(__name__)

            if not inherit_logging_config:
                self._logger.setLevel(logging.DEBUG)

                formatter = logging.Formatter(
                    fmt="%(asctime)s %(name)12s: %(levelname)8s > %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                )
                handler_console = logging.StreamHandler()
                handler_console.setFormatter(formatter)

                if output_log:
                    if log_path and log_path[-1] != "/":
                        log_path += "/"
                    self._log_file = (
                        f"{log_path}{log_file_prefix}_log__"
                        f"{datetime.now(tz=timezone.utc):%Y-%m-%d_%H-%M-%S}.log"
                    )
                    handler_log = logging.FileHandler(filename=self._log_file)
                    handler_log.setFormatter(formatter)

                if output_log and not self._logger.hasHandlers():
                    self._logger.addHandler(handler_log)
                    if print_console:
                        handler_console.setLevel(logging.INFO)
                        self._logger.addHandler(handler_console)
                elif print_console and not self._logger.hasHandlers():
                    self._logger.addHandler(handler_console)
        else:
            self._logger = None

        # Creates the API session
        self._session = AsyncRestSession(
            logger=self._logger,
            api_key=api_key,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            certificate_path=certificate_path,
            requests_proxy=requests_proxy,
            wait_on_rate_limit=wait_on_rate_limit,
            nginx_429_retry_wait_time=nginx_429_retry_wait_time,
            action_batch_retry_wait_time=action_batch_retry_wait_time,
            network_delete_retry_wait_time=network_delete_retry_wait_time,
            retry_4xx_error=retry_4xx_error,
            retry_4xx_error_wait_time=retry_4xx_error_wait_time,
            maximum_retries=maximum_retries,
            simulate=simulate,
            be_geo_id=be_geo_id,
            caller=caller,
            use_iterator_for_get_pages=use_iterator_for_get_pages,
            maximum_concurrent_requests=maximum_concurrent_requests,
        )

        # API endpoints by section
        self.administered = AsyncAdministered(self._session)
        self.organizations = AsyncOrganizations(self._session)
        self.networks = AsyncNetworks(self._session)
        self.devices = AsyncDevices(self._session)
        self.appliance = AsyncAppliance(self._session)
        self.camera = AsyncCamera(self._session)
        self.cellular_gateway = AsyncCellularGateway(self._session)
        self.insight = AsyncInsight(self._session)
        self.licensing = AsyncLicensing(self._session)
        self.sensor = AsyncSensor(self._session)
        self.switch = AsyncSwitch(self._session)
        self.sm = AsyncSm(self._session)
        self.wireless = AsyncWireless(self._session)
        self.spaces = AsyncSpaces(self._session)
        self.wireless_controller = AsyncWirelessController(self._session)
        self.campus_gateway = AsyncCampusGateway(self._session)

        # Batch definitions
        self.batch = Batch()

    async def __aenter__(self) -> "MerakiClient":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self._session.close()
