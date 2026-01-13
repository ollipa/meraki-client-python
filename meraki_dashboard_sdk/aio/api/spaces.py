"""Spaces API endpoints."""

import urllib

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncSpaces:
    """Spaces class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_organization_spaces_integrate_status(self, organizationId: str):
        """Get the status of the Spaces integration in Meraki.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-spaces-integrate-status

        - organizationId (string): Organization ID

        """
        metadata = {
            "tags": ["spaces", "configure", "integrate", "status"],
            "operation": "get_organization_spaces_integrate_status",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/spaces/integrate/status"

        return self._session.get(metadata, resource)

    def remove_organization_spaces_integration(self, organizationId: str):
        """Remove the Spaces integration from Meraki.

        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        - organizationId (string): Organization ID

        """
        metadata = {
            "tags": ["spaces", "configure", "integration"],
            "operation": "remove_organization_spaces_integration",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/spaces/integration/remove"

        return self._session.post(metadata, resource)
