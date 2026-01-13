"""Sensor API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.rest_session import RestSession


class Sensor:
    """Sensor class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
        self._session = session

    def get_device_sensor_commands(
        self, serial: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns a historical log of all commands.

        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-commands

        Args:
            serial: Serial.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            operations: Optional parameter to filter commands by operation. Allowed values are
              disableDownstreamPower, enableDownstreamPower, cycleDownstreamPower, and
              refreshData.
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
            sortOrder: Sorted order of entries. Order options are 'ascending' and 'descending'.
              Default is 'descending'.
            t0: The beginning of the timespan for the data. The maximum lookback period is 30 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 30 days. The default is 30 days.

        """
        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["sensor", "configure", "commands"],
            "operation": "get_device_sensor_commands",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/sensor/commands"

        query_params = [
            "operations",
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "operations",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_device_sensor_command(self, serial: str, operation: str) -> dict[str, Any] | None:
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
        kwargs = locals()

        if "operation" in kwargs:
            options = [
                "cycleDownstreamPower",
                "disableDownstreamPower",
                "enableDownstreamPower",
                "refreshData",
            ]
            assert kwargs["operation"] in options, (
                f'''"operation" cannot be "{kwargs["operation"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["sensor", "configure", "commands"],
            "operation": "create_device_sensor_command",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/sensor/commands"

        body_params = [
            "operation",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_device_sensor_command(self, serial: str, command_id: str) -> dict[str, Any] | None:
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

    def get_device_sensor_relationships(self, serial: str) -> dict[str, Any] | None:
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
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Assign one or more sensor roles to a given sensor or camera device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-sensor-relationships

        Args:
            serial: Serial.
            livestream: A role defined between an MT sensor and an MV camera that adds the camera's
              livestream to the sensor's details page. Snapshots from the camera will
              also appear in alert notifications that the sensor triggers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sensor", "configure", "relationships"],
            "operation": "update_device_sensor_relationships",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/sensor/relationships"

        body_params = [
            "livestream",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_sensor_alerts_current_overview_by_metric(
        self, network_id: str
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
        self, network_id: str, **kwargs: Any
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
        kwargs.update(locals())

        metadata = {
            "tags": ["sensor", "monitor", "alerts", "overview", "byMetric"],
            "operation": "get_network_sensor_alerts_overview_by_metric",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/overview/byMetric"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_sensor_alerts_profiles(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, name: str, conditions: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Creates a sensor alert profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            name: Name of the sensor alert profile.
            conditions: List of conditions that will cause the profile to send an alert.
            schedule: The sensor schedule to use with the alert profile.
            recipients: List of recipients that will receive the alert.
            serials: List of device serials assigned to this sensor alert profile.
            includeSensorUrl: Include dashboard link to sensor in messages (default: true).
            message: A custom message that will appear in email and text message alerts.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "create_network_sensor_alerts_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles"

        body_params = [
            "name",
            "schedule",
            "conditions",
            "recipients",
            "serials",
            "includeSensorUrl",
            "message",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_sensor_alerts_profile(self, network_id: str, id: str) -> dict[str, Any] | None:
        """Show details of a sensor alert profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            id: ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "get_network_sensor_alerts_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles/{id}"

        return self._session.get(metadata, resource)

    def update_network_sensor_alerts_profile(
        self, network_id: str, id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Updates a sensor alert profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            id: ID.
            name: Name of the sensor alert profile.
            schedule: The sensor schedule to use with the alert profile.
            conditions: List of conditions that will cause the profile to send an alert.
            recipients: List of recipients that will receive the alert.
            serials: List of device serials assigned to this sensor alert profile.
            includeSensorUrl: Include dashboard link to sensor in messages (default: true).
            message: A custom message that will appear in email and text message alerts.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "update_network_sensor_alerts_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles/{id}"

        body_params = [
            "name",
            "schedule",
            "conditions",
            "recipients",
            "serials",
            "includeSensorUrl",
            "message",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_sensor_alerts_profile(self, network_id: str, id: str) -> None:
        """Deletes a sensor alert profile from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            id: ID.

        """
        metadata = {
            "tags": ["sensor", "configure", "alerts", "profiles"],
            "operation": "delete_network_sensor_alerts_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/networks/{network_id}/sensor/alerts/profiles/{id}"

        return self._session.delete(metadata, resource)

    def get_network_sensor_mqtt_brokers(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, mqtt_broker_id: str
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
        self, network_id: str, mqtt_broker_id: str, enabled: bool
    ) -> dict[str, Any] | None:
        """Update the sensor settings of an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.
            enabled: Set to true to enable MQTT broker for sensor network.

        """
        kwargs = locals()

        metadata = {
            "tags": ["sensor", "configure", "mqttBrokers"],
            "operation": "update_network_sensor_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/sensor/mqttBrokers/{mqtt_broker_id}"

        body_params = [
            "enabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_sensor_relationships(self, network_id: str) -> dict[str, Any] | None:
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
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns latest sensor-gateway connectivity data.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-gateways-connections-latest

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            sensorSerials: List of sensor serials to filter connectivity data by sensor.
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
            "tags": ["sensor", "monitor", "gateways", "connections", "latest"],
            "operation": "get_organization_sensor_gateways_connections_latest",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/sensor/gateways/connections/latest"

        query_params = [
            "sensorSerials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "sensorSerials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_sensor_readings_history(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return all reported readings from sensors in a given timespan, sorted by timestamp.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history

        Args:
            organization_id: Organization ID.
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              and 6 hours from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days. The default is 2 hours.
            networkIds: Optional parameter to filter readings by network.
            serials: Optional parameter to filter readings by sensor.
            metrics: Types of sensor readings to retrieve. If no metrics are supplied, all available
              types of readings will be retrieved.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sensor", "monitor", "readings", "history"],
            "operation": "get_organization_sensor_readings_history",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/sensor/readings/history"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "networkIds",
            "serials",
            "metrics",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "metrics",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_sensor_readings_latest(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the latest available reading for each metric from each sensor, sorted by sensor serial.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-latest

        Args:
            organization_id: Organization ID.
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
            networkIds: Optional parameter to filter readings by network.
            serials: Optional parameter to filter readings by sensor.
            metrics: Types of sensor readings to retrieve. If no metrics are supplied, all available
              types of readings will be retrieved.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sensor", "monitor", "readings", "latest"],
            "operation": "get_organization_sensor_readings_latest",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/sensor/readings/latest"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "metrics",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "metrics",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
