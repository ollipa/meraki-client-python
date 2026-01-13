"""CampusGateway API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncCampusGateway:
    """CampusGateway class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def create_network_campus_gateway_cluster(
        self,
        networkId: str,
        name: str,
        uplinks: list,
        tunnels: list,
        nameservers: dict,
        portChannels: list,
        **kwargs: Any,
    ) -> dict[str, Any] | None:
        """Create a cluster and add campus gateways to it.

        https://developer.cisco.com/meraki/api-v1/#!create-network-campus-gateway-cluster

        Args:
            networkId: Network ID.
            name: Name of the new cluster.
            uplinks: Uplink interface settings of the cluster.
            tunnels: Tunnel interface settings of the cluster: Reuse uplink or specify tunnel
              interface.
            nameservers: Nameservers of the cluster.
            portChannels: Port channel settings of the cluster.
            devices: Devices to be added to the cluster.
            notes: Notes about cluster with max size of 511 characters allowed.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "create_network_campus_gateway_cluster",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/campusGateway/clusters"

        body_params = [
            "name",
            "uplinks",
            "tunnels",
            "nameservers",
            "portChannels",
            "devices",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_network_campus_gateway_cluster(
        self, networkId: str, clusterId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a cluster and add/remove campus gateways to/from it.

        https://developer.cisco.com/meraki/api-v1/#!update-network-campus-gateway-cluster

        Args:
            networkId: Network ID.
            clusterId: Cluster ID.
            name: Name of the cluster.
            uplinks: Uplink interface settings of the cluster.
            tunnels: Tunnel interface settings of the cluster: Reuse uplink or specify tunnel
              interface.
            nameservers: Nameservers of the cluster.
            portChannels: Port channel settings of the cluster.
            devices: Devices in the cluster.
            notes: Notes about cluster with max size of 511 characters allowed.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "update_network_campus_gateway_cluster",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clusterId = urllib.parse.quote(str(clusterId), safe="")
        resource = f"/networks/{networkId}/campusGateway/clusters/{clusterId}"

        body_params = [
            "name",
            "uplinks",
            "tunnels",
            "nameservers",
            "portChannels",
            "devices",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_campus_gateway_clusters(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get the details of campus gateway clusters.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            networkIds: Networks for which information should be gathered.
            perPage: The number of entries per page returned. Acceptable range is 3 - 100. Default
              is 50.
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
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "get_organization_campus_gateway_clusters",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_campus_gateway_devices_uplinks_local_overrides_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Uplink overrides configured locally on Campus Gateway devices in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-devices-uplinks-local-overrides-by-device

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            serials: A list of serial numbers. The returned devices will be filtered to only include
              these serials.
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/campusGateway/devices/uplinks/localOverrides/byDevice"
        )

        query_params = [
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
