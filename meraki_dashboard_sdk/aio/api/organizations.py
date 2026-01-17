"""Organizations API endpoints."""

from __future__ import annotations

import urllib
from collections.abc import Generator
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from meraki_dashboard_sdk.aio.session import Session


class Organizations:
    """Organizations class."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_organizations(
        self,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the organizations that the user has privileges on.

        https://developer.cisco.com/meraki/api-v1/#!get-organizations

        Args:
            per_page: The number of entries per page returned. Acceptable range is 3 - 9000. Default
              is 9000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        path = f"/organizations"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def create_organization(
        self, *, name: str, management: dict | None = None
    ) -> dict[str, Any] | None:
        """Create a new organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization

        Args:
            name: The name of the organization.
            management: Information about the organization's management system.

        """
        path = f"/organizations"

        payload = {}
        if name is not None:
            payload["name"] = name
        if management is not None:
            payload["management"] = management

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization(self, *, organization_id: str) -> dict[str, Any] | None:
        """Return an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}"

        return self._session.get(scope="organizations", operation_id="getOrganization", path=path)

    def update_organization(
        self,
        *,
        organization_id: str,
        name: str | None = None,
        management: dict | None = None,
        api: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization

        Args:
            organization_id: Organization ID.
            name: The name of the organization.
            management: Information about the organization's management system.
            api: API-specific settings.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if management is not None:
            payload["management"] = management
        if api is not None:
            payload["api"] = api

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization(self, *, organization_id: str) -> None:
        """Delete an organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganization", path=path
        )

    def get_organization_action_batches(
        self, *, organization_id: str, status: str | None = None
    ) -> dict[str, Any] | None:
        """Return the list of action batches in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches

        Args:
            organization_id: Organization ID.
            status: Filter batches by status. Valid types are pending, completed, and failed.

        """
        if status is not None:
            options = ["completed", "failed", "pending"]
            assert status in options, (
                f'"status" cannot be "{status}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/actionBatches"

        params = {}
        if status is not None:
            params["status"] = status

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def create_organization_action_batch(
        self,
        *,
        organization_id: str,
        actions: list,
        confirmed: bool | None = None,
        synchronous: bool | None = None,
        callback: dict | None = None,
    ) -> dict[str, Any] | None:
        """Create an action batch.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-action-batch

        Args:
            organization_id: Organization ID.
            confirmed: Set to true for immediate execution. Set to false if the action should be
              previewed before executing. This property cannot be unset once it is true.
              Defaults to false.
            synchronous: Set to true to force the batch to run synchronous. There can be at most 20
              actions in synchronous batch. Defaults to false.
            actions: A set of changes to make as part of this action (<a
              href='https://developer.cisco.com/meraki/api/#/rest/guides/action-
              batches/'>more details</a>).
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/actionBatches"

        payload = {}
        if confirmed is not None:
            payload["confirmed"] = confirmed
        if synchronous is not None:
            payload["synchronous"] = synchronous
        if actions is not None:
            payload["actions"] = actions
        if callback is not None:
            payload["callback"] = callback

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_action_batch(
        self, *, organization_id: str, action_batch_id: str
    ) -> dict[str, Any] | None:
        """Return an action batch.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch

        Args:
            organization_id: Organization ID.
            action_batch_id: Action batch ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        action_batch_id = urllib.parse.quote(str(action_batch_id), safe="")
        path = f"/organizations/{organization_id}/actionBatches/{action_batch_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationActionBatch", path=path
        )

    def update_organization_action_batch(
        self,
        *,
        organization_id: str,
        action_batch_id: str,
        confirmed: bool | None = None,
        synchronous: bool | None = None,
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        action_batch_id = urllib.parse.quote(str(action_batch_id), safe="")
        path = f"/organizations/{organization_id}/actionBatches/{action_batch_id}"

        payload = {}
        if confirmed is not None:
            payload["confirmed"] = confirmed
        if synchronous is not None:
            payload["synchronous"] = synchronous

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_action_batch(
        self, *, organization_id: str, action_batch_id: str
    ) -> None:
        """Delete an action batch.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-action-batch

        Args:
            organization_id: Organization ID.
            action_batch_id: Action batch ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        action_batch_id = urllib.parse.quote(str(action_batch_id), safe="")
        path = f"/organizations/{organization_id}/actionBatches/{action_batch_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationActionBatch", path=path
        )

    def get_organization_adaptive_policy_acls(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List adaptive policy ACLs in a organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acls

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/acls"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAdaptivePolicyAcls", path=path
        )

    def create_organization_adaptive_policy_acl(
        self,
        *,
        organization_id: str,
        name: str,
        rules: list,
        ip_version: str,
        description: str | None = None,
    ) -> dict[str, Any] | None:
        """Creates new adaptive policy ACL.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-acl

        Args:
            organization_id: Organization ID.
            name: Name of the adaptive policy ACL.
            description: Description of the adaptive policy ACL.
            rules: An ordered array of the adaptive policy ACL rules.
            ip_version: IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'.

        """
        if ip_version is not None:
            options = ["any", "ipv4", "ipv6"]
            assert ip_version in options, (
                f'"ip_version" cannot be "{ip_version}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/acls"

        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if rules is not None:
            payload["rules"] = rules
        if ip_version is not None:
            payload["ipVersion"] = ip_version

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_adaptive_policy_acl(
        self, *, organization_id: str, acl_id: str
    ) -> dict[str, Any] | None:
        """Returns the adaptive policy ACL information.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acl

        Args:
            organization_id: Organization ID.
            acl_id: Acl ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        acl_id = urllib.parse.quote(str(acl_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAdaptivePolicyAcl", path=path
        )

    def update_organization_adaptive_policy_acl(
        self,
        *,
        organization_id: str,
        acl_id: str,
        name: str | None = None,
        description: str | None = None,
        rules: list | None = None,
        ip_version: str | None = None,
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
            ip_version: IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'.

        """
        if ip_version is not None:
            options = ["any", "ipv4", "ipv6"]
            assert ip_version in options, (
                f'"ip_version" cannot be "{ip_version}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        acl_id = urllib.parse.quote(str(acl_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if rules is not None:
            payload["rules"] = rules
        if ip_version is not None:
            payload["ipVersion"] = ip_version

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_adaptive_policy_acl(self, *, organization_id: str, acl_id: str) -> None:
        """Deletes the specified adaptive policy ACL.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-acl

        Args:
            organization_id: Organization ID.
            acl_id: Acl ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        acl_id = urllib.parse.quote(str(acl_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationAdaptivePolicyAcl", path=path
        )

    def get_organization_adaptive_policy_groups(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List adaptive policy groups in a organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-groups

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/groups"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAdaptivePolicyGroups", path=path
        )

    def create_organization_adaptive_policy_group(
        self,
        *,
        organization_id: str,
        name: str,
        sgt: int,
        description: str | None = None,
        policy_objects: list | None = None,
    ) -> dict[str, Any] | None:
        """Creates a new adaptive policy group.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-group

        Args:
            organization_id: Organization ID.
            name: Name of the group.
            sgt: SGT value of the group.
            description: Description of the group (default: "").
            policy_objects: The policy objects that belong to this group; traffic from addresses
              specified by these policy objects will be tagged with this group's SGT
              value if no other tagging scheme is being used (each requires one unique
              attribute) (default: []).

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/groups"

        payload = {}
        if name is not None:
            payload["name"] = name
        if sgt is not None:
            payload["sgt"] = sgt
        if description is not None:
            payload["description"] = description
        if policy_objects is not None:
            payload["policyObjects"] = policy_objects

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_adaptive_policy_group(
        self, *, organization_id: str, id_: str
    ) -> dict[str, Any] | None:
        """Returns an adaptive policy group.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-group

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/groups/{id_}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAdaptivePolicyGroup", path=path
        )

    def update_organization_adaptive_policy_group(
        self,
        *,
        organization_id: str,
        id_: str,
        name: str | None = None,
        sgt: int | None = None,
        description: str | None = None,
        policy_objects: list | None = None,
    ) -> dict[str, Any] | None:
        """Updates an adaptive policy group.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-group

        Args:
            organization_id: Organization ID.
            id_: ID.
            name: Name of the group.
            sgt: SGT value of the group.
            description: Description of the group.
            policy_objects: The policy objects that belong to this group; traffic from addresses
              specified by these policy objects will be tagged with this group's SGT
              value if no other tagging scheme is being used (each requires one unique
              attribute).

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/groups/{id_}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if sgt is not None:
            payload["sgt"] = sgt
        if description is not None:
            payload["description"] = description
        if policy_objects is not None:
            payload["policyObjects"] = policy_objects

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_adaptive_policy_group(self, *, organization_id: str, id_: str) -> None:
        """Deletes the specified adaptive policy group and any associated policies and references.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-group

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/groups/{id_}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationAdaptivePolicyGroup", path=path
        )

    def get_organization_adaptive_policy_overview(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Returns adaptive policy aggregate statistics for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-overview

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/overview"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAdaptivePolicyOverview", path=path
        )

    def get_organization_adaptive_policy_policies(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List adaptive policies in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policies

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/policies"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAdaptivePolicyPolicies", path=path
        )

    def create_organization_adaptive_policy_policy(
        self,
        *,
        organization_id: str,
        source_group: dict,
        destination_group: dict,
        acls: list | None = None,
        last_entry_rule: str | None = None,
    ) -> dict[str, Any] | None:
        """Add an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-policy

        Args:
            organization_id: Organization ID.
            source_group: The source adaptive policy group (requires one unique attribute).
            destination_group: The destination adaptive policy group (requires one unique
              attribute).
            acls: An ordered array of adaptive policy ACLs (each requires one unique attribute) that
              apply to this policy (default: []).
            last_entry_rule: The rule to apply if there is no matching ACL (default: "default").

        """
        if last_entry_rule is not None:
            options = ["allow", "default", "deny"]
            assert last_entry_rule in options, (
                f'"last_entry_rule" cannot be "{last_entry_rule}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/policies"

        payload = {}
        if source_group is not None:
            payload["sourceGroup"] = source_group
        if destination_group is not None:
            payload["destinationGroup"] = destination_group
        if acls is not None:
            payload["acls"] = acls
        if last_entry_rule is not None:
            payload["lastEntryRule"] = last_entry_rule

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_adaptive_policy_policy(
        self, *, organization_id: str, id_: str
    ) -> dict[str, Any] | None:
        """Return an adaptive policy.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policy

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/policies/{id_}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAdaptivePolicyPolicy", path=path
        )

    def update_organization_adaptive_policy_policy(
        self,
        *,
        organization_id: str,
        id_: str,
        source_group: dict | None = None,
        destination_group: dict | None = None,
        acls: list | None = None,
        last_entry_rule: str | None = None,
    ) -> dict[str, Any] | None:
        """Update an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-policy

        Args:
            organization_id: Organization ID.
            id_: ID.
            source_group: The source adaptive policy group (requires one unique attribute).
            destination_group: The destination adaptive policy group (requires one unique
              attribute).
            acls: An ordered array of adaptive policy ACLs (each requires one unique attribute) that
              apply to this policy.
            last_entry_rule: The rule to apply if there is no matching ACL.

        """
        if last_entry_rule is not None:
            options = ["allow", "default", "deny"]
            assert last_entry_rule in options, (
                f'"last_entry_rule" cannot be "{last_entry_rule}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/policies/{id_}"

        payload = {}
        if source_group is not None:
            payload["sourceGroup"] = source_group
        if destination_group is not None:
            payload["destinationGroup"] = destination_group
        if acls is not None:
            payload["acls"] = acls
        if last_entry_rule is not None:
            payload["lastEntryRule"] = last_entry_rule

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_adaptive_policy_policy(self, *, organization_id: str, id_: str) -> None:
        """Delete an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-policy

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/policies/{id_}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationAdaptivePolicyPolicy", path=path
        )

    def get_organization_adaptive_policy_settings(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Returns global adaptive policy settings in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-settings

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/settings"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAdaptivePolicySettings", path=path
        )

    def update_organization_adaptive_policy_settings(
        self, *, organization_id: str, enabled_networks: list | None = None
    ) -> dict[str, Any] | None:
        """Update global adaptive policy settings.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-settings

        Args:
            organization_id: Organization ID.
            enabled_networks: List of network IDs with adaptive policy enabled.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/adaptivePolicy/settings"

        payload = {}
        if enabled_networks is not None:
            payload["enabledNetworks"] = enabled_networks

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_admins(
        self, *, organization_id: str, network_ids: list | None = None
    ) -> dict[str, Any] | None:
        """List the dashboard administrators in this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-admins

        Args:
            organization_id: Organization ID.
            network_ids: Optional parameter to filter the result set by the included set of network
              IDs.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/admins"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def create_organization_admin(
        self,
        *,
        organization_id: str,
        email: str,
        name: str,
        org_access: str,
        tags: list | None = None,
        networks: list | None = None,
        authentication_method: str | None = None,
    ) -> dict[str, Any] | None:
        """Create a new dashboard administrator.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-admin

        Args:
            organization_id: Organization ID.
            email: The email of the dashboard administrator. This attribute can not be updated.
            name: The name of the dashboard administrator.
            org_access: The privilege of the dashboard administrator on the organization. Can be one
              of 'full', 'read-only', 'enterprise' or 'none'.
            tags: The list of tags that the dashboard administrator has privileges on.
            networks: The list of networks that the dashboard administrator has privileges on.
            authentication_method: No longer used as of Cisco SecureX end-of-life. Can be one of
              'Email'. The default is Email authentication.

        """
        if org_access is not None:
            options = ["enterprise", "full", "none", "read-only"]
            assert org_access in options, (
                f'"org_access" cannot be "{org_access}", & must be set to one of: {options}'
            )
        if authentication_method is not None:
            options = ["Email"]
            assert authentication_method in options, (
                f'"authentication_method" cannot be "{authentication_method}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/admins"

        payload = {}
        if email is not None:
            payload["email"] = email
        if name is not None:
            payload["name"] = name
        if org_access is not None:
            payload["orgAccess"] = org_access
        if tags is not None:
            payload["tags"] = tags
        if networks is not None:
            payload["networks"] = networks
        if authentication_method is not None:
            payload["authenticationMethod"] = authentication_method

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def update_organization_admin(
        self,
        *,
        organization_id: str,
        admin_id: str,
        name: str | None = None,
        org_access: str | None = None,
        tags: list | None = None,
        networks: list | None = None,
    ) -> dict[str, Any] | None:
        """Update an administrator.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-admin

        Args:
            organization_id: Organization ID.
            admin_id: Admin ID.
            name: The name of the dashboard administrator.
            org_access: The privilege of the dashboard administrator on the organization. Can be one
              of 'full', 'read-only', 'enterprise' or 'none'.
            tags: The list of tags that the dashboard administrator has privileges on.
            networks: The list of networks that the dashboard administrator has privileges on.

        """
        if org_access is not None:
            options = ["enterprise", "full", "none", "read-only"]
            assert org_access in options, (
                f'"org_access" cannot be "{org_access}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        admin_id = urllib.parse.quote(str(admin_id), safe="")
        path = f"/organizations/{organization_id}/admins/{admin_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if org_access is not None:
            payload["orgAccess"] = org_access
        if tags is not None:
            payload["tags"] = tags
        if networks is not None:
            payload["networks"] = networks

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_admin(self, *, organization_id: str, admin_id: str) -> None:
        """Revoke all access for a dashboard administrator within this organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-admin

        Args:
            organization_id: Organization ID.
            admin_id: Admin ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        admin_id = urllib.parse.quote(str(admin_id), safe="")
        path = f"/organizations/{organization_id}/admins/{admin_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationAdmin", path=path
        )

    def get_organization_alerts_profiles(self, *, organization_id: str) -> dict[str, Any] | None:
        """List all organization-wide alert configurations.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-alerts-profiles

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/alerts/profiles"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAlertsProfiles", path=path
        )

    def create_organization_alerts_profile(
        self,
        *,
        organization_id: str,
        type_: str,
        alert_condition: dict,
        recipients: dict,
        network_tags: list,
        description: str | None = None,
    ) -> dict[str, Any] | None:
        """Create an organization-wide alert configuration.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-alerts-profile

        Args:
            organization_id: Organization ID.
            type_: The alert type.
            alert_condition: The conditions that determine if the alert triggers.
            recipients: List of recipients that will recieve the alert.
            network_tags: Networks with these tags will be monitored for the alert.
            description: User supplied description of the alert.

        """
        if type_ is not None:
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
            assert type_ in options, (
                f'"type_" cannot be "{type_}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/alerts/profiles"

        payload = {}
        if type_ is not None:
            payload["type"] = type_
        if alert_condition is not None:
            payload["alertCondition"] = alert_condition
        if recipients is not None:
            payload["recipients"] = recipients
        if network_tags is not None:
            payload["networkTags"] = network_tags
        if description is not None:
            payload["description"] = description

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def update_organization_alerts_profile(
        self,
        *,
        organization_id: str,
        alert_config_id: str,
        enabled: bool | None = None,
        type_: str | None = None,
        alert_condition: dict | None = None,
        recipients: dict | None = None,
        network_tags: list | None = None,
        description: str | None = None,
    ) -> dict[str, Any] | None:
        """Update an organization-wide alert config.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-alerts-profile

        Args:
            organization_id: Organization ID.
            alert_config_id: Alert config ID.
            enabled: Is the alert config enabled.
            type_: The alert type.
            alert_condition: The conditions that determine if the alert triggers.
            recipients: List of recipients that will recieve the alert.
            network_tags: Networks with these tags will be monitored for the alert.
            description: User supplied description of the alert.

        """
        if type_ is not None:
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
            assert type_ in options, (
                f'"type_" cannot be "{type_}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        alert_config_id = urllib.parse.quote(str(alert_config_id), safe="")
        path = f"/organizations/{organization_id}/alerts/profiles/{alert_config_id}"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if type_ is not None:
            payload["type"] = type_
        if alert_condition is not None:
            payload["alertCondition"] = alert_condition
        if recipients is not None:
            payload["recipients"] = recipients
        if network_tags is not None:
            payload["networkTags"] = network_tags
        if description is not None:
            payload["description"] = description

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_alerts_profile(
        self, *, organization_id: str, alert_config_id: str
    ) -> None:
        """Removes an organization-wide alert config.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-alerts-profile

        Args:
            organization_id: Organization ID.
            alert_config_id: Alert config ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        alert_config_id = urllib.parse.quote(str(alert_config_id), safe="")
        path = f"/organizations/{organization_id}/alerts/profiles/{alert_config_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationAlertsProfile", path=path
        )

    def get_organization_api_requests(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        admin_id: str | None = None,
        path: str | None = None,
        method: str | None = None,
        response_code: int | None = None,
        source_ip: str | None = None,
        user_agent: str | None = None,
        version: int | None = None,
        operation_ids: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the API requests made by an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 31 days.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            admin_id: Filter the results by the ID of the admin who made the API requests.
            path: Filter the results by the path of the API requests.
            method: Filter the results by the method of the API requests (must be 'GET', 'PUT',
              'POST' or 'DELETE').
            response_code: Filter the results by the response code of the API requests.
            source_ip: Filter the results by the IP address of the originating API request.
            user_agent: Filter the results by the user agent string of the API request.
            version: Filter the results by the API version of the API request.
            operation_ids: Filter the results by one or more operation IDs for the API request.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if method is not None:
            options = ["DELETE", "GET", "POST", "PUT"]
            assert method in options, (
                f'"method" cannot be "{method}", & must be set to one of: {options}'
            )
        if version is not None:
            options = [0, 1]
            assert version in options, (
                f'"version" cannot be "{version}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/apiRequests"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if admin_id is not None:
            params["adminId"] = admin_id
        if path is not None:
            params["path"] = path
        if method is not None:
            params["method"] = method
        if response_code is not None:
            params["responseCode"] = response_code
        if source_ip is not None:
            params["sourceIp"] = source_ip
        if user_agent is not None:
            params["userAgent"] = user_agent
        if version is not None:
            params["version"] = version
        if operation_ids is not None:
            params["operationIds[]"] = operation_ids

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_api_requests_overview(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/apiRequests/overview"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_api_requests_overview_response_codes_by_interval(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        interval: int | None = None,
        version: int | None = None,
        operation_ids: list | None = None,
        source_ips: list | None = None,
        admin_ids: list | None = None,
        user_agent: str | None = None,
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
            operation_ids: Filter by operation ID of the endpoint.
            source_ips: Filter by source IP that made the API request.
            admin_ids: Filter by admin ID of user that made the API request.
            user_agent: Filter by user agent string for API request. This will filter by a complete
              or partial match.

        """
        if version is not None:
            options = [0, 1]
            assert version in options, (
                f'"version" cannot be "{version}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/apiRequests/overview/responseCodes/byInterval"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if interval is not None:
            params["interval"] = interval
        if version is not None:
            params["version"] = version
        if operation_ids is not None:
            params["operationIds[]"] = operation_ids
        if source_ips is not None:
            params["sourceIps[]"] = source_ips
        if admin_ids is not None:
            params["adminIds[]"] = admin_ids
        if user_agent is not None:
            params["userAgent"] = user_agent

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_assurance_alerts(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        network_id: str | None = None,
        severity: str | None = None,
        types: list | None = None,
        ts_start: str | None = None,
        ts_end: str | None = None,
        category: str | None = None,
        sort_by: str | None = None,
        serials: list | None = None,
        device_types: list | None = None,
        device_tags: list | None = None,
        active: bool | None = None,
        dismissed: bool | None = None,
        resolved: bool | None = None,
        suppress_alerts_for_offline_nodes: bool | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Return all health alerts for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 4 - 300. Default
              is 30.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sort_order: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'ascending'.
            network_id: Optional parameter to filter alerts by network ids.
            severity: Optional parameter to filter by severity type.
            types: Optional parameter to filter by alert type.
            ts_start: Optional parameter to filter by starting timestamp.
            ts_end: Optional parameter to filter by end timestamp.
            category: Optional parameter to filter by category.
            sort_by: Optional parameter to set column to sort by.
            serials: Optional parameter to filter by primary device serial.
            device_types: Optional parameter to filter by device types.
            device_tags: Optional parameter to filter by device tags.
            active: Optional parameter to filter by active alerts defaults to true.
            dismissed: Optional parameter to filter by dismissed alerts defaults to false.
            resolved: Optional parameter to filter by resolved alerts defaults to false.
            suppress_alerts_for_offline_nodes: When set to true the api will only return
              connectivity alerts for a given device if that device is in an offline
              state. This only applies to devices. This is ignored when resolved is
              true. Example: If a Switch has a VLan Mismatch and is Unreachable. only
              the Unreachable alert will be returned. Defaults to false.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )
        if category is not None:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert category in options, (
                f'"category" cannot be "{category}", & must be set to one of: {options}'
            )
        if sort_by is not None:
            options = ["category", "dismissedAt", "resolvedAt", "severity", "startedAt"]
            assert sort_by in options, (
                f'"sort_by" cannot be "{sort_by}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if sort_order is not None:
            params["sortOrder"] = sort_order
        if network_id is not None:
            params["networkId"] = network_id
        if severity is not None:
            params["severity"] = severity
        if types is not None:
            params["types[]"] = types
        if ts_start is not None:
            params["tsStart"] = ts_start
        if ts_end is not None:
            params["tsEnd"] = ts_end
        if category is not None:
            params["category"] = category
        if sort_by is not None:
            params["sortBy"] = sort_by
        if serials is not None:
            params["serials[]"] = serials
        if device_types is not None:
            params["deviceTypes[]"] = device_types
        if device_tags is not None:
            params["deviceTags[]"] = device_tags
        if active is not None:
            params["active"] = active
        if dismissed is not None:
            params["dismissed"] = dismissed
        if resolved is not None:
            params["resolved"] = resolved
        if suppress_alerts_for_offline_nodes is not None:
            params["suppressAlertsForOfflineNodes"] = suppress_alerts_for_offline_nodes

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def dismiss_organization_assurance_alerts(
        self, *, organization_id: str, alert_ids: list
    ) -> dict[str, Any] | None:
        """Dismiss health alerts.

        https://developer.cisco.com/meraki/api-v1/#!dismiss-organization-assurance-alerts

        Args:
            organization_id: Organization ID.
            alert_ids: Array of alert IDs to dismiss.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/dismiss"

        payload = {}
        if alert_ids is not None:
            payload["alertIds"] = alert_ids

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_assurance_alerts_overview(
        self,
        *,
        organization_id: str,
        network_id: str | None = None,
        severity: str | None = None,
        types: list | None = None,
        ts_start: str | None = None,
        ts_end: str | None = None,
        category: str | None = None,
        serials: list | None = None,
        device_types: list | None = None,
        device_tags: list | None = None,
        active: bool | None = None,
        dismissed: bool | None = None,
        resolved: bool | None = None,
        suppress_alerts_for_offline_nodes: bool | None = None,
    ) -> dict[str, Any] | None:
        """Return overview of active health alerts for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview

        Args:
            organization_id: Organization ID.
            network_id: Optional parameter to filter alerts overview by network ids.
            severity: Optional parameter to filter alerts overview by severity type.
            types: Optional parameter to filter by alert type.
            ts_start: Optional parameter to filter by starting timestamp.
            ts_end: Optional parameter to filter by end timestamp.
            category: Optional parameter to filter by category.
            serials: Optional parameter to filter by primary device serial.
            device_types: Optional parameter to filter by device types.
            device_tags: Optional parameter to filter by device tags.
            active: Optional parameter to filter by active alerts defaults to true.
            dismissed: Optional parameter to filter by dismissed alerts defaults to false.
            resolved: Optional parameter to filter by resolved alerts defaults to false.
            suppress_alerts_for_offline_nodes: When set to true the api will only return
              connectivity alerts for a given device if that device is in an offline
              state. This only applies to devices. This is ignored when resolved is
              true. Example: If a Switch has a VLan Mismatch and is Unreachable. only
              the Unreachable alert will be returned. Defaults to false.

        """
        if category is not None:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert category in options, (
                f'"category" cannot be "{category}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/overview"

        params = {}
        if network_id is not None:
            params["networkId"] = network_id
        if severity is not None:
            params["severity"] = severity
        if types is not None:
            params["types[]"] = types
        if ts_start is not None:
            params["tsStart"] = ts_start
        if ts_end is not None:
            params["tsEnd"] = ts_end
        if category is not None:
            params["category"] = category
        if serials is not None:
            params["serials[]"] = serials
        if device_types is not None:
            params["deviceTypes[]"] = device_types
        if device_tags is not None:
            params["deviceTags[]"] = device_tags
        if active is not None:
            params["active"] = active
        if dismissed is not None:
            params["dismissed"] = dismissed
        if resolved is not None:
            params["resolved"] = resolved
        if suppress_alerts_for_offline_nodes is not None:
            params["suppressAlertsForOfflineNodes"] = suppress_alerts_for_offline_nodes

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_assurance_alerts_overview_by_network(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        network_id: str | None = None,
        severity: str | None = None,
        types: list | None = None,
        ts_start: str | None = None,
        ts_end: str | None = None,
        category: str | None = None,
        serials: list | None = None,
        device_types: list | None = None,
        device_tags: list | None = None,
        active: bool | None = None,
        dismissed: bool | None = None,
        resolved: bool | None = None,
        suppress_alerts_for_offline_nodes: bool | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Return a Summary of Alerts grouped by network and severity.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-by-network

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sort_order: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'ascending'.
            network_id: Optional parameter to filter alerts overview by network id.
            severity: Optional parameter to filter alerts overview by severity type.
            types: Optional parameter to filter by alert type.
            ts_start: Optional parameter to filter by starting timestamp.
            ts_end: Optional parameter to filter by end timestamp.
            category: Optional parameter to filter by category.
            serials: Optional parameter to filter by primary device serial.
            device_types: Optional parameter to filter by device types.
            device_tags: Optional parameter to filter by device tags.
            active: Optional parameter to filter by active alerts defaults to true.
            dismissed: Optional parameter to filter by dismissed alerts defaults to false.
            resolved: Optional parameter to filter by resolved alerts defaults to false.
            suppress_alerts_for_offline_nodes: When set to true the api will only return
              connectivity alerts for a given device if that device is in an offline
              state. This only applies to devices. This is ignored when resolved is
              true. Example: If a Switch has a VLan Mismatch and is Unreachable. only
              the Unreachable alert will be returned. Defaults to false.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )
        if category is not None:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert category in options, (
                f'"category" cannot be "{category}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/overview/byNetwork"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if sort_order is not None:
            params["sortOrder"] = sort_order
        if network_id is not None:
            params["networkId"] = network_id
        if severity is not None:
            params["severity"] = severity
        if types is not None:
            params["types[]"] = types
        if ts_start is not None:
            params["tsStart"] = ts_start
        if ts_end is not None:
            params["tsEnd"] = ts_end
        if category is not None:
            params["category"] = category
        if serials is not None:
            params["serials[]"] = serials
        if device_types is not None:
            params["deviceTypes[]"] = device_types
        if device_tags is not None:
            params["deviceTags[]"] = device_tags
        if active is not None:
            params["active"] = active
        if dismissed is not None:
            params["dismissed"] = dismissed
        if resolved is not None:
            params["resolved"] = resolved
        if suppress_alerts_for_offline_nodes is not None:
            params["suppressAlertsForOfflineNodes"] = suppress_alerts_for_offline_nodes

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_assurance_alerts_overview_by_type(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        network_id: str | None = None,
        severity: str | None = None,
        types: list | None = None,
        ts_start: str | None = None,
        ts_end: str | None = None,
        category: str | None = None,
        sort_by: str | None = None,
        serials: list | None = None,
        device_types: list | None = None,
        device_tags: list | None = None,
        active: bool | None = None,
        dismissed: bool | None = None,
        resolved: bool | None = None,
        suppress_alerts_for_offline_nodes: bool | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Return a Summary of Alerts grouped by type and severity.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-by-type

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sort_order: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'ascending'.
            network_id: Optional parameter to filter alerts overview by network ids.
            severity: Optional parameter to filter alerts overview by severity type.
            types: Optional parameter to filter by alert type.
            ts_start: Optional parameter to filter by starting timestamp.
            ts_end: Optional parameter to filter by end timestamp.
            category: Optional parameter to filter by category.
            sort_by: Optional parameter to set column to sort by.
            serials: Optional parameter to filter by primary device serial.
            device_types: Optional parameter to filter by device types.
            device_tags: Optional parameter to filter by device tags.
            active: Optional parameter to filter by active alerts defaults to true.
            dismissed: Optional parameter to filter by dismissed alerts defaults to false.
            resolved: Optional parameter to filter by resolved alerts defaults to false.
            suppress_alerts_for_offline_nodes: When set to true the api will only return
              connectivity alerts for a given device if that device is in an offline
              state. This only applies to devices. This is ignored when resolved is
              true. Example: If a Switch has a VLan Mismatch and is Unreachable. only
              the Unreachable alert will be returned. Defaults to false.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )
        if category is not None:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert category in options, (
                f'"category" cannot be "{category}", & must be set to one of: {options}'
            )
        if sort_by is not None:
            options = ["count", "lastAlertedAt", "networkCount", "severity", "startedAt"]
            assert sort_by in options, (
                f'"sort_by" cannot be "{sort_by}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/overview/byType"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if sort_order is not None:
            params["sortOrder"] = sort_order
        if network_id is not None:
            params["networkId"] = network_id
        if severity is not None:
            params["severity"] = severity
        if types is not None:
            params["types[]"] = types
        if ts_start is not None:
            params["tsStart"] = ts_start
        if ts_end is not None:
            params["tsEnd"] = ts_end
        if category is not None:
            params["category"] = category
        if sort_by is not None:
            params["sortBy"] = sort_by
        if serials is not None:
            params["serials[]"] = serials
        if device_types is not None:
            params["deviceTypes[]"] = device_types
        if device_tags is not None:
            params["deviceTags[]"] = device_tags
        if active is not None:
            params["active"] = active
        if dismissed is not None:
            params["dismissed"] = dismissed
        if resolved is not None:
            params["resolved"] = resolved
        if suppress_alerts_for_offline_nodes is not None:
            params["suppressAlertsForOfflineNodes"] = suppress_alerts_for_offline_nodes

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_assurance_alerts_overview_historical(
        self,
        *,
        organization_id: str,
        segment_duration: int,
        ts_start: str,
        network_id: str | None = None,
        severity: str | None = None,
        types: list | None = None,
        ts_end: str | None = None,
        category: str | None = None,
        serials: list | None = None,
        device_types: list | None = None,
    ) -> dict[str, Any] | None:
        """Returns historical health alert overviews.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-historical

        Args:
            organization_id: Organization ID.
            segment_duration: Amount of time in seconds for each segment in the returned dataset.
            network_id: Optional parameter to filter alerts overview by network ids.
            severity: Optional parameter to filter alerts overview by severity type.
            types: Optional parameter to filter by alert type.
            ts_start: Parameter to define starting timestamp of historical totals.
            ts_end: Optional parameter to filter by end timestamp defaults to the current time.
            category: Optional parameter to filter by category.
            serials: Optional parameter to filter by primary device serial.
            device_types: Optional parameter to filter by device types.

        """
        if category is not None:
            options = ["configuration", "connectivity", "device_health", "insights"]
            assert category in options, (
                f'"category" cannot be "{category}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/overview/historical"

        params = {}
        if segment_duration is not None:
            params["segmentDuration"] = segment_duration
        if network_id is not None:
            params["networkId"] = network_id
        if severity is not None:
            params["severity"] = severity
        if types is not None:
            params["types[]"] = types
        if ts_start is not None:
            params["tsStart"] = ts_start
        if ts_end is not None:
            params["tsEnd"] = ts_end
        if category is not None:
            params["category"] = category
        if serials is not None:
            params["serials[]"] = serials
        if device_types is not None:
            params["deviceTypes[]"] = device_types

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def restore_organization_assurance_alerts(
        self, *, organization_id: str, alert_ids: list
    ) -> dict[str, Any] | None:
        """Restore health alerts from dismissed.

        https://developer.cisco.com/meraki/api-v1/#!restore-organization-assurance-alerts

        Args:
            organization_id: Organization ID.
            alert_ids: Array of alert IDs to restore.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/restore"

        payload = {}
        if alert_ids is not None:
            payload["alertIds"] = alert_ids

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_assurance_alerts_taxonomy_categories(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Return a list of Category Types.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-taxonomy-categories

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/taxonomy/categories"

        return self._session.get(
            scope="organizations",
            operation_id="getOrganizationAssuranceAlertsTaxonomyCategories",
            path=path,
        )

    def get_organization_assurance_alerts_taxonomy_types(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Return a list of alert types.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-taxonomy-types

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/taxonomy/types"

        return self._session.get(
            scope="organizations",
            operation_id="getOrganizationAssuranceAlertsTaxonomyTypes",
            path=path,
        )

    def get_organization_assurance_alert(
        self, *, organization_id: str, id_: str
    ) -> dict[str, Any] | None:
        """Return a singular Health Alert by its id.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alert

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/assurance/alerts/{id_}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationAssuranceAlert", path=path
        )

    def get_organization_branding_policies(self, *, organization_id: str) -> dict[str, Any] | None:
        """List the branding policies of an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/brandingPolicies"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationBrandingPolicies", path=path
        )

    def create_organization_branding_policy(
        self,
        *,
        organization_id: str,
        name: str,
        enabled: bool | None = None,
        admin_settings: dict | None = None,
        help_settings: dict | None = None,
        custom_logo: dict | None = None,
    ) -> dict[str, Any] | None:
        """Add a new branding policy to an organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

        Args:
            organization_id: Organization ID.
            name: Name of the Dashboard branding policy.
            enabled: Boolean indicating whether this policy is enabled.
            admin_settings: Settings for describing which kinds of admins this policy applies to.
            help_settings: Settings for describing the modifications to various Help page features.
              Each property in this object accepts one of 'default or inherit' (do not
              modify functionality), 'hide' (remove the section from Dashboard), or
              'show' (always show the section on Dashboard). Some properties in this
              object also accept custom HTML used to replace the section on Dashboard;
              see the documentation for each property to see the allowed values. Each
              property defaults to 'default or inherit' when not provided.
            custom_logo: Properties describing the custom logo attached to the branding policy.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/brandingPolicies"

        payload = {}
        if name is not None:
            payload["name"] = name
        if enabled is not None:
            payload["enabled"] = enabled
        if admin_settings is not None:
            payload["adminSettings"] = admin_settings
        if help_settings is not None:
            payload["helpSettings"] = help_settings
        if custom_logo is not None:
            payload["customLogo"] = custom_logo

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_branding_policies_priorities(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Return the branding policy IDs of an organization in priority order.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies-priorities

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/brandingPolicies/priorities"

        return self._session.get(
            scope="organizations",
            operation_id="getOrganizationBrandingPoliciesPriorities",
            path=path,
        )

    def update_organization_branding_policies_priorities(
        self, *, organization_id: str, branding_policy_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Update the priority ordering of an organization's branding policies.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

        Args:
            organization_id: Organization ID.
            branding_policy_ids: An ordered list of branding policy IDs that determines the priority
              order of how to apply the policies.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/brandingPolicies/priorities"

        payload = {}
        if branding_policy_ids is not None:
            payload["brandingPolicyIds"] = branding_policy_ids

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_branding_policy(
        self, *, organization_id: str, branding_policy_id: str
    ) -> dict[str, Any] | None:
        """Return a branding policy.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policy

        Args:
            organization_id: Organization ID.
            branding_policy_id: Branding policy ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        branding_policy_id = urllib.parse.quote(str(branding_policy_id), safe="")
        path = f"/organizations/{organization_id}/brandingPolicies/{branding_policy_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationBrandingPolicy", path=path
        )

    def update_organization_branding_policy(
        self,
        *,
        organization_id: str,
        branding_policy_id: str,
        name: str,
        enabled: bool | None = None,
        admin_settings: dict | None = None,
        help_settings: dict | None = None,
        custom_logo: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a branding policy.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

        Args:
            organization_id: Organization ID.
            branding_policy_id: Branding policy ID.
            name: Name of the Dashboard branding policy.
            enabled: Boolean indicating whether this policy is enabled.
            admin_settings: Settings for describing which kinds of admins this policy applies to.
            help_settings: Settings for describing the modifications to various Help page features.
              Each property in this object accepts one of 'default or inherit' (do not
              modify functionality), 'hide' (remove the section from Dashboard), or
              'show' (always show the section on Dashboard). Some properties in this
              object also accept custom HTML used to replace the section on Dashboard;
              see the documentation for each property to see the allowed values.
            custom_logo: Properties describing the custom logo attached to the branding policy.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        branding_policy_id = urllib.parse.quote(str(branding_policy_id), safe="")
        path = f"/organizations/{organization_id}/brandingPolicies/{branding_policy_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if enabled is not None:
            payload["enabled"] = enabled
        if admin_settings is not None:
            payload["adminSettings"] = admin_settings
        if help_settings is not None:
            payload["helpSettings"] = help_settings
        if custom_logo is not None:
            payload["customLogo"] = custom_logo

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_branding_policy(
        self, *, organization_id: str, branding_policy_id: str
    ) -> None:
        """Delete a branding policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

        Args:
            organization_id: Organization ID.
            branding_policy_id: Branding policy ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        branding_policy_id = urllib.parse.quote(str(branding_policy_id), safe="")
        path = f"/organizations/{organization_id}/brandingPolicies/{branding_policy_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationBrandingPolicy", path=path
        )

    def claim_into_organization(
        self,
        *,
        organization_id: str,
        orders: list | None = None,
        serials: list | None = None,
        licenses: list | None = None,
    ) -> dict[str, Any] | None:
        """Claim a list of devices, licenses, and/or orders into an organization inventory.

        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization

        Args:
            organization_id: Organization ID.
            orders: The numbers of the orders that should be claimed.
            serials: The serials of the devices that should be claimed.
            licenses: The licenses that should be claimed.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/claim"

        payload = {}
        if orders is not None:
            payload["orders"] = orders
        if serials is not None:
            payload["serials"] = serials
        if licenses is not None:
            payload["licenses"] = licenses

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_clients_bandwidth_usage_history(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-bandwidth-usage-history

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/clients/bandwidthUsageHistory"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_clients_overview(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/clients/overview"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_clients_search(
        self,
        *,
        organization_id: str,
        mac: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Return the client details in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-search

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 5. Default is
              5.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            mac: The MAC address of the client. Required.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/clients/search"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if mac is not None:
            params["mac"] = mac

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def clone_organization(self, *, organization_id: str, name: str) -> dict[str, Any] | None:
        """Create a new organization by cloning the addressed organization.

        https://developer.cisco.com/meraki/api-v1/#!clone-organization

        Args:
            organization_id: Organization ID.
            name: The name of the new organization.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/clone"

        payload = {}
        if name is not None:
            payload["name"] = name

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_config_templates(self, *, organization_id: str) -> dict[str, Any] | None:
        """List the configuration templates for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/configTemplates"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationConfigTemplates", path=path
        )

    def create_organization_config_template(
        self,
        *,
        organization_id: str,
        name: str,
        time_zone: str | None = None,
        copy_from_network_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Create a new configuration template.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

        Args:
            organization_id: Organization ID.
            name: The name of the configuration template.
            time_zone: The timezone of the configuration template. For a list of allowed timezones,
              please see the 'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article</a>. Not applicable if copying from existing network or template.
            copy_from_network_id: The ID of the network or config template to copy configuration
              from.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/configTemplates"

        payload = {}
        if name is not None:
            payload["name"] = name
        if time_zone is not None:
            payload["timeZone"] = time_zone
        if copy_from_network_id is not None:
            payload["copyFromNetworkId"] = copy_from_network_id

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_config_template(
        self, *, organization_id: str, config_template_id: str
    ) -> dict[str, Any] | None:
        """Return a single configuration template.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        path = f"/organizations/{organization_id}/configTemplates/{config_template_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationConfigTemplate", path=path
        )

    def update_organization_config_template(
        self,
        *,
        organization_id: str,
        config_template_id: str,
        name: str | None = None,
        time_zone: str | None = None,
    ) -> dict[str, Any] | None:
        """Update a configuration template.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.
            name: The name of the configuration template.
            time_zone: The timezone of the configuration template. For a list of allowed timezones,
              please see the 'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article.</a>.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        path = f"/organizations/{organization_id}/configTemplates/{config_template_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if time_zone is not None:
            payload["timeZone"] = time_zone

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_config_template(
        self, *, organization_id: str, config_template_id: str
    ) -> None:
        """Remove a configuration template.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-config-template

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        path = f"/organizations/{organization_id}/configTemplates/{config_template_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationConfigTemplate", path=path
        )

    def get_organization_configuration_changes(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_id: str | None = None,
        admin_id: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "prev",
    ) -> Generator[Any, None, None]:
        """View the Change Log for your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-configuration-changes

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 365 days. The default is 365 days.
            per_page: The number of entries per page returned. Acceptable range is 3 - 5000. Default
              is 5000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_id: Filters on the given network.
            admin_id: Filters on the given Admin.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" or "prev" (default) page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/configurationChanges"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_id is not None:
            params["networkId"] = network_id
        if admin_id is not None:
            params["adminId"] = admin_id

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        configuration_updated_after: str | None = None,
        network_ids: list | None = None,
        product_types: list | None = None,
        tags: list | None = None,
        tags_filter_type: str | None = None,
        name: str | None = None,
        mac: str | None = None,
        serial: str | None = None,
        model: str | None = None,
        macs: list | None = None,
        serials: list | None = None,
        sensor_metrics: list | None = None,
        sensor_alert_profile_ids: list | None = None,
        models: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the devices in an organization that have been assigned to a network.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 5000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            configuration_updated_after: Filter results by whether or not the device's configuration
              has been updated after the given timestamp.
            network_ids: Optional parameter to filter devices by network.
            product_types: Optional parameter to filter devices by product type. Valid types are
              wireless, appliance, switch, systemsManager, camera, cellularGateway,
              sensor, wirelessController, campusGateway, and secureConnect.
            tags: Optional parameter to filter devices by tags.
            tags_filter_type: Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate
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
            sensor_metrics: Optional parameter to filter devices by the metrics that they provide.
              Only applies to sensor devices.
            sensor_alert_profile_ids: Optional parameter to filter devices by the alert profiles
              that are bound to them. Only applies to sensor devices.
            models: Optional parameter to filter devices by one or more models. All returned devices
              will have a model that is an exact match.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if tags_filter_type is not None:
            options = ["withAllTags", "withAnyTags"]
            assert tags_filter_type in options, (
                f'"tags_filter_type" cannot be "{tags_filter_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if configuration_updated_after is not None:
            params["configurationUpdatedAfter"] = configuration_updated_after
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if product_types is not None:
            params["productTypes[]"] = product_types
        if tags is not None:
            params["tags[]"] = tags
        if tags_filter_type is not None:
            params["tagsFilterType"] = tags_filter_type
        if name is not None:
            params["name"] = name
        if mac is not None:
            params["mac"] = mac
        if serial is not None:
            params["serial"] = serial
        if model is not None:
            params["model"] = model
        if macs is not None:
            params["macs[]"] = macs
        if serials is not None:
            params["serials[]"] = serials
        if sensor_metrics is not None:
            params["sensorMetrics[]"] = sensor_metrics
        if sensor_alert_profile_ids is not None:
            params["sensorAlertProfileIds[]"] = sensor_alert_profile_ids
        if models is not None:
            params["models[]"] = models

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices_availabilities(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        product_types: list | None = None,
        serials: list | None = None,
        tags: list | None = None,
        tags_filter_type: str | None = None,
        statuses: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the availability information for devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter device availabilities by network ID. This
              filter uses multiple exact matches.
            product_types: Optional parameter to filter device availabilities by device product
              types. This filter uses multiple exact matches. Valid types are wireless,
              appliance, switch, camera, cellularGateway, sensor, wirelessController,
              and campusGateway.
            serials: Optional parameter to filter device availabilities by device serial numbers.
              This filter uses multiple exact matches.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below). This filter uses multiple exact matches.
            tags_filter_type: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.
            statuses: Optional parameter to filter device availabilities by device status. This
              filter uses multiple exact matches.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if tags_filter_type is not None:
            options = ["withAllTags", "withAnyTags"]
            assert tags_filter_type in options, (
                f'"tags_filter_type" cannot be "{tags_filter_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/availabilities"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if product_types is not None:
            params["productTypes[]"] = product_types
        if serials is not None:
            params["serials[]"] = serials
        if tags is not None:
            params["tags[]"] = tags
        if tags_filter_type is not None:
            params["tagsFilterType"] = tags_filter_type
        if statuses is not None:
            params["statuses[]"] = statuses

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices_availabilities_change_history(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        serials: list | None = None,
        product_types: list | None = None,
        network_ids: list | None = None,
        statuses: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the availability history information for devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities-change-history

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
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
            product_types: Optional parameter to filter device availabilities history by device
              product types.
            network_ids: Optional parameter to filter device availabilities history by network IDs.
            statuses: Optional parameter to filter device availabilities history by device statuses.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/availabilities/changeHistory"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if serials is not None:
            params["serials[]"] = serials
        if product_types is not None:
            params["productTypes[]"] = product_types
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if statuses is not None:
            params["statuses[]"] = statuses

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices_controller_migrations(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        network_ids: list | None = None,
        target: str | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Retrieve device migration statuses in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-controller-migrations

        Args:
            organization_id: Organization ID.
            serials: A list of Meraki Serials for which to retrieve migrations.
            network_ids: Filter device migrations by network IDs.
            target: Filter device migrations by target destination.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if target is not None:
            options = ["wirelessController"]
            assert target in options, (
                f'"target" cannot be "{target}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/controller/migrations"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if target is not None:
            params["target"] = target
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def create_organization_devices_controller_migration(
        self, *, organization_id: str, serials: list, target: str
    ) -> dict[str, Any] | None:
        """Migrate devices to another controller or management mode.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-controller-migration

        Args:
            organization_id: Organization ID.
            serials: A list of Meraki Serials to migrate.
            target: The controller or management mode to which the devices will be migrated.

        """
        if target is not None:
            options = ["wirelessController"]
            assert target in options, (
                f'"target" cannot be "{target}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/controller/migrations"

        payload = {}
        if serials is not None:
            payload["serials"] = serials
        if target is not None:
            payload["target"] = target

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def bulk_update_organization_devices_details(
        self, *, organization_id: str, serials: list, details: list
    ) -> dict[str, Any] | None:
        """Updating device details (currently only used for Catalyst devices).

        https://developer.cisco.com/meraki/api-v1/#!bulk-update-organization-devices-details

        Args:
            organization_id: Organization ID.
            serials: A list of serials of devices to update.
            details: An array of details.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/details/bulkUpdate"

        payload = {}
        if serials is not None:
            payload["serials"] = serials
        if details is not None:
            payload["details"] = details

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_devices_overview_by_model(
        self,
        *,
        organization_id: str,
        models: list | None = None,
        network_ids: list | None = None,
        product_types: list | None = None,
    ) -> dict[str, Any] | None:
        """Lists the count for each device model.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-overview-by-model

        Args:
            organization_id: Organization ID.
            models: Optional parameter to filter devices by one or more models. All returned devices
              will have a model that is an exact match.
            network_ids: Optional parameter to filter devices by networkId.
            product_types: Optional parameter to filter device by device product types. This filter
              uses multiple exact matches.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/overview/byModel"

        params = {}
        if models is not None:
            params["models[]"] = models
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if product_types is not None:
            params["productTypes[]"] = product_types

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_devices_packet_capture_captures(
        self,
        *,
        organization_id: str,
        capture_ids: list | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        process: list | None = None,
        capture_status: list | None = None,
        name: list | None = None,
        client_mac: list | None = None,
        notes: str | None = None,
        device_name: str | None = None,
        admin_name: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List Packet Captures.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-packet-capture-captures

        Args:
            organization_id: Organization ID.
            capture_ids: Return the packet captures of the specified capture ids.
            network_ids: Return the packet captures of the specified network(s).
            serials: Return the packet captures of the specified device(s).
            process: Return the packet captures of the specified process.
            capture_status: Return the packet captures of the specified capture status.
            name: Return the packet captures matching the specified name.
            client_mac: Return the packet captures matching the specified client macs.
            notes: Return the packet captures matching the specified notes.
            device_name: Return the packet captures matching the specified device name.
            admin_name: Return the packet captures matching the admin name.
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 365 days. The default is 365 days.
            per_page: The number of entries per page returned. Acceptable range is 3 - 100. Default
              is 10.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sort_order: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'descending'.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/captures"

        params = {}
        if capture_ids is not None:
            params["captureIds[]"] = capture_ids
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if process is not None:
            params["process[]"] = process
        if capture_status is not None:
            params["captureStatus[]"] = capture_status
        if name is not None:
            params["name[]"] = name
        if client_mac is not None:
            params["clientMac[]"] = client_mac
        if notes is not None:
            params["notes"] = notes
        if device_name is not None:
            params["deviceName"] = device_name
        if admin_name is not None:
            params["adminName"] = admin_name
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if sort_order is not None:
            params["sortOrder"] = sort_order

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def create_organization_devices_packet_capture_capture(
        self,
        *,
        organization_id: str,
        serials: list,
        name: str,
        output_type: str | None = None,
        destination: str | None = None,
        ports: str | None = None,
        notes: str | None = None,
        duration: int | None = None,
        filter_expression: str | None = None,
        interface: str | None = None,
        advanced: dict | None = None,
    ) -> dict[str, Any] | None:
        """Perform a packet capture on a device and store in Meraki Cloud.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-capture

        Args:
            organization_id: Organization ID.
            serials: The serial(s) of the device(s).
            name: Name of packet capture file.
            output_type: Output type of packet capture file. Possible values: text, pcap,
              cloudshark, or upload_to_cloud.
            destination: Destination of packet capture file. Possible values: [upload_to_cloud].
            ports: Ports of packet capture file, comma-separated.
            notes: Reason for taking the packet capture.
            duration: Duration in seconds of packet capture.
            filter_expression: Filter expression for packet capture.
            interface: Interface of the device.
            advanced: Advanced filters for IOSXE devices (supported for Campus Gateway devices
              only).

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/captures"

        payload = {}
        if serials is not None:
            payload["serials"] = serials
        if name is not None:
            payload["name"] = name
        if output_type is not None:
            payload["outputType"] = output_type
        if destination is not None:
            payload["destination"] = destination
        if ports is not None:
            payload["ports"] = ports
        if notes is not None:
            payload["notes"] = notes
        if duration is not None:
            payload["duration"] = duration
        if filter_expression is not None:
            payload["filterExpression"] = filter_expression
        if interface is not None:
            payload["interface"] = interface
        if advanced is not None:
            payload["advanced"] = advanced

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def bulk_organization_devices_packet_capture_captures_create(
        self,
        *,
        organization_id: str,
        devices: list,
        name: str,
        notes: str | None = None,
        duration: int | None = None,
        filter_expression: str | None = None,
        advanced: dict | None = None,
    ) -> dict[str, Any] | None:
        """Perform a packet capture on multiple devices and store in Meraki Cloud.

        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-create

        Args:
            organization_id: Organization ID.
            devices: Device details (maximum of 20 devices allowed).
            notes: Reason for capture.
            duration: Duration of the capture in seconds.
            filter_expression: Filter expression for the capture.
            name: Name of packet capture file.
            advanced: Advanced capture options (optional).

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/captures/bulkCreate"

        payload = {}
        if devices is not None:
            payload["devices"] = devices
        if notes is not None:
            payload["notes"] = notes
        if duration is not None:
            payload["duration"] = duration
        if filter_expression is not None:
            payload["filterExpression"] = filter_expression
        if name is not None:
            payload["name"] = name
        if advanced is not None:
            payload["advanced"] = advanced

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def bulk_organization_devices_packet_capture_captures_delete(
        self, *, organization_id: str, capture_ids: list
    ) -> dict[str, Any] | None:
        """BulkDelete packet captures from cloud.

        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-delete

        Args:
            organization_id: Organization ID.
            capture_ids: Delete the packet captures of the specified capture ids.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/captures/bulkDelete"

        payload = {}
        if capture_ids is not None:
            payload["captureIds"] = capture_ids

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_devices_packet_capture_capture(
        self, *, organization_id: str, capture_id: str
    ) -> None:
        """Delete a single packet capture from cloud using captureId.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-capture

        Args:
            organization_id: Organization ID.
            capture_id: Capture ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        capture_id = urllib.parse.quote(str(capture_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/captures/{capture_id}"

        return self._session.delete(
            scope="organizations",
            operation_id="deleteOrganizationDevicesPacketCaptureCapture",
            path=path,
        )

    def generate_organization_devices_packet_capture_capture_download_url(
        self, *, organization_id: str, capture_id: str
    ) -> dict[str, Any] | None:
        """Get presigned download URL for given packet capture id.

        https://developer.cisco.com/meraki/api-v1/#!generate-organization-devices-packet-capture-capture-download-url

        Args:
            organization_id: Organization ID.
            capture_id: Capture ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        capture_id = urllib.parse.quote(str(capture_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/captures/{capture_id}/downloadUrl/generate"

        return self._session.post(
            scope="organizations",
            operation_id="generateOrganizationDevicesPacketCaptureCaptureDownloadUrl",
            path=path,
        )

    def stop_organization_devices_packet_capture_capture(
        self, *, organization_id: str, capture_id: str, serials: list
    ) -> dict[str, Any] | None:
        """Stop a specific packet capture (not supported for Catalyst devices).

        https://developer.cisco.com/meraki/api-v1/#!stop-organization-devices-packet-capture-capture

        Args:
            organization_id: Organization ID.
            capture_id: Capture ID.
            serials: The serial(s) of the device(s) to stop the capture on.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        capture_id = urllib.parse.quote(str(capture_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/captures/{capture_id}/stop"

        payload = {}
        if serials is not None:
            payload["serials"] = serials

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_devices_packet_capture_schedules(
        self,
        *,
        organization_id: str,
        schedule_ids: list | None = None,
        network_ids: list | None = None,
        device_ids: list | None = None,
    ) -> dict[str, Any] | None:
        """List the Packet Capture Schedules.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-packet-capture-schedules

        Args:
            organization_id: Organization ID.
            schedule_ids: Return the packet captures schedules of the specified packet capture
              schedule ids.
            network_ids: Return the scheduled packet captures of the specified network(s).
            device_ids: Return the scheduled packet captures of the specified device(s).

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/schedules"

        params = {}
        if schedule_ids is not None:
            params["scheduleIds[]"] = schedule_ids
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if device_ids is not None:
            params["deviceIds[]"] = device_ids

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def create_organization_devices_packet_capture_schedule(
        self,
        *,
        organization_id: str,
        devices: list,
        name: str | None = None,
        notes: str | None = None,
        duration: int | None = None,
        filter_expression: str | None = None,
        enabled: bool | None = None,
        schedule: dict | None = None,
    ) -> dict[str, Any] | None:
        """Create a schedule for packet capture.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-schedule

        Args:
            organization_id: Organization ID.
            devices: device details.
            name: Name of the packet capture file.
            notes: Reason for capture.
            duration: Duration of the capture in seconds.
            filter_expression: Filter expression for the capture.
            enabled: Enable or disable the schedule.
            schedule: Schedule details.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/schedules"

        payload = {}
        if devices is not None:
            payload["devices"] = devices
        if name is not None:
            payload["name"] = name
        if notes is not None:
            payload["notes"] = notes
        if duration is not None:
            payload["duration"] = duration
        if filter_expression is not None:
            payload["filterExpression"] = filter_expression
        if enabled is not None:
            payload["enabled"] = enabled
        if schedule is not None:
            payload["schedule"] = schedule

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def reorder_organization_devices_packet_capture_schedules(
        self, *, organization_id: str, order: list
    ) -> dict[str, Any] | None:
        """Bulk update priorities of pcap schedules.

        https://developer.cisco.com/meraki/api-v1/#!reorder-organization-devices-packet-capture-schedules

        Args:
            organization_id: Organization ID.
            order: Array of schedule IDs and their priorities to reorder.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/schedules/reorder"

        payload = {}
        if order is not None:
            payload["order"] = order

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def update_organization_devices_packet_capture_schedule(
        self,
        *,
        organization_id: str,
        schedule_id: str,
        devices: list,
        name: str | None = None,
        notes: str | None = None,
        duration: int | None = None,
        filter_expression: str | None = None,
        enabled: bool | None = None,
        schedule: dict | None = None,
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
            filter_expression: Filter expression for the capture.
            enabled: Enable or disable the schedule.
            schedule: Schedule details.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        schedule_id = urllib.parse.quote(str(schedule_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/schedules/{schedule_id}"

        payload = {}
        if devices is not None:
            payload["devices"] = devices
        if name is not None:
            payload["name"] = name
        if notes is not None:
            payload["notes"] = notes
        if duration is not None:
            payload["duration"] = duration
        if filter_expression is not None:
            payload["filterExpression"] = filter_expression
        if enabled is not None:
            payload["enabled"] = enabled
        if schedule is not None:
            payload["schedule"] = schedule

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_devices_packet_capture_schedule(
        self, *, organization_id: str, schedule_id: str
    ) -> None:
        """Delete schedule from cloud.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-schedule

        Args:
            organization_id: Organization ID.
            schedule_id: Schedule ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        schedule_id = urllib.parse.quote(str(schedule_id), safe="")
        path = f"/organizations/{organization_id}/devices/packetCapture/schedules/{schedule_id}"

        payload = {}
        if schedule_id is not None:
            payload["scheduleId"] = schedule_id

        return self._session.delete(
            scope="organizations",
            operation_id="deleteOrganizationDevicesPacketCaptureSchedule",
            path=path,
        )

    def get_organization_devices_power_modules_statuses_by_device(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        product_types: list | None = None,
        serials: list | None = None,
        tags: list | None = None,
        tags_filter_type: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the most recent status information for power modules in rackmount MX and MS devices that support them.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-power-modules-statuses-by-device

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter device availabilities by network ID. This
              filter uses multiple exact matches.
            product_types: Optional parameter to filter device availabilities by device product
              types. This filter uses multiple exact matches.
            serials: Optional parameter to filter device availabilities by device serial numbers.
              This filter uses multiple exact matches.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below). This filter uses multiple exact matches.
            tags_filter_type: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if tags_filter_type is not None:
            options = ["withAllTags", "withAnyTags"]
            assert tags_filter_type in options, (
                f'"tags_filter_type" cannot be "{tags_filter_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/powerModules/statuses/byDevice"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if product_types is not None:
            params["productTypes[]"] = product_types
        if serials is not None:
            params["serials[]"] = serials
        if tags is not None:
            params["tags[]"] = tags
        if tags_filter_type is not None:
            params["tagsFilterType"] = tags_filter_type

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices_provisioning_statuses(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        product_types: list | None = None,
        serials: list | None = None,
        status: str | None = None,
        tags: list | None = None,
        tags_filter_type: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the provisioning statuses information for devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-provisioning-statuses

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter device by network ID. This filter uses
              multiple exact matches.
            product_types: Optional parameter to filter device by device product types. This filter
              uses multiple exact matches.
            serials: Optional parameter to filter device by device serial numbers. This filter uses
              multiple exact matches.
            status: An optional parameter to filter devices by the provisioning status. Accepted
              statuses: unprovisioned, incomplete, complete.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below). This filter uses multiple exact matches.
            tags_filter_type: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if status is not None:
            options = ["complete", "incomplete", "unprovisioned"]
            assert status in options, (
                f'"status" cannot be "{status}", & must be set to one of: {options}'
            )
        if tags_filter_type is not None:
            options = ["withAllTags", "withAnyTags"]
            assert tags_filter_type in options, (
                f'"tags_filter_type" cannot be "{tags_filter_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/provisioning/statuses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if product_types is not None:
            params["productTypes[]"] = product_types
        if serials is not None:
            params["serials[]"] = serials
        if status is not None:
            params["status"] = status
        if tags is not None:
            params["tags[]"] = tags
        if tags_filter_type is not None:
            params["tagsFilterType"] = tags_filter_type

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices_statuses(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        statuses: list | None = None,
        product_types: list | None = None,
        models: list | None = None,
        tags: list | None = None,
        tags_filter_type: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the status of every Meraki device in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter devices by network ids.
            serials: Optional parameter to filter devices by serials.
            statuses: Optional parameter to filter devices by statuses. Valid statuses are
              ["online", "alerting", "offline", "dormant"].
            product_types: An optional parameter to filter device statuses by product type. Valid
              types are wireless, appliance, switch, systemsManager, camera,
              cellularGateway, sensor, wirelessController, campusGateway, and
              secureConnect.
            models: Optional parameter to filter devices by models.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below).
            tags_filter_type: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if tags_filter_type is not None:
            options = ["withAllTags", "withAnyTags"]
            assert tags_filter_type in options, (
                f'"tags_filter_type" cannot be "{tags_filter_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/statuses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if statuses is not None:
            params["statuses[]"] = statuses
        if product_types is not None:
            params["productTypes[]"] = product_types
        if models is not None:
            params["models[]"] = models
        if tags is not None:
            params["tags[]"] = tags
        if tags_filter_type is not None:
            params["tagsFilterType"] = tags_filter_type

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices_statuses_overview(
        self,
        *,
        organization_id: str,
        product_types: list | None = None,
        network_ids: list | None = None,
    ) -> dict[str, Any] | None:
        """Return an overview of current device statuses.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses-overview

        Args:
            organization_id: Organization ID.
            product_types: An optional parameter to filter device statuses by product type. Valid
              types are wireless, appliance, switch, systemsManager, camera,
              cellularGateway, sensor, wirelessController, campusGateway, and
              secureConnect.
            network_ids: An optional parameter to filter device statuses by network.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/statuses/overview"

        params = {}
        if product_types is not None:
            params["productTypes[]"] = product_types
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_devices_system_memory_usage_history_by_interval(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        interval: int | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        product_types: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Return the memory utilization history in kB for devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-system-memory-usage-history-by-interval

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 20. Default
              is 10.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
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
            network_ids: Optional parameter to filter the result set by the included set of network
              IDs.
            serials: Optional parameter to filter device availabilities history by device serial
              numbers.
            product_types: Optional parameter to filter device statuses by product type. Valid types
              are wireless, appliance, switch, systemsManager, camera, cellularGateway,
              sensor, wirelessController, campusGateway, and secureConnect.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/system/memory/usage/history/byInterval"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if interval is not None:
            params["interval"] = interval
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if product_types is not None:
            params["productTypes[]"] = product_types

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices_uplinks_addresses_by_device(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        product_types: list | None = None,
        serials: list | None = None,
        tags: list | None = None,
        tags_filter_type: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the current uplink addresses for devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-addresses-by-device

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter device uplinks by network ID. This filter uses
              multiple exact matches.
            product_types: Optional parameter to filter device uplinks by device product types. This
              filter uses multiple exact matches.
            serials: Optional parameter to filter device availabilities by device serial numbers.
              This filter uses multiple exact matches.
            tags: An optional parameter to filter devices by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below). This filter uses multiple exact matches.
            tags_filter_type: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return devices which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if tags_filter_type is not None:
            options = ["withAllTags", "withAnyTags"]
            assert tags_filter_type in options, (
                f'"tags_filter_type" cannot be "{tags_filter_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/uplinks/addresses/byDevice"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if product_types is not None:
            params["productTypes[]"] = product_types
        if serials is not None:
            params["serials[]"] = serials
        if tags is not None:
            params["tags[]"] = tags
        if tags_filter_type is not None:
            params["tagsFilterType"] = tags_filter_type

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_devices_uplinks_loss_and_latency(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        uplink: str | None = None,
        ip: str | None = None,
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
        if uplink is not None:
            options = ["cellular", "wan1", "wan2", "wan3"]
            assert uplink in options, (
                f'"uplink" cannot be "{uplink}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/devices/uplinksLossAndLatency"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if uplink is not None:
            params["uplink"] = uplink
        if ip is not None:
            params["ip"] = ip

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_early_access_features(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List the available early access features for organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/earlyAccess/features"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationEarlyAccessFeatures", path=path
        )

    def get_organization_early_access_features_opt_ins(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List the early access feature opt-ins for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-ins

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/earlyAccess/features/optIns"

        return self._session.get(
            scope="organizations",
            operation_id="getOrganizationEarlyAccessFeaturesOptIns",
            path=path,
        )

    def create_organization_early_access_features_opt_in(
        self, *, organization_id: str, short_name: str, limit_scope_to_networks: list | None = None
    ) -> dict[str, Any] | None:
        """Create a new early access feature opt-in for an organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-early-access-features-opt-in

        Args:
            organization_id: Organization ID.
            short_name: Short name of the early access feature.
            limit_scope_to_networks: A list of network IDs to apply the opt-in to.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/earlyAccess/features/optIns"

        payload = {}
        if short_name is not None:
            payload["shortName"] = short_name
        if limit_scope_to_networks is not None:
            payload["limitScopeToNetworks"] = limit_scope_to_networks

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_early_access_features_opt_in(
        self, *, organization_id: str, opt_in_id: str
    ) -> dict[str, Any] | None:
        """Show an early access feature opt-in for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-in

        Args:
            organization_id: Organization ID.
            opt_in_id: Opt in ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        opt_in_id = urllib.parse.quote(str(opt_in_id), safe="")
        path = f"/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationEarlyAccessFeaturesOptIn", path=path
        )

    def update_organization_early_access_features_opt_in(
        self, *, organization_id: str, opt_in_id: str, limit_scope_to_networks: list | None = None
    ) -> dict[str, Any] | None:
        """Update an early access feature opt-in for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-early-access-features-opt-in

        Args:
            organization_id: Organization ID.
            opt_in_id: Opt in ID.
            limit_scope_to_networks: A list of network IDs to apply the opt-in to.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        opt_in_id = urllib.parse.quote(str(opt_in_id), safe="")
        path = f"/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}"

        payload = {}
        if limit_scope_to_networks is not None:
            payload["limitScopeToNetworks"] = limit_scope_to_networks

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_early_access_features_opt_in(
        self, *, organization_id: str, opt_in_id: str
    ) -> None:
        """Delete an early access feature opt-in.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-early-access-features-opt-in

        Args:
            organization_id: Organization ID.
            opt_in_id: Opt in ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        opt_in_id = urllib.parse.quote(str(opt_in_id), safe="")
        path = f"/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}"

        return self._session.delete(
            scope="organizations",
            operation_id="deleteOrganizationEarlyAccessFeaturesOptIn",
            path=path,
        )

    def get_organization_firmware_upgrades(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        status: list | None = None,
        product_types: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Get firmware upgrade information for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            status: Optional parameter to filter the upgrade by status.
            product_types: Optional parameter to filter the upgrade by product type.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/firmware/upgrades"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if status is not None:
            params["status[]"] = status
        if product_types is not None:
            params["productTypes[]"] = product_types

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_firmware_upgrades_by_device(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        macs: list | None = None,
        firmware_upgrade_batch_ids: list | None = None,
        upgrade_statuses: list | None = None,
        current_upgrades_only: bool | None = None,
        limit_per_device: int | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Get firmware upgrade status for the filtered devices.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades-by-device

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter by network.
            serials: Optional parameter to filter by serial number. All returned devices will have a
              serial number that is an exact match.
            macs: Optional parameter to filter by one or more MAC addresses belonging to devices.
              All devices returned belong to MAC addresses that are an exact match.
            firmware_upgrade_batch_ids: Optional parameter to filter by firmware upgrade batch ids.
            upgrade_statuses: Optional parameter to filter by firmware upgrade statuses.
            current_upgrades_only: Optional parameter to filter to only current or pending upgrade
              statuses.
            limit_per_device: Optional parameter to limit the number of upgrade statuses returned
              per device. If omitted, a value of 5 is used.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/firmware/upgrades/byDevice"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if macs is not None:
            params["macs[]"] = macs
        if firmware_upgrade_batch_ids is not None:
            params["firmwareUpgradeBatchIds[]"] = firmware_upgrade_batch_ids
        if upgrade_statuses is not None:
            params["upgradeStatuses[]"] = upgrade_statuses
        if current_upgrades_only is not None:
            params["currentUpgradesOnly"] = current_upgrades_only
        if limit_per_device is not None:
            params["limitPerDevice"] = limit_per_device

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_floor_plans_auto_locate_devices(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        floor_plan_ids: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List auto locate details for each device in your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-floor-plans-auto-locate-devices

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 10000.
              Default is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter devices by one or more network IDs.
            floor_plan_ids: Optional parameter to filter devices by one or more floorplan IDs.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/floorPlans/autoLocate/devices"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if floor_plan_ids is not None:
            params["floorPlanIds[]"] = floor_plan_ids

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_floor_plans_auto_locate_statuses(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        floor_plan_ids: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the status of auto locate for each floorplan in your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-floor-plans-auto-locate-statuses

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 10000.
              Default is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter floorplans by one or more network IDs.
            floor_plan_ids: Optional parameter to filter floorplans by one or more floorplan IDs.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/floorPlans/autoLocate/statuses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if floor_plan_ids is not None:
            params["floorPlanIds[]"] = floor_plan_ids

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_integrations_xdr_networks(
        self,
        *,
        organization_id: str,
        network_ids: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Returns the networks in the organization that have XDR enabled.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-integrations-xdr-networks

        Args:
            organization_id: Organization ID.
            network_ids: Optional parameter to filter the results by network IDs.
            per_page: The number of entries per page returned. Acceptable range is 3 - 100. Default
              is 20.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/integrations/xdr/networks"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def disable_organization_integrations_xdr_networks(
        self, *, organization_id: str, networks: list
    ) -> dict[str, Any] | None:
        """Disable XDR on networks.

        https://developer.cisco.com/meraki/api-v1/#!disable-organization-integrations-xdr-networks

        Args:
            organization_id: Organization ID.
            networks: List containing the network ID and the product type to disable XDR on.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/integrations/xdr/networks/disable"

        payload = {}
        if networks is not None:
            payload["networks"] = networks

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def enable_organization_integrations_xdr_networks(
        self, *, organization_id: str, networks: list
    ) -> dict[str, Any] | None:
        """Enable XDR on networks.

        https://developer.cisco.com/meraki/api-v1/#!enable-organization-integrations-xdr-networks

        Args:
            organization_id: Organization ID.
            networks: List containing the network ID and the product type to enable XDR on.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/integrations/xdr/networks/enable"

        payload = {}
        if networks is not None:
            payload["networks"] = networks

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def claim_into_organization_inventory(
        self,
        *,
        organization_id: str,
        orders: list | None = None,
        serials: list | None = None,
        licenses: list | None = None,
    ) -> dict[str, Any] | None:
        """Claim a list of devices, licenses, and/or orders into an organization inventory.

        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization-inventory

        Args:
            organization_id: Organization ID.
            orders: The numbers of the orders that should be claimed.
            serials: The serials of the devices that should be claimed.
            licenses: The licenses that should be claimed.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/claim"

        payload = {}
        if orders is not None:
            payload["orders"] = orders
        if serials is not None:
            payload["serials"] = serials
        if licenses is not None:
            payload["licenses"] = licenses

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_inventory_devices(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        used_state: str | None = None,
        search: str | None = None,
        macs: list | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        models: list | None = None,
        order_numbers: list | None = None,
        tags: list | None = None,
        tags_filter_type: str | None = None,
        product_types: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Return the device inventory for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            used_state: Filter results by used or unused inventory. Accepted values are 'used' or
              'unused'.
            search: Search for devices in inventory based on serial number, mac address, or model.
            macs: Search for devices in inventory based on mac addresses.
            network_ids: Search for devices in inventory based on network ids. Use explicit 'null'
              value to get available devices only.
            serials: Search for devices in inventory based on serials.
            models: Search for devices in inventory based on model.
            order_numbers: Search for devices in inventory based on order numbers.
            tags: Filter devices by tags. The filtering is case-sensitive. If tags are included,
              'tagsFilterType' should also be included (see below).
            tags_filter_type: To use with 'tags' parameter, to filter devices which contain ANY or
              ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags',
              default is 'withAnyTags'.
            product_types: Filter devices by product type. Accepted values are appliance, camera,
              campusGateway, cellularGateway, secureConnect, sensor, switch,
              systemsManager, wireless, and wirelessController.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if used_state is not None:
            options = ["unused", "used"]
            assert used_state in options, (
                f'"used_state" cannot be "{used_state}", & must be set to one of: {options}'
            )
        if tags_filter_type is not None:
            options = ["withAllTags", "withAnyTags"]
            assert tags_filter_type in options, (
                f'"tags_filter_type" cannot be "{tags_filter_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/devices"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if used_state is not None:
            params["usedState"] = used_state
        if search is not None:
            params["search"] = search
        if macs is not None:
            params["macs[]"] = macs
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if models is not None:
            params["models[]"] = models
        if order_numbers is not None:
            params["orderNumbers[]"] = order_numbers
        if tags is not None:
            params["tags[]"] = tags
        if tags_filter_type is not None:
            params["tagsFilterType"] = tags_filter_type
        if product_types is not None:
            params["productTypes[]"] = product_types

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def create_organization_inventory_devices_swaps_bulk(
        self, *, organization_id: str, swaps: list
    ) -> dict[str, Any] | None:
        """Swap the devices identified by devices.old with a devices.new, then perform the :afterAction on the devices.old.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-devices-swaps-bulk

        Args:
            organization_id: Organization ID.
            swaps: List of replacments to perform.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/devices/swaps/bulk"

        payload = {}
        if swaps is not None:
            payload["swaps"] = swaps

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_inventory_devices_swaps_bulk(
        self, *, organization_id: str, id_: str
    ) -> dict[str, Any] | None:
        """List of device swaps for a given request ID ({id}).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices-swaps-bulk

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/inventory/devices/swaps/bulk/{id_}"

        return self._session.get(
            scope="organizations",
            operation_id="getOrganizationInventoryDevicesSwapsBulk",
            path=path,
        )

    def get_organization_inventory_device(
        self, *, organization_id: str, serial: str
    ) -> dict[str, Any] | None:
        """Return a single device from the inventory of an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-device

        Args:
            organization_id: Organization ID.
            serial: Serial.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/organizations/{organization_id}/inventory/devices/{serial}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationInventoryDevice", path=path
        )

    def create_organization_inventory_onboarding_cloud_monitoring_export_event(
        self,
        *,
        organization_id: str,
        log_event: str,
        timestamp: int,
        target_o_s: str | None = None,
        request: str | None = None,
    ) -> dict[str, Any] | None:
        """Imports event logs related to the onboarding app into elastisearch.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-export-event

        Args:
            organization_id: Organization ID.
            log_event: The type of log event this is recording, e.g. download or opening a banner.
            timestamp: A JavaScript UTC datetime stamp for when the even occurred.
            target_o_s: The name of the onboarding distro being downloaded.
            request: Used to describe if this event was the result of a redirect. E.g. a query param
              if an info banner is being used.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/exportEvents"

        payload = {}
        if log_event is not None:
            payload["logEvent"] = log_event
        if timestamp is not None:
            payload["timestamp"] = timestamp
        if target_o_s is not None:
            payload["targetOS"] = target_o_s
        if request is not None:
            payload["request"] = request

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_inventory_onboarding_cloud_monitoring_imports(
        self, *, organization_id: str, import_ids: list
    ) -> dict[str, Any] | None:
        """Check the status of a committed Import operation.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-imports

        Args:
            organization_id: Organization ID.
            import_ids: import ids from an imports.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/imports"

        params = {}
        if import_ids is not None:
            params["importIds[]"] = import_ids

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def create_organization_inventory_onboarding_cloud_monitoring_import(
        self, *, organization_id: str, devices: list
    ) -> dict[str, Any] | None:
        """Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-import

        Args:
            organization_id: Organization ID.
            devices: A set of device imports to commit.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/imports"

        payload = {}
        if devices is not None:
            payload["devices"] = devices

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_inventory_onboarding_cloud_monitoring_networks(
        self,
        *,
        organization_id: str,
        device_type: str,
        search: str | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Returns list of networks eligible for adding cloud monitored device.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-networks

        Args:
            organization_id: Organization ID.
            device_type: Device Type switch or wireless controller.
            search: Optional parameter to search on network name.
            per_page: The number of entries per page returned. Acceptable range is 3 - 100000.
              Default is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if device_type is not None:
            options = ["switch", "wireless_controller"]
            assert device_type in options, (
                f'"device_type" cannot be "{device_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/networks"

        params = {}
        if device_type is not None:
            params["deviceType"] = device_type
        if search is not None:
            params["search"] = search
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def create_organization_inventory_onboarding_cloud_monitoring_prepare(
        self, *, organization_id: str, devices: list, options: dict | None = None
    ) -> dict[str, Any] | None:
        """Initiates or updates an import session.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-prepare

        Args:
            organization_id: Organization ID.
            devices: A set of devices to import (or update).
            options: Additional options for the import.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/prepare"

        payload = {}
        if devices is not None:
            payload["devices"] = devices
        if options is not None:
            payload["options"] = options

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def claim_organization_inventory_orders(
        self, *, organization_id: str, claim_id: str, subscriptions: list | None = None
    ) -> dict[str, Any] | None:
        """Claim an order by the secure unique order claim number, the order claim id.

        https://developer.cisco.com/meraki/api-v1/#!claim-organization-inventory-orders

        Args:
            organization_id: Organization ID.
            claim_id: The unique order claim id.
            subscriptions: The individual subscriptions to claim.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/orders/claim"

        payload = {}
        if claim_id is not None:
            payload["claimId"] = claim_id
        if subscriptions is not None:
            payload["subscriptions"] = subscriptions

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def preview_organization_inventory_orders(
        self, *, organization_id: str, claim_id: str
    ) -> dict[str, Any] | None:
        """Preview the results and status of an order claim by the secure order id.

        https://developer.cisco.com/meraki/api-v1/#!preview-organization-inventory-orders

        Args:
            organization_id: Organization ID.
            claim_id: The unique order claim id.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/orders/preview"

        payload = {}
        if claim_id is not None:
            payload["claimId"] = claim_id

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def release_from_organization_inventory(
        self, *, organization_id: str, serials: list | None = None
    ) -> dict[str, Any] | None:
        """Release a list of claimed devices from an organization.

        https://developer.cisco.com/meraki/api-v1/#!release-from-organization-inventory

        Args:
            organization_id: Organization ID.
            serials: Serials of the devices that should be released.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/inventory/release"

        payload = {}
        if serials is not None:
            payload["serials"] = serials

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_licenses(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        device_serial: str | None = None,
        network_id: str | None = None,
        state: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the licenses for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            device_serial: Filter the licenses to those assigned to a particular device. Returned in
              the same order that they are queued to the device.
            network_id: Filter the licenses to those assigned in a particular network.
            state: Filter the licenses to those in a particular state. Can be one of 'active',
              'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if state is not None:
            options = ["active", "expired", "expiring", "recentlyQueued", "unused", "unusedActive"]
            assert state in options, (
                f'"state" cannot be "{state}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/licenses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if device_serial is not None:
            params["deviceSerial"] = device_serial
        if network_id is not None:
            params["networkId"] = network_id
        if state is not None:
            params["state"] = state

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def assign_organization_licenses_seats(
        self, *, organization_id: str, license_id: str, network_id: str, seat_count: int
    ) -> dict[str, Any] | None:
        """Assign SM seats to a network.

        https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

        Args:
            organization_id: Organization ID.
            license_id: The ID of the SM license to assign seats from.
            network_id: The ID of the SM network to assign the seats to.
            seat_count: The number of seats to assign to the SM network. Must be less than or equal
              to the total number of seats of the license.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/licenses/assignSeats"

        payload = {}
        if license_id is not None:
            payload["licenseId"] = license_id
        if network_id is not None:
            payload["networkId"] = network_id
        if seat_count is not None:
            payload["seatCount"] = seat_count

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def move_organization_licenses(
        self, *, organization_id: str, dest_organization_id: str, license_ids: list
    ) -> dict[str, Any] | None:
        """Move licenses to another organization.

        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

        Args:
            organization_id: Organization ID.
            dest_organization_id: The ID of the organization to move the licenses to.
            license_ids: A list of IDs of licenses to move to the new organization.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/licenses/move"

        payload = {}
        if dest_organization_id is not None:
            payload["destOrganizationId"] = dest_organization_id
        if license_ids is not None:
            payload["licenseIds"] = license_ids

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def move_organization_licenses_seats(
        self, *, organization_id: str, dest_organization_id: str, license_id: str, seat_count: int
    ) -> dict[str, Any] | None:
        """Move SM seats to another organization.

        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

        Args:
            organization_id: Organization ID.
            dest_organization_id: The ID of the organization to move the SM seats to.
            license_id: The ID of the SM license to move the seats from.
            seat_count: The number of seats to move to the new organization. Must be less than or
              equal to the total number of seats of the license.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/licenses/moveSeats"

        payload = {}
        if dest_organization_id is not None:
            payload["destOrganizationId"] = dest_organization_id
        if license_id is not None:
            payload["licenseId"] = license_id
        if seat_count is not None:
            payload["seatCount"] = seat_count

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_licenses_overview(self, *, organization_id: str) -> dict[str, Any] | None:
        """Return an overview of the license state for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/licenses/overview"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationLicensesOverview", path=path
        )

    def renew_organization_licenses_seats(
        self, *, organization_id: str, license_id_to_renew: str, unused_license_id: str
    ) -> dict[str, Any] | None:
        """Renew SM seats of a license.

        https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

        Args:
            organization_id: Organization ID.
            license_id_to_renew: The ID of the SM license to renew. This license must already be
              assigned to an SM network.
            unused_license_id: The SM license to use to renew the seats on 'licenseIdToRenew'. This
              license must have at least as many seats available as there are seats on
              'licenseIdToRenew'.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/licenses/renewSeats"

        payload = {}
        if license_id_to_renew is not None:
            payload["licenseIdToRenew"] = license_id_to_renew
        if unused_license_id is not None:
            payload["unusedLicenseId"] = unused_license_id

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_license(
        self, *, organization_id: str, license_id: str
    ) -> dict[str, Any] | None:
        """Display a license.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-license

        Args:
            organization_id: Organization ID.
            license_id: License ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        license_id = urllib.parse.quote(str(license_id), safe="")
        path = f"/organizations/{organization_id}/licenses/{license_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationLicense", path=path
        )

    def update_organization_license(
        self, *, organization_id: str, license_id: str, device_serial: str | None = None
    ) -> dict[str, Any] | None:
        """Update a license.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-license

        Args:
            organization_id: Organization ID.
            license_id: License ID.
            device_serial: The serial number of the device to assign this license to. Set this to
              null to unassign the license. If a different license is already active on
              the device, this parameter will control queueing/dequeuing this license.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        license_id = urllib.parse.quote(str(license_id), safe="")
        path = f"/organizations/{organization_id}/licenses/{license_id}"

        payload = {}
        if device_serial is not None:
            payload["deviceSerial"] = device_serial

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_login_security(self, *, organization_id: str) -> dict[str, Any] | None:
        """Returns the login security settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-login-security

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/loginSecurity"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationLoginSecurity", path=path
        )

    def update_organization_login_security(
        self,
        *,
        organization_id: str,
        enforce_password_expiration: bool | None = None,
        password_expiration_days: int | None = None,
        enforce_different_passwords: bool | None = None,
        num_different_passwords: int | None = None,
        enforce_strong_passwords: bool | None = None,
        minimum_password_length: int | None = None,
        enforce_account_lockout: bool | None = None,
        account_lockout_attempts: int | None = None,
        enforce_idle_timeout: bool | None = None,
        idle_timeout_minutes: int | None = None,
        enforce_two_factor_auth: bool | None = None,
        enforce_login_ip_ranges: bool | None = None,
        login_ip_ranges: list | None = None,
        api_authentication: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the login security settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

        Args:
            organization_id: Organization ID.
            enforce_password_expiration: Boolean indicating whether users are forced to change their
              password every X number of days.
            password_expiration_days: Number of days after which users will be forced to change
              their password.
            enforce_different_passwords: Boolean indicating whether users, when setting a new
              password, are forced to choose a new password that is different from any
              past passwords.
            num_different_passwords: Number of recent passwords that new password must be distinct
              from.
            enforce_strong_passwords: Deprecated. Values of 'false' are always ignored.
            minimum_password_length: Minimum number of characters required in admins' passwords.
            enforce_account_lockout: Boolean indicating whether users' Dashboard accounts will be
              locked out after a specified number of consecutive failed login attempts.
            account_lockout_attempts: Number of consecutive failed login attempts after which users'
              accounts will be locked.
            enforce_idle_timeout: Boolean indicating whether users will be logged out after being
              idle for the specified number of minutes.
            idle_timeout_minutes: Number of minutes users can remain idle before being logged out of
              their accounts.
            enforce_two_factor_auth: Boolean indicating whether users in this organization will be
              required to use an extra verification code when logging in to Dashboard.
              This code will be sent to their mobile phone via SMS, or can be generated
              by the authenticator application.
            enforce_login_ip_ranges: Boolean indicating whether organization will restrict access to
              Dashboard (including the API) from certain IP addresses.
            login_ip_ranges: List of acceptable IP ranges. Entries can be single IP addresses, IP
              address ranges, and CIDR subnets.
            api_authentication: Details for indicating whether organization will restrict access to
              API (but not Dashboard) to certain IP addresses.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/loginSecurity"

        payload = {}
        if enforce_password_expiration is not None:
            payload["enforcePasswordExpiration"] = enforce_password_expiration
        if password_expiration_days is not None:
            payload["passwordExpirationDays"] = password_expiration_days
        if enforce_different_passwords is not None:
            payload["enforceDifferentPasswords"] = enforce_different_passwords
        if num_different_passwords is not None:
            payload["numDifferentPasswords"] = num_different_passwords
        if enforce_strong_passwords is not None:
            payload["enforceStrongPasswords"] = enforce_strong_passwords
        if minimum_password_length is not None:
            payload["minimumPasswordLength"] = minimum_password_length
        if enforce_account_lockout is not None:
            payload["enforceAccountLockout"] = enforce_account_lockout
        if account_lockout_attempts is not None:
            payload["accountLockoutAttempts"] = account_lockout_attempts
        if enforce_idle_timeout is not None:
            payload["enforceIdleTimeout"] = enforce_idle_timeout
        if idle_timeout_minutes is not None:
            payload["idleTimeoutMinutes"] = idle_timeout_minutes
        if enforce_two_factor_auth is not None:
            payload["enforceTwoFactorAuth"] = enforce_two_factor_auth
        if enforce_login_ip_ranges is not None:
            payload["enforceLoginIpRanges"] = enforce_login_ip_ranges
        if login_ip_ranges is not None:
            payload["loginIpRanges"] = login_ip_ranges
        if api_authentication is not None:
            payload["apiAuthentication"] = api_authentication

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_networks(
        self,
        *,
        organization_id: str,
        config_template_id: str | None = None,
        is_bound_to_config_template: bool | None = None,
        tags: list | None = None,
        tags_filter_type: str | None = None,
        product_types: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the networks that the user has privileges on in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-networks

        Args:
            organization_id: Organization ID.
            config_template_id: An optional parameter that is the ID of a config template. Will
              return all networks bound to that template.
            is_bound_to_config_template: An optional parameter to filter config template bound
              networks. If configTemplateId is set, this cannot be false.
            tags: An optional parameter to filter networks by tags. The filtering is case-sensitive.
              If tags are included, 'tagsFilterType' should also be included (see
              below).
            tags_filter_type: An optional parameter of value 'withAnyTags' or 'withAllTags' to
              indicate whether to return networks which contain ANY or ALL of the
              included tags. If no type is included, 'withAnyTags' will be selected.
            product_types: An optional parameter to filter networks by product type. Results will
              have at least one of the included product types.
            per_page: The number of entries per page returned. Acceptable range is 3 - 100000.
              Default is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if tags_filter_type is not None:
            options = ["withAllTags", "withAnyTags"]
            assert tags_filter_type in options, (
                f'"tags_filter_type" cannot be "{tags_filter_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/networks"

        params = {}
        if config_template_id is not None:
            params["configTemplateId"] = config_template_id
        if is_bound_to_config_template is not None:
            params["isBoundToConfigTemplate"] = is_bound_to_config_template
        if tags is not None:
            params["tags[]"] = tags
        if tags_filter_type is not None:
            params["tagsFilterType"] = tags_filter_type
        if product_types is not None:
            params["productTypes[]"] = product_types
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def create_organization_network(
        self,
        *,
        organization_id: str,
        name: str,
        product_types: list,
        tags: list | None = None,
        time_zone: str | None = None,
        copy_from_network_id: str | None = None,
        notes: str | None = None,
    ) -> dict[str, Any] | None:
        """Create a network.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-network

        Args:
            organization_id: Organization ID.
            name: The name of the new network.
            product_types: The product type(s) of the new network. If more than one type is
              included, the network will be a combined network.
            tags: A list of tags to be applied to the network.
            time_zone: The timezone of the network. For a list of allowed timezones, please see the
              'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article.</a>.
            copy_from_network_id: The ID of the network to copy configuration from. Other provided
              parameters will override the copied configuration, except type which must
              match this network's type exactly.
            notes: Add any notes or additional information about this network here.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/networks"

        payload = {}
        if name is not None:
            payload["name"] = name
        if product_types is not None:
            payload["productTypes"] = product_types
        if tags is not None:
            payload["tags"] = tags
        if time_zone is not None:
            payload["timeZone"] = time_zone
        if copy_from_network_id is not None:
            payload["copyFromNetworkId"] = copy_from_network_id
        if notes is not None:
            payload["notes"] = notes

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def combine_organization_networks(
        self,
        *,
        organization_id: str,
        name: str,
        network_ids: list,
        enrollment_string: str | None = None,
    ) -> dict[str, Any] | None:
        """Combine multiple networks into a single network.

        https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

        Args:
            organization_id: Organization ID.
            name: The name of the combined network.
            network_ids: A list of the network IDs that will be combined. If an ID of a combined
              network is included in this list, the other networks in the list will be
              grouped into that network.
            enrollment_string: A unique identifier which can be used for device enrollment or easy
              access through the Meraki SM Registration page or the Self Service Portal.
              Please note that changing this field may cause existing bookmarks to
              break. All networks that are part of this combined network will have their
              enrollment string appended by '-network_type'. If left empty, all exisitng
              enrollment strings will be deleted.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/networks/combine"

        payload = {}
        if name is not None:
            payload["name"] = name
        if network_ids is not None:
            payload["networkIds"] = network_ids
        if enrollment_string is not None:
            payload["enrollmentString"] = enrollment_string

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_openapi_spec(
        self, *, organization_id: str, version: int | None = None
    ) -> dict[str, Any] | None:
        """Return the OpenAPI Specification of the organization's API documentation in JSON.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-openapi-spec

        Args:
            organization_id: Organization ID.
            version: OpenAPI Specification version to return. Default is 2.

        """
        if version is not None:
            options = [2, 3]
            assert version in options, (
                f'"version" cannot be "{version}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/openapiSpec"

        params = {}
        if version is not None:
            params["version"] = version

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_policies_assignments_by_client(
        self,
        *,
        organization_id: str,
        network_ids: list,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        timespan: float | None = None,
        include_undetected_clients: bool | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Get policies for all clients with policies.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-assignments-by-client

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.
            include_undetected_clients: Include provisioned clients that have not associated to the
              network. Default: false.
            network_ids: Network Ids (minimum: 1, maximum: 30).
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/policies/assignments/byClient"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan
        if include_undetected_clients is not None:
            params["includeUndetectedClients"] = include_undetected_clients
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_policy_objects(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Lists Policy Objects belonging to the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 10 - 5000.
              Default is 5000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def create_organization_policy_object(
        self,
        *,
        organization_id: str,
        name: str,
        category: str,
        type_: str,
        cidr: str | None = None,
        fqdn: str | None = None,
        mask: str | None = None,
        ip: str | None = None,
        group_ids: list | None = None,
    ) -> dict[str, Any] | None:
        """Creates a new Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-object

        Args:
            organization_id: Organization ID.
            name: Name of a policy object, unique within the organization (alphanumeric, space,
              dash, or underscore characters only).
            category: Category of a policy object (one of: adaptivePolicy, network).
            type_: Type of a policy object (one of: adaptivePolicyIpv4Cidr, cidr, fqdn, ipAndMask).
            cidr: CIDR Value of a policy object (e.g. 10.11.12.1/24").
            fqdn: Fully qualified domain name of policy object (e.g. "example.com").
            mask: Mask of a policy object (e.g. "255.255.0.0").
            ip: IP Address of a policy object (e.g. "1.2.3.4").
            group_ids: The IDs of policy object groups the policy object belongs to.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects"

        payload = {}
        if name is not None:
            payload["name"] = name
        if category is not None:
            payload["category"] = category
        if type_ is not None:
            payload["type"] = type_
        if cidr is not None:
            payload["cidr"] = cidr
        if fqdn is not None:
            payload["fqdn"] = fqdn
        if mask is not None:
            payload["mask"] = mask
        if ip is not None:
            payload["ip"] = ip
        if group_ids is not None:
            payload["groupIds"] = group_ids

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_policy_objects_groups(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Lists Policy Object Groups belonging to the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-groups

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 10 - 1000.
              Default is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects/groups"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def create_organization_policy_objects_group(
        self,
        *,
        organization_id: str,
        name: str,
        category: str | None = None,
        object_ids: list | None = None,
    ) -> dict[str, Any] | None:
        """Creates a new Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-objects-group

        Args:
            organization_id: Organization ID.
            name: A name for the group of network addresses, unique within the organization
              (alphanumeric, space, dash, or underscore characters only).
            category: Category of a policy object group (one of: NetworkObjectGroup,
              GeoLocationGroup, PortObjectGroup, ApplicationGroup).
            object_ids: A list of Policy Object ID's that this NetworkObjectGroup should be
              associated to (note: these ID's will replace the existing associated
              Policy Objects).

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects/groups"

        payload = {}
        if name is not None:
            payload["name"] = name
        if category is not None:
            payload["category"] = category
        if object_ids is not None:
            payload["objectIds"] = object_ids

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_policy_objects_group(
        self, *, organization_id: str, policy_object_group_id: str
    ) -> dict[str, Any] | None:
        """Shows details of a Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-group

        Args:
            organization_id: Organization ID.
            policy_object_group_id: Policy object group ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_group_id = urllib.parse.quote(str(policy_object_group_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationPolicyObjectsGroup", path=path
        )

    def update_organization_policy_objects_group(
        self,
        *,
        organization_id: str,
        policy_object_group_id: str,
        name: str | None = None,
        object_ids: list | None = None,
    ) -> dict[str, Any] | None:
        """Updates a Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-objects-group

        Args:
            organization_id: Organization ID.
            policy_object_group_id: Policy object group ID.
            name: A name for the group of network addresses, unique within the organization
              (alphanumeric, space, dash, or underscore characters only).
            object_ids: A list of Policy Object ID's that this NetworkObjectGroup should be
              associated to (note: these ID's will replace the existing associated
              Policy Objects).

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_group_id = urllib.parse.quote(str(policy_object_group_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if object_ids is not None:
            payload["objectIds"] = object_ids

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_policy_objects_group(
        self, *, organization_id: str, policy_object_group_id: str
    ) -> None:
        """Deletes a Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-objects-group

        Args:
            organization_id: Organization ID.
            policy_object_group_id: Policy object group ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_group_id = urllib.parse.quote(str(policy_object_group_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationPolicyObjectsGroup", path=path
        )

    def get_organization_policy_object(
        self, *, organization_id: str, policy_object_id: str
    ) -> dict[str, Any] | None:
        """Shows details of a Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-object

        Args:
            organization_id: Organization ID.
            policy_object_id: Policy object ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_id = urllib.parse.quote(str(policy_object_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects/{policy_object_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationPolicyObject", path=path
        )

    def update_organization_policy_object(
        self,
        *,
        organization_id: str,
        policy_object_id: str,
        name: str | None = None,
        cidr: str | None = None,
        fqdn: str | None = None,
        mask: str | None = None,
        ip: str | None = None,
        group_ids: list | None = None,
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
            group_ids: The IDs of policy object groups the policy object belongs to.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_id = urllib.parse.quote(str(policy_object_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects/{policy_object_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if cidr is not None:
            payload["cidr"] = cidr
        if fqdn is not None:
            payload["fqdn"] = fqdn
        if mask is not None:
            payload["mask"] = mask
        if ip is not None:
            payload["ip"] = ip
        if group_ids is not None:
            payload["groupIds"] = group_ids

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_policy_object(
        self, *, organization_id: str, policy_object_id: str
    ) -> None:
        """Deletes a Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-object

        Args:
            organization_id: Organization ID.
            policy_object_id: Policy object ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        policy_object_id = urllib.parse.quote(str(policy_object_id), safe="")
        path = f"/organizations/{organization_id}/policyObjects/{policy_object_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationPolicyObject", path=path
        )

    def get_organization_saml(self, *, organization_id: str) -> dict[str, Any] | None:
        """Returns the SAML SSO enabled settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/saml"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationSaml", path=path
        )

    def update_organization_saml(
        self, *, organization_id: str, enabled: bool | None = None, sp_initiated: dict | None = None
    ) -> dict[str, Any] | None:
        """Updates the SAML SSO enabled settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml

        Args:
            organization_id: Organization ID.
            enabled: Boolean for updating SAML SSO enabled settings.
            sp_initiated: SP-Initiated SSO settings.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/saml"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if sp_initiated is not None:
            payload["spInitiated"] = sp_initiated

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_saml_idps(self, *, organization_id: str) -> dict[str, Any] | None:
        """List the SAML IdPs in your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idps

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/saml/idps"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationSamlIdps", path=path
        )

    def create_organization_saml_idp(
        self,
        *,
        organization_id: str,
        x509cert_sha1_fingerprint: str,
        sso_login_url: str | None = None,
        slo_logout_url: str | None = None,
    ) -> dict[str, Any] | None:
        """Create a SAML IdP for your organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

        Args:
            organization_id: Organization ID.
            x509cert_sha1_fingerprint: Fingerprint (SHA1) of the SAML certificate provided by your
              Identity Provider (IdP). This will be used for encryption / validation.
            sso_login_url: Dashboard will redirect users to this URL to log in again when their
              sessions expire.
            slo_logout_url: Dashboard will redirect users to this URL when they sign out.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/saml/idps"

        payload = {}
        if x509cert_sha1_fingerprint is not None:
            payload["x509certSha1Fingerprint"] = x509cert_sha1_fingerprint
        if sso_login_url is not None:
            payload["ssoLoginUrl"] = sso_login_url
        if slo_logout_url is not None:
            payload["sloLogoutUrl"] = slo_logout_url

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_saml_idp(
        self, *, organization_id: str, idp_id: str
    ) -> dict[str, Any] | None:
        """Get a SAML IdP from your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idp

        Args:
            organization_id: Organization ID.
            idp_id: Idp ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        idp_id = urllib.parse.quote(str(idp_id), safe="")
        path = f"/organizations/{organization_id}/saml/idps/{idp_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationSamlIdp", path=path
        )

    def update_organization_saml_idp(
        self,
        *,
        organization_id: str,
        idp_id: str,
        x509cert_sha1_fingerprint: str | None = None,
        sso_login_url: str | None = None,
        slo_logout_url: str | None = None,
    ) -> dict[str, Any] | None:
        """Update a SAML IdP in your organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

        Args:
            organization_id: Organization ID.
            idp_id: Idp ID.
            x509cert_sha1_fingerprint: Fingerprint (SHA1) of the SAML certificate provided by your
              Identity Provider (IdP). This will be used for encryption / validation.
            sso_login_url: Dashboard will redirect users to this URL to log in again when their
              sessions expire.
            slo_logout_url: Dashboard will redirect users to this URL when they sign out.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        idp_id = urllib.parse.quote(str(idp_id), safe="")
        path = f"/organizations/{organization_id}/saml/idps/{idp_id}"

        payload = {}
        if x509cert_sha1_fingerprint is not None:
            payload["x509certSha1Fingerprint"] = x509cert_sha1_fingerprint
        if sso_login_url is not None:
            payload["ssoLoginUrl"] = sso_login_url
        if slo_logout_url is not None:
            payload["sloLogoutUrl"] = slo_logout_url

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_saml_idp(self, *, organization_id: str, idp_id: str) -> None:
        """Remove a SAML IdP in your organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

        Args:
            organization_id: Organization ID.
            idp_id: Idp ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        idp_id = urllib.parse.quote(str(idp_id), safe="")
        path = f"/organizations/{organization_id}/saml/idps/{idp_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationSamlIdp", path=path
        )

    def get_organization_saml_roles(self, *, organization_id: str) -> dict[str, Any] | None:
        """List the SAML roles for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-roles

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/samlRoles"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationSamlRoles", path=path
        )

    def create_organization_saml_role(
        self,
        *,
        organization_id: str,
        role: str,
        org_access: str,
        tags: list | None = None,
        networks: list | None = None,
    ) -> dict[str, Any] | None:
        """Create a SAML role.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-role

        Args:
            organization_id: Organization ID.
            role: The role of the SAML administrator.
            org_access: The privilege of the SAML administrator on the organization. Can be one of
              'none', 'read-only', 'full' or 'enterprise' or a custom role in the format
              custom-role:ID:NAME.
            tags: The list of tags that the SAML administrator has privileges on.
            networks: The list of networks that the SAML administrator has privileges on.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/samlRoles"

        payload = {}
        if role is not None:
            payload["role"] = role
        if org_access is not None:
            payload["orgAccess"] = org_access
        if tags is not None:
            payload["tags"] = tags
        if networks is not None:
            payload["networks"] = networks

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_saml_role(
        self, *, organization_id: str, saml_role_id: str
    ) -> dict[str, Any] | None:
        """Return a SAML role.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-role

        Args:
            organization_id: Organization ID.
            saml_role_id: Saml role ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        saml_role_id = urllib.parse.quote(str(saml_role_id), safe="")
        path = f"/organizations/{organization_id}/samlRoles/{saml_role_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationSamlRole", path=path
        )

    def update_organization_saml_role(
        self,
        *,
        organization_id: str,
        saml_role_id: str,
        role: str | None = None,
        org_access: str | None = None,
        tags: list | None = None,
        networks: list | None = None,
    ) -> dict[str, Any] | None:
        """Update a SAML role.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-role

        Args:
            organization_id: Organization ID.
            saml_role_id: Saml role ID.
            role: The role of the SAML administrator.
            org_access: The privilege of the SAML administrator on the organization. Can be one of
              'none', 'read-only', 'full' or 'enterprise' or a custom role in the format
              custom-role:ID:NAME.
            tags: The list of tags that the SAML administrator has privileges on.
            networks: The list of networks that the SAML administrator has privileges on.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        saml_role_id = urllib.parse.quote(str(saml_role_id), safe="")
        path = f"/organizations/{organization_id}/samlRoles/{saml_role_id}"

        payload = {}
        if role is not None:
            payload["role"] = role
        if org_access is not None:
            payload["orgAccess"] = org_access
        if tags is not None:
            payload["tags"] = tags
        if networks is not None:
            payload["networks"] = networks

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_saml_role(self, *, organization_id: str, saml_role_id: str) -> None:
        """Remove a SAML role.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-role

        Args:
            organization_id: Organization ID.
            saml_role_id: Saml role ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        saml_role_id = urllib.parse.quote(str(saml_role_id), safe="")
        path = f"/organizations/{organization_id}/samlRoles/{saml_role_id}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationSamlRole", path=path
        )

    def get_organization_snmp(self, *, organization_id: str) -> dict[str, Any] | None:
        """Return the SNMP settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/snmp"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationSnmp", path=path
        )

    def update_organization_snmp(
        self,
        *,
        organization_id: str,
        v2c_enabled: bool | None = None,
        v3_enabled: bool | None = None,
        v3_auth_mode: str | None = None,
        v3_auth_pass: str | None = None,
        v3_priv_mode: str | None = None,
        v3_priv_pass: str | None = None,
        peer_ips: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the SNMP settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-snmp

        Args:
            organization_id: Organization ID.
            v2c_enabled: Boolean indicating whether SNMP version 2c is enabled for the organization.
            v3_enabled: Boolean indicating whether SNMP version 3 is enabled for the organization.
            v3_auth_mode: The SNMP version 3 authentication mode. Can be either 'MD5' or 'SHA'.
            v3_auth_pass: The SNMP version 3 authentication password. Must be at least 8 characters
              if specified.
            v3_priv_mode: The SNMP version 3 privacy mode. Can be either 'DES' or 'AES128'.
            v3_priv_pass: The SNMP version 3 privacy password. Must be at least 8 characters if
              specified.
            peer_ips: The list of IPv4 addresses that are allowed to access the SNMP server.

        """
        if v3_auth_mode is not None:
            options = ["MD5", "SHA"]
            assert v3_auth_mode in options, (
                f'"v3_auth_mode" cannot be "{v3_auth_mode}", & must be set to one of: {options}'
            )
        if v3_priv_mode is not None:
            options = ["AES128", "DES"]
            assert v3_priv_mode in options, (
                f'"v3_priv_mode" cannot be "{v3_priv_mode}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/snmp"

        payload = {}
        if v2c_enabled is not None:
            payload["v2cEnabled"] = v2c_enabled
        if v3_enabled is not None:
            payload["v3Enabled"] = v3_enabled
        if v3_auth_mode is not None:
            payload["v3AuthMode"] = v3_auth_mode
        if v3_auth_pass is not None:
            payload["v3AuthPass"] = v3_auth_pass
        if v3_priv_mode is not None:
            payload["v3PrivMode"] = v3_priv_mode
        if v3_priv_pass is not None:
            payload["v3PrivPass"] = v3_priv_pass
        if peer_ips is not None:
            payload["peerIps"] = peer_ips

        return self._session.put(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_splash_asset(
        self, *, organization_id: str, id_: str
    ) -> dict[str, Any] | None:
        """Get a Splash Theme Asset.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-splash-asset

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/splash/assets/{id_}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationSplashAsset", path=path
        )

    def delete_organization_splash_asset(self, *, organization_id: str, id_: str) -> None:
        """Delete a Splash Theme Asset.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-asset

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/splash/assets/{id_}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationSplashAsset", path=path
        )

    def get_organization_splash_themes(self, *, organization_id: str) -> dict[str, Any] | None:
        """List Splash Themes.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-splash-themes

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/splash/themes"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationSplashThemes", path=path
        )

    def create_organization_splash_theme(
        self, *, organization_id: str, name: str | None = None, base_theme: str | None = None
    ) -> dict[str, Any] | None:
        """Create a Splash Theme.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme

        Args:
            organization_id: Organization ID.
            name: theme name.
            base_theme: base theme id.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/splash/themes"

        payload = {}
        if name is not None:
            payload["name"] = name
        if base_theme is not None:
            payload["baseTheme"] = base_theme

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def delete_organization_splash_theme(self, *, organization_id: str, id_: str) -> None:
        """Delete a Splash Theme.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-theme

        Args:
            organization_id: Organization ID.
            id_: ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/organizations/{organization_id}/splash/themes/{id_}"

        return self._session.delete(
            scope="organizations", operation_id="deleteOrganizationSplashTheme", path=path
        )

    def create_organization_splash_theme_asset(
        self,
        *,
        organization_id: str,
        theme_identifier: str,
        name: str | None = None,
        content: str | None = None,
    ) -> dict[str, Any] | None:
        """Create a Splash Theme Asset.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme-asset

        Args:
            organization_id: Organization ID.
            theme_identifier: Theme identifier.
            name: File name. Will overwrite files with same name.
            content: a file containing the asset content.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        theme_identifier = urllib.parse.quote(str(theme_identifier), safe="")
        path = f"/organizations/{organization_id}/splash/themes/{theme_identifier}/assets"

        payload = {}
        if name is not None:
            payload["name"] = name
        if content is not None:
            payload["content"] = content

        return self._session.post(
            scope="organizations", operation_id="{operation_id}", path=path, json=payload
        )

    def get_organization_summary_top_appliances_by_utilization(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return the top 10 appliances sorted by utilization over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-appliances-by-utilization

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 25 minutes and be less than or
              equal to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/appliances/byUtilization"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_summary_top_applications_by_usage(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device: str | None = None,
        network_id: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return the top applications sorted by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-applications-by-usage

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device: Match result to an exact device tag.
            network_id: Match result to an exact network id.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 25 minutes and be less than or
              equal to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/applications/byUsage"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device is not None:
            params["device"] = device
        if network_id is not None:
            params["networkId"] = network_id
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_summary_top_applications_categories_by_usage(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        network_id: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return the top application categories sorted by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-applications-categories-by-usage

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            network_id: Match result to an exact network id.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 25 minutes and be less than or
              equal to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/applications/categories/byUsage"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if network_id is not None:
            params["networkId"] = network_id
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_summary_top_clients_by_usage(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 clients by data usage (in mb) over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-by-usage

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 8 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/clients/byUsage"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_summary_top_clients_manufacturers_by_usage(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-manufacturers-by-usage

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/clients/manufacturers/byUsage"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_summary_top_devices_by_usage(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 devices sorted by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-by-usage

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 8 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/devices/byUsage"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_summary_top_devices_models_by_usage(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 device models sorted by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-models-by-usage

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 8 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/devices/models/byUsage"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_summary_top_networks_by_status(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the client and status overview information for the networks in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-networks-by-status

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            per_page: The number of entries per page returned. Acceptable range is 3 - 5000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/networks/byStatus"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_summary_top_ssids_by_usage(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 ssids by data usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-ssids-by-usage

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 8 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/ssids/byUsage"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_summary_top_switches_by_energy_usage(
        self,
        *,
        organization_id: str,
        network_tag: str | None = None,
        device_tag: str | None = None,
        quantity: int | None = None,
        ssid_name: str | None = None,
        usage_uplink: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return metrics for organization's top 10 switches by energy usage over given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-switches-by-energy-usage

        Args:
            organization_id: Organization ID.
            network_tag: Match result to an exact network tag.
            device_tag: Match result to an exact device tag.
            quantity: Set number of desired results to return. Default is 10. Maximum is 50.
            ssid_name: Filter results by ssid name.
            usage_uplink: Filter results by usage uplink.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 25 minutes and be less than or
              equal to 186 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/summary/top/switches/byEnergyUsage"

        params = {}
        if network_tag is not None:
            params["networkTag"] = network_tag
        if device_tag is not None:
            params["deviceTag"] = device_tag
        if quantity is not None:
            params["quantity"] = quantity
        if ssid_name is not None:
            params["ssidName"] = ssid_name
        if usage_uplink is not None:
            params["usageUplink"] = usage_uplink
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_uplinks_statuses(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        iccids: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """List the uplink status of every Meraki MX, MG and Z series devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-uplinks-statuses

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: A list of network IDs. The returned devices will be filtered to only
              include these networks.
            serials: A list of serial numbers. The returned devices will be filtered to only include
              these serials.
            iccids: A list of ICCIDs. The returned devices will be filtered to only include these
              ICCIDs.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/uplinks/statuses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if iccids is not None:
            params["iccids[]"] = iccids

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_webhooks_alert_types(
        self, *, organization_id: str, product_type: str | None = None
    ) -> dict[str, Any] | None:
        """Return a list of alert types to be used with managing webhook alerts.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-alert-types

        Args:
            organization_id: Organization ID.
            product_type: Filter sample alerts to a specific product type.

        """
        if product_type is not None:
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
            assert product_type in options, (
                f'"product_type" cannot be "{product_type}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/webhooks/alertTypes"

        params = {}
        if product_type is not None:
            params["productType"] = product_type

        return self._session.get(
            scope="organizations", operation_id="{operation_id}", path=path, params=params
        )

    def get_organization_webhooks_callbacks_status(
        self, *, organization_id: str, callback_id: str
    ) -> dict[str, Any] | None:
        """Return the status of an API callback.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-callbacks-status

        Args:
            organization_id: Organization ID.
            callback_id: Callback ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        callback_id = urllib.parse.quote(str(callback_id), safe="")
        path = f"/organizations/{organization_id}/webhooks/callbacks/statuses/{callback_id}"

        return self._session.get(
            scope="organizations", operation_id="getOrganizationWebhooksCallbacksStatus", path=path
        )

    def get_organization_webhooks_logs(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        url: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Return the log of webhook POSTs sent.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-logs

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            url: The URL the webhook was sent to.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/webhooks/logs"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if url is not None:
            params["url"] = url

        return self._session.get_pages(
            scope="organizations",
            operation_id="{operation_id}",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )
