"""ActionBatchSwitch API endpoints."""

import urllib
from typing import Any


class ActionBatchSwitch:
    """ActionBatchSwitch class."""

    def __init__(self) -> None:
        pass

    def cycle_device_switch_ports(self, serial: str, ports: list) -> dict[str, Any]:
        """Cycle a set of switch ports.

        https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports

        Args:
            serial: Serial.
            ports: List of switch ports.

        """
        kwargs = locals()

        metadata = {
            "tags": ["switch", "liveTools", "ports"],
            "operation": "cycle_device_switch_ports",
        }
        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/ports/cycle"

        body_params = [
            "ports",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_device_switch_port(self, serial: str, port_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update a switch port.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port

        Args:
            serial: Serial.
            port_id: Port ID.
            name: The name of the switch port.
            tags: The list of tags of the switch port.
            enabled: The status of the switch port.
            poeEnabled: The PoE status of the switch port.
            type: The type of the switch port ('access', 'trunk', 'stack', 'routed', 'svl' or
              'dad').
            vlan: The VLAN of the switch port. For a trunk port, this is the native VLAN. A null
              value will clear the value set for trunk ports.
            voiceVlan: The voice VLAN of the switch port. Only applicable to access ports.
            allowedVlans: The VLANs allowed on the switch port. Only applicable to trunk ports.
            isolationEnabled: The isolation status of the switch port.
            rstpEnabled: The rapid spanning tree protocol status.
            stpGuard: The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop
              guard').
            stpPortFastTrunk: The state of STP PortFast Trunk on the switch port.
            linkNegotiation: The link speed for the switch port.
            portScheduleId: The ID of the port schedule. A value of null will clear the port
              schedule.
            udld: The action to take when Unidirectional Link is detected (Alert only, Enforce).
              Default configuration is Alert only.
            accessPolicyType: The type of the access policy of the switch port. Only applicable to
              access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow
              list' or 'Sticky MAC allow list'.
            accessPolicyNumber: The number of a custom access policy to configure on the switch
              port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
            macAllowList: Only devices with MAC addresses specified in this list will have access to
              this port. Up to 20 MAC addresses can be defined. Only applicable when
              'accessPolicyType' is 'MAC allow list'.
            macWhitelistLimit: The maximum number of MAC addresses for regular MAC allow list. Only
              applicable when 'accessPolicyType' is 'MAC allow list'.           Note:
              Config only supported on verions greater than ms18 only for classic
              switches.
            stickyMacAllowList: The initial list of MAC addresses for sticky Mac allow list. Only
              applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
            stickyMacAllowListLimit: The maximum number of MAC addresses for sticky MAC allow list.
              Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
            stormControlEnabled: The storm control status of the switch port.
            adaptivePolicyGroupId: The adaptive policy group ID that will be used to tag traffic
              through this switch port. This ID must pre-exist during the configuration,
              else needs to be created using adaptivePolicy/groups API. Cannot be
              applied to a port on a switch bound to profile.
            peerSgtCapable: If true, Peer SGT is enabled for traffic through this switch port.
              Applicable to trunk port only, not access port. Cannot be applied to a
              port on a switch bound to profile.
            flexibleStackingEnabled: For supported switches (e.g. MS420/MS425), whether or not the
              port has flexible stacking enabled.
            daiTrusted: If true, ARP packets for this port will be considered trusted, and Dynamic
              ARP Inspection will allow the traffic.
            profile: Profile attributes.
            dot3az: dot3az settings for the port.
            highSpeed: High speed port enablement settings for C9500-32QC.

        """
        kwargs.update(locals())

        if "type" in kwargs:
            options = ["access", "dad", "routed", "stack", "svl", "trunk"]
            assert kwargs["type"] in options, (
                f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
            )
        if "stpGuard" in kwargs:
            options = ["bpdu guard", "disabled", "loop guard", "root guard"]
            assert kwargs["stpGuard"] in options, (
                f'''"stpGuard" cannot be "{kwargs["stpGuard"]}", & must be set to one of: {options}'''
            )
        if "udld" in kwargs:
            options = ["Alert only", "Enforce"]
            assert kwargs["udld"] in options, (
                f'''"udld" cannot be "{kwargs["udld"]}", & must be set to one of: {options}'''
            )
        if "accessPolicyType" in kwargs:
            options = ["Custom access policy", "MAC allow list", "Open", "Sticky MAC allow list"]
            assert kwargs["accessPolicyType"] in options, (
                f'''"accessPolicyType" cannot be "{kwargs["accessPolicyType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "ports"],
            "operation": "update_device_switch_port",
        }
        serial = urllib.parse.quote(serial, safe="")
        port_id = urllib.parse.quote(port_id, safe="")
        resource = f"/devices/{serial}/switch/ports/{port_id}"

        body_params = [
            "name",
            "tags",
            "enabled",
            "poeEnabled",
            "type",
            "vlan",
            "voiceVlan",
            "allowedVlans",
            "isolationEnabled",
            "rstpEnabled",
            "stpGuard",
            "stpPortFastTrunk",
            "linkNegotiation",
            "portScheduleId",
            "udld",
            "accessPolicyType",
            "accessPolicyNumber",
            "macAllowList",
            "macWhitelistLimit",
            "stickyMacAllowList",
            "stickyMacAllowListLimit",
            "stormControlEnabled",
            "adaptivePolicyGroupId",
            "peerSgtCapable",
            "flexibleStackingEnabled",
            "daiTrusted",
            "profile",
            "dot3az",
            "highSpeed",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_device_switch_routing_interface(
        self, serial: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a layer 3 interface for a switch.

        https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface

        Args:
            serial: Serial.
            name: A friendly name or description for the interface or VLAN (max length 128
              characters).
            mode: L3 Interface mode, can be one of 'vlan', 'routed', 'loopback'. Default is 'vlan'.
              CS 17.18 or higher is required for 'routed' mode. .
            subnet: The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
            switchPortId: Switch Port ID when in Routed mode (CS 17.18 or higher required).
            interfaceIp: The IP address that will be used for Layer 3 routing on this VLAN or
              subnet. This cannot be the same         as the device management IP.
            multicastRouting: Enable multicast support if, multicast routing between VLANs is
              required. Options are:         'disabled', 'enabled' or 'IGMP snooping
              querier'. Default is 'disabled'.
            vlanId: The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
            defaultGateway: The next hop for any traffic that isn't going to a directly connected
              subnet or over a static route.         This IP address must exist in a
              subnet with a L3 interface. Required if this is the first IPv4 interface.
            ospfSettings: The OSPF routing settings of the interface.
            ipv6: The IPv6 settings of the interface.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.
            loopback: The loopback settings of the interface.

        """
        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert kwargs["mode"] in options, (
                f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
            )
        if "multicastRouting" in kwargs:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert kwargs["multicastRouting"] in options, (
                f'''"multicastRouting" cannot be "{kwargs["multicastRouting"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "create_device_switch_routing_interface",
        }
        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces"

        body_params = [
            "name",
            "mode",
            "subnet",
            "switchPortId",
            "interfaceIp",
            "multicastRouting",
            "vlanId",
            "defaultGateway",
            "ospfSettings",
            "ipv6",
            "vrf",
            "loopback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_device_switch_routing_interface(
        self, serial: str, interface_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a layer 3 interface for a switch.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface

        Args:
            serial: Serial.
            interface_id: Interface ID.
            name: A friendly name or description for the interface or VLAN (max length 128
              characters).
            subnet: The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
            switchPortId: Switch Port ID when in Routed mode (CS 17.18 or higher required).
            interfaceIp: The IP address that will be used for Layer 3 routing on this VLAN or
              subnet. This cannot be the same         as the device management IP.
            multicastRouting: Enable multicast support if, multicast routing between VLANs is
              required. Options are:         'disabled', 'enabled' or 'IGMP snooping
              querier'. Default is 'disabled'.
            vlanId: The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
            defaultGateway: The next hop for any traffic that isn't going to a directly connected
              subnet or over a static route.         This IP address must exist in a
              subnet with a L3 interface. Required if this is the first IPv4 interface.
            ospfSettings: The OSPF routing settings of the interface.
            ipv6: The IPv6 settings of the interface.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.
            loopback: The loopback settings of the interface.

        """
        kwargs.update(locals())

        if "multicastRouting" in kwargs:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert kwargs["multicastRouting"] in options, (
                f'''"multicastRouting" cannot be "{kwargs["multicastRouting"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "update_device_switch_routing_interface",
        }
        serial = urllib.parse.quote(serial, safe="")
        interface_id = urllib.parse.quote(interface_id, safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interface_id}"

        body_params = [
            "name",
            "subnet",
            "switchPortId",
            "interfaceIp",
            "multicastRouting",
            "vlanId",
            "defaultGateway",
            "ospfSettings",
            "ipv6",
            "vrf",
            "loopback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_device_switch_routing_interface(
        self, serial: str, interface_id: str
    ) -> dict[str, Any]:
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
        serial = urllib.parse.quote(serial, safe="")
        interface_id = urllib.parse.quote(interface_id, safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interface_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_device_switch_routing_interface_dhcp(
        self, serial: str, interface_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a layer 3 interface DHCP configuration for a switch.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface-dhcp

        Args:
            serial: Serial.
            interface_id: Interface ID.
            dhcpMode: The DHCP mode options for the switch interface        ('dhcpDisabled',
              'dhcpRelay' or 'dhcpServer').
            dhcpRelayServerIps: The DHCP relay server IPs to which DHCP packets would get relayed
              for the switch interface.
            dhcpLeaseTime: The DHCP lease time config for the dhcp server running on switch
              interface         ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day'
              or '1 week').
            dnsNameserversOption: The DHCP name server option for the dhcp server running on the
              switch interface         ('googlePublicDns', 'openDns' or 'custom').
            dnsCustomNameservers: The DHCP name server IPs when DHCP name server option is
              'custom'.
            bootOptionsEnabled: Enable DHCP boot options to provide PXE boot options configs for the
              dhcp server running on the switch         interface.
            bootNextServer: The PXE boot server IP for the DHCP server running on the switch
              interface.
            bootFileName: The PXE boot server filename for the DHCP server running on the switch
              interface.
            dhcpOptions: Array of DHCP options consisting of code, type and value for the DHCP
              server running on the switch interface.
            reservedIpRanges: Array of DHCP reserved IP assignments for the DHCP server running on
              the switch interface.
            fixedIpAssignments: Array of DHCP fixed IP assignments for the DHCP server running on
              the switch interface.

        """
        kwargs.update(locals())

        if "dhcpMode" in kwargs:
            options = ["dhcpDisabled", "dhcpRelay", "dhcpServer"]
            assert kwargs["dhcpMode"] in options, (
                f'''"dhcpMode" cannot be "{kwargs["dhcpMode"]}", & must be set to one of: {options}'''
            )
        if "dhcpLeaseTime" in kwargs:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert kwargs["dhcpLeaseTime"] in options, (
                f'''"dhcpLeaseTime" cannot be "{kwargs["dhcpLeaseTime"]}", & must be set to one of: {options}'''
            )
        if "dnsNameserversOption" in kwargs:
            options = ["custom", "googlePublicDns", "openDns"]
            assert kwargs["dnsNameserversOption"] in options, (
                f'''"dnsNameserversOption" cannot be "{kwargs["dnsNameserversOption"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces", "dhcp"],
            "operation": "update_device_switch_routing_interface_dhcp",
        }
        serial = urllib.parse.quote(serial, safe="")
        interface_id = urllib.parse.quote(interface_id, safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interface_id}/dhcp"

        body_params = [
            "dhcpMode",
            "dhcpRelayServerIps",
            "dhcpLeaseTime",
            "dnsNameserversOption",
            "dnsCustomNameservers",
            "bootOptionsEnabled",
            "bootNextServer",
            "bootFileName",
            "dhcpOptions",
            "reservedIpRanges",
            "fixedIpAssignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_device_switch_routing_static_route(
        self, serial: str, subnet: str, nextHopIp: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a layer 3 static route for a switch.

        https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-static-route

        Args:
            serial: Serial.
            subnet: The subnet which is routed via this static route and should be specified in CIDR
              notation (ex. 1.2.3.0/24).
            nextHopIp: IP address of the next hop device to which the device sends its traffic for
              the subnet.
            name: Name or description for layer 3 static route.
            advertiseViaOspfEnabled: Option to advertise static route via OSPF.
            preferOverOspfRoutesEnabled: Option to prefer static route over OSPF routes.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "create_device_switch_routing_static_route",
        }
        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes"

        body_params = [
            "name",
            "subnet",
            "nextHopIp",
            "advertiseViaOspfEnabled",
            "preferOverOspfRoutesEnabled",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_device_switch_routing_static_route(
        self, serial: str, static_route_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a layer 3 static route for a switch.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-static-route

        Args:
            serial: Serial.
            static_route_id: Static route ID.
            name: Name or description for layer 3 static route.
            subnet: The subnet which is routed via this static route and should be specified in CIDR
              notation (ex. 1.2.3.0/24).
            nextHopIp: IP address of the next hop device to which the device sends its traffic for
              the subnet.
            managementNextHop: Optional fallback IP address for management traffic.
            advertiseViaOspfEnabled: Option to advertise static route via OSPF.
            preferOverOspfRoutesEnabled: Option to prefer static route over OSPF routes.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "update_device_switch_routing_static_route",
        }
        serial = urllib.parse.quote(serial, safe="")
        static_route_id = urllib.parse.quote(static_route_id, safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{static_route_id}"

        body_params = [
            "name",
            "subnet",
            "nextHopIp",
            "managementNextHop",
            "advertiseViaOspfEnabled",
            "preferOverOspfRoutesEnabled",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_device_switch_routing_static_route(
        self, serial: str, static_route_id: str
    ) -> dict[str, Any]:
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
        serial = urllib.parse.quote(serial, safe="")
        static_route_id = urllib.parse.quote(static_route_id, safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{static_route_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_device_switch_warm_spare(
        self, serial: str, enabled: bool, **kwargs: Any
    ) -> dict[str, Any]:
        """Update warm spare configuration for a switch.

        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-warm-spare

        Args:
            serial: Serial.
            enabled: Enable or disable warm spare for a switch.
            spareSerial: Serial number of the warm spare switch.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "warmSpare"],
            "operation": "update_device_switch_warm_spare",
        }
        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/warmSpare"

        body_params = [
            "enabled",
            "spareSerial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_switch_access_policy(
        self,
        network_id: str,
        name: str,
        radiusServers: list,
        radiusAccountingEnabled: bool,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create an access policy for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy

        Args:
            network_id: Network ID.
            name: Name of the access policy(max length 255).
            radiusServers: List of RADIUS servers to require connecting devices to authenticate
              against before granting network access.
            radiusAccountingEnabled: Enable to send start, interim-update and stop messages to a
              configured RADIUS accounting server for tracking connected clients.
            radius: Object for RADIUS Settings.
            guestPortBouncing: If enabled, Meraki devices will periodically send access-request
              messages to these RADIUS servers.
            radiusTestingEnabled: If enabled, Meraki devices will periodically send access-request
              messages to these RADIUS servers.
            radiusCoaSupportEnabled: Change of authentication for RADIUS re-authentication and
              disconnection.
            radiusAccountingServers: List of RADIUS accounting servers to require connecting devices
              to authenticate against before granting network access.
            radiusGroupAttribute: Acceptable values are `""` for None, or `"11"` for Group Policies
              ACL.
            hostMode: Choose the Host Mode for the access policy.
            accessPolicyType: Access Type of the policy. Automatically 'Hybrid authentication' when
              hostMode is 'Multi-Domain'.
            increaseAccessSpeed: Enabling this option will make switches execute 802.1X and MAC-
              bypass authentication simultaneously so that clients authenticate faster.
              Only required when accessPolicyType is 'Hybrid Authentication.
            guestVlanId: ID for the guest VLAN allow unauthorized devices access to limited network
              resources.
            dot1x: 802.1x Settings.
            voiceVlanClients: CDP/LLDP capable voice clients will be able to use this VLAN.
              Automatically true when hostMode is 'Multi-Domain'.
            urlRedirectWalledGardenEnabled: Enable to restrict access for clients to a specific set
              of IP addresses or hostnames prior to authentication.
            urlRedirectWalledGardenRanges: IP address ranges, in CIDR notation, to restrict access
              for clients to a specific set of IP addresses or hostnames prior to
              authentication.
            guestGroupPolicyId: Group policy Number for guest group policy.
            guestSgtId: Security Group Tag ID for guest group policy.

        """
        kwargs.update(locals())

        if "hostMode" in kwargs:
            options = ["Multi-Auth", "Multi-Domain", "Multi-Host", "Single-Host"]
            assert kwargs["hostMode"] in options, (
                f'''"hostMode" cannot be "{kwargs["hostMode"]}", & must be set to one of: {options}'''
            )
        if "accessPolicyType" in kwargs:
            options = ["802.1x", "Hybrid authentication", "MAC authentication bypass"]
            assert kwargs["accessPolicyType"] in options, (
                f'''"accessPolicyType" cannot be "{kwargs["accessPolicyType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "create_network_switch_access_policy",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/accessPolicies"

        body_params = [
            "name",
            "radiusServers",
            "radius",
            "guestPortBouncing",
            "radiusTestingEnabled",
            "radiusCoaSupportEnabled",
            "radiusAccountingEnabled",
            "radiusAccountingServers",
            "radiusGroupAttribute",
            "hostMode",
            "accessPolicyType",
            "increaseAccessSpeed",
            "guestVlanId",
            "dot1x",
            "voiceVlanClients",
            "urlRedirectWalledGardenEnabled",
            "urlRedirectWalledGardenRanges",
            "guestGroupPolicyId",
            "guestSgtId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_switch_access_policy(
        self, network_id: str, access_policy_number: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update an access policy for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy

        Args:
            network_id: Network ID.
            access_policy_number: Access policy number.
            name: Name of the access policy(max length 255).
            radiusServers: List of RADIUS servers to require connecting devices to authenticate
              against before granting network access.
            radius: Object for RADIUS Settings.
            guestPortBouncing: If enabled, Meraki devices will periodically send access-request
              messages to these RADIUS servers.
            radiusTestingEnabled: If enabled, Meraki devices will periodically send access-request
              messages to these RADIUS servers.
            radiusCoaSupportEnabled: Change of authentication for RADIUS re-authentication and
              disconnection.
            radiusAccountingEnabled: Enable to send start, interim-update and stop messages to a
              configured RADIUS accounting server for tracking connected clients.
            radiusAccountingServers: List of RADIUS accounting servers to require connecting devices
              to authenticate against before granting network access.
            radiusGroupAttribute: Acceptable values are `""` for None, or `"11"` for Group Policies
              ACL.
            hostMode: Choose the Host Mode for the access policy.
            accessPolicyType: Access Type of the policy. Automatically 'Hybrid authentication' when
              hostMode is 'Multi-Domain'.
            increaseAccessSpeed: Enabling this option will make switches execute 802.1X and MAC-
              bypass authentication simultaneously so that clients authenticate faster.
              Only required when accessPolicyType is 'Hybrid Authentication.
            guestVlanId: ID for the guest VLAN allow unauthorized devices access to limited network
              resources.
            dot1x: 802.1x Settings.
            voiceVlanClients: CDP/LLDP capable voice clients will be able to use this VLAN.
              Automatically true when hostMode is 'Multi-Domain'.
            urlRedirectWalledGardenEnabled: Enable to restrict access for clients to a specific set
              of IP addresses or hostnames prior to authentication.
            urlRedirectWalledGardenRanges: IP address ranges, in CIDR notation, to restrict access
              for clients to a specific set of IP addresses or hostnames prior to
              authentication.
            guestGroupPolicyId: Group policy Number for guest group policy.
            guestSgtId: Security Group Tag ID for guest group policy.

        """
        kwargs.update(locals())

        if "hostMode" in kwargs:
            options = ["Multi-Auth", "Multi-Domain", "Multi-Host", "Single-Host"]
            assert kwargs["hostMode"] in options, (
                f'''"hostMode" cannot be "{kwargs["hostMode"]}", & must be set to one of: {options}'''
            )
        if "accessPolicyType" in kwargs:
            options = ["802.1x", "Hybrid authentication", "MAC authentication bypass"]
            assert kwargs["accessPolicyType"] in options, (
                f'''"accessPolicyType" cannot be "{kwargs["accessPolicyType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "update_network_switch_access_policy",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        access_policy_number = urllib.parse.quote(access_policy_number, safe="")
        resource = f"/networks/{network_id}/switch/accessPolicies/{access_policy_number}"

        body_params = [
            "name",
            "radiusServers",
            "radius",
            "guestPortBouncing",
            "radiusTestingEnabled",
            "radiusCoaSupportEnabled",
            "radiusAccountingEnabled",
            "radiusAccountingServers",
            "radiusGroupAttribute",
            "hostMode",
            "accessPolicyType",
            "increaseAccessSpeed",
            "guestVlanId",
            "dot1x",
            "voiceVlanClients",
            "urlRedirectWalledGardenEnabled",
            "urlRedirectWalledGardenRanges",
            "guestGroupPolicyId",
            "guestSgtId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_switch_access_policy(
        self, network_id: str, access_policy_number: str
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(network_id, safe="")
        access_policy_number = urllib.parse.quote(access_policy_number, safe="")
        resource = f"/networks/{network_id}/switch/accessPolicies/{access_policy_number}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_switch_alternate_management_interface(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the switch alternate management interface for the network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-alternate-management-interface

        Args:
            network_id: Network ID.
            enabled: Boolean value to enable or disable AMI configuration. If enabled, VLAN and
              protocols must be set.
            vlanId: Alternate management VLAN, must be between 1 and 4094.
            protocols: Can be one or more of the following values: 'radius', 'snmp' or 'syslog'.
            switches: Array of switch serial number and IP assignment. If parameter is present, it
              cannot have empty body. Note: switches parameter is not applicable for
              template networks, in other words, do not put 'switches' in the body when
              updating template networks. Also, an empty 'switches' array will remove
              all previous assignments.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "alternateManagementInterface"],
            "operation": "update_network_switch_alternate_management_interface",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/alternateManagementInterface"

        body_params = [
            "enabled",
            "vlanId",
            "protocols",
            "switches",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_switch_dhcp_server_policy(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the DHCP server settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy

        Args:
            network_id: Network ID.
            alerts: Alert settings for DHCP servers.
            defaultPolicy: 'allow' or 'block' new DHCP servers. Default value is 'allow'.
            allowedServers: List the MAC addresses of DHCP servers to permit on the network when
              defaultPolicy is set to block. An empty array will clear the entries.
            blockedServers: List the MAC addresses of DHCP servers to block on the network when
              defaultPolicy is set to allow. An empty array will clear the entries.
            arpInspection: Dynamic ARP Inspection settings.

        """
        kwargs.update(locals())

        if "defaultPolicy" in kwargs:
            options = ["allow", "block"]
            assert kwargs["defaultPolicy"] in options, (
                f'''"defaultPolicy" cannot be "{kwargs["defaultPolicy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy"],
            "operation": "update_network_switch_dhcp_server_policy",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy"

        body_params = [
            "alerts",
            "defaultPolicy",
            "allowedServers",
            "blockedServers",
            "arpInspection",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_switch_dhcp_server_policy_arp_inspection_trusted_server(
        self, network_id: str, mac: str, vlan: int, ipv4: dict
    ) -> dict[str, Any]:
        """Add a server to be trusted by Dynamic ARP Inspection on this network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        Args:
            network_id: Network ID.
            mac: The mac address of the trusted server being added.
            vlan: The VLAN of the trusted server being added. It must be between 1 and 4094.
            ipv4: The IPv4 attributes of the trusted server being added.

        """
        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "create_network_switch_dhcp_server_policy_arp_inspection_trusted_server",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers"

        body_params = [
            "mac",
            "vlan",
            "ipv4",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_switch_dhcp_server_policy_arp_inspection_trusted_server(
        self, network_id: str, trusted_server_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a server that is trusted by Dynamic ARP Inspection on this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        Args:
            network_id: Network ID.
            trusted_server_id: Trusted server ID.
            mac: The updated mac address of the trusted server.
            vlan: The updated VLAN of the trusted server. It must be between 1 and 4094.
            ipv4: The updated IPv4 attributes of the trusted server.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "update_network_switch_dhcp_server_policy_arp_inspection_trusted_server",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        trusted_server_id = urllib.parse.quote(trusted_server_id, safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trusted_server_id}"

        body_params = [
            "mac",
            "vlan",
            "ipv4",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server(
        self, network_id: str, trusted_server_id: str
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(network_id, safe="")
        trusted_server_id = urllib.parse.quote(trusted_server_id, safe="")
        resource = f"/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trusted_server_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_switch_dscp_to_cos_mappings(
        self, network_id: str, mappings: list
    ) -> dict[str, Any]:
        """Update the DSCP to CoS mappings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings

        Args:
            network_id: Network ID.
            mappings: An array of DSCP to CoS mappings. An empty array will reset the mappings to
              default.

        """
        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "dscpToCosMappings"],
            "operation": "update_network_switch_dscp_to_cos_mappings",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/dscpToCosMappings"

        body_params = [
            "mappings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_switch_link_aggregation(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a link aggregation group.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-link-aggregation

        Args:
            network_id: Network ID.
            switchPorts: Array of switch or stack ports for creating aggregation group. Minimum 2
              and maximum 8 ports are supported.
            switchProfilePorts: Array of switch profile ports for creating aggregation group.
              Minimum 2 and maximum 8 ports are supported.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "create_network_switch_link_aggregation",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/linkAggregations"

        body_params = [
            "switchPorts",
            "switchProfilePorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_switch_link_aggregation(
        self, network_id: str, link_aggregation_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a link aggregation group.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-link-aggregation

        Args:
            network_id: Network ID.
            link_aggregation_id: Link aggregation ID.
            switchPorts: Array of switch or stack ports for updating aggregation group. Minimum 2
              and maximum 8 ports are supported.
            switchProfilePorts: Array of switch profile ports for updating aggregation group.
              Minimum 2 and maximum 8 ports are supported.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "update_network_switch_link_aggregation",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        link_aggregation_id = urllib.parse.quote(link_aggregation_id, safe="")
        resource = f"/networks/{network_id}/switch/linkAggregations/{link_aggregation_id}"

        body_params = [
            "switchPorts",
            "switchProfilePorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_switch_link_aggregation(
        self, network_id: str, link_aggregation_id: str
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(network_id, safe="")
        link_aggregation_id = urllib.parse.quote(link_aggregation_id, safe="")
        resource = f"/networks/{network_id}/switch/linkAggregations/{link_aggregation_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_switch_mtu(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update the MTU configuration.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-mtu

        Args:
            network_id: Network ID.
            defaultMtuSize: MTU size for the entire network. Default value is 9578.
            overrides: Override MTU size for individual switches or switch templates. An empty array
              will clear overrides.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "mtu"],
            "operation": "update_network_switch_mtu",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/mtu"

        body_params = [
            "defaultMtuSize",
            "overrides",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_switch_port_schedule(
        self, network_id: str, port_schedule_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a switch port schedule.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-port-schedule

        Args:
            network_id: Network ID.
            port_schedule_id: Port schedule ID.
            name: The name for your port schedule.
            portSchedule:     The schedule for switch port scheduling. Schedules are applied to days
              of the week.     When it's empty, default schedule with all days of a week
              are configured.     Any unspecified day in the schedule is added as a
              default schedule configuration of the day. .

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "update_network_switch_port_schedule",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        port_schedule_id = urllib.parse.quote(port_schedule_id, safe="")
        resource = f"/networks/{network_id}/switch/portSchedules/{port_schedule_id}"

        body_params = [
            "name",
            "portSchedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_switch_qos_rule(
        self, network_id: str, vlan: int, **kwargs: Any
    ) -> dict[str, Any]:
        """Add a quality of service rule.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-qos-rule

        Args:
            network_id: Network ID.
            vlan: The VLAN of the incoming packet. A null value will match any VLAN.
            protocol: The protocol of the incoming packet. Default value is "ANY".
            srcPort: The source port of the incoming packet. Applicable only if protocol is TCP or
              UDP.
            srcPortRange: The source port range of the incoming packet. Applicable only if protocol
              is set to TCP or UDP.
            dstPort: The destination port of the incoming packet. Applicable only if protocol is TCP
              or UDP.
            dstPortRange: The destination port range of the incoming packet. Applicable only if
              protocol is set to TCP or UDP.
            dscp: DSCP tag for the incoming packet. Set this to -1 to trust incoming DSCP. Default
              value is 0.

        """
        kwargs.update(locals())

        if "protocol" in kwargs:
            options = ["ANY", "TCP", "UDP"]
            assert kwargs["protocol"] in options, (
                f'''"protocol" cannot be "{kwargs["protocol"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "create_network_switch_qos_rule",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/qosRules"

        body_params = [
            "vlan",
            "protocol",
            "srcPort",
            "srcPortRange",
            "dstPort",
            "dstPortRange",
            "dscp",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_switch_qos_rules_order(
        self, network_id: str, ruleIds: list
    ) -> dict[str, Any]:
        """Update the order in which the rules should be processed by the switch.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order

        Args:
            network_id: Network ID.
            ruleIds: A list of quality of service rule IDs arranged in order in which they should be
              processed by the switch.

        """
        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "qosRules", "order"],
            "operation": "update_network_switch_qos_rules_order",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/qosRules/order"

        body_params = [
            "ruleIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_switch_qos_rule(self, network_id: str, qos_rule_id: str) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(network_id, safe="")
        qos_rule_id = urllib.parse.quote(qos_rule_id, safe="")
        resource = f"/networks/{network_id}/switch/qosRules/{qos_rule_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_switch_qos_rule(
        self, network_id: str, qos_rule_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a quality of service rule.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule

        Args:
            network_id: Network ID.
            qos_rule_id: Qos rule ID.
            vlan: The VLAN of the incoming packet. A null value will match any VLAN.
            protocol: The protocol of the incoming packet. Default value is "ANY".
            srcPort: The source port of the incoming packet. Applicable only if protocol is TCP or
              UDP.
            srcPortRange: The source port range of the incoming packet. Applicable only if protocol
              is set to TCP or UDP.
            dstPort: The destination port of the incoming packet. Applicable only if protocol is TCP
              or UDP.
            dstPortRange: The destination port range of the incoming packet. Applicable only if
              protocol is set to TCP or UDP.
            dscp: DSCP tag that should be assigned to incoming packet. Set this to -1 to trust
              incoming DSCP. Default value is 0.

        """
        kwargs.update(locals())

        if "protocol" in kwargs:
            options = ["ANY", "TCP", "UDP"]
            assert kwargs["protocol"] in options, (
                f'''"protocol" cannot be "{kwargs["protocol"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "update_network_switch_qos_rule",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        qos_rule_id = urllib.parse.quote(qos_rule_id, safe="")
        resource = f"/networks/{network_id}/switch/qosRules/{qos_rule_id}"

        body_params = [
            "vlan",
            "protocol",
            "srcPort",
            "srcPortRange",
            "dstPort",
            "dstPortRange",
            "dscp",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_switch_routing_multicast(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update multicast settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast

        Args:
            network_id: Network ID.
            defaultSettings: Default multicast setting for entire network. IGMP snooping and Flood
              unknown multicast traffic settings are enabled by default.
            overrides: Array of paired switches/stacks/profiles and corresponding multicast
              settings. An empty array will clear the multicast settings.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast"],
            "operation": "update_network_switch_routing_multicast",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast"

        body_params = [
            "defaultSettings",
            "overrides",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_switch_routing_multicast_rendezvous_point(
        self, network_id: str, interfaceIp: str, multicastGroup: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a multicast rendezvous point.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-routing-multicast-rendezvous-point

        Args:
            network_id: Network ID.
            interfaceIp: The IP address of the interface where the RP needs to be created.
            multicastGroup: 'Any', or the IP address of a multicast group.
            vrf: The VRF with PIM enabled L3 interface.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "create_network_switch_routing_multicast_rendezvous_point",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast/rendezvousPoints"

        body_params = [
            "interfaceIp",
            "multicastGroup",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def delete_network_switch_routing_multicast_rendezvous_point(
        self, network_id: str, rendezvous_point_id: str
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(network_id, safe="")
        rendezvous_point_id = urllib.parse.quote(rendezvous_point_id, safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_switch_routing_multicast_rendezvous_point(
        self,
        network_id: str,
        rendezvous_point_id: str,
        interfaceIp: str,
        multicastGroup: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update a multicast rendezvous point.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point

        Args:
            network_id: Network ID.
            rendezvous_point_id: Rendezvous point ID.
            interfaceIp: The IP address of the interface where the RP needs to be created.
            multicastGroup: 'Any', or the IP address of a multicast group.
            vrf: The VRF with PIM enabled L3 interface.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "update_network_switch_routing_multicast_rendezvous_point",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        rendezvous_point_id = urllib.parse.quote(rendezvous_point_id, safe="")
        resource = f"/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}"

        body_params = [
            "interfaceIp",
            "multicastGroup",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_switch_routing_ospf(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update layer 3 OSPF routing configuration.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-ospf

        Args:
            network_id: Network ID.
            vrf: The VRF to return the OSPF routing configuration for. When not provided, the
              default VRF is used. Requires IOS XE 17.18 or higher.
            enabled: Boolean value to enable or disable OSPF routing. OSPF routing is disabled by
              default.
            helloTimerInSeconds: Time interval in seconds at which hello packet will be sent to OSPF
              neighbors to maintain connectivity. Value must be between 1 and 255.
              Default is 10 seconds.
            deadTimerInSeconds: Time interval to determine when the peer will be declared
              inactive/dead. Value must be between 1 and 65535.
            areas: OSPF areas.
            v3: OSPF v3 configuration.
            md5AuthenticationEnabled: Boolean value to enable or disable MD5 authentication. MD5
              authentication is disabled by default.
            md5AuthenticationKey: MD5 authentication credentials. This param is only relevant if
              md5AuthenticationEnabled is true.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "ospf"],
            "operation": "update_network_switch_routing_ospf",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/routing/ospf"

        body_params = [
            "enabled",
            "helloTimerInSeconds",
            "deadTimerInSeconds",
            "areas",
            "v3",
            "md5AuthenticationEnabled",
            "md5AuthenticationKey",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_switch_settings(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update switch network settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-settings

        Args:
            network_id: Network ID.
            vlan: Management VLAN.
            useCombinedPower: The use Combined Power as the default behavior of secondary power
              supplies on supported devices.
            powerExceptions: Exceptions on a per switch basis to "useCombinedPower".
            uplinkClientSampling: Uplink client sampling.
            macBlocklist: MAC blocklist.
            uplinkSelection: Settings related to uplink selection on IOS-XE switches.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "settings"],
            "operation": "update_network_switch_settings",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/settings"

        body_params = [
            "vlan",
            "useCombinedPower",
            "powerExceptions",
            "uplinkClientSampling",
            "macBlocklist",
            "uplinkSelection",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_switch_stack_routing_interface(
        self, network_id: str, switch_stack_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a layer 3 interface for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            name: A friendly name or description for the interface or VLAN (max length 128
              characters).
            mode: L3 Interface mode, can be one of 'vlan', 'routed', 'loopback'. Default is 'vlan'.
              CS 17.18 or higher is required for 'routed' mode. .
            subnet: The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
            switchPortId: Switch Port ID when in Routed mode (CS 17.18 or higher required).
            interfaceIp: The IP address that will be used for Layer 3 routing on this VLAN or
              subnet. This cannot be the same         as the device management IP.
            multicastRouting: Enable multicast support if, multicast routing between VLANs is
              required. Options are:         'disabled', 'enabled' or 'IGMP snooping
              querier'. Default is 'disabled'.
            vlanId: The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
            defaultGateway: The next hop for any traffic that isn't going to a directly connected
              subnet or over a static route.         This IP address must exist in a
              subnet with a L3 interface. Required if this is the first IPv4 interface.
            ospfSettings: The OSPF routing settings of the interface.
            ipv6: The IPv6 settings of the interface.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.
            loopback: The loopback settings of the interface.

        """
        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert kwargs["mode"] in options, (
                f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
            )
        if "multicastRouting" in kwargs:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert kwargs["multicastRouting"] in options, (
                f'''"multicastRouting" cannot be "{kwargs["multicastRouting"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "create_network_switch_stack_routing_interface",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        switch_stack_id = urllib.parse.quote(switch_stack_id, safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces"

        body_params = [
            "name",
            "mode",
            "subnet",
            "switchPortId",
            "interfaceIp",
            "multicastRouting",
            "vlanId",
            "defaultGateway",
            "ospfSettings",
            "ipv6",
            "vrf",
            "loopback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_switch_stack_routing_interface(
        self, network_id: str, switch_stack_id: str, interface_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a layer 3 interface for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            interface_id: Interface ID.
            name: A friendly name or description for the interface or VLAN (max length 128
              characters).
            subnet: The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
            switchPortId: Switch Port ID when in Routed mode (CS 17.18 or higher required).
            interfaceIp: The IP address that will be used for Layer 3 routing on this VLAN or
              subnet. This cannot be the same         as the device management IP.
            multicastRouting: Enable multicast support if, multicast routing between VLANs is
              required. Options are:         'disabled', 'enabled' or 'IGMP snooping
              querier'. Default is 'disabled'.
            vlanId: The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
            defaultGateway: The next hop for any traffic that isn't going to a directly connected
              subnet or over a static route.         This IP address must exist in a
              subnet with a L3 interface. Required if this is the first IPv4 interface.
            ospfSettings: The OSPF routing settings of the interface.
            ipv6: The IPv6 settings of the interface.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.
            loopback: The loopback settings of the interface.

        """
        kwargs.update(locals())

        if "multicastRouting" in kwargs:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert kwargs["multicastRouting"] in options, (
                f'''"multicastRouting" cannot be "{kwargs["multicastRouting"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "update_network_switch_stack_routing_interface",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        switch_stack_id = urllib.parse.quote(switch_stack_id, safe="")
        interface_id = urllib.parse.quote(interface_id, safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}"

        body_params = [
            "name",
            "subnet",
            "switchPortId",
            "interfaceIp",
            "multicastRouting",
            "vlanId",
            "defaultGateway",
            "ospfSettings",
            "ipv6",
            "vrf",
            "loopback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_switch_stack_routing_interface(
        self, network_id: str, switch_stack_id: str, interface_id: str
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(network_id, safe="")
        switch_stack_id = urllib.parse.quote(switch_stack_id, safe="")
        interface_id = urllib.parse.quote(interface_id, safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_switch_stack_routing_interface_dhcp(
        self, network_id: str, switch_stack_id: str, interface_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a layer 3 interface DHCP configuration for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface-dhcp

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            interface_id: Interface ID.
            dhcpMode: The DHCP mode options for the switch stack interface         ('dhcpDisabled',
              'dhcpRelay' or 'dhcpServer').
            dhcpRelayServerIps: The DHCP relay server IPs to which DHCP packets would get relayed
              for the switch stack interface.
            dhcpLeaseTime: The DHCP lease time config for the dhcp server running on switch stack
              interface         ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day'
              or '1 week').
            dnsNameserversOption: The DHCP name server option for the dhcp server running on the
              switch stack interface         ('googlePublicDns', 'openDns' or 'custom').
            dnsCustomNameservers: The DHCP name server IPs when DHCP name server option is '
              custom'.
            bootOptionsEnabled: Enable DHCP boot options to provide PXE boot options configs for the
              dhcp server running on the switch         stack interface.
            bootNextServer: The PXE boot server IP for the DHCP server running on the switch stack
              interface.
            bootFileName: The PXE boot server file name for the DHCP server running on the switch
              stack interface.
            dhcpOptions: Array of DHCP options consisting of code, type and value for the DHCP
              server running on the         switch stack interface.
            reservedIpRanges: Array of DHCP reserved IP assignments for the DHCP server running on
              the switch stack interface.
            fixedIpAssignments: Array of DHCP fixed IP assignments for the DHCP server running on
              the switch stack interface.

        """
        kwargs.update(locals())

        if "dhcpMode" in kwargs:
            options = ["dhcpDisabled", "dhcpRelay", "dhcpServer"]
            assert kwargs["dhcpMode"] in options, (
                f'''"dhcpMode" cannot be "{kwargs["dhcpMode"]}", & must be set to one of: {options}'''
            )
        if "dhcpLeaseTime" in kwargs:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert kwargs["dhcpLeaseTime"] in options, (
                f'''"dhcpLeaseTime" cannot be "{kwargs["dhcpLeaseTime"]}", & must be set to one of: {options}'''
            )
        if "dnsNameserversOption" in kwargs:
            options = ["custom", "googlePublicDns", "openDns"]
            assert kwargs["dnsNameserversOption"] in options, (
                f'''"dnsNameserversOption" cannot be "{kwargs["dnsNameserversOption"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces", "dhcp"],
            "operation": "update_network_switch_stack_routing_interface_dhcp",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        switch_stack_id = urllib.parse.quote(switch_stack_id, safe="")
        interface_id = urllib.parse.quote(interface_id, safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}/dhcp"

        body_params = [
            "dhcpMode",
            "dhcpRelayServerIps",
            "dhcpLeaseTime",
            "dnsNameserversOption",
            "dnsCustomNameservers",
            "bootOptionsEnabled",
            "bootNextServer",
            "bootFileName",
            "dhcpOptions",
            "reservedIpRanges",
            "fixedIpAssignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_network_switch_stack_routing_static_route(
        self, network_id: str, switch_stack_id: str, subnet: str, nextHopIp: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a layer 3 static route for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-static-route

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            subnet: The subnet which is routed via this static route and should be specified in CIDR
              notation (ex. 1.2.3.0/24).
            nextHopIp: IP address of the next hop device to which the device sends its traffic for
              the subnet.
            name: Name or description for layer 3 static route.
            advertiseViaOspfEnabled: Option to advertise static route via OSPF.
            preferOverOspfRoutesEnabled: Option to prefer static route over OSPF routes.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "create_network_switch_stack_routing_static_route",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        switch_stack_id = urllib.parse.quote(switch_stack_id, safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes"

        body_params = [
            "name",
            "subnet",
            "nextHopIp",
            "advertiseViaOspfEnabled",
            "preferOverOspfRoutesEnabled",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_switch_stack_routing_static_route(
        self, network_id: str, switch_stack_id: str, static_route_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a layer 3 static route for a switch stack.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-static-route

        Args:
            network_id: Network ID.
            switch_stack_id: Switch stack ID.
            static_route_id: Static route ID.
            name: Name or description for layer 3 static route.
            subnet: The subnet which is routed via this static route and should be specified in CIDR
              notation (ex. 1.2.3.0/24).
            nextHopIp: IP address of the next hop device to which the device sends its traffic for
              the subnet.
            managementNextHop: Optional fallback IP address for management traffic.
            advertiseViaOspfEnabled: Option to advertise static route via OSPF.
            preferOverOspfRoutesEnabled: Option to prefer static route over OSPF routes.
            vrf: The VRF settings of the interface. Requires IOS XE 17.18 or higher.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "update_network_switch_stack_routing_static_route",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        switch_stack_id = urllib.parse.quote(switch_stack_id, safe="")
        static_route_id = urllib.parse.quote(static_route_id, safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes/{static_route_id}"

        body_params = [
            "name",
            "subnet",
            "nextHopIp",
            "managementNextHop",
            "advertiseViaOspfEnabled",
            "preferOverOspfRoutesEnabled",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_network_switch_stack_routing_static_route(
        self, network_id: str, switch_stack_id: str, static_route_id: str
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(network_id, safe="")
        switch_stack_id = urllib.parse.quote(switch_stack_id, safe="")
        static_route_id = urllib.parse.quote(static_route_id, safe="")
        resource = f"/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes/{static_route_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def update_network_switch_storm_control(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update the storm control configuration for a switch network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control

        Args:
            network_id: Network ID.
            broadcastThreshold: Percentage (1 to 99) of total available port bandwidth for broadcast
              traffic type. Default value 100 percent rate is to clear the
              configuration.
            multicastThreshold: Percentage (1 to 99) of total available port bandwidth for multicast
              traffic type. Default value 100 percent rate is to clear the
              configuration.
            unknownUnicastThreshold: Percentage (1 to 99) of total available port bandwidth for
              unknown unicast (dlf-destination lookup failure) traffic type. Default
              value 100 percent rate is to clear the configuration.
            treatTheseTrafficTypesAsOneThreshold: Grouped traffic types.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "stormControl"],
            "operation": "update_network_switch_storm_control",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/stormControl"

        body_params = [
            "broadcastThreshold",
            "multicastThreshold",
            "unknownUnicastThreshold",
            "treatTheseTrafficTypesAsOneThreshold",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_switch_stp(self, network_id: str, **kwargs: Any) -> dict[str, Any]:
        """Updates STP settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stp

        Args:
            network_id: Network ID.
            rstpEnabled: The spanning tree protocol status in network.
            stpBridgePriority: STP bridge priority for switches/stacks or switch templates. An empty
              array will clear the STP bridge priority settings.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "stp"],
            "operation": "update_network_switch_stp",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/switch/stp"

        body_params = [
            "rstpEnabled",
            "stpBridgePriority",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_config_template_switch_profile_port(
        self,
        organization_id: str,
        config_template_id: str,
        profile_id: str,
        port_id: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
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
            poeEnabled: The PoE status of the switch template port.
            type: The type of the switch template port ('access', 'trunk', 'stack', 'routed', 'svl'
              or 'dad').
            vlan: The VLAN of the switch template port. For a trunk port, this is the native VLAN. A
              null value will clear the value set for trunk ports.
            voiceVlan: The voice VLAN of the switch template port. Only applicable to access ports.
            allowedVlans: The VLANs allowed on the switch template port. Only applicable to trunk
              ports.
            isolationEnabled: The isolation status of the switch template port.
            rstpEnabled: The rapid spanning tree protocol status.
            stpGuard: The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop
              guard').
            stpPortFastTrunk: The state of STP PortFast Trunk on the switch template port.
            linkNegotiation: The link speed for the switch template port.
            portScheduleId: The ID of the port schedule. A value of null will clear the port
              schedule.
            udld: The action to take when Unidirectional Link is detected (Alert only, Enforce).
              Default configuration is Alert only.
            accessPolicyType: The type of the access policy of the switch template port. Only
              applicable to access ports. Can be one of 'Open', 'Custom access policy',
              'MAC allow list' or 'Sticky MAC allow list'.
            accessPolicyNumber: The number of a custom access policy to configure on the switch
              template port. Only applicable when 'accessPolicyType' is 'Custom access
              policy'.
            macAllowList: Only devices with MAC addresses specified in this list will have access to
              this port. Up to 20 MAC addresses can be defined. Only applicable when
              'accessPolicyType' is 'MAC allow list'.
            macWhitelistLimit: The maximum number of MAC addresses for regular MAC allow list. Only
              applicable when 'accessPolicyType' is 'MAC allow list'.           Note:
              Config only supported on verions greater than ms18 only for classic
              switches.
            stickyMacAllowList: The initial list of MAC addresses for sticky Mac allow list. Only
              applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
            stickyMacAllowListLimit: The maximum number of MAC addresses for sticky MAC allow list.
              Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
            stormControlEnabled: The storm control status of the switch template port.
            flexibleStackingEnabled: For supported switches (e.g. MS420/MS425), whether or not the
              port has flexible stacking enabled.
            daiTrusted: If true, ARP packets for this port will be considered trusted, and Dynamic
              ARP Inspection will allow the traffic.
            profile: Profile attributes.
            dot3az: dot3az settings for the port.
            highSpeed: High speed port enablement settings for C9500-32QC.

        """
        kwargs.update(locals())

        if "type" in kwargs:
            options = ["access", "dad", "routed", "stack", "svl", "trunk"]
            assert kwargs["type"] in options, (
                f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
            )
        if "stpGuard" in kwargs:
            options = ["bpdu guard", "disabled", "loop guard", "root guard"]
            assert kwargs["stpGuard"] in options, (
                f'''"stpGuard" cannot be "{kwargs["stpGuard"]}", & must be set to one of: {options}'''
            )
        if "udld" in kwargs:
            options = ["Alert only", "Enforce"]
            assert kwargs["udld"] in options, (
                f'''"udld" cannot be "{kwargs["udld"]}", & must be set to one of: {options}'''
            )
        if "accessPolicyType" in kwargs:
            options = ["Custom access policy", "MAC allow list", "Open", "Sticky MAC allow list"]
            assert kwargs["accessPolicyType"] in options, (
                f'''"accessPolicyType" cannot be "{kwargs["accessPolicyType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports"],
            "operation": "update_organization_config_template_switch_profile_port",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        config_template_id = urllib.parse.quote(config_template_id, safe="")
        profile_id = urllib.parse.quote(profile_id, safe="")
        port_id = urllib.parse.quote(port_id, safe="")
        resource = f"/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}"

        body_params = [
            "name",
            "tags",
            "enabled",
            "poeEnabled",
            "type",
            "vlan",
            "voiceVlan",
            "allowedVlans",
            "isolationEnabled",
            "rstpEnabled",
            "stpGuard",
            "stpPortFastTrunk",
            "linkNegotiation",
            "portScheduleId",
            "udld",
            "accessPolicyType",
            "accessPolicyNumber",
            "macAllowList",
            "macWhitelistLimit",
            "stickyMacAllowList",
            "stickyMacAllowListLimit",
            "stormControlEnabled",
            "flexibleStackingEnabled",
            "daiTrusted",
            "profile",
            "dot3az",
            "highSpeed",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def clone_organization_switch_devices(
        self, organization_id: str, sourceSerial: str, targetSerials: list
    ) -> dict[str, Any]:
        """Clone port-level and some switch-level configuration settings from a source switch to one or more target switches.

        https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices

        Args:
            organization_id: Organization ID.
            sourceSerial: Serial number of the source switch (must be on a network not bound to a
              template).
            targetSerials: Array of serial numbers of one or more target switches (must be on a
              network not bound to a template).

        """
        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "devices"],
            "operation": "clone_organization_switch_devices",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/switch/devices/clone"

        body_params = [
            "sourceSerial",
            "targetSerials",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action
