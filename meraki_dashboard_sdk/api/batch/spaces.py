"""ActionBatchSpaces API endpoints."""

import urllib
from typing import Any, Literal


class ActionBatchSpaces:
    """ActionBatchSpaces class."""

    def __init__(self) -> None:
        pass

    def remove_organization_spaces_integration(self, *, organization_id: str) -> dict[str, Any]:
        """Remove the Spaces integration from Meraki.

        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/spaces/integration/remove"

        action = {
            "path": path,
            "operation": "create",
        }
        return action  # noqa: RET504
