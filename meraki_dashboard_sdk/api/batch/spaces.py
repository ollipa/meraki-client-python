"""ActionBatchSpaces API endpoints."""

import urllib
from typing import Any


class ActionBatchSpaces:
    """ActionBatchSpaces class."""

    def __init__(self) -> None:
        pass

    def remove_organization_spaces_integration(self, organizationId: str) -> dict[str, Any]:
        """Remove the Spaces integration from Meraki.

        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        Args:
            organizationId: Organization ID.

        """
        metadata = {
            "tags": ["spaces", "configure", "integration"],
            "operation": "remove_organization_spaces_integration",
        }
        resource = f"/organizations/{organizationId}/spaces/integration/remove"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action
