"""ActionBatchAppliance API endpoints."""

import urllib
from typing import Any


class ActionBatchAppliance:
    """ActionBatchAppliance class."""

    def __init__(self) -> None:
        pass

    def update_device_appliance_radio_settings(self, serial: str, **kwargs: Any) -> dict[str, Any]:
        """Update the radio settings of an appliance.

        https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-radio-settings

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
            "tags": ["appliance", "configure", "radio", "settings"],
            "operation": "update_device_appliance_radio_settings",
        }
        resource = f"/devices/{serial}/appliance/radio/settings"

        body_params = [
            "rfProfileId",
            "twoFourGhzSettings",
            "fiveGhzSettings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_device_appliance_uplinks_settings(
        self, serial: str, interfaces: dict
    ) -> dict[str, Any]:
        """Update the uplink settings for an MX appliance.

        https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-uplinks-settings

        Args:
            serial: Serial.
            interfaces: Interface settings.

        """
        kwargs = locals()

        metadata = {
            "tags": ["appliance", "configure", "uplinks", "settings"],
            "operation": "update_device_appliance_uplinks_settings",
        }
        resource = f"/devices/{serial}/appliance/uplinks/settings"

        body_params = [
            "interfaces",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_device_appliance_vmx_authentication_token(self, serial: str) -> dict[str, Any]:
        """Generate a new vMX authentication token.

        https://developer.cisco.com/meraki/api-v1/#!create-device-appliance-vmx-authentication-token

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["appliance", "configure", "vmx", "authenticationToken"],
            "operation": "create_device_appliance_vmx_authentication_token",
        }
        resource = f"/devices/{serial}/appliance/vmx/authenticationToken"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action

    def update_network_appliance_connectivity_monitoring_destinations(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the connectivity testing destinations for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-connectivity-monitoring-destinations

        Args:
            networkId: Network ID.
            destinations: The list of connectivity monitoring destinations.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "connectivityMonitoringDestinations"],
            "operation": "update_network_appliance_connectivity_monitoring_destinations",
        }
        resource = f"/networks/{networkId}/appliance/connectivityMonitoringDestinations"

        body_params = [
            "destinations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_firewall_l7_firewall_rules(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the MX L7 firewall rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules

        Args:
            networkId: Network ID.
            rules: An ordered array of the MX L7 firewall rules.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "firewall", "l7FirewallRules"],
            "operation": "update_network_appliance_firewall_l7_firewall_rules",
        }
        resource = f"/networks/{networkId}/appliance/firewall/l7FirewallRules"

        body_params = [
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_firewall_multicast_forwarding(
        self, networkId: str, rules: list
    ) -> dict[str, Any]:
        """Update static multicast forward rules for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-multicast-forwarding

        Args:
            networkId: Network ID.
            rules: Static multicast forwarding rules. Pass an empty array to clear all rules.

        """
        kwargs = locals()

        metadata = {
            "tags": ["appliance", "configure", "firewall", "multicastForwarding"],
            "operation": "update_network_appliance_firewall_multicast_forwarding",
        }
        resource = f"/networks/{networkId}/appliance/firewall/multicastForwarding"

        body_params = [
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_port(
        self, networkId: str, portId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the per-port VLAN settings for a single MX port.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port

        Args:
            networkId: Network ID.
            portId: Port ID.
            enabled: The status of the port.
            dropUntaggedTraffic: Trunk port can Drop all Untagged traffic. When true, no VLAN is
              required. Access ports cannot have dropUntaggedTraffic set to true.
            type: The type of the port: 'access' or 'trunk'.
            vlan: Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access
              mode.
            allowedVlans: Comma-delimited list of the VLAN ID's allowed on the port, or 'all' to
              permit all VLAN's on the port.
            accessPolicy: The name of the policy. Only applicable to Access ports. Valid values are:
              'open', '8021x-radius', 'mac-radius', 'hybris-radius' for MX64 or Z3 or
              any MX supporting the per port authentication feature. Otherwise, 'open'
              is the only valid value and 'open' is the default value if the field is
              missing.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "ports"],
            "operation": "update_network_appliance_port",
        }
        resource = f"/networks/{networkId}/appliance/ports/{portId}"

        body_params = [
            "enabled",
            "dropUntaggedTraffic",
            "type",
            "vlan",
            "allowedVlans",
            "accessPolicy",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_appliance_prefixes_delegated_static(
        self, networkId: str, prefix: str, origin: dict, **kwargs: Any
    ) -> dict[str, Any]:
        """Add a static delegated prefix from a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-prefixes-delegated-static

        Args:
            networkId: Network ID.
            prefix: A static IPv6 prefix.
            origin: The origin of the prefix.
            description: A name or description for the prefix.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "prefixes", "delegated", "statics"],
            "operation": "create_network_appliance_prefixes_delegated_static",
        }
        resource = f"/networks/{networkId}/appliance/prefixes/delegated/statics"

        body_params = [
            "prefix",
            "origin",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_appliance_prefixes_delegated_static(
        self, networkId: str, staticDelegatedPrefixId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a static delegated prefix from a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-prefixes-delegated-static

        Args:
            networkId: Network ID.
            staticDelegatedPrefixId: Static delegated prefix ID.
            prefix: A static IPv6 prefix.
            origin: The origin of the prefix.
            description: A name or description for the prefix.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "prefixes", "delegated", "statics"],
            "operation": "update_network_appliance_prefixes_delegated_static",
        }
        resource = (
            f"/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}"
        )

        body_params = [
            "prefix",
            "origin",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_appliance_prefixes_delegated_static(
        self, networkId: str, staticDelegatedPrefixId: str
    ) -> dict[str, Any]:
        """Delete a static delegated prefix from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-prefixes-delegated-static

        Args:
            networkId: Network ID.
            staticDelegatedPrefixId: Static delegated prefix ID.

        """
        metadata = {
            "tags": ["appliance", "configure", "prefixes", "delegated", "statics"],
            "operation": "delete_network_appliance_prefixes_delegated_static",
        }
        resource = (
            f"/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}"
        )

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_network_appliance_rf_profile(
        self, networkId: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Creates new RF profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-rf-profile

        Args:
            networkId: Network ID.
            name: The name of the new profile. Must be unique. This param is required on creation.
            twoFourGhzSettings: Settings related to 2.4Ghz band.
            fiveGhzSettings: Settings related to 5Ghz band.
            perSsidSettings: Per-SSID radio settings by number.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "rfProfiles"],
            "operation": "create_network_appliance_rf_profile",
        }
        resource = f"/networks/{networkId}/appliance/rfProfiles"

        body_params = [
            "name",
            "twoFourGhzSettings",
            "fiveGhzSettings",
            "perSsidSettings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_appliance_rf_profile(
        self, networkId: str, rfProfileId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates specified RF profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-rf-profile

        Args:
            networkId: Network ID.
            rfProfileId: Rf profile ID.
            name: The name of the new profile. Must be unique.
            twoFourGhzSettings: Settings related to 2.4Ghz band.
            fiveGhzSettings: Settings related to 5Ghz band.
            perSsidSettings: Per-SSID radio settings by number.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "rfProfiles"],
            "operation": "update_network_appliance_rf_profile",
        }
        resource = f"/networks/{networkId}/appliance/rfProfiles/{rfProfileId}"

        body_params = [
            "name",
            "twoFourGhzSettings",
            "fiveGhzSettings",
            "perSsidSettings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_appliance_rf_profile(
        self, networkId: str, rfProfileId: str
    ) -> dict[str, Any]:
        """Delete a RF Profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-rf-profile

        Args:
            networkId: Network ID.
            rfProfileId: Rf profile ID.

        """
        metadata = {
            "tags": ["appliance", "configure", "rfProfiles"],
            "operation": "delete_network_appliance_rf_profile",
        }
        resource = f"/networks/{networkId}/appliance/rfProfiles/{rfProfileId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_appliance_sdwan_internet_policies(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update SDWAN internet traffic preferences for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-sdwan-internet-policies

        Args:
            networkId: Network ID.
            wanTrafficUplinkPreferences: policies with respective traffic filters for an MX network.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "sdwan", "internetPolicies"],
            "operation": "update_network_appliance_sdwan_internet_policies",
        }
        resource = f"/networks/{networkId}/appliance/sdwan/internetPolicies"

        body_params = [
            "wanTrafficUplinkPreferences",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_settings(self, networkId: str, **kwargs: Any) -> dict[str, Any]:
        """Update the appliance settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-settings

        Args:
            networkId: Network ID.
            clientTrackingMethod: Client tracking method of a network.
            deploymentMode: Deployment mode of a network.
            dynamicDns: Dynamic DNS settings for a network.

        """
        kwargs.update(locals())

        if "clientTrackingMethod" in kwargs:
            options = ["IP address", "MAC address", "Unique client identifier"]
            assert kwargs["clientTrackingMethod"] in options, (
                f'''"clientTrackingMethod" cannot be "{kwargs["clientTrackingMethod"]}", & must be set to one of: {options}'''
            )
        if "deploymentMode" in kwargs:
            options = ["passthrough", "routed"]
            assert kwargs["deploymentMode"] in options, (
                f'''"deploymentMode" cannot be "{kwargs["deploymentMode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["appliance", "configure", "settings"],
            "operation": "update_network_appliance_settings",
        }
        resource = f"/networks/{networkId}/appliance/settings"

        body_params = [
            "clientTrackingMethod",
            "deploymentMode",
            "dynamicDns",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_single_lan(self, networkId: str, **kwargs: Any) -> dict[str, Any]:
        """Update single LAN configuration.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-single-lan

        Args:
            networkId: Network ID.
            subnet: The subnet of the single LAN configuration.
            applianceIp: The appliance IP address of the single LAN.
            ipv6: IPv6 configuration on the VLAN.
            mandatoryDhcp: Mandatory DHCP will enforce that clients connecting to this LAN must use
              the IP address assigned by the DHCP server. Clients who use a static IP
              address won't be able to associate. Only available on firmware versions
              17.0 and above.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "singleLan"],
            "operation": "update_network_appliance_single_lan",
        }
        resource = f"/networks/{networkId}/appliance/singleLan"

        body_params = [
            "subnet",
            "applianceIp",
            "ipv6",
            "mandatoryDhcp",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_ssid(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the attributes of an MX SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-ssid

        Args:
            networkId: Network ID.
            number: Number.
            name: The name of the SSID.
            enabled: Whether or not the SSID is enabled.
            defaultVlanId: The VLAN ID of the VLAN associated to this SSID. This parameter is only
              valid if the network is in routed mode.
            authMode: The association control method for the SSID ('open', 'psk', '8021x-meraki' or
              '8021x-radius').
            psk: The passkey for the SSID. This param is only valid if the authMode is 'psk'.
            radiusServers: The RADIUS 802.1x servers to be used for authentication. This param is
              only valid if the authMode is '8021x-radius'.
            encryptionMode: The psk encryption mode for the SSID ('wep' or 'wpa'). This param is
              only valid if the authMode is 'psk'.
            wpaEncryptionMode: The types of WPA encryption. ('WPA1 and WPA2', 'WPA2 only', 'WPA3
              Transition Mode' or 'WPA3 only'). This param is only valid if (1) the
              authMode is 'psk' & the encryptionMode is 'wpa' OR (2) the authMode is
              '8021x-meraki' OR (3) the authMode is '8021x-radius'.
            visible: Boolean indicating whether the MX should advertise or hide this SSID.
            dhcpEnforcedDeauthentication: DHCP Enforced Deauthentication enables the disassociation
              of wireless clients in addition to Mandatory DHCP. This param is only
              valid on firmware versions >= MX 17.0 where the associated LAN has
              Mandatory DHCP Enabled .
            dot11w: The current setting for Protected Management Frames (802.11w).

        """
        kwargs.update(locals())

        if "authMode" in kwargs:
            options = ["8021x-meraki", "8021x-radius", "open", "psk"]
            assert kwargs["authMode"] in options, (
                f'''"authMode" cannot be "{kwargs["authMode"]}", & must be set to one of: {options}'''
            )
        if "encryptionMode" in kwargs:
            options = ["wep", "wpa"]
            assert kwargs["encryptionMode"] in options, (
                f'''"encryptionMode" cannot be "{kwargs["encryptionMode"]}", & must be set to one of: {options}'''
            )
        if "wpaEncryptionMode" in kwargs:
            options = ["WPA1 and WPA2", "WPA2 only", "WPA3 Transition Mode", "WPA3 only"]
            assert kwargs["wpaEncryptionMode"] in options, (
                f'''"wpaEncryptionMode" cannot be "{kwargs["wpaEncryptionMode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["appliance", "configure", "ssids"],
            "operation": "update_network_appliance_ssid",
        }
        resource = f"/networks/{networkId}/appliance/ssids/{number}"

        body_params = [
            "name",
            "enabled",
            "defaultVlanId",
            "authMode",
            "psk",
            "radiusServers",
            "encryptionMode",
            "wpaEncryptionMode",
            "visible",
            "dhcpEnforcedDeauthentication",
            "dot11w",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_appliance_traffic_shaping_custom_performance_class(
        self, networkId: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Add a custom performance class for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-traffic-shaping-custom-performance-class

        Args:
            networkId: Network ID.
            name: Name of the custom performance class.
            maxLatency: Maximum latency in milliseconds.
            maxJitter: Maximum jitter in milliseconds.
            maxLossPercentage: Maximum percentage of packet loss.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "trafficShaping", "customPerformanceClasses"],
            "operation": "create_network_appliance_traffic_shaping_custom_performance_class",
        }
        resource = f"/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses"

        body_params = [
            "name",
            "maxLatency",
            "maxJitter",
            "maxLossPercentage",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_appliance_traffic_shaping_custom_performance_class(
        self, networkId: str, customPerformanceClassId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a custom performance class for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-custom-performance-class

        Args:
            networkId: Network ID.
            customPerformanceClassId: Custom performance class ID.
            name: Name of the custom performance class.
            maxLatency: Maximum latency in milliseconds.
            maxJitter: Maximum jitter in milliseconds.
            maxLossPercentage: Maximum percentage of packet loss.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "trafficShaping", "customPerformanceClasses"],
            "operation": "update_network_appliance_traffic_shaping_custom_performance_class",
        }
        resource = f"/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}"

        body_params = [
            "name",
            "maxLatency",
            "maxJitter",
            "maxLossPercentage",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_appliance_traffic_shaping_custom_performance_class(
        self, networkId: str, customPerformanceClassId: str
    ) -> dict[str, Any]:
        """Delete a custom performance class from an MX network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-traffic-shaping-custom-performance-class

        Args:
            networkId: Network ID.
            customPerformanceClassId: Custom performance class ID.

        """
        metadata = {
            "tags": ["appliance", "configure", "trafficShaping", "customPerformanceClasses"],
            "operation": "delete_network_appliance_traffic_shaping_custom_performance_class",
        }
        resource = f"/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_appliance_traffic_shaping_rules(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the traffic shaping settings rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-rules

        Args:
            networkId: Network ID.
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
            "tags": ["appliance", "configure", "trafficShaping", "rules"],
            "operation": "update_network_appliance_traffic_shaping_rules",
        }
        resource = f"/networks/{networkId}/appliance/trafficShaping/rules"

        body_params = [
            "defaultRulesEnabled",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_traffic_shaping_uplink_bandwidth(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates the uplink bandwidth settings for your MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-bandwidth

        Args:
            networkId: Network ID.
            bandwidthLimits: A mapping of uplinks to their bandwidth settings (be sure to check
              which uplinks are supported for your network).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "trafficShaping", "uplinkBandwidth"],
            "operation": "update_network_appliance_traffic_shaping_uplink_bandwidth",
        }
        resource = f"/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth"

        body_params = [
            "bandwidthLimits",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_traffic_shaping_uplink_selection(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update uplink selection settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection

        Args:
            networkId: Network ID.
            activeActiveAutoVpnEnabled: Toggle for enabling or disabling active-active AutoVPN.
            defaultUplink: The default uplink. Must be a WAN interface 'wanX'.
            loadBalancingEnabled: Toggle for enabling or disabling load balancing.
            failoverAndFailback: WAN failover and failback behavior.
            wanTrafficUplinkPreferences: Array of uplink preference rules for WAN traffic.
            vpnTrafficUplinkPreferences: Array of uplink preference rules for VPN traffic.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "trafficShaping", "uplinkSelection"],
            "operation": "update_network_appliance_traffic_shaping_uplink_selection",
        }
        resource = f"/networks/{networkId}/appliance/trafficShaping/uplinkSelection"

        body_params = [
            "activeActiveAutoVpnEnabled",
            "defaultUplink",
            "loadBalancingEnabled",
            "failoverAndFailback",
            "wanTrafficUplinkPreferences",
            "vpnTrafficUplinkPreferences",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_traffic_shaping_vpn_exclusions(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update VPN exclusion rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-vpn-exclusions

        Args:
            networkId: Network ID.
            custom: Custom VPN exclusion rules. Pass an empty array to clear existing rules.
            majorApplications: Major Application based VPN exclusion rules. Pass an empty array to
              clear existing rules.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "trafficShaping", "vpnExclusions"],
            "operation": "update_network_appliance_traffic_shaping_vpn_exclusions",
        }
        resource = f"/networks/{networkId}/appliance/trafficShaping/vpnExclusions"

        body_params = [
            "custom",
            "majorApplications",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_appliance_vlan(
        self, networkId: str, id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Add a VLAN.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan

        Args:
            networkId: Network ID.
            id: The VLAN ID of the new VLAN (must be between 1 and 4094).
            name: The name of the new VLAN.
            subnet: The subnet of the VLAN.
            applianceIp: The local IP of the appliance on the VLAN.
            groupPolicyId: The id of the desired group policy to apply to the VLAN.
            templateVlanType: Type of subnetting of the VLAN. Applicable only for template network.
            cidr: CIDR of the pool of subnets. Applicable only for template network. Each network
              bound to the template will automatically pick a subnet from this pool to
              build its own VLAN.
            mask: Mask used for the subnet of all bound to the template networks. Applicable only
              for template network.
            ipv6: IPv6 configuration on the VLAN.
            dhcpHandling: The appliance's handling of DHCP requests on this VLAN. One of: 'Run a
              DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP
              requests'.
            dhcpRelayServerIps: The IPs (IPv4) of the DHCP servers that DHCP requests should be
              relayed to. CIDR/subnet notation and hostnames are not supported.
            dhcpLeaseTime: The term of DHCP leases if the appliance is running a DHCP server on this
              VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1
              week'.
            mandatoryDhcp: Mandatory DHCP will enforce that clients connecting to this VLAN must use
              the IP address assigned by the DHCP server. Clients who use a static IP
              address won't be able to associate. Only available on firmware versions
              17.0 and above.
            dhcpBootOptionsEnabled: Use DHCP boot options specified in other properties.
            dhcpBootNextServer: DHCP boot option to direct boot clients to the server to load the
              boot file from.
            dhcpBootFilename: DHCP boot option for boot filename.
            dhcpOptions: The list of DHCP options that will be included in DHCP responses. Each
              object in the list should have "code", "type", and "value" properties.

        """
        kwargs.update(locals())

        if "templateVlanType" in kwargs:
            options = ["same", "unique"]
            assert kwargs["templateVlanType"] in options, (
                f'''"templateVlanType" cannot be "{kwargs["templateVlanType"]}", & must be set to one of: {options}'''
            )
        if "dhcpHandling" in kwargs:
            options = [
                "Do not respond to DHCP requests",
                "Relay DHCP to another server",
                "Run a DHCP server",
            ]
            assert kwargs["dhcpHandling"] in options, (
                f'''"dhcpHandling" cannot be "{kwargs["dhcpHandling"]}", & must be set to one of: {options}'''
            )
        if "dhcpLeaseTime" in kwargs:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert kwargs["dhcpLeaseTime"] in options, (
                f'''"dhcpLeaseTime" cannot be "{kwargs["dhcpLeaseTime"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["appliance", "configure", "vlans"],
            "operation": "create_network_appliance_vlan",
        }
        resource = f"/networks/{networkId}/appliance/vlans"

        body_params = [
            "id",
            "name",
            "subnet",
            "applianceIp",
            "groupPolicyId",
            "templateVlanType",
            "cidr",
            "mask",
            "ipv6",
            "dhcpHandling",
            "dhcpRelayServerIps",
            "dhcpLeaseTime",
            "mandatoryDhcp",
            "dhcpBootOptionsEnabled",
            "dhcpBootNextServer",
            "dhcpBootFilename",
            "dhcpOptions",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_appliance_vlans_settings(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Enable/Disable VLANs for the given network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlans-settings

        Args:
            networkId: Network ID.
            vlansEnabled: Boolean indicating whether to enable (true) or disable (false) VLANs for
              the network.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "vlans", "settings"],
            "operation": "update_network_appliance_vlans_settings",
        }
        resource = f"/networks/{networkId}/appliance/vlans/settings"

        body_params = [
            "vlansEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_vlan(
        self, networkId: str, vlanId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a VLAN.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan

        Args:
            networkId: Network ID.
            vlanId: Vlan ID.
            name: The name of the VLAN.
            subnet: The subnet of the VLAN.
            applianceIp: The local IP of the appliance on the VLAN.
            groupPolicyId: The id of the desired group policy to apply to the VLAN.
            vpnNatSubnet: The translated VPN subnet if VPN and VPN subnet translation are enabled on
              the VLAN.
            dhcpHandling: The appliance's handling of DHCP requests on this VLAN. One of: 'Run a
              DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP
              requests'.
            dhcpRelayServerIps: The IPs (IPv4) of the DHCP servers that DHCP requests should be
              relayed to. CIDR/subnet notation and hostnames are not supported.
            dhcpLeaseTime: The term of DHCP leases if the appliance is running a DHCP server on this
              VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1
              week'.
            dhcpBootOptionsEnabled: Use DHCP boot options specified in other properties.
            dhcpBootNextServer: DHCP boot option to direct boot clients to the server to load the
              boot file from.
            dhcpBootFilename: DHCP boot option for boot filename.
            fixedIpAssignments: The DHCP fixed IP assignments on the VLAN. This should be an object
              that contains mappings from MAC addresses to objects that themselves each
              contain "ip" and "name" string fields. See the sample request/response for
              more details.
            reservedIpRanges: The DHCP reserved IP ranges on the VLAN.
            dnsNameservers: The DNS nameservers used for DHCP responses, either "upstream_dns",
              "google_dns", "opendns", or a newline seperated string of IP addresses or
              domain names.
            dhcpOptions: The list of DHCP options that will be included in DHCP responses. Each
              object in the list should have "code", "type", and "value" properties.
            templateVlanType: Type of subnetting of the VLAN. Applicable only for template network.
            cidr: CIDR of the pool of subnets. Applicable only for template network. Each network
              bound to the template will automatically pick a subnet from this pool to
              build its own VLAN.
            mask: Mask used for the subnet of all bound to the template networks. Applicable only
              for template network.
            ipv6: IPv6 configuration on the VLAN.
            mandatoryDhcp: Mandatory DHCP will enforce that clients connecting to this VLAN must use
              the IP address assigned by the DHCP server. Clients who use a static IP
              address won't be able to associate. Only available on firmware versions
              17.0 and above.

        """
        kwargs.update(locals())

        if "dhcpHandling" in kwargs:
            options = [
                "Do not respond to DHCP requests",
                "Relay DHCP to another server",
                "Run a DHCP server",
            ]
            assert kwargs["dhcpHandling"] in options, (
                f'''"dhcpHandling" cannot be "{kwargs["dhcpHandling"]}", & must be set to one of: {options}'''
            )
        if "dhcpLeaseTime" in kwargs:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert kwargs["dhcpLeaseTime"] in options, (
                f'''"dhcpLeaseTime" cannot be "{kwargs["dhcpLeaseTime"]}", & must be set to one of: {options}'''
            )
        if "templateVlanType" in kwargs:
            options = ["same", "unique"]
            assert kwargs["templateVlanType"] in options, (
                f'''"templateVlanType" cannot be "{kwargs["templateVlanType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["appliance", "configure", "vlans"],
            "operation": "update_network_appliance_vlan",
        }
        resource = f"/networks/{networkId}/appliance/vlans/{vlanId}"

        body_params = [
            "name",
            "subnet",
            "applianceIp",
            "groupPolicyId",
            "vpnNatSubnet",
            "dhcpHandling",
            "dhcpRelayServerIps",
            "dhcpLeaseTime",
            "dhcpBootOptionsEnabled",
            "dhcpBootNextServer",
            "dhcpBootFilename",
            "fixedIpAssignments",
            "reservedIpRanges",
            "dnsNameservers",
            "dhcpOptions",
            "templateVlanType",
            "cidr",
            "mask",
            "ipv6",
            "mandatoryDhcp",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_appliance_vlan(self, networkId: str, vlanId: str) -> dict[str, Any]:
        """Delete a VLAN from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan

        Args:
            networkId: Network ID.
            vlanId: Vlan ID.

        """
        metadata = {
            "tags": ["appliance", "configure", "vlans"],
            "operation": "delete_network_appliance_vlan",
        }
        resource = f"/networks/{networkId}/appliance/vlans/{vlanId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_appliance_vpn_bgp(
        self, networkId: str, enabled: bool, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a Hub BGP Configuration.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-bgp

        Args:
            networkId: Network ID.
            enabled: Boolean value to enable or disable the BGP configuration. When BGP is enabled,
              the asNumber (ASN) will be autopopulated with the preconfigured ASN at
              other Hubs or a default value if there is no ASN configured.
            asNumber: An Autonomous System Number (ASN) is required if you are to run BGP and peer
              with another BGP Speaker outside of the Auto VPN domain. This ASN will be
              applied to the entire Auto VPN domain. The entire 4-byte ASN range is
              supported. So, the ASN must be an integer between 1 and 4294967295. When
              absent, this field is not updated. If no value exists then it defaults to
              64512.
            ibgpHoldTimer: The iBGP holdtimer in seconds. The iBGP holdtimer must be an integer
              between 12 and 240. When absent, this field is not updated. If no value
              exists then it defaults to 240.
            neighbors: List of BGP neighbors. This list replaces the existing set of neighbors. When
              absent, this field is not updated.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "vpn", "bgp"],
            "operation": "update_network_appliance_vpn_bgp",
        }
        resource = f"/networks/{networkId}/appliance/vpn/bgp"

        body_params = [
            "enabled",
            "asNumber",
            "ibgpHoldTimer",
            "neighbors",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_vpn_site_to_site_vpn(
        self, networkId: str, mode: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the site-to-site VPN settings of a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn

        Args:
            networkId: Network ID.
            mode: The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'.
            hubs: The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is
              required.
            subnets: The list of subnets and their VPN presence.
            subnet: Configuration of subnet features.

        """
        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["hub", "none", "spoke"]
            assert kwargs["mode"] in options, (
                f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["appliance", "configure", "vpn", "siteToSiteVpn"],
            "operation": "update_network_appliance_vpn_site_to_site_vpn",
        }
        resource = f"/networks/{networkId}/appliance/vpn/siteToSiteVpn"

        body_params = [
            "mode",
            "hubs",
            "subnets",
            "subnet",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_appliance_warm_spare(
        self, networkId: str, enabled: bool, **kwargs: Any
    ) -> dict[str, Any]:
        """Update MX warm spare settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-warm-spare

        Args:
            networkId: Network ID.
            enabled: Enable warm spare.
            spareSerial: Serial number of the warm spare appliance.
            uplinkMode: Uplink mode, either virtual or public.
            virtualIp1: The WAN 1 shared IP.
            virtualIp2: The WAN 2 shared IP.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "warmSpare"],
            "operation": "update_network_appliance_warm_spare",
        }
        resource = f"/networks/{networkId}/appliance/warmSpare"

        body_params = [
            "enabled",
            "spareSerial",
            "uplinkMode",
            "virtualIp1",
            "virtualIp2",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def swap_network_appliance_warm_spare(self, networkId: str) -> dict[str, Any]:
        """Swap MX primary and warm spare appliances.

        https://developer.cisco.com/meraki/api-v1/#!swap-network-appliance-warm-spare

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["appliance", "configure", "warmSpare"],
            "operation": "swap_network_appliance_warm_spare",
        }
        resource = f"/networks/{networkId}/appliance/warmSpare/swap"

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action

    def create_organization_appliance_dns_local_profile(
        self, organizationId: str, name: str
    ) -> dict[str, Any]:
        """Create a new local DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-local-profile

        Args:
            organizationId: Organization ID.
            name: Name of profile.

        """
        kwargs = locals()

        metadata = {
            "tags": ["appliance", "configure", "dns", "local", "profiles"],
            "operation": "create_organization_appliance_dns_local_profile",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/local/profiles"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def bulk_organization_appliance_dns_local_profiles_assignments_create(
        self, organizationId: str, items: list
    ) -> dict[str, Any]:
        """Assign the local DNS profile to networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-appliance-dns-local-profiles-assignments-create

        Args:
            organizationId: Organization ID.
            items: List containing the network ID and Profile ID.

        """
        kwargs = locals()

        metadata = {
            "tags": ["appliance", "configure", "dns", "local", "profiles", "assignments"],
            "operation": "bulk_organization_appliance_dns_local_profiles_assignments_create",
        }
        resource = (
            f"/organizations/{organizationId}/appliance/dns/local/profiles/assignments/bulkCreate"
        )

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_organization_appliance_dns_local_profiles_assignments_bulk_delete(
        self, organizationId: str, items: list
    ) -> dict[str, Any]:
        """Unassign the local DNS profile to networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-local-profiles-assignments-bulk-delete

        Args:
            organizationId: Organization ID.
            items: List containing the assignment ID.

        """
        kwargs = locals()

        metadata = {
            "tags": [
                "appliance",
                "configure",
                "dns",
                "local",
                "profiles",
                "assignments",
                "bulkDelete",
            ],
            "operation": "create_organization_appliance_dns_local_profiles_assignments_bulk_delete",
        }
        resource = (
            f"/organizations/{organizationId}/appliance/dns/local/profiles/assignments/bulkDelete"
        )

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_appliance_dns_local_profile(
        self, organizationId: str, profileId: str, name: str
    ) -> dict[str, Any]:
        """Update a local DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-dns-local-profile

        Args:
            organizationId: Organization ID.
            profileId: Profile ID.
            name: Name of profile.

        """
        kwargs = locals()

        metadata = {
            "tags": ["appliance", "configure", "dns", "local", "profiles"],
            "operation": "update_organization_appliance_dns_local_profile",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/local/profiles/{profileId}"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_appliance_dns_local_profile(
        self, organizationId: str, profileId: str
    ) -> dict[str, Any]:
        """Deletes a local DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-appliance-dns-local-profile

        Args:
            organizationId: Organization ID.
            profileId: Profile ID.

        """
        metadata = {
            "tags": ["appliance", "configure", "dns", "local", "profiles"],
            "operation": "delete_organization_appliance_dns_local_profile",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/local/profiles/{profileId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_appliance_dns_local_record(
        self, organizationId: str, hostname: str, address: str, profile: dict
    ) -> dict[str, Any]:
        """Create a new local DNS record.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-local-record

        Args:
            organizationId: Organization ID.
            hostname: Hostname for the DNS record.
            address: IP for the DNS record.
            profile: The profile the DNS record is associated with.

        """
        kwargs = locals()

        metadata = {
            "tags": ["appliance", "configure", "dns", "local", "records"],
            "operation": "create_organization_appliance_dns_local_record",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/local/records"

        body_params = [
            "hostname",
            "address",
            "profile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_appliance_dns_local_record(
        self, organizationId: str, recordId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates a local DNS record.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-dns-local-record

        Args:
            organizationId: Organization ID.
            recordId: Record ID.
            hostname: Hostname for the DNS record.
            address: IP for the DNS record.
            profile: The profile the DNS record is associated with.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "dns", "local", "records"],
            "operation": "update_organization_appliance_dns_local_record",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/local/records/{recordId}"

        body_params = [
            "hostname",
            "address",
            "profile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_appliance_dns_local_record(
        self, organizationId: str, recordId: str
    ) -> dict[str, Any]:
        """Deletes a local DNS record.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-appliance-dns-local-record

        Args:
            organizationId: Organization ID.
            recordId: Record ID.

        """
        metadata = {
            "tags": ["appliance", "configure", "dns", "local", "records"],
            "operation": "delete_organization_appliance_dns_local_record",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/local/records/{recordId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_appliance_dns_split_profile(
        self, organizationId: str, name: str, hostnames: list, nameservers: dict
    ) -> dict[str, Any]:
        """Create a new split DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-split-profile

        Args:
            organizationId: Organization ID.
            name: Name of profile.
            hostnames: The hostname patterns to match for redirection. For more information on Split
              DNS hostname pattern formatting, please consult the Split DNS KB.
            nameservers: Contains the nameserver information for redirection.

        """
        kwargs = locals()

        metadata = {
            "tags": ["appliance", "configure", "dns", "split", "profiles"],
            "operation": "create_organization_appliance_dns_split_profile",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/split/profiles"

        body_params = [
            "name",
            "hostnames",
            "nameservers",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_organization_appliance_dns_split_profiles_assignments_bulk_create(
        self, organizationId: str, items: list
    ) -> dict[str, Any]:
        """Assign the split DNS profile to networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-split-profiles-assignments-bulk-create

        Args:
            organizationId: Organization ID.
            items: List containing the network ID and Profile ID.

        """
        kwargs = locals()

        metadata = {
            "tags": [
                "appliance",
                "configure",
                "dns",
                "split",
                "profiles",
                "assignments",
                "bulkCreate",
            ],
            "operation": "create_organization_appliance_dns_split_profiles_assignments_bulk_create",
        }
        resource = (
            f"/organizations/{organizationId}/appliance/dns/split/profiles/assignments/bulkCreate"
        )

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def create_organization_appliance_dns_split_profiles_assignments_bulk_delete(
        self, organizationId: str, items: list
    ) -> dict[str, Any]:
        """Unassign the split DNS profile to networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-split-profiles-assignments-bulk-delete

        Args:
            organizationId: Organization ID.
            items: List containing the assignment ID.

        """
        kwargs = locals()

        metadata = {
            "tags": [
                "appliance",
                "configure",
                "dns",
                "split",
                "profiles",
                "assignments",
                "bulkDelete",
            ],
            "operation": "create_organization_appliance_dns_split_profiles_assignments_bulk_delete",
        }
        resource = (
            f"/organizations/{organizationId}/appliance/dns/split/profiles/assignments/bulkDelete"
        )

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_appliance_dns_split_profile(
        self, organizationId: str, profileId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a split DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-dns-split-profile

        Args:
            organizationId: Organization ID.
            profileId: Profile ID.
            name: Name of profile.
            hostnames: The hostname patterns to match for redirection. For more information on Split
              DNS hostname pattern formatting, please consult the Split DNS KB.
            nameservers: Contains the nameserver information for redirection.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "dns", "split", "profiles"],
            "operation": "update_organization_appliance_dns_split_profile",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/split/profiles/{profileId}"

        body_params = [
            "name",
            "hostnames",
            "nameservers",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_appliance_dns_split_profile(
        self, organizationId: str, profileId: str
    ) -> dict[str, Any]:
        """Deletes a split DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-appliance-dns-split-profile

        Args:
            organizationId: Organization ID.
            profileId: Profile ID.

        """
        metadata = {
            "tags": ["appliance", "configure", "dns", "split", "profiles"],
            "operation": "delete_organization_appliance_dns_split_profile",
        }
        resource = f"/organizations/{organizationId}/appliance/dns/split/profiles/{profileId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_organization_appliance_vpn_site_to_site_ipsec_peers_slas(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the IPsec SLA policies for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-site-to-site-ipsec-peers-slas

        Args:
            organizationId: Organization ID.
            items: List of IPsec SLA policies.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["appliance", "configure", "vpn", "siteToSite", "ipsec", "peers", "slas"],
            "operation": "update_organization_appliance_vpn_site_to_site_ipsec_peers_slas",
        }
        resource = f"/organizations/{organizationId}/appliance/vpn/siteToSite/ipsec/peers/slas"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_appliance_vpn_third_party_v_p_n_peers(
        self, organizationId: str, peers: list
    ) -> dict[str, Any]:
        """Update the third party VPN peers for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-v-p-n-peers

        Args:
            organizationId: Organization ID.
            peers: The list of VPN peers.

        """
        kwargs = locals()

        metadata = {
            "tags": ["appliance", "configure", "vpn", "thirdPartyVPNPeers"],
            "operation": "update_organization_appliance_vpn_third_party_v_p_n_peers",
        }
        resource = f"/organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers"

        body_params = [
            "peers",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action
