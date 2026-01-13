"""Organizations API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncOrganizations:
    """Organizations class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_organizations(self) -> Generator[Any, None, None]:
        """List the organizations that the user has privileges on.

        https://developer.cisco.com/meraki/api-v1/#!get-organizations

        Args:
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 9000. Default
              is 9000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {"tags": ["organizations", "configure"], "operation": "get_organizations"}
        resource = f"/organizations"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization(self, name: str, **kwargs: Any) -> dict[str, Any] | None:
        """Create a new organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization

        Args:
            name: The name of the organization.
            management: Information about the organization's management system.

        """
        kwargs.update(locals())

        metadata = {"tags": ["organizations", "configure"], "operation": "create_organization"}
        resource = f"/organizations"

        body_params = [
            "name",
            "management",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization(self, organization_id: str) -> dict[str, Any] | None:
        """Return an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization

        Args:
            organization_id: Organization ID.

        """
        metadata = {"tags": ["organizations", "configure"], "operation": "get_organization"}
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}"

        return self._session.get(metadata, resource)

    def update_organization(self, organization_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Update an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization

        Args:
            organization_id: Organization ID.
            name: The name of the organization.
            management: Information about the organization's management system.
            api: API-specific settings.

        """
        kwargs.update(locals())

        metadata = {"tags": ["organizations", "configure"], "operation": "update_organization"}
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}"

        body_params = [
            "name",
            "management",
            "api",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization(self, organization_id: str) -> None:
        """Delete an organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization

        Args:
            organization_id: Organization ID.

        """
        metadata = {"tags": ["organizations", "configure"], "operation": "delete_organization"}
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}"

        return self._session.delete(metadata, resource)

    def create_organization_action_batch(
        self, organization_id: str, actions: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create an action batch.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-action-batch

        Args:
            organization_id: Organization ID.
            actions: A set of changes to make as part of this action (<a
              href='https://developer.cisco.com/meraki/api/#/rest/guides/action-
              batches/'>more details</a>).
            confirmed: Set to true for immediate execution. Set to false if the action should be
              previewed before executing. This property cannot be unset once it is true.
              Defaults to false.
            synchronous: Set to true to force the batch to run synchronous. There can be at most 20
              actions in synchronous batch. Defaults to false.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "create_organization_action_batch",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/actionBatches"

        body_params = [
            "confirmed",
            "synchronous",
            "actions",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_action_batches(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return the list of action batches in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches

        Args:
            organization_id: Organization ID.
            status: Filter batches by status. Valid types are pending, completed, and failed.

        """
        kwargs.update(locals())

        if "status" in kwargs:
            options = ["completed", "failed", "pending"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "get_organization_action_batches",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/actionBatches"

        query_params = [
            "status",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_action_batch(
        self, organization_id: str, action_batch_id: str
    ) -> dict[str, Any] | None:
        """Return an action batch.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch

        Args:
            organization_id: Organization ID.
            action_batch_id: Action batch ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "get_organization_action_batch",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        action_batch_id = urllib.parse.quote(str(action_batch_id), safe="")
        resource = f"/organizations/{organization_id}/actionBatches/{action_batch_id}"

        return self._session.get(metadata, resource)

    def delete_organization_action_batch(self, organization_id: str, action_batch_id: str) -> None:
        """Delete an action batch.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-action-batch

        Args:
            organization_id: Organization ID.
            action_batch_id: Action batch ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "delete_organization_action_batch",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        action_batch_id = urllib.parse.quote(str(action_batch_id), safe="")
        resource = f"/organizations/{organization_id}/actionBatches/{action_batch_id}"

        return self._session.delete(metadata, resource)

    def update_organization_action_batch(
        self, organization_id: str, action_batch_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update an action batch.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-action-batch

        Args:
            organization_id: Organization ID.
            action_batch_id: Action batch ID.
            confirmed: A boolean representing whether or not the batch has been confirmed. This
              property cannot be unset once it is true.
            synchronous: Set to true to force the batch to run synchronous. There can be at most 20
              actions in synchronous batch.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "update_organization_action_batch",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        action_batch_id = urllib.parse.quote(str(action_batch_id), safe="")
        resource = f"/organizations/{organization_id}/actionBatches/{action_batch_id}"

        body_params = [
            "confirmed",
            "synchronous",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_adaptive_policy_acls(self, organization_id: str) -> dict[str, Any] | None:
        """List adaptive policy ACLs in a organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acls

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "get_organization_adaptive_policy_acls",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/acls"

        return self._session.get(metadata, resource)

    def create_organization_adaptive_policy_acl(
        self, organization_id: str, name: str, rules: list, ipVersion: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Creates new adaptive policy ACL.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-acl

        Args:
            organization_id: Organization ID.
            name: Name of the adaptive policy ACL.
            rules: An ordered array of the adaptive policy ACL rules.
            ipVersion: IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'.
            description: Description of the adaptive policy ACL.

        """
        kwargs.update(locals())

        if "ipVersion" in kwargs:
            options = ["any", "ipv4", "ipv6"]
            assert kwargs["ipVersion"] in options, (
                f'''"ipVersion" cannot be "{kwargs["ipVersion"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "create_organization_adaptive_policy_acl",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/acls"

        body_params = [
            "name",
            "description",
            "rules",
            "ipVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_adaptive_policy_acl(
        self, organization_id: str, acl_id: str
    ) -> dict[str, Any] | None:
        """Returns the adaptive policy ACL information.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acl

        Args:
            organization_id: Organization ID.
            acl_id: Acl ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "get_organization_adaptive_policy_acl",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        acl_id = urllib.parse.quote(str(acl_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}"

        return self._session.get(metadata, resource)

    def update_organization_adaptive_policy_acl(
        self, organization_id: str, acl_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Updates an adaptive policy ACL.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-acl

        Args:
            organization_id: Organization ID.
            acl_id: Acl ID.
            name: Name of the adaptive policy ACL.
            description: Description of the adaptive policy ACL.
            rules: An ordered array of the adaptive policy ACL rules. An empty array will clear the
              rules.
            ipVersion: IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'.

        """
        kwargs.update(locals())

        if "ipVersion" in kwargs:
            options = ["any", "ipv4", "ipv6"]
            assert kwargs["ipVersion"] in options, (
                f'''"ipVersion" cannot be "{kwargs["ipVersion"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "update_organization_adaptive_policy_acl",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        acl_id = urllib.parse.quote(str(acl_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}"

        body_params = [
            "name",
            "description",
            "rules",
            "ipVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_adaptive_policy_acl(self, organization_id: str, acl_id: str) -> None:
        """Deletes the specified adaptive policy ACL.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-acl

        Args:
            organization_id: Organization ID.
            acl_id: Acl ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "delete_organization_adaptive_policy_acl",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        acl_id = urllib.parse.quote(str(acl_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}"

        return self._session.delete(metadata, resource)

    def get_organization_adaptive_policy_groups(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """List adaptive policy groups in a organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-groups

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "get_organization_adaptive_policy_groups",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/groups"

        return self._session.get(metadata, resource)

    def create_organization_adaptive_policy_group(
        self, organization_id: str, name: str, sgt: int, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Creates a new adaptive policy group.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-group

        Args:
            organization_id: Organization ID.
            name: Name of the group.
            sgt: SGT value of the group.
            description: Description of the group (default: "").
            policyObjects: The policy objects that belong to this group; traffic from addresses
              specified by these policy objects will be tagged with this group's SGT
              value if no other tagging scheme is being used (each requires one unique
              attribute) (default: []).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "create_organization_adaptive_policy_group",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/groups"

        body_params = [
            "name",
            "sgt",
            "description",
            "policyObjects",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_adaptive_policy_group(
        self, organization_id: str, id: str
    ) -> dict[str, Any] | None:
        """Returns an adaptive policy group.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-group

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "get_organization_adaptive_policy_group",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/groups/{id}"

        return self._session.get(metadata, resource)

    def update_organization_adaptive_policy_group(
        self, organization_id: str, id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Updates an adaptive policy group.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-group

        Args:
            organization_id: Organization ID.
            id: ID.
            name: Name of the group.
            sgt: SGT value of the group.
            description: Description of the group.
            policyObjects: The policy objects that belong to this group; traffic from addresses
              specified by these policy objects will be tagged with this group's SGT
              value if no other tagging scheme is being used (each requires one unique
              attribute).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "update_organization_adaptive_policy_group",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/groups/{id}"

        body_params = [
            "name",
            "sgt",
            "description",
            "policyObjects",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_adaptive_policy_group(self, organization_id: str, id: str) -> None:
        """Deletes the specified adaptive policy group and any associated policies and references.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-group

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "delete_organization_adaptive_policy_group",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/groups/{id}"

        return self._session.delete(metadata, resource)

    def get_organization_adaptive_policy_overview(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """Returns adaptive policy aggregate statistics for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-overview

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "monitor", "adaptivePolicy", "overview"],
            "operation": "get_organization_adaptive_policy_overview",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/overview"

        return self._session.get(metadata, resource)

    def get_organization_adaptive_policy_policies(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """List adaptive policies in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policies

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "get_organization_adaptive_policy_policies",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/policies"

        return self._session.get(metadata, resource)

    def create_organization_adaptive_policy_policy(
        self, organization_id: str, sourceGroup: dict, destinationGroup: dict, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Add an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-policy

        Args:
            organization_id: Organization ID.
            sourceGroup: The source adaptive policy group (requires one unique attribute).
            destinationGroup: The destination adaptive policy group (requires one unique attribute).
            acls: An ordered array of adaptive policy ACLs (each requires one unique attribute) that
              apply to this policy (default: []).
            lastEntryRule: The rule to apply if there is no matching ACL (default: "default").

        """
        kwargs.update(locals())

        if "lastEntryRule" in kwargs:
            options = ["allow", "default", "deny"]
            assert kwargs["lastEntryRule"] in options, (
                f'''"lastEntryRule" cannot be "{kwargs["lastEntryRule"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "create_organization_adaptive_policy_policy",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/policies"

        body_params = [
            "sourceGroup",
            "destinationGroup",
            "acls",
            "lastEntryRule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_adaptive_policy_policy(
        self, organization_id: str, id: str
    ) -> dict[str, Any] | None:
        """Return an adaptive policy.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policy

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "get_organization_adaptive_policy_policy",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/policies/{id}"

        return self._session.get(metadata, resource)

    def update_organization_adaptive_policy_policy(
        self, organization_id: str, id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-policy

        Args:
            organization_id: Organization ID.
            id: ID.
            sourceGroup: The source adaptive policy group (requires one unique attribute).
            destinationGroup: The destination adaptive policy group (requires one unique attribute).
            acls: An ordered array of adaptive policy ACLs (each requires one unique attribute) that
              apply to this policy.
            lastEntryRule: The rule to apply if there is no matching ACL.

        """
        kwargs.update(locals())

        if "lastEntryRule" in kwargs:
            options = ["allow", "default", "deny"]
            assert kwargs["lastEntryRule"] in options, (
                f'''"lastEntryRule" cannot be "{kwargs["lastEntryRule"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "update_organization_adaptive_policy_policy",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/policies/{id}"

        body_params = [
            "sourceGroup",
            "destinationGroup",
            "acls",
            "lastEntryRule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_adaptive_policy_policy(self, organization_id: str, id: str) -> None:
        """Delete an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-policy

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "delete_organization_adaptive_policy_policy",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/policies/{id}"

        return self._session.delete(metadata, resource)

    def get_organization_adaptive_policy_settings(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """Returns global adaptive policy settings in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-settings

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "settings"],
            "operation": "get_organization_adaptive_policy_settings",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/settings"

        return self._session.get(metadata, resource)

    def update_organization_adaptive_policy_settings(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update global adaptive policy settings.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-settings

        Args:
            organization_id: Organization ID.
            enabledNetworks: List of network IDs with adaptive policy enabled.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "settings"],
            "operation": "update_organization_adaptive_policy_settings",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/settings"

        body_params = [
            "enabledNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_admins(self, organization_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """List the dashboard administrators in this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-admins

        Args:
            organization_id: Organization ID.
            networkIds: Optional parameter to filter the result set by the included set of network
              IDs.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "admins"],
            "operation": "get_organization_admins",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/admins"

        query_params = [
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def create_organization_admin(
        self, organization_id: str, email: str, name: str, orgAccess: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a new dashboard administrator.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-admin

        Args:
            organization_id: Organization ID.
            email: The email of the dashboard administrator. This attribute can not be updated.
            name: The name of the dashboard administrator.
            orgAccess: The privilege of the dashboard administrator on the organization. Can be one
              of 'full', 'read-only', 'enterprise' or 'none'.
            tags: The list of tags that the dashboard administrator has privileges on.
            networks: The list of networks that the dashboard administrator has privileges on.
            authenticationMethod: No longer used as of Cisco SecureX end-of-life. Can be one of
              'Email'. The default is Email authentication.

        """
        kwargs.update(locals())

        if "orgAccess" in kwargs:
            options = ["enterprise", "full", "none", "read-only"]
            assert kwargs["orgAccess"] in options, (
                f'''"orgAccess" cannot be "{kwargs["orgAccess"]}", & must be set to one of: {options}'''
            )
        if "authenticationMethod" in kwargs:
            options = ["Email"]
            assert kwargs["authenticationMethod"] in options, (
                f'''"authenticationMethod" cannot be "{kwargs["authenticationMethod"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "admins"],
            "operation": "create_organization_admin",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/admins"

        body_params = [
            "email",
            "name",
            "orgAccess",
            "tags",
            "networks",
            "authenticationMethod",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_organization_admin(
        self, organization_id: str, admin_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update an administrator.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-admin

        Args:
            organization_id: Organization ID.
            admin_id: Admin ID.
            name: The name of the dashboard administrator.
            orgAccess: The privilege of the dashboard administrator on the organization. Can be one
              of 'full', 'read-only', 'enterprise' or 'none'.
            tags: The list of tags that the dashboard administrator has privileges on.
            networks: The list of networks that the dashboard administrator has privileges on.

        """
        kwargs.update(locals())

        if "orgAccess" in kwargs:
            options = ["enterprise", "full", "none", "read-only"]
            assert kwargs["orgAccess"] in options, (
                f'''"orgAccess" cannot be "{kwargs["orgAccess"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "admins"],
            "operation": "update_organization_admin",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        admin_id = urllib.parse.quote(str(admin_id), safe="")
        resource = f"/organizations/{organization_id}/admins/{admin_id}"

        body_params = [
            "name",
            "orgAccess",
            "tags",
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_admin(self, organization_id: str, admin_id: str) -> None:
        """Revoke all access for a dashboard administrator within this organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-admin

        Args:
            organization_id: Organization ID.
            admin_id: Admin ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "admins"],
            "operation": "delete_organization_admin",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        admin_id = urllib.parse.quote(str(admin_id), safe="")
        resource = f"/organizations/{organization_id}/admins/{admin_id}"

        return self._session.delete(metadata, resource)

    def get_organization_alerts_profiles(self, organization_id: str) -> dict[str, Any] | None:
        """List all organization-wide alert configurations.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-alerts-profiles

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "get_organization_alerts_profiles",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/alerts/profiles"

        return self._session.get(metadata, resource)

    def create_organization_alerts_profile(
        self,
        organization_id: str,
        type: str,
        alertCondition: dict,
        recipients: dict,
        networkTags: list,
        **kwargs: Any,
    ) -> dict[str, Any] | None:
        """Create an organization-wide alert configuration.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-alerts-profile

        Args:
            organization_id: Organization ID.
            type: The alert type.
            alertCondition: The conditions that determine if the alert triggers.
            recipients: List of recipients that will recieve the alert.
            networkTags: Networks with these tags will be monitored for the alert.
            description: User supplied description of the alert.

        """
        kwargs.update(locals())

        if "type" in kwargs:
            options = [
                "appOutage",
                "voipJitter",
                "voipMos",
                "voipPacketLoss",
                "wanLatency",
                "wanPacketLoss",
                "wanStatus",
                "wanUtilization",
            ]
            assert kwargs["type"] in options, (
                f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "create_organization_alerts_profile",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/alerts/profiles"

        body_params = [
            "type",
            "alertCondition",
            "recipients",
            "networkTags",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_organization_alerts_profile(
        self, organization_id: str, alert_config_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update an organization-wide alert config.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-alerts-profile

        Args:
            organization_id: Organization ID.
            alert_config_id: Alert config ID.
            enabled: Is the alert config enabled.
            type: The alert type.
            alertCondition: The conditions that determine if the alert triggers.
            recipients: List of recipients that will recieve the alert.
            networkTags: Networks with these tags will be monitored for the alert.
            description: User supplied description of the alert.

        """
        kwargs.update(locals())

        if "type" in kwargs:
            options = [
                "appOutage",
                "voipJitter",
                "voipMos",
                "voipPacketLoss",
                "wanLatency",
                "wanPacketLoss",
                "wanStatus",
                "wanUtilization",
            ]
            assert kwargs["type"] in options, (
                f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "update_organization_alerts_profile",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        alert_config_id = urllib.parse.quote(str(alert_config_id), safe="")
        resource = f"/organizations/{organization_id}/alerts/profiles/{alert_config_id}"

        body_params = [
            "enabled",
            "type",
            "alertCondition",
            "recipients",
            "networkTags",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_alerts_profile(
        self, organization_id: str, alert_config_id: str
    ) -> None:
        """Removes an organization-wide alert config.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-alerts-profile

        Args:
            organization_id: Organization ID.
            alert_config_id: Alert config ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "delete_organization_alerts_profile",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        alert_config_id = urllib.parse.quote(str(alert_config_id), safe="")
        resource = f"/organizations/{organization_id}/alerts/profiles/{alert_config_id}"

        return self._session.delete(metadata, resource)

    def get_organization_api_requests(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the API requests made by an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 31 days.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            adminId: Filter the results by the ID of the admin who made the API requests.
            path: Filter the results by the path of the API requests.
            method: Filter the results by the method of the API requests (must be 'GET', 'PUT',
              'POST' or 'DELETE').
            responseCode: Filter the results by the response code of the API requests.
            sourceIp: Filter the results by the IP address of the originating API request.
            userAgent: Filter the results by the user agent string of the API request.
            version: Filter the results by the API version of the API request.
            operationIds: Filter the results by one or more operation IDs for the API request.

        """
        kwargs.update(locals())

        if "method" in kwargs:
            options = ["DELETE", "GET", "POST", "PUT"]
            assert kwargs["method"] in options, (
                f'''"method" cannot be "{kwargs["method"]}", & must be set to one of: {options}'''
            )
        if "version" in kwargs:
            options = [0, 1]
            assert kwargs["version"] in options, (
                f'''"version" cannot be "{kwargs["version"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests"],
            "operation": "get_organization_api_requests",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/apiRequests"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "adminId",
            "path",
            "method",
            "responseCode",
            "sourceIp",
            "userAgent",
            "version",
            "operationIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "operationIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_api_requests_overview(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return an aggregated overview of API requests data.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 31 days.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests", "overview"],
            "operation": "get_organization_api_requests_overview",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/apiRequests/overview"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_api_requests_overview_response_codes_by_interval(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Tracks organizations' API requests by response code across a given time period.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview-response-codes-by-interval

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 31 days. If
              interval is provided, the timespan will be autocalculated.
            interval: The time interval in seconds for returned data. The valid intervals are: 120,
              3600, 14400, 21600. The default is 21600. Interval is calculated if time
              params are provided.
            version: Filter by API version of the endpoint. Allowable values are: [0, 1].
            operationIds: Filter by operation ID of the endpoint.
            sourceIps: Filter by source IP that made the API request.
            adminIds: Filter by admin ID of user that made the API request.
            userAgent: Filter by user agent string for API request. This will filter by a complete
              or partial match.

        """
        kwargs.update(locals())

        if "version" in kwargs:
            options = [0, 1]
            assert kwargs["version"] in options, (
                f'''"version" cannot be "{kwargs["version"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": [
                "organizations",
                "monitor",
                "apiRequests",
                "overview",
                "responseCodes",
                "byInterval",
            ],
            "operation": "get_organization_api_requests_overview_response_codes_by_interval",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/apiRequests/overview/responseCodes/byInterval"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "interval",
            "version",
            "operationIds",
            "sourceIps",
            "adminIds",
            "userAgent",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "operationIds",
            "sourceIps",
            "adminIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_organization_assurance_alerts(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return all health alerts for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 4 - 300. Default
              is 30.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sortOrder: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'ascending'.
            networkId: Optional parameter to filter alerts by network ids.
            severity: Optional parameter to filter by severity type.
            types: Optional parameter to filter by alert type.
            tsStart: Optional parameter to filter by starting timestamp.
            tsEnd: Optional parameter to filter by end timestamp.
            category: Optional parameter to filter by category.
            sortBy: Optional parameter to set column to sort by.
            serials: Optional parameter to filter by primary device serial.
            deviceTypes: Optional parameter to filter by device types.
            deviceTags: Optional parameter to filter by device tags.
            active: Optional parameter to filter by active alerts defaults to true.
            dismissed: Optional parameter to filter by dismissed alerts defaults to false.
            resolved: Optional parameter to filter by resolved alerts defaults to false.
            suppressAlertsForOfflineNodes: When set to true the api will only return connectivity
              alerts for a given device if that device is in an offline state. This only
              applies to devices. This is ignored when resolved is true. Example:  If a
              Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert
              will be returned. Defaults to false.

        """
        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )
        if "sortBy" in kwargs:
            options = ["category", "dismissedAt", "resolvedAt", "severity", "startedAt"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts"],
            "operation": "get_organization_assurance_alerts",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "sortBy",
            "serials",
            "deviceTypes",
            "deviceTags",
            "active",
            "dismissed",
            "resolved",
            "suppressAlertsForOfflineNodes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
            "deviceTags",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def dismiss_organization_assurance_alerts(
        self, organization_id: str, alertIds: list
    ) -> dict[str, Any] | None:
        """Dismiss health alerts.

        https://developer.cisco.com/meraki/api-v1/#!dismiss-organization-assurance-alerts

        Args:
            organization_id: Organization ID.
            alertIds: Array of alert IDs to dismiss.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "monitor", "alerts"],
            "operation": "dismiss_organization_assurance_alerts",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/dismiss"

        body_params = [
            "alertIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_assurance_alerts_overview(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return overview of active health alerts for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview

        Args:
            organization_id: Organization ID.
            networkId: Optional parameter to filter alerts overview by network ids.
            severity: Optional parameter to filter alerts overview by severity type.
            types: Optional parameter to filter by alert type.
            tsStart: Optional parameter to filter by starting timestamp.
            tsEnd: Optional parameter to filter by end timestamp.
            category: Optional parameter to filter by category.
            serials: Optional parameter to filter by primary device serial.
            deviceTypes: Optional parameter to filter by device types.
            deviceTags: Optional parameter to filter by device tags.
            active: Optional parameter to filter by active alerts defaults to true.
            dismissed: Optional parameter to filter by dismissed alerts defaults to false.
            resolved: Optional parameter to filter by resolved alerts defaults to false.
            suppressAlertsForOfflineNodes: When set to true the api will only return connectivity
              alerts for a given device if that device is in an offline state. This only
              applies to devices. This is ignored when resolved is true. Example:  If a
              Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert
              will be returned. Defaults to false.

        """
        kwargs.update(locals())

        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "overview"],
            "operation": "get_organization_assurance_alerts_overview",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/overview"

        query_params = [
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "serials",
            "deviceTypes",
            "deviceTags",
            "active",
            "dismissed",
            "resolved",
            "suppressAlertsForOfflineNodes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
            "deviceTags",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_organization_assurance_alerts_overview_by_network(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return a Summary of Alerts grouped by network and severity.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-by-network

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sortOrder: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'ascending'.
            networkId: Optional parameter to filter alerts overview by network id.
            severity: Optional parameter to filter alerts overview by severity type.
            types: Optional parameter to filter by alert type.
            tsStart: Optional parameter to filter by starting timestamp.
            tsEnd: Optional parameter to filter by end timestamp.
            category: Optional parameter to filter by category.
            serials: Optional parameter to filter by primary device serial.
            deviceTypes: Optional parameter to filter by device types.
            deviceTags: Optional parameter to filter by device tags.
            active: Optional parameter to filter by active alerts defaults to true.
            dismissed: Optional parameter to filter by dismissed alerts defaults to false.
            resolved: Optional parameter to filter by resolved alerts defaults to false.
            suppressAlertsForOfflineNodes: When set to true the api will only return connectivity
              alerts for a given device if that device is in an offline state. This only
              applies to devices. This is ignored when resolved is true. Example:  If a
              Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert
              will be returned. Defaults to false.

        """
        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "overview", "byNetwork"],
            "operation": "get_organization_assurance_alerts_overview_by_network",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/overview/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "serials",
            "deviceTypes",
            "deviceTags",
            "active",
            "dismissed",
            "resolved",
            "suppressAlertsForOfflineNodes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
            "deviceTags",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_assurance_alerts_overview_by_type(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return a Summary of Alerts grouped by type and severity.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-by-type

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sortOrder: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'ascending'.
            networkId: Optional parameter to filter alerts overview by network ids.
            severity: Optional parameter to filter alerts overview by severity type.
            types: Optional parameter to filter by alert type.
            tsStart: Optional parameter to filter by starting timestamp.
            tsEnd: Optional parameter to filter by end timestamp.
            category: Optional parameter to filter by category.
            sortBy: Optional parameter to set column to sort by.
            serials: Optional parameter to filter by primary device serial.
            deviceTypes: Optional parameter to filter by device types.
            deviceTags: Optional parameter to filter by device tags.
            active: Optional parameter to filter by active alerts defaults to true.
            dismissed: Optional parameter to filter by dismissed alerts defaults to false.
            resolved: Optional parameter to filter by resolved alerts defaults to false.
            suppressAlertsForOfflineNodes: When set to true the api will only return connectivity
              alerts for a given device if that device is in an offline state. This only
              applies to devices. This is ignored when resolved is true. Example:  If a
              Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert
              will be returned. Defaults to false.

        """
        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )
        if "sortBy" in kwargs:
            options = ["count", "lastAlertedAt", "networkCount", "severity", "startedAt"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "overview", "byType"],
            "operation": "get_organization_assurance_alerts_overview_by_type",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/overview/byType"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "sortBy",
            "serials",
            "deviceTypes",
            "deviceTags",
            "active",
            "dismissed",
            "resolved",
            "suppressAlertsForOfflineNodes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
            "deviceTags",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_assurance_alerts_overview_historical(
        self, organization_id: str, segmentDuration: int, tsStart: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Returns historical health alert overviews.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-historical

        Args:
            organization_id: Organization ID.
            segmentDuration: Amount of time in seconds for each segment in the returned dataset.
            tsStart: Parameter to define starting timestamp of historical totals.
            networkId: Optional parameter to filter alerts overview by network ids.
            severity: Optional parameter to filter alerts overview by severity type.
            types: Optional parameter to filter by alert type.
            tsEnd: Optional parameter to filter by end timestamp defaults to the current time.
            category: Optional parameter to filter by category.
            serials: Optional parameter to filter by primary device serial.
            deviceTypes: Optional parameter to filter by device types.

        """
        kwargs.update(locals())

        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "overview", "historical"],
            "operation": "get_organization_assurance_alerts_overview_historical",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/overview/historical"

        query_params = [
            "segmentDuration",
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "serials",
            "deviceTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def restore_organization_assurance_alerts(
        self, organization_id: str, alertIds: list
    ) -> dict[str, Any] | None:
        """Restore health alerts from dismissed.

        https://developer.cisco.com/meraki/api-v1/#!restore-organization-assurance-alerts

        Args:
            organization_id: Organization ID.
            alertIds: Array of alert IDs to restore.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "monitor", "alerts"],
            "operation": "restore_organization_assurance_alerts",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/restore"

        body_params = [
            "alertIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_assurance_alerts_taxonomy_categories(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """Return a list of Category Types.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-taxonomy-categories

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "monitor", "alerts", "taxonomy", "categories"],
            "operation": "get_organization_assurance_alerts_taxonomy_categories",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/taxonomy/categories"

        return self._session.get(metadata, resource)

    def get_organization_assurance_alerts_taxonomy_types(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """Return a list of alert types.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-taxonomy-types

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "monitor", "alerts", "taxonomy", "types"],
            "operation": "get_organization_assurance_alerts_taxonomy_types",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/taxonomy/types"

        return self._session.get(metadata, resource)

    def get_organization_assurance_alert(
        self, organization_id: str, id: str
    ) -> dict[str, Any] | None:
        """Return a singular Health Alert by its id.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alert

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "monitor", "alerts"],
            "operation": "get_organization_assurance_alert",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/assurance/alerts/{id}"

        return self._session.get(metadata, resource)

    def get_organization_branding_policies(self, organization_id: str) -> dict[str, Any] | None:
        """List the branding policies of an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "get_organization_branding_policies",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies"

        return self._session.get(metadata, resource)

    def create_organization_branding_policy(
        self, organization_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Add a new branding policy to an organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

        Args:
            organization_id: Organization ID.
            name: Name of the Dashboard branding policy.
            enabled: Boolean indicating whether this policy is enabled.
            adminSettings: Settings for describing which kinds of admins this policy applies to.
            helpSettings:       Settings for describing the modifications to various Help page
              features. Each property in this object accepts one of       'default or
              inherit' (do not modify functionality), 'hide' (remove the section from
              Dashboard), or 'show' (always show       the section on Dashboard). Some
              properties in this object also accept custom HTML used to replace the
              section on       Dashboard; see the documentation for each property to see
              the allowed values.  Each property defaults to 'default or inherit' when
              not provided.
            customLogo: Properties describing the custom logo attached to the branding policy.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "create_organization_branding_policy",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies"

        body_params = [
            "name",
            "enabled",
            "adminSettings",
            "helpSettings",
            "customLogo",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_branding_policies_priorities(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """Return the branding policy IDs of an organization in priority order.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies-priorities

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies", "priorities"],
            "operation": "get_organization_branding_policies_priorities",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies/priorities"

        return self._session.get(metadata, resource)

    def update_organization_branding_policies_priorities(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the priority ordering of an organization's branding policies.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

        Args:
            organization_id: Organization ID.
            brandingPolicyIds:       An ordered list of branding policy IDs that determines the
              priority order of how to apply the policies .

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies", "priorities"],
            "operation": "update_organization_branding_policies_priorities",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies/priorities"

        body_params = [
            "brandingPolicyIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_branding_policy(
        self, organization_id: str, branding_policy_id: str
    ) -> dict[str, Any] | None:
        """Return a branding policy.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policy

        Args:
            organization_id: Organization ID.
            branding_policy_id: Branding policy ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "get_organization_branding_policy",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        branding_policy_id = urllib.parse.quote(str(branding_policy_id), safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies/{branding_policy_id}"

        return self._session.get(metadata, resource)

    def update_organization_branding_policy(
        self, organization_id: str, branding_policy_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a branding policy.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

        Args:
            organization_id: Organization ID.
            branding_policy_id: Branding policy ID.
            name: Name of the Dashboard branding policy.
            enabled: Boolean indicating whether this policy is enabled.
            adminSettings: Settings for describing which kinds of admins this policy applies to.
            helpSettings:       Settings for describing the modifications to various Help page
              features. Each property in this object accepts one of       'default or
              inherit' (do not modify functionality), 'hide' (remove the section from
              Dashboard), or 'show' (always show       the section on Dashboard). Some
              properties in this object also accept custom HTML used to replace the
              section on       Dashboard; see the documentation for each property to see
              the allowed values. .
            customLogo: Properties describing the custom logo attached to the branding policy.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "update_organization_branding_policy",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        branding_policy_id = urllib.parse.quote(str(branding_policy_id), safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies/{branding_policy_id}"

        body_params = [
            "name",
            "enabled",
            "adminSettings",
            "helpSettings",
            "customLogo",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_branding_policy(
        self, organization_id: str, branding_policy_id: str
    ) -> None:
        """Delete a branding policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

        Args:
            organization_id: Organization ID.
            branding_policy_id: Branding policy ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "delete_organization_branding_policy",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        branding_policy_id = urllib.parse.quote(str(branding_policy_id), safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies/{branding_policy_id}"

        return self._session.delete(metadata, resource)

    def claim_into_organization(self, organization_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Claim a list of devices, licenses, and/or orders into an organization inventory.

        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization

        Args:
            organization_id: Organization ID.
            orders: The numbers of the orders that should be claimed.
            serials: The serials of the devices that should be claimed.
            licenses: The licenses that should be claimed.

        """
        kwargs.update(locals())

        metadata = {"tags": ["organizations", "configure"], "operation": "claim_into_organization"}
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/claim"

        body_params = [
            "orders",
            "serials",
            "licenses",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_clients_bandwidth_usage_history(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-bandwidth-usage-history

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "clients", "bandwidthUsageHistory"],
            "operation": "get_organization_clients_bandwidth_usage_history",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/clients/bandwidthUsageHistory"

        query_params = [
            "networkTag",
            "deviceTag",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_clients_overview(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return summary information around client data usage (in kb) across the given organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-overview

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "clients", "overview"],
            "operation": "get_organization_clients_overview",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/clients/overview"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_clients_search(
        self, organization_id: str, mac: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the client details in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-search

        Args:
            organization_id: Organization ID.
            mac: The MAC address of the client. Required.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 5. Default is
              5.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "clients", "search"],
            "operation": "get_organization_clients_search",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/clients/search"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "mac",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def clone_organization(self, organization_id: str, name: str) -> dict[str, Any] | None:
        """Create a new organization by cloning the addressed organization.

        https://developer.cisco.com/meraki/api-v1/#!clone-organization

        Args:
            organization_id: Organization ID.
            name: The name of the new organization.

        """
        kwargs = locals()

        metadata = {"tags": ["organizations", "configure"], "operation": "clone_organization"}
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/clone"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_config_templates(self, organization_id: str) -> dict[str, Any] | None:
        """List the configuration templates for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "get_organization_config_templates",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/configTemplates"

        return self._session.get(metadata, resource)

    def create_organization_config_template(
        self, organization_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a new configuration template.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

        Args:
            organization_id: Organization ID.
            name: The name of the configuration template.
            timeZone: The timezone of the configuration template. For a list of allowed timezones,
              please see the 'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article</a>. Not applicable if copying from existing network or template.
            copyFromNetworkId: The ID of the network or config template to copy configuration from.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "create_organization_config_template",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/configTemplates"

        body_params = [
            "name",
            "timeZone",
            "copyFromNetworkId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_config_template(
        self, organization_id: str, config_template_id: str
    ) -> dict[str, Any] | None:
        """Return a single configuration template.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "get_organization_config_template",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        resource = f"/organizations/{organization_id}/configTemplates/{config_template_id}"

        return self._session.get(metadata, resource)

    def update_organization_config_template(
        self, organization_id: str, config_template_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a configuration template.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.
            name: The name of the configuration template.
            timeZone: The timezone of the configuration template. For a list of allowed timezones,
              please see the 'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article.</a>.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "update_organization_config_template",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        resource = f"/organizations/{organization_id}/configTemplates/{config_template_id}"

        body_params = [
            "name",
            "timeZone",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_config_template(
        self, organization_id: str, config_template_id: str
    ) -> None:
        """Remove a configuration template.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-config-template

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "delete_organization_config_template",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        resource = f"/organizations/{organization_id}/configTemplates/{config_template_id}"

        return self._session.delete(metadata, resource)

    def get_organization_configuration_changes(
        self, organization_id: str, total_pages=1, direction="prev", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """View the Change Log for your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-configuration-changes

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" or "prev" (default) page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 365 days. The default is 365 days.
            perPage: The number of entries per page returned. Acceptable range is 3 - 5000. Default
              is 5000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkId: Filters on the given network.
            adminId: Filters on the given Admin.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "configurationChanges"],
            "operation": "get_organization_configuration_changes",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/configurationChanges"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkId",
            "adminId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_devices(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the devices in an organization that have been assigned to a network.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 5000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            configurationUpdatedAfter: Filter results by whether or not the device's configuration
              has been updated after the given timestamp.
            networkIds: Optional parameter to filter devices by network.
            productTypes: Optional parameter to filter devices by product type. Valid types are
              wireless, appliance, switch, systemsManager, camera, cellularGateway,
              sensor, wirelessController, campusGateway, and secureConnect.
            tags: Optional parameter to filter devices by tags.
            tagsFilterType: Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate
              whether to return networks which contain ANY or ALL of the included tags.
              If no type is included, 'withAnyTags' will be selected.
            name: Optional parameter to filter devices by name. All returned devices will have a
              name that contains the search term or is an exact match.
            mac: Optional parameter to filter devices by MAC address. All returned devices will have
              a MAC address that contains the search term or is an exact match.
            serial: Optional parameter to filter devices by serial number. All returned devices will
              have a serial number that contains the search term or is an exact match.
            model: Optional parameter to filter devices by model. All returned devices will have a
              model that contains the search term or is an exact match.
            macs: Optional parameter to filter devices by one or more MAC addresses. All returned
              devices will have a MAC address that is an exact match.
            serials: Optional parameter to filter devices by one or more serial numbers. All
              returned devices will have a serial number that is an exact match.
            sensorMetrics: Optional parameter to filter devices by the metrics that they provide.
              Only applies to sensor devices.
            sensorAlertProfileIds: Optional parameter to filter devices by the alert profiles that
              are bound to them. Only applies to sensor devices.
            models: Optional parameter to filter devices by one or more models. All returned devices
              will have a model that is an exact match.

        """
        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices"],
            "operation": "get_organization_devices",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "configurationUpdatedAfter",
            "networkIds",
            "productTypes",
            "tags",
            "tagsFilterType",
            "name",
            "mac",
            "serial",
            "model",
            "macs",
            "serials",
            "sensorMetrics",
            "sensorAlertProfileIds",
            "models",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "tags",
            "macs",
            "serials",
            "sensorMetrics",
            "sensorAlertProfileIds",
            "models",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_devices_availabilities(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the availability information for devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter device availabilities by network ID. This
              filter uses multiple exact matches.
            productTypes: Optional parameter to filter device availabilities by device product
              types. This filter uses multiple exact matches. Valid types are wireless,
              appliance, switch, camera, cellularGateway, sensor, wirelessController,
              and campusGateway.
            serials: Optional parameter to filter device availabilities by device serial numbers.
              This filter uses multiple exact matches.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below). This filter uses multiple exact matches.
            tagsFilterType: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.
            statuses: Optional parameter to filter device availabilities by device status. This
              filter uses multiple exact matches.

        """
        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "availabilities"],
            "operation": "get_organization_devices_availabilities",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/availabilities"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "serials",
            "tags",
            "tagsFilterType",
            "statuses",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "serials",
            "tags",
            "statuses",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_devices_availabilities_change_history(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the availability history information for devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities-change-history

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            serials: Optional parameter to filter device availabilities history by device serial
              numbers.
            productTypes: Optional parameter to filter device availabilities history by device
              product types.
            networkIds: Optional parameter to filter device availabilities history by network IDs.
            statuses: Optional parameter to filter device availabilities history by device statuses.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "availabilities", "changeHistory"],
            "operation": "get_organization_devices_availabilities_change_history",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/availabilities/changeHistory"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "serials",
            "productTypes",
            "networkIds",
            "statuses",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "productTypes",
            "networkIds",
            "statuses",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_devices_controller_migration(
        self, organization_id: str, serials: list, target: str
    ) -> dict[str, Any] | None:
        """Migrate devices to another controller or management mode.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-controller-migration

        Args:
            organization_id: Organization ID.
            serials: A list of Meraki Serials to migrate.
            target: The controller or management mode to which the devices will be migrated.

        """
        kwargs = locals()

        if "target" in kwargs:
            options = ["wirelessController"]
            assert kwargs["target"] in options, (
                f'''"target" cannot be "{kwargs["target"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "controller", "migrations"],
            "operation": "create_organization_devices_controller_migration",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/controller/migrations"

        body_params = [
            "serials",
            "target",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_devices_controller_migrations(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Retrieve device migration statuses in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-controller-migrations

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            serials: A list of Meraki Serials for which to retrieve migrations.
            networkIds: Filter device migrations by network IDs.
            target: Filter device migrations by target destination.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        if "target" in kwargs:
            options = ["wirelessController"]
            assert kwargs["target"] in options, (
                f'''"target" cannot be "{kwargs["target"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "controller", "migrations"],
            "operation": "get_organization_devices_controller_migrations",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/controller/migrations"

        query_params = [
            "serials",
            "networkIds",
            "target",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def bulk_update_organization_devices_details(
        self, organization_id: str, serials: list, details: list
    ) -> dict[str, Any] | None:
        """Updating device details (currently only used for Catalyst devices).

        https://developer.cisco.com/meraki/api-v1/#!bulk-update-organization-devices-details

        Args:
            organization_id: Organization ID.
            serials: A list of serials of devices to update.
            details: An array of details.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "details", "bulkUpdate"],
            "operation": "bulk_update_organization_devices_details",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/details/bulkUpdate"

        body_params = [
            "serials",
            "details",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_devices_overview_by_model(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Lists the count for each device model.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-overview-by-model

        Args:
            organization_id: Organization ID.
            models: Optional parameter to filter devices by one or more models. All returned devices
              will have a model that is an exact match.
            networkIds: Optional parameter to filter devices by networkId.
            productTypes: Optional parameter to filter device by device product types. This filter
              uses multiple exact matches.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "overview", "byModel"],
            "operation": "get_organization_devices_overview_by_model",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/overview/byModel"

        query_params = [
            "models",
            "networkIds",
            "productTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "models",
            "networkIds",
            "productTypes",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_organization_devices_packet_capture_captures(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List Packet Captures.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-packet-capture-captures

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            captureIds: Return the packet captures of the specified capture ids.
            networkIds: Return the packet captures of the specified network(s).
            serials: Return the packet captures of the specified device(s).
            process: Return the packet captures of the specified process.
            captureStatus: Return the packet captures of the specified capture status.
            name: Return the packet captures matching the specified name.
            clientMac: Return the packet captures matching the specified client macs.
            notes: Return the packet captures matching the specified notes.
            deviceName: Return the packet captures matching the specified device name.
            adminName: Return the packet captures matching the admin name.
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 365 days. The default is 365 days.
            perPage: The number of entries per page returned. Acceptable range is 3 - 100. Default
              is 10.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sortOrder: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'descending'.

        """
        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "get_organization_devices_packet_capture_captures",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/captures"

        query_params = [
            "captureIds",
            "networkIds",
            "serials",
            "process",
            "captureStatus",
            "name",
            "clientMac",
            "notes",
            "deviceName",
            "adminName",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "captureIds",
            "networkIds",
            "serials",
            "process",
            "captureStatus",
            "name",
            "clientMac",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_devices_packet_capture_capture(
        self, organization_id: str, serials: list, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Perform a packet capture on a device and store in Meraki Cloud.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-capture

        Args:
            organization_id: Organization ID.
            serials: The serial(s) of the device(s).
            name: Name of packet capture file.
            outputType: Output type of packet capture file. Possible values: text, pcap, cloudshark,
              or upload_to_cloud.
            destination: Destination of packet capture file. Possible values: [upload_to_cloud].
            ports: Ports of packet capture file, comma-separated.
            notes: Reason for taking the packet capture.
            duration: Duration in seconds of packet capture.
            filterExpression: Filter expression for packet capture.
            interface: Interface of the device.
            advanced: Advanced filters for IOSXE devices (supported for Campus Gateway devices
              only).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "create_organization_devices_packet_capture_capture",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/captures"

        body_params = [
            "serials",
            "name",
            "outputType",
            "destination",
            "ports",
            "notes",
            "duration",
            "filterExpression",
            "interface",
            "advanced",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def bulk_organization_devices_packet_capture_captures_create(
        self, organization_id: str, devices: list, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Perform a packet capture on multiple devices and store in Meraki Cloud.

        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-create

        Args:
            organization_id: Organization ID.
            devices: Device details (maximum of 20 devices allowed).
            name: Name of packet capture file.
            notes: Reason for capture.
            duration: Duration of the capture in seconds.
            filterExpression: Filter expression for the capture.
            advanced: Advanced capture options (optional).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "bulk_organization_devices_packet_capture_captures_create",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/captures/bulkCreate"

        body_params = [
            "devices",
            "notes",
            "duration",
            "filterExpression",
            "name",
            "advanced",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def bulk_organization_devices_packet_capture_captures_delete(
        self, organization_id: str, captureIds: list
    ) -> dict[str, Any] | None:
        """BulkDelete packet captures from cloud.

        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-delete

        Args:
            organization_id: Organization ID.
            captureIds: Delete the packet captures of the specified capture ids.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "bulk_organization_devices_packet_capture_captures_delete",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/captures/bulkDelete"

        body_params = [
            "captureIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def delete_organization_devices_packet_capture_capture(
        self, organization_id: str, capture_id: str
    ) -> None:
        """Delete a single packet capture from cloud using captureId.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-capture

        Args:
            organization_id: Organization ID.
            capture_id: Capture ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "delete_organization_devices_packet_capture_capture",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        capture_id = urllib.parse.quote(str(capture_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/captures/{capture_id}"

        return self._session.delete(metadata, resource)

    def generate_organization_devices_packet_capture_capture_download_url(
        self, organization_id: str, capture_id: str
    ) -> dict[str, Any] | None:
        """Get presigned download URL for given packet capture id.

        https://developer.cisco.com/meraki/api-v1/#!generate-organization-devices-packet-capture-capture-download-url

        Args:
            organization_id: Organization ID.
            capture_id: Capture ID.

        """
        metadata = {
            "tags": [
                "organizations",
                "configure",
                "devices",
                "packetCapture",
                "captures",
                "downloadUrl",
            ],
            "operation": "generate_organization_devices_packet_capture_capture_download_url",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        capture_id = urllib.parse.quote(str(capture_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/captures/{capture_id}/downloadUrl/generate"

        return self._session.post(metadata, resource)

    def stop_organization_devices_packet_capture_capture(
        self, organization_id: str, capture_id: str, serials: list
    ) -> dict[str, Any] | None:
        """Stop a specific packet capture (not supported for Catalyst devices).

        https://developer.cisco.com/meraki/api-v1/#!stop-organization-devices-packet-capture-capture

        Args:
            organization_id: Organization ID.
            capture_id: Capture ID.
            serials: The serial(s) of the device(s) to stop the capture on.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "stop_organization_devices_packet_capture_capture",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        capture_id = urllib.parse.quote(str(capture_id), safe="")
        resource = (
            f"/organizations/{organization_id}/devices/packetCapture/captures/{capture_id}/stop"
        )

        body_params = [
            "serials",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_devices_packet_capture_schedules(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """List the Packet Capture Schedules.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-packet-capture-schedules

        Args:
            organization_id: Organization ID.
            scheduleIds: Return the packet captures schedules of the specified packet capture
              schedule ids.
            networkIds: Return the scheduled packet captures of the specified network(s).
            deviceIds: Return the scheduled packet captures of the specified device(s).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "get_organization_devices_packet_capture_schedules",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/schedules"

        query_params = [
            "scheduleIds",
            "networkIds",
            "deviceIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "scheduleIds",
            "networkIds",
            "deviceIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def create_organization_devices_packet_capture_schedule(
        self, organization_id: str, devices: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a schedule for packet capture.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-schedule

        Args:
            organization_id: Organization ID.
            devices: device details.
            name: Name of the packet capture file.
            notes: Reason for capture.
            duration: Duration of the capture in seconds.
            filterExpression: Filter expression for the capture.
            enabled: Enable or disable the schedule.
            schedule: Schedule details.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "create_organization_devices_packet_capture_schedule",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/schedules"

        body_params = [
            "devices",
            "name",
            "notes",
            "duration",
            "filterExpression",
            "enabled",
            "schedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def reorder_organization_devices_packet_capture_schedules(
        self, organization_id: str, order: list
    ) -> dict[str, Any] | None:
        """Bulk update priorities of pcap schedules.

        https://developer.cisco.com/meraki/api-v1/#!reorder-organization-devices-packet-capture-schedules

        Args:
            organization_id: Organization ID.
            order: Array of schedule IDs and their priorities to reorder.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "reorder_organization_devices_packet_capture_schedules",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/schedules/reorder"

        body_params = [
            "order",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_organization_devices_packet_capture_schedule(
        self, organization_id: str, schedule_id: str, devices: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a schedule for packet capture.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-devices-packet-capture-schedule

        Args:
            organization_id: Organization ID.
            schedule_id: Schedule ID.
            devices: device details.
            name: Name of the packet capture file.
            notes: Reason for capture.
            duration: Duration of the capture in seconds.
            filterExpression: Filter expression for the capture.
            enabled: Enable or disable the schedule.
            schedule: Schedule details.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "update_organization_devices_packet_capture_schedule",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        schedule_id = urllib.parse.quote(str(schedule_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/schedules/{schedule_id}"

        body_params = [
            "devices",
            "name",
            "notes",
            "duration",
            "filterExpression",
            "enabled",
            "schedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_devices_packet_capture_schedule(
        self, organization_id: str, scheduleId: str
    ) -> None:
        """Delete schedule from cloud.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-schedule

        Args:
            organization_id: Organization ID.
            scheduleId: Delete the capture schedules of the specified capture schedule id.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "delete_organization_devices_packet_capture_schedule",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/schedules/{scheduleId}"

        return self._session.delete(metadata, resource)

    def get_organization_devices_power_modules_statuses_by_device(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the most recent status information for power modules in rackmount MX and MS devices that support them.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-power-modules-statuses-by-device

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter device availabilities by network ID. This
              filter uses multiple exact matches.
            productTypes: Optional parameter to filter device availabilities by device product
              types. This filter uses multiple exact matches.
            serials: Optional parameter to filter device availabilities by device serial numbers.
              This filter uses multiple exact matches.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below). This filter uses multiple exact matches.
            tagsFilterType: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.

        """
        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "powerModules", "statuses", "byDevice"],
            "operation": "get_organization_devices_power_modules_statuses_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/powerModules/statuses/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "serials",
            "tags",
            "tagsFilterType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "serials",
            "tags",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_devices_provisioning_statuses(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the provisioning statuses information for devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-provisioning-statuses

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter device by network ID. This filter uses multiple
              exact matches.
            productTypes: Optional parameter to filter device by device product types. This filter
              uses multiple exact matches.
            serials: Optional parameter to filter device by device serial numbers. This filter uses
              multiple exact matches.
            status: An optional parameter to filter devices by the provisioning status. Accepted
              statuses: unprovisioned, incomplete, complete.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below). This filter uses multiple exact matches.
            tagsFilterType: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.

        """
        kwargs.update(locals())

        if "status" in kwargs:
            options = ["complete", "incomplete", "unprovisioned"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )
        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "provisioning", "statuses"],
            "operation": "get_organization_devices_provisioning_statuses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/provisioning/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "serials",
            "status",
            "tags",
            "tagsFilterType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "serials",
            "tags",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_devices_statuses(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the status of every Meraki device in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter devices by network ids.
            serials: Optional parameter to filter devices by serials.
            statuses: Optional parameter to filter devices by statuses. Valid statuses are
              ["online", "alerting", "offline", "dormant"].
            productTypes: An optional parameter to filter device statuses by product type. Valid
              types are wireless, appliance, switch, systemsManager, camera,
              cellularGateway, sensor, wirelessController, campusGateway, and
              secureConnect.
            models: Optional parameter to filter devices by models.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below).
            tagsFilterType: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.

        """
        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "statuses"],
            "operation": "get_organization_devices_statuses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "statuses",
            "productTypes",
            "models",
            "tags",
            "tagsFilterType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "statuses",
            "productTypes",
            "models",
            "tags",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_devices_statuses_overview(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return an overview of current device statuses.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses-overview

        Args:
            organization_id: Organization ID.
            productTypes: An optional parameter to filter device statuses by product type. Valid
              types are wireless, appliance, switch, systemsManager, camera,
              cellularGateway, sensor, wirelessController, campusGateway, and
              secureConnect.
            networkIds: An optional parameter to filter device statuses by network.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "statuses", "overview"],
            "operation": "get_organization_devices_statuses_overview",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/statuses/overview"

        query_params = [
            "productTypes",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "productTypes",
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_organization_devices_system_memory_usage_history_by_interval(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the memory utilization history in kB for devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-system-memory-usage-history-by-interval

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 20. Default is
              10.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 2 hours. If
              interval is provided, the timespan will be autocalculated.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              1200, 3600, 14400. The default is 300. Interval is calculated if time
              params are provided.
            networkIds: Optional parameter to filter the result set by the included set of network
              IDs.
            serials: Optional parameter to filter device availabilities history by device serial
              numbers.
            productTypes: Optional parameter to filter device statuses by product type. Valid types
              are wireless, appliance, switch, systemsManager, camera, cellularGateway,
              sensor, wirelessController, campusGateway, and secureConnect.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "organizations",
                "monitor",
                "devices",
                "system",
                "memory",
                "usage",
                "history",
                "byInterval",
            ],
            "operation": "get_organization_devices_system_memory_usage_history_by_interval",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/devices/system/memory/usage/history/byInterval"
        )

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
            "networkIds",
            "serials",
            "productTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "productTypes",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_devices_uplinks_addresses_by_device(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the current uplink addresses for devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-addresses-by-device

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter device uplinks by network ID. This filter uses
              multiple exact matches.
            productTypes: Optional parameter to filter device uplinks by device product types. This
              filter uses multiple exact matches.
            serials: Optional parameter to filter device availabilities by device serial numbers.
              This filter uses multiple exact matches.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below). This filter uses multiple exact matches.
            tagsFilterType: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.

        """
        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "uplinks", "addresses", "byDevice"],
            "operation": "get_organization_devices_uplinks_addresses_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/uplinks/addresses/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "serials",
            "tags",
            "tagsFilterType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "serials",
            "tags",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_devices_uplinks_loss_and_latency(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 60 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The
              latest possible time that t1 can be is 2 minutes into the past.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 5 minutes. The default is 5 minutes.
            uplink: Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, wan3,
              cellular. Default will return all uplinks.
            ip: Optional filter for a specific destination IP. Default will return all destination
              IPs.

        """
        kwargs.update(locals())

        if "uplink" in kwargs:
            options = ["cellular", "wan1", "wan2", "wan3"]
            assert kwargs["uplink"] in options, (
                f'''"uplink" cannot be "{kwargs["uplink"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "uplinks", "uplinksLossAndLatency"],
            "operation": "get_organization_devices_uplinks_loss_and_latency",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/devices/uplinksLossAndLatency"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "uplink",
            "ip",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_early_access_features(self, organization_id: str) -> dict[str, Any] | None:
        """List the available early access features for organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features"],
            "operation": "get_organization_early_access_features",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/earlyAccess/features"

        return self._session.get(metadata, resource)

    def get_organization_early_access_features_opt_ins(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """List the early access feature opt-ins for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-ins

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "get_organization_early_access_features_opt_ins",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/earlyAccess/features/optIns"

        return self._session.get(metadata, resource)

    def create_organization_early_access_features_opt_in(
        self, organization_id: str, shortName: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a new early access feature opt-in for an organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-early-access-features-opt-in

        Args:
            organization_id: Organization ID.
            shortName: Short name of the early access feature.
            limitScopeToNetworks: A list of network IDs to apply the opt-in to.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "create_organization_early_access_features_opt_in",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/earlyAccess/features/optIns"

        body_params = [
            "shortName",
            "limitScopeToNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_early_access_features_opt_in(
        self, organization_id: str, opt_in_id: str
    ) -> dict[str, Any] | None:
        """Show an early access feature opt-in for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-in

        Args:
            organization_id: Organization ID.
            opt_in_id: Opt in ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "get_organization_early_access_features_opt_in",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        opt_in_id = urllib.parse.quote(str(opt_in_id), safe="")
        resource = f"/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}"

        return self._session.get(metadata, resource)

    def update_organization_early_access_features_opt_in(
        self, organization_id: str, opt_in_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update an early access feature opt-in for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-early-access-features-opt-in

        Args:
            organization_id: Organization ID.
            opt_in_id: Opt in ID.
            limitScopeToNetworks: A list of network IDs to apply the opt-in to.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "update_organization_early_access_features_opt_in",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        opt_in_id = urllib.parse.quote(str(opt_in_id), safe="")
        resource = f"/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}"

        body_params = [
            "limitScopeToNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_early_access_features_opt_in(
        self, organization_id: str, opt_in_id: str
    ) -> None:
        """Delete an early access feature opt-in.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-early-access-features-opt-in

        Args:
            organization_id: Organization ID.
            opt_in_id: Opt in ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "delete_organization_early_access_features_opt_in",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        opt_in_id = urllib.parse.quote(str(opt_in_id), safe="")
        resource = f"/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}"

        return self._session.delete(metadata, resource)

    def get_organization_firmware_upgrades(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get firmware upgrade information for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            status: Optional parameter to filter the upgrade by status.
            productTypes: Optional parameter to filter the upgrade by product type.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "firmware", "upgrades"],
            "operation": "get_organization_firmware_upgrades",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/firmware/upgrades"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "status",
            "productTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "status",
            "productTypes",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_firmware_upgrades_by_device(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get firmware upgrade status for the filtered devices.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades-by-device

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter by network.
            serials: Optional parameter to filter by serial number.  All returned devices will have
              a serial number that is an exact match.
            macs: Optional parameter to filter by one or more MAC addresses belonging to devices.
              All devices returned belong to MAC addresses that are an exact match.
            firmwareUpgradeBatchIds: Optional parameter to filter by firmware upgrade batch ids.
            upgradeStatuses: Optional parameter to filter by firmware upgrade statuses.
            currentUpgradesOnly: Optional parameter to filter to only current or pending upgrade
              statuses.
            limitPerDevice: Optional parameter to limit the number of upgrade statuses returned per
              device. If omitted, a value of 5 is used.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "firmware", "upgrades", "byDevice"],
            "operation": "get_organization_firmware_upgrades_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/firmware/upgrades/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "macs",
            "firmwareUpgradeBatchIds",
            "upgradeStatuses",
            "currentUpgradesOnly",
            "limitPerDevice",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "macs",
            "firmwareUpgradeBatchIds",
            "upgradeStatuses",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_floor_plans_auto_locate_devices(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List auto locate details for each device in your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-floor-plans-auto-locate-devices

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 10000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter devices by one or more network IDs.
            floorPlanIds: Optional parameter to filter devices by one or more floorplan IDs.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "floorPlans", "autoLocate", "devices"],
            "operation": "get_organization_floor_plans_auto_locate_devices",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/floorPlans/autoLocate/devices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "floorPlanIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "floorPlanIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_floor_plans_auto_locate_statuses(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the status of auto locate for each floorplan in your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-floor-plans-auto-locate-statuses

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 10000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter floorplans by one or more network IDs.
            floorPlanIds: Optional parameter to filter floorplans by one or more floorplan IDs.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "floorPlans", "autoLocate", "statuses"],
            "operation": "get_organization_floor_plans_auto_locate_statuses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/floorPlans/autoLocate/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "floorPlanIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "floorPlanIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_integrations_xdr_networks(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns the networks in the organization that have XDR enabled.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-integrations-xdr-networks

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Optional parameter to filter the results by network IDs.
            perPage: The number of entries per page returned. Acceptable range is 3 - 100. Default
              is 20.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "integrations", "xdr", "networks"],
            "operation": "get_organization_integrations_xdr_networks",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/integrations/xdr/networks"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def disable_organization_integrations_xdr_networks(
        self, organization_id: str, networks: list
    ) -> dict[str, Any] | None:
        """Disable XDR on networks.

        https://developer.cisco.com/meraki/api-v1/#!disable-organization-integrations-xdr-networks

        Args:
            organization_id: Organization ID.
            networks: List containing the network ID and the product type to disable XDR on.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "integrations", "xdr", "networks"],
            "operation": "disable_organization_integrations_xdr_networks",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/integrations/xdr/networks/disable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def enable_organization_integrations_xdr_networks(
        self, organization_id: str, networks: list
    ) -> dict[str, Any] | None:
        """Enable XDR on networks.

        https://developer.cisco.com/meraki/api-v1/#!enable-organization-integrations-xdr-networks

        Args:
            organization_id: Organization ID.
            networks: List containing the network ID and the product type to enable XDR on.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "integrations", "xdr", "networks"],
            "operation": "enable_organization_integrations_xdr_networks",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/integrations/xdr/networks/enable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def claim_into_organization_inventory(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Claim a list of devices, licenses, and/or orders into an organization inventory.

        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization-inventory

        Args:
            organization_id: Organization ID.
            orders: The numbers of the orders that should be claimed.
            serials: The serials of the devices that should be claimed.
            licenses: The licenses that should be claimed.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "inventory"],
            "operation": "claim_into_organization_inventory",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/claim"

        body_params = [
            "orders",
            "serials",
            "licenses",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_inventory_devices(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the device inventory for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            usedState: Filter results by used or unused inventory. Accepted values are 'used' or
              'unused'.
            search: Search for devices in inventory based on serial number, mac address, or model.
            macs: Search for devices in inventory based on mac addresses.
            networkIds: Search for devices in inventory based on network ids. Use explicit 'null'
              value to get available devices only.
            serials: Search for devices in inventory based on serials.
            models: Search for devices in inventory based on model.
            orderNumbers: Search for devices in inventory based on order numbers.
            tags: Filter devices by tags. The filtering is case-sensitive. If tags are included,
              'tagsFilterType' should also be included (see below).
            tagsFilterType: To use with 'tags' parameter, to filter devices which contain ANY or ALL
              given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is
              'withAnyTags'.
            productTypes: Filter devices by product type. Accepted values are appliance, camera,
              campusGateway, cellularGateway, secureConnect, sensor, switch,
              systemsManager, wireless, and wirelessController.

        """
        kwargs.update(locals())

        if "usedState" in kwargs:
            options = ["unused", "used"]
            assert kwargs["usedState"] in options, (
                f'''"usedState" cannot be "{kwargs["usedState"]}", & must be set to one of: {options}'''
            )
        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices"],
            "operation": "get_organization_inventory_devices",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/devices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "usedState",
            "search",
            "macs",
            "networkIds",
            "serials",
            "models",
            "orderNumbers",
            "tags",
            "tagsFilterType",
            "productTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "macs",
            "networkIds",
            "serials",
            "models",
            "orderNumbers",
            "tags",
            "productTypes",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_inventory_devices_swaps_bulk(
        self, organization_id: str, swaps: list
    ) -> dict[str, Any] | None:
        """Swap the devices identified by devices.old with a devices.new, then perform the :afterAction on the devices.old.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-devices-swaps-bulk

        Args:
            organization_id: Organization ID.
            swaps: List of replacments to perform.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices", "swaps", "bulk"],
            "operation": "create_organization_inventory_devices_swaps_bulk",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/devices/swaps/bulk"

        body_params = [
            "swaps",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_inventory_devices_swaps_bulk(
        self, organization_id: str, id: str
    ) -> dict[str, Any] | None:
        """List of device swaps for a given request ID ({id}).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices-swaps-bulk

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices", "swaps", "bulk"],
            "operation": "get_organization_inventory_devices_swaps_bulk",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/inventory/devices/swaps/bulk/{id}"

        return self._session.get(metadata, resource)

    def get_organization_inventory_device(
        self, organization_id: str, serial: str
    ) -> dict[str, Any] | None:
        """Return a single device from the inventory of an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-device

        Args:
            organization_id: Organization ID.
            serial: Serial.

        """
        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices"],
            "operation": "get_organization_inventory_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/organizations/{organization_id}/inventory/devices/{serial}"

        return self._session.get(metadata, resource)

    def create_organization_inventory_onboarding_cloud_monitoring_export_event(
        self, organization_id: str, logEvent: str, timestamp: int, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Imports event logs related to the onboarding app into elastisearch.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-export-event

        Args:
            organization_id: Organization ID.
            logEvent: The type of log event this is recording, e.g. download or opening a banner.
            timestamp: A JavaScript UTC datetime stamp for when the even occurred.
            targetOS: The name of the onboarding distro being downloaded.
            request: Used to describe if this event was the result of a redirect. E.g. a query param
              if an info banner is being used.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "organizations",
                "configure",
                "inventory",
                "onboarding",
                "cloudMonitoring",
                "exportEvents",
            ],
            "operation": "create_organization_inventory_onboarding_cloud_monitoring_export_event",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/exportEvents"
        )

        body_params = [
            "logEvent",
            "timestamp",
            "targetOS",
            "request",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def create_organization_inventory_onboarding_cloud_monitoring_import(
        self, organization_id: str, devices: list
    ) -> dict[str, Any] | None:
        """Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-import

        Args:
            organization_id: Organization ID.
            devices: A set of device imports to commit.

        """
        kwargs = locals()

        metadata = {
            "tags": [
                "organizations",
                "configure",
                "inventory",
                "onboarding",
                "cloudMonitoring",
                "imports",
            ],
            "operation": "create_organization_inventory_onboarding_cloud_monitoring_import",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/imports"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_inventory_onboarding_cloud_monitoring_imports(
        self, organization_id: str, importIds: list
    ) -> dict[str, Any] | None:
        """Check the status of a committed Import operation.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-imports

        Args:
            organization_id: Organization ID.
            importIds: import ids from an imports.

        """
        kwargs = locals()

        metadata = {
            "tags": [
                "organizations",
                "configure",
                "inventory",
                "onboarding",
                "cloudMonitoring",
                "imports",
            ],
            "operation": "get_organization_inventory_onboarding_cloud_monitoring_imports",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/imports"

        query_params = [
            "importIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "importIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_organization_inventory_onboarding_cloud_monitoring_networks(
        self, organization_id: str, deviceType: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns list of networks eligible for adding cloud monitored device.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-networks

        Args:
            organization_id: Organization ID.
            deviceType: Device Type switch or wireless controller.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            search: Optional parameter to search on network name.
            perPage: The number of entries per page returned. Acceptable range is 3 - 100000.
              Default is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        if "deviceType" in kwargs:
            options = ["switch", "wireless_controller"]
            assert kwargs["deviceType"] in options, (
                f'''"deviceType" cannot be "{kwargs["deviceType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": [
                "organizations",
                "configure",
                "inventory",
                "onboarding",
                "cloudMonitoring",
                "networks",
            ],
            "operation": "get_organization_inventory_onboarding_cloud_monitoring_networks",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/networks"

        query_params = [
            "deviceType",
            "search",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_inventory_onboarding_cloud_monitoring_prepare(
        self, organization_id: str, devices: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Initiates or updates an import session.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-prepare

        Args:
            organization_id: Organization ID.
            devices: A set of devices to import (or update).
            options: Additional options for the import.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "organizations",
                "configure",
                "inventory",
                "onboarding",
                "cloudMonitoring",
                "prepare",
            ],
            "operation": "create_organization_inventory_onboarding_cloud_monitoring_prepare",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/prepare"

        body_params = [
            "devices",
            "options",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def claim_organization_inventory_orders(
        self, organization_id: str, claimId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Claim an order by the secure unique order claim number, the order claim id.

        https://developer.cisco.com/meraki/api-v1/#!claim-organization-inventory-orders

        Args:
            organization_id: Organization ID.
            claimId: The unique order claim id.
            subscriptions: The individual subscriptions to claim.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "inventory", "orders"],
            "operation": "claim_organization_inventory_orders",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/orders/claim"

        body_params = [
            "claimId",
            "subscriptions",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def preview_organization_inventory_orders(
        self, organization_id: str, claimId: str
    ) -> dict[str, Any] | None:
        """Preview the results and status of an order claim by the secure order id.

        https://developer.cisco.com/meraki/api-v1/#!preview-organization-inventory-orders

        Args:
            organization_id: Organization ID.
            claimId: The unique order claim id.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "inventory", "orders"],
            "operation": "preview_organization_inventory_orders",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/orders/preview"

        body_params = [
            "claimId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def release_from_organization_inventory(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Release a list of claimed devices from an organization.

        https://developer.cisco.com/meraki/api-v1/#!release-from-organization-inventory

        Args:
            organization_id: Organization ID.
            serials: Serials of the devices that should be released.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "inventory"],
            "operation": "release_from_organization_inventory",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/inventory/release"

        body_params = [
            "serials",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_licenses(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the licenses for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            deviceSerial: Filter the licenses to those assigned to a particular device. Returned in
              the same order that they are queued to the device.
            networkId: Filter the licenses to those assigned in a particular network.
            state: Filter the licenses to those in a particular state. Can be one of 'active',
              'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'.

        """
        kwargs.update(locals())

        if "state" in kwargs:
            options = ["active", "expired", "expiring", "recentlyQueued", "unused", "unusedActive"]
            assert kwargs["state"] in options, (
                f'''"state" cannot be "{kwargs["state"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "get_organization_licenses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/licenses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "deviceSerial",
            "networkId",
            "state",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def assign_organization_licenses_seats(
        self, organization_id: str, licenseId: str, networkId: str, seatCount: int
    ) -> dict[str, Any] | None:
        """Assign SM seats to a network.

        https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

        Args:
            organization_id: Organization ID.
            licenseId: The ID of the SM license to assign seats from.
            networkId: The ID of the SM network to assign the seats to.
            seatCount: The number of seats to assign to the SM network. Must be less than or equal
              to the total number of seats of the license.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "assign_organization_licenses_seats",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/licenses/assignSeats"

        body_params = [
            "licenseId",
            "networkId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def move_organization_licenses(
        self, organization_id: str, destOrganizationId: str, licenseIds: list
    ) -> dict[str, Any] | None:
        """Move licenses to another organization.

        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

        Args:
            organization_id: Organization ID.
            destOrganizationId: The ID of the organization to move the licenses to.
            licenseIds: A list of IDs of licenses to move to the new organization.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "move_organization_licenses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/licenses/move"

        body_params = [
            "destOrganizationId",
            "licenseIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def move_organization_licenses_seats(
        self, organization_id: str, destOrganizationId: str, licenseId: str, seatCount: int
    ) -> dict[str, Any] | None:
        """Move SM seats to another organization.

        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

        Args:
            organization_id: Organization ID.
            destOrganizationId: The ID of the organization to move the SM seats to.
            licenseId: The ID of the SM license to move the seats from.
            seatCount: The number of seats to move to the new organization. Must be less than or
              equal to the total number of seats of the license.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "move_organization_licenses_seats",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/licenses/moveSeats"

        body_params = [
            "destOrganizationId",
            "licenseId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_licenses_overview(self, organization_id: str) -> dict[str, Any] | None:
        """Return an overview of the license state for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "monitor", "licenses", "overview"],
            "operation": "get_organization_licenses_overview",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/licenses/overview"

        return self._session.get(metadata, resource)

    def renew_organization_licenses_seats(
        self, organization_id: str, licenseIdToRenew: str, unusedLicenseId: str
    ) -> dict[str, Any] | None:
        """Renew SM seats of a license.

        https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

        Args:
            organization_id: Organization ID.
            licenseIdToRenew: The ID of the SM license to renew. This license must already be
              assigned to an SM network.
            unusedLicenseId: The SM license to use to renew the seats on 'licenseIdToRenew'. This
              license must have at least as many seats available as there are seats on
              'licenseIdToRenew'.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "renew_organization_licenses_seats",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/licenses/renewSeats"

        body_params = [
            "licenseIdToRenew",
            "unusedLicenseId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_license(
        self, organization_id: str, license_id: str
    ) -> dict[str, Any] | None:
        """Display a license.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-license

        Args:
            organization_id: Organization ID.
            license_id: License ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "get_organization_license",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        license_id = urllib.parse.quote(str(license_id), safe="")
        resource = f"/organizations/{organization_id}/licenses/{license_id}"

        return self._session.get(metadata, resource)

    def update_organization_license(
        self, organization_id: str, license_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a license.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-license

        Args:
            organization_id: Organization ID.
            license_id: License ID.
            deviceSerial: The serial number of the device to assign this license to. Set this to
              null to unassign the license. If a different license is already active on
              the device, this parameter will control queueing/dequeuing this license.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "update_organization_license",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        license_id = urllib.parse.quote(str(license_id), safe="")
        resource = f"/organizations/{organization_id}/licenses/{license_id}"

        body_params = [
            "deviceSerial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_login_security(self, organization_id: str) -> dict[str, Any] | None:
        """Returns the login security settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-login-security

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "loginSecurity"],
            "operation": "get_organization_login_security",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/loginSecurity"

        return self._session.get(metadata, resource)

    def update_organization_login_security(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the login security settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

        Args:
            organization_id: Organization ID.
            enforcePasswordExpiration: Boolean indicating whether users are forced to change their
              password every X number of days.
            passwordExpirationDays: Number of days after which users will be forced to change their
              password.
            enforceDifferentPasswords: Boolean indicating whether users, when setting a new
              password, are forced to choose a new password that is different from any
              past passwords.
            numDifferentPasswords: Number of recent passwords that new password must be distinct
              from.
            enforceStrongPasswords: Deprecated. Values of 'false' are always ignored.
            minimumPasswordLength: Minimum number of characters required in admins' passwords.
            enforceAccountLockout: Boolean indicating whether users' Dashboard accounts will be
              locked out after a specified number of consecutive failed login attempts.
            accountLockoutAttempts: Number of consecutive failed login attempts after which users'
              accounts will be locked.
            enforceIdleTimeout: Boolean indicating whether users will be logged out after being idle
              for the specified number of minutes.
            idleTimeoutMinutes: Number of minutes users can remain idle before being logged out of
              their accounts.
            enforceTwoFactorAuth: Boolean indicating whether users in this organization will be
              required to use an extra verification code when logging in to Dashboard.
              This code will be sent to their mobile phone via SMS, or can be generated
              by the authenticator application.
            enforceLoginIpRanges: Boolean indicating whether organization will restrict access to
              Dashboard (including the API) from certain IP addresses.
            loginIpRanges: List of acceptable IP ranges. Entries can be single IP addresses, IP
              address ranges, and CIDR subnets.
            apiAuthentication: Details for indicating whether organization will restrict access to
              API (but not Dashboard) to certain IP addresses.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "loginSecurity"],
            "operation": "update_organization_login_security",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/loginSecurity"

        body_params = [
            "enforcePasswordExpiration",
            "passwordExpirationDays",
            "enforceDifferentPasswords",
            "numDifferentPasswords",
            "enforceStrongPasswords",
            "minimumPasswordLength",
            "enforceAccountLockout",
            "accountLockoutAttempts",
            "enforceIdleTimeout",
            "idleTimeoutMinutes",
            "enforceTwoFactorAuth",
            "enforceLoginIpRanges",
            "loginIpRanges",
            "apiAuthentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_networks(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the networks that the user has privileges on in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-networks

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            configTemplateId: An optional parameter that is the ID of a config template. Will return
              all networks bound to that template.
            isBoundToConfigTemplate: An optional parameter to filter config template bound networks.
              If configTemplateId is set, this cannot be false.
            tags: An optional parameter to filter networks by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below).
            tagsFilterType: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return networks which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.
            productTypes: An optional parameter to filter networks by product type. Results will
              have at least one of the included product types.
            perPage: The number of entries per page returned. Acceptable range is 3 - 100000.
              Default is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "networks"],
            "operation": "get_organization_networks",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/networks"

        query_params = [
            "configTemplateId",
            "isBoundToConfigTemplate",
            "tags",
            "tagsFilterType",
            "productTypes",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "tags",
            "productTypes",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_network(
        self, organization_id: str, name: str, productTypes: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a network.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-network

        Args:
            organization_id: Organization ID.
            name: The name of the new network.
            productTypes: The product type(s) of the new network. If more than one type is included,
              the network will be a combined network.
            tags: A list of tags to be applied to the network.
            timeZone: The timezone of the network. For a list of allowed timezones, please see the
              'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article.</a>.
            copyFromNetworkId: The ID of the network to copy configuration from. Other provided
              parameters will override the copied configuration, except type which must
              match this network's type exactly.
            notes: Add any notes or additional information about this network here.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networks"],
            "operation": "create_organization_network",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/networks"

        body_params = [
            "name",
            "productTypes",
            "tags",
            "timeZone",
            "copyFromNetworkId",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def combine_organization_networks(
        self, organization_id: str, name: str, networkIds: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Combine multiple networks into a single network.

        https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

        Args:
            organization_id: Organization ID.
            name: The name of the combined network.
            networkIds: A list of the network IDs that will be combined. If an ID of a combined
              network is included in this list, the other networks in the list will be
              grouped into that network.
            enrollmentString: A unique identifier which can be used for device enrollment or easy
              access through the Meraki SM Registration page or the Self Service Portal.
              Please note that changing this field may cause existing bookmarks to
              break. All networks that are part of this combined network will have their
              enrollment string appended by '-network_type'. If left empty, all exisitng
              enrollment strings will be deleted.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networks"],
            "operation": "combine_organization_networks",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/networks/combine"

        body_params = [
            "name",
            "networkIds",
            "enrollmentString",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_openapi_spec(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return the OpenAPI Specification of the organization's API documentation in JSON.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-openapi-spec

        Args:
            organization_id: Organization ID.
            version: OpenAPI Specification version to return. Default is 2.

        """
        kwargs.update(locals())

        if "version" in kwargs:
            options = [2, 3]
            assert kwargs["version"] in options, (
                f'''"version" cannot be "{kwargs["version"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "openapiSpec"],
            "operation": "get_organization_openapi_spec",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/openapiSpec"

        query_params = [
            "version",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_policies_assignments_by_client(
        self, organization_id: str, networkIds: list, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get policies for all clients with policies.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-assignments-by-client

        Args:
            organization_id: Organization ID.
            networkIds: Network Ids (minimum: 1, maximum: 30).
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.
            includeUndetectedClients: Include provisioned clients that have not associated to the
              network. Default: false.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "assignments", "byClient"],
            "operation": "get_organization_policies_assignments_by_client",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/policies/assignments/byClient"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "timespan",
            "includeUndetectedClients",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_policy_objects(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Lists Policy Objects belonging to the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 10 - 5000. Default
              is 5000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "get_organization_policy_objects",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_policy_object(
        self, organization_id: str, name: str, category: str, type: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Creates a new Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-object

        Args:
            organization_id: Organization ID.
            name: Name of a policy object, unique within the organization (alphanumeric, space,
              dash, or underscore characters only).
            category: Category of a policy object (one of: adaptivePolicy, network).
            type: Type of a policy object (one of: adaptivePolicyIpv4Cidr, cidr, fqdn, ipAndMask).
            cidr: CIDR Value of a policy object (e.g. 10.11.12.1/24").
            fqdn: Fully qualified domain name of policy object (e.g. "example.com").
            mask: Mask of a policy object (e.g. "255.255.0.0").
            ip: IP Address of a policy object (e.g. "1.2.3.4").
            groupIds: The IDs of policy object groups the policy object belongs to.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "create_organization_policy_object",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects"

        body_params = [
            "name",
            "category",
            "type",
            "cidr",
            "fqdn",
            "mask",
            "ip",
            "groupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_policy_objects_groups(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Lists Policy Object Groups belonging to the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-groups

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 10 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "get_organization_policy_objects_groups",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects/groups"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_policy_objects_group(
        self, organization_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Creates a new Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-objects-group

        Args:
            organization_id: Organization ID.
            name: A name for the group of network addresses, unique within the organization
              (alphanumeric, space, dash, or underscore characters only).
            category: Category of a policy object group (one of: NetworkObjectGroup,
              GeoLocationGroup, PortObjectGroup, ApplicationGroup).
            objectIds: A list of Policy Object ID's that this NetworkObjectGroup should be
              associated to (note: these ID's will replace the existing associated
              Policy Objects).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "create_organization_policy_objects_group",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects/groups"

        body_params = [
            "name",
            "category",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_policy_objects_group(
        self, organization_id: str, policy_object_group_id: str
    ) -> dict[str, Any] | None:
        """Shows details of a Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-group

        Args:
            organization_id: Organization ID.
            policy_object_group_id: Policy object group ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "get_organization_policy_objects_group",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_group_id = urllib.parse.quote(str(policy_object_group_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}"

        return self._session.get(metadata, resource)

    def update_organization_policy_objects_group(
        self, organization_id: str, policy_object_group_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Updates a Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-objects-group

        Args:
            organization_id: Organization ID.
            policy_object_group_id: Policy object group ID.
            name: A name for the group of network addresses, unique within the organization
              (alphanumeric, space, dash, or underscore characters only).
            objectIds: A list of Policy Object ID's that this NetworkObjectGroup should be
              associated to (note: these ID's will replace the existing associated
              Policy Objects).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "update_organization_policy_objects_group",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_group_id = urllib.parse.quote(str(policy_object_group_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}"

        body_params = [
            "name",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_policy_objects_group(
        self, organization_id: str, policy_object_group_id: str
    ) -> None:
        """Deletes a Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-objects-group

        Args:
            organization_id: Organization ID.
            policy_object_group_id: Policy object group ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "delete_organization_policy_objects_group",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_group_id = urllib.parse.quote(str(policy_object_group_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}"

        return self._session.delete(metadata, resource)

    def get_organization_policy_object(
        self, organization_id: str, policy_object_id: str
    ) -> dict[str, Any] | None:
        """Shows details of a Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-object

        Args:
            organization_id: Organization ID.
            policy_object_id: Policy object ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "get_organization_policy_object",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_id = urllib.parse.quote(str(policy_object_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects/{policy_object_id}"

        return self._session.get(metadata, resource)

    def update_organization_policy_object(
        self, organization_id: str, policy_object_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Updates a Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-object

        Args:
            organization_id: Organization ID.
            policy_object_id: Policy object ID.
            name: Name of a policy object, unique within the organization (alphanumeric, space,
              dash, or underscore characters only).
            cidr: CIDR Value of a policy object (e.g. 10.11.12.1/24").
            fqdn: Fully qualified domain name of policy object (e.g. "example.com").
            mask: Mask of a policy object (e.g. "255.255.0.0").
            ip: IP Address of a policy object (e.g. "1.2.3.4").
            groupIds: The IDs of policy object groups the policy object belongs to.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "update_organization_policy_object",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_id = urllib.parse.quote(str(policy_object_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects/{policy_object_id}"

        body_params = [
            "name",
            "cidr",
            "fqdn",
            "mask",
            "ip",
            "groupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_policy_object(
        self, organization_id: str, policy_object_id: str
    ) -> None:
        """Deletes a Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-object

        Args:
            organization_id: Organization ID.
            policy_object_id: Policy object ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "delete_organization_policy_object",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_id = urllib.parse.quote(str(policy_object_id), safe="")
        resource = f"/organizations/{organization_id}/policyObjects/{policy_object_id}"

        return self._session.delete(metadata, resource)

    def get_organization_saml(self, organization_id: str) -> dict[str, Any] | None:
        """Returns the SAML SSO enabled settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "saml"],
            "operation": "get_organization_saml",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/saml"

        return self._session.get(metadata, resource)

    def update_organization_saml(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Updates the SAML SSO enabled settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml

        Args:
            organization_id: Organization ID.
            enabled: Boolean for updating SAML SSO enabled settings.
            spInitiated: SP-Initiated SSO settings.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "saml"],
            "operation": "update_organization_saml",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/saml"

        body_params = [
            "enabled",
            "spInitiated",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_saml_idps(self, organization_id: str) -> dict[str, Any] | None:
        """List the SAML IdPs in your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idps

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "get_organization_saml_idps",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/saml/idps"

        return self._session.get(metadata, resource)

    def create_organization_saml_idp(
        self, organization_id: str, x509certSha1Fingerprint: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a SAML IdP for your organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

        Args:
            organization_id: Organization ID.
            x509certSha1Fingerprint: Fingerprint (SHA1) of the SAML certificate provided by your
              Identity Provider (IdP). This will be used for encryption / validation.
            ssoLoginUrl: Dashboard will redirect users to this URL to log in again when their
              sessions expire.
            sloLogoutUrl: Dashboard will redirect users to this URL when they sign out.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "create_organization_saml_idp",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/saml/idps"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_organization_saml_idp(
        self, organization_id: str, idp_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a SAML IdP in your organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

        Args:
            organization_id: Organization ID.
            idp_id: Idp ID.
            x509certSha1Fingerprint: Fingerprint (SHA1) of the SAML certificate provided by your
              Identity Provider (IdP). This will be used for encryption / validation.
            ssoLoginUrl: Dashboard will redirect users to this URL to log in again when their
              sessions expire.
            sloLogoutUrl: Dashboard will redirect users to this URL when they sign out.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "update_organization_saml_idp",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        idp_id = urllib.parse.quote(str(idp_id), safe="")
        resource = f"/organizations/{organization_id}/saml/idps/{idp_id}"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_saml_idp(self, organization_id: str, idp_id: str) -> dict[str, Any] | None:
        """Get a SAML IdP from your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idp

        Args:
            organization_id: Organization ID.
            idp_id: Idp ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "get_organization_saml_idp",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        idp_id = urllib.parse.quote(str(idp_id), safe="")
        resource = f"/organizations/{organization_id}/saml/idps/{idp_id}"

        return self._session.get(metadata, resource)

    def delete_organization_saml_idp(self, organization_id: str, idp_id: str) -> None:
        """Remove a SAML IdP in your organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

        Args:
            organization_id: Organization ID.
            idp_id: Idp ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "delete_organization_saml_idp",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        idp_id = urllib.parse.quote(str(idp_id), safe="")
        resource = f"/organizations/{organization_id}/saml/idps/{idp_id}"

        return self._session.delete(metadata, resource)

    def get_organization_saml_roles(self, organization_id: str) -> dict[str, Any] | None:
        """List the SAML roles for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-roles

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "get_organization_saml_roles",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/samlRoles"

        return self._session.get(metadata, resource)

    def create_organization_saml_role(
        self, organization_id: str, role: str, orgAccess: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a SAML role.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-role

        Args:
            organization_id: Organization ID.
            role: The role of the SAML administrator.
            orgAccess: The privilege of the SAML administrator on the organization. Can be one of
              'none', 'read-only', 'full' or 'enterprise' or a custom role in the format
              custom-role:ID:NAME.
            tags: The list of tags that the SAML administrator has privileges on.
            networks: The list of networks that the SAML administrator has privileges on.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "create_organization_saml_role",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/samlRoles"

        body_params = [
            "role",
            "orgAccess",
            "tags",
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_saml_role(
        self, organization_id: str, saml_role_id: str
    ) -> dict[str, Any] | None:
        """Return a SAML role.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-role

        Args:
            organization_id: Organization ID.
            saml_role_id: Saml role ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "get_organization_saml_role",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        saml_role_id = urllib.parse.quote(str(saml_role_id), safe="")
        resource = f"/organizations/{organization_id}/samlRoles/{saml_role_id}"

        return self._session.get(metadata, resource)

    def update_organization_saml_role(
        self, organization_id: str, saml_role_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a SAML role.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-role

        Args:
            organization_id: Organization ID.
            saml_role_id: Saml role ID.
            role: The role of the SAML administrator.
            orgAccess: The privilege of the SAML administrator on the organization. Can be one of
              'none', 'read-only', 'full' or 'enterprise' or a custom role in the format
              custom-role:ID:NAME.
            tags: The list of tags that the SAML administrator has privileges on.
            networks: The list of networks that the SAML administrator has privileges on.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "update_organization_saml_role",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        saml_role_id = urllib.parse.quote(str(saml_role_id), safe="")
        resource = f"/organizations/{organization_id}/samlRoles/{saml_role_id}"

        body_params = [
            "role",
            "orgAccess",
            "tags",
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_saml_role(self, organization_id: str, saml_role_id: str) -> None:
        """Remove a SAML role.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-role

        Args:
            organization_id: Organization ID.
            saml_role_id: Saml role ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "delete_organization_saml_role",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        saml_role_id = urllib.parse.quote(str(saml_role_id), safe="")
        resource = f"/organizations/{organization_id}/samlRoles/{saml_role_id}"

        return self._session.delete(metadata, resource)

    def get_organization_snmp(self, organization_id: str) -> dict[str, Any] | None:
        """Return the SNMP settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "snmp"],
            "operation": "get_organization_snmp",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/snmp"

        return self._session.get(metadata, resource)

    def update_organization_snmp(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the SNMP settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-snmp

        Args:
            organization_id: Organization ID.
            v2cEnabled: Boolean indicating whether SNMP version 2c is enabled for the organization.
            v3Enabled: Boolean indicating whether SNMP version 3 is enabled for the organization.
            v3AuthMode: The SNMP version 3 authentication mode. Can be either 'MD5' or 'SHA'.
            v3AuthPass: The SNMP version 3 authentication password. Must be at least 8 characters if
              specified.
            v3PrivMode: The SNMP version 3 privacy mode. Can be either 'DES' or 'AES128'.
            v3PrivPass: The SNMP version 3 privacy password. Must be at least 8 characters if
              specified.
            peerIps: The list of IPv4 addresses that are allowed to access the SNMP server.

        """
        kwargs.update(locals())

        if "v3AuthMode" in kwargs:
            options = ["MD5", "SHA"]
            assert kwargs["v3AuthMode"] in options, (
                f'''"v3AuthMode" cannot be "{kwargs["v3AuthMode"]}", & must be set to one of: {options}'''
            )
        if "v3PrivMode" in kwargs:
            options = ["AES128", "DES"]
            assert kwargs["v3PrivMode"] in options, (
                f'''"v3PrivMode" cannot be "{kwargs["v3PrivMode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "snmp"],
            "operation": "update_organization_snmp",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/snmp"

        body_params = [
            "v2cEnabled",
            "v3Enabled",
            "v3AuthMode",
            "v3AuthPass",
            "v3PrivMode",
            "v3PrivPass",
            "peerIps",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_splash_asset(self, organization_id: str, id: str) -> dict[str, Any] | None:
        """Get a Splash Theme Asset.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-splash-asset

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "splash", "assets"],
            "operation": "get_organization_splash_asset",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/splash/assets/{id}"

        return self._session.get(metadata, resource)

    def delete_organization_splash_asset(self, organization_id: str, id: str) -> None:
        """Delete a Splash Theme Asset.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-asset

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "splash", "assets"],
            "operation": "delete_organization_splash_asset",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/splash/assets/{id}"

        return self._session.delete(metadata, resource)

    def get_organization_splash_themes(self, organization_id: str) -> dict[str, Any] | None:
        """List Splash Themes.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-splash-themes

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "splash", "themes"],
            "operation": "get_organization_splash_themes",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/splash/themes"

        return self._session.get(metadata, resource)

    def create_organization_splash_theme(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a Splash Theme.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme

        Args:
            organization_id: Organization ID.
            name: theme name.
            baseTheme: base theme id .

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "splash", "themes"],
            "operation": "create_organization_splash_theme",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/splash/themes"

        body_params = [
            "name",
            "baseTheme",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def delete_organization_splash_theme(self, organization_id: str, id: str) -> None:
        """Delete a Splash Theme.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-theme

        Args:
            organization_id: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "splash", "themes"],
            "operation": "delete_organization_splash_theme",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organization_id}/splash/themes/{id}"

        return self._session.delete(metadata, resource)

    def create_organization_splash_theme_asset(
        self, organization_id: str, theme_identifier: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a Splash Theme Asset.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme-asset

        Args:
            organization_id: Organization ID.
            theme_identifier: Theme identifier.
            name: File name. Will overwrite files with same name.
            content: a file containing the asset content.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "splash", "themes", "assets"],
            "operation": "create_organization_splash_theme_asset",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        theme_identifier = urllib.parse.quote(str(theme_identifier), safe="")
        resource = f"/organizations/{organization_id}/splash/themes/{theme_identifier}/assets"

        body_params = [
            "name",
            "content",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_summary_top_appliances_by_utilization(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return the top 10 appliances sorted by utilization over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-appliances-by-utilization

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 25 minutes and be less than or
              equal to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "appliances", "byUtilization"],
            "operation": "get_organization_summary_top_appliances_by_utilization",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/appliances/byUtilization"

        query_params = [
            "networkTag",
            "deviceTag",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_summary_top_applications_by_usage(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return the top applications sorted by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-applications-by-usage

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            device: Match result to an exact device tag.
            networkId: Match result to an exact network id.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 25 minutes and be less than or
              equal to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "applications", "byUsage"],
            "operation": "get_organization_summary_top_applications_by_usage",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/applications/byUsage"

        query_params = [
            "networkTag",
            "device",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_summary_top_applications_categories_by_usage(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return the top application categories sorted by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-applications-categories-by-usage

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            networkId: Match result to an exact network id.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 25 minutes and be less than or
              equal to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "organizations",
                "monitor",
                "summary",
                "top",
                "applications",
                "categories",
                "byUsage",
            ],
            "operation": "get_organization_summary_top_applications_categories_by_usage",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/applications/categories/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_summary_top_clients_by_usage(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 clients by data usage (in mb) over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-by-usage

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 8 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "clients", "byUsage"],
            "operation": "get_organization_summary_top_clients_by_usage",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/clients/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_summary_top_clients_manufacturers_by_usage(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-manufacturers-by-usage

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "organizations",
                "monitor",
                "summary",
                "top",
                "clients",
                "manufacturers",
                "byUsage",
            ],
            "operation": "get_organization_summary_top_clients_manufacturers_by_usage",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/clients/manufacturers/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_summary_top_devices_by_usage(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 devices sorted by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-by-usage

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 8 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "devices", "byUsage"],
            "operation": "get_organization_summary_top_devices_by_usage",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/devices/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_summary_top_devices_models_by_usage(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 device models sorted by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-models-by-usage

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 8 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "devices", "models", "byUsage"],
            "operation": "get_organization_summary_top_devices_models_by_usage",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/devices/models/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_summary_top_networks_by_status(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the client and status overview information for the networks in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-networks-by-status

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            perPage: The number of entries per page returned. Acceptable range is 3 - 5000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "networks", "byStatus"],
            "operation": "get_organization_summary_top_networks_by_status",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/networks/byStatus"

        query_params = [
            "networkTag",
            "deviceTag",
            "quantity",
            "ssidName",
            "usageUplink",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_summary_top_ssids_by_usage(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 ssids by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-ssids-by-usage

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 8 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "ssids", "byUsage"],
            "operation": "get_organization_summary_top_ssids_by_usage",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/ssids/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_summary_top_switches_by_energy_usage(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 switches by energy usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-switches-by-energy-usage

        Args:
            organization_id: Organization ID.
            networkTag: Match result to an exact network tag.
            deviceTag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssidName: Filter results by ssid name.
            usageUplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 25 minutes and be less than or
              equal to 186 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "switches", "byEnergyUsage"],
            "operation": "get_organization_summary_top_switches_by_energy_usage",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/top/switches/byEnergyUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_uplinks_statuses(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the uplink status of every Meraki MX, MG and Z series devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-uplinks-statuses

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: A list of network IDs. The returned devices will be filtered to only include
              these networks.
            serials: A list of serial numbers. The returned devices will be filtered to only include
              these serials.
            iccids: A list of ICCIDs. The returned devices will be filtered to only include these
              ICCIDs.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "uplinks", "statuses"],
            "operation": "get_organization_uplinks_statuses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/uplinks/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "iccids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "iccids",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_webhooks_alert_types(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return a list of alert types to be used with managing webhook alerts.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-alert-types

        Args:
            organization_id: Organization ID.
            productType: Filter sample alerts to a specific product type.

        """
        kwargs.update(locals())

        if "productType" in kwargs:
            options = [
                "appliance",
                "camera",
                "cellularGateway",
                "platform",
                "sensor",
                "sm",
                "switch",
                "wireless",
            ]
            assert kwargs["productType"] in options, (
                f'''"productType" cannot be "{kwargs["productType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "webhooks", "alertTypes"],
            "operation": "get_organization_webhooks_alert_types",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/webhooks/alertTypes"

        query_params = [
            "productType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_webhooks_callbacks_status(
        self, organization_id: str, callback_id: str
    ) -> dict[str, Any] | None:
        """Return the status of an API callback.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-callbacks-status

        Args:
            organization_id: Organization ID.
            callback_id: Callback ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "webhooks", "callbacks", "statuses"],
            "operation": "get_organization_webhooks_callbacks_status",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        callback_id = urllib.parse.quote(str(callback_id), safe="")
        resource = f"/organizations/{organization_id}/webhooks/callbacks/statuses/{callback_id}"

        return self._session.get(metadata, resource)

    def get_organization_webhooks_logs(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the log of webhook POSTs sent.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-logs

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            url: The URL the webhook was sent to.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "webhooks", "logs"],
            "operation": "get_organization_webhooks_logs",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/webhooks/logs"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "url",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
