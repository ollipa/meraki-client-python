"""Wireless API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.rest_session import RestSession


class Wireless:
    """Wireless class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
        self._session = session

    def update_device_wireless_alternate_management_interface_ipv6(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/alternateManagementInterface/ipv6"

        body_params = [
            "addresses",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_device_wireless_bluetooth_settings(self, serial: str) -> dict[str, Any] | None:
        """Return the bluetooth settings for a wireless device.

        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-bluetooth-settings

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "get_device_wireless_bluetooth_settings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/bluetooth/settings"

        return self._session.get(metadata, resource)

    def update_device_wireless_bluetooth_settings(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/bluetooth/settings"

        body_params = [
            "uuid",
            "major",
            "minor",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_device_wireless_connection_stats(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for a given AP on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-connection-stats

        Args:
            serial: Serial.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "connectionStats"],
            "operation": "get_device_wireless_connection_stats",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_device_wireless_electronic_shelf_label(self, serial: str) -> dict[str, Any] | None:
        """Return the ESL settings of a device.

        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-electronic-shelf-label

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "get_device_wireless_electronic_shelf_label",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/electronicShelfLabel"

        return self._session.get(metadata, resource)

    def update_device_wireless_electronic_shelf_label(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/electronicShelfLabel"

        body_params = [
            "channel",
            "enabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_device_wireless_latency_stats(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated latency info for a given AP on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-latency-stats

        Args:
            serial: Serial.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "latencyStats"],
            "operation": "get_device_wireless_latency_stats",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_device_wireless_radio_settings(self, serial: str) -> dict[str, Any] | None:
        """Return the manually configured radio settings overrides of a device, which take precedence over RF profiles.

        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-settings

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["wireless", "configure", "radio", "settings"],
            "operation": "get_device_wireless_radio_settings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/settings"

        return self._session.get(metadata, resource)

    def update_device_wireless_radio_settings(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/settings"

        body_params = [
            "rfProfileId",
            "twoFourGhzSettings",
            "fiveGhzSettings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_device_wireless_status(self, serial: str) -> dict[str, Any] | None:
        """Return the SSID statuses of an access point.

        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-status

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["wireless", "monitor", "status"],
            "operation": "get_device_wireless_status",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/status"

        return self._session.get(metadata, resource)

    def create_device_wireless_zigbee_enrollment(self, serial: str) -> dict[str, Any] | None:
        """Enqueue a job to start enrolling door locks on zigbee configured wireless devices.

        https://developer.cisco.com/meraki/api-v1/#!create-device-wireless-zigbee-enrollment

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "enrollments"],
            "operation": "create_device_wireless_zigbee_enrollment",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/zigbee/enrollments"

        return self._session.post(metadata, resource)

    def get_device_wireless_zigbee_enrollment(
        self, serial: str, enrollmentId: str
    ) -> dict[str, Any] | None:
        """Return an enrollment.

        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-zigbee-enrollment

        Args:
            serial: Serial.
            enrollmentId: Enrollment ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "enrollments"],
            "operation": "get_device_wireless_zigbee_enrollment",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        enrollmentId = urllib.parse.quote(str(enrollmentId), safe="")
        resource = f"/devices/{serial}/wireless/zigbee/enrollments/{enrollmentId}"

        return self._session.get(metadata, resource)

    def get_network_wireless_air_marshal(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """List Air Marshal scan results from a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-air-marshal

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 7 days.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "airMarshal"],
            "operation": "get_network_wireless_air_marshal",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal"

        query_params = [
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def create_network_wireless_air_marshal_rule(
        self, networkId: str, type: str, match: dict
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal/rules"

        body_params = [
            "type",
            "match",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_network_wireless_air_marshal_rule(
        self, networkId: str, ruleId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        ruleId = urllib.parse.quote(str(ruleId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal/rules/{ruleId}"

        body_params = [
            "type",
            "match",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_wireless_air_marshal_rule(self, networkId: str, ruleId: str) -> None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        ruleId = urllib.parse.quote(str(ruleId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal/rules/{ruleId}"

        return self._session.delete(metadata, resource)

    def update_network_wireless_air_marshal_settings(
        self, networkId: str, defaultPolicy: str
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal/settings"

        body_params = [
            "defaultPolicy",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_alternate_management_interface(
        self, networkId: str
    ) -> dict[str, Any] | None:
        """Return alternate management interface and devices with IP assigned.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-alternate-management-interface

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "alternateManagementInterface"],
            "operation": "get_network_wireless_alternate_management_interface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/alternateManagementInterface"

        return self._session.get(metadata, resource)

    def update_network_wireless_alternate_management_interface(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/alternateManagementInterface"

        body_params = [
            "enabled",
            "vlanId",
            "protocols",
            "accessPoints",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_billing(self, networkId: str) -> dict[str, Any] | None:
        """Return the billing settings of this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-billing

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "billing"],
            "operation": "get_network_wireless_billing",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/billing"

        return self._session.get(metadata, resource)

    def update_network_wireless_billing(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/billing"

        body_params = [
            "currency",
            "plans",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_bluetooth_settings(self, networkId: str) -> dict[str, Any] | None:
        """Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-bluetooth-settings

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "get_network_wireless_bluetooth_settings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/bluetooth/settings"

        return self._session.get(metadata, resource)

    def update_network_wireless_bluetooth_settings(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the Bluetooth settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-bluetooth-settings

        Args:
            networkId: Network ID.
            scanningEnabled: Whether APs will scan for Bluetooth enabled clients.
            advertisingEnabled: Whether APs will advertise beacons.
            uuid: The UUID to be used in the beacon identifier.
            majorMinorAssignmentMode: The way major and minor number should be assigned to nodes in
              the network. ('Unique', 'Non-unique').
            major: The major number to be used in the beacon identifier. Only valid in 'Non-unique'
              mode.
            minor: The minor number to be used in the beacon identifier. Only valid in 'Non-unique'
              mode.

        """
        kwargs.update(locals())

        if "majorMinorAssignmentMode" in kwargs:
            options = ["Non-unique", "Unique"]
            assert kwargs["majorMinorAssignmentMode"] in options, (
                f'''"majorMinorAssignmentMode" cannot be "{kwargs["majorMinorAssignmentMode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "update_network_wireless_bluetooth_settings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/bluetooth/settings"

        body_params = [
            "scanningEnabled",
            "advertisingEnabled",
            "uuid",
            "majorMinorAssignmentMode",
            "major",
            "minor",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_channel_utilization_history(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return AP channel utilization over time for a device or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-channel-utilization-history

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              600, 1200, 3600, 14400, 86400. The default is 86400.
            autoResolution: Automatically select a data resolution based on the given timespan; this
              overrides the value specified by the 'resolution' parameter. The default
              setting is false.
            clientId: Filter results by network client to return per-device, per-band AP channel
              utilization metrics inner joined by the queried client's connection
              history.
            deviceSerial: Filter results by device to return AP channel utilization metrics for the
              queried device; either :band or :clientId must be jointly specified.
            apTag: Filter results by AP tag to return AP channel utilization metrics for devices
              labeled with the given tag; either :clientId or :deviceSerial must be
              jointly specified.
            band: Filter results by band (either '2.4', '5' or '6').

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "channelUtilizationHistory"],
            "operation": "get_network_wireless_channel_utilization_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/channelUtilizationHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_client_count_history(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return wireless client counts over time for a network, device, or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-count-history

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            autoResolution: Automatically select a data resolution based on the given timespan; this
              overrides the value specified by the 'resolution' parameter. The default
              setting is false.
            clientId: Filter results by network client to return per-device client counts over time
              inner joined by the queried client's connection history.
            deviceSerial: Filter results by device.
            apTag: Filter results by AP tag.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clientCountHistory"],
            "operation": "get_network_wireless_client_count_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/clientCountHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_clients_connection_stats(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for this network, grouped by clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-connection-stats

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectionStats"],
            "operation": "get_network_wireless_clients_connection_stats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_clients_latency_stats(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated latency info for this network, grouped by clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-latency-stats

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "latencyStats"],
            "operation": "get_network_wireless_clients_latency_stats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_client_connection_stats(
        self, networkId: str, clientId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for a given client on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connection-stats

        Args:
            networkId: Network ID.
            clientId: Client ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectionStats"],
            "operation": "get_network_wireless_client_connection_stats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_client_connectivity_events(
        self, networkId: str, clientId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the wireless connectivity events for a client within a network in the timespan.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connectivity-events

        Args:
            networkId: Network ID.
            clientId: Client ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sortOrder: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'ascending'.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            types: A list of event types to include. If not specified, events of all types will be
              returned. Valid types are 'assoc', 'disassoc', 'auth', 'deauth', 'dns',
              'dhcp', 'roam', 'connection' and/or 'sticky'.
            band: Filter results by band. Valid bands are '2.4', '5' or '6'.
            ssidNumber: Filter results by SSID. If not specified, events for all SSIDs will be
              returned.
            includedSeverities: A list of severities to include. If not specified, events of all
              severities will be returned. Valid severities are 'good', 'info', 'warn'
              and/or 'bad'.
            deviceSerial: Filter results by an AP's serial number.

        """
        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )
        if "ssidNumber" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssidNumber"] in options, (
                f'''"ssidNumber" cannot be "{kwargs["ssidNumber"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectivityEvents"],
            "operation": "get_network_wireless_client_connectivity_events",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/connectivityEvents"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "t0",
            "t1",
            "timespan",
            "types",
            "band",
            "ssidNumber",
            "includedSeverities",
            "deviceSerial",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "includedSeverities",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_wireless_client_latency_history(
        self, networkId: str, clientId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return the latency history for a client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-history

        Args:
            networkId: Network ID.
            clientId: Client ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 791 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 791 days. The default is 1 day.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              86400. The default is 86400.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "clients", "latencyHistory"],
            "operation": "get_network_wireless_client_latency_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/latencyHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_client_latency_stats(
        self, networkId: str, clientId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated latency info for a given client on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-stats

        Args:
            networkId: Network ID.
            clientId: Client ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "latencyStats"],
            "operation": "get_network_wireless_client_latency_stats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_connection_stats(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-connection-stats

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "connectionStats"],
            "operation": "get_network_wireless_connection_stats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_data_rate_history(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return PHY data rates over time for a network, device, or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-data-rate-history

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            autoResolution: Automatically select a data resolution based on the given timespan; this
              overrides the value specified by the 'resolution' parameter. The default
              setting is false.
            clientId: Filter results by network client.
            deviceSerial: Filter results by device.
            apTag: Filter results by AP tag.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "dataRateHistory"],
            "operation": "get_network_wireless_data_rate_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/dataRateHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_devices_connection_stats(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for this network, grouped by node.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-connection-stats

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "devices", "connectionStats"],
            "operation": "get_network_wireless_devices_connection_stats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/devices/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_devices_latency_stats(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated latency info for this network, grouped by node.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-latency-stats

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "devices", "latencyStats"],
            "operation": "get_network_wireless_devices_latency_stats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/devices/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_electronic_shelf_label(self, networkId: str) -> dict[str, Any] | None:
        """Return the ESL settings of a wireless network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-electronic-shelf-label

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "get_network_wireless_electronic_shelf_label",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/electronicShelfLabel"

        return self._session.get(metadata, resource)

    def update_network_wireless_electronic_shelf_label(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/electronicShelfLabel"

        body_params = [
            "hostname",
            "enabled",
            "mode",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_electronic_shelf_label_configured_devices(
        self, networkId: str
    ) -> dict[str, Any] | None:
        """Get a list of all ESL eligible devices of a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-electronic-shelf-label-configured-devices

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel", "configuredDevices"],
            "operation": "get_network_wireless_electronic_shelf_label_configured_devices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/electronicShelfLabel/configuredDevices"

        return self._session.get(metadata, resource)

    def get_network_wireless_ethernet_ports_profiles(self, networkId: str) -> dict[str, Any] | None:
        """List the AP port profiles for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profiles

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "get_network_wireless_ethernet_ports_profiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles"

        return self._session.get(metadata, resource)

    def create_network_wireless_ethernet_ports_profile(
        self, networkId: str, name: str, ports: list, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles"

        body_params = [
            "name",
            "ports",
            "usbPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def assign_network_wireless_ethernet_ports_profiles(
        self, networkId: str, serials: list, profileId: str
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/assign"

        body_params = [
            "serials",
            "profileId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def set_network_wireless_ethernet_ports_profiles_default(
        self, networkId: str, profileId: str
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/setDefault"

        body_params = [
            "profileId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_wireless_ethernet_ports_profile(
        self, networkId: str, profileId: str
    ) -> dict[str, Any] | None:
        """Show the AP port profile by ID for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profile

        Args:
            networkId: Network ID.
            profileId: Profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "get_network_wireless_ethernet_ports_profile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}"

        return self._session.get(metadata, resource)

    def update_network_wireless_ethernet_ports_profile(
        self, networkId: str, profileId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}"

        body_params = [
            "name",
            "ports",
            "usbPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_wireless_ethernet_ports_profile(
        self, networkId: str, profileId: str
    ) -> None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}"

        return self._session.delete(metadata, resource)

    def get_network_wireless_failed_connections(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """List of all failed client connection events on this network in a given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-failed-connections

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.
            serial: Filter by AP.
            clientId: Filter by client MAC.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "failedConnections"],
            "operation": "get_network_wireless_failed_connections",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/failedConnections"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "serial",
            "clientId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_latency_history(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return average wireless latency over time for a network, device, or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-history

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            autoResolution: Automatically select a data resolution based on the given timespan; this
              overrides the value specified by the 'resolution' parameter. The default
              setting is false.
            clientId: Filter results by network client.
            deviceSerial: Filter results by device.
            apTag: Filter results by AP tag.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.
            accessCategory: Filter by access category.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )
        if "accessCategory" in kwargs:
            options = ["backgroundTraffic", "bestEffortTraffic", "videoTraffic", "voiceTraffic"]
            assert kwargs["accessCategory"] in options, (
                f'''"accessCategory" cannot be "{kwargs["accessCategory"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "latencyHistory"],
            "operation": "get_network_wireless_latency_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/latencyHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
            "accessCategory",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_latency_stats(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Aggregated latency info for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-stats

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            apTag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "latencyStats"],
            "operation": "get_network_wireless_latency_stats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def update_network_wireless_location_scanning(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/location/scanning"

        body_params = [
            "enabled",
            "api",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_mesh_statuses(
        self, networkId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List wireless mesh statuses for repeaters.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-mesh-statuses

        Args:
            networkId: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 500. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "meshStatuses"],
            "operation": "get_network_wireless_mesh_statuses",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/meshStatuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_wireless_rf_profiles(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """List RF profiles for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles

        Args:
            networkId: Network ID.
            includeTemplateProfiles: If the network is bound to a template, this parameter controls
              whether or not the non-basic RF profiles defined on the template should be
              included in the response alongside the non-basic profiles defined on the
              bound network. Defaults to false.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "get_network_wireless_rf_profiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/rfProfiles"

        query_params = [
            "includeTemplateProfiles",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def create_network_wireless_rf_profile(
        self, networkId: str, name: str, bandSelectionType: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
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

        return self._session.post(metadata, resource, payload)

    def update_network_wireless_rf_profile(
        self, networkId: str, rfProfileId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe="")
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

        return self._session.put(metadata, resource, payload)

    def delete_network_wireless_rf_profile(self, networkId: str, rfProfileId: str) -> None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe="")
        resource = f"/networks/{networkId}/wireless/rfProfiles/{rfProfileId}"

        return self._session.delete(metadata, resource)

    def get_network_wireless_rf_profile(
        self, networkId: str, rfProfileId: str
    ) -> dict[str, Any] | None:
        """Return a RF profile.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile

        Args:
            networkId: Network ID.
            rfProfileId: Rf profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "get_network_wireless_rf_profile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe="")
        resource = f"/networks/{networkId}/wireless/rfProfiles/{rfProfileId}"

        return self._session.get(metadata, resource)

    def get_network_wireless_settings(self, networkId: str) -> dict[str, Any] | None:
        """Return the wireless settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-settings

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "settings"],
            "operation": "get_network_wireless_settings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/settings"

        return self._session.get(metadata, resource)

    def update_network_wireless_settings(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
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

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_signal_quality_history(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return signal quality (SNR/RSSI) over time for a device or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-signal-quality-history

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            autoResolution: Automatically select a data resolution based on the given timespan; this
              overrides the value specified by the 'resolution' parameter. The default
              setting is false.
            clientId: Filter results by network client.
            deviceSerial: Filter results by device.
            apTag: Filter results by AP tag; either :clientId or :deviceSerial must be jointly
              specified.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "signalQualityHistory"],
            "operation": "get_network_wireless_signal_quality_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/signalQualityHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_wireless_ssids(self, networkId: str) -> dict[str, Any] | None:
        """List the MR SSIDs in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssids

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "get_network_wireless_ssids",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ssids"

        return self._session.get(metadata, resource)

    def get_network_wireless_ssid(self, networkId: str, number: str) -> dict[str, Any] | None:
        """Return a single MR SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "get_network_wireless_ssid",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
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

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_bonjour_forwarding(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """List the Bonjour forwarding setting and rules for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-bonjour-forwarding

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "bonjourForwarding"],
            "operation": "get_network_wireless_ssid_bonjour_forwarding",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_bonjour_forwarding(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding"

        body_params = [
            "enabled",
            "rules",
            "exception",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_device_type_group_policies(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """List the device type group policies for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-device-type-group-policies

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "deviceTypeGroupPolicies"],
            "operation": "get_network_wireless_ssid_device_type_group_policies",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_device_type_group_policies(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies"

        body_params = [
            "enabled",
            "deviceTypePolicies",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_eap_override(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """Return the EAP overridden parameters for an SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-eap-override

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "eapOverride"],
            "operation": "get_network_wireless_ssid_eap_override",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/eapOverride"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_eap_override(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/eapOverride"

        body_params = [
            "timeout",
            "identity",
            "maxRetries",
            "eapolKey",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_firewall_l3_firewall_rules(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """Return the L3 firewall rules for an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-3-firewall-rules

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l3FirewallRules"],
            "operation": "get_network_wireless_ssid_firewall_l3_firewall_rules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_firewall_l3_firewall_rules(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules"

        body_params = [
            "rules",
            "allowLanAccess",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_firewall_l7_firewall_rules(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """Return the L7 firewall rules for an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-7-firewall-rules

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l7FirewallRules"],
            "operation": "get_network_wireless_ssid_firewall_l7_firewall_rules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_firewall_l7_firewall_rules(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules"

        body_params = [
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_hotspot20(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """Return the Hotspot 2.0 settings for an SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-hotspot-2-0

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "hotspot20"],
            "operation": "get_network_wireless_ssid_hotspot20",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/hotspot20"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_hotspot20(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
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

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_identity_psks(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """List all Identity PSKs in a wireless network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psks

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "get_network_wireless_ssid_identity_psks",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks"

        return self._session.get(metadata, resource)

    def create_network_wireless_ssid_identity_psk(
        self, networkId: str, number: str, name: str, groupPolicyId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks"

        body_params = [
            "name",
            "passphrase",
            "groupPolicyId",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_wireless_ssid_identity_psk(
        self, networkId: str, number: str, identityPskId: str
    ) -> dict[str, Any] | None:
        """Return an Identity PSK.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psk

        Args:
            networkId: Network ID.
            number: Number.
            identityPskId: Identity psk ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "get_network_wireless_ssid_identity_psk",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identityPskId = urllib.parse.quote(str(identityPskId), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_identity_psk(
        self, networkId: str, number: str, identityPskId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identityPskId = urllib.parse.quote(str(identityPskId), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}"

        body_params = [
            "name",
            "passphrase",
            "groupPolicyId",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_wireless_ssid_identity_psk(
        self, networkId: str, number: str, identityPskId: str
    ) -> None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identityPskId = urllib.parse.quote(str(identityPskId), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}"

        return self._session.delete(metadata, resource)

    def update_network_wireless_ssid_open_roaming(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/openRoaming"

        body_params = [
            "enabled",
            "tenantId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_schedules(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """List the outage schedule for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-schedules

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "schedules"],
            "operation": "get_network_wireless_ssid_schedules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/schedules"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_schedules(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/schedules"

        body_params = [
            "enabled",
            "ranges",
            "rangesInSeconds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_splash_settings(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """Display the splash page settings for the given SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-splash-settings

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "splash", "settings"],
            "operation": "get_network_wireless_ssid_splash_settings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/splash/settings"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_splash_settings(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
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

        return self._session.put(metadata, resource, payload)

    def update_network_wireless_ssid_traffic_shaping_rules(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules"

        body_params = [
            "trafficShapingEnabled",
            "defaultRulesEnabled",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_traffic_shaping_rules(
        self, networkId: str, number: str
    ) -> dict[str, Any] | None:
        """Display the traffic shaping settings for a SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-traffic-shaping-rules

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "trafficShaping", "rules"],
            "operation": "get_network_wireless_ssid_traffic_shaping_rules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules"

        return self._session.get(metadata, resource)

    def get_network_wireless_ssid_vpn(self, networkId: str, number: str) -> dict[str, Any] | None:
        """List the VPN settings for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-vpn

        Args:
            networkId: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "vpn"],
            "operation": "get_network_wireless_ssid_vpn",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/vpn"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_vpn(
        self, networkId: str, number: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/vpn"

        body_params = [
            "concentrator",
            "splitTunnel",
            "failover",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_usage_history(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return AP usage over time for a device or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-usage-history

        Args:
            networkId: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            autoResolution: Automatically select a data resolution based on the given timespan; this
              overrides the value specified by the 'resolution' parameter. The default
              setting is false.
            clientId: Filter results by network client to return per-device AP usage over time inner
              joined by the queried client's connection history.
            deviceSerial: Filter results by device. Requires :band.
            apTag: Filter results by AP tag; either :clientId or :deviceSerial must be jointly
              specified.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.

        """
        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, (
                f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "usageHistory"],
            "operation": "get_network_wireless_usage_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/usageHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def update_network_wireless_zigbee(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/zigbee"

        body_params = [
            "enabled",
            "iotController",
            "lockManagement",
            "defaults",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_wireless_air_marshal_rules(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns the current Air Marshal rules for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-air-marshal-rules

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: (optional) The set of network IDs to include.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "get_organization_wireless_air_marshal_rules",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/airMarshal/rules"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_air_marshal_settings_by_network(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns the current Air Marshal settings for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-air-marshal-settings-by-network

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: The network IDs to include in the result set.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "settings", "byNetwork"],
            "operation": "get_organization_wireless_air_marshal_settings_by_network",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/airMarshal/settings/byNetwork"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_clients_overview_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List access point client count at the moment in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-overview-by-device

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Optional parameter to filter access points client counts by network ID. This
              filter uses multiple exact matches.
            serials: Optional parameter to filter access points client counts by its serial numbers.
              This filter uses multiple exact matches.
            campusGatewayClusterIds: Optional parameter to filter access points client counts by MCG
              cluster IDs. This filter uses multiple exact matches.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "clients", "overview", "byDevice"],
            "operation": "get_organization_wireless_clients_overview_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/overview/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "campusGatewayClusterIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "campusGatewayClusterIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_channel_utilization_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get average channel utilization for all bands in a network, split by AP.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-device

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Filter results by network.
            serials: Filter results by device.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 90 days. The default is 7 days.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              600, 3600, 7200, 14400, 21600. The default is 3600.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "channelUtilization", "byDevice"],
            "operation": "get_organization_wireless_devices_channel_utilization_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/channelUtilization/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_channel_utilization_by_network(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get average channel utilization across all bands for all networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-network

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Filter results by network.
            serials: Filter results by device.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 90 days. The default is 7 days.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              600, 3600, 7200, 14400, 21600. The default is 3600.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "channelUtilization", "byNetwork"],
            "operation": "get_organization_wireless_devices_channel_utilization_by_network",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/channelUtilization/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_channel_utilization_history_by_device_by_interval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get a time-series of average channel utilization for all bands, segmented by device.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-history-by-device-by-interval

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Filter results by network.
            serials: Filter results by device.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              600, 3600, 7200, 14400, 21600. The default is 3600.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wireless",
                "monitor",
                "devices",
                "channelUtilization",
                "history",
                "byDevice",
                "byInterval",
            ],
            "operation": "get_organization_wireless_devices_channel_utilization_history_by_device_by_interval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/channelUtilization/history/byDevice/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_channel_utilization_history_by_network_by_interval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get a time-series of average channel utilization for all bands.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-history-by-network-by-interval

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Filter results by network.
            serials: Filter results by device.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              600, 3600, 7200, 14400, 21600. The default is 3600.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wireless",
                "monitor",
                "devices",
                "channelUtilization",
                "history",
                "byNetwork",
                "byInterval",
            ],
            "operation": "get_organization_wireless_devices_channel_utilization_history_by_network_by_interval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/channelUtilization/history/byNetwork/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_ethernet_statuses(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the most recent Ethernet link speed, duplex, aggregation and power mode and status information for wireless devices.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-ethernet-statuses

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: A list of Meraki network IDs to filter results to contain only specified
              networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "ethernet", "statuses"],
            "operation": "get_organization_wireless_devices_ethernet_statuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/ethernet/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_packet_loss_by_client(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get average packet loss for the given timespan for all clients in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-client

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Filter results by network.
            ssids: Filter results by SSID number.
            bands: Filter results by band. Valid bands are: 2.4, 5, and 6.
            macs: Filter results by client mac address(es).
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 5 minutes and be less than or
              equal to 90 days. The default is 7 days.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byClient"],
            "operation": "get_organization_wireless_devices_packet_loss_by_client",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/packetLoss/byClient"

        query_params = [
            "networkIds",
            "ssids",
            "bands",
            "macs",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "ssids",
            "bands",
            "macs",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_packet_loss_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get average packet loss for the given timespan for all devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-device

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Filter results by network.
            serials: Filter results by device.
            ssids: Filter results by SSID number.
            bands: Filter results by band. Valid bands are: 2.4, 5, and 6.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 5 minutes and be less than or
              equal to 90 days. The default is 7 days.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byDevice"],
            "operation": "get_organization_wireless_devices_packet_loss_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/packetLoss/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_packet_loss_by_network(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get average packet loss for the given timespan for all networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-network

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Filter results by network.
            serials: Filter results by device.
            ssids: Filter results by SSID number.
            bands: Filter results by band. Valid bands are: 2.4, 5, and 6.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 5 minutes and be less than or
              equal to 90 days. The default is 7 days.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byNetwork"],
            "operation": "get_organization_wireless_devices_packet_loss_by_network",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/packetLoss/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_power_mode_history(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return a record of power mode changes for wireless devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-power-mode-history

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 1 day
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 1 day after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 1 day. The default is 1 day.
            perPage: The number of entries per page returned. Acceptable range is 3 - 20. Default is
              10.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter the result set by the included set of network
              IDs.
            serials: Optional parameter to filter device availabilities history by device serial
              numbers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "power", "mode", "history"],
            "operation": "get_organization_wireless_devices_power_mode_history",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/power/mode/history"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_radsec_certificates_authorities(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Query for details on the organization's RADSEC device Certificate Authority certificates (CAs).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities

        Args:
            organizationId: Organization ID.
            certificateAuthorityIds: Optional parameter to filter CAs by one or more CA IDs. All
              returned CAs will have an ID that is an exact match.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "get_organization_wireless_devices_radsec_certificates_authorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities"
        )

        query_params = [
            "certificateAuthorityIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "certificateAuthorityIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def update_organization_wireless_devices_radsec_certificates_authorities(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update an organization's RADSEC device Certificate Authority (CA) state.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-devices-radsec-certificates-authorities

        Args:
            organizationId: Organization ID.
            status: The "status" to update the Certificate Authority to. Only valid option is
              "trusted".
            certificateAuthorityId: The ID of the Certificate Authority to update.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "update_organization_wireless_devices_radsec_certificates_authorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities"
        )

        body_params = [
            "status",
            "certificateAuthorityId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def create_organization_wireless_devices_radsec_certificates_authority(
        self, organizationId: str
    ) -> dict[str, Any] | None:
        """Create an organization's RADSEC device Certificate Authority (CA).

        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-devices-radsec-certificates-authority

        Args:
            organizationId: Organization ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "create_organization_wireless_devices_radsec_certificates_authority",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities"
        )

        return self._session.post(metadata, resource)

    def get_organization_wireless_devices_radsec_certificates_authorities_crls(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Query for certificate revocation list (CRL) for the organization's RADSEC device Certificate Authorities (CAs).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities-crls

        Args:
            organizationId: Organization ID.
            certificateAuthorityIds: Optional parameter to filter CAs by one or more CA IDs. All
              returned CAs will have an ID that is an exact match.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wireless",
                "configure",
                "devices",
                "radsec",
                "certificates",
                "authorities",
                "crls",
            ],
            "operation": "get_organization_wireless_devices_radsec_certificates_authorities_crls",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities/crls"
        )

        query_params = [
            "certificateAuthorityIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "certificateAuthorityIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_organization_wireless_devices_radsec_certificates_authorities_crls_deltas(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Query for all delta certificate revocation list (CRL) for the organization's RADSEC device Certificate Authority (CA) with the given id.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities-crls-deltas

        Args:
            organizationId: Organization ID.
            certificateAuthorityIds: Parameter to filter CAs by one or more CA IDs. All returned CAs
              will have an ID that is an exact match.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wireless",
                "configure",
                "devices",
                "radsec",
                "certificates",
                "authorities",
                "crls",
                "deltas",
            ],
            "operation": "get_organization_wireless_devices_radsec_certificates_authorities_crls_deltas",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities/crls/deltas"

        query_params = [
            "certificateAuthorityIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "certificateAuthorityIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_organization_wireless_devices_system_cpu_load_history(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the CPU Load history for a list of wireless devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-system-cpu-load-history

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 1 day
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 1 day after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 1 day. The default is 1 day.
            perPage: The number of entries per page returned. Acceptable range is 3 - 20. Default is
              10.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter the result set by the included set of network
              IDs.
            serials: Optional parameter to filter device availabilities history by device serial
              numbers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "system", "cpu", "load", "history"],
            "operation": "get_organization_wireless_devices_system_cpu_load_history",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/system/cpu/load/history"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_wireless_controllers_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List of Catalyst access points information.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-wireless-controllers-by-device

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Optional parameter to filter access points by network ID. This filter uses
              multiple exact matches.
            serials: Optional parameter to filter access points by its cloud ID. This filter uses
              multiple exact matches.
            controllerSerials: Optional parameter to filter access points by its wireless LAN
              controller cloud ID. This filter uses multiple exact matches.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "wirelessControllers", "byDevice"],
            "operation": "get_organization_wireless_devices_wireless_controllers_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/wirelessControllers/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "controllerSerials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "controllerSerials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_location_scanning_by_network(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return scanning API settings.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-location-scanning-by-network

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 250. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter scanning settings by network ID.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "byNetwork"],
            "operation": "get_organization_wireless_location_scanning_by_network",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/scanning/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_location_scanning_receivers(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return scanning API receivers.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-location-scanning-receivers

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 250. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter scanning API receivers by network ID.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "get_organization_wireless_location_scanning_receivers",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/scanning/receivers"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_wireless_location_scanning_receiver(
        self,
        organizationId: str,
        network: dict,
        url: str,
        version: str,
        radio: dict,
        sharedSecret: str,
    ) -> dict[str, Any] | None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/scanning/receivers"

        body_params = [
            "network",
            "url",
            "version",
            "radio",
            "sharedSecret",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_organization_wireless_location_scanning_receiver(
        self, organizationId: str, receiverId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        receiverId = urllib.parse.quote(str(receiverId), safe="")
        resource = (
            f"/organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId}"
        )

        body_params = [
            "url",
            "version",
            "radio",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_wireless_location_scanning_receiver(
        self, organizationId: str, receiverId: str
    ) -> None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        receiverId = urllib.parse.quote(str(receiverId), safe="")
        resource = (
            f"/organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId}"
        )

        return self._session.delete(metadata, resource)

    def get_organization_wireless_mqtt_settings(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return MQTT Settings for networks.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-mqtt-settings

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 250. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter mqtt settings by network ID.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "mqtt", "settings"],
            "operation": "get_organization_wireless_mqtt_settings",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/mqtt/settings"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def update_organization_wireless_mqtt_settings(
        self, organizationId: str, network: dict, mqtt: dict, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/mqtt/settings"

        body_params = [
            "network",
            "mqtt",
            "ble",
            "wifi",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def recalculate_organization_wireless_radio_auto_rf_channels(
        self, organizationId: str, networkIds: list
    ) -> dict[str, Any] | None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/autoRf/channels/recalculate"

        body_params = [
            "networkIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_wireless_rf_profiles_assignments_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the RF profiles of an organization by device.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-rf-profiles-assignments-by-device

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter devices by network.
            productTypes: Optional parameter to filter devices by product type. Valid types are
              wireless, appliance, switch, systemsManager, camera, cellularGateway,
              sensor, wirelessController, campusGateway, and secureConnect.
            name: Optional parameter to filter RF profiles by device name. All returned devices will
              have a name that contains the search term or is an exact match.
            mac: Optional parameter to filter RF profiles by device MAC address. All returned
              devices will have a MAC address that contains the search term or is an
              exact match.
            serial: Optional parameter to filter RF profiles by device serial number. All returned
              devices will have a serial number that contains the search term or is an
              exact match.
            model: Optional parameter to filter RF profiles by device model. All returned devices
              will have a model that contains the search term or is an exact match.
            macs: Optional parameter to filter RF profiles by one or more device MAC addresses. All
              returned devices will have a MAC address that is an exact match.
            serials: Optional parameter to filter RF profiles by one or more device serial numbers.
              All returned devices will have a serial number that is an exact match.
            models: Optional parameter to filter RF profiles by one or more device models. All
              returned devices will have a model that is an exact match.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles", "assignments", "byDevice"],
            "operation": "get_organization_wireless_rf_profiles_assignments_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/rfProfiles/assignments/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "name",
            "mac",
            "serial",
            "model",
            "macs",
            "serials",
            "models",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "macs",
            "serials",
            "models",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_ssids_firewall_isolation_allowlist_entries(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the L2 isolation allow list MAC entry in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-firewall-isolation-allowlist-entries

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: networkIds array to filter out results.
            ssids: ssids number array to filter out results.

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
            "operation": "get_organization_wireless_ssids_firewall_isolation_allowlist_entries",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries"
        )

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "ssids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "ssids",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self, organizationId: str, client: dict, ssid: dict, network: dict, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
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

        return self._session.post(metadata, resource, payload)

    def delete_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self, organizationId: str, entryId: str
    ) -> None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        entryId = urllib.parse.quote(str(entryId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries/{entryId}"

        return self._session.delete(metadata, resource)

    def update_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self, organizationId: str, entryId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        entryId = urllib.parse.quote(str(entryId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries/{entryId}"

        body_params = [
            "description",
            "client",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_wireless_ssids_open_roaming_by_network(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns an array of objects, each containing SSID OpenRoaming configs for the corresponding network.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-open-roaming-by-network

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Optional parameter to filter OpenRoaming configuration by Network Id.
            includeDisabledSsids: Optional parameter to include OpenRoaming configuration for
              disabled ssids.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "openRoaming", "byNetwork"],
            "operation": "get_organization_wireless_ssids_open_roaming_by_network",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/openRoaming/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "includeDisabledSsids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_ssids_statuses_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List status information of all BSSIDs in your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-statuses-by-device

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Optional parameter to filter the result set by the included set of network
              IDs.
            serials: A list of serial numbers. The returned devices will be filtered to only include
              these serials.
            bssids: A list of BSSIDs. The returned devices will be filtered to only include these
              BSSIDs.
            hideDisabled: If true, the returned devices will not include disabled SSIDs. (default:
              true).
            perPage: The number of entries per page returned. Acceptable range is 3 - 500. Default
              is 100.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "ssids", "statuses", "byDevice"],
            "operation": "get_organization_wireless_ssids_statuses_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/statuses/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "bssids",
            "hideDisabled",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "bssids",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_zigbee_by_network(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return list of Zigbee configs.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-by-network

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Filter by specified Network IDs.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "byNetwork"],
            "operation": "get_organization_wireless_zigbee_by_network",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_zigbee_devices(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the Zigbee wireless devices for an organization or the supplied network(s).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-devices

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 10.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            networkIds: Parameter of networks you want the zigbee devices for. E.g.:
              networkIds[]=N_12345678&networkIds[]=N_3456.
            isEnrolled: Filter devices based on if they are enrolled or not.
            search: Filter devices by their name, tag or serial.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "devices"],
            "operation": "get_organization_wireless_zigbee_devices",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/devices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "isEnrolled",
            "search",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def update_organization_wireless_zigbee_device(
        self, organizationId: str, id: str, enrolled: bool, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/devices/{id}"

        body_params = [
            "enrolled",
            "channel",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def create_organization_wireless_zigbee_disenrollment(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Enqueue a job to start disenrolling door locks on zigbee configured wireless devices.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-zigbee-disenrollment

        Args:
            organizationId: Organization ID.
            doorLockIds: A list of Meraki door lock ids to disenroll from the device.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "disenrollments"],
            "operation": "create_organization_wireless_zigbee_disenrollment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/disenrollments"

        body_params = [
            "doorLockIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_wireless_zigbee_disenrollment(
        self, organizationId: str, disenrollmentId: str
    ) -> dict[str, Any] | None:
        """Return a disenrollment.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-disenrollment

        Args:
            organizationId: Organization ID.
            disenrollmentId: Disenrollment ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "disenrollments"],
            "operation": "get_organization_wireless_zigbee_disenrollment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        disenrollmentId = urllib.parse.quote(str(disenrollmentId), safe="")
        resource = (
            f"/organizations/{organizationId}/wireless/zigbee/disenrollments/{disenrollmentId}"
        )

        return self._session.get(metadata, resource)

    def get_organization_wireless_zigbee_door_locks(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the list of door locks for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-door-locks

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Filter by specified Network IDs.
            serial: Filter by device serial.
            perPage: The number of entries per page returned. Acceptable range is 3 - 500. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "doorLocks"],
            "operation": "get_organization_wireless_zigbee_door_locks",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/doorLocks"

        query_params = [
            "networkIds",
            "serial",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def update_organization_wireless_zigbee_door_lock(
        self, organizationId: str, doorLockId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        doorLockId = urllib.parse.quote(str(doorLockId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/doorLocks/{doorLockId}"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
