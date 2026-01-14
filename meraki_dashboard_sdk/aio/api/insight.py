"""Insight API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncInsight:
    """Insight class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_network_insight_application_health_by_time(
        self,
        *,
        network_id: str,
        application_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
    ) -> dict[str, Any] | None:
        """Get application health by time.

        https://developer.cisco.com/meraki/api-v1/#!get-network-insight-application-health-by-time

        Args:
            network_id: Network ID.
            application_id: Application ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 7 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days. The default is 2 hours.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              60, 300, 3600, 86400. The default is 300.

        """
        metadata = {
            "tags": ["insight", "monitor", "applications", "healthByTime"],
            "operation": "get_network_insight_application_health_by_time",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        application_id = urllib.parse.quote(str(application_id), safe="")
        resource = f"/networks/{network_id}/insight/applications/{application_id}/healthByTime"

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

    def get_organization_insight_applications(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List all Insight tracked applications.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-applications

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["insight", "configure", "applications"],
            "operation": "get_organization_insight_applications",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/insight/applications"

        return self._session.get(metadata, resource)

    def get_organization_insight_monitored_media_servers(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List the monitored media servers for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-servers

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "get_organization_insight_monitored_media_servers",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers"

        return self._session.get(metadata, resource)

    def create_organization_insight_monitored_media_server(
        self,
        *,
        organization_id: str,
        name: str,
        address: str,
        best_effort_monitoring_enabled: bool | None = None,
    ) -> dict[str, Any] | None:
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

        return self._session.post(metadata, resource, payload)

    def get_organization_insight_monitored_media_server(
        self, *, organization_id: str, monitored_media_server_id: str
    ) -> dict[str, Any] | None:
        """Return a monitored media server for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-server

        Args:
            organization_id: Organization ID.
            monitored_media_server_id: Monitored media server ID.

        """
        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "get_organization_insight_monitored_media_server",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        monitored_media_server_id = urllib.parse.quote(str(monitored_media_server_id), safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}"

        return self._session.get(metadata, resource)

    def update_organization_insight_monitored_media_server(
        self,
        *,
        organization_id: str,
        monitored_media_server_id: str,
        name: str | None = None,
        address: str | None = None,
        best_effort_monitoring_enabled: bool | None = None,
    ) -> dict[str, Any] | None:
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

        return self._session.put(metadata, resource, payload)

    def delete_organization_insight_monitored_media_server(
        self, *, organization_id: str, monitored_media_server_id: str
    ) -> None:
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

        return self._session.delete(metadata, resource)
