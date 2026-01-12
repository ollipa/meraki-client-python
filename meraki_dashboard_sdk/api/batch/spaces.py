"""ActionBatchSpaces API endpoints."""


class ActionBatchSpaces:
    """ActionBatchSpaces class."""

    def __init__(self) -> None:
        pass

    def removeOrganizationSpacesIntegration(self, organizationId: str):
        """
        **Remove the Spaces integration from Meraki**
        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["spaces", "configure", "integration"],
            "operation": "removeOrganizationSpacesIntegration",
        }
        resource = f"/organizations/{organizationId}/spaces/integration/remove"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action
