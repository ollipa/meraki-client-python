"""CampusGateway API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.rest_session import RestSession


class CampusGateway:
    """CampusGateway class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
        self._session = session

    def create_network_campus_gateway_cluster(
        self,
        *,
        network_id: str,
        name: str,
        uplinks: list,
        tunnels: list,
        nameservers: dict,
        port_channels: list,
        devices: list | None = None,
        notes: str | None = None,
    ) -> dict[str, Any] | None:
        """Create a cluster and add campus gateways to it.

        https://developer.cisco.com/meraki/api-v1/#!create-network-campus-gateway-cluster

        Args:
            network_id: Network ID.
            name: Name of the new cluster.
            uplinks: Uplink interface settings of the cluster.
            tunnels: Tunnel interface settings of the cluster: Reuse uplink or specify tunnel
              interface.
            nameservers: Nameservers of the cluster.
            port_channels: Port channel settings of the cluster.
            devices: Devices to be added to the cluster.
            notes: Notes about cluster with max size of 511 characters allowed.

        """
        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "create_network_campus_gateway_cluster",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/campusGateway/clusters"

        payload = {}
        if name is not None:
            payload["name"] = name
        if uplinks is not None:
            payload["uplinks"] = uplinks
        if tunnels is not None:
            payload["tunnels"] = tunnels
        if nameservers is not None:
            payload["nameservers"] = nameservers
        if port_channels is not None:
            payload["portChannels"] = port_channels
        if devices is not None:
            payload["devices"] = devices
        if notes is not None:
            payload["notes"] = notes

        return self._session.post(metadata, resource, payload)

    def update_network_campus_gateway_cluster(
        self,
        *,
        network_id: str,
        cluster_id: str,
        name: str | None = None,
        uplinks: list | None = None,
        tunnels: list | None = None,
        nameservers: dict | None = None,
        port_channels: list | None = None,
        devices: list | None = None,
        notes: str | None = None,
    ) -> dict[str, Any] | None:
        """Update a cluster and add/remove campus gateways to/from it.

        https://developer.cisco.com/meraki/api-v1/#!update-network-campus-gateway-cluster

        Args:
            network_id: Network ID.
            cluster_id: Cluster ID.
            name: Name of the cluster.
            uplinks: Uplink interface settings of the cluster.
            tunnels: Tunnel interface settings of the cluster: Reuse uplink or specify tunnel
              interface.
            nameservers: Nameservers of the cluster.
            port_channels: Port channel settings of the cluster.
            devices: Devices in the cluster.
            notes: Notes about cluster with max size of 511 characters allowed.

        """
        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "update_network_campus_gateway_cluster",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        cluster_id = urllib.parse.quote(str(cluster_id), safe="")
        resource = f"/networks/{network_id}/campusGateway/clusters/{cluster_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if uplinks is not None:
            payload["uplinks"] = uplinks
        if tunnels is not None:
            payload["tunnels"] = tunnels
        if nameservers is not None:
            payload["nameservers"] = nameservers
        if port_channels is not None:
            payload["portChannels"] = port_channels
        if devices is not None:
            payload["devices"] = devices
        if notes is not None:
            payload["notes"] = notes

        return self._session.put(metadata, resource, payload)

    def get_organization_campus_gateway_clusters(
        self,
        *,
        organization_id: str,
        network_ids: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Get the details of campus gateway clusters.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters

        Args:
            organization_id: Organization ID.
            network_ids: Networks for which information should be gathered.
            per_page: The number of entries per page returned. Acceptable range is 3 - 100. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "get_organization_campus_gateway_clusters",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/campusGateway/clusters"

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

    def get_organization_campus_gateway_devices_uplinks_local_overrides_by_device(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev" | "next"] = "next",
    ) -> Generator[Any, None, None]:
        """Uplink overrides configured locally on Campus Gateway devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-devices-uplinks-local-overrides-by-device

        Args:
            organization_id: Organization ID.
            serials: A list of serial numbers. The returned devices will be filtered to only include
              these serials.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": [
                "campusGateway",
                "configure",
                "devices",
                "uplinks",
                "localOverrides",
                "byDevice",
            ],
            "operation": "get_organization_campus_gateway_devices_uplinks_local_overrides_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/campusGateway/devices/uplinks/localOverrides/byDevice"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
