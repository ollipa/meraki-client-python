"""ActionBatchSm API endpoints."""

import urllib
from typing import Any


class ActionBatchSm:
    """ActionBatchSm class."""

    def __init__(self) -> None:
        pass

    def delete_network_sm_user_access_device(
        self, network_id: str, user_access_device_id: str
    ) -> dict[str, Any]:
        """Delete a User Access Device.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        Args:
            network_id: Network ID.
            user_access_device_id: User access device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "userAccessDevices"],
            "operation": "delete_network_sm_user_access_device",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        user_access_device_id = urllib.parse.quote(user_access_device_id, safe="")
        resource = f"/networks/{network_id}/sm/userAccessDevices/{user_access_device_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_sm_admins_role(
        self, organization_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            name: The name of the Limited Access Role.
            scope: The scope of the Limited Access Role.
            tags: The tags of the Limited Access Role.

        """
        kwargs.update(locals())

        if "scope" in kwargs:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert kwargs["scope"] in options, (
                f'''"scope" cannot be "{kwargs["scope"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "create_organization_sm_admins_role",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/sm/admins/roles"

        body_params = [
            "name",
            "scope",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_sm_admins_role(
        self, organization_id: str, role_id: str, **kwargs: Any
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
        kwargs.update(locals())

        if "scope" in kwargs:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert kwargs["scope"] in options, (
                f'''"scope" cannot be "{kwargs["scope"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "update_organization_sm_admins_role",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        role_id = urllib.parse.quote(role_id, safe="")
        resource = f"/organizations/{organization_id}/sm/admins/roles/{role_id}"

        body_params = [
            "name",
            "scope",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_sm_admins_role(
        self, organization_id: str, role_id: str
    ) -> dict[str, Any]:
        """Delete a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.

        """
        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "delete_organization_sm_admins_role",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        role_id = urllib.parse.quote(role_id, safe="")
        resource = f"/organizations/{organization_id}/sm/admins/roles/{role_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_sm_sentry_policies_assignments(
        self, organization_id: str, items: list
    ) -> dict[str, Any]:
        """Update an Organizations Sentry Policies using the provided list.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-sentry-policies-assignments

        Args:
            organization_id: Organization ID.
            items: Sentry Group Policies for the Organization keyed by Network Id.

        """
        kwargs = locals()

        metadata = {
            "tags": ["sm", "configure", "sentry", "policies", "assignments"],
            "operation": "update_organization_sm_sentry_policies_assignments",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/sm/sentry/policies/assignments"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action
