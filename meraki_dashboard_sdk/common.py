"""Common functions for the SDK."""

import re
import sys
import urllib.parse

from .exceptions import SessionInputError


def validate_user_agent(be_geo_id: str, caller: str) -> str:
    """Generate extended portion of the User Agent.

    Validate that it follows the expected format
    """
    user_agent = {}

    allowed_format_in_regex = (
        r"^[A-Za-z0-9]+(?:/[0-9A-Za-z]+(?:\.[0-9A-Za-z]+)*(-[a-z]+)?)? [A-Za-z-0-9]+$"
    )

    if caller and re.match(allowed_format_in_regex, caller):
        user_agent["caller"] = caller
    elif be_geo_id and re.match(allowed_format_in_regex, be_geo_id):
        user_agent["caller"] = be_geo_id
    elif caller:
        message = (
            "Please follow the user agent format prescribed in User Agents guide, available at:"
        )
        doc_link = "https://developer.cisco.com/meraki/api-v1/user-agents-overview/"
        raise SessionInputError("MERAKI_PTYHON_SDK_CALLER", caller, message, doc_link)
    elif be_geo_id:
        message = (
            "Use of be_geo_id is deprecated. "
            "Please use the argument MERAKI_PTYHON_SDK_CALLER instead."
        )
        doc_link = "https://developer.cisco.com/meraki/api-v1/user-agents-overview/"
        raise SessionInputError("BE_GEO_ID", caller, message, doc_link)
    else:
        user_agent["caller"] = "unidentified"

    return f"Caller/({user_agent['caller']})"


def sanitize_base_url(base_url: str) -> str:
    """Sanitize base URL by rejecting v0 and stripping trailing slashes."""
    if "v0" in base_url:
        sys.exit(
            f"This library does not support dashboard API v0 ({base_url} was configured as the base"
            f" URL).  API v0 has been end of life since 2020 August 5."
        )
    elif base_url[-1] == "/":
        base_url = base_url[:-1]
    return base_url


def iterator_for_get_pages_bool(self):  # noqa: ANN001, ANN201
    """Return the value of the use_iterator_for_get_pages attribute."""
    return self._use_iterator_for_get_pages


def use_iterator_for_get_pages_setter(self, value):  # noqa: ANN001, ANN201
    """Set the value of the use_iterator_for_get_pages attribute."""
    if value:
        self.get_pages = self._get_pages_iterator
    else:
        self.get_pages = self._get_pages_legacy

    self._use_iterator_for_get_pages = value


def validate_base_url(base_url: str, url: str) -> str:
    """Validate base URL by checking if it is in the allowed domains."""
    allowed_domains = [
        "meraki.com",
        "meraki.ca",
        "meraki.cn",
        "meraki.in",
        "gov-meraki.com",
    ]
    parsed_url = urllib.parse.urlparse(url)
    return url if any(domain in parsed_url.netloc for domain in allowed_domains) else base_url + url
