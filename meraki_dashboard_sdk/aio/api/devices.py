"""Devices API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncDevices:
    """Devices class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_device(self, serial: str) -> dict[str, Any] | None:
        """Return a single device.

        https://developer.cisco.com/meraki/api-v1/#!get-device

        Args:
            serial: Serial.

        """
        metadata = {"tags": ["devices", "configure"], "operation": "get_device"}
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}"

        return self._session.get(metadata, resource)

    def update_device(self, serial: str, **kwargs: Any) -> dict[str, Any] | None:
        """Update the attributes of a device.

        https://developer.cisco.com/meraki/api-v1/#!update-device

        Args:
            serial: Serial.
            name: The name of a device.
            tags: The list of tags of a device.
            lat: The latitude of a device.
            lng: The longitude of a device.
            address: The address of a device.
            notes: The notes for the device. String. Limited to 255 characters.
            moveMapMarker: Whether or not to set the latitude and longitude of a device based on the
              new address. Only applies when lat and lng are not specified.
            switchProfileId: The ID of a switch template to bind to the device (for available switch
              templates, see the 'Switch Templates' endpoint). Use null to unbind the
              switch device from the current profile. For a device to be bindable to a
              switch template, it must (1) be a switch, and (2) belong to a network that
              is bound to a configuration template.
            floorPlanId: The floor plan to associate to this device. null disassociates the device
              from the floorplan.

        """
        kwargs.update(locals())

        metadata = {"tags": ["devices", "configure"], "operation": "update_device"}
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}"

        body_params = [
            "name",
            "tags",
            "lat",
            "lng",
            "address",
            "notes",
            "moveMapMarker",
            "switchProfileId",
            "floorPlanId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def blink_device_leds(self, serial: str, **kwargs: Any) -> dict[str, Any] | None:
        """Blink the LEDs on a device.

        https://developer.cisco.com/meraki/api-v1/#!blink-device-leds

        Args:
            serial: Serial.
            duration: The duration in seconds. Must be between 5 and 120. Default is 20 seconds.
            period: The period in milliseconds. Must be between 100 and 1000. Default is 160
              milliseconds.
            duty: The duty cycle as the percent active. Must be between 10 and 90. Default is 50.

        """
        kwargs.update(locals())

        metadata = {"tags": ["devices", "liveTools"], "operation": "blink_device_leds"}
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/blinkLeds"

        body_params = [
            "duration",
            "period",
            "duty",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_cellular_sims(self, serial: str) -> dict[str, Any] | None:
        """Return the SIM and APN configurations for a cellular device.

        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-sims

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["devices", "configure", "cellular", "sims"],
            "operation": "get_device_cellular_sims",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellular/sims"

        return self._session.get(metadata, resource)

    def update_device_cellular_sims(self, serial: str, **kwargs: Any) -> dict[str, Any] | None:
        """Updates the SIM and APN configurations for a cellular device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-sims

        Args:
            serial: Serial.
            sims: List of SIMs. If a SIM was previously configured and not specified in this
              request, it will remain unchanged.
            simOrdering: Specifies the ordering of all SIMs for an MG: primary, secondary, and not-
              in-use (when applicable). It's required for devices with 3 or more SIMs
              and can be used in place of 'isPrimary' for dual-SIM devices. To indicate
              eSIM, use 'sim3'. Sim failover will occur only between primary and
              secondary sim slots.
            simFailover: SIM Failover settings.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "configure", "cellular", "sims"],
            "operation": "update_device_cellular_sims",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellular/sims"

        body_params = [
            "sims",
            "simOrdering",
            "simFailover",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_device_clients(self, serial: str, **kwargs: Any) -> dict[str, Any] | None:
        """List the clients of a device, up to a maximum of a month ago.

        https://developer.cisco.com/meraki/api-v1/#!get-device-clients

        Args:
            serial: Serial.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {"tags": ["devices", "monitor", "clients"], "operation": "get_device_clients"}
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/clients"

        query_params = [
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def create_device_live_tools_arp_table(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to perform a ARP table request for the device.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-arp-table

        Args:
            serial: Serial.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "arpTable"],
            "operation": "create_device_live_tools_arp_table",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/arpTable"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_arp_table(
        self, serial: str, arpTableId: str
    ) -> dict[str, Any] | None:
        """Return an ARP table live tool job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-arp-table

        Args:
            serial: Serial.
            arpTableId: Arp table ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "arpTable"],
            "operation": "get_device_live_tools_arp_table",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        arpTableId = urllib.parse.quote(str(arpTableId), safe="")
        resource = f"/devices/{serial}/liveTools/arpTable/{arpTableId}"

        return self._session.get(metadata, resource)

    def create_device_live_tools_cable_test(
        self, serial: str, ports: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to perform a cable test for the device on the specified ports.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-cable-test

        Args:
            serial: Serial.
            ports: A list of ports for which to perform the cable test.  For Catalyst switches, IOS
              interface names are also supported, such as "GigabitEthernet1/0/8",
              "Gi1/0/8", or even "1/0/8".
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "cableTest"],
            "operation": "create_device_live_tools_cable_test",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/cableTest"

        body_params = [
            "ports",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_cable_test(self, serial: str, id: str) -> dict[str, Any] | None:
        """Return a cable test live tool job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-cable-test

        Args:
            serial: Serial.
            id: ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "cableTest"],
            "operation": "get_device_live_tools_cable_test",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/cableTest/{id}"

        return self._session.get(metadata, resource)

    def create_device_live_tools_leds_blink(
        self, serial: str, duration: int, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to blink LEDs on a device.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-leds-blink

        Args:
            serial: Serial.
            duration: The duration in seconds to blink LEDs.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "leds", "blink"],
            "operation": "create_device_live_tools_leds_blink",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/leds/blink"

        body_params = [
            "duration",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_leds_blink(
        self, serial: str, ledsBlinkId: str
    ) -> dict[str, Any] | None:
        """Return a blink LEDs job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-leds-blink

        Args:
            serial: Serial.
            ledsBlinkId: Leds blink ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "leds", "blink"],
            "operation": "get_device_live_tools_leds_blink",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        ledsBlinkId = urllib.parse.quote(str(ledsBlinkId), safe="")
        resource = f"/devices/{serial}/liveTools/leds/blink/{ledsBlinkId}"

        return self._session.get(metadata, resource)

    def create_device_live_tools_mac_table(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to request the MAC table from the device.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-mac-table

        Args:
            serial: Serial.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "macTable"],
            "operation": "create_device_live_tools_mac_table",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/macTable"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_mac_table(
        self, serial: str, macTableId: str
    ) -> dict[str, Any] | None:
        """Return a MAC table live tool job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-mac-table

        Args:
            serial: Serial.
            macTableId: Mac table ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "macTable"],
            "operation": "get_device_live_tools_mac_table",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        macTableId = urllib.parse.quote(str(macTableId), safe="")
        resource = f"/devices/{serial}/liveTools/macTable/{macTableId}"

        return self._session.get(metadata, resource)

    def create_device_live_tools_multicast_routing(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to perform a Multicast routing request for the device.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-multicast-routing

        Args:
            serial: Serial.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "multicastRouting"],
            "operation": "create_device_live_tools_multicast_routing",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/multicastRouting"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_multicast_routing(
        self, serial: str, multicastRoutingId: str
    ) -> dict[str, Any] | None:
        """Return a Multicast routing live tool job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-multicast-routing

        Args:
            serial: Serial.
            multicastRoutingId: Multicast routing ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "multicastRouting"],
            "operation": "get_device_live_tools_multicast_routing",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        multicastRoutingId = urllib.parse.quote(str(multicastRoutingId), safe="")
        resource = f"/devices/{serial}/liveTools/multicastRouting/{multicastRoutingId}"

        return self._session.get(metadata, resource)

    def create_device_live_tools_ping(
        self, serial: str, target: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to ping a target host from the device.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ping

        Args:
            serial: Serial.
            target: FQDN, IPv4 or IPv6 address.
            count: Count parameter to pass to ping. [1..5], default 5.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "ping"],
            "operation": "create_device_live_tools_ping",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/ping"

        body_params = [
            "target",
            "count",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_ping(self, serial: str, id: str) -> dict[str, Any] | None:
        """Return a ping job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ping

        Args:
            serial: Serial.
            id: ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "ping"],
            "operation": "get_device_live_tools_ping",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/ping/{id}"

        return self._session.get(metadata, resource)

    def create_device_live_tools_ping_device(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to check connectivity status to the device.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ping-device

        Args:
            serial: Serial.
            count: Count parameter to pass to ping. [1..5], default 5.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "pingDevice"],
            "operation": "create_device_live_tools_ping_device",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/pingDevice"

        body_params = [
            "count",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_ping_device(self, serial: str, id: str) -> dict[str, Any] | None:
        """Return a ping device job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ping-device

        Args:
            serial: Serial.
            id: ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "pingDevice"],
            "operation": "get_device_live_tools_ping_device",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/pingDevice/{id}"

        return self._session.get(metadata, resource)

    def create_device_live_tools_throughput_test(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to test a device throughput, the test will run for 10 secs to test throughput.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-throughput-test

        Args:
            serial: Serial.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "throughputTest"],
            "operation": "create_device_live_tools_throughput_test",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/throughputTest"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_throughput_test(
        self, serial: str, throughputTestId: str
    ) -> dict[str, Any] | None:
        """Return a throughput test job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-throughput-test

        Args:
            serial: Serial.
            throughputTestId: Throughput test ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "throughputTest"],
            "operation": "get_device_live_tools_throughput_test",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        throughputTestId = urllib.parse.quote(str(throughputTestId), safe="")
        resource = f"/devices/{serial}/liveTools/throughputTest/{throughputTestId}"

        return self._session.get(metadata, resource)

    def create_device_live_tools_wake_on_lan(
        self, serial: str, vlanId: int, mac: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to send a Wake-on-LAN packet from the device.

        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-wake-on-lan

        Args:
            serial: Serial.
            vlanId: The target's VLAN (1 to 4094).
            mac: The target's MAC address.
            callback: Details for the callback. Please include either an httpServerId OR url and
              sharedSecret.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "wakeOnLan"],
            "operation": "create_device_live_tools_wake_on_lan",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/wakeOnLan"

        body_params = [
            "vlanId",
            "mac",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_live_tools_wake_on_lan(
        self, serial: str, wakeOnLanId: str
    ) -> dict[str, Any] | None:
        """Return a Wake-on-LAN job.

        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-wake-on-lan

        Args:
            serial: Serial.
            wakeOnLanId: Wake on lan ID.

        """
        metadata = {
            "tags": ["devices", "liveTools", "wakeOnLan"],
            "operation": "get_device_live_tools_wake_on_lan",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        wakeOnLanId = urllib.parse.quote(str(wakeOnLanId), safe="")
        resource = f"/devices/{serial}/liveTools/wakeOnLan/{wakeOnLanId}"

        return self._session.get(metadata, resource)

    def get_device_lldp_cdp(self, serial: str) -> dict[str, Any] | None:
        """List LLDP and CDP information for a device.

        https://developer.cisco.com/meraki/api-v1/#!get-device-lldp-cdp

        Args:
            serial: Serial.

        """
        metadata = {"tags": ["devices", "monitor", "lldpCdp"], "operation": "get_device_lldp_cdp"}
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/lldpCdp"

        return self._session.get(metadata, resource)

    def get_device_loss_and_latency_history(
        self, serial: str, ip: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for MX, MG and Z devices.

        https://developer.cisco.com/meraki/api-v1/#!get-device-loss-and-latency-history

        Args:
            serial: Serial.
            ip: The destination IP used to obtain the requested stats. This is required.
            t0: The beginning of the timespan for the data. The maximum lookback period is 60 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              60, 600, 3600, 86400. The default is 60.
            uplink: The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2,
              wan3, cellular. The default is wan1.

        """
        kwargs.update(locals())

        if "uplink" in kwargs:
            options = ["cellular", "wan1", "wan2", "wan3"]
            assert kwargs["uplink"] in options, (
                f'''"uplink" cannot be "{kwargs["uplink"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["devices", "monitor", "uplinks", "lossAndLatencyHistory"],
            "operation": "get_device_loss_and_latency_history",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/lossAndLatencyHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "uplink",
            "ip",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_device_management_interface(self, serial: str) -> dict[str, Any] | None:
        """Return the management interface settings for a device.

        https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["devices", "configure", "managementInterface"],
            "operation": "get_device_management_interface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/managementInterface"

        return self._session.get(metadata, resource)

    def update_device_management_interface(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the management interface settings for a device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-management-interface

        Args:
            serial: Serial.
            wan1: WAN 1 settings.
            wan2: WAN 2 settings (only for MX devices).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "configure", "managementInterface"],
            "operation": "update_device_management_interface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/managementInterface"

        body_params = [
            "wan1",
            "wan2",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def reboot_device(self, serial: str) -> dict[str, Any] | None:
        """Reboot a device.

        https://developer.cisco.com/meraki/api-v1/#!reboot-device

        Args:
            serial: Serial.

        """
        metadata = {"tags": ["devices", "liveTools"], "operation": "reboot_device"}
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/reboot"

        return self._session.post(metadata, resource)
