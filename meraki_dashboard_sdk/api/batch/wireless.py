"""ActionBatchWireless API endpoints."""

import urllib
from typing import Any


class ActionBatchWireless:
    """ActionBatchWireless class."""

    def __init__(self) -> None:
        pass

    def update_device_wireless_alternate_management_interface_ipv6(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update alternate management interface IPv6 address.

        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-alternate-management-interface-ipv-6

        Args:
            serial: Serial.
            addresses: configured alternate management interface addresses.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "alternateManagementInterface", "ipv6"],
            "operation": "update_device_wireless_alternate_management_interface_ipv6",
        }
        resource = f"/devices/{serial}/wireless/alternateManagementInterface/ipv6"

        body_params = [
            "addresses",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_device_wireless_bluetooth_settings(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the bluetooth settings for a wireless device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-bluetooth-settings

        Args:
            serial: Serial.
            uuid: Desired UUID of the beacon. If the value is set to null it will reset to
              Dashboard's           automatically generated value.
            major: Desired major value of the beacon. If the value is set to null it will reset to
              Dashboard's automatically generated value.
            minor: Desired minor value of the beacon. If the value is set to null it will reset to
              Dashboard's automatically generated value.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "update_device_wireless_bluetooth_settings",
        }
        resource = f"/devices/{serial}/wireless/bluetooth/settings"

        body_params = [
            "uuid",
            "major",
            "minor",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_device_wireless_electronic_shelf_label(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the ESL settings of a device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-electronic-shelf-label

        Args:
            serial: Serial.
            channel: Desired ESL channel for the device, or 'Auto' (case insensitive) to use the
              recommended channel.
            enabled: Turn ESL features on and off for this device.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "update_device_wireless_electronic_shelf_label",
        }
        resource = f"/devices/{serial}/wireless/electronicShelfLabel"

        body_params = [
            "channel",
            "enabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_device_wireless_radio_settings(self, serial: str, **kwargs: Any) -> dict[str, Any]:
        """Update the radio settings overrides of a device, which take precedence over RF profiles.

        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-settings

        Args:
            serial: Serial.
            rfProfileId: The ID of an RF profile to assign to the device. If the value of this
              parameter is null, the appropriate basic RF profile (indoor or outdoor)
              will be assigned to the device. Assigning an RF profile will clear ALL
              manually configured overrides on the device (channel width, channel,
              power).
            twoFourGhzSettings: Manual radio settings for 2.4 GHz.
            fiveGhzSettings: Manual radio settings for 5 GHz.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "settings"],
            "operation": "update_device_wireless_radio_settings",
        }
        resource = f"/devices/{serial}/wireless/radio/settings"

        body_params = [
            "rfProfileId",
            "twoFourGhzSettings",
            "fiveGhzSettings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_wireless_air_marshal_rule(
        self, networkId: str, type: str, match: dict
    ) -> dict[str, Any]:
        """Creates a new rule.

        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-air-marshal-rule

        Args:
            networkId: Network ID.
            type: Indicates if this rule will allow, block, or alert.
            match: Object describing the rule specification.

        """
        kwargs = locals()

        if "type" in kwargs:
            options = ["alert", "allow", "block"]
            assert kwargs["type"] in options, (
                f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "create_network_wireless_air_marshal_rule",
        }
        resource = f"/networks/{networkId}/wireless/airMarshal/rules"

        body_params = [
            "type",
            "match",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_wireless_air_marshal_rule(
        self, networkId: str, ruleId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a rule.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-air-marshal-rule

        Args:
            networkId: Network ID.
            ruleId: Rule ID.
            type: Indicates if this rule will allow, block, or alert.
            match: Object describing the rule specification.

        """
        kwargs.update(locals())

        if "type" in kwargs:
            options = ["alert", "allow", "block"]
            assert kwargs["type"] in options, (
                f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "update_network_wireless_air_marshal_rule",
        }
        resource = f"/networks/{networkId}/wireless/airMarshal/rules/{ruleId}"

        body_params = [
            "type",
            "match",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_wireless_air_marshal_rule(
        self, networkId: str, ruleId: str
    ) -> dict[str, Any]:
        """Delete an Air Marshal rule.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-air-marshal-rule

        Args:
            networkId: Network ID.
            ruleId: Rule ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "delete_network_wireless_air_marshal_rule",
        }
        resource = f"/networks/{networkId}/wireless/airMarshal/rules/{ruleId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_wireless_air_marshal_settings(
        self, networkId: str, defaultPolicy: str
    ) -> dict[str, Any]:
        """Updates Air Marshal settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-air-marshal-settings

        Args:
            networkId: Network ID.
            defaultPolicy: Allows clients to access rogue networks. Blocked by default.

        """
        kwargs = locals()

        if "defaultPolicy" in kwargs:
            options = ["allow", "block"]
            assert kwargs["defaultPolicy"] in options, (
                f'''"defaultPolicy" cannot be "{kwargs["defaultPolicy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "settings"],
            "operation": "update_network_wireless_air_marshal_settings",
        }
        resource = f"/networks/{networkId}/wireless/airMarshal/settings"

        body_params = [
            "defaultPolicy",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_alternate_management_interface(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update alternate management interface and device static IP.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-alternate-management-interface

        Args:
            networkId: Network ID.
            enabled: Boolean value to enable or disable alternate management interface.
            vlanId: Alternate management interface VLAN, must be between 1 and 4094.
            protocols: Can be one or more of the following values: 'radius', 'snmp', 'syslog' or
              'ldap'.
            accessPoints: Array of access point serial number and IP assignment. Note: accessPoints
              IP assignment is not applicable for template networks, in other words, do
              not put 'accessPoints' in the body when updating template networks. Also,
              an empty 'accessPoints' array will remove all previous static IP
              assignments.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "alternateManagementInterface"],
            "operation": "update_network_wireless_alternate_management_interface",
        }
        resource = f"/networks/{networkId}/wireless/alternateManagementInterface"

        body_params = [
            "enabled",
            "vlanId",
            "protocols",
            "accessPoints",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_billing(self, networkId: str, **kwargs: Any) -> dict[str, Any]:
        """Update the billing settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-billing

        Args:
            networkId: Network ID.
            currency: The currency code of this node group's billing plans.
            plans: Array of billing plans in the node group. (Can configure a maximum of 5).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "billing"],
            "operation": "update_network_wireless_billing",
        }
        resource = f"/networks/{networkId}/wireless/billing"

        body_params = [
            "currency",
            "plans",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_electronic_shelf_label(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the ESL settings of a wireless network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-electronic-shelf-label

        Args:
            networkId: Network ID.
            hostname: Desired ESL hostname of the network.
            enabled: Turn ESL features on and off for this network.
            mode: Electronic shelf label mode of the network. Valid options are 'Bluetooth', 'high
              frequency'.

        """
        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["Bluetooth", "high frequency"]
            assert kwargs["mode"] in options, (
                f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "update_network_wireless_electronic_shelf_label",
        }
        resource = f"/networks/{networkId}/wireless/electronicShelfLabel"

        body_params = [
            "hostname",
            "enabled",
            "mode",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_wireless_ethernet_ports_profile(
        self, networkId: str, name: str, ports: list, **kwargs: Any
    ) -> dict[str, Any]:
        """Create an AP port profile.

        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ethernet-ports-profile

        Args:
            networkId: Network ID.
            name: AP port profile name.
            ports: AP ports configuration.
            usbPorts: AP usb ports configuration.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "create_network_wireless_ethernet_ports_profile",
        }
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles"

        body_params = [
            "name",
            "ports",
            "usbPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def assign_network_wireless_ethernet_ports_profiles(
        self, networkId: str, serials: list, profileId: str
    ) -> dict[str, Any]:
        """Assign AP port profile to list of APs.

        https://developer.cisco.com/meraki/api-v1/#!assign-network-wireless-ethernet-ports-profiles

        Args:
            networkId: Network ID.
            serials: List of AP serials.
            profileId: AP profile ID.

        """
        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "assign_network_wireless_ethernet_ports_profiles",
        }
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/assign"

        body_params = [
            "serials",
            "profileId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def set_network_wireless_ethernet_ports_profiles_default(
        self, networkId: str, profileId: str
    ) -> dict[str, Any]:
        """Set the AP port profile to be default for this network.

        https://developer.cisco.com/meraki/api-v1/#!set-network-wireless-ethernet-ports-profiles-default

        Args:
            networkId: Network ID.
            profileId: AP profile ID.

        """
        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "set_network_wireless_ethernet_ports_profiles_default",
        }
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/setDefault"

        body_params = [
            "profileId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_wireless_ethernet_ports_profile(
        self, networkId: str, profileId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the AP port profile by ID for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ethernet-ports-profile

        Args:
            networkId: Network ID.
            profileId: Profile ID.
            name: AP port profile name.
            ports: AP ports configuration.
            usbPorts: AP usb ports configuration.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "update_network_wireless_ethernet_ports_profile",
        }
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}"

        body_params = [
            "name",
            "ports",
            "usbPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_wireless_ethernet_ports_profile(
        self, networkId: str, profileId: str
    ) -> dict[str, Any]:
        """Delete an AP port profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ethernet-ports-profile

        Args:
            networkId: Network ID.
            profileId: Profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "delete_network_wireless_ethernet_ports_profile",
        }
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_wireless_location_scanning(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Change scanning API settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-location-scanning

        Args:
            networkId: Network ID.
            enabled: Collect location and scanning analytics.
            api: Enable push API for scanning events, analytics must be enabled.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "location", "scanning"],
            "operation": "update_network_wireless_location_scanning",
        }
        resource = f"/networks/{networkId}/wireless/location/scanning"

        body_params = [
            "enabled",
            "api",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_wireless_rf_profile(
        self, networkId: str, name: str, bandSelectionType: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Creates new RF profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-rf-profile

        Args:
            networkId: Network ID.
            name: The name of the new profile. Must be unique. This param is required on creation.
            bandSelectionType: Band selection can be set to either 'ssid' or 'ap'. This param is
              required on creation.
            clientBalancingEnabled: Steers client to best available access point. Can be either true
              or false. Defaults to true.
            minBitrateType: Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to band.
            apBandSettings: Settings that will be enabled if selectionType is set to 'ap'.
            twoFourGhzSettings: Settings related to 2.4Ghz band.
            fiveGhzSettings: Settings related to 5Ghz band.
            sixGhzSettings: Settings related to 6Ghz band. Only applicable to networks with 6Ghz
              capable APs.
            transmission: Settings related to radio transmission.
            perSsidSettings: Per-SSID radio settings by number.
            flexRadios: Flex radio settings.

        """
        kwargs.update(locals())

        if "minBitrateType" in kwargs:
            options = ["band", "ssid"]
            assert kwargs["minBitrateType"] in options, (
                f'''"minBitrateType" cannot be "{kwargs["minBitrateType"]}", & must be set to one of: {options}'''
            )
        if "bandSelectionType" in kwargs:
            options = ["ap", "ssid"]
            assert kwargs["bandSelectionType"] in options, (
                f'''"bandSelectionType" cannot be "{kwargs["bandSelectionType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "create_network_wireless_rf_profile",
        }
        resource = f"/networks/{networkId}/wireless/rfProfiles"

        body_params = [
            "name",
            "clientBalancingEnabled",
            "minBitrateType",
            "bandSelectionType",
            "apBandSettings",
            "twoFourGhzSettings",
            "fiveGhzSettings",
            "sixGhzSettings",
            "transmission",
            "perSsidSettings",
            "flexRadios",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_wireless_rf_profile(
        self, networkId: str, rfProfileId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates specified RF profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile

        Args:
            networkId: Network ID.
            rfProfileId: Rf profile ID.
            name: The name of the new profile. Must be unique.
            isIndoorDefault: Set this profile as the default indoor rf profile. If the profile ID is
              one of 'indoor' or 'outdoor',   then a new profile will be created from
              the respective ID and set as the default.
            isOutdoorDefault: Set this profile as the default outdoor rf profile. If the profile ID
              is one of 'indoor' or 'outdoor',   then a new profile will be created from
              the respective ID and set as the default.
            clientBalancingEnabled: Steers client to best available access point. Can be either true
              or false.
            minBitrateType: Minimum bitrate can be set to either 'band' or 'ssid'.
            bandSelectionType: Band selection can be set to either 'ssid' or 'ap'.
            apBandSettings: Settings that will be enabled if selectionType is set to 'ap'.
            twoFourGhzSettings: Settings related to 2.4Ghz band.
            fiveGhzSettings: Settings related to 5Ghz band.
            sixGhzSettings: Settings related to 6Ghz band. Only applicable to networks with 6Ghz
              capable APs.
            transmission: Settings related to radio transmission.
            perSsidSettings: Per-SSID radio settings by number.
            flexRadios: Flex radio settings.

        """
        kwargs.update(locals())

        if "minBitrateType" in kwargs:
            options = ["band", "ssid"]
            assert kwargs["minBitrateType"] in options, (
                f'''"minBitrateType" cannot be "{kwargs["minBitrateType"]}", & must be set to one of: {options}'''
            )
        if "bandSelectionType" in kwargs:
            options = ["ap", "ssid"]
            assert kwargs["bandSelectionType"] in options, (
                f'''"bandSelectionType" cannot be "{kwargs["bandSelectionType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "update_network_wireless_rf_profile",
        }
        resource = f"/networks/{networkId}/wireless/rfProfiles/{rfProfileId}"

        body_params = [
            "name",
            "isIndoorDefault",
            "isOutdoorDefault",
            "clientBalancingEnabled",
            "minBitrateType",
            "bandSelectionType",
            "apBandSettings",
            "twoFourGhzSettings",
            "fiveGhzSettings",
            "sixGhzSettings",
            "transmission",
            "perSsidSettings",
            "flexRadios",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_wireless_rf_profile(
        self, networkId: str, rfProfileId: str
    ) -> dict[str, Any]:
        """Delete a RF Profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile

        Args:
            networkId: Network ID.
            rfProfileId: Rf profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "delete_network_wireless_rf_profile",
        }
        resource = f"/networks/{networkId}/wireless/rfProfiles/{rfProfileId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_wireless_settings(self, networkId: str, **kwargs: Any) -> dict[str, Any]:
        """Update the wireless settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-settings

        Args:
            networkId: Network ID.
            meshingEnabled: Toggle for enabling or disabling meshing in a network.
            ipv6BridgeEnabled: Toggle for enabling or disabling IPv6 bridging in a network (Note: if
              enabled, SSIDs must also be configured to use bridge mode).
            locationAnalyticsEnabled: Toggle for enabling or disabling location analytics for your
              network.
            upgradeStrategy: The default strategy that network devices will use to perform an
              upgrade. Requires firmware version MR 26.8 or higher.
            ledLightsOn: Toggle for enabling or disabling LED lights on all APs in the network
              (making them run dark).
            namedVlans: Named VLAN settings for wireless networks.

        """
        kwargs.update(locals())

        if "upgradeStrategy" in kwargs:
            options = ["minimizeClientDowntime", "minimizeUpgradeTime"]
            assert kwargs["upgradeStrategy"] in options, (
                f'''"upgradeStrategy" cannot be "{kwargs["upgradeStrategy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "settings"],
            "operation": "update_network_wireless_settings",
        }
        resource = f"/networks/{networkId}/wireless/settings"

        body_params = [
            "meshingEnabled",
            "ipv6BridgeEnabled",
            "locationAnalyticsEnabled",
            "upgradeStrategy",
            "ledLightsOn",
            "namedVlans",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the attributes of an MR SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid

        Args:
            networkId: Network ID.
            number: Number.
            name: The name of the SSID.
            enabled: Whether or not the SSID is enabled.
            authMode: The association control method for the SSID ('open', 'open-enhanced', 'psk',
              'open-with-radius', 'open-with-nac', '8021x-meraki', '8021x-nac',
              '8021x-radius', '8021x-google', '8021x-entra', '8021x-localradius', 'ipsk-
              with-radius', 'ipsk-without-radius', 'ipsk-with-nac' or 'ipsk-with-radius-
              easy-psk').
            enterpriseAdminAccess: Whether or not an SSID is accessible by 'enterprise'
              administrators ('access disabled' or 'access enabled').
            encryptionMode: The psk encryption mode for the SSID ('wep' or 'wpa'). This param is
              only valid if the authMode is 'psk'.
            psk: The passkey for the SSID. This param is only valid if the authMode is 'psk'.
            wpaEncryptionMode: The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2
              only', 'WPA3 Transition Mode', 'WPA3 only' or 'WPA3 192-bit Security').
            dot11w: The current setting for Protected Management Frames (802.11w).
            dot11r: The current setting for 802.11r.
            splashPage: The type of splash page for the SSID ('None', 'Click-through splash page',
              'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected
              with custom RADIUS', 'Password-protected with Active Directory',
              'Password-protected with LDAP', 'SMS authentication', 'Systems Manager
              Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Microsoft Entra ID',
              'Sponsored guest', 'Cisco ISE' or 'Google Apps domain').This attribute is
              not supported for template children.
            splashGuestSponsorDomains: Array of valid sponsor email domains for sponsored guest
              splash type.
            oauth: The OAuth settings of this SSID. Only valid if splashPage is 'Google OAuth'.
            localRadius: The current setting for Local Authentication, a built-in RADIUS server on
              the access point. Only valid if authMode is '8021x-localradius'.
            ldap: The current setting for LDAP. Only valid if splashPage is 'Password-protected with
              LDAP'.
            activeDirectory: The current setting for Active Directory. Only valid if splashPage is
              'Password-protected with Active Directory'.
            radiusServers: The RADIUS 802.1X servers to be used for authentication. This param is
              only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-
              with-radius'.
            radiusProxyEnabled: If true, Meraki devices will proxy RADIUS messages through the
              Meraki cloud to the configured RADIUS auth and accounting servers.
            radiusTestingEnabled: If true, Meraki devices will periodically send Access-Request
              messages to configured RADIUS servers using identity 'meraki_8021x_test'
              to ensure that the RADIUS servers are reachable.
            radiusCalledStationId: The template of the called station identifier to be used for
              RADIUS (ex. $NODE_MAC$:$VAP_NUM$).
            radiusAuthenticationNasId: The template of the NAS identifier to be used for RADIUS
              authentication (ex. $NODE_MAC$:$VAP_NUM$).
            radiusServerTimeout: The amount of time for which a RADIUS client waits for a reply from
              the RADIUS server (must be between 1-10 seconds).
            radiusServerAttemptsLimit: The maximum number of transmit attempts after which a RADIUS
              server is failed over (must be between 1-5).
            radiusFallbackEnabled: Whether or not higher priority RADIUS servers should be retried
              after 60 seconds.
            radiusRadsec: The current settings for RADIUS RADSec.
            radiusCoaEnabled: If true, Meraki devices will act as a RADIUS Dynamic Authorization
              Server and will respond to RADIUS Change-of-Authorization and Disconnect
              messages sent by the RADIUS server.
            radiusFailoverPolicy: This policy determines how authentication requests should be
              handled in the event that all of the configured RADIUS servers are
              unreachable ('Deny access' or 'Allow access').
            radiusLoadBalancingPolicy: This policy determines which RADIUS server will be contacted
              first in an authentication attempt and the ordering of any necessary retry
              attempts ('Strict priority order' or 'Round robin').
            radiusAccountingEnabled: Whether or not RADIUS accounting is enabled. This param is only
              valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-
              radius'.
            radiusAccountingServers: The RADIUS accounting 802.1X servers to be used for
              authentication. This param is only valid if the authMode is 'open-with-
              radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled
              is 'true'.
            radiusAccountingInterimInterval: The interval (in seconds) in which accounting
              information is updated and sent to the RADIUS accounting server.
            radiusAttributeForGroupPolicies: Specify the RADIUS attribute used to look up group
              policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-
              User-Role'). Access points must receive this attribute in the RADIUS
              Access-Accept message.
            ipAssignmentMode: The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3
              roaming', 'Ethernet over GRE', 'Layer 3 roaming with a concentrator',
              'VPN' or 'Campus Gateway').
            useVlanTagging: Whether or not traffic should be directed to use specific VLANs. This
              param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3
              roaming'.
            concentratorNetworkId: The concentrator to use when the ipAssignmentMode is 'Layer 3
              roaming with a concentrator' or 'VPN'.
            secondaryConcentratorNetworkId: The secondary concentrator to use when the
              ipAssignmentMode is 'VPN'. If configured, the APs will switch to using
              this concentrator if the primary concentrator is unreachable. This param
              is optional. ('disabled' represents no secondary concentrator.).
            disassociateClientsOnVpnFailover: Disassociate clients when 'VPN' concentrator failover
              occurs in order to trigger clients to re-associate and generate new DHCP
              requests. This param is only valid if ipAssignmentMode is 'VPN'.
            vlanId: The VLAN ID used for VLAN tagging. This param is only valid when the
              ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
            defaultVlanId: The default VLAN ID used for 'all other APs'. This param is only valid
              when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'.
            apTagsAndVlanIds: The list of tags and VLAN IDs used for VLAN tagging. This param is
              only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3
              roaming'.
            walledGardenEnabled: Allow access to a configurable list of IP ranges, which users may
              access prior to sign-on.
            walledGardenRanges: Specify your walled garden by entering an array of addresses, ranges
              using CIDR notation, domain names, and domain wildcards (e.g.
              '192.168.1.1/24', '192.168.37.10/32', 'www.yahoo.com', '*.google.com']).
              Meraki's splash page is automatically included in your walled garden.
            gre: Ethernet over GRE settings.
            radiusOverride: If true, the RADIUS response can override VLAN tag. This is not valid
              when ipAssignmentMode is 'NAT mode'.
            radiusGuestVlanEnabled: Whether or not RADIUS Guest VLAN is enabled. This param is only
              valid if the authMode is 'open-with-radius' and addressing mode is not set
              to 'isolated' or 'nat' mode.
            radiusGuestVlanId: VLAN ID of the RADIUS Guest VLAN. This param is only valid if the
              authMode is 'open-with-radius' and addressing mode is not set to
              'isolated' or 'nat' mode.
            minBitrate: The minimum bitrate in Mbps of this SSID in the default indoor RF profile.
              ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54').
            bandSelection: The client-serving radio frequencies of this SSID in the default indoor
              RF profile. ('Dual band operation', '5 GHz band only' or 'Dual band
              operation with Band Steering').
            perClientBandwidthLimitUp: The upload bandwidth limit in Kbps. (0 represents no limit.).
            perClientBandwidthLimitDown: The download bandwidth limit in Kbps. (0 represents no
              limit.).
            perSsidBandwidthLimitUp: The total upload bandwidth limit in Kbps. (0 represents no
              limit.).
            perSsidBandwidthLimitDown: The total download bandwidth limit in Kbps. (0 represents no
              limit.).
            lanIsolationEnabled: Boolean indicating whether Layer 2 LAN isolation should be enabled
              or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
            visible: Boolean indicating whether APs should advertise or hide this SSID. APs will
              only broadcast this SSID if set to true.
            availableOnAllAps: Boolean indicating whether all APs should broadcast the SSID or if it
              should be restricted to APs matching any availability tags. Can only be
              false if the SSID has availability tags.
            availabilityTags: Accepts a list of tags for this SSID. If availableOnAllAps is false,
              then the SSID will only be broadcast by APs with tags matching any of the
              tags in this list.
            adaptivePolicyGroupId: Adaptive policy group ID this SSID is assigned to.
            mandatoryDhcpEnabled: If true, Mandatory DHCP will enforce that clients connecting to
              this SSID must use the IP address assigned by the DHCP server. Clients who
              use a static IP address won't be able to associate.
            adultContentFilteringEnabled: Boolean indicating whether or not adult content will be
              blocked.
            dnsRewrite: DNS servers rewrite settings.
            speedBurst: The SpeedBurst setting for this SSID'.
            namedVlans: Named VLAN settings.
            localAuthFallback: The current configuration for Local Authentication Fallback. Enables
              the Access Point (AP) to store client authentication data for a specified
              duration that can be adjusted as needed.
            radiusAccountingStartDelay: The delay (in seconds) before sending the first RADIUS
              accounting start message. Must be between 0 and 60 seconds.

        """
        kwargs.update(locals())

        if "authMode" in kwargs:
            options = [
                "8021x-entra",
                "8021x-google",
                "8021x-localradius",
                "8021x-meraki",
                "8021x-nac",
                "8021x-radius",
                "ipsk-with-nac",
                "ipsk-with-radius",
                "ipsk-with-radius-easy-psk",
                "ipsk-without-radius",
                "open",
                "open-enhanced",
                "open-with-nac",
                "open-with-radius",
                "psk",
            ]
            assert kwargs["authMode"] in options, (
                f'''"authMode" cannot be "{kwargs["authMode"]}", & must be set to one of: {options}'''
            )
        if "enterpriseAdminAccess" in kwargs:
            options = ["access disabled", "access enabled"]
            assert kwargs["enterpriseAdminAccess"] in options, (
                f'''"enterpriseAdminAccess" cannot be "{kwargs["enterpriseAdminAccess"]}", & must be set to one of: {options}'''
            )
        if "encryptionMode" in kwargs:
            options = ["open", "wep", "wpa", "wpa-eap"]
            assert kwargs["encryptionMode"] in options, (
                f'''"encryptionMode" cannot be "{kwargs["encryptionMode"]}", & must be set to one of: {options}'''
            )
        if "wpaEncryptionMode" in kwargs:
            options = [
                "WPA1 and WPA2",
                "WPA1 only",
                "WPA2 only",
                "WPA3 192-bit Security",
                "WPA3 Transition Mode",
                "WPA3 only",
            ]
            assert kwargs["wpaEncryptionMode"] in options, (
                f'''"wpaEncryptionMode" cannot be "{kwargs["wpaEncryptionMode"]}", & must be set to one of: {options}'''
            )
        if "splashPage" in kwargs:
            options = [
                "Billing",
                "Cisco ISE",
                "Click-through splash page",
                "Facebook Wi-Fi",
                "Google Apps domain",
                "Google OAuth",
                "Microsoft Entra ID",
                "None",
                "Password-protected with Active Directory",
                "Password-protected with LDAP",
                "Password-protected with Meraki RADIUS",
                "Password-protected with custom RADIUS",
                "SMS authentication",
                "Sponsored guest",
                "Systems Manager Sentry",
            ]
            assert kwargs["splashPage"] in options, (
                f'''"splashPage" cannot be "{kwargs["splashPage"]}", & must be set to one of: {options}'''
            )
        if "radiusFailoverPolicy" in kwargs:
            options = ["Allow access", "Deny access"]
            assert kwargs["radiusFailoverPolicy"] in options, (
                f'''"radiusFailoverPolicy" cannot be "{kwargs["radiusFailoverPolicy"]}", & must be set to one of: {options}'''
            )
        if "radiusLoadBalancingPolicy" in kwargs:
            options = ["Round robin", "Strict priority order"]
            assert kwargs["radiusLoadBalancingPolicy"] in options, (
                f'''"radiusLoadBalancingPolicy" cannot be "{kwargs["radiusLoadBalancingPolicy"]}", & must be set to one of: {options}'''
            )
        if "radiusAttributeForGroupPolicies" in kwargs:
            options = ["Airespace-ACL-Name", "Aruba-User-Role", "Filter-Id", "Reply-Message"]
            assert kwargs["radiusAttributeForGroupPolicies"] in options, (
                f'''"radiusAttributeForGroupPolicies" cannot be "{kwargs["radiusAttributeForGroupPolicies"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "update_network_wireless_ssid",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}"

        body_params = [
            "name",
            "enabled",
            "authMode",
            "enterpriseAdminAccess",
            "encryptionMode",
            "psk",
            "wpaEncryptionMode",
            "dot11w",
            "dot11r",
            "splashPage",
            "splashGuestSponsorDomains",
            "oauth",
            "localRadius",
            "ldap",
            "activeDirectory",
            "radiusServers",
            "radiusProxyEnabled",
            "radiusTestingEnabled",
            "radiusCalledStationId",
            "radiusAuthenticationNasId",
            "radiusServerTimeout",
            "radiusServerAttemptsLimit",
            "radiusFallbackEnabled",
            "radiusRadsec",
            "radiusCoaEnabled",
            "radiusFailoverPolicy",
            "radiusLoadBalancingPolicy",
            "radiusAccountingEnabled",
            "radiusAccountingServers",
            "radiusAccountingInterimInterval",
            "radiusAttributeForGroupPolicies",
            "ipAssignmentMode",
            "useVlanTagging",
            "concentratorNetworkId",
            "secondaryConcentratorNetworkId",
            "disassociateClientsOnVpnFailover",
            "vlanId",
            "defaultVlanId",
            "apTagsAndVlanIds",
            "walledGardenEnabled",
            "walledGardenRanges",
            "gre",
            "radiusOverride",
            "radiusGuestVlanEnabled",
            "radiusGuestVlanId",
            "minBitrate",
            "bandSelection",
            "perClientBandwidthLimitUp",
            "perClientBandwidthLimitDown",
            "perSsidBandwidthLimitUp",
            "perSsidBandwidthLimitDown",
            "lanIsolationEnabled",
            "visible",
            "availableOnAllAps",
            "availabilityTags",
            "adaptivePolicyGroupId",
            "mandatoryDhcpEnabled",
            "adultContentFilteringEnabled",
            "dnsRewrite",
            "speedBurst",
            "namedVlans",
            "localAuthFallback",
            "radiusAccountingStartDelay",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_bonjour_forwarding(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the bonjour forwarding setting and rules for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-bonjour-forwarding

        Args:
            networkId: Network ID.
            number: Number.
            enabled: If true, Bonjour forwarding is enabled on this SSID.
            rules: List of bonjour forwarding rules.
            exception: Bonjour forwarding exception.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "bonjourForwarding"],
            "operation": "update_network_wireless_ssid_bonjour_forwarding",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding"

        body_params = [
            "enabled",
            "rules",
            "exception",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_device_type_group_policies(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the device type group policies for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-device-type-group-policies

        Args:
            networkId: Network ID.
            number: Number.
            enabled: If true, the SSID device type group policies are enabled.
            deviceTypePolicies: List of device type policies.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "deviceTypeGroupPolicies"],
            "operation": "update_network_wireless_ssid_device_type_group_policies",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies"

        body_params = [
            "enabled",
            "deviceTypePolicies",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_eap_override(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the EAP overridden parameters for an SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-eap-override

        Args:
            networkId: Network ID.
            number: Number.
            timeout: General EAP timeout in seconds.
            identity: EAP settings for identity requests.
            maxRetries: Maximum number of general EAP retries.
            eapolKey: EAPOL Key settings.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "eapOverride"],
            "operation": "update_network_wireless_ssid_eap_override",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/eapOverride"

        body_params = [
            "timeout",
            "identity",
            "maxRetries",
            "eapolKey",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_firewall_l3_firewall_rules(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the L3 firewall rules of an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules

        Args:
            networkId: Network ID.
            number: Number.
            rules: An ordered array of the firewall rules for this SSID.
            allowLanAccess: Allow wireless client access to local LAN (boolean value - true allows
              access and false denies access) (optional).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l3FirewallRules"],
            "operation": "update_network_wireless_ssid_firewall_l3_firewall_rules",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules"

        body_params = [
            "rules",
            "allowLanAccess",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_firewall_l7_firewall_rules(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the L7 firewall rules of an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-7-firewall-rules

        Args:
            networkId: Network ID.
            number: Number.
            rules: An array of L7 firewall rules for this SSID. Rules will get applied in the same
              order user has specified in request. Empty array will clear the L7
              firewall rule configuration.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l7FirewallRules"],
            "operation": "update_network_wireless_ssid_firewall_l7_firewall_rules",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules"

        body_params = [
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_hotspot20(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the Hotspot 2.0 settings of an SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-hotspot-2-0

        Args:
            networkId: Network ID.
            number: Number.
            enabled: Whether or not Hotspot 2.0 for this SSID is enabled.
            operator: Operator settings for this SSID.
            venue: Venue settings for this SSID.
            networkAccessType: The network type of this SSID ('Private network', 'Private network
              with guest access', 'Chargeable public network', 'Free public network',
              'Personal device network', 'Emergency services only network', 'Test or
              experimental', 'Wildcard').
            domains: An array of domain names.
            roamConsortOis: An array of roaming consortium OIs (hexadecimal number 3-5 octets in
              length).
            mccMncs: An array of MCC/MNC pairs.
            naiRealms: An array of NAI realms.

        """
        kwargs.update(locals())

        if "networkAccessType" in kwargs:
            options = [
                "Chargeable public network",
                "Emergency services only network",
                "Free public network",
                "Personal device network",
                "Private network",
                "Private network with guest access",
                "Test or experimental",
                "Wildcard",
            ]
            assert kwargs["networkAccessType"] in options, (
                f'''"networkAccessType" cannot be "{kwargs["networkAccessType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "hotspot20"],
            "operation": "update_network_wireless_ssid_hotspot20",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/hotspot20"

        body_params = [
            "enabled",
            "operator",
            "venue",
            "networkAccessType",
            "domains",
            "roamConsortOis",
            "mccMncs",
            "naiRealms",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_wireless_ssid_identity_psk(
        self, networkId: str, number: str, name: str, groupPolicyId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create an Identity PSK.

        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-identity-psk

        Args:
            networkId: Network ID.
            number: Number.
            name: The name of the Identity PSK.
            groupPolicyId: The group policy to be applied to clients.
            passphrase: The passphrase for client authentication. If left blank, one will be auto-
              generated.
            expiresAt: Timestamp for when the Identity PSK expires. Will not expire if left blank.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "create_network_wireless_ssid_identity_psk",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks"

        body_params = [
            "name",
            "passphrase",
            "groupPolicyId",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_wireless_ssid_identity_psk(
        self, networkId: str, number: str, identityPskId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update an Identity PSK.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-identity-psk

        Args:
            networkId: Network ID.
            number: Number.
            identityPskId: Identity psk ID.
            name: The name of the Identity PSK.
            passphrase: The passphrase for client authentication.
            groupPolicyId: The group policy to be applied to clients.
            expiresAt: Timestamp for when the Identity PSK expires, or 'null' to never expire.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "update_network_wireless_ssid_identity_psk",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}"

        body_params = [
            "name",
            "passphrase",
            "groupPolicyId",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_wireless_ssid_identity_psk(
        self, networkId: str, number: str, identityPskId: str
    ) -> dict[str, Any]:
        """Delete an Identity PSK.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ssid-identity-psk

        Args:
            networkId: Network ID.
            number: Number.
            identityPskId: Identity psk ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "delete_network_wireless_ssid_identity_psk",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_wireless_ssid_open_roaming(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the OpenRoaming setting for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-open-roaming

        Args:
            networkId: Network ID.
            number: Number.
            enabled: If true, OpenRoaming is enabled on this SSID.
            tenantId: The OpenRoaming DNA Spaces tenant ID.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "openRoaming"],
            "operation": "update_network_wireless_ssid_open_roaming",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/openRoaming"

        body_params = [
            "enabled",
            "tenantId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_schedules(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the outage schedule for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-schedules

        Args:
            networkId: Network ID.
            number: Number.
            enabled: If true, the SSID outage schedule is enabled.
            ranges: List of outage ranges. Has a start date and time, and end date and time. If this
              parameter is passed in along with rangesInSeconds parameter, this will
              take precedence.
            rangesInSeconds: List of outage ranges in seconds since Sunday at Midnight. Has a start
              and end. If this parameter is passed in along with the ranges parameter,
              ranges will take precedence.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "schedules"],
            "operation": "update_network_wireless_ssid_schedules",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/schedules"

        body_params = [
            "enabled",
            "ranges",
            "rangesInSeconds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_splash_settings(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Modify the splash page settings for the given SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-splash-settings

        Args:
            networkId: Network ID.
            number: Number.
            splashUrl: [optional] The custom splash URL of the click-through splash page. Note that
              the URL can be configured without necessarily being used. In order to
              enable the custom URL, see 'useSplashUrl'.
            useSplashUrl: [optional] Boolean indicating whether the users will be redirected to the
              custom splash url. A custom splash URL must be set if this is true. Note
              that depending on your SSID's access control settings, it may not be
              possible to use the custom splash URL.
            splashTimeout: Splash timeout in minutes. This will determine how often users will see
              the splash page.
            redirectUrl: The custom redirect URL where the users will go after the splash page.
            useRedirectUrl: The Boolean indicating whether the the user will be redirected to the
              custom redirect URL after the splash page. A custom redirect URL must be
              set if this is true.
            welcomeMessage: The welcome message for the users on the splash page.
            themeId: The id of the selected splash theme.
            splashLogo: The logo used in the splash page.
            splashImage: The image used in the splash page.
            splashPrepaidFront: The prepaid front image used in the splash page.
            blockAllTrafficBeforeSignOn: How restricted allowing traffic should be. If true, all
              traffic types are blocked until the splash page is acknowledged. If false,
              all non-HTTP traffic is allowed before the splash page is acknowledged.
            controllerDisconnectionBehavior: How login attempts should be handled when the
              controller is unreachable. Can be either 'open', 'restricted', or
              'default'.
            allowSimultaneousLogins: Whether or not to allow simultaneous logins from different
              devices.
            guestSponsorship: Details associated with guest sponsored splash.
            billing: Details associated with billing splash.
            sentryEnrollment: Systems Manager sentry enrollment splash settings.
            selfRegistration: Self-registration settings for splash with Meraki authentication.

        """
        kwargs.update(locals())

        if "splashTimeout" in kwargs:
            options = [
                30,
                60,
                120,
                240,
                480,
                720,
                1080,
                1440,
                2880,
                5760,
                7200,
                10080,
                20160,
                43200,
                86400,
                129600,
            ]
            assert kwargs["splashTimeout"] in options, (
                f'''"splashTimeout" cannot be "{kwargs["splashTimeout"]}", & must be set to one of: {options}'''
            )
        if "controllerDisconnectionBehavior" in kwargs:
            options = ["default", "open", "restricted"]
            assert kwargs["controllerDisconnectionBehavior"] in options, (
                f'''"controllerDisconnectionBehavior" cannot be "{kwargs["controllerDisconnectionBehavior"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "splash", "settings"],
            "operation": "update_network_wireless_ssid_splash_settings",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/splash/settings"

        body_params = [
            "splashUrl",
            "useSplashUrl",
            "splashTimeout",
            "redirectUrl",
            "useRedirectUrl",
            "welcomeMessage",
            "themeId",
            "splashLogo",
            "splashImage",
            "splashPrepaidFront",
            "blockAllTrafficBeforeSignOn",
            "controllerDisconnectionBehavior",
            "allowSimultaneousLogins",
            "guestSponsorship",
            "billing",
            "sentryEnrollment",
            "selfRegistration",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_traffic_shaping_rules(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the traffic shaping rules for an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-traffic-shaping-rules

        Args:
            networkId: Network ID.
            number: Number.
            trafficShapingEnabled: Whether traffic shaping rules are applied to clients on your
              SSID.
            defaultRulesEnabled: Whether default traffic shaping rules are enabled (true) or
              disabled (false). There are 4 default rules, which can be seen on your
              network's traffic shaping page. Note that default rules count against the
              rule limit of 8.
            rules:     An array of traffic shaping rules. Rules are applied in the order that
              they are specified in. An empty list (or null) means no rules. Note that
              you are allowed a maximum of 8 rules. .

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "trafficShaping", "rules"],
            "operation": "update_network_wireless_ssid_traffic_shaping_rules",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules"

        body_params = [
            "trafficShapingEnabled",
            "defaultRulesEnabled",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_ssid_vpn(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the VPN settings for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-vpn

        Args:
            networkId: Network ID.
            number: Number.
            concentrator: The VPN concentrator settings for this SSID.
            splitTunnel: The VPN split tunnel settings for this SSID.
            failover: Secondary VPN concentrator settings. This is only used when two VPN
              concentrators are configured on the SSID.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "vpn"],
            "operation": "update_network_wireless_ssid_vpn",
        }
        resource = f"/networks/{networkId}/wireless/ssids/{number}/vpn"

        body_params = [
            "concentrator",
            "splitTunnel",
            "failover",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_wireless_zigbee(self, networkId: str, **kwargs: Any) -> dict[str, Any]:
        """Update Zigbee Configs for specified network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-zigbee

        Args:
            networkId: Network ID.
            enabled: To enable/disable Zigbee on the network.
            iotController: Zigbee's IoT controller details.
            lockManagement: Login Credentials of on-premises lock management.
            defaults: Default Settings for Zigbee Devices.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee"],
            "operation": "update_network_wireless_zigbee",
        }
        resource = f"/networks/{networkId}/wireless/zigbee"

        body_params = [
            "enabled",
            "iotController",
            "lockManagement",
            "defaults",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_organization_wireless_location_scanning_receiver(
        self,
        organizationId: str,
        network: dict,
        url: str,
        version: str,
        radio: dict,
        sharedSecret: str,
    ) -> dict[str, Any]:
        """Add new receiver for scanning API.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-location-scanning-receiver

        Args:
            organizationId: Organization ID.
            network: Add scanning API receiver for network.
            url: Receiver Url.
            version: Scanning API Version.
            radio: Add scanning API Radio.
            sharedSecret: Secret Value for Receiver.

        """
        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "create_organization_wireless_location_scanning_receiver",
        }
        resource = f"/organizations/{organizationId}/wireless/location/scanning/receivers"

        body_params = [
            "network",
            "url",
            "version",
            "radio",
            "sharedSecret",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_wireless_location_scanning_receiver(
        self, organizationId: str, receiverId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Change scanning API receiver settings.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-location-scanning-receiver

        Args:
            organizationId: Organization ID.
            receiverId: Receiver ID.
            url: Receiver Url.
            version: Scanning API Version.
            radio: Add scanning API Radio.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "update_organization_wireless_location_scanning_receiver",
        }
        resource = (
            f"/organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId}"
        )

        body_params = [
            "url",
            "version",
            "radio",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_wireless_location_scanning_receiver(
        self, organizationId: str, receiverId: str
    ) -> dict[str, Any]:
        """Delete a scanning API receiver.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-location-scanning-receiver

        Args:
            organizationId: Organization ID.
            receiverId: Receiver ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "delete_organization_wireless_location_scanning_receiver",
        }
        resource = (
            f"/organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId}"
        )

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_wireless_mqtt_settings(
        self, organizationId: str, network: dict, mqtt: dict, **kwargs: Any
    ) -> dict[str, Any]:
        """Add new broker config for wireless MQTT.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-mqtt-settings

        Args:
            organizationId: Organization ID.
            network: Add MQTT Settings for network.
            mqtt: MQTT Settings for network.
            ble: MQTT BLE Settings for network.
            wifi: MQTT Wi-Fi Settings for network.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "mqtt", "settings"],
            "operation": "update_organization_wireless_mqtt_settings",
        }
        resource = f"/organizations/{organizationId}/wireless/mqtt/settings"

        body_params = [
            "network",
            "mqtt",
            "ble",
            "wifi",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def recalculate_organization_wireless_radio_auto_rf_channels(
        self, organizationId: str, networkIds: list
    ) -> dict[str, Any]:
        """Recalculates automatically assigned channels for every AP within specified the specified network(s).

        https://developer.cisco.com/meraki/api-v1/#!recalculate-organization-wireless-radio-auto-rf-channels

        Args:
            organizationId: Organization ID.
            networkIds: A list of network ids (limit: 15).

        """
        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "radio", "autoRf", "channels"],
            "operation": "recalculate_organization_wireless_radio_auto_rf_channels",
        }
        resource = f"/organizations/{organizationId}/wireless/radio/autoRf/channels/recalculate"

        body_params = [
            "networkIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self, organizationId: str, client: dict, ssid: dict, network: dict, **kwargs: Any
    ) -> dict[str, Any]:
        """Create isolation allow list MAC entry for this organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-ssids-firewall-isolation-allowlist-entry

        Args:
            organizationId: Organization ID.
            client: The client of allowlist.
            ssid: The SSID that allowlist belongs to.
            network: The Network that allowlist belongs to.
            description: The description of mac address.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wireless",
                "configure",
                "ssids",
                "firewall",
                "isolation",
                "allowlist",
                "entries",
            ],
            "operation": "create_organization_wireless_ssids_firewall_isolation_allowlist_entry",
        }
        resource = (
            f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries"
        )

        body_params = [
            "description",
            "client",
            "ssid",
            "network",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self, organizationId: str, entryId: str
    ) -> dict[str, Any]:
        """Destroy isolation allow list MAC entry for this organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-ssids-firewall-isolation-allowlist-entry

        Args:
            organizationId: Organization ID.
            entryId: Entry ID.

        """
        metadata = {
            "tags": [
                "wireless",
                "configure",
                "ssids",
                "firewall",
                "isolation",
                "allowlist",
                "entries",
            ],
            "operation": "delete_organization_wireless_ssids_firewall_isolation_allowlist_entry",
        }
        resource = f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries/{entryId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self, organizationId: str, entryId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update isolation allow list MAC entry info.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-ssids-firewall-isolation-allowlist-entry

        Args:
            organizationId: Organization ID.
            entryId: Entry ID.
            description: The description of mac address.
            client: The client of allowlist.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wireless",
                "configure",
                "ssids",
                "firewall",
                "isolation",
                "allowlist",
                "entries",
            ],
            "operation": "update_organization_wireless_ssids_firewall_isolation_allowlist_entry",
        }
        resource = f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries/{entryId}"

        body_params = [
            "description",
            "client",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_wireless_zigbee_device(
        self, organizationId: str, id: str, enrolled: bool, **kwargs: Any
    ) -> dict[str, Any]:
        """Endpoint to update zigbee gateways.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-zigbee-device

        Args:
            organizationId: Organization ID.
            id: ID.
            enrolled: Parameter to enroll or unenroll the zigbee devices.
            channel: The new channel for the zigbee device.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "devices"],
            "operation": "update_organization_wireless_zigbee_device",
        }
        resource = f"/organizations/{organizationId}/wireless/zigbee/devices/{id}"

        body_params = [
            "enrolled",
            "channel",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_wireless_zigbee_door_lock(
        self, organizationId: str, doorLockId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Endpoint to batch update door locks params.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-zigbee-door-lock

        Args:
            organizationId: Organization ID.
            doorLockId: Door lock ID.
            name: Door lock name to update.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "doorLocks"],
            "operation": "update_organization_wireless_zigbee_door_lock",
        }
        resource = f"/organizations/{organizationId}/wireless/zigbee/doorLocks/{doorLockId}"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action
