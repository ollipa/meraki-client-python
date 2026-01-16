"""Meraki dashboard API SDK."""

import os
import sys

from .api.administered import Administered
from .api.appliance import Appliance
from .api.batch import Batch
from .api.camera import Camera
from .api.campus_gateway import CampusGateway
from .api.cellular_gateway import CellularGateway
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
from .api.wireless_controller import WirelessController
from .config import (
    BE_GEO_ID,
    CERTIFICATE_PATH,
    DEFAULT_BASE_URL,
    MAXIMUM_RETRIES,
    MERAKI_PYTHON_SDK_CALLER,
    REQUESTS_PROXY,
    SINGLE_REQUEST_TIMEOUT,
    WAIT_ON_RATE_LIMIT,
)
from .rest_session import RestSession

if sys.version_info < (3, 11):  # noqa: UP036
    raise RuntimeError(
        "Python 3.11 or higher is required. "
        f"You are using Python {sys.version_info.major}.{sys.version_info.minor}."
    )

__version__ = ""
__api_version__ = ""


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
        maximum_retries: Retry up to this many times when encountering 429s or other server-side
          errors.
        be_geo_id: Optional partner identifier for API usage tracking; can also be set as an
          environment variable BE_GEO_ID.
        caller: Optional identifier for API usage tracking; can also be set as an environment
          variable MERAKI_PYTHON_SDK_CALLER.

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
        maximum_retries: int = MAXIMUM_RETRIES,
        be_geo_id: str | None = BE_GEO_ID,
        caller: str | None = MERAKI_PYTHON_SDK_CALLER,
    ) -> None:
        # Check that the API key is defined
        api_key = api_key or os.environ.get("MERAKI_DASHBOARD_API_KEY")
        if not api_key:
            raise ValueError(
                "API key needs to be defined. Give the API key as an argument "
                "or set the MERAKI_DASHBOARD_API_KEY environment variable."
            )

        # Pull the BE GEO ID from an environment variable if present
        be_geo_id = be_geo_id or os.environ.get("BE_GEO_ID")
        # Pull the caller from an environment variable if present
        caller = caller or os.environ.get("MERAKI_PYTHON_SDK_CALLER")

        # Creates the API session
        self._session = RestSession(
            api_key=api_key,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            certificate_path=certificate_path,
            requests_proxy=requests_proxy,
            wait_on_rate_limit=wait_on_rate_limit,
            maximum_retries=maximum_retries,
            be_geo_id=be_geo_id,
            caller=caller,
            version=__api_version__,
        )

        # API endpoints by section
        self.administered = Administered(self._session)
        self.organizations = Organizations(self._session)
        self.networks = Networks(self._session)
        self.devices = Devices(self._session)
        self.appliance = Appliance(self._session)
        self.camera = Camera(self._session)
        self.cellular_gateway = CellularGateway(self._session)
        self.insight = Insight(self._session)
        self.licensing = Licensing(self._session)
        self.sensor = Sensor(self._session)
        self.sm = Sm(self._session)
        self.switch = Switch(self._session)
        self.wireless = Wireless(self._session)
        self.spaces = Spaces(self._session)
        self.wireless_controller = WirelessController(self._session)
        self.campus_gateway = CampusGateway(self._session)

        # Batch definitions
        self.batch = Batch()
