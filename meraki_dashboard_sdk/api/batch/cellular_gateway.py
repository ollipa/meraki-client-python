"""ActionBatchCellularGateway API endpoints."""

import urllib
from typing import Any


class ActionBatchCellularGateway:
    """ActionBatchCellularGateway class."""

    def __init__(self) -> None:
        pass

    def update_device_cellular_gateway_lan(self, serial: str, **kwargs: Any) -> dict[str, Any]:
        """Update the LAN Settings for a single MG.

        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-lan

        Args:
            serial: Serial.
            reservedIpRanges: list of all reserved IP ranges for a single MG.
            fixedIpAssignments: list of all fixed IP assignments for a single MG.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "lan"],
            "operation": "update_device_cellular_gateway_lan",
        }
        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/cellularGateway/lan"

        body_params = [
            "reservedIpRanges",
            "fixedIpAssignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_device_cellular_gateway_port_forwarding_rules(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates the port forwarding rules for a single MG.

        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-port-forwarding-rules

        Args:
            serial: Serial.
            rules: An array of port forwarding params.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "portForwardingRules"],
            "operation": "update_device_cellular_gateway_port_forwarding_rules",
        }
        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/cellularGateway/portForwardingRules"

        body_params = [
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_cellular_gateway_connectivity_monitoring_destinations(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the connectivity testing destinations for an MG network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations

        Args:
            network_id: Network ID.
            destinations: The list of connectivity monitoring destinations.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "connectivityMonitoringDestinations"],
            "operation": "update_network_cellular_gateway_connectivity_monitoring_destinations",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/cellularGateway/connectivityMonitoringDestinations"

        body_params = [
            "destinations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_cellular_gateway_dhcp(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update common DHCP settings of MGs.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-dhcp

        Args:
            network_id: Network ID.
            dhcpLeaseTime: DHCP Lease time for all MG of the network. Possible values are '30
              minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
            dnsNameservers: DNS name servers mode for all MG of the network. Possible values are:
              'upstream_dns', 'google_dns', 'opendns', 'custom'.
            dnsCustomNameservers: list of fixed IPs representing the the DNS Name servers when the
              mode is 'custom'.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "dhcp"],
            "operation": "update_network_cellular_gateway_dhcp",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/cellularGateway/dhcp"

        body_params = [
            "dhcpLeaseTime",
            "dnsNameservers",
            "dnsCustomNameservers",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_cellular_gateway_subnet_pool(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update the subnet pool and mask configuration for MGs in the network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool

        Args:
            network_id: Network ID.
            mask: Mask used for the subnet of all MGs in  this network.
            cidr: CIDR of the pool of subnets. Each MG in this network will automatically pick a
              subnet from this pool.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "subnetPool"],
            "operation": "update_network_cellular_gateway_subnet_pool",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/cellularGateway/subnetPool"

        body_params = [
            "mask",
            "cidr",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_network_cellular_gateway_uplink(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Updates the uplink settings for your MG network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-uplink

        Args:
            network_id: Network ID.
            bandwidthLimits: The bandwidth settings for the 'cellular' uplink.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "uplink"],
            "operation": "update_network_cellular_gateway_uplink",
        }
        network_id = urllib.parse.quote(network_id, safe="")
        resource = f"/networks/{network_id}/cellularGateway/uplink"

        body_params = [
            "bandwidthLimits",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def update_organization_cellular_gateway_esims_inventory(
        self, organization_id: str, id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Toggle the status of an eSIM.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-inventory

        Args:
            organization_id: Organization ID.
            id: ID.
            status: Status the eSIM will be updated to.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "inventory"],
            "operation": "update_organization_cellular_gateway_esims_inventory",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/inventory/{id}"

        body_params = [
            "status",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def create_organization_cellular_gateway_esims_service_providers_account(
        self,
        organization_id: str,
        accountId: str,
        apiKey: str,
        serviceProvider: dict,
        title: str,
        username: str,
    ) -> dict[str, Any]:
        """Add a service provider account.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-cellular-gateway-esims-service-providers-account

        Args:
            organization_id: Organization ID.
            accountId: Service provider account ID.
            apiKey: Service provider account API key.
            serviceProvider: Service Provider information.
            title: Service provider account name.
            username: Service provider account username.

        """
        kwargs = locals()

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "create_organization_cellular_gateway_esims_service_providers_account",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = (
            f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts"
        )

        body_params = [
            "accountId",
            "apiKey",
            "serviceProvider",
            "title",
            "username",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_cellular_gateway_esims_service_providers_account(
        self, organization_id: str, account_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Edit service provider account info stored in Meraki's database.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-service-providers-account

        Args:
            organization_id: Organization ID.
            account_id: Account ID.
            title: Service provider account name used on the Meraki UI.
            apiKey: Service provider account API key.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "update_organization_cellular_gateway_esims_service_providers_account",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        account_id = urllib.parse.quote(account_id, safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts/{account_id}"

        body_params = [
            "title",
            "apiKey",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "update", "body": payload}
        return action

    def delete_organization_cellular_gateway_esims_service_providers_account(
        self, organization_id: str, account_id: str
    ) -> dict[str, Any]:
        """Remove a service provider account's integration with the Dashboard.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-cellular-gateway-esims-service-providers-account

        Args:
            organization_id: Organization ID.
            account_id: Account ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "delete_organization_cellular_gateway_esims_service_providers_account",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        account_id = urllib.parse.quote(account_id, safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts/{account_id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def create_organization_cellular_gateway_esims_swap(
        self, organization_id: str, swaps: list
    ) -> dict[str, Any]:
        """Swap which profile an eSIM uses.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-cellular-gateway-esims-swap

        Args:
            organization_id: Organization ID.
            swaps: Each object represents a swap for one eSIM.

        """
        kwargs = locals()

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "swap"],
            "operation": "create_organization_cellular_gateway_esims_swap",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/swap"

        body_params = [
            "swaps",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action

    def update_organization_cellular_gateway_esims_swap(
        self, id: str, organization_id: str
    ) -> dict[str, Any]:
        """Get the status of a profile swap.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-swap

        Args:
            id: eSIM EID.
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "swap"],
            "operation": "update_organization_cellular_gateway_esims_swap",
        }
        id = urllib.parse.quote(id, safe="")
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/swap/{id}"

        action = {
            "resource": resource,
            "operation": "update",
        }
        return action
