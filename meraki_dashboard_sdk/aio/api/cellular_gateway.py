"""CellularGateway API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncCellularGateway:
    """CellularGateway class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_device_cellular_gateway_lan(self, serial: str) -> dict[str, Any] | None:
        """Show the LAN Settings of a MG.

        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-lan

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "lan"],
            "operation": "get_device_cellular_gateway_lan",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellularGateway/lan"

        return self._session.get(metadata, resource)

    def update_device_cellular_gateway_lan(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellularGateway/lan"

        body_params = [
            "reservedIpRanges",
            "fixedIpAssignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_device_cellular_gateway_port_forwarding_rules(
        self, serial: str
    ) -> dict[str, Any] | None:
        """Returns the port forwarding rules for a single MG.

        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-port-forwarding-rules

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "portForwardingRules"],
            "operation": "get_device_cellular_gateway_port_forwarding_rules",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellularGateway/portForwardingRules"

        return self._session.get(metadata, resource)

    def update_device_cellular_gateway_port_forwarding_rules(
        self, serial: str, **kwargs: Any
    ) -> dict[str, Any] | None:
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
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellularGateway/portForwardingRules"

        body_params = [
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_cellular_gateway_connectivity_monitoring_destinations(
        self, networkId: str
    ) -> dict[str, Any] | None:
        """Return the connectivity testing destinations for an MG network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-connectivity-monitoring-destinations

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "connectivityMonitoringDestinations"],
            "operation": "get_network_cellular_gateway_connectivity_monitoring_destinations",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations"

        return self._session.get(metadata, resource)

    def update_network_cellular_gateway_connectivity_monitoring_destinations(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the connectivity testing destinations for an MG network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations

        Args:
            networkId: Network ID.
            destinations: The list of connectivity monitoring destinations.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "connectivityMonitoringDestinations"],
            "operation": "update_network_cellular_gateway_connectivity_monitoring_destinations",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations"

        body_params = [
            "destinations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_cellular_gateway_dhcp(self, networkId: str) -> dict[str, Any] | None:
        """List common DHCP settings of MGs.

        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-dhcp

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "dhcp"],
            "operation": "get_network_cellular_gateway_dhcp",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/cellularGateway/dhcp"

        return self._session.get(metadata, resource)

    def update_network_cellular_gateway_dhcp(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update common DHCP settings of MGs.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-dhcp

        Args:
            networkId: Network ID.
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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/cellularGateway/dhcp"

        body_params = [
            "dhcpLeaseTime",
            "dnsNameservers",
            "dnsCustomNameservers",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_cellular_gateway_subnet_pool(self, networkId: str) -> dict[str, Any] | None:
        """Return the subnet pool and mask configured for MGs in the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-subnet-pool

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "subnetPool"],
            "operation": "get_network_cellular_gateway_subnet_pool",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/cellularGateway/subnetPool"

        return self._session.get(metadata, resource)

    def update_network_cellular_gateway_subnet_pool(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the subnet pool and mask configuration for MGs in the network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool

        Args:
            networkId: Network ID.
            mask: Mask used for the subnet of all MGs in  this network.
            cidr: CIDR of the pool of subnets. Each MG in this network will automatically pick a
              subnet from this pool.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "subnetPool"],
            "operation": "update_network_cellular_gateway_subnet_pool",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/cellularGateway/subnetPool"

        body_params = [
            "mask",
            "cidr",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_cellular_gateway_uplink(self, networkId: str) -> dict[str, Any] | None:
        """Returns the uplink settings for your MG network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-uplink

        Args:
            networkId: Network ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "uplink"],
            "operation": "get_network_cellular_gateway_uplink",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/cellularGateway/uplink"

        return self._session.get(metadata, resource)

    def update_network_cellular_gateway_uplink(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Updates the uplink settings for your MG network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-uplink

        Args:
            networkId: Network ID.
            bandwidthLimits: The bandwidth settings for the 'cellular' uplink.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "uplink"],
            "operation": "update_network_cellular_gateway_uplink",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/cellularGateway/uplink"

        body_params = [
            "bandwidthLimits",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_cellular_gateway_esims_inventory(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """The eSIM inventory of a given organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-inventory

        Args:
            organizationId: Organization ID.
            eids: Optional parameter to filter the results by EID.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "inventory"],
            "operation": "get_organization_cellular_gateway_esims_inventory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/inventory"

        query_params = [
            "eids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "eids",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def update_organization_cellular_gateway_esims_inventory(
        self, organizationId: str, id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Toggle the status of an eSIM.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-inventory

        Args:
            organizationId: Organization ID.
            id: ID.
            status: Status the eSIM will be updated to.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "inventory"],
            "operation": "update_organization_cellular_gateway_esims_inventory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/inventory/{id}"

        body_params = [
            "status",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_cellular_gateway_esims_service_providers(
        self, organizationId: str
    ) -> dict[str, Any] | None:
        """Service providers customers can add accounts for.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers

        Args:
            organizationId: Organization ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders"],
            "operation": "get_organization_cellular_gateway_esims_service_providers",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/serviceProviders"

        return self._session.get(metadata, resource)

    def get_organization_cellular_gateway_esims_service_providers_accounts(
        self, organizationId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Inventory of service provider accounts tied to the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts

        Args:
            organizationId: Organization ID.
            accountIds: Optional parameter to filter the results by service provider account IDs.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "get_organization_cellular_gateway_esims_service_providers_accounts",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts"
        )

        query_params = [
            "accountIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "accountIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def create_organization_cellular_gateway_esims_service_providers_account(
        self,
        organizationId: str,
        accountId: str,
        apiKey: str,
        serviceProvider: dict,
        title: str,
        username: str,
    ) -> dict[str, Any] | None:
        """Add a service provider account.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-cellular-gateway-esims-service-providers-account

        Args:
            organizationId: Organization ID.
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
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts"
        )

        body_params = [
            "accountId",
            "apiKey",
            "serviceProvider",
            "title",
            "username",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_cellular_gateway_esims_service_providers_accounts_communication_plans(
        self, organizationId: str, accountIds: list
    ) -> dict[str, Any] | None:
        """The communication plans available for a given provider.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts-communication-plans

        Args:
            organizationId: Organization ID.
            accountIds: Account IDs that communication plans will be fetched for.

        """
        kwargs = locals()

        metadata = {
            "tags": [
                "cellularGateway",
                "configure",
                "esims",
                "serviceProviders",
                "accounts",
                "communicationPlans",
            ],
            "operation": "get_organization_cellular_gateway_esims_service_providers_accounts_communication_plans",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/communicationPlans"

        query_params = [
            "accountIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "accountIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_organization_cellular_gateway_esims_service_providers_accounts_rate_plans(
        self, organizationId: str, accountIds: list
    ) -> dict[str, Any] | None:
        """The rate plans available for a given provider.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts-rate-plans

        Args:
            organizationId: Organization ID.
            accountIds: Account IDs that rate plans will be fetched for.

        """
        kwargs = locals()

        metadata = {
            "tags": [
                "cellularGateway",
                "configure",
                "esims",
                "serviceProviders",
                "accounts",
                "ratePlans",
            ],
            "operation": "get_organization_cellular_gateway_esims_service_providers_accounts_rate_plans",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/ratePlans"

        query_params = [
            "accountIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "accountIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def update_organization_cellular_gateway_esims_service_providers_account(
        self, organizationId: str, accountId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Edit service provider account info stored in Meraki's database.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-service-providers-account

        Args:
            organizationId: Organization ID.
            accountId: Account ID.
            title: Service provider account name used on the Meraki UI.
            apiKey: Service provider account API key.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "update_organization_cellular_gateway_esims_service_providers_account",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        accountId = urllib.parse.quote(str(accountId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/{accountId}"

        body_params = [
            "title",
            "apiKey",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_cellular_gateway_esims_service_providers_account(
        self, organizationId: str, accountId: str
    ) -> None:
        """Remove a service provider account's integration with the Dashboard.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-cellular-gateway-esims-service-providers-account

        Args:
            organizationId: Organization ID.
            accountId: Account ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "delete_organization_cellular_gateway_esims_service_providers_account",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        accountId = urllib.parse.quote(str(accountId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/{accountId}"

        return self._session.delete(metadata, resource)

    def create_organization_cellular_gateway_esims_swap(
        self, organizationId: str, swaps: list
    ) -> dict[str, Any] | None:
        """Swap which profile an eSIM uses.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-cellular-gateway-esims-swap

        Args:
            organizationId: Organization ID.
            swaps: Each object represents a swap for one eSIM.

        """
        kwargs = locals()

        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "swap"],
            "operation": "create_organization_cellular_gateway_esims_swap",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/swap"

        body_params = [
            "swaps",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_organization_cellular_gateway_esims_swap(
        self, id: str, organizationId: str
    ) -> dict[str, Any] | None:
        """Get the status of a profile swap.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-swap

        Args:
            id: eSIM EID.
            organizationId: Organization ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "swap"],
            "operation": "update_organization_cellular_gateway_esims_swap",
        }
        id = urllib.parse.quote(str(id), safe="")
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/esims/swap/{id}"

        return self._session.put(metadata, resource)

    def get_organization_cellular_gateway_uplink_statuses(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the uplink status of every Meraki MG cellular gateway in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-uplink-statuses

        Args:
            organizationId: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
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
            networkIds: A list of network IDs. The returned devices will be filtered to only include
              these networks.
            serials: A list of serial numbers. The returned devices will be filtered to only include
              these serials.
            iccids: A list of ICCIDs. The returned devices will be filtered to only include these
              ICCIDs.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["cellularGateway", "monitor", "uplink", "statuses"],
            "operation": "get_organization_cellular_gateway_uplink_statuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/cellularGateway/uplink/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "iccids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "iccids",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
