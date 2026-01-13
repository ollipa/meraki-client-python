"""ActionBatchSm API endpoints."""


class ActionBatchSm:
    """ActionBatchSm class."""

    def __init__(self) -> None:
        pass

    def delete_network_sm_user_access_device(self, networkId: str, userAccessDeviceId: str):
        """
        **Delete a User Access Device.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        - networkId (string): Network ID
        - userAccessDeviceId (string): User access device ID
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

    def create_organization_sm_admins_role(self, organizationId: str, name: str, **kwargs):
        """
        **Create a Limited Access Role.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-admins-role

        - organizationId (string): Organization ID
        - name (string): The name of the Limited Access Role
        - scope (string): The scope of the Limited Access Role
        - tags (array): The tags of the Limited Access Role
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

    def update_organization_sm_admins_role(self, organizationId: str, roleId: str, **kwargs):
        """
        **Update a Limited Access Role.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-admins-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
        - name (string): The name of the Limited Access Role
        - scope (string): The scope of the Limited Access Role
        - tags (array): The tags of the Limited Access Role
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

    def delete_organization_sm_admins_role(self, organizationId: str, roleId: str):
        """
        **Delete a Limited Access Role.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-admins-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
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

    def update_organization_sm_sentry_policies_assignments(self, organizationId: str, items: list):
        """
        **Update an Organizations Sentry Policies using the provided list.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-sentry-policies-assignments

        - organizationId (string): Organization ID
        - items (array): Sentry Group Policies for the Organization keyed by Network Id
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
