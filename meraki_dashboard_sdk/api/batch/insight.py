"""ActionBatchInsight API endpoints."""

import urllib
from typing import Any


class ActionBatchInsight:
    """ActionBatchInsight class."""

    def __init__(self) -> None:
        pass

    def create_organization_insight_monitored_media_server(
        self, organization_id: str, name: str, address: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Add a media server to be monitored for this organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

        Args:
            organization_id: Organization ID.
            name: The name of the VoIP provider.
            address: The IP address (IPv4 only) or hostname of the media server to monitor.
            bestEffortMonitoringEnabled: Indicates that if the media server doesn't respond to ICMP
              pings, the nearest hop will be used in its stead.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "create_organization_insight_monitored_media_server",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_insight_monitored_media_server(
        self, organization_id: str, monitored_media_server_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a monitored media server for this organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

        Args:
            organization_id: Organization ID.
            monitored_media_server_id: Monitored media server ID.
            name: The name of the VoIP provider.
            address: The IP address (IPv4 only) or hostname of the media server to monitor.
            bestEffortMonitoringEnabled: Indicates that if the media server doesn't respond to ICMP
              pings, the nearest hop will be used in its stead.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "update_organization_insight_monitored_media_server",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        monitored_media_server_id = urllib.parse.quote(monitored_media_server_id, safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
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
        organization_id = urllib.parse.quote(organization_id, safe="")
        monitored_media_server_id = urllib.parse.quote(monitored_media_server_id, safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
