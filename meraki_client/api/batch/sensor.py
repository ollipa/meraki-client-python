"""ActionBatchSensor API endpoints."""

import urllib.parse
from typing import Any


class ActionBatchSensor:
    """ActionBatchSensor class."""

    def __init__(self) -> None:
        pass

    def create_device_sensor_command(self, *, serial: str, operation: str) -> dict[str, Any]:
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

        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/sensor/commands"

        payload = {}
        if operation is not None:
            payload["operation"] = operation

        action = {
            "path": path,
            "operation": "create",
            "body": payload,
        }
        return action  # noqa: RET504

    def update_device_sensor_relationships(
        self, *, serial: str, livestream: dict | None = None
    ) -> dict[str, Any]:
        """Assign one or more sensor roles to a given sensor or camera device.

        https://developer.cisco.com/meraki/api-v1/#!update-device-sensor-relationships

        Args:
            serial: Serial.
            livestream: A role defined between an MT sensor and an MV camera that adds the camera's
              livestream to the sensor's details page. Snapshots from the camera will
              also appear in alert notifications that the sensor triggers.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/sensor/relationships"

        payload = {}
        if livestream is not None:
            payload["livestream"] = livestream

        action = {
            "path": path,
            "operation": "update",
            "body": payload,
        }
        return action  # noqa: RET504

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
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sensor/alerts/profiles"

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

        action = {
            "path": path,
            "operation": "create",
            "body": payload,
        }
        return action  # noqa: RET504

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
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/networks/{network_id}/sensor/alerts/profiles/{id_}"

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

        action = {
            "path": path,
            "operation": "update",
            "body": payload,
        }
        return action  # noqa: RET504

    def delete_network_sensor_alerts_profile(self, *, network_id: str, id_: str) -> dict[str, Any]:
        """Deletes a sensor alert profile from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile

        Args:
            network_id: Network ID.
            id_: ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        path = f"/networks/{network_id}/sensor/alerts/profiles/{id_}"

        action = {
            "path": path,
            "operation": "destroy",
        }
        return action  # noqa: RET504

    def update_network_sensor_mqtt_broker(
        self, *, network_id: str, mqtt_broker_id: str, enabled: bool
    ) -> dict[str, Any]:
        """Update the sensor settings of an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.
            enabled: Set to true to enable MQTT broker for sensor network.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        path = f"/networks/{network_id}/sensor/mqttBrokers/{mqtt_broker_id}"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled

        action = {
            "path": path,
            "operation": "update",
            "body": payload,
        }
        return action  # noqa: RET504
