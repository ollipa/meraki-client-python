"""Administered API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.rest_session import RestSession


class Administered:
    """Administered class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
        self._session = session

    def get_administered_identities_me(self) -> dict[str, Any] | None:
        """Returns the identity of the current user.

        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me

        """
        metadata = {
            "tags": ["administered", "monitor", "identities", "me"],
            "operation": "get_administered_identities_me",
        }
        resource = f"/administered/identities/me"

        return self._session.get(metadata, resource)

    def get_administered_identities_me_api_keys(self) -> dict[str, Any] | None:
        """List the non-sensitive metadata associated with the API keys that belong to the user.

        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me-api-keys

        """
        metadata = {
            "tags": ["administered", "configure", "identities", "me", "api", "keys"],
            "operation": "get_administered_identities_me_api_keys",
        }
        resource = f"/administered/identities/me/api/keys"

        return self._session.get(metadata, resource)

    def generate_administered_identities_me_api_keys(self) -> dict[str, Any] | None:
        """Generates an API key for an identity.

        https://developer.cisco.com/meraki/api-v1/#!generate-administered-identities-me-api-keys

        """
        metadata = {
            "tags": ["administered", "configure", "identities", "me", "api", "keys"],
            "operation": "generate_administered_identities_me_api_keys",
        }
        resource = f"/administered/identities/me/api/keys/generate"

        return self._session.post(metadata, resource)

    def revoke_administered_identities_me_api_keys(self, suffix: str) -> dict[str, Any] | None:
        """Revokes an identity's API key, using the last four characters of the key.

        https://developer.cisco.com/meraki/api-v1/#!revoke-administered-identities-me-api-keys

        Args:
            suffix: Suffix.

        """
        metadata = {
            "tags": ["administered", "configure", "identities", "me", "api", "keys"],
            "operation": "revoke_administered_identities_me_api_keys",
        }
        suffix = urllib.parse.quote(str(suffix), safe="")
        resource = f"/administered/identities/me/api/keys/{suffix}/revoke"

        return self._session.post(metadata, resource)
