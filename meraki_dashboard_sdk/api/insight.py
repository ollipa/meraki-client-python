"""Insight API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.rest_session import RestSession


class Insight:
    """Insight class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
        self._session = session

    def get_network_insight_application_health_by_time(
        self, network_id: str, application_id: str, **kwargs: Any
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
        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "monitor", "applications", "healthByTime"],
            "operation": "get_network_insight_application_health_by_time",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        application_id = urllib.parse.quote(str(application_id), safe="")
        resource = f"/networks/{network_id}/insight/applications/{application_id}/healthByTime"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_organization_insight_applications(self, organization_id: str) -> dict[str, Any] | None:
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
        self, organization_id: str
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
        self, organization_id: str, name: str, address: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_insight_monitored_media_server(
        self, organization_id: str, monitored_media_server_id: str
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
        self, organization_id: str, monitored_media_server_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        monitored_media_server_id = urllib.parse.quote(str(monitored_media_server_id), safe="")
        resource = f"/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_insight_monitored_media_server(
        self, organization_id: str, monitored_media_server_id: str
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
