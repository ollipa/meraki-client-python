"""Response handler for the SDK."""

import requests


def handle_3xx(base_url: str, response: requests.Response) -> str:
    """Handle 3xx redirects."""
    abs_url = response.headers["Location"]
    substring = "meraki.com/api/v"
    if substring not in abs_url:
        substring = "meraki.cn/api/v"
    base_url = abs_url[: abs_url.find(substring) + len(substring) + 1]
    return abs_url, base_url
