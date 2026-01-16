"""Spaces API endpoints."""

from __future__ import annotations

import urllib
from collections.abc import Generator
from typing import Any, Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from meraki_dashboard_sdk.rest_session import RestSession


class Spaces:
    """Spaces class."""

    def __init__(self, session: RestSession) -> None:
        self._session = session

    def get_organization_spaces_integrate_status(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Get the status of the Spaces integration in Meraki.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-spaces-integrate-status

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/spaces/integrate/status"

        return self._session.get(
            scope="spaces", operation_id="getOrganizationSpacesIntegrateStatus", path=path
        )

    def remove_organization_spaces_integration(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Remove the Spaces integration from Meraki.

        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/spaces/integration/remove"

        return self._session.post(
            scope="spaces", operation_id="removeOrganizationSpacesIntegration", path=path
        )
