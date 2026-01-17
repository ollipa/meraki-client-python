"""Meraki dashboard API SDK."""

import os
import sys

from meraki_dashboard_sdk.api.administered import Administered
from meraki_dashboard_sdk.api.appliance import Appliance
from meraki_dashboard_sdk.api.batch import Batch
from meraki_dashboard_sdk.api.camera import Camera
from meraki_dashboard_sdk.api.campus_gateway import CampusGateway
from meraki_dashboard_sdk.api.cellular_gateway import CellularGateway
from meraki_dashboard_sdk.api.devices import Devices
from meraki_dashboard_sdk.api.insight import Insight
from meraki_dashboard_sdk.api.licensing import Licensing
from meraki_dashboard_sdk.api.nac import Nac
from meraki_dashboard_sdk.api.networks import Networks
from meraki_dashboard_sdk.api.organizations import Organizations
from meraki_dashboard_sdk.api.sensor import Sensor
from meraki_dashboard_sdk.api.sm import Sm
from meraki_dashboard_sdk.api.spaces import Spaces
from meraki_dashboard_sdk.api.switch import Switch
from meraki_dashboard_sdk.api.wireless import Wireless
from meraki_dashboard_sdk.api.wireless_controller import WirelessController
from meraki_dashboard_sdk.common import BaseURL
from meraki_dashboard_sdk.const import (
    MAXIMUM_RETRIES,
    SINGLE_REQUEST_TIMEOUT,
    WAIT_ON_RATE_LIMIT,
)
from meraki_dashboard_sdk.session import Session

if sys.version_info < (3, 11):  # noqa: UP036
    raise RuntimeError(
        "Python 3.11 or higher is required. "
        f"You are using Python {sys.version_info.major}.{sys.version_info.minor}."
    )


__all__ = [
    "BaseURL",
    "MerakiClient",
]
__version__ = "0.1.0"
__api_version__ = "v1.66.0"


class MerakiClient:
    """Client class for the Meraki dashboard API.

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
        caller: Optional identifier for API usage tracking; can also be set as an environment
          variable MERAKI_PYTHON_SDK_CALLER.

    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: BaseURL = BaseURL.DEFAULT,
        single_request_timeout: int = SINGLE_REQUEST_TIMEOUT,
        wait_on_rate_limit: bool = WAIT_ON_RATE_LIMIT,
        maximum_retries: int = MAXIMUM_RETRIES,
        certificate_path: str | None = None,
        requests_proxy: str | None = None,
        caller: str | None = None,
    ) -> None:
        # Check that the API key is defined
        api_key = api_key or os.environ.get("MERAKI_DASHBOARD_API_KEY")
        if not api_key:
            raise ValueError(
                "API key needs to be defined. Give the API key as an argument "
                "or set the MERAKI_DASHBOARD_API_KEY environment variable."
            )
        caller = caller or os.environ.get("MERAKI_PYTHON_SDK_CALLER")

        # Creates the API session
        self._session = Session(
            api_key=api_key,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            certificate_path=certificate_path,
            proxy=requests_proxy,
            wait_on_rate_limit=wait_on_rate_limit,
            maximum_retries=maximum_retries,
            caller=caller,
            version=__version__,
        )

        # API endpoints by section
        self.administered = Administered(self._session)
        self.appliance = Appliance(self._session)
        self.camera = Camera(self._session)
        self.campus_gateway = CampusGateway(self._session)
        self.cellular_gateway = CellularGateway(self._session)
        self.devices = Devices(self._session)
        self.insight = Insight(self._session)
        self.licensing = Licensing(self._session)
        self.nac = Nac(self._session)
        self.networks = Networks(self._session)
        self.organizations = Organizations(self._session)
        self.sensor = Sensor(self._session)
        self.sm = Sm(self._session)
        self.spaces = Spaces(self._session)
        self.switch = Switch(self._session)
        self.wireless = Wireless(self._session)
        self.wireless_controller = WirelessController(self._session)

        # Batch definitions
        self.batch = Batch()
