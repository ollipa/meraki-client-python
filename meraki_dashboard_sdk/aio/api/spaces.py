"""Spaces API endpoints."""

from __future__ import annotations

import urllib.parse
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from meraki_dashboard_sdk.aio.session import Session


class Spaces:
    """Spaces class."""

    def __init__(self, session: Session) -> None:
        self._session = session

    async def get_organization_spaces_integrate_status(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Get the status of the Spaces integration in Meraki.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-spaces-integrate-status

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/spaces/integrate/status"

        return await self._session.get(
            scope="spaces", operation_id="getOrganizationSpacesIntegrateStatus", path=path
        )

    async def remove_organization_spaces_integration(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Remove the Spaces integration from Meraki.

        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/spaces/integration/remove"

        return await self._session.post(
            scope="spaces", operation_id="removeOrganizationSpacesIntegration", path=path
        )
