"""ActionBatchNetworks API endpoints."""

import urllib
from typing import Any


class ActionBatchNetworks:
    """ActionBatchNetworks class."""

    def __init__(self) -> None:
        pass

    def update_network(
        self,
        network_id: str,
        *,
        name: str | None = None,
        time_zone: str | None = None,
        tags: list | None = None,
        enrollment_string: str | None = None,
        notes: str | None = None,
    ) -> dict[str, Any]:
        """Update a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network

        Args:
            network_id: Network ID.
            name: The name of the network.
            time_zone: The timezone of the network. For a list of allowed timezones, please see the
              'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article.</a>.
            tags: A list of tags to be applied to the network.
            enrollment_string: A unique identifier which can be used for device enrollment or easy
              access through the Meraki SM Registration page or the Self Service Portal.
              Please note that changing this field may cause existing bookmarks to
              break.
            notes: Add any notes or additional information about this network here.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "update_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if time_zone is not None:
            payload["timeZone"] = time_zone
        if tags is not None:
            payload["tags"] = tags
        if enrollment_string is not None:
            payload["enrollmentString"] = enrollment_string
        if notes is not None:
            payload["notes"] = notes

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def delete_network(self, network_id: str) -> dict[str, Any]:
        """Delete a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "delete_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def bind_network(
        self, network_id: str, config_template_id: str, *, auto_bind: bool | None = None
    ) -> dict[str, Any]:
        """Bind a network to a template.

        https://developer.cisco.com/meraki/api-v1/#!bind-network

        Args:
            network_id: Network ID.
            config_template_id: The ID of the template to which the network should be bound.
            auto_bind: Optional boolean indicating whether the network's switches should
              automatically bind to profiles of the same model. Defaults to false if
              left unspecified. This option only affects switch networks and switch
              templates. Auto-bind is not valid unless the switch template has at least
              one profile and has at most one profile per switch model.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "bind_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/bind"

        payload = {}
        if config_template_id is not None:
            payload["configTemplateId"] = config_template_id
        if auto_bind is not None:
            payload["autoBind"] = auto_bind

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def provision_network_clients(
        self,
        network_id: str,
        clients: list,
        device_policy: str,
        *,
        group_policy_id: str | None = None,
        policies_by_security_appliance: dict | None = None,
        policies_by_ssid: dict | None = None,
    ) -> dict[str, Any]:
        """Provisions a client with a name and policy.

        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        Args:
            network_id: Network ID.
            clients: The array of clients to provision.
            device_policy: The policy to apply to the specified client. Can be 'Group policy',
              'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
            group_policy_id: The ID of the desired group policy to apply to the client. Required if
              'devicePolicy' is set to "Group policy". Otherwise this is ignored.
            policies_by_security_appliance: An object, describing what the policy-connection
              association is for the security appliance. (Only relevant if the security
              appliance is actually within the network).
            policies_by_ssid: An object, describing the policy-connection associations for each
              active SSID within the network. Keys should be the number of enabled
              SSIDs, mapping to an object describing the client's policy.

        """
        if device_policy is not None:
            options = ["Allowed", "Blocked", "Group policy", "Normal", "Per connection"]
            assert device_policy in options, (
                f'"device_policy" cannot be "{device_policy}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "clients"],
            "operation": "provision_network_clients",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/provision"

        payload = {}
        if clients is not None:
            payload["clients"] = clients
        if device_policy is not None:
            payload["devicePolicy"] = device_policy
        if group_policy_id is not None:
            payload["groupPolicyId"] = group_policy_id
        if policies_by_security_appliance is not None:
            payload["policiesBySecurityAppliance"] = policies_by_security_appliance
        if policies_by_ssid is not None:
            payload["policiesBySsid"] = policies_by_ssid

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def claim_network_devices(
        self,
        network_id: str,
        serials: list,
        *,
        add_atomically: bool | None = None,
        details_by_device: list | None = None,
    ) -> dict[str, Any]:
        """Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed).

        https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

        Args:
            network_id: Network ID.
            add_atomically: Whether to claim devices atomically. If true, all devices will be
              claimed or none will be claimed. Default is true.
            serials: A list of serials of devices to claim.
            details_by_device: Optional details for claimed devices (currently only used for
              Catalyst devices).

        """
        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "claim_network_devices",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/claim"

        params = {}
        if add_atomically is not None:
            params["addAtomically"] = add_atomically

        payload = {}
        if serials is not None:
            payload["serials"] = serials
        if details_by_device is not None:
            payload["detailsByDevice"] = details_by_device

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def vmx_network_devices_claim(self, network_id: str, size: str) -> dict[str, Any]:
        """Claim a vMX into a network.

        https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim

        Args:
            network_id: Network ID.
            size: The size of the vMX you claim. It can be one of: small, medium, large, xlarge,
              100.

        """
        if size is not None:
            options = ["100", "large", "medium", "small", "xlarge"]
            assert size in options, f'"size" cannot be "{size}", & must be set to one of: {options}'

        metadata = {
            "tags": ["networks", "configure", "devices", "claim"],
            "operation": "vmx_network_devices_claim",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/claim/vmx"

        payload = {}
        if size is not None:
            payload["size"] = size

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def remove_network_devices(self, network_id: str, serial: str) -> dict[str, Any]:
        """Remove a single device.

        https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

        Args:
            network_id: Network ID.
            serial: The serial of a device.

        """
        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "remove_network_devices",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/remove"

        payload = {}
        if serial is not None:
            payload["serial"] = serial

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def update_network_firmware_upgrades(
        self,
        network_id: str,
        *,
        upgrade_window: dict | None = None,
        timezone: str | None = None,
        products: dict | None = None,
    ) -> dict[str, Any]:
        """Update firmware upgrade information for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

        Args:
            network_id: Network ID.
            upgrade_window: Upgrade window for devices in network.
            timezone: The timezone for the network.
            products: Contains information about the network to update.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades"],
            "operation": "update_network_firmware_upgrades",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades"

        payload = {}
        if upgrade_window is not None:
            payload["upgradeWindow"] = upgrade_window
        if timezone is not None:
            payload["timezone"] = timezone
        if products is not None:
            payload["products"] = products

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def create_network_firmware_upgrades_rollback(
        self,
        network_id: str,
        reasons: list,
        *,
        product: str | None = None,
        time: str | None = None,
        to_version: dict | None = None,
    ) -> dict[str, Any]:
        """Rollback a Firmware Upgrade For A Network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

        Args:
            network_id: Network ID.
            product: Product type to rollback (if the network is a combined network).
            time: Scheduled time for the rollback.
            reasons: Reasons for the rollback.
            to_version: Version to downgrade to (if the network has firmware flexibility).

        """
        if product is not None:
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
            assert product in options, (
                f'"product" cannot be "{product}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "rollbacks"],
            "operation": "create_network_firmware_upgrades_rollback",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/rollbacks"

        payload = {}
        if product is not None:
            payload["product"] = product
        if time is not None:
            payload["time"] = time
        if reasons is not None:
            payload["reasons"] = reasons
        if to_version is not None:
            payload["toVersion"] = to_version

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def create_network_firmware_upgrades_staged_group(
        self,
        network_id: str,
        name: str,
        is_default: bool,
        *,
        description: str | None = None,
        assigned_devices: dict | None = None,
    ) -> dict[str, Any]:
        """Create a Staged Upgrade Group for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            name: Name of the Staged Upgrade Group. Length must be 1 to 255 characters.
            description: Description of the Staged Upgrade Group. Length must be 1 to 255
              characters.
            is_default: Boolean indicating the default Group. Any device that does not have a group
              explicitly assigned will upgrade with this group.
            assigned_devices: The devices and Switch Stacks assigned to the Group.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "create_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups"

        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if is_default is not None:
            payload["isDefault"] = is_default
        if assigned_devices is not None:
            payload["assignedDevices"] = assigned_devices

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_id = urllib.parse.quote(str(group_id), safe="")
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
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "batch_network_floor_plans_auto_locate_jobs",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/batch"

        payload = {}
        if jobs is not None:
            payload["jobs"] = jobs

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        job_id = urllib.parse.quote(str(job_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/cancel"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action

    def publish_network_floor_plans_auto_locate_job(
        self, network_id: str, job_id: str, *, devices: list | None = None
    ) -> dict[str, Any]:
        """Update the status of a finished auto locate job to be published, and update device locations.

        https://developer.cisco.com/meraki/api-v1/#!publish-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.
            devices: The list of devices to publish positions for.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "publish_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        job_id = urllib.parse.quote(str(job_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/publish"

        payload = {}
        if devices is not None:
            payload["devices"] = devices

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def recalculate_network_floor_plans_auto_locate_job(
        self, network_id: str, job_id: str, *, devices: list | None = None
    ) -> dict[str, Any]:
        """Trigger auto locate recalculation for a job, and optionally set anchors.

        https://developer.cisco.com/meraki/api-v1/#!recalculate-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.
            devices: The list of devices to update anchor positions for.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "recalculate_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        job_id = urllib.parse.quote(str(job_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/recalculate"

        payload = {}
        if devices is not None:
            payload["devices"] = devices

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
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
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "devices"],
            "operation": "batch_network_floor_plans_devices_update",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/devices/batchUpdate"

        payload = {}
        if assignments is not None:
            payload["assignments"] = assignments

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def update_network_floor_plan(
        self,
        network_id: str,
        floor_plan_id: str,
        *,
        name: str | None = None,
        center: dict | None = None,
        bottom_left_corner: dict | None = None,
        bottom_right_corner: dict | None = None,
        top_left_corner: dict | None = None,
        top_right_corner: dict | None = None,
        floor_number: float | None = None,
        image_contents: str | None = None,
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
            bottom_left_corner: The longitude and latitude of the bottom left corner of your floor
              plan.
            bottom_right_corner: The longitude and latitude of the bottom right corner of your floor
              plan.
            top_left_corner: The longitude and latitude of the top left corner of your floor plan.
            top_right_corner: The longitude and latitude of the top right corner of your floor plan.
            floor_number: The floor number of the floors within the building.
            image_contents: The file contents (a base 64 encoded string) of your new image.
              Supported formats are PNG, GIF, and JPG. Note that all images are saved as
              PNG files, regardless of the format they are uploaded in. If you upload a
              new image, and you do NOT specify any new geolocation fields ('center,
              'topLeftCorner', etc), the floor plan will be recentered with no rotation
              in order to maintain the aspect ratio of your new image.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "update_network_floor_plan",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        floor_plan_id = urllib.parse.quote(str(floor_plan_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/{floor_plan_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if center is not None:
            payload["center"] = center
        if bottom_left_corner is not None:
            payload["bottomLeftCorner"] = bottom_left_corner
        if bottom_right_corner is not None:
            payload["bottomRightCorner"] = bottom_right_corner
        if top_left_corner is not None:
            payload["topLeftCorner"] = top_left_corner
        if top_right_corner is not None:
            payload["topRightCorner"] = top_right_corner
        if floor_number is not None:
            payload["floorNumber"] = floor_number
        if image_contents is not None:
            payload["imageContents"] = image_contents

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        floor_plan_id = urllib.parse.quote(str(floor_plan_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/{floor_plan_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_group_policy(
        self,
        network_id: str,
        name: str,
        *,
        scheduling: dict | None = None,
        bandwidth: dict | None = None,
        firewall_and_traffic_shaping: dict | None = None,
        content_filtering: dict | None = None,
        splash_auth_settings: str | None = None,
        vlan_tagging: dict | None = None,
        bonjour_forwarding: dict | None = None,
    ) -> dict[str, Any]:
        """Create a group policy.

        https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

        Args:
            network_id: Network ID.
            name: The name for your group policy. Required.
            scheduling: The schedule for the group policy. Schedules are applied to days of the
              week.
            bandwidth: The bandwidth settings for clients bound to your group policy.
            firewall_and_traffic_shaping: The firewall and traffic shaping rules and settings for
              your policy.
            content_filtering: The content filtering settings for your group policy.
            splash_auth_settings: Whether clients bound to your policy will bypass splash
              authorization or behave according to the network's rules. Can be one of
              'network default' or 'bypass'. Only available if your network has a
              wireless configuration.
            vlan_tagging: The VLAN tagging settings for your group policy. Only available if your
              network has a wireless configuration.
            bonjour_forwarding: The Bonjour settings for your group policy. Only valid if your
              network has a wireless configuration.

        """
        if splash_auth_settings is not None:
            options = ["bypass", "network default"]
            assert splash_auth_settings in options, (
                f'"splash_auth_settings" cannot be "{splash_auth_settings}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "create_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scheduling is not None:
            payload["scheduling"] = scheduling
        if bandwidth is not None:
            payload["bandwidth"] = bandwidth
        if firewall_and_traffic_shaping is not None:
            payload["firewallAndTrafficShaping"] = firewall_and_traffic_shaping
        if content_filtering is not None:
            payload["contentFiltering"] = content_filtering
        if splash_auth_settings is not None:
            payload["splashAuthSettings"] = splash_auth_settings
        if vlan_tagging is not None:
            payload["vlanTagging"] = vlan_tagging
        if bonjour_forwarding is not None:
            payload["bonjourForwarding"] = bonjour_forwarding

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def update_network_group_policy(
        self,
        network_id: str,
        group_policy_id: str,
        *,
        name: str | None = None,
        scheduling: dict | None = None,
        bandwidth: dict | None = None,
        firewall_and_traffic_shaping: dict | None = None,
        content_filtering: dict | None = None,
        splash_auth_settings: str | None = None,
        vlan_tagging: dict | None = None,
        bonjour_forwarding: dict | None = None,
    ) -> dict[str, Any]:
        """Update a group policy.

        https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

        Args:
            network_id: Network ID.
            group_policy_id: Group policy ID.
            name: The name for your group policy.
            scheduling: The schedule for the group policy. Schedules are applied to days of the
              week.
            bandwidth: The bandwidth settings for clients bound to your group policy.
            firewall_and_traffic_shaping: The firewall and traffic shaping rules and settings for
              your policy.
            content_filtering: The content filtering settings for your group policy.
            splash_auth_settings: Whether clients bound to your policy will bypass splash
              authorization or behave according to the network's rules. Can be one of
              'network default' or 'bypass'. Only available if your network has a
              wireless configuration.
            vlan_tagging: The VLAN tagging settings for your group policy. Only available if your
              network has a wireless configuration.
            bonjour_forwarding: The Bonjour settings for your group policy. Only valid if your
              network has a wireless configuration.

        """
        if splash_auth_settings is not None:
            options = ["bypass", "network default"]
            assert splash_auth_settings in options, (
                f'"splash_auth_settings" cannot be "{splash_auth_settings}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "update_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_policy_id = urllib.parse.quote(str(group_policy_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scheduling is not None:
            payload["scheduling"] = scheduling
        if bandwidth is not None:
            payload["bandwidth"] = bandwidth
        if firewall_and_traffic_shaping is not None:
            payload["firewallAndTrafficShaping"] = firewall_and_traffic_shaping
        if content_filtering is not None:
            payload["contentFiltering"] = content_filtering
        if splash_auth_settings is not None:
            payload["splashAuthSettings"] = splash_auth_settings
        if vlan_tagging is not None:
            payload["vlanTagging"] = vlan_tagging
        if bonjour_forwarding is not None:
            payload["bonjourForwarding"] = bonjour_forwarding

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def delete_network_group_policy(
        self, network_id: str, group_policy_id: str, *, force: bool | None = None
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
        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "delete_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_policy_id = urllib.parse.quote(str(group_policy_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        params = {}
        if force is not None:
            params["force"] = force

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_meraki_auth_user(
        self,
        network_id: str,
        email: str,
        authorizations: list,
        *,
        name: str | None = None,
        password: str | None = None,
        account_type: str | None = None,
        email_password_to_user: bool | None = None,
        is_admin: bool | None = None,
    ) -> dict[str, Any]:
        """Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap).

        https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

        Args:
            network_id: Network ID.
            email: Email address of the user.
            name: Name of the user. Only required If the user is not a Dashboard administrator.
            password: The password for this user account. Only required If the user is not a
              Dashboard administrator.
            account_type: Authorization type for user. Can be 'Guest' or '802.1X' for wireless
              networks, or 'Client VPN' for MX networks. Defaults to '802.1X'.
            email_password_to_user: Whether or not Meraki should email the password to user. Default
              is false.
            is_admin: Whether or not the user is a Dashboard administrator.
            authorizations: Authorization zones and expiration dates for the user.

        """
        if account_type is not None:
            options = ["802.1X", "Client VPN", "Guest"]
            assert account_type in options, (
                f'"account_type" cannot be "{account_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "create_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers"

        payload = {}
        if email is not None:
            payload["email"] = email
        if name is not None:
            payload["name"] = name
        if password is not None:
            payload["password"] = password
        if account_type is not None:
            payload["accountType"] = account_type
        if email_password_to_user is not None:
            payload["emailPasswordToUser"] = email_password_to_user
        if is_admin is not None:
            payload["isAdmin"] = is_admin
        if authorizations is not None:
            payload["authorizations"] = authorizations

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def delete_network_meraki_auth_user(
        self, network_id: str, meraki_auth_user_id: str, *, delete: bool | None = None
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
        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "delete_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        meraki_auth_user_id = urllib.parse.quote(str(meraki_auth_user_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        params = {}
        if delete is not None:
            params["delete"] = delete

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_meraki_auth_user(
        self,
        network_id: str,
        meraki_auth_user_id: str,
        *,
        name: str | None = None,
        password: str | None = None,
        email_password_to_user: bool | None = None,
        authorizations: list | None = None,
    ) -> dict[str, Any]:
        """Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated).

        https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

        Args:
            network_id: Network ID.
            meraki_auth_user_id: Meraki auth user ID.
            name: Name of the user. Only allowed If the user is not Dashboard administrator.
            password: The password for this user account. Only allowed If the user is not Dashboard
              administrator.
            email_password_to_user: Whether or not Meraki should email the password to user. Default
              is false.
            authorizations: Authorization zones and expiration dates for the user.

        """
        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "update_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        meraki_auth_user_id = urllib.parse.quote(str(meraki_auth_user_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if password is not None:
            payload["password"] = password
        if email_password_to_user is not None:
            payload["emailPasswordToUser"] = email_password_to_user
        if authorizations is not None:
            payload["authorizations"] = authorizations

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def create_network_mqtt_broker(
        self,
        network_id: str,
        name: str,
        host: str,
        port: int,
        *,
        security: dict | None = None,
        authentication: dict | None = None,
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
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "create_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers"

        payload = {}
        if name is not None:
            payload["name"] = name
        if host is not None:
            payload["host"] = host
        if port is not None:
            payload["port"] = port
        if security is not None:
            payload["security"] = security
        if authentication is not None:
            payload["authentication"] = authentication

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def update_network_mqtt_broker(
        self,
        network_id: str,
        mqtt_broker_id: str,
        *,
        name: str | None = None,
        host: str | None = None,
        port: int | None = None,
        security: dict | None = None,
        authentication: dict | None = None,
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
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "update_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers/{mqtt_broker_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if host is not None:
            payload["host"] = host
        if port is not None:
            payload["port"] = port
        if security is not None:
            payload["security"] = security
        if authentication is not None:
            payload["authentication"] = authentication

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers/{mqtt_broker_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_settings(
        self,
        network_id: str,
        *,
        local_status_page_enabled: bool | None = None,
        remote_status_page_enabled: bool | None = None,
        local_status_page: dict | None = None,
        secure_port: dict | None = None,
        named_vlans: dict | None = None,
    ) -> dict[str, Any]:
        """Update the settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        Args:
            network_id: Network ID.
            local_status_page_enabled: Enables / disables the local device status pages (<a
              target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a
              target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a
              target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a
              target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>).
              Optional (defaults to false).
            remote_status_page_enabled: Enables / disables access to the device status page (<a
              target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set
              if localStatusPageEnabled is set to true.
            local_status_page: A hash of Local Status page(s)' authentication options applied to the
              Network.
            secure_port: A hash of SecureConnect options applied to the Network.
            named_vlans: A hash of Named VLANs options applied to the Network.

        """
        metadata = {
            "tags": ["networks", "configure", "settings"],
            "operation": "update_network_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/settings"

        payload = {}
        if local_status_page_enabled is not None:
            payload["localStatusPageEnabled"] = local_status_page_enabled
        if remote_status_page_enabled is not None:
            payload["remoteStatusPageEnabled"] = remote_status_page_enabled
        if local_status_page is not None:
            payload["localStatusPage"] = local_status_page
        if secure_port is not None:
            payload["securePort"] = secure_port
        if named_vlans is not None:
            payload["namedVlans"] = named_vlans

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def split_network(self, network_id: str) -> dict[str, Any]:
        """Split a combined network into individual networks for each type of device.

        https://developer.cisco.com/meraki/api-v1/#!split-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "split_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/split"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action

    def unbind_network(
        self, network_id: str, *, retain_configs: bool | None = None
    ) -> dict[str, Any]:
        """Unbind a network from a template.

        https://developer.cisco.com/meraki/api-v1/#!unbind-network

        Args:
            network_id: Network ID.
            retain_configs: Optional boolean to retain all the current configs given by the
              template.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "unbind_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/unbind"

        payload = {}
        if retain_configs is not None:
            payload["retainConfigs"] = retain_configs

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def create_network_vlan_profile(
        self, network_id: str, name: str, vlan_names: list, vlan_groups: list, iname: str
    ) -> dict[str, Any]:
        """Create a VLAN profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-vlan-profile

        Args:
            network_id: Network ID.
            name: Name of the profile, string length must be from 1 to 255 characters.
            vlan_names: An array of named VLANs.
            vlan_groups: An array of VLAN groups.
            iname: IName of the profile.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "create_network_vlan_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/vlanProfiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if vlan_names is not None:
            payload["vlanNames"] = vlan_names
        if vlan_groups is not None:
            payload["vlanGroups"] = vlan_groups
        if iname is not None:
            payload["iname"] = iname

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/{iname}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_webhooks_payload_template(
        self,
        network_id: str,
        name: str,
        *,
        body: str | None = None,
        headers: list | None = None,
        body_file: str | None = None,
        headers_file: str | None = None,
    ) -> dict[str, Any]:
        """Create a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            name: The name of the new template.
            body: The liquid template used for the body of the webhook message. Either `body` or
              `bodyFile` must be specified.
            headers: The liquid template used with the webhook headers.
            body_file: A Base64 encoded file containing liquid template used for the body of the
              webhook message. Either `body` or `bodyFile` must be specified.
            headers_file: A Base64 encoded file containing the liquid template used with the webhook
              headers.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "create_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates"

        payload = {}
        if name is not None:
            payload["name"] = name
        if body is not None:
            payload["body"] = body
        if headers is not None:
            payload["headers"] = headers
        if body_file is not None:
            payload["bodyFile"] = body_file
        if headers_file is not None:
            payload["headersFile"] = headers_file

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        payload_template_id = urllib.parse.quote(str(payload_template_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_webhooks_payload_template(
        self,
        network_id: str,
        payload_template_id: str,
        *,
        name: str | None = None,
        body: str | None = None,
        headers: list | None = None,
        body_file: str | None = None,
        headers_file: str | None = None,
    ) -> dict[str, Any]:
        """Update a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            payload_template_id: Payload template ID.
            name: The name of the template.
            body: The liquid template used for the body of the webhook message.
            headers: The liquid template used with the webhook headers.
            body_file: A file containing liquid template used for the body of the webhook message.
            headers_file: A file containing the liquid template used with the webhook headers.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "update_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        payload_template_id = urllib.parse.quote(str(payload_template_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if body is not None:
            payload["body"] = body
        if headers is not None:
            payload["headers"] = headers
        if body_file is not None:
            payload["bodyFile"] = body_file
        if headers_file is not None:
            payload["headersFile"] = headers_file

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action
