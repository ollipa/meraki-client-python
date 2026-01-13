"""CellularGateway API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.rest_session import RestSession


class CellularGateway:
    """CellularGateway class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
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
        self,
        serial: str,
        *,
        reserved_ip_ranges: list | None = None,
        fixed_ip_assignments: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the LAN Settings for a single MG.

        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-lan

        Args:
            serial: Serial.
            reserved_ip_ranges: list of all reserved IP ranges for a single MG.
            fixed_ip_assignments: list of all fixed IP assignments for a single MG.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "lan"],
            "operation": "update_device_cellular_gateway_lan",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellularGateway/lan"

        payload = {}
        if reserved_ip_ranges is not None:
            payload["reservedIpRanges"] = reserved_ip_ranges
        if fixed_ip_assignments is not None:
            payload["fixedIpAssignments"] = fixed_ip_assignments

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
        self, serial: str, *, rules: list | None = None
    ) -> dict[str, Any] | None:
        """Updates the port forwarding rules for a single MG.

        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-port-forwarding-rules

        Args:
            serial: Serial.
            rules: An array of port forwarding params.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "portForwardingRules"],
            "operation": "update_device_cellular_gateway_port_forwarding_rules",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellularGateway/portForwardingRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return self._session.put(metadata, resource, payload)

    def get_network_cellular_gateway_connectivity_monitoring_destinations(
        self, network_id: str
    ) -> dict[str, Any] | None:
        """Return the connectivity testing destinations for an MG network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-connectivity-monitoring-destinations

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "connectivityMonitoringDestinations"],
            "operation": "get_network_cellular_gateway_connectivity_monitoring_destinations",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/cellularGateway/connectivityMonitoringDestinations"

        return self._session.get(metadata, resource)

    def update_network_cellular_gateway_connectivity_monitoring_destinations(
        self, network_id: str, *, destinations: list | None = None
    ) -> dict[str, Any] | None:
        """Update the connectivity testing destinations for an MG network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations

        Args:
            network_id: Network ID.
            destinations: The list of connectivity monitoring destinations.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "connectivityMonitoringDestinations"],
            "operation": "update_network_cellular_gateway_connectivity_monitoring_destinations",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/cellularGateway/connectivityMonitoringDestinations"

        payload = {}
        if destinations is not None:
            payload["destinations"] = destinations

        return self._session.put(metadata, resource, payload)

    def get_network_cellular_gateway_dhcp(self, network_id: str) -> dict[str, Any] | None:
        """List common DHCP settings of MGs.

        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-dhcp

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "dhcp"],
            "operation": "get_network_cellular_gateway_dhcp",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/cellularGateway/dhcp"

        return self._session.get(metadata, resource)

    def update_network_cellular_gateway_dhcp(
        self,
        network_id: str,
        *,
        dhcp_lease_time: str | None = None,
        dns_nameservers: str | None = None,
        dns_custom_nameservers: list | None = None,
    ) -> dict[str, Any] | None:
        """Update common DHCP settings of MGs.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-dhcp

        Args:
            network_id: Network ID.
            dhcp_lease_time: DHCP Lease time for all MG of the network. Possible values are '30
              minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
            dns_nameservers: DNS name servers mode for all MG of the network. Possible values are:
              'upstream_dns', 'google_dns', 'opendns', 'custom'.
            dns_custom_nameservers: list of fixed IPs representing the the DNS Name servers when the
              mode is 'custom'.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "dhcp"],
            "operation": "update_network_cellular_gateway_dhcp",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/cellularGateway/dhcp"

        payload = {}
        if dhcp_lease_time is not None:
            payload["dhcpLeaseTime"] = dhcp_lease_time
        if dns_nameservers is not None:
            payload["dnsNameservers"] = dns_nameservers
        if dns_custom_nameservers is not None:
            payload["dnsCustomNameservers"] = dns_custom_nameservers

        return self._session.put(metadata, resource, payload)

    def get_network_cellular_gateway_subnet_pool(self, network_id: str) -> dict[str, Any] | None:
        """Return the subnet pool and mask configured for MGs in the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-subnet-pool

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "subnetPool"],
            "operation": "get_network_cellular_gateway_subnet_pool",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/cellularGateway/subnetPool"

        return self._session.get(metadata, resource)

    def update_network_cellular_gateway_subnet_pool(
        self, network_id: str, *, mask: int | None = None, cidr: str | None = None
    ) -> dict[str, Any] | None:
        """Update the subnet pool and mask configuration for MGs in the network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool

        Args:
            network_id: Network ID.
            mask: Mask used for the subnet of all MGs in this network.
            cidr: CIDR of the pool of subnets. Each MG in this network will automatically pick a
              subnet from this pool.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "subnetPool"],
            "operation": "update_network_cellular_gateway_subnet_pool",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/cellularGateway/subnetPool"

        payload = {}
        if mask is not None:
            payload["mask"] = mask
        if cidr is not None:
            payload["cidr"] = cidr

        return self._session.put(metadata, resource, payload)

    def get_network_cellular_gateway_uplink(self, network_id: str) -> dict[str, Any] | None:
        """Returns the uplink settings for your MG network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-uplink

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "uplink"],
            "operation": "get_network_cellular_gateway_uplink",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/cellularGateway/uplink"

        return self._session.get(metadata, resource)

    def update_network_cellular_gateway_uplink(
        self, network_id: str, *, bandwidth_limits: dict | None = None
    ) -> dict[str, Any] | None:
        """Updates the uplink settings for your MG network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-uplink

        Args:
            network_id: Network ID.
            bandwidth_limits: The bandwidth settings for the 'cellular' uplink.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "uplink"],
            "operation": "update_network_cellular_gateway_uplink",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/cellularGateway/uplink"

        payload = {}
        if bandwidth_limits is not None:
            payload["bandwidthLimits"] = bandwidth_limits

        return self._session.put(metadata, resource, payload)

    def get_organization_cellular_gateway_esims_inventory(
        self, organization_id: str, *, eids: list | None = None
    ) -> dict[str, Any] | None:
        """The eSIM inventory of a given organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-inventory

        Args:
            organization_id: Organization ID.
            eids: Optional parameter to filter the results by EID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "inventory"],
            "operation": "get_organization_cellular_gateway_esims_inventory",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/inventory"

        params = {}
        if eids is not None:
            params["eids[]"] = eids

        return self._session.get(metadata, resource, params)

    def update_organization_cellular_gateway_esims_inventory(
        self, organization_id: str, id_: str, *, status: str | None = None
    ) -> dict[str, Any] | None:
        """Toggle the status of an eSIM.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-inventory

        Args:
            organization_id: Organization ID.
            id_: ID.
            status: Status the eSIM will be updated to.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "inventory"],
            "operation": "update_organization_cellular_gateway_esims_inventory",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        id_ = urllib.parse.quote(str(id_), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/inventory/{id_}"

        payload = {}
        if status is not None:
            payload["status"] = status

        return self._session.put(metadata, resource, payload)

    def get_organization_cellular_gateway_esims_service_providers(
        self, organization_id: str
    ) -> dict[str, Any] | None:
        """Service providers customers can add accounts for.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders"],
            "operation": "get_organization_cellular_gateway_esims_service_providers",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders"

        return self._session.get(metadata, resource)

    def get_organization_cellular_gateway_esims_service_providers_accounts(
        self, organization_id: str, *, account_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Inventory of service provider accounts tied to the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts

        Args:
            organization_id: Organization ID.
            account_ids: Optional parameter to filter the results by service provider account IDs.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "get_organization_cellular_gateway_esims_service_providers_accounts",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts"
        )

        params = {}
        if account_ids is not None:
            params["accountIds[]"] = account_ids

        return self._session.get(metadata, resource, params)

    def create_organization_cellular_gateway_esims_service_providers_account(
        self,
        organization_id: str,
        account_id: str,
        api_key: str,
        service_provider: dict,
        title: str,
        username: str,
    ) -> dict[str, Any] | None:
        """Add a service provider account.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-cellular-gateway-esims-service-providers-account

        Args:
            organization_id: Organization ID.
            account_id: Service provider account ID.
            api_key: Service provider account API key.
            service_provider: Service Provider information.
            title: Service provider account name.
            username: Service provider account username.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "create_organization_cellular_gateway_esims_service_providers_account",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts"
        )

        payload = {}
        if account_id is not None:
            payload["accountId"] = account_id
        if api_key is not None:
            payload["apiKey"] = api_key
        if service_provider is not None:
            payload["serviceProvider"] = service_provider
        if title is not None:
            payload["title"] = title
        if username is not None:
            payload["username"] = username

        return self._session.post(metadata, resource, payload)

    def get_organization_cellular_gateway_esims_service_providers_accounts_communication_plans(
        self, organization_id: str, account_ids: list
    ) -> dict[str, Any] | None:
        """The communication plans available for a given provider.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts-communication-plans

        Args:
            organization_id: Organization ID.
            account_ids: Account IDs that communication plans will be fetched for.

        """
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts/communicationPlans"

        params = {}
        if account_ids is not None:
            params["accountIds[]"] = account_ids

        return self._session.get(metadata, resource, params)

    def get_organization_cellular_gateway_esims_service_providers_accounts_rate_plans(
        self, organization_id: str, account_ids: list
    ) -> dict[str, Any] | None:
        """The rate plans available for a given provider.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts-rate-plans

        Args:
            organization_id: Organization ID.
            account_ids: Account IDs that rate plans will be fetched for.

        """
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts/ratePlans"

        params = {}
        if account_ids is not None:
            params["accountIds[]"] = account_ids

        return self._session.get(metadata, resource, params)

    def update_organization_cellular_gateway_esims_service_providers_account(
        self,
        organization_id: str,
        account_id: str,
        *,
        title: str | None = None,
        api_key: str | None = None,
    ) -> dict[str, Any] | None:
        """Edit service provider account info stored in Meraki's database.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-service-providers-account

        Args:
            organization_id: Organization ID.
            account_id: Account ID.
            title: Service provider account name used on the Meraki UI.
            api_key: Service provider account API key.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "serviceProviders", "accounts"],
            "operation": "update_organization_cellular_gateway_esims_service_providers_account",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        account_id = urllib.parse.quote(str(account_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts/{account_id}"

        payload = {}
        if title is not None:
            payload["title"] = title
        if api_key is not None:
            payload["apiKey"] = api_key

        return self._session.put(metadata, resource, payload)

    def delete_organization_cellular_gateway_esims_service_providers_account(
        self, organization_id: str, account_id: str
    ) -> None:
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        account_id = urllib.parse.quote(str(account_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/serviceProviders/accounts/{account_id}"

        return self._session.delete(metadata, resource)

    def create_organization_cellular_gateway_esims_swap(
        self, organization_id: str, swaps: list
    ) -> dict[str, Any] | None:
        """Swap which profile an eSIM uses.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-cellular-gateway-esims-swap

        Args:
            organization_id: Organization ID.
            swaps: Each object represents a swap for one eSIM.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "swap"],
            "operation": "create_organization_cellular_gateway_esims_swap",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/swap"

        payload = {}
        if swaps is not None:
            payload["swaps"] = swaps

        return self._session.post(metadata, resource, payload)

    def update_organization_cellular_gateway_esims_swap(
        self, id_: str, organization_id: str
    ) -> dict[str, Any] | None:
        """Get the status of a profile swap.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-swap

        Args:
            id_: eSIM EID.
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["cellularGateway", "configure", "esims", "swap"],
            "operation": "update_organization_cellular_gateway_esims_swap",
        }
        id_ = urllib.parse.quote(str(id_), safe="")
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/esims/swap/{id_}"

        return self._session.put(metadata, resource)

    def get_organization_cellular_gateway_uplink_statuses(
        self,
        organization_id: str,
        *,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        iccids: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the uplink status of every Meraki MG cellular gateway in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-uplink-statuses

        Args:
            organization_id: Organization ID.
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
            network_ids: A list of network IDs. The returned devices will be filtered to only
              include these networks.
            serials: A list of serial numbers. The returned devices will be filtered to only include
              these serials.
            iccids: A list of ICCIDs. The returned devices will be filtered to only include these
              ICCIDs.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["cellularGateway", "monitor", "uplink", "statuses"],
            "operation": "get_organization_cellular_gateway_uplink_statuses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/cellularGateway/uplink/statuses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if iccids is not None:
            params["iccids[]"] = iccids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
