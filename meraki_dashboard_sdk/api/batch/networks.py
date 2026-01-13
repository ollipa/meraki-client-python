"""ActionBatchNetworks API endpoints."""


class ActionBatchNetworks:
    """ActionBatchNetworks class."""

    def __init__(self) -> None:
        pass

    def update_network(self, networkId: str, **kwargs):
        """
        **Update a network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network

        - networkId (string): Network ID
        - name (string): The name of the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - tags (array): A list of tags to be applied to the network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break.
        - notes (string): Add any notes or additional information about this network here.
        """

        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "update_network"}
        resource = f"/networks/{networkId}"

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

    def delete_network(self, networkId: str):
        """
        **Delete a network.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network

        - networkId (string): Network ID
        """

        metadata = {"tags": ["networks", "configure"], "operation": "delete_network"}
        resource = f"/networks/{networkId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def bind_network(self, networkId: str, configTemplateId: str, **kwargs):
        """
        **Bind a network to a template.**
        https://developer.cisco.com/meraki/api-v1/#!bind-network

        - networkId (string): Network ID
        - configTemplateId (string): The ID of the template to which the network should be bound.
        - autoBind (boolean): Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model. Defaults to false if left unspecified. This option only affects switch networks and switch templates. Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.
        """

        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "bind_network"}
        resource = f"/networks/{networkId}/bind"

        body_params = [
            "configTemplateId",
            "autoBind",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def provision_network_clients(self, networkId: str, clients: list, devicePolicy: str, **kwargs):
        """
        **Provisions a client with a name and policy.**
        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        - networkId (string): Network ID
        - clients (array): The array of clients to provision
        - devicePolicy (string): The policy to apply to the specified client. Can be 'Group policy', 'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
        - groupPolicyId (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
        - policiesBySecurityAppliance (object): An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)
        - policiesBySsid (object): An object, describing the policy-connection associations for each active SSID within the network. Keys should be the number of enabled SSIDs, mapping to an object describing the client's policy
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
        resource = f"/networks/{networkId}/clients/provision"

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

    def claim_network_devices(self, networkId: str, serials: list, **kwargs):
        """
        **Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed).**
        https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

        - networkId (string): Network ID
        - serials (array): A list of serials of devices to claim
        - addAtomically (boolean): Whether to claim devices atomically. If true, all devices will be claimed or none will be claimed. Default is true.
        - detailsByDevice (array): Optional details for claimed devices (currently only used for Catalyst devices)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "claim_network_devices",
        }
        resource = f"/networks/{networkId}/devices/claim"

        body_params = [
            "serials",
            "detailsByDevice",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def vmx_network_devices_claim(self, networkId: str, size: str):
        """
        **Claim a vMX into a network.**
        https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim

        - networkId (string): Network ID
        - size (string): The size of the vMX you claim. It can be one of: small, medium, large, xlarge, 100
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
        resource = f"/networks/{networkId}/devices/claim/vmx"

        body_params = [
            "size",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def remove_network_devices(self, networkId: str, serial: str):
        """
        **Remove a single device.**
        https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

        - networkId (string): Network ID
        - serial (string): The serial of a device
        """

        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "remove_network_devices",
        }
        resource = f"/networks/{networkId}/devices/remove"

        body_params = [
            "serial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_firmware_upgrades(self, networkId: str, **kwargs):
        """
        **Update firmware upgrade information for a network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

        - networkId (string): Network ID
        - upgradeWindow (object): Upgrade window for devices in network
        - timezone (string): The timezone for the network
        - products (object): Contains information about the network to update
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades"],
            "operation": "update_network_firmware_upgrades",
        }
        resource = f"/networks/{networkId}/firmwareUpgrades"

        body_params = [
            "upgradeWindow",
            "timezone",
            "products",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_firmware_upgrades_rollback(self, networkId: str, reasons: list, **kwargs):
        """
        **Rollback a Firmware Upgrade For A Network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

        - networkId (string): Network ID
        - reasons (array): Reasons for the rollback
        - product (string): Product type to rollback (if the network is a combined network)
        - time (string): Scheduled time for the rollback
        - toVersion (object): Version to downgrade to (if the network has firmware flexibility)
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
        resource = f"/networks/{networkId}/firmwareUpgrades/rollbacks"

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
        self, networkId: str, name: str, isDefault: bool, **kwargs
    ):
        """
        **Create a Staged Upgrade Group for a network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group

        - networkId (string): Network ID
        - name (string): Name of the Staged Upgrade Group. Length must be 1 to 255 characters
        - isDefault (boolean): Boolean indicating the default Group. Any device that does not have a group explicitly assigned will upgrade with this group
        - description (string): Description of the Staged Upgrade Group. Length must be 1 to 255 characters
        - assignedDevices (object): The devices and Switch Stacks assigned to the Group
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "create_network_firmware_upgrades_staged_group",
        }
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/groups"

        body_params = [
            "name",
            "description",
            "isDefault",
            "assignedDevices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_network_firmware_upgrades_staged_group(self, networkId: str, groupId: str):
        """
        **Delete a Staged Upgrade Group.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-firmware-upgrades-staged-group

        - networkId (string): Network ID
        - groupId (string): Group ID
        """

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "delete_network_firmware_upgrades_staged_group",
        }
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def batch_network_floor_plans_auto_locate_jobs(self, networkId: str, jobs: list):
        """
        **Schedule auto locate jobs for one or more floor plans in a network.**
        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-auto-locate-jobs

        - networkId (string): Network ID
        - jobs (array): The list of auto locate jobs to be scheduled. Up to 100 jobs can be provided in a request.
        """

        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "batch_network_floor_plans_auto_locate_jobs",
        }
        resource = f"/networks/{networkId}/floorPlans/autoLocate/jobs/batch"

        body_params = [
            "jobs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def cancel_network_floor_plans_auto_locate_job(self, networkId: str, jobId: str):
        """
        **Cancel a scheduled or running auto locate job.**
        https://developer.cisco.com/meraki/api-v1/#!cancel-network-floor-plans-auto-locate-job

        - networkId (string): Network ID
        - jobId (string): Job ID
        """

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "cancel_network_floor_plans_auto_locate_job",
        }
        resource = f"/networks/{networkId}/floorPlans/autoLocate/jobs/{jobId}/cancel"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action

    def publish_network_floor_plans_auto_locate_job(self, networkId: str, jobId: str, **kwargs):
        """
        **Update the status of a finished auto locate job to be published, and update device locations.**
        https://developer.cisco.com/meraki/api-v1/#!publish-network-floor-plans-auto-locate-job

        - networkId (string): Network ID
        - jobId (string): Job ID
        - devices (array): The list of devices to publish positions for
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "publish_network_floor_plans_auto_locate_job",
        }
        resource = f"/networks/{networkId}/floorPlans/autoLocate/jobs/{jobId}/publish"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def recalculate_network_floor_plans_auto_locate_job(self, networkId: str, jobId: str, **kwargs):
        """
        **Trigger auto locate recalculation for a job, and optionally set anchors.**
        https://developer.cisco.com/meraki/api-v1/#!recalculate-network-floor-plans-auto-locate-job

        - networkId (string): Network ID
        - jobId (string): Job ID
        - devices (array): The list of devices to update anchor positions for
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "recalculate_network_floor_plans_auto_locate_job",
        }
        resource = f"/networks/{networkId}/floorPlans/autoLocate/jobs/{jobId}/recalculate"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def batch_network_floor_plans_devices_update(self, networkId: str, assignments: list):
        """
        **Update floorplan assignments for a batch of devices.**
        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-devices-update

        - networkId (string): Network ID
        - assignments (array): List of floorplan assignments to update. Up to 100 floor plan assignments can be provided in a request.
        """

        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "devices"],
            "operation": "batch_network_floor_plans_devices_update",
        }
        resource = f"/networks/{networkId}/floorPlans/devices/batchUpdate"

        body_params = [
            "assignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_floor_plan(self, networkId: str, floorPlanId: str, **kwargs):
        """
        **Update a floor plan's geolocation and other meta data.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

        - networkId (string): Network ID
        - floorPlanId (string): Floor plan ID
        - name (string): The name of your floor plan.
        - center (object): The longitude and latitude of the center of your floor plan. If you want to change the geolocation data of your floor plan, either the 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
        - bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
        - bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
        - topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
        - topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
        - floorNumber (number): The floor number of the floors within the building
        - imageContents (string): The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields ('center, 'topLeftCorner', etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "update_network_floor_plan",
        }
        resource = f"/networks/{networkId}/floorPlans/{floorPlanId}"

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

    def delete_network_floor_plan(self, networkId: str, floorPlanId: str):
        """
        **Destroy a floor plan.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

        - networkId (string): Network ID
        - floorPlanId (string): Floor plan ID
        """

        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "delete_network_floor_plan",
        }
        resource = f"/networks/{networkId}/floorPlans/{floorPlanId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_group_policy(self, networkId: str, name: str, **kwargs):
        """
        **Create a group policy.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

        - networkId (string): Network ID
        - name (string): The name for your group policy. Required.
        - scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

        - bandwidth (object):     The bandwidth settings for clients bound to your group policy.

        - firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

        - contentFiltering (object): The content filtering settings for your group policy
        - splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
        - vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
        - bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.
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
        resource = f"/networks/{networkId}/groupPolicies"

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

    def update_network_group_policy(self, networkId: str, groupPolicyId: str, **kwargs):
        """
        **Update a group policy.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

        - networkId (string): Network ID
        - groupPolicyId (string): Group policy ID
        - name (string): The name for your group policy.
        - scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

        - bandwidth (object):     The bandwidth settings for clients bound to your group policy.

        - firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

        - contentFiltering (object): The content filtering settings for your group policy
        - splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
        - vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
        - bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.
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
        resource = f"/networks/{networkId}/groupPolicies/{groupPolicyId}"

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

    def delete_network_group_policy(self, networkId: str, groupPolicyId: str, **kwargs):
        """
        **Delete a group policy.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

        - networkId (string): Network ID
        - groupPolicyId (string): Group policy ID
        - force (boolean): If true, the system deletes the GP even if there are active clients using the GP. After deletion, active clients that were assigned to that Group Policy will be left without any policy applied. Default is false.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "delete_network_group_policy",
        }
        resource = f"/networks/{networkId}/groupPolicies/{groupPolicyId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_meraki_auth_user(
        self, networkId: str, email: str, authorizations: list, **kwargs
    ):
        """
        **Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap).**
        https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

        - networkId (string): Network ID
        - email (string): Email address of the user
        - authorizations (array): Authorization zones and expiration dates for the user.
        - name (string): Name of the user. Only required If the user is not a Dashboard administrator.
        - password (string): The password for this user account. Only required If the user is not a Dashboard administrator.
        - accountType (string): Authorization type for user. Can be 'Guest' or '802.1X' for wireless networks, or 'Client VPN' for MX networks. Defaults to '802.1X'.
        - emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
        - isAdmin (boolean): Whether or not the user is a Dashboard administrator.
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
        resource = f"/networks/{networkId}/merakiAuthUsers"

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

    def delete_network_meraki_auth_user(self, networkId: str, merakiAuthUserId: str, **kwargs):
        """
        **Delete an 802.1X RADIUS user, or deauthorize and optionally delete a splash guest or client VPN user.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

        - networkId (string): Network ID
        - merakiAuthUserId (string): Meraki auth user ID
        - delete (boolean): If the ID supplied is for a splash guest or client VPN user, and that user is not authorized for any other networks in the organization, then also delete the user. 802.1X RADIUS users are always deleted regardless of this optional attribute.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "delete_network_meraki_auth_user",
        }
        resource = f"/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_meraki_auth_user(self, networkId: str, merakiAuthUserId: str, **kwargs):
        """
        **Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated).**
        https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

        - networkId (string): Network ID
        - merakiAuthUserId (string): Meraki auth user ID
        - name (string): Name of the user. Only allowed If the user is not Dashboard administrator.
        - password (string): The password for this user account. Only allowed If the user is not Dashboard administrator.
        - emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
        - authorizations (array): Authorization zones and expiration dates for the user.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "update_network_meraki_auth_user",
        }
        resource = f"/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}"

        body_params = [
            "name",
            "password",
            "emailPasswordToUser",
            "authorizations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_mqtt_broker(self, networkId: str, name: str, host: str, port: int, **kwargs):
        """
        **Add an MQTT broker.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

        - networkId (string): Network ID
        - name (string): Name of the MQTT broker.
        - host (string): Host name/IP address where the MQTT broker runs.
        - port (integer): Host port though which the MQTT broker can be reached.
        - security (object): Security settings of the MQTT broker.
        - authentication (object): Authentication settings of the MQTT broker
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "create_network_mqtt_broker",
        }
        resource = f"/networks/{networkId}/mqttBrokers"

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

    def update_network_mqtt_broker(self, networkId: str, mqttBrokerId: str, **kwargs):
        """
        **Update an MQTT broker.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

        - networkId (string): Network ID
        - mqttBrokerId (string): Mqtt broker ID
        - name (string): Name of the MQTT broker.
        - host (string): Host name/IP address where the MQTT broker runs.
        - port (integer): Host port though which the MQTT broker can be reached.
        - security (object): Security settings of the MQTT broker.
        - authentication (object): Authentication settings of the MQTT broker
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "update_network_mqtt_broker",
        }
        resource = f"/networks/{networkId}/mqttBrokers/{mqttBrokerId}"

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

    def delete_network_mqtt_broker(self, networkId: str, mqttBrokerId: str):
        """
        **Delete an MQTT broker.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

        - networkId (string): Network ID
        - mqttBrokerId (string): Mqtt broker ID
        """

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "delete_network_mqtt_broker",
        }
        resource = f"/networks/{networkId}/mqttBrokers/{mqttBrokerId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_settings(self, networkId: str, **kwargs):
        """
        **Update the settings for a network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        - networkId (string): Network ID
        - localStatusPageEnabled (boolean): Enables / disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
        - remoteStatusPageEnabled (boolean): Enables / disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if localStatusPageEnabled is set to true
        - localStatusPage (object): A hash of Local Status page(s)' authentication options applied to the Network.
        - securePort (object): A hash of SecureConnect options applied to the Network.
        - namedVlans (object): A hash of Named VLANs options applied to the Network.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "settings"],
            "operation": "update_network_settings",
        }
        resource = f"/networks/{networkId}/settings"

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

    def split_network(self, networkId: str):
        """
        **Split a combined network into individual networks for each type of device.**
        https://developer.cisco.com/meraki/api-v1/#!split-network

        - networkId (string): Network ID
        """

        metadata = {"tags": ["networks", "configure"], "operation": "split_network"}
        resource = f"/networks/{networkId}/split"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action

    def unbind_network(self, networkId: str, **kwargs):
        """
        **Unbind a network from a template.**
        https://developer.cisco.com/meraki/api-v1/#!unbind-network

        - networkId (string): Network ID
        - retainConfigs (boolean): Optional boolean to retain all the current configs given by the template.
        """

        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "unbind_network"}
        resource = f"/networks/{networkId}/unbind"

        body_params = [
            "retainConfigs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_network_vlan_profile(
        self, networkId: str, name: str, vlanNames: list, vlanGroups: list, iname: str
    ):
        """
        **Create a VLAN profile for a network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-vlan-profile

        - networkId (string): Network ID
        - name (string): Name of the profile, string length must be from 1 to 255 characters
        - vlanNames (array): An array of named VLANs
        - vlanGroups (array): An array of VLAN groups
        - iname (string): IName of the profile
        """

        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "create_network_vlan_profile",
        }
        resource = f"/networks/{networkId}/vlanProfiles"

        body_params = [
            "name",
            "vlanNames",
            "vlanGroups",
            "iname",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_network_vlan_profile(self, networkId: str, iname: str):
        """
        **Delete a VLAN profile of a network.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-vlan-profile

        - networkId (string): Network ID
        - iname (string): Iname
        """

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "delete_network_vlan_profile",
        }
        resource = f"/networks/{networkId}/vlanProfiles/{iname}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_webhooks_payload_template(self, networkId: str, name: str, **kwargs):
        """
        **Create a webhook payload template for a network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-payload-template

        - networkId (string): Network ID
        - name (string): The name of the new template
        - body (string): The liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
        - headers (array): The liquid template used with the webhook headers.
        - bodyFile (string): A Base64 encoded file containing liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
        - headersFile (string): A Base64 encoded file containing the liquid template used with the webhook headers.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "create_network_webhooks_payload_template",
        }
        resource = f"/networks/{networkId}/webhooks/payloadTemplates"

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

    def delete_network_webhooks_payload_template(self, networkId: str, payloadTemplateId: str):
        """
        **Destroy a webhook payload template for a network.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-payload-template

        - networkId (string): Network ID
        - payloadTemplateId (string): Payload template ID
        """

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "delete_network_webhooks_payload_template",
        }
        resource = f"/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_webhooks_payload_template(
        self, networkId: str, payloadTemplateId: str, **kwargs
    ):
        """
        **Update a webhook payload template for a network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-payload-template

        - networkId (string): Network ID
        - payloadTemplateId (string): Payload template ID
        - name (string): The name of the template
        - body (string): The liquid template used for the body of the webhook message.
        - headers (array): The liquid template used with the webhook headers.
        - bodyFile (string): A file containing liquid template used for the body of the webhook message.
        - headersFile (string): A file containing the liquid template used with the webhook headers.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "update_network_webhooks_payload_template",
        }
        resource = f"/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}"

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
