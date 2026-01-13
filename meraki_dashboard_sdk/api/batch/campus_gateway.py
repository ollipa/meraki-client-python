"""ActionBatchCampusGateway API endpoints."""

import urllib
from typing import Any


class ActionBatchCampusGateway:
    """ActionBatchCampusGateway class."""

    def __init__(self) -> None:
        pass

    def create_network_campus_gateway_cluster(
        self,
        networkId: str,
        name: str,
        uplinks: list,
        tunnels: list,
        nameservers: dict,
        portChannels: list,
        **kwargs: Any,
    ) -> dict[str, Any]:
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
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_network_campus_gateway_cluster(
        self, networkId: str, clusterId: str, **kwargs: Any
    ) -> dict[str, Any]:
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
        action = {"resource": resource, "operation": "update", "body": payload}
        return action
