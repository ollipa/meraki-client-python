"""ActionBatchNetworks API endpoints."""

import urllib
from typing import Any


class ActionBatchNetworks:
    """ActionBatchNetworks class."""

    def __init__(self) -> None:
        pass

    def update_network(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network

        Args:
            network_id: Network ID.
            name: The name of the network.
            timeZone: The timezone of the network. For a list of allowed timezones, please see the
              'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article.</a>.
            tags: A list of tags to be applied to the network.
            enrollmentString: A unique identifier which can be used for device enrollment or easy
              access through the Meraki SM Registration page or the Self Service Portal.
              Please note that changing this field may cause existing bookmarks to
              break.
            notes: Add any notes or additional information about this network here.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "update_network"}
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}"

        body_params = [
            "name",
            "timeZone",
            "tags",
            "enrollmentString",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network(self, network_id: str) -> dict[str, Any]:
        """Delete a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "delete_network"}
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def bind_network(self, network_id: str, configTemplateId: str, **kwargs: Any) -> dict[str, Any]:
        """Bind a network to a template.

        https://developer.cisco.com/meraki/api-v1/#!bind-network

        Args:
            network_id: Network ID.
            configTemplateId: The ID of the template to which the network should be bound.
            autoBind: Optional boolean indicating whether the network's switches should
              automatically bind to profiles of the same model. Defaults to false if
              left unspecified. This option only affects switch networks and switch
              templates. Auto-bind is not valid unless the switch template has at least
              one profile and has at most one profile per switch model.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "bind_network"}
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/bind"

        body_params = [
            "configTemplateId",
            "autoBind",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def provision_network_clients(
        self, network_id: str, clients: list, devicePolicy: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Provisions a client with a name and policy.

        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        Args:
            network_id: Network ID.
            clients: The array of clients to provision.
            devicePolicy: The policy to apply to the specified client. Can be 'Group policy',
              'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
            groupPolicyId: The ID of the desired group policy to apply to the client. Required if
              'devicePolicy' is set to "Group policy". Otherwise this is ignored.
            policiesBySecurityAppliance: An object, describing what the policy-connection
              association is for the security appliance. (Only relevant if the security
              appliance is actually within the network).
            policiesBySsid: An object, describing the policy-connection associations for each active
              SSID within the network. Keys should be the number of enabled SSIDs,
              mapping to an object describing the client's policy.

        """
        kwargs.update(locals())

        if "devicePolicy" in kwargs:
            options = ["Allowed", "Blocked", "Group policy", "Normal", "Per connection"]
            assert kwargs["devicePolicy"] in options, (
                f'''"devicePolicy" cannot be "{kwargs["devicePolicy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "clients"],
            "operation": "provision_network_clients",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/clients/provision"

        body_params = [
            "clients",
            "devicePolicy",
            "groupPolicyId",
            "policiesBySecurityAppliance",
            "policiesBySsid",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def claim_network_devices(
        self, network_id: str, serials: list, **kwargs: Any
    ) -> dict[str, Any]:
        """Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed).

        https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

        Args:
            network_id: Network ID.
            serials: A list of serials of devices to claim.
            addAtomically: Whether to claim devices atomically. If true, all devices will be claimed
              or none will be claimed. Default is true.
            detailsByDevice: Optional details for claimed devices (currently only used for Catalyst
              devices).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "claim_network_devices",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/devices/claim"

        body_params = [
            "serials",
            "detailsByDevice",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def vmx_network_devices_claim(self, network_id: str, size: str) -> dict[str, Any]:
        """Claim a vMX into a network.

        https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim

        Args:
            network_id: Network ID.
            size: The size of the vMX you claim. It can be one of: small, medium, large, xlarge,
              100.

        """
        kwargs = locals()

        if "size" in kwargs:
            options = ["100", "large", "medium", "small", "xlarge"]
            assert kwargs["size"] in options, (
                f'''"size" cannot be "{kwargs["size"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "devices", "claim"],
            "operation": "vmx_network_devices_claim",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/devices/claim/vmx"

        body_params = [
            "size",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def remove_network_devices(self, network_id: str, serial: str) -> dict[str, Any]:
        """Remove a single device.

        https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

        Args:
            network_id: Network ID.
            serial: The serial of a device.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "remove_network_devices",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/devices/remove"

        body_params = [
            "serial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_firmware_upgrades(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update firmware upgrade information for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

        Args:
            network_id: Network ID.
            upgradeWindow: Upgrade window for devices in network.
            timezone: The timezone for the network.
            products: Contains information about the network to update.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades"],
            "operation": "update_network_firmware_upgrades",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades"

        body_params = [
            "upgradeWindow",
            "timezone",
            "products",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_firmware_upgrades_rollback(
        self, network_id: str, reasons: list, **kwargs: Any
    ) -> dict[str, Any]:
        """Rollback a Firmware Upgrade For A Network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

        Args:
            network_id: Network ID.
            reasons: Reasons for the rollback.
            product: Product type to rollback (if the network is a combined network).
            time: Scheduled time for the rollback.
            toVersion: Version to downgrade to (if the network has firmware flexibility).

        """
        kwargs.update(locals())

        if "product" in kwargs:
            options = [
                "appliance",
                "camera",
                "cellularGateway",
                "secureConnect",
                "switch",
                "switchCatalyst",
                "wireless",
                "wirelessController",
            ]
            assert kwargs["product"] in options, (
                f'''"product" cannot be "{kwargs["product"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "rollbacks"],
            "operation": "create_network_firmware_upgrades_rollback",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/rollbacks"

        body_params = [
            "product",
            "time",
            "reasons",
            "toVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_network_firmware_upgrades_staged_group(
        self, network_id: str, name: str, isDefault: bool, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a Staged Upgrade Group for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            name: Name of the Staged Upgrade Group. Length must be 1 to 255 characters.
            isDefault: Boolean indicating the default Group. Any device that does not have a group
              explicitly assigned will upgrade with this group.
            description: Description of the Staged Upgrade Group. Length must be 1 to 255
              characters.
            assignedDevices: The devices and Switch Stacks assigned to the Group.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "create_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups"

        body_params = [
            "name",
            "description",
            "isDefault",
            "assignedDevices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_network_firmware_upgrades_staged_group(
        self, network_id: str, group_id: str
    ) -> dict[str, Any]:
        """Delete a Staged Upgrade Group.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            group_id: Group ID.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "delete_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        group_id = urllib.parse.quote(group_id, safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def batch_network_floor_plans_auto_locate_jobs(
        self, network_id: str, jobs: list
    ) -> dict[str, Any]:
        """Schedule auto locate jobs for one or more floor plans in a network.

        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-auto-locate-jobs

        Args:
            network_id: Network ID.
            jobs: The list of auto locate jobs to be scheduled. Up to 100 jobs can be provided in a
              request.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "batch_network_floor_plans_auto_locate_jobs",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/batch"

        body_params = [
            "jobs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def cancel_network_floor_plans_auto_locate_job(
        self, network_id: str, job_id: str
    ) -> dict[str, Any]:
        """Cancel a scheduled or running auto locate job.

        https://developer.cisco.com/meraki/api-v1/#!cancel-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "cancel_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        job_id = urllib.parse.quote(job_id, safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/cancel"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action

    def publish_network_floor_plans_auto_locate_job(
        self, network_id: str, job_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the status of a finished auto locate job to be published, and update device locations.

        https://developer.cisco.com/meraki/api-v1/#!publish-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.
            devices: The list of devices to publish positions for.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "publish_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        job_id = urllib.parse.quote(job_id, safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/publish"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def recalculate_network_floor_plans_auto_locate_job(
        self, network_id: str, job_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Trigger auto locate recalculation for a job, and optionally set anchors.

        https://developer.cisco.com/meraki/api-v1/#!recalculate-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.
            devices: The list of devices to update anchor positions for.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "recalculate_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        job_id = urllib.parse.quote(job_id, safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/recalculate"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def batch_network_floor_plans_devices_update(
        self, network_id: str, assignments: list
    ) -> dict[str, Any]:
        """Update floorplan assignments for a batch of devices.

        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-devices-update

        Args:
            network_id: Network ID.
            assignments: List of floorplan assignments to update. Up to 100 floor plan assignments
              can be provided in a request.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "devices"],
            "operation": "batch_network_floor_plans_devices_update",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/floorPlans/devices/batchUpdate"

        body_params = [
            "assignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_floor_plan(
        self, network_id: str, floor_plan_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a floor plan's geolocation and other meta data.

        https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

        Args:
            network_id: Network ID.
            floor_plan_id: Floor plan ID.
            name: The name of your floor plan.
            center: The longitude and latitude of the center of your floor plan. If you want to
              change the geolocation data of your floor plan, either the 'center' or two
              adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be
              specified. If 'center' is specified, the floor plan is placed over that
              point with no rotation. If two adjacent corners are specified, the floor
              plan is rotated to line up with the two specified points. The aspect ratio
              of the floor plan's image is preserved regardless of which corners/center
              are specified. (This means if that more than two corners are specified,
              only two corners may be used to preserve the floor plan's aspect ratio.).
              No two points can have the same latitude, longitude pair.
            bottomLeftCorner: The longitude and latitude of the bottom left corner of your floor
              plan.
            bottomRightCorner: The longitude and latitude of the bottom right corner of your floor
              plan.
            topLeftCorner: The longitude and latitude of the top left corner of your floor plan.
            topRightCorner: The longitude and latitude of the top right corner of your floor plan.
            floorNumber: The floor number of the floors within the building.
            imageContents: The file contents (a base 64 encoded string) of your new image. Supported
              formats are PNG, GIF, and JPG. Note that all images are saved as PNG
              files, regardless of the format they are uploaded in. If you upload a new
              image, and you do NOT specify any new geolocation fields ('center,
              'topLeftCorner', etc), the floor plan will be recentered with no rotation
              in order to maintain the aspect ratio of your new image.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "update_network_floor_plan",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        floor_plan_id = urllib.parse.quote(floor_plan_id, safe="")
        resource = f"/networks/{network_id}/floorPlans/{floor_plan_id}"

        body_params = [
            "name",
            "center",
            "bottomLeftCorner",
            "bottomRightCorner",
            "topLeftCorner",
            "topRightCorner",
            "floorNumber",
            "imageContents",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_floor_plan(self, network_id: str, floor_plan_id: str) -> dict[str, Any]:
        """Destroy a floor plan.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

        Args:
            network_id: Network ID.
            floor_plan_id: Floor plan ID.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "delete_network_floor_plan",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        floor_plan_id = urllib.parse.quote(floor_plan_id, safe="")
        resource = f"/networks/{network_id}/floorPlans/{floor_plan_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_group_policy(
        self, network_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a group policy.

                https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

                Args:
                    network_id: Network ID.
                    name: The name for your group policy. Required.
                    scheduling:     The schedule for the group policy. Schedules are applied to days of the
                      week. .
                    bandwidth:     The bandwidth settings for clients bound to your group policy.
        .
                    firewallAndTrafficShaping:     The firewall and traffic shaping rules and settings for
                      your policy. .
                    contentFiltering: The content filtering settings for your group policy.
                    splashAuthSettings: Whether clients bound to your policy will bypass splash
                      authorization or behave according to the network's rules. Can be one of
                      'network default' or 'bypass'. Only available if your network has a
                      wireless configuration.
                    vlanTagging: The VLAN tagging settings for your group policy. Only available if your
                      network has a wireless configuration.
                    bonjourForwarding: The Bonjour settings for your group policy. Only valid if your
                      network has a wireless configuration.

        """
        kwargs.update(locals())

        if "splashAuthSettings" in kwargs:
            options = ["bypass", "network default"]
            assert kwargs["splashAuthSettings"] in options, (
                f'''"splashAuthSettings" cannot be "{kwargs["splashAuthSettings"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "create_network_group_policy",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/groupPolicies"

        body_params = [
            "name",
            "scheduling",
            "bandwidth",
            "firewallAndTrafficShaping",
            "contentFiltering",
            "splashAuthSettings",
            "vlanTagging",
            "bonjourForwarding",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_group_policy(
        self, network_id: str, group_policy_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a group policy.

                https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

                Args:
                    network_id: Network ID.
                    group_policy_id: Group policy ID.
                    name: The name for your group policy.
                    scheduling:     The schedule for the group policy. Schedules are applied to days of the
                      week. .
                    bandwidth:     The bandwidth settings for clients bound to your group policy.
        .
                    firewallAndTrafficShaping:     The firewall and traffic shaping rules and settings for
                      your policy. .
                    contentFiltering: The content filtering settings for your group policy.
                    splashAuthSettings: Whether clients bound to your policy will bypass splash
                      authorization or behave according to the network's rules. Can be one of
                      'network default' or 'bypass'. Only available if your network has a
                      wireless configuration.
                    vlanTagging: The VLAN tagging settings for your group policy. Only available if your
                      network has a wireless configuration.
                    bonjourForwarding: The Bonjour settings for your group policy. Only valid if your
                      network has a wireless configuration.

        """
        kwargs.update(locals())

        if "splashAuthSettings" in kwargs:
            options = ["bypass", "network default"]
            assert kwargs["splashAuthSettings"] in options, (
                f'''"splashAuthSettings" cannot be "{kwargs["splashAuthSettings"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "update_network_group_policy",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        group_policy_id = urllib.parse.quote(group_policy_id, safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        body_params = [
            "name",
            "scheduling",
            "bandwidth",
            "firewallAndTrafficShaping",
            "contentFiltering",
            "splashAuthSettings",
            "vlanTagging",
            "bonjourForwarding",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_group_policy(
        self, network_id: str, group_policy_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Delete a group policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

        Args:
            network_id: Network ID.
            group_policy_id: Group policy ID.
            force: If true, the system deletes the GP even if there are active clients using the GP.
              After deletion, active clients that were assigned to that Group Policy
              will be left without any policy applied. Default is false.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "delete_network_group_policy",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        group_policy_id = urllib.parse.quote(group_policy_id, safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_meraki_auth_user(
        self, network_id: str, email: str, authorizations: list, **kwargs: Any
    ) -> dict[str, Any]:
        """Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap).

        https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

        Args:
            network_id: Network ID.
            email: Email address of the user.
            authorizations: Authorization zones and expiration dates for the user.
            name: Name of the user. Only required If the user is not a Dashboard administrator.
            password: The password for this user account. Only required If the user is not a
              Dashboard administrator.
            accountType: Authorization type for user. Can be 'Guest' or '802.1X' for wireless
              networks, or 'Client VPN' for MX networks. Defaults to '802.1X'.
            emailPasswordToUser: Whether or not Meraki should email the password to user. Default is
              false.
            isAdmin: Whether or not the user is a Dashboard administrator.

        """
        kwargs.update(locals())

        if "accountType" in kwargs:
            options = ["802.1X", "Client VPN", "Guest"]
            assert kwargs["accountType"] in options, (
                f'''"accountType" cannot be "{kwargs["accountType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "create_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers"

        body_params = [
            "email",
            "name",
            "password",
            "accountType",
            "emailPasswordToUser",
            "isAdmin",
            "authorizations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_network_meraki_auth_user(
        self, network_id: str, meraki_auth_user_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Delete an 802.1X RADIUS user, or deauthorize and optionally delete a splash guest or client VPN user.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

        Args:
            network_id: Network ID.
            meraki_auth_user_id: Meraki auth user ID.
            delete: If the ID supplied is for a splash guest or client VPN user, and that user is
              not authorized for any other networks in the organization, then also
              delete the user. 802.1X RADIUS users are always deleted regardless of this
              optional attribute.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "delete_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        meraki_auth_user_id = urllib.parse.quote(meraki_auth_user_id, safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_meraki_auth_user(
        self, network_id: str, meraki_auth_user_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated).

        https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

        Args:
            network_id: Network ID.
            meraki_auth_user_id: Meraki auth user ID.
            name: Name of the user. Only allowed If the user is not Dashboard administrator.
            password: The password for this user account. Only allowed If the user is not Dashboard
              administrator.
            emailPasswordToUser: Whether or not Meraki should email the password to user. Default is
              false.
            authorizations: Authorization zones and expiration dates for the user.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "update_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        meraki_auth_user_id = urllib.parse.quote(meraki_auth_user_id, safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        body_params = [
            "name",
            "password",
            "emailPasswordToUser",
            "authorizations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_mqtt_broker(
        self, network_id: str, name: str, host: str, port: int, **kwargs: Any
    ) -> dict[str, Any]:
        """Add an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

        Args:
            network_id: Network ID.
            name: Name of the MQTT broker.
            host: Host name/IP address where the MQTT broker runs.
            port: Host port though which the MQTT broker can be reached.
            security: Security settings of the MQTT broker.
            authentication: Authentication settings of the MQTT broker.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "create_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/mqttBrokers"

        body_params = [
            "name",
            "host",
            "port",
            "security",
            "authentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_mqtt_broker(
        self, network_id: str, mqtt_broker_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.
            name: Name of the MQTT broker.
            host: Host name/IP address where the MQTT broker runs.
            port: Host port though which the MQTT broker can be reached.
            security: Security settings of the MQTT broker.
            authentication: Authentication settings of the MQTT broker.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "update_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        mqtt_broker_id = urllib.parse.quote(mqtt_broker_id, safe="")
        resource = f"/networks/{network_id}/mqttBrokers/{mqtt_broker_id}"

        body_params = [
            "name",
            "host",
            "port",
            "security",
            "authentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_mqtt_broker(self, network_id: str, mqtt_broker_id: str) -> dict[str, Any]:
        """Delete an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "delete_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        mqtt_broker_id = urllib.parse.quote(mqtt_broker_id, safe="")
        resource = f"/networks/{network_id}/mqttBrokers/{mqtt_broker_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_settings(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update the settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        Args:
            network_id: Network ID.
            localStatusPageEnabled: Enables / disables the local device status pages (<a
              target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a
              target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a
              target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a
              target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>).
              Optional (defaults to false).
            remoteStatusPageEnabled: Enables / disables access to the device status page (<a
              target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set
              if localStatusPageEnabled is set to true.
            localStatusPage: A hash of Local Status page(s)' authentication options applied to the
              Network.
            securePort: A hash of SecureConnect options applied to the Network.
            namedVlans: A hash of Named VLANs options applied to the Network.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "settings"],
            "operation": "update_network_settings",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/settings"

        body_params = [
            "localStatusPageEnabled",
            "remoteStatusPageEnabled",
            "localStatusPage",
            "securePort",
            "namedVlans",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def split_network(self, network_id: str) -> dict[str, Any]:
        """Split a combined network into individual networks for each type of device.

        https://developer.cisco.com/meraki/api-v1/#!split-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "split_network"}
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/split"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action

    def unbind_network(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Unbind a network from a template.

        https://developer.cisco.com/meraki/api-v1/#!unbind-network

        Args:
            network_id: Network ID.
            retainConfigs: Optional boolean to retain all the current configs given by the template.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "unbind_network"}
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/unbind"

        body_params = [
            "retainConfigs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_network_vlan_profile(
        self, network_id: str, name: str, vlanNames: list, vlanGroups: list, iname: str
    ) -> dict[str, Any]:
        """Create a VLAN profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-vlan-profile

        Args:
            network_id: Network ID.
            name: Name of the profile, string length must be from 1 to 255 characters.
            vlanNames: An array of named VLANs.
            vlanGroups: An array of VLAN groups.
            iname: IName of the profile.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "create_network_vlan_profile",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/vlanProfiles"

        body_params = [
            "name",
            "vlanNames",
            "vlanGroups",
            "iname",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_network_vlan_profile(self, network_id: str, iname: str) -> dict[str, Any]:
        """Delete a VLAN profile of a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-vlan-profile

        Args:
            network_id: Network ID.
            iname: Iname.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "delete_network_vlan_profile",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        iname = urllib.parse.quote(iname, safe="")
        resource = f"/networks/{network_id}/vlanProfiles/{iname}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_webhooks_payload_template(
        self, network_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            name: The name of the new template.
            body: The liquid template used for the body of the webhook message. Either `body` or
              `bodyFile` must be specified.
            headers: The liquid template used with the webhook headers.
            bodyFile: A Base64 encoded file containing liquid template used for the body of the
              webhook message. Either `body` or `bodyFile` must be specified.
            headersFile: A Base64 encoded file containing the liquid template used with the webhook
              headers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "create_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates"

        body_params = [
            "name",
            "body",
            "headers",
            "bodyFile",
            "headersFile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_network_webhooks_payload_template(
        self, network_id: str, payload_template_id: str
    ) -> dict[str, Any]:
        """Destroy a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            payload_template_id: Payload template ID.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "delete_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        payload_template_id = urllib.parse.quote(payload_template_id, safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_webhooks_payload_template(
        self, network_id: str, payload_template_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            payload_template_id: Payload template ID.
            name: The name of the template.
            body: The liquid template used for the body of the webhook message.
            headers: The liquid template used with the webhook headers.
            bodyFile: A file containing liquid template used for the body of the webhook message.
            headersFile: A file containing the liquid template used with the webhook headers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "update_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        payload_template_id = urllib.parse.quote(payload_template_id, safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}"

        body_params = [
            "name",
            "body",
            "headers",
            "bodyFile",
            "headersFile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action
