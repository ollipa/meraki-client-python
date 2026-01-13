"""ActionBatchOrganizations API endpoints."""

import urllib
from typing import Any


class ActionBatchOrganizations:
    """ActionBatchOrganizations class."""

    def __init__(self) -> None:
        pass

    def create_organization_adaptive_policy_acl(
        self, organizationId: str, name: str, rules: list, ipVersion: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Creates new adaptive policy ACL.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-acl

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls"

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
        self, organizationId: str, aclId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates an adaptive policy ACL.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-acl

        Args:
            organizationId: Organization ID.
            aclId: Acl ID.
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
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls/{aclId}"

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
        self, organizationId: str, aclId: str
    ) -> dict[str, Any]:
        """Deletes the specified adaptive policy ACL.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-acl

        Args:
            organizationId: Organization ID.
            aclId: Acl ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "delete_organization_adaptive_policy_acl",
        }
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls/{aclId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_adaptive_policy_group(
        self, organizationId: str, name: str, sgt: int, **kwargs: Any
    ) -> dict[str, Any]:
        """Creates a new adaptive policy group.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-group

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups"

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
        self, organizationId: str, id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates an adaptive policy group.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-group

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups/{id}"

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
        self, organizationId: str, id: str
    ) -> dict[str, Any]:
        """Deletes the specified adaptive policy group and any associated policies and references.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-group

        Args:
            organizationId: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "delete_organization_adaptive_policy_group",
        }
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_adaptive_policy_policy(
        self, organizationId: str, sourceGroup: dict, destinationGroup: dict, **kwargs: Any
    ) -> dict[str, Any]:
        """Add an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-policy

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies"

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
        self, organizationId: str, id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-policy

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies/{id}"

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
        self, organizationId: str, id: str
    ) -> dict[str, Any]:
        """Delete an Adaptive Policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-policy

        Args:
            organizationId: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "delete_organization_adaptive_policy_policy",
        }
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_adaptive_policy_settings(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update global adaptive policy settings.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-settings

        Args:
            organizationId: Organization ID.
            enabledNetworks: List of network IDs with adaptive policy enabled.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "settings"],
            "operation": "update_organization_adaptive_policy_settings",
        }
        resource = f"/organizations/{organizationId}/adaptivePolicy/settings"

        body_params = [
            "enabledNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_organization_alerts_profile(
        self,
        organizationId: str,
        type: str,
        alertCondition: dict,
        recipients: dict,
        networkTags: list,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create an organization-wide alert configuration.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-alerts-profile

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/alerts/profiles"

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
        self, organizationId: str, alertConfigId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update an organization-wide alert config.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-alerts-profile

        Args:
            organizationId: Organization ID.
            alertConfigId: Alert config ID.
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
        resource = f"/organizations/{organizationId}/alerts/profiles/{alertConfigId}"

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
        self, organizationId: str, alertConfigId: str
    ) -> dict[str, Any]:
        """Removes an organization-wide alert config.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-alerts-profile

        Args:
            organizationId: Organization ID.
            alertConfigId: Alert config ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "delete_organization_alerts_profile",
        }
        resource = f"/organizations/{organizationId}/alerts/profiles/{alertConfigId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_branding_policy(
        self, organizationId: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Add a new branding policy to an organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/brandingPolicies"

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
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the priority ordering of an organization's branding policies.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

        Args:
            organizationId: Organization ID.
            brandingPolicyIds:       An ordered list of branding policy IDs that determines the
              priority order of how to apply the policies .

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies", "priorities"],
            "operation": "update_organization_branding_policies_priorities",
        }
        resource = f"/organizations/{organizationId}/brandingPolicies/priorities"

        body_params = [
            "brandingPolicyIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_branding_policy(
        self, organizationId: str, brandingPolicyId: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a branding policy.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

        Args:
            organizationId: Organization ID.
            brandingPolicyId: Branding policy ID.
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
        resource = f"/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}"

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
        self, organizationId: str, brandingPolicyId: str
    ) -> dict[str, Any]:
        """Delete a branding policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

        Args:
            organizationId: Organization ID.
            brandingPolicyId: Branding policy ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "delete_organization_branding_policy",
        }
        resource = f"/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_config_template(
        self, organizationId: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new configuration template.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/configTemplates"

        body_params = [
            "name",
            "timeZone",
            "copyFromNetworkId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_config_template(
        self, organizationId: str, configTemplateId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a configuration template.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

        Args:
            organizationId: Organization ID.
            configTemplateId: Config template ID.
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
        resource = f"/organizations/{organizationId}/configTemplates/{configTemplateId}"

        body_params = [
            "name",
            "timeZone",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_organization_devices_controller_migration(
        self, organizationId: str, serials: list, target: str
    ) -> dict[str, Any]:
        """Migrate devices to another controller or management mode.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-controller-migration

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/devices/controller/migrations"

        body_params = [
            "serials",
            "target",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def bulk_update_organization_devices_details(
        self, organizationId: str, serials: list, details: list
    ) -> dict[str, Any]:
        """Updating device details (currently only used for Catalyst devices).

        https://developer.cisco.com/meraki/api-v1/#!bulk-update-organization-devices-details

        Args:
            organizationId: Organization ID.
            serials: A list of serials of devices to update.
            details: An array of details.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "details", "bulkUpdate"],
            "operation": "bulk_update_organization_devices_details",
        }
        resource = f"/organizations/{organizationId}/devices/details/bulkUpdate"

        body_params = [
            "serials",
            "details",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def bulk_organization_devices_packet_capture_captures_delete(
        self, organizationId: str, captureIds: list
    ) -> dict[str, Any]:
        """BulkDelete packet captures from cloud.

        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-delete

        Args:
            organizationId: Organization ID.
            captureIds: Delete the packet captures of the specified capture ids.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "bulk_organization_devices_packet_capture_captures_delete",
        }
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/bulkDelete"

        body_params = [
            "captureIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_organization_devices_packet_capture_capture(
        self, organizationId: str, captureId: str
    ) -> dict[str, Any]:
        """Delete a single packet capture from cloud using captureId.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-capture

        Args:
            organizationId: Organization ID.
            captureId: Capture ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "delete_organization_devices_packet_capture_capture",
        }
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/{captureId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_devices_packet_capture_schedule(
        self, organizationId: str, devices: list, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a schedule for packet capture.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-schedule

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules"

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
        self, organizationId: str, order: list
    ) -> dict[str, Any]:
        """Bulk update priorities of pcap schedules.

        https://developer.cisco.com/meraki/api-v1/#!reorder-organization-devices-packet-capture-schedules

        Args:
            organizationId: Organization ID.
            order: Array of schedule IDs and their priorities to reorder.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "reorder_organization_devices_packet_capture_schedules",
        }
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/reorder"

        body_params = [
            "order",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_devices_packet_capture_schedule(
        self, organizationId: str, scheduleId: str, devices: list, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a schedule for packet capture.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-devices-packet-capture-schedule

        Args:
            organizationId: Organization ID.
            scheduleId: Schedule ID.
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
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/{scheduleId}"

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
        self, organizationId: str, scheduleId: str
    ) -> dict[str, Any]:
        """Delete schedule from cloud.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-schedule

        Args:
            organizationId: Organization ID.
            scheduleId: Delete the capture schedules of the specified capture schedule id.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "delete_organization_devices_packet_capture_schedule",
        }
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/{scheduleId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_early_access_features_opt_in(
        self, organizationId: str, optInId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update an early access feature opt-in for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-early-access-features-opt-in

        Args:
            organizationId: Organization ID.
            optInId: Opt in ID.
            limitScopeToNetworks: A list of network IDs to apply the opt-in to.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "update_organization_early_access_features_opt_in",
        }
        resource = f"/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}"

        body_params = [
            "limitScopeToNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def disable_organization_integrations_xdr_networks(
        self, organizationId: str, networks: list
    ) -> dict[str, Any]:
        """Disable XDR on networks.

        https://developer.cisco.com/meraki/api-v1/#!disable-organization-integrations-xdr-networks

        Args:
            organizationId: Organization ID.
            networks: List containing the network ID and the product type to disable XDR on.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "integrations", "xdr", "networks"],
            "operation": "disable_organization_integrations_xdr_networks",
        }
        resource = f"/organizations/{organizationId}/integrations/xdr/networks/disable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def enable_organization_integrations_xdr_networks(
        self, organizationId: str, networks: list
    ) -> dict[str, Any]:
        """Enable XDR on networks.

        https://developer.cisco.com/meraki/api-v1/#!enable-organization-integrations-xdr-networks

        Args:
            organizationId: Organization ID.
            networks: List containing the network ID and the product type to enable XDR on.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "integrations", "xdr", "networks"],
            "operation": "enable_organization_integrations_xdr_networks",
        }
        resource = f"/organizations/{organizationId}/integrations/xdr/networks/enable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def claim_organization_inventory_orders(
        self, organizationId: str, claimId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Claim an order by the secure unique order claim number, the order claim id.

        https://developer.cisco.com/meraki/api-v1/#!claim-organization-inventory-orders

        Args:
            organizationId: Organization ID.
            claimId: The unique order claim id.
            subscriptions: The individual subscriptions to claim.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "inventory", "orders"],
            "operation": "claim_organization_inventory_orders",
        }
        resource = f"/organizations/{organizationId}/inventory/orders/claim"

        body_params = [
            "claimId",
            "subscriptions",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def assign_organization_licenses_seats(
        self, organizationId: str, licenseId: str, networkId: str, seatCount: int
    ) -> dict[str, Any]:
        """Assign SM seats to a network.

        https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/licenses/assignSeats"

        body_params = [
            "licenseId",
            "networkId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def move_organization_licenses(
        self, organizationId: str, destOrganizationId: str, licenseIds: list
    ) -> dict[str, Any]:
        """Move licenses to another organization.

        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

        Args:
            organizationId: Organization ID.
            destOrganizationId: The ID of the organization to move the licenses to.
            licenseIds: A list of IDs of licenses to move to the new organization.

        """
        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "move_organization_licenses",
        }
        resource = f"/organizations/{organizationId}/licenses/move"

        body_params = [
            "destOrganizationId",
            "licenseIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def move_organization_licenses_seats(
        self, organizationId: str, destOrganizationId: str, licenseId: str, seatCount: int
    ) -> dict[str, Any]:
        """Move SM seats to another organization.

        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/licenses/moveSeats"

        body_params = [
            "destOrganizationId",
            "licenseId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def renew_organization_licenses_seats(
        self, organizationId: str, licenseIdToRenew: str, unusedLicenseId: str
    ) -> dict[str, Any]:
        """Renew SM seats of a license.

        https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/licenses/renewSeats"

        body_params = [
            "licenseIdToRenew",
            "unusedLicenseId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_license(
        self, organizationId: str, licenseId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a license.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-license

        Args:
            organizationId: Organization ID.
            licenseId: License ID.
            deviceSerial: The serial number of the device to assign this license to. Set this to
              null to unassign the license. If a different license is already active on
              the device, this parameter will control queueing/dequeuing this license.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "update_organization_license",
        }
        resource = f"/organizations/{organizationId}/licenses/{licenseId}"

        body_params = [
            "deviceSerial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_login_security(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the login security settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/loginSecurity"

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
        self, organizationId: str, name: str, productTypes: list, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a network.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-network

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/networks"

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
        self, organizationId: str, name: str, networkIds: list, **kwargs: Any
    ) -> dict[str, Any]:
        """Combine multiple networks into a single network.

        https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/networks/combine"

        body_params = [
            "name",
            "networkIds",
            "enrollmentString",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_organization_policy_object(
        self, organizationId: str, name: str, category: str, type: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Creates a new Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-object

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/policyObjects"

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
        self, organizationId: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Creates a new Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-objects-group

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/policyObjects/groups"

        body_params = [
            "name",
            "category",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_policy_objects_group(
        self, organizationId: str, policyObjectGroupId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates a Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-objects-group

        Args:
            organizationId: Organization ID.
            policyObjectGroupId: Policy object group ID.
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
        resource = f"/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}"

        body_params = [
            "name",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_policy_objects_group(
        self, organizationId: str, policyObjectGroupId: str
    ) -> dict[str, Any]:
        """Deletes a Policy Object Group.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-objects-group

        Args:
            organizationId: Organization ID.
            policyObjectGroupId: Policy object group ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "delete_organization_policy_objects_group",
        }
        resource = f"/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_policy_object(
        self, organizationId: str, policyObjectId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates a Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-object

        Args:
            organizationId: Organization ID.
            policyObjectId: Policy object ID.
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
        resource = f"/organizations/{organizationId}/policyObjects/{policyObjectId}"

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
        self, organizationId: str, policyObjectId: str
    ) -> dict[str, Any]:
        """Deletes a Policy Object.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-object

        Args:
            organizationId: Organization ID.
            policyObjectId: Policy object ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "delete_organization_policy_object",
        }
        resource = f"/organizations/{organizationId}/policyObjects/{policyObjectId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_saml_idp(
        self, organizationId: str, x509certSha1Fingerprint: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a SAML IdP for your organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

        Args:
            organizationId: Organization ID.
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
        resource = f"/organizations/{organizationId}/saml/idps"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_saml_idp(
        self, organizationId: str, idpId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a SAML IdP in your organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

        Args:
            organizationId: Organization ID.
            idpId: Idp ID.
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
        resource = f"/organizations/{organizationId}/saml/idps/{idpId}"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_saml_idp(self, organizationId: str, idpId: str) -> dict[str, Any]:
        """Remove a SAML IdP in your organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

        Args:
            organizationId: Organization ID.
            idpId: Idp ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "delete_organization_saml_idp",
        }
        resource = f"/organizations/{organizationId}/saml/idps/{idpId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def delete_organization_splash_asset(self, organizationId: str, id: str) -> dict[str, Any]:
        """Delete a Splash Theme Asset.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-asset

        Args:
            organizationId: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "splash", "assets"],
            "operation": "delete_organization_splash_asset",
        }
        resource = f"/organizations/{organizationId}/splash/assets/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_splash_theme(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a Splash Theme.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme

        Args:
            organizationId: Organization ID.
            name: theme name.
            baseTheme: base theme id .

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "splash", "themes"],
            "operation": "create_organization_splash_theme",
        }
        resource = f"/organizations/{organizationId}/splash/themes"

        body_params = [
            "name",
            "baseTheme",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_organization_splash_theme(self, organizationId: str, id: str) -> dict[str, Any]:
        """Delete a Splash Theme.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-theme

        Args:
            organizationId: Organization ID.
            id: ID.

        """
        metadata = {
            "tags": ["organizations", "configure", "splash", "themes"],
            "operation": "delete_organization_splash_theme",
        }
        resource = f"/organizations/{organizationId}/splash/themes/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_splash_theme_asset(
        self, organizationId: str, themeIdentifier: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a Splash Theme Asset.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme-asset

        Args:
            organizationId: Organization ID.
            themeIdentifier: Theme identifier.
            name: File name. Will overwrite files with same name.
            content: a file containing the asset content.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "splash", "themes", "assets"],
            "operation": "create_organization_splash_theme_asset",
        }
        resource = f"/organizations/{organizationId}/splash/themes/{themeIdentifier}/assets"

        body_params = [
            "name",
            "content",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action
