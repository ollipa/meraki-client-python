"""ActionBatchInsight API endpoints."""

import urllib
from typing import Any


class ActionBatchInsight:
    """ActionBatchInsight class."""

    def __init__(self) -> None:
        pass

    def create_organization_insight_monitored_media_server(
        self,
        organization_id: str,
        name: str,
        address: str,
        *,
        best_effort_monitoring_enabled: bool | None = None,
    ) -> dict[str, Any]:
        """Add a media server to be monitored for this organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

        Args:
            organization_id: Organization ID.
            name: The name of the VoIP provider.
            address: The IP address (IPv4 only) or hostname of the media server to monitor.
            best_effort_monitoring_enabled: Indicates that if the media server doesn't respond to
              ICMP pings, the nearest hop will be used in its stead.

        """
        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "create_organization_insight_monitored_media_server",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers"

        payload = {}
        if name is not None:
            payload["name"] = name
        if address is not None:
            payload["address"] = address
        if best_effort_monitoring_enabled is not None:
            payload["bestEffortMonitoringEnabled"] = best_effort_monitoring_enabled

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def update_organization_insight_monitored_media_server(
        self,
        organization_id: str,
        monitored_media_server_id: str,
        *,
        name: str | None = None,
        address: str | None = None,
        best_effort_monitoring_enabled: bool | None = None,
    ) -> dict[str, Any]:
        """Update a monitored media server for this organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

        Args:
            organization_id: Organization ID.
            monitored_media_server_id: Monitored media server ID.
            name: The name of the VoIP provider.
            address: The IP address (IPv4 only) or hostname of the media server to monitor.
            best_effort_monitoring_enabled: Indicates that if the media server doesn't respond to
              ICMP pings, the nearest hop will be used in its stead.

        """
        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "update_organization_insight_monitored_media_server",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        monitored_media_server_id = urllib.parse.quote(str(monitored_media_server_id), safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if address is not None:
            payload["address"] = address
        if best_effort_monitoring_enabled is not None:
            payload["bestEffortMonitoringEnabled"] = best_effort_monitoring_enabled

        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def delete_organization_insight_monitored_media_server(
        self, organization_id: str, monitored_media_server_id: str
    ) -> dict[str, Any]:
        """Delete a monitored media server from this organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

        Args:
            organization_id: Organization ID.
            monitored_media_server_id: Monitored media server ID.

        """
        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "delete_organization_insight_monitored_media_server",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        monitored_media_server_id = urllib.parse.quote(str(monitored_media_server_id), safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
