"""ActionBatchCampusGateway API endpoints."""

import urllib
from typing import Any


class ActionBatchCampusGateway:
    """ActionBatchCampusGateway class."""

    def __init__(self) -> None:
        pass

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
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/campusGateway/clusters"

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

        action = {
            "path": path,
            "operation": "create",
            "body": payload,
        }
        return action  # noqa: RET504

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
    ) -> dict[str, Any]:
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        cluster_id = urllib.parse.quote(str(cluster_id), safe="")
        path = f"/networks/{network_id}/campusGateway/clusters/{cluster_id}"

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

        action = {
            "path": path,
            "operation": "update",
            "body": payload,
        }
        return action  # noqa: RET504
