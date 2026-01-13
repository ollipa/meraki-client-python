"""ActionBatchOrganizations API endpoints."""

import urllib
from typing import Any


class ActionBatchOrganizations:
    """ActionBatchOrganizations class."""

    def __init__(self) -> None:
        pass

    def create_organization_adaptive_policy_acl(
        self, organization_id: str, name: str, rules: list, ipVersion: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/acls"

        body_params = [
            "name",
            "description",
            "rules",
            "ipVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_adaptive_policy_acl(
        self, organization_id: str, acl_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        acl_id = urllib.parse.quote(acl_id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}"

        body_params = [
            "name",
            "description",
            "rules",
            "ipVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_adaptive_policy_acl(
        self, organization_id: str, acl_id: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        acl_id = urllib.parse.quote(acl_id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_adaptive_policy_group(
        self, organization_id: str, name: str, sgt: int, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/groups"

        body_params = [
            "name",
            "sgt",
            "description",
            "policyObjects",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_adaptive_policy_group(
        self, organization_id: str, id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/groups/{id}"

        body_params = [
            "name",
            "sgt",
            "description",
            "policyObjects",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_adaptive_policy_group(
        self, organization_id: str, id: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/groups/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_adaptive_policy_policy(
        self, organization_id: str, sourceGroup: dict, destinationGroup: dict, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/policies"

        body_params = [
            "sourceGroup",
            "destinationGroup",
            "acls",
            "lastEntryRule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_adaptive_policy_policy(
        self, organization_id: str, id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/policies/{id}"

        body_params = [
            "sourceGroup",
            "destinationGroup",
            "acls",
            "lastEntryRule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_adaptive_policy_policy(
        self, organization_id: str, id: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/policies/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_adaptive_policy_settings(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/adaptivePolicy/settings"

        body_params = [
            "enabledNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_organization_alerts_profile(
        self,
        organization_id: str,
        type: str,
        alertCondition: dict,
        recipients: dict,
        networkTags: list,
        **kwargs: Any,
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/alerts/profiles"

        body_params = [
            "type",
            "alertCondition",
            "recipients",
            "networkTags",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_alerts_profile(
        self, organization_id: str, alert_config_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        alert_config_id = urllib.parse.quote(alert_config_id, safe="")
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
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_alerts_profile(
        self, organization_id: str, alert_config_id: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        alert_config_id = urllib.parse.quote(alert_config_id, safe="")
        resource = f"/organizations/{organization_id}/alerts/profiles/{alert_config_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_branding_policy(
        self, organization_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies"

        body_params = [
            "name",
            "enabled",
            "adminSettings",
            "helpSettings",
            "customLogo",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_branding_policies_priorities(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies/priorities"

        body_params = [
            "brandingPolicyIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_branding_policy(
        self, organization_id: str, branding_policy_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        branding_policy_id = urllib.parse.quote(branding_policy_id, safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies/{branding_policy_id}"

        body_params = [
            "name",
            "enabled",
            "adminSettings",
            "helpSettings",
            "customLogo",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_branding_policy(
        self, organization_id: str, branding_policy_id: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        branding_policy_id = urllib.parse.quote(branding_policy_id, safe="")
        resource = f"/organizations/{organization_id}/brandingPolicies/{branding_policy_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_config_template(
        self, organization_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/configTemplates"

        body_params = [
            "name",
            "timeZone",
            "copyFromNetworkId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_config_template(
        self, organization_id: str, config_template_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        config_template_id = urllib.parse.quote(config_template_id, safe="")
        resource = f"/organizations/{organization_id}/configTemplates/{config_template_id}"

        body_params = [
            "name",
            "timeZone",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_organization_devices_controller_migration(
        self, organization_id: str, serials: list, target: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/devices/controller/migrations"

        body_params = [
            "serials",
            "target",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def bulk_update_organization_devices_details(
        self, organization_id: str, serials: list, details: list
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/devices/details/bulkUpdate"

        body_params = [
            "serials",
            "details",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def bulk_organization_devices_packet_capture_captures_delete(
        self, organization_id: str, captureIds: list
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/captures/bulkDelete"

        body_params = [
            "captureIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_organization_devices_packet_capture_capture(
        self, organization_id: str, capture_id: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        capture_id = urllib.parse.quote(capture_id, safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/captures/{capture_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_devices_packet_capture_schedule(
        self, organization_id: str, devices: list, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
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
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def reorder_organization_devices_packet_capture_schedules(
        self, organization_id: str, order: list
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/schedules/reorder"

        body_params = [
            "order",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_devices_packet_capture_schedule(
        self, organization_id: str, schedule_id: str, devices: list, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        schedule_id = urllib.parse.quote(schedule_id, safe="")
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
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_devices_packet_capture_schedule(
        self, organization_id: str, scheduleId: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/devices/packetCapture/schedules/{scheduleId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_early_access_features_opt_in(
        self, organization_id: str, opt_in_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        opt_in_id = urllib.parse.quote(opt_in_id, safe="")
        resource = f"/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}"

        body_params = [
            "limitScopeToNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def disable_organization_integrations_xdr_networks(
        self, organization_id: str, networks: list
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/integrations/xdr/networks/disable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def enable_organization_integrations_xdr_networks(
        self, organization_id: str, networks: list
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/integrations/xdr/networks/enable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def claim_organization_inventory_orders(
        self, organization_id: str, claimId: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/inventory/orders/claim"

        body_params = [
            "claimId",
            "subscriptions",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def assign_organization_licenses_seats(
        self, organization_id: str, licenseId: str, networkId: str, seatCount: int
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/licenses/assignSeats"

        body_params = [
            "licenseId",
            "networkId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def move_organization_licenses(
        self, organization_id: str, destOrganizationId: str, licenseIds: list
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/licenses/move"

        body_params = [
            "destOrganizationId",
            "licenseIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def move_organization_licenses_seats(
        self, organization_id: str, destOrganizationId: str, licenseId: str, seatCount: int
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/licenses/moveSeats"

        body_params = [
            "destOrganizationId",
            "licenseId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def renew_organization_licenses_seats(
        self, organization_id: str, licenseIdToRenew: str, unusedLicenseId: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/licenses/renewSeats"

        body_params = [
            "licenseIdToRenew",
            "unusedLicenseId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_license(
        self, organization_id: str, license_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        license_id = urllib.parse.quote(license_id, safe="")
        resource = f"/organizations/{organization_id}/licenses/{license_id}"

        body_params = [
            "deviceSerial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_login_security(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
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
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_organization_network(
        self, organization_id: str, name: str, productTypes: list, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
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
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def combine_organization_networks(
        self, organization_id: str, name: str, networkIds: list, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/networks/combine"

        body_params = [
            "name",
            "networkIds",
            "enrollmentString",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_organization_policy_object(
        self, organization_id: str, name: str, category: str, type: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
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
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_organization_policy_objects_group(
        self, organization_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/policyObjects/groups"

        body_params = [
            "name",
            "category",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_policy_objects_group(
        self, organization_id: str, policy_object_group_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        policy_object_group_id = urllib.parse.quote(policy_object_group_id, safe="")
        resource = f"/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}"

        body_params = [
            "name",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_policy_objects_group(
        self, organization_id: str, policy_object_group_id: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        policy_object_group_id = urllib.parse.quote(policy_object_group_id, safe="")
        resource = f"/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_policy_object(
        self, organization_id: str, policy_object_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        policy_object_id = urllib.parse.quote(policy_object_id, safe="")
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
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_policy_object(
        self, organization_id: str, policy_object_id: str
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        policy_object_id = urllib.parse.quote(policy_object_id, safe="")
        resource = f"/organizations/{organization_id}/policyObjects/{policy_object_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_saml_idp(
        self, organization_id: str, x509certSha1Fingerprint: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/saml/idps"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_saml_idp(
        self, organization_id: str, idp_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        idp_id = urllib.parse.quote(idp_id, safe="")
        resource = f"/organizations/{organization_id}/saml/idps/{idp_id}"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_saml_idp(self, organization_id: str, idp_id: str) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        idp_id = urllib.parse.quote(idp_id, safe="")
        resource = f"/organizations/{organization_id}/saml/idps/{idp_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def delete_organization_splash_asset(self, organization_id: str, id: str) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organization_id}/splash/assets/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_splash_theme(
        self, organization_id: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/splash/themes"

        body_params = [
            "name",
            "baseTheme",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_organization_splash_theme(self, organization_id: str, id: str) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organization_id}/splash/themes/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_splash_theme_asset(
        self, organization_id: str, theme_identifier: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        theme_identifier = urllib.parse.quote(theme_identifier, safe="")
        resource = f"/organizations/{organization_id}/splash/themes/{theme_identifier}/assets"

        body_params = [
            "name",
            "content",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action
