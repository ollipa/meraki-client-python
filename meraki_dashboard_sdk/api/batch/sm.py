"""ActionBatchSm API endpoints."""

import urllib
from typing import Any


class ActionBatchSm:
    """ActionBatchSm class."""

    def __init__(self) -> None:
        pass

    def delete_network_sm_user_access_device(
        self, networkId: str, userAccessDeviceId: str
    ) -> dict[str, Any]:
        """Delete a User Access Device.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        Args:
            networkId: Network ID.
            userAccessDeviceId: User access device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "userAccessDevices"],
            "operation": "delete_network_sm_user_access_device",
        }
        resource = f"/networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_sm_admins_role(
        self, organizationId: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-admins-role

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/sm/admins/roles"

        body_params = [
            "name",
            "scope",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_sm_admins_role(
        self, organizationId: str, roleId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-admins-role

        Args:
            organizationId: Organization ID.
            roleId: Role ID.
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
        resource = f"/organizations/{organizationId}/sm/admins/roles/{roleId}"

        body_params = [
            "name",
            "scope",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_sm_admins_role(
        self, organizationId: str, roleId: str
    ) -> dict[str, Any]:
        """Delete a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-admins-role

        Args:
            organizationId: Organization ID.
            roleId: Role ID.

        """
        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "delete_organization_sm_admins_role",
        }
        resource = f"/organizations/{organizationId}/sm/admins/roles/{roleId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_sm_sentry_policies_assignments(
        self, organizationId: str, items: list
    ) -> dict[str, Any]:
        """Update an Organizations Sentry Policies using the provided list.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-sentry-policies-assignments

        Args:
            organizationId: Organization ID.
            items: Sentry Group Policies for the Organization keyed by Network Id.

        """
        kwargs = locals()

        metadata = {
            "tags": ["sm", "configure", "sentry", "policies", "assignments"],
            "operation": "update_organization_sm_sentry_policies_assignments",
        }
        resource = f"/organizations/{organizationId}/sm/sentry/policies/assignments"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action
