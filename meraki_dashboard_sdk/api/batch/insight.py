"""ActionBatchInsight API endpoints."""


class ActionBatchInsight:
    """ActionBatchInsight class."""

    def __init__(self) -> None:
        pass

    def create_organization_insight_monitored_media_server(
        self, organizationId: str, name: str, address: str, **kwargs
    ):
        """
        **Add a media server to be monitored for this organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "create_organization_insight_monitored_media_server",
        }
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_insight_monitored_media_server(
        self, organizationId: str, monitoredMediaServerId: str, **kwargs
    ):
        """
        **Update a monitored media server for this organization.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "update_organization_insight_monitored_media_server",
        }
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_insight_monitored_media_server(
        self, organizationId: str, monitoredMediaServerId: str
    ):
        """
        **Delete a monitored media server from this organization.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        """

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "delete_organization_insight_monitored_media_server",
        }
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
