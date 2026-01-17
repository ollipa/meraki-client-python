"""Administered API endpoints."""

from __future__ import annotations

import urllib
from collections.abc import Generator
from typing import Any, Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from meraki_dashboard_sdk.aio.session import AsyncSession


class AsyncAdministered:
    """Administered class."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def get_administered_identities_me(self) -> dict[str, Any] | None:
        """Returns the identity of the current user.

        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me

        """
        path = f"/administered/identities/me"

        return self._session.get(
            scope="administered", operation_id="getAdministeredIdentitiesMe", path=path
        )

    def get_administered_identities_me_api_keys(self) -> dict[str, Any] | None:
        """List the non-sensitive metadata associated with the API keys that belong to the user.

        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me-api-keys

        """
        path = f"/administered/identities/me/api/keys"

        return self._session.get(
            scope="administered", operation_id="getAdministeredIdentitiesMeApiKeys", path=path
        )

    def generate_administered_identities_me_api_keys(self) -> dict[str, Any] | None:
        """Generates an API key for an identity.

        https://developer.cisco.com/meraki/api-v1/#!generate-administered-identities-me-api-keys

        """
        path = f"/administered/identities/me/api/keys/generate"

        return self._session.post(
            scope="administered", operation_id="generateAdministeredIdentitiesMeApiKeys", path=path
        )

    def revoke_administered_identities_me_api_keys(self, *, suffix: str) -> dict[str, Any] | None:
        """Revokes an identity's API key, using the last four characters of the key.

        https://developer.cisco.com/meraki/api-v1/#!revoke-administered-identities-me-api-keys

        Args:
            suffix: Suffix.

        """
        suffix = urllib.parse.quote(str(suffix), safe="")
        path = f"/administered/identities/me/api/keys/{suffix}/revoke"

        return self._session.post(
            scope="administered", operation_id="revokeAdministeredIdentitiesMeApiKeys", path=path
        )
