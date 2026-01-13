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
        self, serial: str, *, addresses: list | None = None
    ) -> dict[str, Any] | None:
        """Update alternate management interface IPv6 address.

        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-alternate-management-interface-ipv-6

        Args:
            serial: Serial.
            addresses: configured alternate management interface addresses.

        """
        metadata = {
            "tags": ["wireless", "configure", "alternateManagementInterface", "ipv6"],
            "operation": "update_device_wireless_alternate_management_interface_ipv6",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/alternateManagementInterface/ipv6"

        payload = {}
        if addresses is not None:
            payload["addresses"] = addresses

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
        self,
        serial: str,
        *,
        uuid: str | None = None,
        major: int | None = None,
        minor: int | None = None,
    ) -> dict[str, Any] | None:
        """Update the bluetooth settings for a wireless device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-bluetooth-settings

        Args:
            serial: Serial.
            uuid: Desired UUID of the beacon. If the value is set to null it will reset to
              Dashboard's automatically generated value.
            major: Desired major value of the beacon. If the value is set to null it will reset to
              Dashboard's automatically generated value.
            minor: Desired minor value of the beacon. If the value is set to null it will reset to
              Dashboard's automatically generated value.

        """
        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "update_device_wireless_bluetooth_settings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/bluetooth/settings"

        payload = {}
        if uuid is not None:
            payload["uuid"] = uuid
        if major is not None:
            payload["major"] = major
        if minor is not None:
            payload["minor"] = minor

        return self._session.put(metadata, resource, payload)

    def get_device_wireless_connection_stats(
        self,
        serial: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
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
            ap_tag: Filter results by AP Tag.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "connectionStats"],
            "operation": "get_device_wireless_connection_stats",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/connectionStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag

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
        self, serial: str, *, channel: str | None = None, enabled: bool | None = None
    ) -> dict[str, Any] | None:
        """Update the ESL settings of a device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-electronic-shelf-label

        Args:
            serial: Serial.
            channel: Desired ESL channel for the device, or 'Auto' (case insensitive) to use the
              recommended channel.
            enabled: Turn ESL features on and off for this device.

        """
        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "update_device_wireless_electronic_shelf_label",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/electronicShelfLabel"

        payload = {}
        if channel is not None:
            payload["channel"] = channel
        if enabled is not None:
            payload["enabled"] = enabled

        return self._session.put(metadata, resource, payload)

    def get_device_wireless_latency_stats(
        self,
        serial: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
        vlan: int | None = None,
        fields: str | None = None,
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
            ap_tag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "latencyStats"],
            "operation": "get_device_wireless_latency_stats",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/latencyStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if vlan is not None:
            params["vlan"] = vlan
        if fields is not None:
            params["fields"] = fields

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
        self,
        serial: str,
        *,
        rf_profile_id: str | None = None,
        two_four_ghz_settings: dict | None = None,
        five_ghz_settings: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the radio settings overrides of a device, which take precedence over RF profiles.

        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-settings

        Args:
            serial: Serial.
            rf_profile_id: The ID of an RF profile to assign to the device. If the value of this
              parameter is null, the appropriate basic RF profile (indoor or outdoor)
              will be assigned to the device. Assigning an RF profile will clear ALL
              manually configured overrides on the device (channel width, channel,
              power).
            two_four_ghz_settings: Manual radio settings for 2.4 GHz.
            five_ghz_settings: Manual radio settings for 5 GHz.

        """
        metadata = {
            "tags": ["wireless", "configure", "radio", "settings"],
            "operation": "update_device_wireless_radio_settings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/settings"

        payload = {}
        if rf_profile_id is not None:
            payload["rfProfileId"] = rf_profile_id
        if two_four_ghz_settings is not None:
            payload["twoFourGhzSettings"] = two_four_ghz_settings
        if five_ghz_settings is not None:
            payload["fiveGhzSettings"] = five_ghz_settings

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
        self, serial: str, enrollment_id: str
    ) -> dict[str, Any] | None:
        """Return an enrollment.

        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-zigbee-enrollment

        Args:
            serial: Serial.
            enrollment_id: Enrollment ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "enrollments"],
            "operation": "get_device_wireless_zigbee_enrollment",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        enrollment_id = urllib.parse.quote(str(enrollment_id), safe="")
        resource = f"/devices/{serial}/wireless/zigbee/enrollments/{enrollment_id}"

        return self._session.get(metadata, resource)

    def get_network_wireless_air_marshal(
        self, network_id: str, *, t0: str | None = None, timespan: float | None = None
    ) -> dict[str, Any] | None:
        """List Air Marshal scan results from a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-air-marshal

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 7 days.

        """
        metadata = {
            "tags": ["wireless", "monitor", "airMarshal"],
            "operation": "get_network_wireless_air_marshal",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/airMarshal"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(metadata, resource, params)

    def create_network_wireless_air_marshal_rule(
        self, network_id: str, type_: str, match: dict
    ) -> dict[str, Any] | None:
        """Creates a new rule.

        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-air-marshal-rule

        Args:
            network_id: Network ID.
            type_: Indicates if this rule will allow, block, or alert.
            match: Object describing the rule specification.

        """
        if type_ is not None:
            options = ["alert", "allow", "block"]
            assert type_ in options, (
                f'"type_" cannot be "{type_}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "create_network_wireless_air_marshal_rule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/airMarshal/rules"

        payload = {}
        if type_ is not None:
            payload["type"] = type_
        if match is not None:
            payload["match"] = match

        return self._session.post(metadata, resource, payload)

    def update_network_wireless_air_marshal_rule(
        self, network_id: str, rule_id: str, *, type_: str | None = None, match: dict | None = None
    ) -> dict[str, Any] | None:
        """Update a rule.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-air-marshal-rule

        Args:
            network_id: Network ID.
            rule_id: Rule ID.
            type_: Indicates if this rule will allow, block, or alert.
            match: Object describing the rule specification.

        """
        if type_ is not None:
            options = ["alert", "allow", "block"]
            assert type_ in options, (
                f'"type_" cannot be "{type_}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "update_network_wireless_air_marshal_rule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        rule_id = urllib.parse.quote(str(rule_id), safe="")
        resource = f"/networks/{network_id}/wireless/airMarshal/rules/{rule_id}"

        payload = {}
        if type_ is not None:
            payload["type"] = type_
        if match is not None:
            payload["match"] = match

        return self._session.put(metadata, resource, payload)

    def delete_network_wireless_air_marshal_rule(self, network_id: str, rule_id: str) -> None:
        """Delete an Air Marshal rule.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-air-marshal-rule

        Args:
            network_id: Network ID.
            rule_id: Rule ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "delete_network_wireless_air_marshal_rule",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        rule_id = urllib.parse.quote(str(rule_id), safe="")
        resource = f"/networks/{network_id}/wireless/airMarshal/rules/{rule_id}"

        return self._session.delete(metadata, resource)

    def update_network_wireless_air_marshal_settings(
        self, network_id: str, default_policy: str
    ) -> dict[str, Any] | None:
        """Updates Air Marshal settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-air-marshal-settings

        Args:
            network_id: Network ID.
            default_policy: Allows clients to access rogue networks. Blocked by default.

        """
        if default_policy is not None:
            options = ["allow", "block"]
            assert default_policy in options, (
                f'"default_policy" cannot be "{default_policy}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "settings"],
            "operation": "update_network_wireless_air_marshal_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/airMarshal/settings"

        payload = {}
        if default_policy is not None:
            payload["defaultPolicy"] = default_policy

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_alternate_management_interface(
        self, network_id: str
    ) -> dict[str, Any] | None:
        """Return alternate management interface and devices with IP assigned.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-alternate-management-interface

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "alternateManagementInterface"],
            "operation": "get_network_wireless_alternate_management_interface",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/alternateManagementInterface"

        return self._session.get(metadata, resource)

    def update_network_wireless_alternate_management_interface(
        self,
        network_id: str,
        *,
        enabled: bool | None = None,
        vlan_id: int | None = None,
        protocols: list | None = None,
        access_points: list | None = None,
    ) -> dict[str, Any] | None:
        """Update alternate management interface and device static IP.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-alternate-management-interface

        Args:
            network_id: Network ID.
            enabled: Boolean value to enable or disable alternate management interface.
            vlan_id: Alternate management interface VLAN, must be between 1 and 4094.
            protocols: Can be one or more of the following values: 'radius', 'snmp', 'syslog' or
              'ldap'.
            access_points: Array of access point serial number and IP assignment. Note: accessPoints
              IP assignment is not applicable for template networks, in other words, do
              not put 'accessPoints' in the body when updating template networks. Also,
              an empty 'accessPoints' array will remove all previous static IP
              assignments.

        """
        metadata = {
            "tags": ["wireless", "configure", "alternateManagementInterface"],
            "operation": "update_network_wireless_alternate_management_interface",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/alternateManagementInterface"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if vlan_id is not None:
            payload["vlanId"] = vlan_id
        if protocols is not None:
            payload["protocols"] = protocols
        if access_points is not None:
            payload["accessPoints"] = access_points

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_billing(self, network_id: str) -> dict[str, Any] | None:
        """Return the billing settings of this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-billing

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "billing"],
            "operation": "get_network_wireless_billing",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/billing"

        return self._session.get(metadata, resource)

    def update_network_wireless_billing(
        self, network_id: str, *, currency: str | None = None, plans: list | None = None
    ) -> dict[str, Any] | None:
        """Update the billing settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-billing

        Args:
            network_id: Network ID.
            currency: The currency code of this node group's billing plans.
            plans: Array of billing plans in the node group. (Can configure a maximum of 5).

        """
        metadata = {
            "tags": ["wireless", "configure", "billing"],
            "operation": "update_network_wireless_billing",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/billing"

        payload = {}
        if currency is not None:
            payload["currency"] = currency
        if plans is not None:
            payload["plans"] = plans

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_bluetooth_settings(self, network_id: str) -> dict[str, Any] | None:
        """Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-bluetooth-settings

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "get_network_wireless_bluetooth_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/bluetooth/settings"

        return self._session.get(metadata, resource)

    def update_network_wireless_bluetooth_settings(
        self,
        network_id: str,
        *,
        scanning_enabled: bool | None = None,
        advertising_enabled: bool | None = None,
        uuid: str | None = None,
        major_minor_assignment_mode: str | None = None,
        major: int | None = None,
        minor: int | None = None,
    ) -> dict[str, Any] | None:
        """Update the Bluetooth settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-bluetooth-settings

        Args:
            network_id: Network ID.
            scanning_enabled: Whether APs will scan for Bluetooth enabled clients.
            advertising_enabled: Whether APs will advertise beacons.
            uuid: The UUID to be used in the beacon identifier.
            major_minor_assignment_mode: The way major and minor number should be assigned to nodes
              in the network. ('Unique', 'Non-unique').
            major: The major number to be used in the beacon identifier. Only valid in 'Non-unique'
              mode.
            minor: The minor number to be used in the beacon identifier. Only valid in 'Non-unique'
              mode.

        """
        if major_minor_assignment_mode is not None:
            options = ["Non-unique", "Unique"]
            assert major_minor_assignment_mode in options, (
                f'"major_minor_assignment_mode" cannot be "{major_minor_assignment_mode}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "update_network_wireless_bluetooth_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/bluetooth/settings"

        payload = {}
        if scanning_enabled is not None:
            payload["scanningEnabled"] = scanning_enabled
        if advertising_enabled is not None:
            payload["advertisingEnabled"] = advertising_enabled
        if uuid is not None:
            payload["uuid"] = uuid
        if major_minor_assignment_mode is not None:
            payload["majorMinorAssignmentMode"] = major_minor_assignment_mode
        if major is not None:
            payload["major"] = major
        if minor is not None:
            payload["minor"] = minor

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_channel_utilization_history(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
        auto_resolution: bool | None = None,
        client_id: str | None = None,
        device_serial: str | None = None,
        ap_tag: str | None = None,
        band: str | None = None,
    ) -> dict[str, Any] | None:
        """Return AP channel utilization over time for a device or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-channel-utilization-history

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              600, 1200, 3600, 14400, 86400. The default is 86400.
            auto_resolution: Automatically select a data resolution based on the given timespan;
              this overrides the value specified by the 'resolution' parameter. The
              default setting is false.
            client_id: Filter results by network client to return per-device, per-band AP channel
              utilization metrics inner joined by the queried client's connection
              history.
            device_serial: Filter results by device to return AP channel utilization metrics for the
              queried device; either :band or :clientId must be jointly specified.
            ap_tag: Filter results by AP tag to return AP channel utilization metrics for devices
              labeled with the given tag; either :clientId or :deviceSerial must be
              jointly specified.
            band: Filter results by band (either '2.4', '5' or '6').

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "channelUtilizationHistory"],
            "operation": "get_network_wireless_channel_utilization_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/channelUtilizationHistory"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution
        if auto_resolution is not None:
            params["autoResolution"] = auto_resolution
        if client_id is not None:
            params["clientId"] = client_id
        if device_serial is not None:
            params["deviceSerial"] = device_serial
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if band is not None:
            params["band"] = band

        return self._session.get(metadata, resource, params)

    def get_network_wireless_client_count_history(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
        auto_resolution: bool | None = None,
        client_id: str | None = None,
        device_serial: str | None = None,
        ap_tag: str | None = None,
        band: str | None = None,
        ssid: int | None = None,
    ) -> dict[str, Any] | None:
        """Return wireless client counts over time for a network, device, or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-count-history

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            auto_resolution: Automatically select a data resolution based on the given timespan;
              this overrides the value specified by the 'resolution' parameter. The
              default setting is false.
            client_id: Filter results by network client to return per-device client counts over time
              inner joined by the queried client's connection history.
            device_serial: Filter results by device.
            ap_tag: Filter results by AP tag.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "clientCountHistory"],
            "operation": "get_network_wireless_client_count_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/clientCountHistory"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution
        if auto_resolution is not None:
            params["autoResolution"] = auto_resolution
        if client_id is not None:
            params["clientId"] = client_id
        if device_serial is not None:
            params["deviceSerial"] = device_serial
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid

        return self._session.get(metadata, resource, params)

    def get_network_wireless_clients_connection_stats(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for this network, grouped by clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-connection-stats

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectionStats"],
            "operation": "get_network_wireless_clients_connection_stats",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/clients/connectionStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag

        return self._session.get(metadata, resource, params)

    def get_network_wireless_clients_latency_stats(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
        vlan: int | None = None,
        fields: str | None = None,
    ) -> dict[str, Any] | None:
        """Aggregated latency info for this network, grouped by clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-latency-stats

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "clients", "latencyStats"],
            "operation": "get_network_wireless_clients_latency_stats",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/clients/latencyStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if vlan is not None:
            params["vlan"] = vlan
        if fields is not None:
            params["fields"] = fields

        return self._session.get(metadata, resource, params)

    def get_network_wireless_client_connection_stats(
        self,
        network_id: str,
        client_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for a given client on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connection-stats

        Args:
            network_id: Network ID.
            client_id: Client ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectionStats"],
            "operation": "get_network_wireless_client_connection_stats",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/wireless/clients/{client_id}/connectionStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag

        return self._session.get(metadata, resource, params)

    def get_network_wireless_client_connectivity_events(
        self,
        network_id: str,
        client_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        types: list | None = None,
        band: str | None = None,
        ssid_number: int | None = None,
        included_severities: list | None = None,
        device_serial: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the wireless connectivity events for a client within a network in the timespan.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connectivity-events

        Args:
            network_id: Network ID.
            client_id: Client ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sort_order: Sorted order of entries. Order options are 'ascending' and 'descending'.
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
            ssid_number: Filter results by SSID. If not specified, events for all SSIDs will be
              returned.
            included_severities: A list of severities to include. If not specified, events of all
              severities will be returned. Valid severities are 'good', 'info', 'warn'
              and/or 'bad'.
            device_serial: Filter results by an AP's serial number.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'
        if ssid_number is not None:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert ssid_number in options, (
                f'"ssid_number" cannot be "{ssid_number}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectivityEvents"],
            "operation": "get_network_wireless_client_connectivity_events",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/wireless/clients/{client_id}/connectivityEvents"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if sort_order is not None:
            params["sortOrder"] = sort_order
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if types is not None:
            params["types[]"] = types
        if band is not None:
            params["band"] = band
        if ssid_number is not None:
            params["ssidNumber"] = ssid_number
        if included_severities is not None:
            params["includedSeverities[]"] = included_severities
        if device_serial is not None:
            params["deviceSerial"] = device_serial

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_wireless_client_latency_history(
        self,
        network_id: str,
        client_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
    ) -> dict[str, Any] | None:
        """Return the latency history for a client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-history

        Args:
            network_id: Network ID.
            client_id: Client ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 791 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 791 days. The default is 1 day.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              86400. The default is 86400.

        """
        metadata = {
            "tags": ["wireless", "monitor", "clients", "latencyHistory"],
            "operation": "get_network_wireless_client_latency_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/wireless/clients/{client_id}/latencyHistory"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution

        return self._session.get(metadata, resource, params)

    def get_network_wireless_client_latency_stats(
        self,
        network_id: str,
        client_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
        vlan: int | None = None,
        fields: str | None = None,
    ) -> dict[str, Any] | None:
        """Aggregated latency info for a given client on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-stats

        Args:
            network_id: Network ID.
            client_id: Client ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "clients", "latencyStats"],
            "operation": "get_network_wireless_client_latency_stats",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/wireless/clients/{client_id}/latencyStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if vlan is not None:
            params["vlan"] = vlan
        if fields is not None:
            params["fields"] = fields

        return self._session.get(metadata, resource, params)

    def get_network_wireless_connection_stats(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-connection-stats

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "connectionStats"],
            "operation": "get_network_wireless_connection_stats",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/connectionStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag

        return self._session.get(metadata, resource, params)

    def get_network_wireless_data_rate_history(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
        auto_resolution: bool | None = None,
        client_id: str | None = None,
        device_serial: str | None = None,
        ap_tag: str | None = None,
        band: str | None = None,
        ssid: int | None = None,
    ) -> dict[str, Any] | None:
        """Return PHY data rates over time for a network, device, or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-data-rate-history

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            auto_resolution: Automatically select a data resolution based on the given timespan;
              this overrides the value specified by the 'resolution' parameter. The
              default setting is false.
            client_id: Filter results by network client.
            device_serial: Filter results by device.
            ap_tag: Filter results by AP tag.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "dataRateHistory"],
            "operation": "get_network_wireless_data_rate_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/dataRateHistory"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution
        if auto_resolution is not None:
            params["autoResolution"] = auto_resolution
        if client_id is not None:
            params["clientId"] = client_id
        if device_serial is not None:
            params["deviceSerial"] = device_serial
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid

        return self._session.get(metadata, resource, params)

    def get_network_wireless_devices_connection_stats(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
    ) -> dict[str, Any] | None:
        """Aggregated connectivity info for this network, grouped by node.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-connection-stats

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "devices", "connectionStats"],
            "operation": "get_network_wireless_devices_connection_stats",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/devices/connectionStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag

        return self._session.get(metadata, resource, params)

    def get_network_wireless_devices_latency_stats(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
        vlan: int | None = None,
        fields: str | None = None,
    ) -> dict[str, Any] | None:
        """Aggregated latency info for this network, grouped by node.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-latency-stats

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "devices", "latencyStats"],
            "operation": "get_network_wireless_devices_latency_stats",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/devices/latencyStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if vlan is not None:
            params["vlan"] = vlan
        if fields is not None:
            params["fields"] = fields

        return self._session.get(metadata, resource, params)

    def get_network_wireless_electronic_shelf_label(self, network_id: str) -> dict[str, Any] | None:
        """Return the ESL settings of a wireless network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-electronic-shelf-label

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "get_network_wireless_electronic_shelf_label",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/electronicShelfLabel"

        return self._session.get(metadata, resource)

    def update_network_wireless_electronic_shelf_label(
        self,
        network_id: str,
        *,
        hostname: str | None = None,
        enabled: bool | None = None,
        mode: str | None = None,
    ) -> dict[str, Any] | None:
        """Update the ESL settings of a wireless network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-electronic-shelf-label

        Args:
            network_id: Network ID.
            hostname: Desired ESL hostname of the network.
            enabled: Turn ESL features on and off for this network.
            mode: Electronic shelf label mode of the network. Valid options are 'Bluetooth', 'high
              frequency'.

        """
        if mode is not None:
            options = ["Bluetooth", "high frequency"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "update_network_wireless_electronic_shelf_label",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/electronicShelfLabel"

        payload = {}
        if hostname is not None:
            payload["hostname"] = hostname
        if enabled is not None:
            payload["enabled"] = enabled
        if mode is not None:
            payload["mode"] = mode

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_electronic_shelf_label_configured_devices(
        self, network_id: str
    ) -> dict[str, Any] | None:
        """Get a list of all ESL eligible devices of a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-electronic-shelf-label-configured-devices

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel", "configuredDevices"],
            "operation": "get_network_wireless_electronic_shelf_label_configured_devices",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/electronicShelfLabel/configuredDevices"

        return self._session.get(metadata, resource)

    def get_network_wireless_ethernet_ports_profiles(
        self, network_id: str
    ) -> dict[str, Any] | None:
        """List the AP port profiles for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profiles

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "get_network_wireless_ethernet_ports_profiles",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/ethernet/ports/profiles"

        return self._session.get(metadata, resource)

    def create_network_wireless_ethernet_ports_profile(
        self, network_id: str, name: str, ports: list, *, usb_ports: list | None = None
    ) -> dict[str, Any] | None:
        """Create an AP port profile.

        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ethernet-ports-profile

        Args:
            network_id: Network ID.
            name: AP port profile name.
            ports: AP ports configuration.
            usb_ports: AP usb ports configuration.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "create_network_wireless_ethernet_ports_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/ethernet/ports/profiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if ports is not None:
            payload["ports"] = ports
        if usb_ports is not None:
            payload["usbPorts"] = usb_ports

        return self._session.post(metadata, resource, payload)

    def assign_network_wireless_ethernet_ports_profiles(
        self, network_id: str, serials: list, profile_id: str
    ) -> dict[str, Any] | None:
        """Assign AP port profile to list of APs.

        https://developer.cisco.com/meraki/api-v1/#!assign-network-wireless-ethernet-ports-profiles

        Args:
            network_id: Network ID.
            serials: List of AP serials.
            profile_id: AP profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "assign_network_wireless_ethernet_ports_profiles",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/ethernet/ports/profiles/assign"

        payload = {}
        if serials is not None:
            payload["serials"] = serials
        if profile_id is not None:
            payload["profileId"] = profile_id

        return self._session.post(metadata, resource, payload)

    def set_network_wireless_ethernet_ports_profiles_default(
        self, network_id: str, profile_id: str
    ) -> dict[str, Any] | None:
        """Set the AP port profile to be default for this network.

        https://developer.cisco.com/meraki/api-v1/#!set-network-wireless-ethernet-ports-profiles-default

        Args:
            network_id: Network ID.
            profile_id: AP profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "set_network_wireless_ethernet_ports_profiles_default",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/ethernet/ports/profiles/setDefault"

        payload = {}
        if profile_id is not None:
            payload["profileId"] = profile_id

        return self._session.post(metadata, resource, payload)

    def get_network_wireless_ethernet_ports_profile(
        self, network_id: str, profile_id: str
    ) -> dict[str, Any] | None:
        """Show the AP port profile by ID for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profile

        Args:
            network_id: Network ID.
            profile_id: Profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "get_network_wireless_ethernet_ports_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        resource = f"/networks/{network_id}/wireless/ethernet/ports/profiles/{profile_id}"

        return self._session.get(metadata, resource)

    def update_network_wireless_ethernet_ports_profile(
        self,
        network_id: str,
        profile_id: str,
        *,
        name: str | None = None,
        ports: list | None = None,
        usb_ports: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the AP port profile by ID for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ethernet-ports-profile

        Args:
            network_id: Network ID.
            profile_id: Profile ID.
            name: AP port profile name.
            ports: AP ports configuration.
            usb_ports: AP usb ports configuration.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "update_network_wireless_ethernet_ports_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        resource = f"/networks/{network_id}/wireless/ethernet/ports/profiles/{profile_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if ports is not None:
            payload["ports"] = ports
        if usb_ports is not None:
            payload["usbPorts"] = usb_ports

        return self._session.put(metadata, resource, payload)

    def delete_network_wireless_ethernet_ports_profile(
        self, network_id: str, profile_id: str
    ) -> None:
        """Delete an AP port profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ethernet-ports-profile

        Args:
            network_id: Network ID.
            profile_id: Profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "delete_network_wireless_ethernet_ports_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        resource = f"/networks/{network_id}/wireless/ethernet/ports/profiles/{profile_id}"

        return self._session.delete(metadata, resource)

    def get_network_wireless_failed_connections(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
        serial: str | None = None,
        client_id: str | None = None,
    ) -> dict[str, Any] | None:
        """List of all failed client connection events on this network in a given time range.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-failed-connections

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.
            serial: Filter by AP.
            client_id: Filter by client MAC.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "failedConnections"],
            "operation": "get_network_wireless_failed_connections",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/failedConnections"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if serial is not None:
            params["serial"] = serial
        if client_id is not None:
            params["clientId"] = client_id

        return self._session.get(metadata, resource, params)

    def get_network_wireless_latency_history(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
        auto_resolution: bool | None = None,
        client_id: str | None = None,
        device_serial: str | None = None,
        ap_tag: str | None = None,
        band: str | None = None,
        ssid: int | None = None,
        access_category: str | None = None,
    ) -> dict[str, Any] | None:
        """Return average wireless latency over time for a network, device, or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-history

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            auto_resolution: Automatically select a data resolution based on the given timespan;
              this overrides the value specified by the 'resolution' parameter. The
              default setting is false.
            client_id: Filter results by network client.
            device_serial: Filter results by device.
            ap_tag: Filter results by AP tag.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.
            access_category: Filter by access category.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'
        if access_category is not None:
            options = ["backgroundTraffic", "bestEffortTraffic", "videoTraffic", "voiceTraffic"]
            assert access_category in options, (
                f'"access_category" cannot be "{access_category}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "monitor", "latencyHistory"],
            "operation": "get_network_wireless_latency_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/latencyHistory"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution
        if auto_resolution is not None:
            params["autoResolution"] = auto_resolution
        if client_id is not None:
            params["clientId"] = client_id
        if device_serial is not None:
            params["deviceSerial"] = device_serial
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if access_category is not None:
            params["accessCategory"] = access_category

        return self._session.get(metadata, resource, params)

    def get_network_wireless_latency_stats(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        band: str | None = None,
        ssid: int | None = None,
        ap_tag: str | None = None,
        vlan: int | None = None,
        fields: str | None = None,
    ) -> dict[str, Any] | None:
        """Aggregated latency info for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-stats

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 180 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days.
            band: Filter results by band (either '2.4', '5' or '6'). Note that data prior to
              February 2020 will not have band information.
            ssid: Filter results by SSID.
            ap_tag: Filter results by AP Tag.
            vlan: Filter results by VLAN.
            fields: Partial selection: If present, this call will return only the selected fields of
              ["rawDistribution", "avg"]. All fields will be returned by default.
              Selected fields must be entered as a comma separated string.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "latencyStats"],
            "operation": "get_network_wireless_latency_stats",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/latencyStats"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if vlan is not None:
            params["vlan"] = vlan
        if fields is not None:
            params["fields"] = fields

        return self._session.get(metadata, resource, params)

    def update_network_wireless_location_scanning(
        self, network_id: str, *, enabled: bool | None = None, api: dict | None = None
    ) -> dict[str, Any] | None:
        """Change scanning API settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-location-scanning

        Args:
            network_id: Network ID.
            enabled: Collect location and scanning analytics.
            api: Enable push API for scanning events, analytics must be enabled.

        """
        metadata = {
            "tags": ["wireless", "configure", "location", "scanning"],
            "operation": "update_network_wireless_location_scanning",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/location/scanning"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if api is not None:
            payload["api"] = api

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_mesh_statuses(
        self,
        network_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List wireless mesh statuses for repeaters.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-mesh-statuses

        Args:
            network_id: Network ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 500. Default
              is 50.
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
            "tags": ["wireless", "monitor", "meshStatuses"],
            "operation": "get_network_wireless_mesh_statuses",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/meshStatuses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_wireless_rf_profiles(
        self, network_id: str, *, include_template_profiles: bool | None = None
    ) -> dict[str, Any] | None:
        """List RF profiles for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles

        Args:
            network_id: Network ID.
            include_template_profiles: If the network is bound to a template, this parameter
              controls whether or not the non-basic RF profiles defined on the template
              should be included in the response alongside the non-basic profiles
              defined on the bound network. Defaults to false.

        """
        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "get_network_wireless_rf_profiles",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/rfProfiles"

        params = {}
        if include_template_profiles is not None:
            params["includeTemplateProfiles"] = include_template_profiles

        return self._session.get(metadata, resource, params)

    def create_network_wireless_rf_profile(
        self,
        network_id: str,
        name: str,
        band_selection_type: str,
        *,
        client_balancing_enabled: bool | None = None,
        min_bitrate_type: str | None = None,
        ap_band_settings: dict | None = None,
        two_four_ghz_settings: dict | None = None,
        five_ghz_settings: dict | None = None,
        six_ghz_settings: dict | None = None,
        transmission: dict | None = None,
        per_ssid_settings: dict | None = None,
        flex_radios: dict | None = None,
    ) -> dict[str, Any] | None:
        """Creates new RF profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-rf-profile

        Args:
            network_id: Network ID.
            name: The name of the new profile. Must be unique. This param is required on creation.
            client_balancing_enabled: Steers client to best available access point. Can be either
              true or false. Defaults to true.
            min_bitrate_type: Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to
              band.
            band_selection_type: Band selection can be set to either 'ssid' or 'ap'. This param is
              required on creation.
            ap_band_settings: Settings that will be enabled if selectionType is set to 'ap'.
            two_four_ghz_settings: Settings related to 2.4Ghz band.
            five_ghz_settings: Settings related to 5Ghz band.
            six_ghz_settings: Settings related to 6Ghz band. Only applicable to networks with 6Ghz
              capable APs.
            transmission: Settings related to radio transmission.
            per_ssid_settings: Per-SSID radio settings by number.
            flex_radios: Flex radio settings.

        """
        if min_bitrate_type is not None:
            options = ["band", "ssid"]
            assert min_bitrate_type in options, (
                f'"min_bitrate_type" cannot be "{min_bitrate_type}", & must be set to one of: {options}'
            )
        if band_selection_type is not None:
            options = ["ap", "ssid"]
            assert band_selection_type in options, (
                f'"band_selection_type" cannot be "{band_selection_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "create_network_wireless_rf_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/rfProfiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if client_balancing_enabled is not None:
            payload["clientBalancingEnabled"] = client_balancing_enabled
        if min_bitrate_type is not None:
            payload["minBitrateType"] = min_bitrate_type
        if band_selection_type is not None:
            payload["bandSelectionType"] = band_selection_type
        if ap_band_settings is not None:
            payload["apBandSettings"] = ap_band_settings
        if two_four_ghz_settings is not None:
            payload["twoFourGhzSettings"] = two_four_ghz_settings
        if five_ghz_settings is not None:
            payload["fiveGhzSettings"] = five_ghz_settings
        if six_ghz_settings is not None:
            payload["sixGhzSettings"] = six_ghz_settings
        if transmission is not None:
            payload["transmission"] = transmission
        if per_ssid_settings is not None:
            payload["perSsidSettings"] = per_ssid_settings
        if flex_radios is not None:
            payload["flexRadios"] = flex_radios

        return self._session.post(metadata, resource, payload)

    def update_network_wireless_rf_profile(
        self,
        network_id: str,
        rf_profile_id: str,
        *,
        name: str | None = None,
        is_indoor_default: bool | None = None,
        is_outdoor_default: bool | None = None,
        client_balancing_enabled: bool | None = None,
        min_bitrate_type: str | None = None,
        band_selection_type: str | None = None,
        ap_band_settings: dict | None = None,
        two_four_ghz_settings: dict | None = None,
        five_ghz_settings: dict | None = None,
        six_ghz_settings: dict | None = None,
        transmission: dict | None = None,
        per_ssid_settings: dict | None = None,
        flex_radios: dict | None = None,
    ) -> dict[str, Any] | None:
        """Updates specified RF profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile

        Args:
            network_id: Network ID.
            rf_profile_id: Rf profile ID.
            name: The name of the new profile. Must be unique.
            is_indoor_default: Set this profile as the default indoor rf profile. If the profile ID
              is one of 'indoor' or 'outdoor', then a new profile will be created from
              the respective ID and set as the default.
            is_outdoor_default: Set this profile as the default outdoor rf profile. If the profile
              ID is one of 'indoor' or 'outdoor', then a new profile will be created
              from the respective ID and set as the default.
            client_balancing_enabled: Steers client to best available access point. Can be either
              true or false.
            min_bitrate_type: Minimum bitrate can be set to either 'band' or 'ssid'.
            band_selection_type: Band selection can be set to either 'ssid' or 'ap'.
            ap_band_settings: Settings that will be enabled if selectionType is set to 'ap'.
            two_four_ghz_settings: Settings related to 2.4Ghz band.
            five_ghz_settings: Settings related to 5Ghz band.
            six_ghz_settings: Settings related to 6Ghz band. Only applicable to networks with 6Ghz
              capable APs.
            transmission: Settings related to radio transmission.
            per_ssid_settings: Per-SSID radio settings by number.
            flex_radios: Flex radio settings.

        """
        if min_bitrate_type is not None:
            options = ["band", "ssid"]
            assert min_bitrate_type in options, (
                f'"min_bitrate_type" cannot be "{min_bitrate_type}", & must be set to one of: {options}'
            )
        if band_selection_type is not None:
            options = ["ap", "ssid"]
            assert band_selection_type in options, (
                f'"band_selection_type" cannot be "{band_selection_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "update_network_wireless_rf_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        rf_profile_id = urllib.parse.quote(str(rf_profile_id), safe="")
        resource = f"/networks/{network_id}/wireless/rfProfiles/{rf_profile_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if is_indoor_default is not None:
            payload["isIndoorDefault"] = is_indoor_default
        if is_outdoor_default is not None:
            payload["isOutdoorDefault"] = is_outdoor_default
        if client_balancing_enabled is not None:
            payload["clientBalancingEnabled"] = client_balancing_enabled
        if min_bitrate_type is not None:
            payload["minBitrateType"] = min_bitrate_type
        if band_selection_type is not None:
            payload["bandSelectionType"] = band_selection_type
        if ap_band_settings is not None:
            payload["apBandSettings"] = ap_band_settings
        if two_four_ghz_settings is not None:
            payload["twoFourGhzSettings"] = two_four_ghz_settings
        if five_ghz_settings is not None:
            payload["fiveGhzSettings"] = five_ghz_settings
        if six_ghz_settings is not None:
            payload["sixGhzSettings"] = six_ghz_settings
        if transmission is not None:
            payload["transmission"] = transmission
        if per_ssid_settings is not None:
            payload["perSsidSettings"] = per_ssid_settings
        if flex_radios is not None:
            payload["flexRadios"] = flex_radios

        return self._session.put(metadata, resource, payload)

    def delete_network_wireless_rf_profile(self, network_id: str, rf_profile_id: str) -> None:
        """Delete a RF Profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile

        Args:
            network_id: Network ID.
            rf_profile_id: Rf profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "delete_network_wireless_rf_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        rf_profile_id = urllib.parse.quote(str(rf_profile_id), safe="")
        resource = f"/networks/{network_id}/wireless/rfProfiles/{rf_profile_id}"

        return self._session.delete(metadata, resource)

    def get_network_wireless_rf_profile(
        self, network_id: str, rf_profile_id: str
    ) -> dict[str, Any] | None:
        """Return a RF profile.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile

        Args:
            network_id: Network ID.
            rf_profile_id: Rf profile ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "get_network_wireless_rf_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        rf_profile_id = urllib.parse.quote(str(rf_profile_id), safe="")
        resource = f"/networks/{network_id}/wireless/rfProfiles/{rf_profile_id}"

        return self._session.get(metadata, resource)

    def get_network_wireless_settings(self, network_id: str) -> dict[str, Any] | None:
        """Return the wireless settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-settings

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "settings"],
            "operation": "get_network_wireless_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/settings"

        return self._session.get(metadata, resource)

    def update_network_wireless_settings(
        self,
        network_id: str,
        *,
        meshing_enabled: bool | None = None,
        ipv6_bridge_enabled: bool | None = None,
        location_analytics_enabled: bool | None = None,
        upgrade_strategy: str | None = None,
        led_lights_on: bool | None = None,
        named_vlans: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the wireless settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-settings

        Args:
            network_id: Network ID.
            meshing_enabled: Toggle for enabling or disabling meshing in a network.
            ipv6_bridge_enabled: Toggle for enabling or disabling IPv6 bridging in a network (Note:
              if enabled, SSIDs must also be configured to use bridge mode).
            location_analytics_enabled: Toggle for enabling or disabling location analytics for your
              network.
            upgrade_strategy: The default strategy that network devices will use to perform an
              upgrade. Requires firmware version MR 26.8 or higher.
            led_lights_on: Toggle for enabling or disabling LED lights on all APs in the network
              (making them run dark).
            named_vlans: Named VLAN settings for wireless networks.

        """
        if upgrade_strategy is not None:
            options = ["minimizeClientDowntime", "minimizeUpgradeTime"]
            assert upgrade_strategy in options, (
                f'"upgrade_strategy" cannot be "{upgrade_strategy}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "settings"],
            "operation": "update_network_wireless_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/settings"

        payload = {}
        if meshing_enabled is not None:
            payload["meshingEnabled"] = meshing_enabled
        if ipv6_bridge_enabled is not None:
            payload["ipv6BridgeEnabled"] = ipv6_bridge_enabled
        if location_analytics_enabled is not None:
            payload["locationAnalyticsEnabled"] = location_analytics_enabled
        if upgrade_strategy is not None:
            payload["upgradeStrategy"] = upgrade_strategy
        if led_lights_on is not None:
            payload["ledLightsOn"] = led_lights_on
        if named_vlans is not None:
            payload["namedVlans"] = named_vlans

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_signal_quality_history(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
        auto_resolution: bool | None = None,
        client_id: str | None = None,
        device_serial: str | None = None,
        ap_tag: str | None = None,
        band: str | None = None,
        ssid: int | None = None,
    ) -> dict[str, Any] | None:
        """Return signal quality (SNR/RSSI) over time for a device or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-signal-quality-history

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            auto_resolution: Automatically select a data resolution based on the given timespan;
              this overrides the value specified by the 'resolution' parameter. The
              default setting is false.
            client_id: Filter results by network client.
            device_serial: Filter results by device.
            ap_tag: Filter results by AP tag; either :clientId or :deviceSerial must be jointly
              specified.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "signalQualityHistory"],
            "operation": "get_network_wireless_signal_quality_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/signalQualityHistory"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution
        if auto_resolution is not None:
            params["autoResolution"] = auto_resolution
        if client_id is not None:
            params["clientId"] = client_id
        if device_serial is not None:
            params["deviceSerial"] = device_serial
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid

        return self._session.get(metadata, resource, params)

    def get_network_wireless_ssids(self, network_id: str) -> dict[str, Any] | None:
        """List the MR SSIDs in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssids

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "get_network_wireless_ssids",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/ssids"

        return self._session.get(metadata, resource)

    def get_network_wireless_ssid(self, network_id: str, number: str) -> dict[str, Any] | None:
        """Return a single MR SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "get_network_wireless_ssid",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid(
        self,
        network_id: str,
        number: str,
        *,
        name: str | None = None,
        enabled: bool | None = None,
        auth_mode: str | None = None,
        enterprise_admin_access: str | None = None,
        encryption_mode: str | None = None,
        psk: str | None = None,
        wpa_encryption_mode: str | None = None,
        dot11w: dict | None = None,
        dot11r: dict | None = None,
        splash_page: str | None = None,
        splash_guest_sponsor_domains: list | None = None,
        oauth: dict | None = None,
        local_radius: dict | None = None,
        ldap: dict | None = None,
        active_directory: dict | None = None,
        radius_servers: list | None = None,
        radius_proxy_enabled: bool | None = None,
        radius_testing_enabled: bool | None = None,
        radius_called_station_id: str | None = None,
        radius_authentication_nas_id: str | None = None,
        radius_server_timeout: int | None = None,
        radius_server_attempts_limit: int | None = None,
        radius_fallback_enabled: bool | None = None,
        radius_radsec: dict | None = None,
        radius_coa_enabled: bool | None = None,
        radius_failover_policy: str | None = None,
        radius_load_balancing_policy: str | None = None,
        radius_accounting_enabled: bool | None = None,
        radius_accounting_servers: list | None = None,
        radius_accounting_interim_interval: int | None = None,
        radius_attribute_for_group_policies: str | None = None,
        ip_assignment_mode: str | None = None,
        use_vlan_tagging: bool | None = None,
        concentrator_network_id: str | None = None,
        secondary_concentrator_network_id: str | None = None,
        disassociate_clients_on_vpn_failover: bool | None = None,
        vlan_id: int | None = None,
        default_vlan_id: int | None = None,
        ap_tags_and_vlan_ids: list | None = None,
        walled_garden_enabled: bool | None = None,
        walled_garden_ranges: list | None = None,
        gre: dict | None = None,
        radius_override: bool | None = None,
        radius_guest_vlan_enabled: bool | None = None,
        radius_guest_vlan_id: int | None = None,
        min_bitrate: float | None = None,
        band_selection: str | None = None,
        per_client_bandwidth_limit_up: int | None = None,
        per_client_bandwidth_limit_down: int | None = None,
        per_ssid_bandwidth_limit_up: int | None = None,
        per_ssid_bandwidth_limit_down: int | None = None,
        lan_isolation_enabled: bool | None = None,
        visible: bool | None = None,
        available_on_all_aps: bool | None = None,
        availability_tags: list | None = None,
        adaptive_policy_group_id: str | None = None,
        mandatory_dhcp_enabled: bool | None = None,
        adult_content_filtering_enabled: bool | None = None,
        dns_rewrite: dict | None = None,
        speed_burst: dict | None = None,
        named_vlans: dict | None = None,
        local_auth_fallback: dict | None = None,
        radius_accounting_start_delay: int | None = None,
    ) -> dict[str, Any] | None:
        """Update the attributes of an MR SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid

        Args:
            network_id: Network ID.
            number: Number.
            name: The name of the SSID.
            enabled: Whether or not the SSID is enabled.
            auth_mode: The association control method for the SSID ('open', 'open-enhanced', 'psk',
              'open-with-radius', 'open-with-nac', '8021x-meraki', '8021x-nac',
              '8021x-radius', '8021x-google', '8021x-entra', '8021x-localradius', 'ipsk-
              with-radius', 'ipsk-without-radius', 'ipsk-with-nac' or 'ipsk-with-radius-
              easy-psk').
            enterprise_admin_access: Whether or not an SSID is accessible by 'enterprise'
              administrators ('access disabled' or 'access enabled').
            encryption_mode: The psk encryption mode for the SSID ('wep' or 'wpa'). This param is
              only valid if the authMode is 'psk'.
            psk: The passkey for the SSID. This param is only valid if the authMode is 'psk'.
            wpa_encryption_mode: The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2
              only', 'WPA3 Transition Mode', 'WPA3 only' or 'WPA3 192-bit Security').
            dot11w: The current setting for Protected Management Frames (802.11w).
            dot11r: The current setting for 802.11r.
            splash_page: The type of splash page for the SSID ('None', 'Click-through splash page',
              'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected
              with custom RADIUS', 'Password-protected with Active Directory',
              'Password-protected with LDAP', 'SMS authentication', 'Systems Manager
              Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Microsoft Entra ID',
              'Sponsored guest', 'Cisco ISE' or 'Google Apps domain').This attribute is
              not supported for template children.
            splash_guest_sponsor_domains: Array of valid sponsor email domains for sponsored guest
              splash type.
            oauth: The OAuth settings of this SSID. Only valid if splashPage is 'Google OAuth'.
            local_radius: The current setting for Local Authentication, a built-in RADIUS server on
              the access point. Only valid if authMode is '8021x-localradius'.
            ldap: The current setting for LDAP. Only valid if splashPage is 'Password-protected with
              LDAP'.
            active_directory: The current setting for Active Directory. Only valid if splashPage is
              'Password-protected with Active Directory'.
            radius_servers: The RADIUS 802.1X servers to be used for authentication. This param is
              only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-
              with-radius'.
            radius_proxy_enabled: If true, Meraki devices will proxy RADIUS messages through the
              Meraki cloud to the configured RADIUS auth and accounting servers.
            radius_testing_enabled: If true, Meraki devices will periodically send Access-Request
              messages to configured RADIUS servers using identity 'meraki_8021x_test'
              to ensure that the RADIUS servers are reachable.
            radius_called_station_id: The template of the called station identifier to be used for
              RADIUS (ex. $NODE_MAC$:$VAP_NUM$).
            radius_authentication_nas_id: The template of the NAS identifier to be used for RADIUS
              authentication (ex. $NODE_MAC$:$VAP_NUM$).
            radius_server_timeout: The amount of time for which a RADIUS client waits for a reply
              from the RADIUS server (must be between 1-10 seconds).
            radius_server_attempts_limit: The maximum number of transmit attempts after which a
              RADIUS server is failed over (must be between 1-5).
            radius_fallback_enabled: Whether or not higher priority RADIUS servers should be retried
              after 60 seconds.
            radius_radsec: The current settings for RADIUS RADSec.
            radius_coa_enabled: If true, Meraki devices will act as a RADIUS Dynamic Authorization
              Server and will respond to RADIUS Change-of-Authorization and Disconnect
              messages sent by the RADIUS server.
            radius_failover_policy: This policy determines how authentication requests should be
              handled in the event that all of the configured RADIUS servers are
              unreachable ('Deny access' or 'Allow access').
            radius_load_balancing_policy: This policy determines which RADIUS server will be
              contacted first in an authentication attempt and the ordering of any
              necessary retry attempts ('Strict priority order' or 'Round robin').
            radius_accounting_enabled: Whether or not RADIUS accounting is enabled. This param is
              only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-
              with-radius'.
            radius_accounting_servers: The RADIUS accounting 802.1X servers to be used for
              authentication. This param is only valid if the authMode is 'open-with-
              radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled
              is 'true'.
            radius_accounting_interim_interval: The interval (in seconds) in which accounting
              information is updated and sent to the RADIUS accounting server.
            radius_attribute_for_group_policies: Specify the RADIUS attribute used to look up group
              policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-
              User-Role'). Access points must receive this attribute in the RADIUS
              Access-Accept message.
            ip_assignment_mode: The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3
              roaming', 'Ethernet over GRE', 'Layer 3 roaming with a concentrator',
              'VPN' or 'Campus Gateway').
            use_vlan_tagging: Whether or not traffic should be directed to use specific VLANs. This
              param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3
              roaming'.
            concentrator_network_id: The concentrator to use when the ipAssignmentMode is 'Layer 3
              roaming with a concentrator' or 'VPN'.
            secondary_concentrator_network_id: The secondary concentrator to use when the
              ipAssignmentMode is 'VPN'. If configured, the APs will switch to using
              this concentrator if the primary concentrator is unreachable. This param
              is optional. ('disabled' represents no secondary concentrator.).
            disassociate_clients_on_vpn_failover: Disassociate clients when 'VPN' concentrator
              failover occurs in order to trigger clients to re-associate and generate
              new DHCP requests. This param is only valid if ipAssignmentMode is 'VPN'.
            vlan_id: The VLAN ID used for VLAN tagging. This param is only valid when the
              ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
            default_vlan_id: The default VLAN ID used for 'all other APs'. This param is only valid
              when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'.
            ap_tags_and_vlan_ids: The list of tags and VLAN IDs used for VLAN tagging. This param is
              only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3
              roaming'.
            walled_garden_enabled: Allow access to a configurable list of IP ranges, which users may
              access prior to sign-on.
            walled_garden_ranges: Specify your walled garden by entering an array of addresses,
              ranges using CIDR notation, domain names, and domain wildcards (e.g.
              '192.168.1.1/24', '192.168.37.10/32', 'www.yahoo.com', '*.google.com']).
              Meraki's splash page is automatically included in your walled garden.
            gre: Ethernet over GRE settings.
            radius_override: If true, the RADIUS response can override VLAN tag. This is not valid
              when ipAssignmentMode is 'NAT mode'.
            radius_guest_vlan_enabled: Whether or not RADIUS Guest VLAN is enabled. This param is
              only valid if the authMode is 'open-with-radius' and addressing mode is
              not set to 'isolated' or 'nat' mode.
            radius_guest_vlan_id: VLAN ID of the RADIUS Guest VLAN. This param is only valid if the
              authMode is 'open-with-radius' and addressing mode is not set to
              'isolated' or 'nat' mode.
            min_bitrate: The minimum bitrate in Mbps of this SSID in the default indoor RF profile.
              ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54').
            band_selection: The client-serving radio frequencies of this SSID in the default indoor
              RF profile. ('Dual band operation', '5 GHz band only' or 'Dual band
              operation with Band Steering').
            per_client_bandwidth_limit_up: The upload bandwidth limit in Kbps. (0 represents no
              limit.).
            per_client_bandwidth_limit_down: The download bandwidth limit in Kbps. (0 represents no
              limit.).
            per_ssid_bandwidth_limit_up: The total upload bandwidth limit in Kbps. (0 represents no
              limit.).
            per_ssid_bandwidth_limit_down: The total download bandwidth limit in Kbps. (0 represents
              no limit.).
            lan_isolation_enabled: Boolean indicating whether Layer 2 LAN isolation should be
              enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge
              mode'.
            visible: Boolean indicating whether APs should advertise or hide this SSID. APs will
              only broadcast this SSID if set to true.
            available_on_all_aps: Boolean indicating whether all APs should broadcast the SSID or if
              it should be restricted to APs matching any availability tags. Can only be
              false if the SSID has availability tags.
            availability_tags: Accepts a list of tags for this SSID. If availableOnAllAps is false,
              then the SSID will only be broadcast by APs with tags matching any of the
              tags in this list.
            adaptive_policy_group_id: Adaptive policy group ID this SSID is assigned to.
            mandatory_dhcp_enabled: If true, Mandatory DHCP will enforce that clients connecting to
              this SSID must use the IP address assigned by the DHCP server. Clients who
              use a static IP address won't be able to associate.
            adult_content_filtering_enabled: Boolean indicating whether or not adult content will be
              blocked.
            dns_rewrite: DNS servers rewrite settings.
            speed_burst: The SpeedBurst setting for this SSID'.
            named_vlans: Named VLAN settings.
            local_auth_fallback: The current configuration for Local Authentication Fallback.
              Enables the Access Point (AP) to store client authentication data for a
              specified duration that can be adjusted as needed.
            radius_accounting_start_delay: The delay (in seconds) before sending the first RADIUS
              accounting start message. Must be between 0 and 60 seconds.

        """
        if auth_mode is not None:
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
            assert auth_mode in options, (
                f'"auth_mode" cannot be "{auth_mode}", & must be set to one of: {options}'
            )
        if enterprise_admin_access is not None:
            options = ["access disabled", "access enabled"]
            assert enterprise_admin_access in options, (
                f'"enterprise_admin_access" cannot be "{enterprise_admin_access}", & must be set to one of: {options}'
            )
        if encryption_mode is not None:
            options = ["open", "wep", "wpa", "wpa-eap"]
            assert encryption_mode in options, (
                f'"encryption_mode" cannot be "{encryption_mode}", & must be set to one of: {options}'
            )
        if wpa_encryption_mode is not None:
            options = [
                "WPA1 and WPA2",
                "WPA1 only",
                "WPA2 only",
                "WPA3 192-bit Security",
                "WPA3 Transition Mode",
                "WPA3 only",
            ]
            assert wpa_encryption_mode in options, (
                f'"wpa_encryption_mode" cannot be "{wpa_encryption_mode}", & must be set to one of: {options}'
            )
        if splash_page is not None:
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
            assert splash_page in options, (
                f'"splash_page" cannot be "{splash_page}", & must be set to one of: {options}'
            )
        if radius_failover_policy is not None:
            options = ["Allow access", "Deny access"]
            assert radius_failover_policy in options, (
                f'"radius_failover_policy" cannot be "{radius_failover_policy}", & must be set to one of: {options}'
            )
        if radius_load_balancing_policy is not None:
            options = ["Round robin", "Strict priority order"]
            assert radius_load_balancing_policy in options, (
                f'"radius_load_balancing_policy" cannot be "{radius_load_balancing_policy}", & must be set to one of: {options}'
            )
        if radius_attribute_for_group_policies is not None:
            options = ["Airespace-ACL-Name", "Aruba-User-Role", "Filter-Id", "Reply-Message"]
            assert radius_attribute_for_group_policies in options, (
                f'"radius_attribute_for_group_policies" cannot be "{radius_attribute_for_group_policies}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "update_network_wireless_ssid",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if enabled is not None:
            payload["enabled"] = enabled
        if auth_mode is not None:
            payload["authMode"] = auth_mode
        if enterprise_admin_access is not None:
            payload["enterpriseAdminAccess"] = enterprise_admin_access
        if encryption_mode is not None:
            payload["encryptionMode"] = encryption_mode
        if psk is not None:
            payload["psk"] = psk
        if wpa_encryption_mode is not None:
            payload["wpaEncryptionMode"] = wpa_encryption_mode
        if dot11w is not None:
            payload["dot11w"] = dot11w
        if dot11r is not None:
            payload["dot11r"] = dot11r
        if splash_page is not None:
            payload["splashPage"] = splash_page
        if splash_guest_sponsor_domains is not None:
            payload["splashGuestSponsorDomains"] = splash_guest_sponsor_domains
        if oauth is not None:
            payload["oauth"] = oauth
        if local_radius is not None:
            payload["localRadius"] = local_radius
        if ldap is not None:
            payload["ldap"] = ldap
        if active_directory is not None:
            payload["activeDirectory"] = active_directory
        if radius_servers is not None:
            payload["radiusServers"] = radius_servers
        if radius_proxy_enabled is not None:
            payload["radiusProxyEnabled"] = radius_proxy_enabled
        if radius_testing_enabled is not None:
            payload["radiusTestingEnabled"] = radius_testing_enabled
        if radius_called_station_id is not None:
            payload["radiusCalledStationId"] = radius_called_station_id
        if radius_authentication_nas_id is not None:
            payload["radiusAuthenticationNasId"] = radius_authentication_nas_id
        if radius_server_timeout is not None:
            payload["radiusServerTimeout"] = radius_server_timeout
        if radius_server_attempts_limit is not None:
            payload["radiusServerAttemptsLimit"] = radius_server_attempts_limit
        if radius_fallback_enabled is not None:
            payload["radiusFallbackEnabled"] = radius_fallback_enabled
        if radius_radsec is not None:
            payload["radiusRadsec"] = radius_radsec
        if radius_coa_enabled is not None:
            payload["radiusCoaEnabled"] = radius_coa_enabled
        if radius_failover_policy is not None:
            payload["radiusFailoverPolicy"] = radius_failover_policy
        if radius_load_balancing_policy is not None:
            payload["radiusLoadBalancingPolicy"] = radius_load_balancing_policy
        if radius_accounting_enabled is not None:
            payload["radiusAccountingEnabled"] = radius_accounting_enabled
        if radius_accounting_servers is not None:
            payload["radiusAccountingServers"] = radius_accounting_servers
        if radius_accounting_interim_interval is not None:
            payload["radiusAccountingInterimInterval"] = radius_accounting_interim_interval
        if radius_attribute_for_group_policies is not None:
            payload["radiusAttributeForGroupPolicies"] = radius_attribute_for_group_policies
        if ip_assignment_mode is not None:
            payload["ipAssignmentMode"] = ip_assignment_mode
        if use_vlan_tagging is not None:
            payload["useVlanTagging"] = use_vlan_tagging
        if concentrator_network_id is not None:
            payload["concentratorNetworkId"] = concentrator_network_id
        if secondary_concentrator_network_id is not None:
            payload["secondaryConcentratorNetworkId"] = secondary_concentrator_network_id
        if disassociate_clients_on_vpn_failover is not None:
            payload["disassociateClientsOnVpnFailover"] = disassociate_clients_on_vpn_failover
        if vlan_id is not None:
            payload["vlanId"] = vlan_id
        if default_vlan_id is not None:
            payload["defaultVlanId"] = default_vlan_id
        if ap_tags_and_vlan_ids is not None:
            payload["apTagsAndVlanIds"] = ap_tags_and_vlan_ids
        if walled_garden_enabled is not None:
            payload["walledGardenEnabled"] = walled_garden_enabled
        if walled_garden_ranges is not None:
            payload["walledGardenRanges"] = walled_garden_ranges
        if gre is not None:
            payload["gre"] = gre
        if radius_override is not None:
            payload["radiusOverride"] = radius_override
        if radius_guest_vlan_enabled is not None:
            payload["radiusGuestVlanEnabled"] = radius_guest_vlan_enabled
        if radius_guest_vlan_id is not None:
            payload["radiusGuestVlanId"] = radius_guest_vlan_id
        if min_bitrate is not None:
            payload["minBitrate"] = min_bitrate
        if band_selection is not None:
            payload["bandSelection"] = band_selection
        if per_client_bandwidth_limit_up is not None:
            payload["perClientBandwidthLimitUp"] = per_client_bandwidth_limit_up
        if per_client_bandwidth_limit_down is not None:
            payload["perClientBandwidthLimitDown"] = per_client_bandwidth_limit_down
        if per_ssid_bandwidth_limit_up is not None:
            payload["perSsidBandwidthLimitUp"] = per_ssid_bandwidth_limit_up
        if per_ssid_bandwidth_limit_down is not None:
            payload["perSsidBandwidthLimitDown"] = per_ssid_bandwidth_limit_down
        if lan_isolation_enabled is not None:
            payload["lanIsolationEnabled"] = lan_isolation_enabled
        if visible is not None:
            payload["visible"] = visible
        if available_on_all_aps is not None:
            payload["availableOnAllAps"] = available_on_all_aps
        if availability_tags is not None:
            payload["availabilityTags"] = availability_tags
        if adaptive_policy_group_id is not None:
            payload["adaptivePolicyGroupId"] = adaptive_policy_group_id
        if mandatory_dhcp_enabled is not None:
            payload["mandatoryDhcpEnabled"] = mandatory_dhcp_enabled
        if adult_content_filtering_enabled is not None:
            payload["adultContentFilteringEnabled"] = adult_content_filtering_enabled
        if dns_rewrite is not None:
            payload["dnsRewrite"] = dns_rewrite
        if speed_burst is not None:
            payload["speedBurst"] = speed_burst
        if named_vlans is not None:
            payload["namedVlans"] = named_vlans
        if local_auth_fallback is not None:
            payload["localAuthFallback"] = local_auth_fallback
        if radius_accounting_start_delay is not None:
            payload["radiusAccountingStartDelay"] = radius_accounting_start_delay

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_bonjour_forwarding(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """List the Bonjour forwarding setting and rules for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-bonjour-forwarding

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "bonjourForwarding"],
            "operation": "get_network_wireless_ssid_bonjour_forwarding",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/bonjourForwarding"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_bonjour_forwarding(
        self,
        network_id: str,
        number: str,
        *,
        enabled: bool | None = None,
        rules: list | None = None,
        exception: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the bonjour forwarding setting and rules for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-bonjour-forwarding

        Args:
            network_id: Network ID.
            number: Number.
            enabled: If true, Bonjour forwarding is enabled on this SSID.
            rules: List of bonjour forwarding rules.
            exception: Bonjour forwarding exception.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "bonjourForwarding"],
            "operation": "update_network_wireless_ssid_bonjour_forwarding",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/bonjourForwarding"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if rules is not None:
            payload["rules"] = rules
        if exception is not None:
            payload["exception"] = exception

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_device_type_group_policies(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """List the device type group policies for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-device-type-group-policies

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "deviceTypeGroupPolicies"],
            "operation": "get_network_wireless_ssid_device_type_group_policies",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/deviceTypeGroupPolicies"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_device_type_group_policies(
        self,
        network_id: str,
        number: str,
        *,
        enabled: bool | None = None,
        device_type_policies: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the device type group policies for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-device-type-group-policies

        Args:
            network_id: Network ID.
            number: Number.
            enabled: If true, the SSID device type group policies are enabled.
            device_type_policies: List of device type policies.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "deviceTypeGroupPolicies"],
            "operation": "update_network_wireless_ssid_device_type_group_policies",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/deviceTypeGroupPolicies"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if device_type_policies is not None:
            payload["deviceTypePolicies"] = device_type_policies

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_eap_override(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """Return the EAP overridden parameters for an SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-eap-override

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "eapOverride"],
            "operation": "get_network_wireless_ssid_eap_override",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/eapOverride"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_eap_override(
        self,
        network_id: str,
        number: str,
        *,
        timeout: int | None = None,
        identity: dict | None = None,
        max_retries: int | None = None,
        eapol_key: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the EAP overridden parameters for an SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-eap-override

        Args:
            network_id: Network ID.
            number: Number.
            timeout: General EAP timeout in seconds.
            identity: EAP settings for identity requests.
            max_retries: Maximum number of general EAP retries.
            eapol_key: EAPOL Key settings.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "eapOverride"],
            "operation": "update_network_wireless_ssid_eap_override",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/eapOverride"

        payload = {}
        if timeout is not None:
            payload["timeout"] = timeout
        if identity is not None:
            payload["identity"] = identity
        if max_retries is not None:
            payload["maxRetries"] = max_retries
        if eapol_key is not None:
            payload["eapolKey"] = eapol_key

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_firewall_l3_firewall_rules(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """Return the L3 firewall rules for an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-3-firewall-rules

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l3FirewallRules"],
            "operation": "get_network_wireless_ssid_firewall_l3_firewall_rules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/firewall/l3FirewallRules"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_firewall_l3_firewall_rules(
        self,
        network_id: str,
        number: str,
        *,
        rules: list | None = None,
        allow_lan_access: bool | None = None,
    ) -> dict[str, Any] | None:
        """Update the L3 firewall rules of an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules

        Args:
            network_id: Network ID.
            number: Number.
            rules: An ordered array of the firewall rules for this SSID.
            allow_lan_access: Allow wireless client access to local LAN (boolean value - true allows
              access and false denies access) (optional).

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l3FirewallRules"],
            "operation": "update_network_wireless_ssid_firewall_l3_firewall_rules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/firewall/l3FirewallRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules
        if allow_lan_access is not None:
            payload["allowLanAccess"] = allow_lan_access

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_firewall_l7_firewall_rules(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """Return the L7 firewall rules for an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-7-firewall-rules

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l7FirewallRules"],
            "operation": "get_network_wireless_ssid_firewall_l7_firewall_rules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/firewall/l7FirewallRules"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_firewall_l7_firewall_rules(
        self, network_id: str, number: str, *, rules: list | None = None
    ) -> dict[str, Any] | None:
        """Update the L7 firewall rules of an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-7-firewall-rules

        Args:
            network_id: Network ID.
            number: Number.
            rules: An array of L7 firewall rules for this SSID. Rules will get applied in the same
              order user has specified in request. Empty array will clear the L7
              firewall rule configuration.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l7FirewallRules"],
            "operation": "update_network_wireless_ssid_firewall_l7_firewall_rules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/firewall/l7FirewallRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_hotspot20(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """Return the Hotspot 2.0 settings for an SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-hotspot-2-0

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "hotspot20"],
            "operation": "get_network_wireless_ssid_hotspot20",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/hotspot20"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_hotspot20(
        self,
        network_id: str,
        number: str,
        *,
        enabled: bool | None = None,
        operator: dict | None = None,
        venue: dict | None = None,
        network_access_type: str | None = None,
        domains: list | None = None,
        roam_consort_ois: list | None = None,
        mcc_mncs: list | None = None,
        nai_realms: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the Hotspot 2.0 settings of an SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-hotspot-2-0

        Args:
            network_id: Network ID.
            number: Number.
            enabled: Whether or not Hotspot 2.0 for this SSID is enabled.
            operator: Operator settings for this SSID.
            venue: Venue settings for this SSID.
            network_access_type: The network type of this SSID ('Private network', 'Private network
              with guest access', 'Chargeable public network', 'Free public network',
              'Personal device network', 'Emergency services only network', 'Test or
              experimental', 'Wildcard').
            domains: An array of domain names.
            roam_consort_ois: An array of roaming consortium OIs (hexadecimal number 3-5 octets in
              length).
            mcc_mncs: An array of MCC/MNC pairs.
            nai_realms: An array of NAI realms.

        """
        if network_access_type is not None:
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
            assert network_access_type in options, (
                f'"network_access_type" cannot be "{network_access_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "hotspot20"],
            "operation": "update_network_wireless_ssid_hotspot20",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/hotspot20"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if operator is not None:
            payload["operator"] = operator
        if venue is not None:
            payload["venue"] = venue
        if network_access_type is not None:
            payload["networkAccessType"] = network_access_type
        if domains is not None:
            payload["domains"] = domains
        if roam_consort_ois is not None:
            payload["roamConsortOis"] = roam_consort_ois
        if mcc_mncs is not None:
            payload["mccMncs"] = mcc_mncs
        if nai_realms is not None:
            payload["naiRealms"] = nai_realms

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_identity_psks(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """List all Identity PSKs in a wireless network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psks

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "get_network_wireless_ssid_identity_psks",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/identityPsks"

        return self._session.get(metadata, resource)

    def create_network_wireless_ssid_identity_psk(
        self,
        network_id: str,
        number: str,
        name: str,
        group_policy_id: str,
        *,
        passphrase: str | None = None,
        expires_at: str | None = None,
    ) -> dict[str, Any] | None:
        """Create an Identity PSK.

        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-identity-psk

        Args:
            network_id: Network ID.
            number: Number.
            name: The name of the Identity PSK.
            passphrase: The passphrase for client authentication. If left blank, one will be auto-
              generated.
            group_policy_id: The group policy to be applied to clients.
            expires_at: Timestamp for when the Identity PSK expires. Will not expire if left blank.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "create_network_wireless_ssid_identity_psk",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/identityPsks"

        payload = {}
        if name is not None:
            payload["name"] = name
        if passphrase is not None:
            payload["passphrase"] = passphrase
        if group_policy_id is not None:
            payload["groupPolicyId"] = group_policy_id
        if expires_at is not None:
            payload["expiresAt"] = expires_at

        return self._session.post(metadata, resource, payload)

    def get_network_wireless_ssid_identity_psk(
        self, network_id: str, number: str, identity_psk_id: str
    ) -> dict[str, Any] | None:
        """Return an Identity PSK.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psk

        Args:
            network_id: Network ID.
            number: Number.
            identity_psk_id: Identity psk ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "get_network_wireless_ssid_identity_psk",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identity_psk_id = urllib.parse.quote(str(identity_psk_id), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_identity_psk(
        self,
        network_id: str,
        number: str,
        identity_psk_id: str,
        *,
        name: str | None = None,
        passphrase: str | None = None,
        group_policy_id: str | None = None,
        expires_at: str | None = None,
    ) -> dict[str, Any] | None:
        """Update an Identity PSK.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-identity-psk

        Args:
            network_id: Network ID.
            number: Number.
            identity_psk_id: Identity psk ID.
            name: The name of the Identity PSK.
            passphrase: The passphrase for client authentication.
            group_policy_id: The group policy to be applied to clients.
            expires_at: Timestamp for when the Identity PSK expires, or 'null' to never expire.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "update_network_wireless_ssid_identity_psk",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identity_psk_id = urllib.parse.quote(str(identity_psk_id), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if passphrase is not None:
            payload["passphrase"] = passphrase
        if group_policy_id is not None:
            payload["groupPolicyId"] = group_policy_id
        if expires_at is not None:
            payload["expiresAt"] = expires_at

        return self._session.put(metadata, resource, payload)

    def delete_network_wireless_ssid_identity_psk(
        self, network_id: str, number: str, identity_psk_id: str
    ) -> None:
        """Delete an Identity PSK.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ssid-identity-psk

        Args:
            network_id: Network ID.
            number: Number.
            identity_psk_id: Identity psk ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "delete_network_wireless_ssid_identity_psk",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identity_psk_id = urllib.parse.quote(str(identity_psk_id), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}"

        return self._session.delete(metadata, resource)

    def update_network_wireless_ssid_open_roaming(
        self,
        network_id: str,
        number: str,
        *,
        enabled: bool | None = None,
        tenant_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Update the OpenRoaming setting for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-open-roaming

        Args:
            network_id: Network ID.
            number: Number.
            enabled: If true, OpenRoaming is enabled on this SSID.
            tenant_id: The OpenRoaming DNA Spaces tenant ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "openRoaming"],
            "operation": "update_network_wireless_ssid_open_roaming",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/openRoaming"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if tenant_id is not None:
            payload["tenantId"] = tenant_id

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_schedules(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """List the outage schedule for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-schedules

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "schedules"],
            "operation": "get_network_wireless_ssid_schedules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/schedules"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_schedules(
        self,
        network_id: str,
        number: str,
        *,
        enabled: bool | None = None,
        ranges: list | None = None,
        ranges_in_seconds: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the outage schedule for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-schedules

        Args:
            network_id: Network ID.
            number: Number.
            enabled: If true, the SSID outage schedule is enabled.
            ranges: List of outage ranges. Has a start date and time, and end date and time. If this
              parameter is passed in along with rangesInSeconds parameter, this will
              take precedence.
            ranges_in_seconds: List of outage ranges in seconds since Sunday at Midnight. Has a
              start and end. If this parameter is passed in along with the ranges
              parameter, ranges will take precedence.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "schedules"],
            "operation": "update_network_wireless_ssid_schedules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/schedules"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if ranges is not None:
            payload["ranges"] = ranges
        if ranges_in_seconds is not None:
            payload["rangesInSeconds"] = ranges_in_seconds

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_splash_settings(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """Display the splash page settings for the given SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-splash-settings

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "splash", "settings"],
            "operation": "get_network_wireless_ssid_splash_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/splash/settings"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_splash_settings(
        self,
        network_id: str,
        number: str,
        *,
        splash_url: str | None = None,
        use_splash_url: bool | None = None,
        splash_timeout: int | None = None,
        redirect_url: str | None = None,
        use_redirect_url: bool | None = None,
        welcome_message: str | None = None,
        theme_id: str | None = None,
        splash_logo: dict | None = None,
        splash_image: dict | None = None,
        splash_prepaid_front: dict | None = None,
        block_all_traffic_before_sign_on: bool | None = None,
        controller_disconnection_behavior: str | None = None,
        allow_simultaneous_logins: bool | None = None,
        guest_sponsorship: dict | None = None,
        billing: dict | None = None,
        sentry_enrollment: dict | None = None,
        self_registration: dict | None = None,
    ) -> dict[str, Any] | None:
        """Modify the splash page settings for the given SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-splash-settings

        Args:
            network_id: Network ID.
            number: Number.
            splash_url: [optional] The custom splash URL of the click-through splash page. Note that
              the URL can be configured without necessarily being used. In order to
              enable the custom URL, see 'useSplashUrl'.
            use_splash_url: [optional] Boolean indicating whether the users will be redirected to
              the custom splash url. A custom splash URL must be set if this is true.
              Note that depending on your SSID's access control settings, it may not be
              possible to use the custom splash URL.
            splash_timeout: Splash timeout in minutes. This will determine how often users will see
              the splash page.
            redirect_url: The custom redirect URL where the users will go after the splash page.
            use_redirect_url: The Boolean indicating whether the the user will be redirected to the
              custom redirect URL after the splash page. A custom redirect URL must be
              set if this is true.
            welcome_message: The welcome message for the users on the splash page.
            theme_id: The id of the selected splash theme.
            splash_logo: The logo used in the splash page.
            splash_image: The image used in the splash page.
            splash_prepaid_front: The prepaid front image used in the splash page.
            block_all_traffic_before_sign_on: How restricted allowing traffic should be. If true,
              all traffic types are blocked until the splash page is acknowledged. If
              false, all non-HTTP traffic is allowed before the splash page is
              acknowledged.
            controller_disconnection_behavior: How login attempts should be handled when the
              controller is unreachable. Can be either 'open', 'restricted', or
              'default'.
            allow_simultaneous_logins: Whether or not to allow simultaneous logins from different
              devices.
            guest_sponsorship: Details associated with guest sponsored splash.
            billing: Details associated with billing splash.
            sentry_enrollment: Systems Manager sentry enrollment splash settings.
            self_registration: Self-registration settings for splash with Meraki authentication.

        """
        if splash_timeout is not None:
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
            assert splash_timeout in options, (
                f'"splash_timeout" cannot be "{splash_timeout}", & must be set to one of: {options}'
            )
        if controller_disconnection_behavior is not None:
            options = ["default", "open", "restricted"]
            assert controller_disconnection_behavior in options, (
                f'"controller_disconnection_behavior" cannot be "{controller_disconnection_behavior}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "splash", "settings"],
            "operation": "update_network_wireless_ssid_splash_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/splash/settings"

        payload = {}
        if splash_url is not None:
            payload["splashUrl"] = splash_url
        if use_splash_url is not None:
            payload["useSplashUrl"] = use_splash_url
        if splash_timeout is not None:
            payload["splashTimeout"] = splash_timeout
        if redirect_url is not None:
            payload["redirectUrl"] = redirect_url
        if use_redirect_url is not None:
            payload["useRedirectUrl"] = use_redirect_url
        if welcome_message is not None:
            payload["welcomeMessage"] = welcome_message
        if theme_id is not None:
            payload["themeId"] = theme_id
        if splash_logo is not None:
            payload["splashLogo"] = splash_logo
        if splash_image is not None:
            payload["splashImage"] = splash_image
        if splash_prepaid_front is not None:
            payload["splashPrepaidFront"] = splash_prepaid_front
        if block_all_traffic_before_sign_on is not None:
            payload["blockAllTrafficBeforeSignOn"] = block_all_traffic_before_sign_on
        if controller_disconnection_behavior is not None:
            payload["controllerDisconnectionBehavior"] = controller_disconnection_behavior
        if allow_simultaneous_logins is not None:
            payload["allowSimultaneousLogins"] = allow_simultaneous_logins
        if guest_sponsorship is not None:
            payload["guestSponsorship"] = guest_sponsorship
        if billing is not None:
            payload["billing"] = billing
        if sentry_enrollment is not None:
            payload["sentryEnrollment"] = sentry_enrollment
        if self_registration is not None:
            payload["selfRegistration"] = self_registration

        return self._session.put(metadata, resource, payload)

    def update_network_wireless_ssid_traffic_shaping_rules(
        self,
        network_id: str,
        number: str,
        *,
        traffic_shaping_enabled: bool | None = None,
        default_rules_enabled: bool | None = None,
        rules: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the traffic shaping rules for an SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-traffic-shaping-rules

        Args:
            network_id: Network ID.
            number: Number.
            traffic_shaping_enabled: Whether traffic shaping rules are applied to clients on your
              SSID.
            default_rules_enabled: Whether default traffic shaping rules are enabled (true) or
              disabled (false). There are 4 default rules, which can be seen on your
              network's traffic shaping page. Note that default rules count against the
              rule limit of 8.
            rules: An array of traffic shaping rules. Rules are applied in the order that they are
              specified in. An empty list (or null) means no rules. Note that you are
              allowed a maximum of 8 rules.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "trafficShaping", "rules"],
            "operation": "update_network_wireless_ssid_traffic_shaping_rules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/trafficShaping/rules"

        payload = {}
        if traffic_shaping_enabled is not None:
            payload["trafficShapingEnabled"] = traffic_shaping_enabled
        if default_rules_enabled is not None:
            payload["defaultRulesEnabled"] = default_rules_enabled
        if rules is not None:
            payload["rules"] = rules

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_ssid_traffic_shaping_rules(
        self, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """Display the traffic shaping settings for a SSID on an MR network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-traffic-shaping-rules

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "trafficShaping", "rules"],
            "operation": "get_network_wireless_ssid_traffic_shaping_rules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/trafficShaping/rules"

        return self._session.get(metadata, resource)

    def get_network_wireless_ssid_vpn(self, network_id: str, number: str) -> dict[str, Any] | None:
        """List the VPN settings for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-vpn

        Args:
            network_id: Network ID.
            number: Number.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "vpn"],
            "operation": "get_network_wireless_ssid_vpn",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/vpn"

        return self._session.get(metadata, resource)

    def update_network_wireless_ssid_vpn(
        self,
        network_id: str,
        number: str,
        *,
        concentrator: dict | None = None,
        split_tunnel: dict | None = None,
        failover: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the VPN settings for the SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-vpn

        Args:
            network_id: Network ID.
            number: Number.
            concentrator: The VPN concentrator settings for this SSID.
            split_tunnel: The VPN split tunnel settings for this SSID.
            failover: Secondary VPN concentrator settings. This is only used when two VPN
              concentrators are configured on the SSID.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "vpn"],
            "operation": "update_network_wireless_ssid_vpn",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{network_id}/wireless/ssids/{number}/vpn"

        payload = {}
        if concentrator is not None:
            payload["concentrator"] = concentrator
        if split_tunnel is not None:
            payload["splitTunnel"] = split_tunnel
        if failover is not None:
            payload["failover"] = failover

        return self._session.put(metadata, resource, payload)

    def get_network_wireless_usage_history(
        self,
        network_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
        auto_resolution: bool | None = None,
        client_id: str | None = None,
        device_serial: str | None = None,
        ap_tag: str | None = None,
        band: str | None = None,
        ssid: int | None = None,
    ) -> dict[str, Any] | None:
        """Return AP usage over time for a device or network client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-usage-history

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            auto_resolution: Automatically select a data resolution based on the given timespan;
              this overrides the value specified by the 'resolution' parameter. The
              default setting is false.
            client_id: Filter results by network client to return per-device AP usage over time
              inner joined by the queried client's connection history.
            device_serial: Filter results by device. Requires :band.
            ap_tag: Filter results by AP tag; either :clientId or :deviceSerial must be jointly
              specified.
            band: Filter results by band (either '2.4', '5' or '6').
            ssid: Filter results by SSID number.

        """
        if band is not None:
            options = ["2.4", "5", "6"]
            assert band in options, f'"band" cannot be "{band}", & must be set to one of: {options}'

        metadata = {
            "tags": ["wireless", "monitor", "usageHistory"],
            "operation": "get_network_wireless_usage_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/usageHistory"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution
        if auto_resolution is not None:
            params["autoResolution"] = auto_resolution
        if client_id is not None:
            params["clientId"] = client_id
        if device_serial is not None:
            params["deviceSerial"] = device_serial
        if ap_tag is not None:
            params["apTag"] = ap_tag
        if band is not None:
            params["band"] = band
        if ssid is not None:
            params["ssid"] = ssid

        return self._session.get(metadata, resource, params)

    def update_network_wireless_zigbee(
        self,
        network_id: str,
        *,
        enabled: bool | None = None,
        iot_controller: dict | None = None,
        lock_management: dict | None = None,
        defaults: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update Zigbee Configs for specified network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-zigbee

        Args:
            network_id: Network ID.
            enabled: To enable/disable Zigbee on the network.
            iot_controller: Zigbee's IoT controller details.
            lock_management: Login Credentials of on-premises lock management.
            defaults: Default Settings for Zigbee Devices.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee"],
            "operation": "update_network_wireless_zigbee",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/wireless/zigbee"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if iot_controller is not None:
            payload["iotController"] = iot_controller
        if lock_management is not None:
            payload["lockManagement"] = lock_management
        if defaults is not None:
            payload["defaults"] = defaults

        return self._session.put(metadata, resource, payload)

    def get_organization_wireless_air_marshal_rules(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Returns the current Air Marshal rules for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-air-marshal-rules

        Args:
            organization_id: Organization ID.
            network_ids: (optional) The set of network IDs to include.
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
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "get_organization_wireless_air_marshal_rules",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/airMarshal/rules"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_air_marshal_settings_by_network(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Returns the current Air Marshal settings for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-air-marshal-settings-by-network

        Args:
            organization_id: Organization ID.
            network_ids: The network IDs to include in the result set.
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
            "tags": ["wireless", "configure", "airMarshal", "settings", "byNetwork"],
            "operation": "get_organization_wireless_air_marshal_settings_by_network",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/airMarshal/settings/byNetwork"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_clients_overview_by_device(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        campus_gateway_cluster_ids: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List access point client count at the moment in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-overview-by-device

        Args:
            organization_id: Organization ID.
            network_ids: Optional parameter to filter access points client counts by network ID.
              This filter uses multiple exact matches.
            serials: Optional parameter to filter access points client counts by its serial numbers.
              This filter uses multiple exact matches.
            campus_gateway_cluster_ids: Optional parameter to filter access points client counts by
              MCG cluster IDs. This filter uses multiple exact matches.
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
            "tags": ["wireless", "monitor", "clients", "overview", "byDevice"],
            "operation": "get_organization_wireless_clients_overview_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/clients/overview/byDevice"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if campus_gateway_cluster_ids is not None:
            params["campusGatewayClusterIds[]"] = campus_gateway_cluster_ids
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_channel_utilization_by_device(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        interval: int | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get average channel utilization for all bands in a network, split by AP.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-device

        Args:
            organization_id: Organization ID.
            network_ids: Filter results by network.
            serials: Filter results by device.
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 90 days. The default is 7 days.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              600, 3600, 7200, 14400, 21600. The default is 3600.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "monitor", "devices", "channelUtilization", "byDevice"],
            "operation": "get_organization_wireless_devices_channel_utilization_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/channelUtilization/byDevice"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if interval is not None:
            params["interval"] = interval

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_channel_utilization_by_network(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        interval: int | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get average channel utilization across all bands for all networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-network

        Args:
            organization_id: Organization ID.
            network_ids: Filter results by network.
            serials: Filter results by device.
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 90 days. The default is 7 days.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              600, 3600, 7200, 14400, 21600. The default is 3600.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "monitor", "devices", "channelUtilization", "byNetwork"],
            "operation": "get_organization_wireless_devices_channel_utilization_by_network",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/channelUtilization/byNetwork"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if interval is not None:
            params["interval"] = interval

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_channel_utilization_history_by_device_by_interval(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        interval: int | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get a time-series of average channel utilization for all bands, segmented by device.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-history-by-device-by-interval

        Args:
            organization_id: Organization ID.
            network_ids: Filter results by network.
            serials: Filter results by device.
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              600, 3600, 7200, 14400, 21600. The default is 3600.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/channelUtilization/history/byDevice/byInterval"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if interval is not None:
            params["interval"] = interval

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_channel_utilization_history_by_network_by_interval(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        interval: int | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get a time-series of average channel utilization for all bands.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-history-by-network-by-interval

        Args:
            organization_id: Organization ID.
            network_ids: Filter results by network.
            serials: Filter results by device.
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
            interval: The time interval in seconds for returned data. The valid intervals are: 300,
              600, 3600, 7200, 14400, 21600. The default is 3600.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/channelUtilization/history/byNetwork/byInterval"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if interval is not None:
            params["interval"] = interval

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_ethernet_statuses(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the most recent Ethernet link speed, duplex, aggregation and power mode and status information for wireless devices.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-ethernet-statuses

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: A list of Meraki network IDs to filter results to contain only specified
              networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "monitor", "devices", "ethernet", "statuses"],
            "operation": "get_organization_wireless_devices_ethernet_statuses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/ethernet/statuses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_packet_loss_by_client(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        ssids: list | None = None,
        bands: list | None = None,
        macs: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get average packet loss for the given timespan for all clients in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-client

        Args:
            organization_id: Organization ID.
            network_ids: Filter results by network.
            ssids: Filter results by SSID number.
            bands: Filter results by band. Valid bands are: 2.4, 5, and 6.
            macs: Filter results by client mac address(es).
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 5 minutes and be less than or
              equal to 90 days. The default is 7 days.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byClient"],
            "operation": "get_organization_wireless_devices_packet_loss_by_client",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/packetLoss/byClient"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if ssids is not None:
            params["ssids[]"] = ssids
        if bands is not None:
            params["bands[]"] = bands
        if macs is not None:
            params["macs[]"] = macs
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_packet_loss_by_device(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        ssids: list | None = None,
        bands: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get average packet loss for the given timespan for all devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-device

        Args:
            organization_id: Organization ID.
            network_ids: Filter results by network.
            serials: Filter results by device.
            ssids: Filter results by SSID number.
            bands: Filter results by band. Valid bands are: 2.4, 5, and 6.
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 5 minutes and be less than or
              equal to 90 days. The default is 7 days.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byDevice"],
            "operation": "get_organization_wireless_devices_packet_loss_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/packetLoss/byDevice"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if ssids is not None:
            params["ssids[]"] = ssids
        if bands is not None:
            params["bands[]"] = bands
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_packet_loss_by_network(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        ssids: list | None = None,
        bands: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get average packet loss for the given timespan for all networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-network

        Args:
            organization_id: Organization ID.
            network_ids: Filter results by network.
            serials: Filter results by device.
            ssids: Filter results by SSID number.
            bands: Filter results by band. Valid bands are: 2.4, 5, and 6.
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 90 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 5 minutes and be less than or
              equal to 90 days. The default is 7 days.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byNetwork"],
            "operation": "get_organization_wireless_devices_packet_loss_by_network",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/packetLoss/byNetwork"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if ssids is not None:
            params["ssids[]"] = ssids
        if bands is not None:
            params["bands[]"] = bands
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_power_mode_history(
        self,
        organization_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return a record of power mode changes for wireless devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-power-mode-history

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 1 day
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 1 day after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 1 day. The default is 1 day.
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
            network_ids: Optional parameter to filter the result set by the included set of network
              IDs.
            serials: Optional parameter to filter device availabilities history by device serial
              numbers.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "monitor", "devices", "power", "mode", "history"],
            "operation": "get_organization_wireless_devices_power_mode_history",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/power/mode/history"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_radsec_certificates_authorities(
        self, organization_id: str, *, certificate_authority_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Query for details on the organization's RADSEC device Certificate Authority certificates (CAs).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities

        Args:
            organization_id: Organization ID.
            certificate_authority_ids: Optional parameter to filter CAs by one or more CA IDs. All
              returned CAs will have an ID that is an exact match.

        """
        metadata = {
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "get_organization_wireless_devices_radsec_certificates_authorities",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/wireless/devices/radsec/certificates/authorities"
        )

        params = {}
        if certificate_authority_ids is not None:
            params["certificateAuthorityIds[]"] = certificate_authority_ids

        return self._session.get(metadata, resource, params)

    def update_organization_wireless_devices_radsec_certificates_authorities(
        self,
        organization_id: str,
        *,
        status: str | None = None,
        certificate_authority_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Update an organization's RADSEC device Certificate Authority (CA) state.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-devices-radsec-certificates-authorities

        Args:
            organization_id: Organization ID.
            status: The "status" to update the Certificate Authority to. Only valid option is
              "trusted".
            certificate_authority_id: The ID of the Certificate Authority to update.

        """
        metadata = {
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "update_organization_wireless_devices_radsec_certificates_authorities",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/wireless/devices/radsec/certificates/authorities"
        )

        payload = {}
        if status is not None:
            payload["status"] = status
        if certificate_authority_id is not None:
            payload["certificateAuthorityId"] = certificate_authority_id

        return self._session.put(metadata, resource, payload)

    def create_organization_wireless_devices_radsec_certificates_authority(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """Create an organization's RADSEC device Certificate Authority (CA).

        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-devices-radsec-certificates-authority

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "create_organization_wireless_devices_radsec_certificates_authority",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/wireless/devices/radsec/certificates/authorities"
        )

        return self._session.post(metadata, resource)

    def get_organization_wireless_devices_radsec_certificates_authorities_crls(
        self, organization_id: str, *, certificate_authority_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Query for certificate revocation list (CRL) for the organization's RADSEC device Certificate Authorities (CAs).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities-crls

        Args:
            organization_id: Organization ID.
            certificate_authority_ids: Optional parameter to filter CAs by one or more CA IDs. All
              returned CAs will have an ID that is an exact match.

        """
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/radsec/certificates/authorities/crls"

        params = {}
        if certificate_authority_ids is not None:
            params["certificateAuthorityIds[]"] = certificate_authority_ids

        return self._session.get(metadata, resource, params)

    def get_organization_wireless_devices_radsec_certificates_authorities_crls_deltas(
        self, organization_id: str, *, certificate_authority_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Query for all delta certificate revocation list (CRL) for the organization's RADSEC device Certificate Authority (CA) with the given id.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities-crls-deltas

        Args:
            organization_id: Organization ID.
            certificate_authority_ids: Parameter to filter CAs by one or more CA IDs. All returned
              CAs will have an ID that is an exact match.

        """
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/radsec/certificates/authorities/crls/deltas"

        params = {}
        if certificate_authority_ids is not None:
            params["certificateAuthorityIds[]"] = certificate_authority_ids

        return self._session.get(metadata, resource, params)

    def get_organization_wireless_devices_system_cpu_load_history(
        self,
        organization_id: str,
        *,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the CPU Load history for a list of wireless devices in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-system-cpu-load-history

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 1 day
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 1 day after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 1 day. The default is 1 day.
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
            network_ids: Optional parameter to filter the result set by the included set of network
              IDs.
            serials: Optional parameter to filter device availabilities history by device serial
              numbers.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "monitor", "devices", "system", "cpu", "load", "history"],
            "operation": "get_organization_wireless_devices_system_cpu_load_history",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/system/cpu/load/history"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_devices_wireless_controllers_by_device(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        controller_serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List of Catalyst access points information.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-wireless-controllers-by-device

        Args:
            organization_id: Organization ID.
            network_ids: Optional parameter to filter access points by network ID. This filter uses
              multiple exact matches.
            serials: Optional parameter to filter access points by its cloud ID. This filter uses
              multiple exact matches.
            controller_serials: Optional parameter to filter access points by its wireless LAN
              controller cloud ID. This filter uses multiple exact matches.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
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
            "tags": ["wireless", "monitor", "devices", "wirelessControllers", "byDevice"],
            "operation": "get_organization_wireless_devices_wireless_controllers_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/devices/wirelessControllers/byDevice"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if controller_serials is not None:
            params["controllerSerials[]"] = controller_serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_location_scanning_by_network(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return scanning API settings.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-location-scanning-by-network

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 250. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter scanning settings by network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "byNetwork"],
            "operation": "get_organization_wireless_location_scanning_by_network",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/location/scanning/byNetwork"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_location_scanning_receivers(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return scanning API receivers.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-location-scanning-receivers

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 250. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter scanning API receivers by network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "get_organization_wireless_location_scanning_receivers",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/location/scanning/receivers"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_wireless_location_scanning_receiver(
        self,
        organization_id: str,
        network: dict,
        url: str,
        version: str,
        radio: dict,
        shared_secret: str,
    ) -> dict[str, Any] | None:
        """Add new receiver for scanning API.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-location-scanning-receiver

        Args:
            organization_id: Organization ID.
            network: Add scanning API receiver for network.
            url: Receiver Url.
            version: Scanning API Version.
            radio: Add scanning API Radio.
            shared_secret: Secret Value for Receiver.

        """
        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "create_organization_wireless_location_scanning_receiver",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/location/scanning/receivers"

        payload = {}
        if network is not None:
            payload["network"] = network
        if url is not None:
            payload["url"] = url
        if version is not None:
            payload["version"] = version
        if radio is not None:
            payload["radio"] = radio
        if shared_secret is not None:
            payload["sharedSecret"] = shared_secret

        return self._session.post(metadata, resource, payload)

    def update_organization_wireless_location_scanning_receiver(
        self,
        organization_id: str,
        receiver_id: str,
        *,
        url: str | None = None,
        version: str | None = None,
        radio: dict | None = None,
    ) -> dict[str, Any] | None:
        """Change scanning API receiver settings.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-location-scanning-receiver

        Args:
            organization_id: Organization ID.
            receiver_id: Receiver ID.
            url: Receiver Url.
            version: Scanning API Version.
            radio: Add scanning API Radio.

        """
        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "update_organization_wireless_location_scanning_receiver",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        receiver_id = urllib.parse.quote(str(receiver_id), safe="")
        resource = (
            f"/organizations/{organization_id}/wireless/location/scanning/receivers/{receiver_id}"
        )

        payload = {}
        if url is not None:
            payload["url"] = url
        if version is not None:
            payload["version"] = version
        if radio is not None:
            payload["radio"] = radio

        return self._session.put(metadata, resource, payload)

    def delete_organization_wireless_location_scanning_receiver(
        self, organization_id: str, receiver_id: str
    ) -> None:
        """Delete a scanning API receiver.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-location-scanning-receiver

        Args:
            organization_id: Organization ID.
            receiver_id: Receiver ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "delete_organization_wireless_location_scanning_receiver",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        receiver_id = urllib.parse.quote(str(receiver_id), safe="")
        resource = (
            f"/organizations/{organization_id}/wireless/location/scanning/receivers/{receiver_id}"
        )

        return self._session.delete(metadata, resource)

    def get_organization_wireless_mqtt_settings(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return MQTT Settings for networks.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-mqtt-settings

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 250. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter mqtt settings by network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "configure", "mqtt", "settings"],
            "operation": "get_organization_wireless_mqtt_settings",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/mqtt/settings"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def update_organization_wireless_mqtt_settings(
        self,
        organization_id: str,
        network: dict,
        mqtt: dict,
        *,
        ble: dict | None = None,
        wifi: dict | None = None,
    ) -> dict[str, Any] | None:
        """Add new broker config for wireless MQTT.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-mqtt-settings

        Args:
            organization_id: Organization ID.
            network: Add MQTT Settings for network.
            mqtt: MQTT Settings for network.
            ble: MQTT BLE Settings for network.
            wifi: MQTT Wi-Fi Settings for network.

        """
        metadata = {
            "tags": ["wireless", "configure", "mqtt", "settings"],
            "operation": "update_organization_wireless_mqtt_settings",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/mqtt/settings"

        payload = {}
        if network is not None:
            payload["network"] = network
        if mqtt is not None:
            payload["mqtt"] = mqtt
        if ble is not None:
            payload["ble"] = ble
        if wifi is not None:
            payload["wifi"] = wifi

        return self._session.put(metadata, resource, payload)

    def recalculate_organization_wireless_radio_auto_rf_channels(
        self, organization_id: str, network_ids: list
    ) -> dict[str, Any] | None:
        """Recalculates automatically assigned channels for every AP within specified the specified network(s).

        https://developer.cisco.com/meraki/api-v1/#!recalculate-organization-wireless-radio-auto-rf-channels

        Args:
            organization_id: Organization ID.
            network_ids: A list of network ids (limit: 15).

        """
        metadata = {
            "tags": ["wireless", "configure", "radio", "autoRf", "channels"],
            "operation": "recalculate_organization_wireless_radio_auto_rf_channels",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/radio/autoRf/channels/recalculate"

        payload = {}
        if network_ids is not None:
            payload["networkIds"] = network_ids

        return self._session.post(metadata, resource, payload)

    def get_organization_wireless_rf_profiles_assignments_by_device(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        product_types: list | None = None,
        name: str | None = None,
        mac: str | None = None,
        serial: str | None = None,
        model: str | None = None,
        macs: list | None = None,
        serials: list | None = None,
        models: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the RF profiles of an organization by device.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-rf-profiles-assignments-by-device

        Args:
            organization_id: Organization ID.
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
            network_ids: Optional parameter to filter devices by network.
            product_types: Optional parameter to filter devices by product type. Valid types are
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
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "configure", "rfProfiles", "assignments", "byDevice"],
            "operation": "get_organization_wireless_rf_profiles_assignments_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/rfProfiles/assignments/byDevice"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if product_types is not None:
            params["productTypes[]"] = product_types
        if name is not None:
            params["name"] = name
        if mac is not None:
            params["mac"] = mac
        if serial is not None:
            params["serial"] = serial
        if model is not None:
            params["model"] = model
        if macs is not None:
            params["macs[]"] = macs
        if serials is not None:
            params["serials[]"] = serials
        if models is not None:
            params["models[]"] = models

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_ssids_firewall_isolation_allowlist_entries(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        ssids: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the L2 isolation allow list MAC entry in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-firewall-isolation-allowlist-entries

        Args:
            organization_id: Organization ID.
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
            network_ids: networkIds array to filter out results.
            ssids: ssids number array to filter out results.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

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
            "operation": "get_organization_wireless_ssids_firewall_isolation_allowlist_entries",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/wireless/ssids/firewall/isolation/allowlist/entries"
        )

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if ssids is not None:
            params["ssids[]"] = ssids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self,
        organization_id: str,
        client: dict,
        ssid: dict,
        network: dict,
        *,
        description: str | None = None,
    ) -> dict[str, Any] | None:
        """Create isolation allow list MAC entry for this organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-ssids-firewall-isolation-allowlist-entry

        Args:
            organization_id: Organization ID.
            description: The description of mac address.
            client: The client of allowlist.
            ssid: The SSID that allowlist belongs to.
            network: The Network that allowlist belongs to.

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
            "operation": "create_organization_wireless_ssids_firewall_isolation_allowlist_entry",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/wireless/ssids/firewall/isolation/allowlist/entries"
        )

        payload = {}
        if description is not None:
            payload["description"] = description
        if client is not None:
            payload["client"] = client
        if ssid is not None:
            payload["ssid"] = ssid
        if network is not None:
            payload["network"] = network

        return self._session.post(metadata, resource, payload)

    def delete_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self, organization_id: str, entry_id: str
    ) -> None:
        """Destroy isolation allow list MAC entry for this organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-ssids-firewall-isolation-allowlist-entry

        Args:
            organization_id: Organization ID.
            entry_id: Entry ID.

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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        entry_id = urllib.parse.quote(str(entry_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/ssids/firewall/isolation/allowlist/entries/{entry_id}"

        return self._session.delete(metadata, resource)

    def update_organization_wireless_ssids_firewall_isolation_allowlist_entry(
        self,
        organization_id: str,
        entry_id: str,
        *,
        description: str | None = None,
        client: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update isolation allow list MAC entry info.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-ssids-firewall-isolation-allowlist-entry

        Args:
            organization_id: Organization ID.
            entry_id: Entry ID.
            description: The description of mac address.
            client: The client of allowlist.

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
            "operation": "update_organization_wireless_ssids_firewall_isolation_allowlist_entry",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        entry_id = urllib.parse.quote(str(entry_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/ssids/firewall/isolation/allowlist/entries/{entry_id}"

        payload = {}
        if description is not None:
            payload["description"] = description
        if client is not None:
            payload["client"] = client

        return self._session.put(metadata, resource, payload)

    def get_organization_wireless_ssids_open_roaming_by_network(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        include_disabled_ssids: bool | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Returns an array of objects, each containing SSID OpenRoaming configs for the corresponding network.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-open-roaming-by-network

        Args:
            organization_id: Organization ID.
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
            network_ids: Optional parameter to filter OpenRoaming configuration by Network Id.
            include_disabled_ssids: Optional parameter to include OpenRoaming configuration for
              disabled ssids.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "configure", "ssids", "openRoaming", "byNetwork"],
            "operation": "get_organization_wireless_ssids_open_roaming_by_network",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/ssids/openRoaming/byNetwork"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if include_disabled_ssids is not None:
            params["includeDisabledSsids"] = include_disabled_ssids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_ssids_statuses_by_device(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serials: list | None = None,
        bssids: list | None = None,
        hide_disabled: bool | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List status information of all BSSIDs in your organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-statuses-by-device

        Args:
            organization_id: Organization ID.
            network_ids: Optional parameter to filter the result set by the included set of network
              IDs.
            serials: A list of serial numbers. The returned devices will be filtered to only include
              these serials.
            bssids: A list of BSSIDs. The returned devices will be filtered to only include these
              BSSIDs.
            hide_disabled: If true, the returned devices will not include disabled SSIDs. (default:
              true).
            per_page: The number of entries per page returned. Acceptable range is 3 - 500. Default
              is 100.
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
            "tags": ["wireless", "monitor", "ssids", "statuses", "byDevice"],
            "operation": "get_organization_wireless_ssids_statuses_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/ssids/statuses/byDevice"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if bssids is not None:
            params["bssids[]"] = bssids
        if hide_disabled is not None:
            params["hideDisabled"] = hide_disabled
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_zigbee_by_network(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return list of Zigbee configs.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-by-network

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Filter by specified Network IDs.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "byNetwork"],
            "operation": "get_organization_wireless_zigbee_by_network",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/zigbee/byNetwork"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_zigbee_devices(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        is_enrolled: bool | None = None,
        search: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the Zigbee wireless devices for an organization or the supplied network(s).

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-devices

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 10.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Parameter of networks you want the zigbee devices for. E.g.:
              networkIds[]=N_12345678&networkIds[]=N_3456.
            is_enrolled: Filter devices based on if they are enrolled or not.
            search: Filter devices by their name, tag or serial.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "devices"],
            "operation": "get_organization_wireless_zigbee_devices",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/zigbee/devices"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if is_enrolled is not None:
            params["isEnrolled"] = is_enrolled
        if search is not None:
            params["search"] = search

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def update_organization_wireless_zigbee_device(
        self, organization_id: str, id_: str, enrolled: bool, *, channel: str | None = None
    ) -> dict[str, Any] | None:
        """Endpoint to update zigbee gateways.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-zigbee-device

        Args:
            organization_id: Organization ID.
            id_: ID.
            enrolled: Parameter to enroll or unenroll the zigbee devices.
            channel: The new channel for the zigbee device.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "devices"],
            "operation": "update_organization_wireless_zigbee_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        resource = f"/organizations/{organization_id}/wireless/zigbee/devices/{id_}"

        payload = {}
        if enrolled is not None:
            payload["enrolled"] = enrolled
        if channel is not None:
            payload["channel"] = channel

        return self._session.put(metadata, resource, payload)

    def create_organization_wireless_zigbee_disenrollment(
        self, organization_id: str, *, door_lock_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Enqueue a job to start disenrolling door locks on zigbee configured wireless devices.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-zigbee-disenrollment

        Args:
            organization_id: Organization ID.
            door_lock_ids: A list of Meraki door lock ids to disenroll from the device.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "disenrollments"],
            "operation": "create_organization_wireless_zigbee_disenrollment",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/zigbee/disenrollments"

        payload = {}
        if door_lock_ids is not None:
            payload["doorLockIds"] = door_lock_ids

        return self._session.post(metadata, resource, payload)

    def get_organization_wireless_zigbee_disenrollment(
        self, organization_id: str, disenrollment_id: str
    ) -> dict[str, Any] | None:
        """Return a disenrollment.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-disenrollment

        Args:
            organization_id: Organization ID.
            disenrollment_id: Disenrollment ID.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "disenrollments"],
            "operation": "get_organization_wireless_zigbee_disenrollment",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        disenrollment_id = urllib.parse.quote(str(disenrollment_id), safe="")
        resource = (
            f"/organizations/{organization_id}/wireless/zigbee/disenrollments/{disenrollment_id}"
        )

        return self._session.get(metadata, resource)

    def get_organization_wireless_zigbee_door_locks(
        self,
        organization_id: str,
        *,
        network_ids: list | None = None,
        serial: str | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the list of door locks for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-door-locks

        Args:
            organization_id: Organization ID.
            network_ids: Filter by specified Network IDs.
            serial: Filter by device serial.
            per_page: The number of entries per page returned. Acceptable range is 3 - 500. Default
              is 50.
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
            "tags": ["wireless", "configure", "zigbee", "doorLocks"],
            "operation": "get_organization_wireless_zigbee_door_locks",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/zigbee/doorLocks"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serial is not None:
            params["serial"] = serial
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def update_organization_wireless_zigbee_door_lock(
        self, organization_id: str, door_lock_id: str, *, name: str | None = None
    ) -> dict[str, Any] | None:
        """Endpoint to batch update door locks params.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-zigbee-door-lock

        Args:
            organization_id: Organization ID.
            door_lock_id: Door lock ID.
            name: Door lock name to update.

        """
        metadata = {
            "tags": ["wireless", "configure", "zigbee", "doorLocks"],
            "operation": "update_organization_wireless_zigbee_door_lock",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        door_lock_id = urllib.parse.quote(str(door_lock_id), safe="")
        resource = f"/organizations/{organization_id}/wireless/zigbee/doorLocks/{door_lock_id}"

        payload = {}
        if name is not None:
            payload["name"] = name

        return self._session.put(metadata, resource, payload)
