"""Sensor API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncSensor:
    """Sensor class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_device_sensor_commands(
        self,
        *,
        serial: str,
        operations: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Returns a historical log of all commands.

        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-commands

        Args:
            serial: Serial.
            operations: Optional parameter to filter commands by operation. Allowed values are
              disableDownstreamPower, enableDownstreamPower, cycleDownstreamPower, and
              refreshData.
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
            sort_order: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'descending'.
            t0: The beginning of the timespan for the data. The maximum lookback period is 30 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 30 days. The default is 30 days.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["sensor", "configure", "commands"],
            "operation": "get_device_sensor_commands",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/sensor/commands"

        params = {}
        if operations is not None:
            params["operations[]"] = operations
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

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_device_sensor_command(self, *, serial: str, operation: str) -> dict[str, Any] | None:
        """Sends a command to a sensor.

        https://developer.cisco.com/meraki/api-v1/#!create-device-sensor-command

        Args:
            serial: Serial.
            operation: Operation to run on the sensor. 'enableDownstreamPower',
              'disableDownstreamPower', and 'cycleDownstreamPower' turn power on/off to
              the device that is connected downstream of an MT40 power monitor.
              'refreshData' causes an MT15 or MT40 device to upload its latest readings
              so that they are immediately available in the Dashboard API.

        """
        if operation is not None:
            options = [
                "cycleDownstreamPower",
                "disableDownstreamPower",
                "enableDownstreamPower",
                "refreshData",
            ]
            assert operation in options, (
                f'"operation" cannot be "{operation}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["sensor", "configure", "commands"],
            "operation": "create_device_sensor_command",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/sensor/commands"

        payload = {}
        if operation is not None:
            payload["operation"] = operation

        return self._session.post(metadata, resource, payload)

    def get_device_sensor_command(self, *, serial: str, command_id: str) -> dict[str, Any] | None:
        """Returns information about the command's execution, including the status.

        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-command

        Args:
            serial: Serial.
            command_id: Command ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "commands"],
            "operation": "get_device_sensor_command",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        command_id = urllib.parse.quote(str(command_id), safe="")
        resource = f"/devices/{serial}/sensor/commands/{command_id}"

        return self._session.get(metadata, resource)

    def get_device_sensor_relationships(self, *, serial: str) -> dict[str, Any] | None:
        """List the sensor roles for a given sensor or camera device.

        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-relationships

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["sensor", "configure", "relationships"],
            "operation": "get_device_sensor_relationships",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/sensor/relationships"

        return self._session.get(metadata, resource)

    def update_device_sensor_relationships(
        self, *, serial: str, livestream: dict | None = None
    ) -> dict[str, Any] | None:
        """Assign one or more sensor roles to a given sensor or camera device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-sensor-relationships

        Args:
            serial: Serial.
            livestream: A role defined between an MT sensor and an MV camera that adds the camera's
              livestream to the sensor's details page. Snapshots from the camera will
              also appear in alert notifications that the sensor triggers.

        """
        metadata = {
            "tags": ["sensor", "configure", "relationships"],
            "operation": "update_device_sensor_relationships",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/sensor/relationships"

        payload = {}
        if livestream is not None:
            payload["livestream"] = livestream

        return self._session.put(metadata, resource, payload)

    def get_network_sensor_alerts_current_overview_by_metric(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return an overview of currently alerting sensors by metric.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-current-overview-by-metric

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["sensor", "monitor", "alerts", "current", "overview", "byMetric"],
            "operation": "get_network_sensor_alerts_current_overview_by_metric",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/current/overview/byMetric"

        return self._session.get(metadata, resource)

    def get_network_sensor_alerts_overview_by_metric(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        interval: int | None = None,
    ) -> dict[str, Any] | None:
        """Return an overview of alert occurrences over a timespan, by metric.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-overview-by-metric

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 731 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 366 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 366 days. The default is 7 days. If
              interval is provided, the timespan will be autocalculated.
            interval: The time interval in seconds for returned data. The valid intervals are: 900,
              3600, 86400, 604800, 2592000. The default is 604800. Interval is
              calculated if time params are provided.

        """
        metadata = {
            "tags": ["sensor", "monitor", "alerts", "overview", "byMetric"],
            "operation": "get_network_sensor_alerts_overview_by_metric",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/overview/byMetric"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if interval is not None:
            params["interval"] = interval

        return self._session.get(metadata, resource, params)

    def get_network_sensor_alerts_profiles(self, *, network_id: str) -> dict[str, Any] | None:
        """Lists all sensor alert profiles for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profiles

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "get_network_sensor_alerts_profiles",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles"

        return self._session.get(metadata, resource)

    def create_network_sensor_alerts_profile(
        self,
        *,
        network_id: str,
        name: str,
        conditions: list,
        schedule: dict | None = None,
        recipients: dict | None = None,
        serials: list | None = None,
        include_sensor_url: bool | None = None,
        message: str | None = None,
    ) -> dict[str, Any] | None:
        """Creates a sensor alert profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            name: Name of the sensor alert profile.
            schedule: The sensor schedule to use with the alert profile.
            conditions: List of conditions that will cause the profile to send an alert.
            recipients: List of recipients that will receive the alert.
            serials: List of device serials assigned to this sensor alert profile.
            include_sensor_url: Include dashboard link to sensor in messages (default: true).
            message: A custom message that will appear in email and text message alerts.

        """
        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "create_network_sensor_alerts_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if schedule is not None:
            payload["schedule"] = schedule
        if conditions is not None:
            payload["conditions"] = conditions
        if recipients is not None:
            payload["recipients"] = recipients
        if serials is not None:
            payload["serials"] = serials
        if include_sensor_url is not None:
            payload["includeSensorUrl"] = include_sensor_url
        if message is not None:
            payload["message"] = message

        return self._session.post(metadata, resource, payload)

    def get_network_sensor_alerts_profile(
        self, *, network_id: str, id_: str
    ) -> dict[str, Any] | None:
        """Show details of a sensor alert profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            id_: ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "get_network_sensor_alerts_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles/{id_}"

        return self._session.get(metadata, resource)

    def update_network_sensor_alerts_profile(
        self,
        *,
        network_id: str,
        id_: str,
        name: str | None = None,
        schedule: dict | None = None,
        conditions: list | None = None,
        recipients: dict | None = None,
        serials: list | None = None,
        include_sensor_url: bool | None = None,
        message: str | None = None,
    ) -> dict[str, Any] | None:
        """Updates a sensor alert profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            id_: ID.
            name: Name of the sensor alert profile.
            schedule: The sensor schedule to use with the alert profile.
            conditions: List of conditions that will cause the profile to send an alert.
            recipients: List of recipients that will receive the alert.
            serials: List of device serials assigned to this sensor alert profile.
            include_sensor_url: Include dashboard link to sensor in messages (default: true).
            message: A custom message that will appear in email and text message alerts.

        """
        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "update_network_sensor_alerts_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles/{id_}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if schedule is not None:
            payload["schedule"] = schedule
        if conditions is not None:
            payload["conditions"] = conditions
        if recipients is not None:
            payload["recipients"] = recipients
        if serials is not None:
            payload["serials"] = serials
        if include_sensor_url is not None:
            payload["includeSensorUrl"] = include_sensor_url
        if message is not None:
            payload["message"] = message

        return self._session.put(metadata, resource, payload)

    def delete_network_sensor_alerts_profile(self, *, network_id: str, id_: str) -> None:
        """Deletes a sensor alert profile from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            id_: ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "delete_network_sensor_alerts_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles/{id_}"

        return self._session.delete(metadata, resource)

    def get_network_sensor_mqtt_brokers(self, *, network_id: str) -> dict[str, Any] | None:
        """List the sensor settings of all MQTT brokers for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-mqtt-brokers

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "mqttBrokers"],
            "operation": "get_network_sensor_mqtt_brokers",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/sensor/mqttBrokers"

        return self._session.get(metadata, resource)

    def get_network_sensor_mqtt_broker(
        self, *, network_id: str, mqtt_broker_id: str
    ) -> dict[str, Any] | None:
        """Return the sensor settings of an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "mqttBrokers"],
            "operation": "get_network_sensor_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/sensor/mqttBrokers/{mqtt_broker_id}"

        return self._session.get(metadata, resource)

    def update_network_sensor_mqtt_broker(
        self, *, network_id: str, mqtt_broker_id: str, enabled: bool
    ) -> dict[str, Any] | None:
        """Update the sensor settings of an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.
            enabled: Set to true to enable MQTT broker for sensor network.

        """
        metadata = {
            "tags": ["sensor", "configure", "mqttBrokers"],
            "operation": "update_network_sensor_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/sensor/mqttBrokers/{mqtt_broker_id}"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled

        return self._session.put(metadata, resource, payload)

    def get_network_sensor_relationships(self, *, network_id: str) -> dict[str, Any] | None:
        """List the sensor roles for devices in a given network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-relationships

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "relationships"],
            "operation": "get_network_sensor_relationships",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/sensor/relationships"

        return self._session.get(metadata, resource)

    def get_organization_sensor_gateways_connections_latest(
        self,
        *,
        organization_id: str,
        sensor_serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Returns latest sensor-gateway connectivity data.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-gateways-connections-latest

        Args:
            organization_id: Organization ID.
            sensor_serials: List of sensor serials to filter connectivity data by sensor.
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
            "tags": ["sensor", "monitor", "gateways", "connections", "latest"],
            "operation": "get_organization_sensor_gateways_connections_latest",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/sensor/gateways/connections/latest"

        params = {}
        if sensor_serials is not None:
            params["sensorSerials[]"] = sensor_serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_sensor_readings_history(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        metrics: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return all reported readings from sensors in a given timespan, sorted by timestamp.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history

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
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              and 6 hours from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days. The default is 2 hours.
            network_ids: Optional parameter to filter readings by network.
            serials: Optional parameter to filter readings by sensor.
            metrics: Types of sensor readings to retrieve. If no metrics are supplied, all available
              types of readings will be retrieved.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["sensor", "monitor", "readings", "history"],
            "operation": "get_organization_sensor_readings_history",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/sensor/readings/history"

        params = {}
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
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if metrics is not None:
            params["metrics[]"] = metrics

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_sensor_readings_latest(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        metrics: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the latest available reading for each metric from each sensor, sorted by sensor serial.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-latest

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
            network_ids: Optional parameter to filter readings by network.
            serials: Optional parameter to filter readings by sensor.
            metrics: Types of sensor readings to retrieve. If no metrics are supplied, all available
              types of readings will be retrieved.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["sensor", "monitor", "readings", "latest"],
            "operation": "get_organization_sensor_readings_latest",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/sensor/readings/latest"

        params = {}
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
        if metrics is not None:
            params["metrics[]"] = metrics

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
