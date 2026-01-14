"""Switch API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncSwitch:
    """Switch class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_device_switch_ports(self, *, serial: str) -> dict[str, Any] | None:
        """List the switch ports for a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["switch", "configure", "ports"],
            "operation": "get_device_switch_ports",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/ports"

        return self._session.get(metadata, resource)

    def cycle_device_switch_ports(self, *, serial: str, ports: list) -> dict[str, Any] | None:
        """Cycle a set of switch ports.

        https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports

        Args:
            serial: Serial.
            ports: List of switch ports.

        """
        metadata = {
            "tags": ["switch", "liveTools", "ports"],
            "operation": "cycle_device_switch_ports",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/ports/cycle"

        payload = {}
        if ports is not None:
            payload["ports"] = ports

        return self._session.post(metadata, resource, payload)

    def get_device_switch_ports_statuses(
        self, *, serial: str, t0: str | None = None, timespan: float | None = None
    ) -> dict[str, Any] | None:
        """Return the status for all the ports of a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses

        Args:
            serial: Serial.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.

        """
        metadata = {
            "tags": ["switch", "monitor", "ports", "statuses"],
            "operation": "get_device_switch_ports_statuses",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/ports/statuses"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(metadata, resource, params)

    def get_device_switch_ports_statuses_packets(
        self, *, serial: str, t0: str | None = None, timespan: float | None = None
    ) -> dict[str, Any] | None:
        """Return the packet counters for all the ports of a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses-packets

        Args:
            serial: Serial.
            t0: The beginning of the timespan for the data. The value is used only to determine the
              elapsed duration between t0 and the time of the request; the API snaps
              that duration to the nearest preset window (5 minutes, 15 minutes, 1 hour,
              or 1 day).
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify t0. The value must be in seconds and be less than
              or equal to 86400 seconds (1 day). The default is 1 day.

        """
        metadata = {
            "tags": ["switch", "monitor", "ports", "statuses", "packets"],
            "operation": "get_device_switch_ports_statuses_packets",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/ports/statuses/packets"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(metadata, resource, params)

    def get_device_switch_port(self, *, serial: str, port_id: str) -> dict[str, Any] | None:
        """Return a switch port.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-port

        Args:
            serial: Serial.
            port_id: Port ID.

        """
        metadata = {"tags": ["switch", "configure", "ports"], "operation": "get_device_switch_port"}
        serial = urllib.parse.quote(str(serial), safe="")
        port_id = urllib.parse.quote(str(port_id), safe="")
        resource = f"/devices/{serial}/switch/ports/{port_id}"

        return self._session.get(metadata, resource)

    def update_device_switch_port(
        self,
        *,
        serial: str,
        port_id: str,
        name: str | None = None,
        tags: list | None = None,
        enabled: bool | None = None,
        poe_enabled: bool | None = None,
        type_: str | None = None,
        vlan: int | None = None,
        voice_vlan: int | None = None,
        allowed_vlans: str | None = None,
        isolation_enabled: bool | None = None,
        rstp_enabled: bool | None = None,
        stp_guard: str | None = None,
        stp_port_fast_trunk: bool | None = None,
        link_negotiation: str | None = None,
        port_schedule_id: str | None = None,
        udld: str | None = None,
        access_policy_type: str | None = None,
        access_policy_number: int | None = None,
        mac_allow_list: list | None = None,
        mac_whitelist_limit: int | None = None,
        sticky_mac_allow_list: list | None = None,
        sticky_mac_allow_list_limit: int | None = None,
        storm_control_enabled: bool | None = None,
        adaptive_policy_group_id: str | None = None,
        peer_sgt_capable: bool | None = None,
        flexible_stacking_enabled: bool | None = None,
        dai_trusted: bool | None = None,
        profile: dict | None = None,
        dot3az: dict | None = None,
        high_speed: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a switch port.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port

        Args:
            serial: Serial.
            port_id: Port ID.
            name: The name of the switch port.
            tags: The list of tags of the switch port.
            enabled: The status of the switch port.
            poe_enabled: The PoE status of the switch port.
            type_: The type of the switch port ('access', 'trunk', 'stack', 'routed', 'svl' or
              'dad').
            vlan: The VLAN of the switch port. For a trunk port, this is the native VLAN. A null
              value will clear the value set for trunk ports.
            voice_vlan: The voice VLAN of the switch port. Only applicable to access ports.
            allowed_vlans: The VLANs allowed on the switch port. Only applicable to trunk ports.
            isolation_enabled: The isolation status of the switch port.
            rstp_enabled: The rapid spanning tree protocol status.
            stp_guard: The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop
              guard').
            stp_port_fast_trunk: The state of STP PortFast Trunk on the switch port.
            link_negotiation: The link speed for the switch port.
            port_schedule_id: The ID of the port schedule. A value of null will clear the port
              schedule.
            udld: The action to take when Unidirectional Link is detected (Alert only, Enforce).
              Default configuration is Alert only.
            access_policy_type: The type of the access policy of the switch port. Only applicable to
              access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow
              list' or 'Sticky MAC allow list'.
            access_policy_number: The number of a custom access policy to configure on the switch
              port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
            mac_allow_list: Only devices with MAC addresses specified in this list will have access
              to this port. Up to 20 MAC addresses can be defined. Only applicable when
              'accessPolicyType' is 'MAC allow list'.
            mac_whitelist_limit: The maximum number of MAC addresses for regular MAC allow list.
              Only applicable when 'accessPolicyType' is 'MAC allow list'. Note: Config
              only supported on verions greater than ms18 only for classic switches.
            sticky_mac_allow_list: The initial list of MAC addresses for sticky Mac allow list. Only
              applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
            sticky_mac_allow_list_limit: The maximum number of MAC addresses for sticky MAC allow
              list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
            storm_control_enabled: The storm control status of the switch port.
            adaptive_policy_group_id: The adaptive policy group ID that will be used to tag traffic
              through this switch port. This ID must pre-exist during the configuration,
              else needs to be created using adaptivePolicy/groups API. Cannot be
              applied to a port on a switch bound to profile.
            peer_sgt_capable: If true, Peer SGT is enabled for traffic through this switch port.
              Applicable to trunk port only, not access port. Cannot be applied to a
              port on a switch bound to profile.
            flexible_stacking_enabled: For supported switches (e.g. MS420/MS425), whether or not the
              port has flexible stacking enabled.
            dai_trusted: If true, ARP packets for this port will be considered trusted, and Dynamic
              ARP Inspection will allow the traffic.
            profile: Profile attributes.
            dot3az: dot3az settings for the port.
            high_speed: High speed port enablement settings for C9500-32QC.

        """
        if type_ is not None:
            options = ["access", "dad", "routed", "stack", "svl", "trunk"]
            assert type_ in options, (
                f'"type_" cannot be "{type_}", & must be set to one of: {options}'
            )
        if stp_guard is not None:
            options = ["bpdu guard", "disabled", "loop guard", "root guard"]
            assert stp_guard in options, (
                f'"stp_guard" cannot be "{stp_guard}", & must be set to one of: {options}'
            )
        if udld is not None:
            options = ["Alert only", "Enforce"]
            assert udld in options, f'"udld" cannot be "{udld}", & must be set to one of: {options}'
        if access_policy_type is not None:
            options = ["Custom access policy", "MAC allow list", "Open", "Sticky MAC allow list"]
            assert access_policy_type in options, (
                f'"access_policy_type" cannot be "{access_policy_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "ports"],
            "operation": "update_device_switch_port",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        port_id = urllib.parse.quote(str(port_id), safe="")
        resource = f"/devices/{serial}/switch/ports/{port_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if tags is not None:
            payload["tags"] = tags
        if enabled is not None:
            payload["enabled"] = enabled
        if poe_enabled is not None:
            payload["poeEnabled"] = poe_enabled
        if type_ is not None:
            payload["type"] = type_
        if vlan is not None:
            payload["vlan"] = vlan
        if voice_vlan is not None:
            payload["voiceVlan"] = voice_vlan
        if allowed_vlans is not None:
            payload["allowedVlans"] = allowed_vlans
        if isolation_enabled is not None:
            payload["isolationEnabled"] = isolation_enabled
        if rstp_enabled is not None:
            payload["rstpEnabled"] = rstp_enabled
        if stp_guard is not None:
            payload["stpGuard"] = stp_guard
        if stp_port_fast_trunk is not None:
            payload["stpPortFastTrunk"] = stp_port_fast_trunk
        if link_negotiation is not None:
            payload["linkNegotiation"] = link_negotiation
        if port_schedule_id is not None:
            payload["portScheduleId"] = port_schedule_id
        if udld is not None:
            payload["udld"] = udld
        if access_policy_type is not None:
            payload["accessPolicyType"] = access_policy_type
        if access_policy_number is not None:
            payload["accessPolicyNumber"] = access_policy_number
        if mac_allow_list is not None:
            payload["macAllowList"] = mac_allow_list
        if mac_whitelist_limit is not None:
            payload["macWhitelistLimit"] = mac_whitelist_limit
        if sticky_mac_allow_list is not None:
            payload["stickyMacAllowList"] = sticky_mac_allow_list
        if sticky_mac_allow_list_limit is not None:
            payload["stickyMacAllowListLimit"] = sticky_mac_allow_list_limit
        if storm_control_enabled is not None:
            payload["stormControlEnabled"] = storm_control_enabled
        if adaptive_policy_group_id is not None:
            payload["adaptivePolicyGroupId"] = adaptive_policy_group_id
        if peer_sgt_capable is not None:
            payload["peerSgtCapable"] = peer_sgt_capable
        if flexible_stacking_enabled is not None:
            payload["flexibleStackingEnabled"] = flexible_stacking_enabled
        if dai_trusted is not None:
            payload["daiTrusted"] = dai_trusted
        if profile is not None:
            payload["profile"] = profile
        if dot3az is not None:
            payload["dot3az"] = dot3az
        if high_speed is not None:
            payload["highSpeed"] = high_speed

        return self._session.put(metadata, resource, payload)

    def get_device_switch_routing_interfaces(
        self, *, serial: str, mode: str | None = None, protocol: str | None = None
    ) -> dict[str, Any] | None:
        """List layer 3 interfaces for a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interfaces

        Args:
            serial: Serial.
            mode: Optional parameter to filter L3 interfaces by mode.
            protocol: Optional parameter to filter L3 interfaces by protocol.

        """
        if mode is not None:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'
        if protocol is not None:
            options = ["ipv4", "ipv6"]
            assert protocol in options, (
                f'"protocol" cannot be "{protocol}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "get_device_switch_routing_interfaces",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces"

        params = {}
        if mode is not None:
            params["mode"] = mode
        if protocol is not None:
            params["protocol"] = protocol

        return self._session.get(metadata, resource, params)

    def create_device_switch_routing_interface(
        self,
        *,
        serial: str,
        name: str,
        mode: str | None = None,
        subnet: str | None = None,
        switch_port_id: str | None = None,
        interface_ip: str | None = None,
        multicast_routing: str | None = None,
        vlan_id: int | None = None,
        default_gateway: str | None = None,
        ospf_settings: dict | None = None,
        ipv6: dict | None = None,
        vrf: dict | None = None,
        loopback: dict | None = None,
    ) -> dict[str, Any] | None:
        """Create a layer 3 interface for a switch.

        https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface

        Args:
            serial: Serial.
            name: A friendly name or description for the interface or VLAN (max length 128
              characters).
            mode: L3 Interface mode, can be one of 'vlan', 'routed', 'loopback'. Default is 'vlan'.
              CS 17.18 or higher is required for 'routed' mode.
            subnet: The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
            switch_port_id: Switch Port ID when in Routed mode (CS 17.18 or higher required).
            interface_ip: The IP address that will be used for Layer 3 routing on this VLAN or
              subnet. This cannot be the same as the device management IP.
            multicast_routing: Enable multicast support if, multicast routing between VLANs is
              required. Options are: 'disabled', 'enabled' or 'IGMP snooping querier'.
              Default is 'disabled'.
            vlan_id: The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
            default_gateway: The next hop for any traffic that isn't going to a directly connected
              subnet or over a static route. This IP address must exist in a subnet with
              a L3 interface. Required if this is the first IPv4 interface.
            ospf_settings: The OSPF routing settings of the interface.
            ipv6: The IPv6 settings of the interface.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.
            loopback: The loopback settings of the interface.

        """
        if mode is not None:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'
        if multicast_routing is not None:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert multicast_routing in options, (
                f'"multicast_routing" cannot be "{multicast_routing}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "create_device_switch_routing_interface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces"

        payload = {}
        if name is not None:
            payload["name"] = name
        if mode is not None:
            payload["mode"] = mode
        if subnet is not None:
            payload["subnet"] = subnet
        if switch_port_id is not None:
            payload["switchPortId"] = switch_port_id
        if interface_ip is not None:
            payload["interfaceIp"] = interface_ip
        if multicast_routing is not None:
            payload["multicastRouting"] = multicast_routing
        if vlan_id is not None:
            payload["vlanId"] = vlan_id
        if default_gateway is not None:
            payload["defaultGateway"] = default_gateway
        if ospf_settings is not None:
            payload["ospfSettings"] = ospf_settings
        if ipv6 is not None:
            payload["ipv6"] = ipv6
        if vrf is not None:
            payload["vrf"] = vrf
        if loopback is not None:
            payload["loopback"] = loopback

        return self._session.post(metadata, resource, payload)

    def get_device_switch_routing_interface(
        self, *, serial: str, interface_id: str
    ) -> dict[str, Any] | None:
        """Return a layer 3 interface for a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface

        Args:
            serial: Serial.
            interface_id: Interface ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "get_device_switch_routing_interface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interface_id}"

        return self._session.get(metadata, resource)

    def update_device_switch_routing_interface(
        self,
        *,
        serial: str,
        interface_id: str,
        name: str | None = None,
        subnet: str | None = None,
        switch_port_id: str | None = None,
        interface_ip: str | None = None,
        multicast_routing: str | None = None,
        vlan_id: int | None = None,
        default_gateway: str | None = None,
        ospf_settings: dict | None = None,
        ipv6: dict | None = None,
        vrf: dict | None = None,
        loopback: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a layer 3 interface for a switch.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface

        Args:
            serial: Serial.
            interface_id: Interface ID.
            name: A friendly name or description for the interface or VLAN (max length 128
              characters).
            subnet: The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
            switch_port_id: Switch Port ID when in Routed mode (CS 17.18 or higher required).
            interface_ip: The IP address that will be used for Layer 3 routing on this VLAN or
              subnet. This cannot be the same as the device management IP.
            multicast_routing: Enable multicast support if, multicast routing between VLANs is
              required. Options are: 'disabled', 'enabled' or 'IGMP snooping querier'.
              Default is 'disabled'.
            vlan_id: The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
            default_gateway: The next hop for any traffic that isn't going to a directly connected
              subnet or over a static route. This IP address must exist in a subnet with
              a L3 interface. Required if this is the first IPv4 interface.
            ospf_settings: The OSPF routing settings of the interface.
            ipv6: The IPv6 settings of the interface.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.
            loopback: The loopback settings of the interface.

        """
        if multicast_routing is not None:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert multicast_routing in options, (
                f'"multicast_routing" cannot be "{multicast_routing}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "update_device_switch_routing_interface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interface_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if switch_port_id is not None:
            payload["switchPortId"] = switch_port_id
        if interface_ip is not None:
            payload["interfaceIp"] = interface_ip
        if multicast_routing is not None:
            payload["multicastRouting"] = multicast_routing
        if vlan_id is not None:
            payload["vlanId"] = vlan_id
        if default_gateway is not None:
            payload["defaultGateway"] = default_gateway
        if ospf_settings is not None:
            payload["ospfSettings"] = ospf_settings
        if ipv6 is not None:
            payload["ipv6"] = ipv6
        if vrf is not None:
            payload["vrf"] = vrf
        if loopback is not None:
            payload["loopback"] = loopback

        return self._session.put(metadata, resource, payload)

    def delete_device_switch_routing_interface(self, *, serial: str, interface_id: str) -> None:
        """Delete a layer 3 interface from the switch.

        https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-interface

        Args:
            serial: Serial.
            interface_id: Interface ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "delete_device_switch_routing_interface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interface_id}"

        return self._session.delete(metadata, resource)

    def get_device_switch_routing_interface_dhcp(
        self, *, serial: str, interface_id: str
    ) -> dict[str, Any] | None:
        """Return a layer 3 interface DHCP configuration for a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface-dhcp

        Args:
            serial: Serial.
            interface_id: Interface ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces", "dhcp"],
            "operation": "get_device_switch_routing_interface_dhcp",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interface_id}/dhcp"

        return self._session.get(metadata, resource)

    def update_device_switch_routing_interface_dhcp(
        self,
        *,
        serial: str,
        interface_id: str,
        dhcp_mode: str | None = None,
        dhcp_relay_server_ips: list | None = None,
        dhcp_lease_time: str | None = None,
        dns_nameservers_option: str | None = None,
        dns_custom_nameservers: list | None = None,
        boot_options_enabled: bool | None = None,
        boot_next_server: str | None = None,
        boot_file_name: str | None = None,
        dhcp_options: list | None = None,
        reserved_ip_ranges: list | None = None,
        fixed_ip_assignments: list | None = None,
    ) -> dict[str, Any] | None:
        """Update a layer 3 interface DHCP configuration for a switch.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface-dhcp

        Args:
            serial: Serial.
            interface_id: Interface ID.
            dhcp_mode: The DHCP mode options for the switch interface ('dhcpDisabled', 'dhcpRelay'
              or 'dhcpServer').
            dhcp_relay_server_ips: The DHCP relay server IPs to which DHCP packets would get relayed
              for the switch interface.
            dhcp_lease_time: The DHCP lease time config for the dhcp server running on switch
              interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1
              week').
            dns_nameservers_option: The DHCP name server option for the dhcp server running on the
              switch interface ('googlePublicDns', 'openDns' or 'custom').
            dns_custom_nameservers: The DHCP name server IPs when DHCP name server option is
              'custom'.
            boot_options_enabled: Enable DHCP boot options to provide PXE boot options configs for
              the dhcp server running on the switch interface.
            boot_next_server: The PXE boot server IP for the DHCP server running on the switch
              interface.
            boot_file_name: The PXE boot server filename for the DHCP server running on the switch
              interface.
            dhcp_options: Array of DHCP options consisting of code, type and value for the DHCP
              server running on the switch interface.
            reserved_ip_ranges: Array of DHCP reserved IP assignments for the DHCP server running on
              the switch interface.
            fixed_ip_assignments: Array of DHCP fixed IP assignments for the DHCP server running on
              the switch interface.

        """
        if dhcp_mode is not None:
            options = ["dhcpDisabled", "dhcpRelay", "dhcpServer"]
            assert dhcp_mode in options, (
                f'"dhcp_mode" cannot be "{dhcp_mode}", & must be set to one of: {options}'
            )
        if dhcp_lease_time is not None:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert dhcp_lease_time in options, (
                f'"dhcp_lease_time" cannot be "{dhcp_lease_time}", & must be set to one of: {options}'
            )
        if dns_nameservers_option is not None:
            options = ["custom", "googlePublicDns", "openDns"]
            assert dns_nameservers_option in options, (
                f'"dns_nameservers_option" cannot be "{dns_nameservers_option}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces", "dhcp"],
            "operation": "update_device_switch_routing_interface_dhcp",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interface_id}/dhcp"

        payload = {}
        if dhcp_mode is not None:
            payload["dhcpMode"] = dhcp_mode
        if dhcp_relay_server_ips is not None:
            payload["dhcpRelayServerIps"] = dhcp_relay_server_ips
        if dhcp_lease_time is not None:
            payload["dhcpLeaseTime"] = dhcp_lease_time
        if dns_nameservers_option is not None:
            payload["dnsNameserversOption"] = dns_nameservers_option
        if dns_custom_nameservers is not None:
            payload["dnsCustomNameservers"] = dns_custom_nameservers
        if boot_options_enabled is not None:
            payload["bootOptionsEnabled"] = boot_options_enabled
        if boot_next_server is not None:
            payload["bootNextServer"] = boot_next_server
        if boot_file_name is not None:
            payload["bootFileName"] = boot_file_name
        if dhcp_options is not None:
            payload["dhcpOptions"] = dhcp_options
        if reserved_ip_ranges is not None:
            payload["reservedIpRanges"] = reserved_ip_ranges
        if fixed_ip_assignments is not None:
            payload["fixedIpAssignments"] = fixed_ip_assignments

        return self._session.put(metadata, resource, payload)

    def get_device_switch_routing_static_routes(self, *, serial: str) -> dict[str, Any] | None:
        """List layer 3 static routes for a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-routes

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "get_device_switch_routing_static_routes",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes"

        return self._session.get(metadata, resource)

    def create_device_switch_routing_static_route(
        self,
        *,
        serial: str,
        subnet: str,
        next_hop_ip: str,
        name: str | None = None,
        advertise_via_ospf_enabled: bool | None = None,
        prefer_over_ospf_routes_enabled: bool | None = None,
        vrf: dict | None = None,
    ) -> dict[str, Any] | None:
        """Create a layer 3 static route for a switch.

        https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-static-route

        Args:
            serial: Serial.
            name: Name or description for layer 3 static route.
            subnet: The subnet which is routed via this static route and should be specified in CIDR
              notation (ex. 1.2.3.0/24).
            next_hop_ip: IP address of the next hop device to which the device sends its traffic for
              the subnet.
            advertise_via_ospf_enabled: Option to advertise static route via OSPF.
            prefer_over_ospf_routes_enabled: Option to prefer static route over OSPF routes.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "create_device_switch_routing_static_route",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if next_hop_ip is not None:
            payload["nextHopIp"] = next_hop_ip
        if advertise_via_ospf_enabled is not None:
            payload["advertiseViaOspfEnabled"] = advertise_via_ospf_enabled
        if prefer_over_ospf_routes_enabled is not None:
            payload["preferOverOspfRoutesEnabled"] = prefer_over_ospf_routes_enabled
        if vrf is not None:
            payload["vrf"] = vrf

        return self._session.post(metadata, resource, payload)

    def get_device_switch_routing_static_route(
        self, *, serial: str, static_route_id: str
    ) -> dict[str, Any] | None:
        """Return a layer 3 static route for a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-route

        Args:
            serial: Serial.
            static_route_id: Static route ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "get_device_switch_routing_static_route",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{static_route_id}"

        return self._session.get(metadata, resource)

    def update_device_switch_routing_static_route(
        self,
        *,
        serial: str,
        static_route_id: str,
        name: str | None = None,
        subnet: str | None = None,
        next_hop_ip: str | None = None,
        management_next_hop: str | None = None,
        advertise_via_ospf_enabled: bool | None = None,
        prefer_over_ospf_routes_enabled: bool | None = None,
        vrf: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a layer 3 static route for a switch.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-static-route

        Args:
            serial: Serial.
            static_route_id: Static route ID.
            name: Name or description for layer 3 static route.
            subnet: The subnet which is routed via this static route and should be specified in CIDR
              notation (ex. 1.2.3.0/24).
            next_hop_ip: IP address of the next hop device to which the device sends its traffic for
              the subnet.
            management_next_hop: Optional fallback IP address for management traffic.
            advertise_via_ospf_enabled: Option to advertise static route via OSPF.
            prefer_over_ospf_routes_enabled: Option to prefer static route over OSPF routes.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "update_device_switch_routing_static_route",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{static_route_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if next_hop_ip is not None:
            payload["nextHopIp"] = next_hop_ip
        if management_next_hop is not None:
            payload["managementNextHop"] = management_next_hop
        if advertise_via_ospf_enabled is not None:
            payload["advertiseViaOspfEnabled"] = advertise_via_ospf_enabled
        if prefer_over_ospf_routes_enabled is not None:
            payload["preferOverOspfRoutesEnabled"] = prefer_over_ospf_routes_enabled
        if vrf is not None:
            payload["vrf"] = vrf

        return self._session.put(metadata, resource, payload)

    def delete_device_switch_routing_static_route(
        self, *, serial: str, static_route_id: str
    ) -> None:
        """Delete a layer 3 static route for a switch.

        https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-static-route

        Args:
            serial: Serial.
            static_route_id: Static route ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "delete_device_switch_routing_static_route",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{static_route_id}"

        return self._session.delete(metadata, resource)

    def get_device_switch_warm_spare(self, *, serial: str) -> dict[str, Any] | None:
        """Return warm spare configuration for a switch.

        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-warm-spare

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["switch", "configure", "warmSpare"],
            "operation": "get_device_switch_warm_spare",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/warmSpare"

        return self._session.get(metadata, resource)

    def update_device_switch_warm_spare(
        self, *, serial: str, enabled: bool, spare_serial: str | None = None
    ) -> dict[str, Any] | None:
        """Update warm spare configuration for a switch.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-warm-spare

        Args:
            serial: Serial.
            enabled: Enable or disable warm spare for a switch.
            spare_serial: Serial number of the warm spare switch.

        """
        metadata = {
            "tags": ["switch", "configure", "warmSpare"],
            "operation": "update_device_switch_warm_spare",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/warmSpare"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if spare_serial is not None:
            payload["spareSerial"] = spare_serial

        return self._session.put(metadata, resource, payload)

    def get_network_switch_access_control_lists(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the access control lists for a MS network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-control-lists

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "accessControlLists"],
            "operation": "get_network_switch_access_control_lists",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/accessControlLists"

        return self._session.get(metadata, resource)

    def update_network_switch_access_control_lists(
        self, *, network_id: str, rules: list
    ) -> dict[str, Any] | None:
        """Update the access control lists for a MS network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-control-lists

        Args:
            network_id: Network ID.
            rules: An ordered array of the access control list rules (not including the default
              rule). An empty array will clear the rules.

        """
        metadata = {
            "tags": ["switch", "configure", "accessControlLists"],
            "operation": "update_network_switch_access_control_lists",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/accessControlLists"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return self._session.put(metadata, resource, payload)

    def get_network_switch_access_policies(self, *, network_id: str) -> dict[str, Any] | None:
        """List the access policies for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policies

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "get_network_switch_access_policies",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/accessPolicies"

        return self._session.get(metadata, resource)

    def create_network_switch_access_policy(
        self,
        *,
        network_id: str,
        name: str,
        radius_servers: list,
        radius_accounting_enabled: bool,
        radius: dict | None = None,
        guest_port_bouncing: bool | None = None,
        radius_testing_enabled: bool | None = None,
        radius_coa_support_enabled: bool | None = None,
        radius_accounting_servers: list | None = None,
        radius_group_attribute: str | None = None,
        host_mode: str | None = None,
        access_policy_type: str | None = None,
        increase_access_speed: bool | None = None,
        guest_vlan_id: int | None = None,
        dot1x: dict | None = None,
        voice_vlan_clients: bool | None = None,
        url_redirect_walled_garden_enabled: bool | None = None,
        url_redirect_walled_garden_ranges: list | None = None,
        guest_group_policy_id: str | None = None,
        guest_sgt_id: int | None = None,
    ) -> dict[str, Any] | None:
        """Create an access policy for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy

        Args:
            network_id: Network ID.
            name: Name of the access policy(max length 255).
            radius_servers: List of RADIUS servers to require connecting devices to authenticate
              against before granting network access.
            radius: Object for RADIUS Settings.
            guest_port_bouncing: If enabled, Meraki devices will periodically send access-request
              messages to these RADIUS servers.
            radius_testing_enabled: If enabled, Meraki devices will periodically send access-request
              messages to these RADIUS servers.
            radius_coa_support_enabled: Change of authentication for RADIUS re-authentication and
              disconnection.
            radius_accounting_enabled: Enable to send start, interim-update and stop messages to a
              configured RADIUS accounting server for tracking connected clients.
            radius_accounting_servers: List of RADIUS accounting servers to require connecting
              devices to authenticate against before granting network access.
            radius_group_attribute: Acceptable values are `""` for None, or `"11"` for Group
              Policies ACL.
            host_mode: Choose the Host Mode for the access policy.
            access_policy_type: Access Type of the policy. Automatically 'Hybrid authentication'
              when hostMode is 'Multi-Domain'.
            increase_access_speed: Enabling this option will make switches execute 802.1X and MAC-
              bypass authentication simultaneously so that clients authenticate faster.
              Only required when accessPolicyType is 'Hybrid Authentication.
            guest_vlan_id: ID for the guest VLAN allow unauthorized devices access to limited
              network resources.
            dot1x: 802.1x Settings.
            voice_vlan_clients: CDP/LLDP capable voice clients will be able to use this VLAN.
              Automatically true when hostMode is 'Multi-Domain'.
            url_redirect_walled_garden_enabled: Enable to restrict access for clients to a specific
              set of IP addresses or hostnames prior to authentication.
            url_redirect_walled_garden_ranges: IP address ranges, in CIDR notation, to restrict
              access for clients to a specific set of IP addresses or hostnames prior to
              authentication.
            guest_group_policy_id: Group policy Number for guest group policy.
            guest_sgt_id: Security Group Tag ID for guest group policy.

        """
        if host_mode is not None:
            options = ["Multi-Auth", "Multi-Domain", "Multi-Host", "Single-Host"]
            assert host_mode in options, (
                f'"host_mode" cannot be "{host_mode}", & must be set to one of: {options}'
            )
        if access_policy_type is not None:
            options = ["802.1x", "Hybrid authentication", "MAC authentication bypass"]
            assert access_policy_type in options, (
                f'"access_policy_type" cannot be "{access_policy_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "create_network_switch_access_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/accessPolicies"

        payload = {}
        if name is not None:
            payload["name"] = name
        if radius_servers is not None:
            payload["radiusServers"] = radius_servers
        if radius is not None:
            payload["radius"] = radius
        if guest_port_bouncing is not None:
            payload["guestPortBouncing"] = guest_port_bouncing
        if radius_testing_enabled is not None:
            payload["radiusTestingEnabled"] = radius_testing_enabled
        if radius_coa_support_enabled is not None:
            payload["radiusCoaSupportEnabled"] = radius_coa_support_enabled
        if radius_accounting_enabled is not None:
            payload["radiusAccountingEnabled"] = radius_accounting_enabled
        if radius_accounting_servers is not None:
            payload["radiusAccountingServers"] = radius_accounting_servers
        if radius_group_attribute is not None:
            payload["radiusGroupAttribute"] = radius_group_attribute
        if host_mode is not None:
            payload["hostMode"] = host_mode
        if access_policy_type is not None:
            payload["accessPolicyType"] = access_policy_type
        if increase_access_speed is not None:
            payload["increaseAccessSpeed"] = increase_access_speed
        if guest_vlan_id is not None:
            payload["guestVlanId"] = guest_vlan_id
        if dot1x is not None:
            payload["dot1x"] = dot1x
        if voice_vlan_clients is not None:
            payload["voiceVlanClients"] = voice_vlan_clients
        if url_redirect_walled_garden_enabled is not None:
            payload["urlRedirectWalledGardenEnabled"] = url_redirect_walled_garden_enabled
        if url_redirect_walled_garden_ranges is not None:
            payload["urlRedirectWalledGardenRanges"] = url_redirect_walled_garden_ranges
        if guest_group_policy_id is not None:
            payload["guestGroupPolicyId"] = guest_group_policy_id
        if guest_sgt_id is not None:
            payload["guestSgtId"] = guest_sgt_id

        return self._session.post(metadata, resource, payload)

    def get_network_switch_access_policy(
        self, *, network_id: str, access_policy_number: str
    ) -> dict[str, Any] | None:
        """Return a specific access policy for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policy

        Args:
            network_id: Network ID.
            access_policy_number: Access policy number.

        """
        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "get_network_switch_access_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        access_policy_number = urllib.parse.quote(str(access_policy_number), safe="")
        resource = f"/networks/{network_id}/switch/accessPolicies/{access_policy_number}"

        return self._session.get(metadata, resource)

    def update_network_switch_access_policy(
        self,
        *,
        network_id: str,
        access_policy_number: str,
        name: str | None = None,
        radius_servers: list | None = None,
        radius: dict | None = None,
        guest_port_bouncing: bool | None = None,
        radius_testing_enabled: bool | None = None,
        radius_coa_support_enabled: bool | None = None,
        radius_accounting_enabled: bool | None = None,
        radius_accounting_servers: list | None = None,
        radius_group_attribute: str | None = None,
        host_mode: str | None = None,
        access_policy_type: str | None = None,
        increase_access_speed: bool | None = None,
        guest_vlan_id: int | None = None,
        dot1x: dict | None = None,
        voice_vlan_clients: bool | None = None,
        url_redirect_walled_garden_enabled: bool | None = None,
        url_redirect_walled_garden_ranges: list | None = None,
        guest_group_policy_id: str | None = None,
        guest_sgt_id: int | None = None,
    ) -> dict[str, Any] | None:
        """Update an access policy for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy

        Args:
            network_id: Network ID.
            access_policy_number: Access policy number.
            name: Name of the access policy(max length 255).
            radius_servers: List of RADIUS servers to require connecting devices to authenticate
              against before granting network access.
            radius: Object for RADIUS Settings.
            guest_port_bouncing: If enabled, Meraki devices will periodically send access-request
              messages to these RADIUS servers.
            radius_testing_enabled: If enabled, Meraki devices will periodically send access-request
              messages to these RADIUS servers.
            radius_coa_support_enabled: Change of authentication for RADIUS re-authentication and
              disconnection.
            radius_accounting_enabled: Enable to send start, interim-update and stop messages to a
              configured RADIUS accounting server for tracking connected clients.
            radius_accounting_servers: List of RADIUS accounting servers to require connecting
              devices to authenticate against before granting network access.
            radius_group_attribute: Acceptable values are `""` for None, or `"11"` for Group
              Policies ACL.
            host_mode: Choose the Host Mode for the access policy.
            access_policy_type: Access Type of the policy. Automatically 'Hybrid authentication'
              when hostMode is 'Multi-Domain'.
            increase_access_speed: Enabling this option will make switches execute 802.1X and MAC-
              bypass authentication simultaneously so that clients authenticate faster.
              Only required when accessPolicyType is 'Hybrid Authentication.
            guest_vlan_id: ID for the guest VLAN allow unauthorized devices access to limited
              network resources.
            dot1x: 802.1x Settings.
            voice_vlan_clients: CDP/LLDP capable voice clients will be able to use this VLAN.
              Automatically true when hostMode is 'Multi-Domain'.
            url_redirect_walled_garden_enabled: Enable to restrict access for clients to a specific
              set of IP addresses or hostnames prior to authentication.
            url_redirect_walled_garden_ranges: IP address ranges, in CIDR notation, to restrict
              access for clients to a specific set of IP addresses or hostnames prior to
              authentication.
            guest_group_policy_id: Group policy Number for guest group policy.
            guest_sgt_id: Security Group Tag ID for guest group policy.

        """
        if host_mode is not None:
            options = ["Multi-Auth", "Multi-Domain", "Multi-Host", "Single-Host"]
            assert host_mode in options, (
                f'"host_mode" cannot be "{host_mode}", & must be set to one of: {options}'
            )
        if access_policy_type is not None:
            options = ["802.1x", "Hybrid authentication", "MAC authentication bypass"]
            assert access_policy_type in options, (
                f'"access_policy_type" cannot be "{access_policy_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "update_network_switch_access_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        access_policy_number = urllib.parse.quote(str(access_policy_number), safe="")
        resource = f"/networks/{network_id}/switch/accessPolicies/{access_policy_number}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if radius_servers is not None:
            payload["radiusServers"] = radius_servers
        if radius is not None:
            payload["radius"] = radius
        if guest_port_bouncing is not None:
            payload["guestPortBouncing"] = guest_port_bouncing
        if radius_testing_enabled is not None:
            payload["radiusTestingEnabled"] = radius_testing_enabled
        if radius_coa_support_enabled is not None:
            payload["radiusCoaSupportEnabled"] = radius_coa_support_enabled
        if radius_accounting_enabled is not None:
            payload["radiusAccountingEnabled"] = radius_accounting_enabled
        if radius_accounting_servers is not None:
            payload["radiusAccountingServers"] = radius_accounting_servers
        if radius_group_attribute is not None:
            payload["radiusGroupAttribute"] = radius_group_attribute
        if host_mode is not None:
            payload["hostMode"] = host_mode
        if access_policy_type is not None:
            payload["accessPolicyType"] = access_policy_type
        if increase_access_speed is not None:
            payload["increaseAccessSpeed"] = increase_access_speed
        if guest_vlan_id is not None:
            payload["guestVlanId"] = guest_vlan_id
        if dot1x is not None:
            payload["dot1x"] = dot1x
        if voice_vlan_clients is not None:
            payload["voiceVlanClients"] = voice_vlan_clients
        if url_redirect_walled_garden_enabled is not None:
            payload["urlRedirectWalledGardenEnabled"] = url_redirect_walled_garden_enabled
        if url_redirect_walled_garden_ranges is not None:
            payload["urlRedirectWalledGardenRanges"] = url_redirect_walled_garden_ranges
        if guest_group_policy_id is not None:
            payload["guestGroupPolicyId"] = guest_group_policy_id
        if guest_sgt_id is not None:
            payload["guestSgtId"] = guest_sgt_id

        return self._session.put(metadata, resource, payload)

    def delete_network_switch_access_policy(
        self, *, network_id: str, access_policy_number: str
    ) -> None:
        """Delete an access policy for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-access-policy

        Args:
            network_id: Network ID.
            access_policy_number: Access policy number.

        """
        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "delete_network_switch_access_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        access_policy_number = urllib.parse.quote(str(access_policy_number), safe="")
        resource = f"/networks/{network_id}/switch/accessPolicies/{access_policy_number}"

        return self._session.delete(metadata, resource)

    def get_network_switch_alternate_management_interface(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the switch alternate management interface for the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-alternate-management-interface

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "alternateManagementInterface"],
            "operation": "get_network_switch_alternate_management_interface",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/alternateManagementInterface"

        return self._session.get(metadata, resource)

    def update_network_switch_alternate_management_interface(
        self,
        *,
        network_id: str,
        enabled: bool | None = None,
        vlan_id: int | None = None,
        protocols: list | None = None,
        switches: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the switch alternate management interface for the network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-alternate-management-interface

        Args:
            network_id: Network ID.
            enabled: Boolean value to enable or disable AMI configuration. If enabled, VLAN and
              protocols must be set.
            vlan_id: Alternate management VLAN, must be between 1 and 4094.
            protocols: Can be one or more of the following values: 'radius', 'snmp' or 'syslog'.
            switches: Array of switch serial number and IP assignment. If parameter is present, it
              cannot have empty body. Note: switches parameter is not applicable for
              template networks, in other words, do not put 'switches' in the body when
              updating template networks. Also, an empty 'switches' array will remove
              all previous assignments.

        """
        metadata = {
            "tags": ["switch", "configure", "alternateManagementInterface"],
            "operation": "update_network_switch_alternate_management_interface",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/alternateManagementInterface"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if vlan_id is not None:
            payload["vlanId"] = vlan_id
        if protocols is not None:
            payload["protocols"] = protocols
        if switches is not None:
            payload["switches"] = switches

        return self._session.put(metadata, resource, payload)

    def get_network_switch_dhcp_v4_servers_seen(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day).

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-v-4-servers-seen

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.
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
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["switch", "configure", "dhcp", "v4", "servers", "seen"],
            "operation": "get_network_switch_dhcp_v4_servers_seen",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/dhcp/v4/servers/seen"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_switch_dhcp_server_policy(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the DHCP server settings.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy"],
            "operation": "get_network_switch_dhcp_server_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy"

        return self._session.get(metadata, resource)

    def update_network_switch_dhcp_server_policy(
        self,
        *,
        network_id: str,
        alerts: dict | None = None,
        default_policy: str | None = None,
        allowed_servers: list | None = None,
        blocked_servers: list | None = None,
        arp_inspection: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the DHCP server settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy

        Args:
            network_id: Network ID.
            alerts: Alert settings for DHCP servers.
            default_policy: 'allow' or 'block' new DHCP servers. Default value is 'allow'.
            allowed_servers: List the MAC addresses of DHCP servers to permit on the network when
              defaultPolicy is set to block. An empty array will clear the entries.
            blocked_servers: List the MAC addresses of DHCP servers to block on the network when
              defaultPolicy is set to allow. An empty array will clear the entries.
            arp_inspection: Dynamic ARP Inspection settings.

        """
        if default_policy is not None:
            options = ["allow", "block"]
            assert default_policy in options, (
                f'"default_policy" cannot be "{default_policy}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy"],
            "operation": "update_network_switch_dhcp_server_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy"

        payload = {}
        if alerts is not None:
            payload["alerts"] = alerts
        if default_policy is not None:
            payload["defaultPolicy"] = default_policy
        if allowed_servers is not None:
            payload["allowedServers"] = allowed_servers
        if blocked_servers is not None:
            payload["blockedServers"] = blocked_servers
        if arp_inspection is not None:
            payload["arpInspection"] = arp_inspection

        return self._session.put(metadata, resource, payload)

    def get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers(
        self,
        *,
        network_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the list of servers trusted by Dynamic ARP Inspection on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy-arp-inspection-trusted-servers

        Args:
            network_id: Network ID.
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
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_network_switch_dhcp_server_policy_arp_inspection_trusted_server(
        self, *, network_id: str, mac: str, vlan: int, ipv4: dict
    ) -> dict[str, Any] | None:
        """Add a server to be trusted by Dynamic ARP Inspection on this network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        Args:
            network_id: Network ID.
            mac: The mac address of the trusted server being added.
            vlan: The VLAN of the trusted server being added. It must be between 1 and 4094.
            ipv4: The IPv4 attributes of the trusted server being added.

        """
        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "create_network_switch_dhcp_server_policy_arp_inspection_trusted_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers"

        payload = {}
        if mac is not None:
            payload["mac"] = mac
        if vlan is not None:
            payload["vlan"] = vlan
        if ipv4 is not None:
            payload["ipv4"] = ipv4

        return self._session.post(metadata, resource, payload)

    def update_network_switch_dhcp_server_policy_arp_inspection_trusted_server(
        self,
        *,
        network_id: str,
        trusted_server_id: str,
        mac: str | None = None,
        vlan: int | None = None,
        ipv4: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a server that is trusted by Dynamic ARP Inspection on this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        Args:
            network_id: Network ID.
            trusted_server_id: Trusted server ID.
            mac: The updated mac address of the trusted server.
            vlan: The updated VLAN of the trusted server. It must be between 1 and 4094.
            ipv4: The updated IPv4 attributes of the trusted server.

        """
        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "update_network_switch_dhcp_server_policy_arp_inspection_trusted_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        trusted_server_id = urllib.parse.quote(str(trusted_server_id), safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trusted_server_id}"

        payload = {}
        if mac is not None:
            payload["mac"] = mac
        if vlan is not None:
            payload["vlan"] = vlan
        if ipv4 is not None:
            payload["ipv4"] = ipv4

        return self._session.put(metadata, resource, payload)

    def delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server(
        self, *, network_id: str, trusted_server_id: str
    ) -> None:
        """Remove a server from being trusted by Dynamic ARP Inspection on this network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        Args:
            network_id: Network ID.
            trusted_server_id: Trusted server ID.

        """
        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        trusted_server_id = urllib.parse.quote(str(trusted_server_id), safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trusted_server_id}"

        return self._session.delete(metadata, resource)

    def get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device(
        self,
        *,
        network_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the devices that have a Dynamic ARP Inspection warning and their warnings.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy-arp-inspection-warnings-by-device

        Args:
            network_id: Network ID.
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
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": [
                "switch",
                "configure",
                "dhcpServerPolicy",
                "arpInspection",
                "warnings",
                "byDevice",
            ],
            "operation": "get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_switch_dscp_to_cos_mappings(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the DSCP to CoS mappings.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dscp-to-cos-mappings

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "dscpToCosMappings"],
            "operation": "get_network_switch_dscp_to_cos_mappings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/dscpToCosMappings"

        return self._session.get(metadata, resource)

    def update_network_switch_dscp_to_cos_mappings(
        self, *, network_id: str, mappings: list
    ) -> dict[str, Any] | None:
        """Update the DSCP to CoS mappings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings

        Args:
            network_id: Network ID.
            mappings: An array of DSCP to CoS mappings. An empty array will reset the mappings to
              default.

        """
        metadata = {
            "tags": ["switch", "configure", "dscpToCosMappings"],
            "operation": "update_network_switch_dscp_to_cos_mappings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/dscpToCosMappings"

        payload = {}
        if mappings is not None:
            payload["mappings"] = mappings

        return self._session.put(metadata, resource, payload)

    def get_network_switch_link_aggregations(self, *, network_id: str) -> dict[str, Any] | None:
        """List link aggregation groups.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-link-aggregations

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "get_network_switch_link_aggregations",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/linkAggregations"

        return self._session.get(metadata, resource)

    def create_network_switch_link_aggregation(
        self,
        *,
        network_id: str,
        switch_ports: list | None = None,
        switch_profile_ports: list | None = None,
    ) -> dict[str, Any] | None:
        """Create a link aggregation group.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-link-aggregation

        Args:
            network_id: Network ID.
            switch_ports: Array of switch or stack ports for creating aggregation group. Minimum 2
              and maximum 8 ports are supported.
            switch_profile_ports: Array of switch profile ports for creating aggregation group.
              Minimum 2 and maximum 8 ports are supported.

        """
        metadata = {
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "create_network_switch_link_aggregation",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/linkAggregations"

        payload = {}
        if switch_ports is not None:
            payload["switchPorts"] = switch_ports
        if switch_profile_ports is not None:
            payload["switchProfilePorts"] = switch_profile_ports

        return self._session.post(metadata, resource, payload)

    def update_network_switch_link_aggregation(
        self,
        *,
        network_id: str,
        link_aggregation_id: str,
        switch_ports: list | None = None,
        switch_profile_ports: list | None = None,
    ) -> dict[str, Any] | None:
        """Update a link aggregation group.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-link-aggregation

        Args:
            network_id: Network ID.
            link_aggregation_id: Link aggregation ID.
            switch_ports: Array of switch or stack ports for updating aggregation group. Minimum 2
              and maximum 8 ports are supported.
            switch_profile_ports: Array of switch profile ports for updating aggregation group.
              Minimum 2 and maximum 8 ports are supported.

        """
        metadata = {
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "update_network_switch_link_aggregation",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        link_aggregation_id = urllib.parse.quote(str(link_aggregation_id), safe="")
        resource = f"/networks/{network_id}/switch/linkAggregations/{link_aggregation_id}"

        payload = {}
        if switch_ports is not None:
            payload["switchPorts"] = switch_ports
        if switch_profile_ports is not None:
            payload["switchProfilePorts"] = switch_profile_ports

        return self._session.put(metadata, resource, payload)

    def delete_network_switch_link_aggregation(
        self, *, network_id: str, link_aggregation_id: str
    ) -> None:
        """Split a link aggregation group into separate ports.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-link-aggregation

        Args:
            network_id: Network ID.
            link_aggregation_id: Link aggregation ID.

        """
        metadata = {
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "delete_network_switch_link_aggregation",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        link_aggregation_id = urllib.parse.quote(str(link_aggregation_id), safe="")
        resource = f"/networks/{network_id}/switch/linkAggregations/{link_aggregation_id}"

        return self._session.delete(metadata, resource)

    def get_network_switch_mtu(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the MTU configuration.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-mtu

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["switch", "configure", "mtu"], "operation": "get_network_switch_mtu"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/mtu"

        return self._session.get(metadata, resource)

    def update_network_switch_mtu(
        self, *, network_id: str, default_mtu_size: int | None = None, overrides: list | None = None
    ) -> dict[str, Any] | None:
        """Update the MTU configuration.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-mtu

        Args:
            network_id: Network ID.
            default_mtu_size: MTU size for the entire network. Default value is 9578.
            overrides: Override MTU size for individual switches or switch templates. An empty array
              will clear overrides.

        """
        metadata = {
            "tags": ["switch", "configure", "mtu"],
            "operation": "update_network_switch_mtu",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/mtu"

        payload = {}
        if default_mtu_size is not None:
            payload["defaultMtuSize"] = default_mtu_size
        if overrides is not None:
            payload["overrides"] = overrides

        return self._session.put(metadata, resource, payload)

    def get_network_switch_port_schedules(self, *, network_id: str) -> dict[str, Any] | None:
        """List switch port schedules.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-port-schedules

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "get_network_switch_port_schedules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/portSchedules"

        return self._session.get(metadata, resource)

    def create_network_switch_port_schedule(
        self, *, network_id: str, name: str, port_schedule: dict | None = None
    ) -> dict[str, Any] | None:
        """Add a switch port schedule.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-port-schedule

        Args:
            network_id: Network ID.
            name: The name for your port schedule. Required.
            port_schedule: The schedule for switch port scheduling. Schedules are applied to days of
              the week. When it's empty, default schedule with all days of a week are
              configured. Any unspecified day in the schedule is added as a default
              schedule configuration of the day.

        """
        metadata = {
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "create_network_switch_port_schedule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/portSchedules"

        payload = {}
        if name is not None:
            payload["name"] = name
        if port_schedule is not None:
            payload["portSchedule"] = port_schedule

        return self._session.post(metadata, resource, payload)

    def delete_network_switch_port_schedule(
        self, *, network_id: str, port_schedule_id: str
    ) -> None:
        """Delete a switch port schedule.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-port-schedule

        Args:
            network_id: Network ID.
            port_schedule_id: Port schedule ID.

        """
        metadata = {
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "delete_network_switch_port_schedule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        port_schedule_id = urllib.parse.quote(str(port_schedule_id), safe="")
        resource = f"/networks/{network_id}/switch/portSchedules/{port_schedule_id}"

        return self._session.delete(metadata, resource)

    def update_network_switch_port_schedule(
        self,
        *,
        network_id: str,
        port_schedule_id: str,
        name: str | None = None,
        port_schedule: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a switch port schedule.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-port-schedule

        Args:
            network_id: Network ID.
            port_schedule_id: Port schedule ID.
            name: The name for your port schedule.
            port_schedule: The schedule for switch port scheduling. Schedules are applied to days of
              the week. When it's empty, default schedule with all days of a week are
              configured. Any unspecified day in the schedule is added as a default
              schedule configuration of the day.

        """
        metadata = {
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "update_network_switch_port_schedule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        port_schedule_id = urllib.parse.quote(str(port_schedule_id), safe="")
        resource = f"/networks/{network_id}/switch/portSchedules/{port_schedule_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if port_schedule is not None:
            payload["portSchedule"] = port_schedule

        return self._session.put(metadata, resource, payload)

    def get_network_switch_qos_rules(self, *, network_id: str) -> dict[str, Any] | None:
        """List quality of service rules.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "get_network_switch_qos_rules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/qosRules"

        return self._session.get(metadata, resource)

    def create_network_switch_qos_rule(
        self,
        *,
        network_id: str,
        vlan: int,
        protocol: str | None = None,
        src_port: int | None = None,
        src_port_range: str | None = None,
        dst_port: int | None = None,
        dst_port_range: str | None = None,
        dscp: int | None = None,
    ) -> dict[str, Any] | None:
        """Add a quality of service rule.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-qos-rule

        Args:
            network_id: Network ID.
            vlan: The VLAN of the incoming packet. A null value will match any VLAN.
            protocol: The protocol of the incoming packet. Default value is "ANY".
            src_port: The source port of the incoming packet. Applicable only if protocol is TCP or
              UDP.
            src_port_range: The source port range of the incoming packet. Applicable only if
              protocol is set to TCP or UDP.
            dst_port: The destination port of the incoming packet. Applicable only if protocol is
              TCP or UDP.
            dst_port_range: The destination port range of the incoming packet. Applicable only if
              protocol is set to TCP or UDP.
            dscp: DSCP tag for the incoming packet. Set this to -1 to trust incoming DSCP. Default
              value is 0.

        """
        if protocol is not None:
            options = ["ANY", "TCP", "UDP"]
            assert protocol in options, (
                f'"protocol" cannot be "{protocol}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "create_network_switch_qos_rule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/qosRules"

        payload = {}
        if vlan is not None:
            payload["vlan"] = vlan
        if protocol is not None:
            payload["protocol"] = protocol
        if src_port is not None:
            payload["srcPort"] = src_port
        if src_port_range is not None:
            payload["srcPortRange"] = src_port_range
        if dst_port is not None:
            payload["dstPort"] = dst_port
        if dst_port_range is not None:
            payload["dstPortRange"] = dst_port_range
        if dscp is not None:
            payload["dscp"] = dscp

        return self._session.post(metadata, resource, payload)

    def get_network_switch_qos_rules_order(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the quality of service rule IDs by order in which they will be processed by the switch.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules-order

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "qosRules", "order"],
            "operation": "get_network_switch_qos_rules_order",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/qosRules/order"

        return self._session.get(metadata, resource)

    def update_network_switch_qos_rules_order(
        self, *, network_id: str, rule_ids: list
    ) -> dict[str, Any] | None:
        """Update the order in which the rules should be processed by the switch.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order

        Args:
            network_id: Network ID.
            rule_ids: A list of quality of service rule IDs arranged in order in which they should
              be processed by the switch.

        """
        metadata = {
            "tags": ["switch", "configure", "qosRules", "order"],
            "operation": "update_network_switch_qos_rules_order",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/qosRules/order"

        payload = {}
        if rule_ids is not None:
            payload["ruleIds"] = rule_ids

        return self._session.put(metadata, resource, payload)

    def get_network_switch_qos_rule(
        self, *, network_id: str, qos_rule_id: str
    ) -> dict[str, Any] | None:
        """Return a quality of service rule.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rule

        Args:
            network_id: Network ID.
            qos_rule_id: Qos rule ID.

        """
        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "get_network_switch_qos_rule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        qos_rule_id = urllib.parse.quote(str(qos_rule_id), safe="")
        resource = f"/networks/{network_id}/switch/qosRules/{qos_rule_id}"

        return self._session.get(metadata, resource)

    def delete_network_switch_qos_rule(self, *, network_id: str, qos_rule_id: str) -> None:
        """Delete a quality of service rule.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule

        Args:
            network_id: Network ID.
            qos_rule_id: Qos rule ID.

        """
        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "delete_network_switch_qos_rule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        qos_rule_id = urllib.parse.quote(str(qos_rule_id), safe="")
        resource = f"/networks/{network_id}/switch/qosRules/{qos_rule_id}"

        return self._session.delete(metadata, resource)

    def update_network_switch_qos_rule(
        self,
        *,
        network_id: str,
        qos_rule_id: str,
        vlan: int | None = None,
        protocol: str | None = None,
        src_port: int | None = None,
        src_port_range: str | None = None,
        dst_port: int | None = None,
        dst_port_range: str | None = None,
        dscp: int | None = None,
    ) -> dict[str, Any] | None:
        """Update a quality of service rule.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule

        Args:
            network_id: Network ID.
            qos_rule_id: Qos rule ID.
            vlan: The VLAN of the incoming packet. A null value will match any VLAN.
            protocol: The protocol of the incoming packet. Default value is "ANY".
            src_port: The source port of the incoming packet. Applicable only if protocol is TCP or
              UDP.
            src_port_range: The source port range of the incoming packet. Applicable only if
              protocol is set to TCP or UDP.
            dst_port: The destination port of the incoming packet. Applicable only if protocol is
              TCP or UDP.
            dst_port_range: The destination port range of the incoming packet. Applicable only if
              protocol is set to TCP or UDP.
            dscp: DSCP tag that should be assigned to incoming packet. Set this to -1 to trust
              incoming DSCP. Default value is 0.

        """
        if protocol is not None:
            options = ["ANY", "TCP", "UDP"]
            assert protocol in options, (
                f'"protocol" cannot be "{protocol}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "update_network_switch_qos_rule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        qos_rule_id = urllib.parse.quote(str(qos_rule_id), safe="")
        resource = f"/networks/{network_id}/switch/qosRules/{qos_rule_id}"

        payload = {}
        if vlan is not None:
            payload["vlan"] = vlan
        if protocol is not None:
            payload["protocol"] = protocol
        if src_port is not None:
            payload["srcPort"] = src_port
        if src_port_range is not None:
            payload["srcPortRange"] = src_port_range
        if dst_port is not None:
            payload["dstPort"] = dst_port
        if dst_port_range is not None:
            payload["dstPortRange"] = dst_port_range
        if dscp is not None:
            payload["dscp"] = dscp

        return self._session.put(metadata, resource, payload)

    def get_network_switch_routing_multicast(self, *, network_id: str) -> dict[str, Any] | None:
        """Return multicast settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "multicast"],
            "operation": "get_network_switch_routing_multicast",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast"

        return self._session.get(metadata, resource)

    def update_network_switch_routing_multicast(
        self,
        *,
        network_id: str,
        default_settings: dict | None = None,
        overrides: list | None = None,
    ) -> dict[str, Any] | None:
        """Update multicast settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast

        Args:
            network_id: Network ID.
            default_settings: Default multicast setting for entire network. IGMP snooping and Flood
              unknown multicast traffic settings are enabled by default.
            overrides: Array of paired switches/stacks/profiles and corresponding multicast
              settings. An empty array will clear the multicast settings.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "multicast"],
            "operation": "update_network_switch_routing_multicast",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast"

        payload = {}
        if default_settings is not None:
            payload["defaultSettings"] = default_settings
        if overrides is not None:
            payload["overrides"] = overrides

        return self._session.put(metadata, resource, payload)

    def get_network_switch_routing_multicast_rendezvous_points(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List multicast rendezvous points.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-points

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "get_network_switch_routing_multicast_rendezvous_points",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast/rendezvousPoints"

        return self._session.get(metadata, resource)

    def create_network_switch_routing_multicast_rendezvous_point(
        self, *, network_id: str, interface_ip: str, multicast_group: str, vrf: dict | None = None
    ) -> dict[str, Any] | None:
        """Create a multicast rendezvous point.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-routing-multicast-rendezvous-point

        Args:
            network_id: Network ID.
            interface_ip: The IP address of the interface where the RP needs to be created.
            multicast_group: 'Any', or the IP address of a multicast group.
            vrf: The VRF with PIM enabled L3 interface.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "create_network_switch_routing_multicast_rendezvous_point",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast/rendezvousPoints"

        payload = {}
        if interface_ip is not None:
            payload["interfaceIp"] = interface_ip
        if multicast_group is not None:
            payload["multicastGroup"] = multicast_group
        if vrf is not None:
            payload["vrf"] = vrf

        return self._session.post(metadata, resource, payload)

    def get_network_switch_routing_multicast_rendezvous_point(
        self, *, network_id: str, rendezvous_point_id: str
    ) -> dict[str, Any] | None:
        """Return a multicast rendezvous point.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-point

        Args:
            network_id: Network ID.
            rendezvous_point_id: Rendezvous point ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "get_network_switch_routing_multicast_rendezvous_point",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        rendezvous_point_id = urllib.parse.quote(str(rendezvous_point_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}"

        return self._session.get(metadata, resource)

    def delete_network_switch_routing_multicast_rendezvous_point(
        self, *, network_id: str, rendezvous_point_id: str
    ) -> None:
        """Delete a multicast rendezvous point.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-routing-multicast-rendezvous-point

        Args:
            network_id: Network ID.
            rendezvous_point_id: Rendezvous point ID.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "delete_network_switch_routing_multicast_rendezvous_point",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        rendezvous_point_id = urllib.parse.quote(str(rendezvous_point_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}"

        return self._session.delete(metadata, resource)

    def update_network_switch_routing_multicast_rendezvous_point(
        self,
        *,
        network_id: str,
        rendezvous_point_id: str,
        interface_ip: str,
        multicast_group: str,
        vrf: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a multicast rendezvous point.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point

        Args:
            network_id: Network ID.
            rendezvous_point_id: Rendezvous point ID.
            interface_ip: The IP address of the interface where the RP needs to be created.
            multicast_group: 'Any', or the IP address of a multicast group.
            vrf: The VRF with PIM enabled L3 interface.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "update_network_switch_routing_multicast_rendezvous_point",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        rendezvous_point_id = urllib.parse.quote(str(rendezvous_point_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}"

        payload = {}
        if interface_ip is not None:
            payload["interfaceIp"] = interface_ip
        if multicast_group is not None:
            payload["multicastGroup"] = multicast_group
        if vrf is not None:
            payload["vrf"] = vrf

        return self._session.put(metadata, resource, payload)

    def get_network_switch_routing_ospf(
        self, *, network_id: str, vrf: str | None = None
    ) -> dict[str, Any] | None:
        """Return layer 3 OSPF routing configuration.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-ospf

        Args:
            network_id: Network ID.
            vrf: The VRF to return the OSPF routing configuration for. When not provided, the
              default VRF is used. Included on networks with IOS XE 17.18 or higher.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "ospf"],
            "operation": "get_network_switch_routing_ospf",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/ospf"

        params = {}
        if vrf is not None:
            params["vrf"] = vrf

        return self._session.get(metadata, resource, params)

    def update_network_switch_routing_ospf(
        self,
        *,
        network_id: str,
        vrf: str | None = None,
        enabled: bool | None = None,
        hello_timer_in_seconds: int | None = None,
        dead_timer_in_seconds: int | None = None,
        areas: list | None = None,
        v3: dict | None = None,
        md5_authentication_enabled: bool | None = None,
        md5_authentication_key: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update layer 3 OSPF routing configuration.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-ospf

        Args:
            network_id: Network ID.
            vrf: The VRF to return the OSPF routing configuration for. When not provided, the
              default VRF is used. Requires IOS XE 17.18 or higher.
            enabled: Boolean value to enable or disable OSPF routing. OSPF routing is disabled by
              default.
            hello_timer_in_seconds: Time interval in seconds at which hello packet will be sent to
              OSPF neighbors to maintain connectivity. Value must be between 1 and 255.
              Default is 10 seconds.
            dead_timer_in_seconds: Time interval to determine when the peer will be declared
              inactive/dead. Value must be between 1 and 65535.
            areas: OSPF areas.
            v3: OSPF v3 configuration.
            md5_authentication_enabled: Boolean value to enable or disable MD5 authentication. MD5
              authentication is disabled by default.
            md5_authentication_key: MD5 authentication credentials. This param is only relevant if
              md5AuthenticationEnabled is true.

        """
        metadata = {
            "tags": ["switch", "configure", "routing", "ospf"],
            "operation": "update_network_switch_routing_ospf",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/routing/ospf"

        params = {}
        if vrf is not None:
            params["vrf"] = vrf

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if hello_timer_in_seconds is not None:
            payload["helloTimerInSeconds"] = hello_timer_in_seconds
        if dead_timer_in_seconds is not None:
            payload["deadTimerInSeconds"] = dead_timer_in_seconds
        if areas is not None:
            payload["areas"] = areas
        if v3 is not None:
            payload["v3"] = v3
        if md5_authentication_enabled is not None:
            payload["md5AuthenticationEnabled"] = md5_authentication_enabled
        if md5_authentication_key is not None:
            payload["md5AuthenticationKey"] = md5_authentication_key

        return self._session.put(metadata, resource, payload)

    def get_network_switch_settings(self, *, network_id: str) -> dict[str, Any] | None:
        """Returns the switch network settings.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-settings

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "settings"],
            "operation": "get_network_switch_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/settings"

        return self._session.get(metadata, resource)

    def update_network_switch_settings(
        self,
        *,
        network_id: str,
        vlan: int | None = None,
        use_combined_power: bool | None = None,
        power_exceptions: list | None = None,
        uplink_client_sampling: dict | None = None,
        mac_blocklist: dict | None = None,
        uplink_selection: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update switch network settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-settings

        Args:
            network_id: Network ID.
            vlan: Management VLAN.
            use_combined_power: The use Combined Power as the default behavior of secondary power
              supplies on supported devices.
            power_exceptions: Exceptions on a per switch basis to "useCombinedPower".
            uplink_client_sampling: Uplink client sampling.
            mac_blocklist: MAC blocklist.
            uplink_selection: Settings related to uplink selection on IOS-XE switches.

        """
        metadata = {
            "tags": ["switch", "configure", "settings"],
            "operation": "update_network_switch_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/settings"

        payload = {}
        if vlan is not None:
            payload["vlan"] = vlan
        if use_combined_power is not None:
            payload["useCombinedPower"] = use_combined_power
        if power_exceptions is not None:
            payload["powerExceptions"] = power_exceptions
        if uplink_client_sampling is not None:
            payload["uplinkClientSampling"] = uplink_client_sampling
        if mac_blocklist is not None:
            payload["macBlocklist"] = mac_blocklist
        if uplink_selection is not None:
            payload["uplinkSelection"] = uplink_selection

        return self._session.put(metadata, resource, payload)

    def get_network_switch_stacks(self, *, network_id: str) -> dict[str, Any] | None:
        """List the switch stacks in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stacks

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "get_network_switch_stacks",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks"

        return self._session.get(metadata, resource)

    def create_network_switch_stack(
        self, *, network_id: str, name: str, serials: list
    ) -> dict[str, Any] | None:
        """Create a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack

        Args:
            network_id: Network ID.
            name: The name of the new stack.
            serials: An array of switch serials to be added into the new stack.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "create_network_switch_stack",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks"

        payload = {}
        if name is not None:
            payload["name"] = name
        if serials is not None:
            payload["serials"] = serials

        return self._session.post(metadata, resource, payload)

    def get_network_switch_stack(
        self, *, network_id: str, switch_stack_id: str
    ) -> dict[str, Any] | None:
        """Show a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "get_network_switch_stack",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}"

        return self._session.get(metadata, resource)

    def delete_network_switch_stack(self, *, network_id: str, switch_stack_id: str) -> None:
        """Delete a stack.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "delete_network_switch_stack",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}"

        return self._session.delete(metadata, resource)

    def add_network_switch_stack(
        self, *, network_id: str, switch_stack_id: str, serial: str
    ) -> dict[str, Any] | None:
        """Add a switch to a stack.

        https://developer.cisco.com/meraki/api-v1/#!add-network-switch-stack

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            serial: The serial of the switch to be added.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "add_network_switch_stack",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/add"

        payload = {}
        if serial is not None:
            payload["serial"] = serial

        return self._session.post(metadata, resource, payload)

    def remove_network_switch_stack(
        self, *, network_id: str, switch_stack_id: str, serial: str
    ) -> dict[str, Any] | None:
        """Remove a switch from a stack.

        https://developer.cisco.com/meraki/api-v1/#!remove-network-switch-stack

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            serial: The serial of the switch to be removed.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "remove_network_switch_stack",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/remove"

        payload = {}
        if serial is not None:
            payload["serial"] = serial

        return self._session.post(metadata, resource, payload)

    def get_network_switch_stack_routing_interfaces(
        self,
        *,
        network_id: str,
        switch_stack_id: str,
        mode: str | None = None,
        protocol: str | None = None,
    ) -> dict[str, Any] | None:
        """List layer 3 interfaces for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interfaces

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            mode: Optional parameter to filter L3 interfaces by mode.
            protocol: Optional parameter to filter L3 interfaces by protocol.

        """
        if mode is not None:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'
        if protocol is not None:
            options = ["ipv4", "ipv6"]
            assert protocol in options, (
                f'"protocol" cannot be "{protocol}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "get_network_switch_stack_routing_interfaces",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces"

        params = {}
        if mode is not None:
            params["mode"] = mode
        if protocol is not None:
            params["protocol"] = protocol

        return self._session.get(metadata, resource, params)

    def create_network_switch_stack_routing_interface(
        self,
        *,
        network_id: str,
        switch_stack_id: str,
        name: str,
        mode: str | None = None,
        subnet: str | None = None,
        switch_port_id: str | None = None,
        interface_ip: str | None = None,
        multicast_routing: str | None = None,
        vlan_id: int | None = None,
        default_gateway: str | None = None,
        ospf_settings: dict | None = None,
        ipv6: dict | None = None,
        vrf: dict | None = None,
        loopback: dict | None = None,
    ) -> dict[str, Any] | None:
        """Create a layer 3 interface for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            name: A friendly name or description for the interface or VLAN (max length 128
              characters).
            mode: L3 Interface mode, can be one of 'vlan', 'routed', 'loopback'. Default is 'vlan'.
              CS 17.18 or higher is required for 'routed' mode.
            subnet: The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
            switch_port_id: Switch Port ID when in Routed mode (CS 17.18 or higher required).
            interface_ip: The IP address that will be used for Layer 3 routing on this VLAN or
              subnet. This cannot be the same as the device management IP.
            multicast_routing: Enable multicast support if, multicast routing between VLANs is
              required. Options are: 'disabled', 'enabled' or 'IGMP snooping querier'.
              Default is 'disabled'.
            vlan_id: The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
            default_gateway: The next hop for any traffic that isn't going to a directly connected
              subnet or over a static route. This IP address must exist in a subnet with
              a L3 interface. Required if this is the first IPv4 interface.
            ospf_settings: The OSPF routing settings of the interface.
            ipv6: The IPv6 settings of the interface.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.
            loopback: The loopback settings of the interface.

        """
        if mode is not None:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'
        if multicast_routing is not None:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert multicast_routing in options, (
                f'"multicast_routing" cannot be "{multicast_routing}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "create_network_switch_stack_routing_interface",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces"

        payload = {}
        if name is not None:
            payload["name"] = name
        if mode is not None:
            payload["mode"] = mode
        if subnet is not None:
            payload["subnet"] = subnet
        if switch_port_id is not None:
            payload["switchPortId"] = switch_port_id
        if interface_ip is not None:
            payload["interfaceIp"] = interface_ip
        if multicast_routing is not None:
            payload["multicastRouting"] = multicast_routing
        if vlan_id is not None:
            payload["vlanId"] = vlan_id
        if default_gateway is not None:
            payload["defaultGateway"] = default_gateway
        if ospf_settings is not None:
            payload["ospfSettings"] = ospf_settings
        if ipv6 is not None:
            payload["ipv6"] = ipv6
        if vrf is not None:
            payload["vrf"] = vrf
        if loopback is not None:
            payload["loopback"] = loopback

        return self._session.post(metadata, resource, payload)

    def get_network_switch_stack_routing_interface(
        self, *, network_id: str, switch_stack_id: str, interface_id: str
    ) -> dict[str, Any] | None:
        """Return a layer 3 interface from a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            interface_id: Interface ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "get_network_switch_stack_routing_interface",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}"

        return self._session.get(metadata, resource)

    def update_network_switch_stack_routing_interface(
        self,
        *,
        network_id: str,
        switch_stack_id: str,
        interface_id: str,
        name: str | None = None,
        subnet: str | None = None,
        switch_port_id: str | None = None,
        interface_ip: str | None = None,
        multicast_routing: str | None = None,
        vlan_id: int | None = None,
        default_gateway: str | None = None,
        ospf_settings: dict | None = None,
        ipv6: dict | None = None,
        vrf: dict | None = None,
        loopback: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a layer 3 interface for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            interface_id: Interface ID.
            name: A friendly name or description for the interface or VLAN (max length 128
              characters).
            subnet: The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
            switch_port_id: Switch Port ID when in Routed mode (CS 17.18 or higher required).
            interface_ip: The IP address that will be used for Layer 3 routing on this VLAN or
              subnet. This cannot be the same as the device management IP.
            multicast_routing: Enable multicast support if, multicast routing between VLANs is
              required. Options are: 'disabled', 'enabled' or 'IGMP snooping querier'.
              Default is 'disabled'.
            vlan_id: The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
            default_gateway: The next hop for any traffic that isn't going to a directly connected
              subnet or over a static route. This IP address must exist in a subnet with
              a L3 interface. Required if this is the first IPv4 interface.
            ospf_settings: The OSPF routing settings of the interface.
            ipv6: The IPv6 settings of the interface.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.
            loopback: The loopback settings of the interface.

        """
        if multicast_routing is not None:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert multicast_routing in options, (
                f'"multicast_routing" cannot be "{multicast_routing}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "update_network_switch_stack_routing_interface",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if switch_port_id is not None:
            payload["switchPortId"] = switch_port_id
        if interface_ip is not None:
            payload["interfaceIp"] = interface_ip
        if multicast_routing is not None:
            payload["multicastRouting"] = multicast_routing
        if vlan_id is not None:
            payload["vlanId"] = vlan_id
        if default_gateway is not None:
            payload["defaultGateway"] = default_gateway
        if ospf_settings is not None:
            payload["ospfSettings"] = ospf_settings
        if ipv6 is not None:
            payload["ipv6"] = ipv6
        if vrf is not None:
            payload["vrf"] = vrf
        if loopback is not None:
            payload["loopback"] = loopback

        return self._session.put(metadata, resource, payload)

    def delete_network_switch_stack_routing_interface(
        self, *, network_id: str, switch_stack_id: str, interface_id: str
    ) -> None:
        """Delete a layer 3 interface from a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-interface

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            interface_id: Interface ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "delete_network_switch_stack_routing_interface",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}"

        return self._session.delete(metadata, resource)

    def get_network_switch_stack_routing_interface_dhcp(
        self, *, network_id: str, switch_stack_id: str, interface_id: str
    ) -> dict[str, Any] | None:
        """Return a layer 3 interface DHCP configuration for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface-dhcp

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            interface_id: Interface ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces", "dhcp"],
            "operation": "get_network_switch_stack_routing_interface_dhcp",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}/dhcp"

        return self._session.get(metadata, resource)

    def update_network_switch_stack_routing_interface_dhcp(
        self,
        *,
        network_id: str,
        switch_stack_id: str,
        interface_id: str,
        dhcp_mode: str | None = None,
        dhcp_relay_server_ips: list | None = None,
        dhcp_lease_time: str | None = None,
        dns_nameservers_option: str | None = None,
        dns_custom_nameservers: list | None = None,
        boot_options_enabled: bool | None = None,
        boot_next_server: str | None = None,
        boot_file_name: str | None = None,
        dhcp_options: list | None = None,
        reserved_ip_ranges: list | None = None,
        fixed_ip_assignments: list | None = None,
    ) -> dict[str, Any] | None:
        """Update a layer 3 interface DHCP configuration for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface-dhcp

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            interface_id: Interface ID.
            dhcp_mode: The DHCP mode options for the switch stack interface ('dhcpDisabled',
              'dhcpRelay' or 'dhcpServer').
            dhcp_relay_server_ips: The DHCP relay server IPs to which DHCP packets would get relayed
              for the switch stack interface.
            dhcp_lease_time: The DHCP lease time config for the dhcp server running on switch stack
              interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1
              week').
            dns_nameservers_option: The DHCP name server option for the dhcp server running on the
              switch stack interface ('googlePublicDns', 'openDns' or 'custom').
            dns_custom_nameservers: The DHCP name server IPs when DHCP name server option is '
              custom'.
            boot_options_enabled: Enable DHCP boot options to provide PXE boot options configs for
              the dhcp server running on the switch stack interface.
            boot_next_server: The PXE boot server IP for the DHCP server running on the switch stack
              interface.
            boot_file_name: The PXE boot server file name for the DHCP server running on the switch
              stack interface.
            dhcp_options: Array of DHCP options consisting of code, type and value for the DHCP
              server running on the switch stack interface.
            reserved_ip_ranges: Array of DHCP reserved IP assignments for the DHCP server running on
              the switch stack interface.
            fixed_ip_assignments: Array of DHCP fixed IP assignments for the DHCP server running on
              the switch stack interface.

        """
        if dhcp_mode is not None:
            options = ["dhcpDisabled", "dhcpRelay", "dhcpServer"]
            assert dhcp_mode in options, (
                f'"dhcp_mode" cannot be "{dhcp_mode}", & must be set to one of: {options}'
            )
        if dhcp_lease_time is not None:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert dhcp_lease_time in options, (
                f'"dhcp_lease_time" cannot be "{dhcp_lease_time}", & must be set to one of: {options}'
            )
        if dns_nameservers_option is not None:
            options = ["custom", "googlePublicDns", "openDns"]
            assert dns_nameservers_option in options, (
                f'"dns_nameservers_option" cannot be "{dns_nameservers_option}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces", "dhcp"],
            "operation": "update_network_switch_stack_routing_interface_dhcp",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        interface_id = urllib.parse.quote(str(interface_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}/dhcp"

        payload = {}
        if dhcp_mode is not None:
            payload["dhcpMode"] = dhcp_mode
        if dhcp_relay_server_ips is not None:
            payload["dhcpRelayServerIps"] = dhcp_relay_server_ips
        if dhcp_lease_time is not None:
            payload["dhcpLeaseTime"] = dhcp_lease_time
        if dns_nameservers_option is not None:
            payload["dnsNameserversOption"] = dns_nameservers_option
        if dns_custom_nameservers is not None:
            payload["dnsCustomNameservers"] = dns_custom_nameservers
        if boot_options_enabled is not None:
            payload["bootOptionsEnabled"] = boot_options_enabled
        if boot_next_server is not None:
            payload["bootNextServer"] = boot_next_server
        if boot_file_name is not None:
            payload["bootFileName"] = boot_file_name
        if dhcp_options is not None:
            payload["dhcpOptions"] = dhcp_options
        if reserved_ip_ranges is not None:
            payload["reservedIpRanges"] = reserved_ip_ranges
        if fixed_ip_assignments is not None:
            payload["fixedIpAssignments"] = fixed_ip_assignments

        return self._session.put(metadata, resource, payload)

    def get_network_switch_stack_routing_static_routes(
        self, *, network_id: str, switch_stack_id: str
    ) -> dict[str, Any] | None:
        """List layer 3 static routes for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-routes

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "get_network_switch_stack_routing_static_routes",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes"

        return self._session.get(metadata, resource)

    def create_network_switch_stack_routing_static_route(
        self,
        *,
        network_id: str,
        switch_stack_id: str,
        subnet: str,
        next_hop_ip: str,
        name: str | None = None,
        advertise_via_ospf_enabled: bool | None = None,
        prefer_over_ospf_routes_enabled: bool | None = None,
        vrf: dict | None = None,
    ) -> dict[str, Any] | None:
        """Create a layer 3 static route for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-static-route

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            name: Name or description for layer 3 static route.
            subnet: The subnet which is routed via this static route and should be specified in CIDR
              notation (ex. 1.2.3.0/24).
            next_hop_ip: IP address of the next hop device to which the device sends its traffic for
              the subnet.
            advertise_via_ospf_enabled: Option to advertise static route via OSPF.
            prefer_over_ospf_routes_enabled: Option to prefer static route over OSPF routes.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "create_network_switch_stack_routing_static_route",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if next_hop_ip is not None:
            payload["nextHopIp"] = next_hop_ip
        if advertise_via_ospf_enabled is not None:
            payload["advertiseViaOspfEnabled"] = advertise_via_ospf_enabled
        if prefer_over_ospf_routes_enabled is not None:
            payload["preferOverOspfRoutesEnabled"] = prefer_over_ospf_routes_enabled
        if vrf is not None:
            payload["vrf"] = vrf

        return self._session.post(metadata, resource, payload)

    def get_network_switch_stack_routing_static_route(
        self, *, network_id: str, switch_stack_id: str, static_route_id: str
    ) -> dict[str, Any] | None:
        """Return a layer 3 static route for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-route

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            static_route_id: Static route ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "get_network_switch_stack_routing_static_route",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes/{static_route_id}"

        return self._session.get(metadata, resource)

    def update_network_switch_stack_routing_static_route(
        self,
        *,
        network_id: str,
        switch_stack_id: str,
        static_route_id: str,
        name: str | None = None,
        subnet: str | None = None,
        next_hop_ip: str | None = None,
        management_next_hop: str | None = None,
        advertise_via_ospf_enabled: bool | None = None,
        prefer_over_ospf_routes_enabled: bool | None = None,
        vrf: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a layer 3 static route for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-static-route

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            static_route_id: Static route ID.
            name: Name or description for layer 3 static route.
            subnet: The subnet which is routed via this static route and should be specified in CIDR
              notation (ex. 1.2.3.0/24).
            next_hop_ip: IP address of the next hop device to which the device sends its traffic for
              the subnet.
            management_next_hop: Optional fallback IP address for management traffic.
            advertise_via_ospf_enabled: Option to advertise static route via OSPF.
            prefer_over_ospf_routes_enabled: Option to prefer static route over OSPF routes.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "update_network_switch_stack_routing_static_route",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes/{static_route_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if next_hop_ip is not None:
            payload["nextHopIp"] = next_hop_ip
        if management_next_hop is not None:
            payload["managementNextHop"] = management_next_hop
        if advertise_via_ospf_enabled is not None:
            payload["advertiseViaOspfEnabled"] = advertise_via_ospf_enabled
        if prefer_over_ospf_routes_enabled is not None:
            payload["preferOverOspfRoutesEnabled"] = prefer_over_ospf_routes_enabled
        if vrf is not None:
            payload["vrf"] = vrf

        return self._session.put(metadata, resource, payload)

    def delete_network_switch_stack_routing_static_route(
        self, *, network_id: str, switch_stack_id: str, static_route_id: str
    ) -> None:
        """Delete a layer 3 static route for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-static-route

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            static_route_id: Static route ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "delete_network_switch_stack_routing_static_route",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        switch_stack_id = urllib.parse.quote(str(switch_stack_id), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes/{static_route_id}"

        return self._session.delete(metadata, resource)

    def get_network_switch_storm_control(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the storm control configuration for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-storm-control

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["switch", "configure", "stormControl"],
            "operation": "get_network_switch_storm_control",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/stormControl"

        return self._session.get(metadata, resource)

    def update_network_switch_storm_control(
        self,
        *,
        network_id: str,
        broadcast_threshold: int | None = None,
        multicast_threshold: int | None = None,
        unknown_unicast_threshold: int | None = None,
        treat_these_traffic_types_as_one_threshold: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the storm control configuration for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control

        Args:
            network_id: Network ID.
            broadcast_threshold: Percentage (1 to 99) of total available port bandwidth for
              broadcast traffic type. Default value 100 percent rate is to clear the
              configuration.
            multicast_threshold: Percentage (1 to 99) of total available port bandwidth for
              multicast traffic type. Default value 100 percent rate is to clear the
              configuration.
            unknown_unicast_threshold: Percentage (1 to 99) of total available port bandwidth for
              unknown unicast (dlf-destination lookup failure) traffic type. Default
              value 100 percent rate is to clear the configuration.
            treat_these_traffic_types_as_one_threshold: Grouped traffic types.

        """
        metadata = {
            "tags": ["switch", "configure", "stormControl"],
            "operation": "update_network_switch_storm_control",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/stormControl"

        payload = {}
        if broadcast_threshold is not None:
            payload["broadcastThreshold"] = broadcast_threshold
        if multicast_threshold is not None:
            payload["multicastThreshold"] = multicast_threshold
        if unknown_unicast_threshold is not None:
            payload["unknownUnicastThreshold"] = unknown_unicast_threshold
        if treat_these_traffic_types_as_one_threshold is not None:
            payload["treatTheseTrafficTypesAsOneThreshold"] = (
                treat_these_traffic_types_as_one_threshold
            )

        return self._session.put(metadata, resource, payload)

    def get_network_switch_stp(self, *, network_id: str) -> dict[str, Any] | None:
        """Returns STP settings.

        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stp

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["switch", "configure", "stp"], "operation": "get_network_switch_stp"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/stp"

        return self._session.get(metadata, resource)

    def update_network_switch_stp(
        self,
        *,
        network_id: str,
        rstp_enabled: bool | None = None,
        stp_bridge_priority: list | None = None,
    ) -> dict[str, Any] | None:
        """Updates STP settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stp

        Args:
            network_id: Network ID.
            rstp_enabled: The spanning tree protocol status in network.
            stp_bridge_priority: STP bridge priority for switches/stacks or switch templates. An
              empty array will clear the STP bridge priority settings.

        """
        metadata = {
            "tags": ["switch", "configure", "stp"],
            "operation": "update_network_switch_stp",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/switch/stp"

        payload = {}
        if rstp_enabled is not None:
            payload["rstpEnabled"] = rstp_enabled
        if stp_bridge_priority is not None:
            payload["stpBridgePriority"] = stp_bridge_priority

        return self._session.put(metadata, resource, payload)

    def get_organization_config_template_switch_profiles(
        self, *, organization_id: str, config_template_id: str
    ) -> dict[str, Any] | None:
        """List the switch templates for your switch template configuration.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profiles

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.

        """
        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles"],
            "operation": "get_organization_config_template_switch_profiles",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        resource = (
            f"/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles"
        )

        return self._session.get(metadata, resource)

    def get_organization_config_template_switch_profile_ports(
        self, *, organization_id: str, config_template_id: str, profile_id: str
    ) -> dict[str, Any] | None:
        """Return all the ports of a switch template.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-ports

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.
            profile_id: Profile ID.

        """
        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports"],
            "operation": "get_organization_config_template_switch_profile_ports",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        resource = f"/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports"

        return self._session.get(metadata, resource)

    def get_organization_config_template_switch_profile_port(
        self, *, organization_id: str, config_template_id: str, profile_id: str, port_id: str
    ) -> dict[str, Any] | None:
        """Return a switch template port.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-port

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.
            profile_id: Profile ID.
            port_id: Port ID.

        """
        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports"],
            "operation": "get_organization_config_template_switch_profile_port",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        port_id = urllib.parse.quote(str(port_id), safe="")
        resource = f"/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}"

        return self._session.get(metadata, resource)

    def update_organization_config_template_switch_profile_port(
        self,
        *,
        organization_id: str,
        config_template_id: str,
        profile_id: str,
        port_id: str,
        name: str | None = None,
        tags: list | None = None,
        enabled: bool | None = None,
        poe_enabled: bool | None = None,
        type_: str | None = None,
        vlan: int | None = None,
        voice_vlan: int | None = None,
        allowed_vlans: str | None = None,
        isolation_enabled: bool | None = None,
        rstp_enabled: bool | None = None,
        stp_guard: str | None = None,
        stp_port_fast_trunk: bool | None = None,
        link_negotiation: str | None = None,
        port_schedule_id: str | None = None,
        udld: str | None = None,
        access_policy_type: str | None = None,
        access_policy_number: int | None = None,
        mac_allow_list: list | None = None,
        mac_whitelist_limit: int | None = None,
        sticky_mac_allow_list: list | None = None,
        sticky_mac_allow_list_limit: int | None = None,
        storm_control_enabled: bool | None = None,
        flexible_stacking_enabled: bool | None = None,
        dai_trusted: bool | None = None,
        profile: dict | None = None,
        dot3az: dict | None = None,
        high_speed: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a switch template port.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port

        Args:
            organization_id: Organization ID.
            config_template_id: Config template ID.
            profile_id: Profile ID.
            port_id: Port ID.
            name: The name of the switch template port.
            tags: The list of tags of the switch template port.
            enabled: The status of the switch template port.
            poe_enabled: The PoE status of the switch template port.
            type_: The type of the switch template port ('access', 'trunk', 'stack', 'routed', 'svl'
              or 'dad').
            vlan: The VLAN of the switch template port. For a trunk port, this is the native VLAN. A
              null value will clear the value set for trunk ports.
            voice_vlan: The voice VLAN of the switch template port. Only applicable to access ports.
            allowed_vlans: The VLANs allowed on the switch template port. Only applicable to trunk
              ports.
            isolation_enabled: The isolation status of the switch template port.
            rstp_enabled: The rapid spanning tree protocol status.
            stp_guard: The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop
              guard').
            stp_port_fast_trunk: The state of STP PortFast Trunk on the switch template port.
            link_negotiation: The link speed for the switch template port.
            port_schedule_id: The ID of the port schedule. A value of null will clear the port
              schedule.
            udld: The action to take when Unidirectional Link is detected (Alert only, Enforce).
              Default configuration is Alert only.
            access_policy_type: The type of the access policy of the switch template port. Only
              applicable to access ports. Can be one of 'Open', 'Custom access policy',
              'MAC allow list' or 'Sticky MAC allow list'.
            access_policy_number: The number of a custom access policy to configure on the switch
              template port. Only applicable when 'accessPolicyType' is 'Custom access
              policy'.
            mac_allow_list: Only devices with MAC addresses specified in this list will have access
              to this port. Up to 20 MAC addresses can be defined. Only applicable when
              'accessPolicyType' is 'MAC allow list'.
            mac_whitelist_limit: The maximum number of MAC addresses for regular MAC allow list.
              Only applicable when 'accessPolicyType' is 'MAC allow list'. Note: Config
              only supported on verions greater than ms18 only for classic switches.
            sticky_mac_allow_list: The initial list of MAC addresses for sticky Mac allow list. Only
              applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
            sticky_mac_allow_list_limit: The maximum number of MAC addresses for sticky MAC allow
              list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
            storm_control_enabled: The storm control status of the switch template port.
            flexible_stacking_enabled: For supported switches (e.g. MS420/MS425), whether or not the
              port has flexible stacking enabled.
            dai_trusted: If true, ARP packets for this port will be considered trusted, and Dynamic
              ARP Inspection will allow the traffic.
            profile: Profile attributes.
            dot3az: dot3az settings for the port.
            high_speed: High speed port enablement settings for C9500-32QC.

        """
        if type_ is not None:
            options = ["access", "dad", "routed", "stack", "svl", "trunk"]
            assert type_ in options, (
                f'"type_" cannot be "{type_}", & must be set to one of: {options}'
            )
        if stp_guard is not None:
            options = ["bpdu guard", "disabled", "loop guard", "root guard"]
            assert stp_guard in options, (
                f'"stp_guard" cannot be "{stp_guard}", & must be set to one of: {options}'
            )
        if udld is not None:
            options = ["Alert only", "Enforce"]
            assert udld in options, f'"udld" cannot be "{udld}", & must be set to one of: {options}'
        if access_policy_type is not None:
            options = ["Custom access policy", "MAC allow list", "Open", "Sticky MAC allow list"]
            assert access_policy_type in options, (
                f'"access_policy_type" cannot be "{access_policy_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports"],
            "operation": "update_organization_config_template_switch_profile_port",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        config_template_id = urllib.parse.quote(str(config_template_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        port_id = urllib.parse.quote(str(port_id), safe="")
        resource = f"/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if tags is not None:
            payload["tags"] = tags
        if enabled is not None:
            payload["enabled"] = enabled
        if poe_enabled is not None:
            payload["poeEnabled"] = poe_enabled
        if type_ is not None:
            payload["type"] = type_
        if vlan is not None:
            payload["vlan"] = vlan
        if voice_vlan is not None:
            payload["voiceVlan"] = voice_vlan
        if allowed_vlans is not None:
            payload["allowedVlans"] = allowed_vlans
        if isolation_enabled is not None:
            payload["isolationEnabled"] = isolation_enabled
        if rstp_enabled is not None:
            payload["rstpEnabled"] = rstp_enabled
        if stp_guard is not None:
            payload["stpGuard"] = stp_guard
        if stp_port_fast_trunk is not None:
            payload["stpPortFastTrunk"] = stp_port_fast_trunk
        if link_negotiation is not None:
            payload["linkNegotiation"] = link_negotiation
        if port_schedule_id is not None:
            payload["portScheduleId"] = port_schedule_id
        if udld is not None:
            payload["udld"] = udld
        if access_policy_type is not None:
            payload["accessPolicyType"] = access_policy_type
        if access_policy_number is not None:
            payload["accessPolicyNumber"] = access_policy_number
        if mac_allow_list is not None:
            payload["macAllowList"] = mac_allow_list
        if mac_whitelist_limit is not None:
            payload["macWhitelistLimit"] = mac_whitelist_limit
        if sticky_mac_allow_list is not None:
            payload["stickyMacAllowList"] = sticky_mac_allow_list
        if sticky_mac_allow_list_limit is not None:
            payload["stickyMacAllowListLimit"] = sticky_mac_allow_list_limit
        if storm_control_enabled is not None:
            payload["stormControlEnabled"] = storm_control_enabled
        if flexible_stacking_enabled is not None:
            payload["flexibleStackingEnabled"] = flexible_stacking_enabled
        if dai_trusted is not None:
            payload["daiTrusted"] = dai_trusted
        if profile is not None:
            payload["profile"] = profile
        if dot3az is not None:
            payload["dot3az"] = dot3az
        if high_speed is not None:
            payload["highSpeed"] = high_speed

        return self._session.put(metadata, resource, payload)

    def get_organization_summary_switch_power_history(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Returns the total PoE power draw for all switch ports in the organization over the requested timespan (by default the last 24 hours).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-switch-power-history

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 186 days. The default is 1 day.

        """
        metadata = {
            "tags": ["switch", "monitor", "summary", "power", "history"],
            "operation": "get_organization_summary_switch_power_history",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/summary/switch/power/history"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(metadata, resource, params)

    def clone_organization_switch_devices(
        self, *, organization_id: str, source_serial: str, target_serials: list
    ) -> dict[str, Any] | None:
        """Clone port-level and some switch-level configuration settings from a source switch to one or more target switches.

        https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices

        Args:
            organization_id: Organization ID.
            source_serial: Serial number of the source switch (must be on a network not bound to a
              template).
            target_serials: Array of serial numbers of one or more target switches (must be on a
              network not bound to a template).

        """
        metadata = {
            "tags": ["switch", "configure", "devices"],
            "operation": "clone_organization_switch_devices",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/switch/devices/clone"

        payload = {}
        if source_serial is not None:
            payload["sourceSerial"] = source_serial
        if target_serials is not None:
            payload["targetSerials"] = target_serials

        return self._session.post(metadata, resource, payload)

    def get_organization_switch_ports_by_switch(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        configuration_updated_after: str | None = None,
        mac: str | None = None,
        macs: list | None = None,
        name: str | None = None,
        network_ids: list | None = None,
        port_profile_ids: list | None = None,
        serial: str | None = None,
        serials: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the switchports in an organization by switch.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-by-switch

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 50. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            configuration_updated_after: Optional parameter to filter items to switches where the
              configuration has been updated after the given timestamp.
            mac: Optional parameter to filter items to switches with MAC addresses that contain the
              search term or are an exact match.
            macs: Optional parameter to filter items to switches that have one of the provided MAC
              addresses.
            name: Optional parameter to filter items to switches with names that contain the search
              term or are an exact match.
            network_ids: Optional parameter to filter items to switches in one of the provided
              networks.
            port_profile_ids: Optional parameter to filter items to switches that contain
              switchports belonging to one of the specified port profiles.
            serial: Optional parameter to filter items to switches with serial number that contains
              the search term or are an exact match.
            serials: Optional parameter to filter items to switches that have one of the provided
              serials.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["switch", "configure", "ports", "bySwitch"],
            "operation": "get_organization_switch_ports_by_switch",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/switch/ports/bySwitch"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if configuration_updated_after is not None:
            params["configurationUpdatedAfter"] = configuration_updated_after
        if mac is not None:
            params["mac"] = mac
        if macs is not None:
            params["macs[]"] = macs
        if name is not None:
            params["name"] = name
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if port_profile_ids is not None:
            params["portProfileIds[]"] = port_profile_ids
        if serial is not None:
            params["serial"] = serial
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_switch_ports_clients_overview_by_device(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        configuration_updated_after: str | None = None,
        mac: str | None = None,
        macs: list | None = None,
        name: str | None = None,
        network_ids: list | None = None,
        port_profile_ids: list | None = None,
        serial: str | None = None,
        serials: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the number of clients for all switchports with at least one online client in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-clients-overview-by-device

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.
            per_page: The number of entries per page returned. Acceptable range is 3 - 20. Default
              is 20.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            configuration_updated_after: Optional parameter to filter items to switches where the
              configuration has been updated after the given timestamp.
            mac: Optional parameter to filter items to switches with MAC addresses that contain the
              search term or are an exact match.
            macs: Optional parameter to filter items to switches that have one of the provided MAC
              addresses.
            name: Optional parameter to filter items to switches with names that contain the search
              term or are an exact match.
            network_ids: Optional parameter to filter items to switches in one of the provided
              networks.
            port_profile_ids: Optional parameter to filter items to switches that contain
              switchports belonging to one of the specified port profiles.
            serial: Optional parameter to filter items to switches with serial number that contains
              the search term or are an exact match.
            serials: Optional parameter to filter items to switches that have one of the provided
              serials.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["switch", "monitor", "ports", "clients", "overview", "byDevice"],
            "operation": "get_organization_switch_ports_clients_overview_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/switch/ports/clients/overview/byDevice"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if configuration_updated_after is not None:
            params["configurationUpdatedAfter"] = configuration_updated_after
        if mac is not None:
            params["mac"] = mac
        if macs is not None:
            params["macs[]"] = macs
        if name is not None:
            params["name"] = name
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if port_profile_ids is not None:
            params["portProfileIds[]"] = port_profile_ids
        if serial is not None:
            params["serial"] = serial
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_switch_ports_overview(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Returns the counts of all active ports for the requested timespan, grouped by speed.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-overview

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data.
            t1: The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 12 hours and be less than or equal
              to 186 days. The default is 1 day.

        """
        metadata = {
            "tags": ["switch", "monitor", "ports", "overview"],
            "operation": "get_organization_switch_ports_overview",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/switch/ports/overview"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(metadata, resource, params)

    def get_organization_switch_ports_statuses_by_switch(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        configuration_updated_after: str | None = None,
        mac: str | None = None,
        macs: list | None = None,
        name: str | None = None,
        network_ids: list | None = None,
        port_profile_ids: list | None = None,
        serial: str | None = None,
        serials: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the switchports in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-statuses-by-switch

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
            configuration_updated_after: Optional parameter to filter items to switches where the
              configuration has been updated after the given timestamp.
            mac: Optional parameter to filter items to switches with MAC addresses that contain the
              search term or are an exact match.
            macs: Optional parameter to filter items to switches that have one of the provided MAC
              addresses.
            name: Optional parameter to filter items to switches with names that contain the search
              term or are an exact match.
            network_ids: Optional parameter to filter items to switches in one of the provided
              networks.
            port_profile_ids: Optional parameter to filter items to switches that contain
              switchports belonging to one of the specified port profiles.
            serial: Optional parameter to filter items to switches with serial number that contains
              the search term or are an exact match.
            serials: Optional parameter to filter items to switches that have one of the provided
              serials.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["switch", "monitor", "ports", "statuses", "bySwitch"],
            "operation": "get_organization_switch_ports_statuses_by_switch",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/switch/ports/statuses/bySwitch"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if configuration_updated_after is not None:
            params["configurationUpdatedAfter"] = configuration_updated_after
        if mac is not None:
            params["mac"] = mac
        if macs is not None:
            params["macs[]"] = macs
        if name is not None:
            params["name"] = name
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if port_profile_ids is not None:
            params["portProfileIds[]"] = port_profile_ids
        if serial is not None:
            params["serial"] = serial
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_switch_ports_topology_discovery_by_device(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        configuration_updated_after: str | None = None,
        mac: str | None = None,
        macs: list | None = None,
        name: str | None = None,
        network_ids: list | None = None,
        port_profile_ids: list | None = None,
        serial: str | None = None,
        serials: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List most recently seen LLDP/CDP discovery and topology information per switch port in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-topology-discovery-by-device

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.
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
            configuration_updated_after: Optional parameter to filter items to switches where the
              configuration has been updated after the given timestamp.
            mac: Optional parameter to filter items to switches with MAC addresses that contain the
              search term or are an exact match.
            macs: Optional parameter to filter items to switches that have one of the provided MAC
              addresses.
            name: Optional parameter to filter items to switches with names that contain the search
              term or are an exact match.
            network_ids: Optional parameter to filter items to switches in one of the provided
              networks.
            port_profile_ids: Optional parameter to filter items to switches that contain
              switchports belonging to one of the specified port profiles.
            serial: Optional parameter to filter items to switches with serial number that contains
              the search term or are an exact match.
            serials: Optional parameter to filter items to switches that have one of the provided
              serials.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["switch", "monitor", "ports", "topology", "discovery", "byDevice"],
            "operation": "get_organization_switch_ports_topology_discovery_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/switch/ports/topology/discovery/byDevice"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if configuration_updated_after is not None:
            params["configurationUpdatedAfter"] = configuration_updated_after
        if mac is not None:
            params["mac"] = mac
        if macs is not None:
            params["macs[]"] = macs
        if name is not None:
            params["name"] = name
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if port_profile_ids is not None:
            params["portProfileIds[]"] = port_profile_ids
        if serial is not None:
            params["serial"] = serial
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_switch_ports_usage_history_by_device_by_interval(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        interval: int | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        configuration_updated_after: str | None = None,
        mac: str | None = None,
        macs: list | None = None,
        name: str | None = None,
        network_ids: list | None = None,
        port_profile_ids: list | None = None,
        serial: str | None = None,
        serials: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the historical usage and traffic data of switchports in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-usage-history-by-device-by-interval

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day. If
              interval is provided, the timespan will be autocalculated.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              1200, 14400, 86400. The default is 1200. Interval is calculated if time
              params are provided.
            per_page: The number of entries per page returned. Acceptable range is 3 - 50. Default
              is 10.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            configuration_updated_after: Optional parameter to filter items to switches where the
              configuration has been updated after the given timestamp.
            mac: Optional parameter to filter items to switches with MAC addresses that contain the
              search term or are an exact match.
            macs: Optional parameter to filter items to switches that have one of the provided MAC
              addresses.
            name: Optional parameter to filter items to switches with names that contain the search
              term or are an exact match.
            network_ids: Optional parameter to filter items to switches in one of the provided
              networks.
            port_profile_ids: Optional parameter to filter items to switches that contain
              switchports belonging to one of the specified port profiles.
            serial: Optional parameter to filter items to switches with serial number that contains
              the search term or are an exact match.
            serials: Optional parameter to filter items to switches that have one of the provided
              serials.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["switch", "monitor", "ports", "usage", "history", "byDevice", "byInterval"],
            "operation": "get_organization_switch_ports_usage_history_by_device_by_interval",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/switch/ports/usage/history/byDevice/byInterval"
        )

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if interval is not None:
            params["interval"] = interval
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if configuration_updated_after is not None:
            params["configurationUpdatedAfter"] = configuration_updated_after
        if mac is not None:
            params["mac"] = mac
        if macs is not None:
            params["macs[]"] = macs
        if name is not None:
            params["name"] = name
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if port_profile_ids is not None:
            params["portProfileIds[]"] = port_profile_ids
        if serial is not None:
            params["serial"] = serial
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
