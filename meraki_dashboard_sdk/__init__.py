"""Meraki dashboard API SDK."""

import logging
import os
import sys
from datetime import datetime, timezone

from .api.administered import Administered
from .api.appliance import Appliance
from .api.batch import Batch
from .api.camera import Camera
from .api.campusGateway import CampusGateway
from .api.cellularGateway import CellularGateway
from .api.devices import Devices
from .api.insight import Insight
from .api.licensing import Licensing
from .api.networks import Networks
from .api.organizations import Organizations
from .api.sensor import Sensor
from .api.sm import Sm
from .api.spaces import Spaces
from .api.switch import Switch
from .api.wireless import Wireless
from .api.wirelessController import WirelessController
from .config import (
    ACTION_BATCH_RETRY_WAIT_TIME,
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
from .exceptions import APIKeyError
from .rest_session import RestSession

if sys.version_info < (3, 10):  # noqa: UP036
    raise RuntimeError(
        "Python 3.10 or higher is required. "
        f"You are using Python {sys.version_info.major}.{sys.version_info.minor}."
    )

__version__ = "0.1.0"
__api_version__ = "v1.66.0"


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
        self._session = RestSession(
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
        )

        # API endpoints by section
        self.administered = Administered(self._session)
        self.organizations = Organizations(self._session)
        self.networks = Networks(self._session)
        self.devices = Devices(self._session)
        self.appliance = Appliance(self._session)
        self.camera = Camera(self._session)
        self.cellularGateway = CellularGateway(self._session)
        self.insight = Insight(self._session)
        self.licensing = Licensing(self._session)
        self.sensor = Sensor(self._session)
        self.sm = Sm(self._session)
        self.switch = Switch(self._session)
        self.wireless = Wireless(self._session)
        self.spaces = Spaces(self._session)
        self.wirelessController = WirelessController(self._session)
        self.campusGateway = CampusGateway(self._session)

        # Batch definitions
        self.batch = Batch()
