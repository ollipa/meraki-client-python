"""ActionBatchSm API endpoints."""

import urllib.parse
from typing import Any


class ActionBatchSm:
    """ActionBatchSm class."""

    def __init__(self) -> None:
        pass

    def delete_network_sm_user_access_device(
        self, *, network_id: str, user_access_device_id: str
    ) -> dict[str, Any]:
        """Delete a User Access Device.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        Args:
            network_id: Network ID.
            user_access_device_id: User access device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        user_access_device_id = urllib.parse.quote(str(user_access_device_id), safe="")
        path = f"/networks/{network_id}/sm/userAccessDevices/{user_access_device_id}"

        return {
            "path": path,
            "operation": "destroy",
        }

    def create_organization_sm_admins_role(
        self, *, organization_id: str, name: str, scope: str | None = None, tags: list | None = None
    ) -> dict[str, Any]:
        """Create a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            name: The name of the Limited Access Role.
            scope: The scope of the Limited Access Role.
            tags: The tags of the Limited Access Role.

        """
        if scope is not None:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert scope in options, (
                f'"scope" cannot be "{scope}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/sm/admins/roles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scope is not None:
            payload["scope"] = scope
        if tags is not None:
            payload["tags"] = tags

        return {
            "path": path,
            "operation": "create",
            "body": payload,
        }

    def update_organization_sm_admins_role(
        self,
        *,
        organization_id: str,
        role_id: str,
        name: str | None = None,
        scope: str | None = None,
        tags: list | None = None,
    ) -> dict[str, Any]:
        """Update a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.
            name: The name of the Limited Access Role.
            scope: The scope of the Limited Access Role.
            tags: The tags of the Limited Access Role.

        """
        if scope is not None:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert scope in options, (
                f'"scope" cannot be "{scope}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        role_id = urllib.parse.quote(str(role_id), safe="")
        path = f"/organizations/{organization_id}/sm/admins/roles/{role_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scope is not None:
            payload["scope"] = scope
        if tags is not None:
            payload["tags"] = tags

        return {
            "path": path,
            "operation": "update",
            "body": payload,
        }

    def delete_organization_sm_admins_role(
        self, *, organization_id: str, role_id: str
    ) -> dict[str, Any]:
        """Delete a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        role_id = urllib.parse.quote(str(role_id), safe="")
        path = f"/organizations/{organization_id}/sm/admins/roles/{role_id}"

        return {
            "path": path,
            "operation": "destroy",
        }

    def update_organization_sm_sentry_policies_assignments(
        self, *, organization_id: str, items: list
    ) -> dict[str, Any]:
        """Update an Organizations Sentry Policies using the provided list.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-sentry-policies-assignments

        Args:
            organization_id: Organization ID.
            items: Sentry Group Policies for the Organization keyed by Network Id.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/sm/sentry/policies/assignments"

        payload = {}
        if items is not None:
            payload["items"] = items

        return {
            "path": path,
            "operation": "update",
            "body": payload,
        }
