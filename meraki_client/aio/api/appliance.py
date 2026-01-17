"""Appliance API endpoints."""

from __future__ import annotations

import urllib.parse
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from meraki_client.aio.session import AsyncPaginatedResponse, Session


class Appliance:
    """Appliance class."""

    def __init__(self, session: Session) -> None:
        self._session = session

    async def get_device_appliance_dhcp_subnets(self, *, serial: str) -> dict[str, Any] | None:
        """Return the DHCP subnet information for an appliance.

        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets

        Args:
            serial: Serial.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/dhcp/subnets"

        return await self._session.get(
            scope="appliance", operation_id="getDeviceApplianceDhcpSubnets", path=path
        )

    async def get_device_appliance_performance(
        self,
        *,
        serial: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Return the performance score for a single MX.

        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-performance

        Args:
            serial: Serial.
            t0: The beginning of the timespan for the data. The maximum lookback period is 30 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be greater than or equal to 30 minutes and be less than or
              equal to 14 days. The default is 30 minutes.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/performance"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return await self._session.get(
            scope="appliance",
            operation_id="getDeviceAppliancePerformance",
            path=path,
            params=params,
        )

    async def get_device_appliance_prefixes_delegated(
        self, *, serial: str
    ) -> dict[str, Any] | None:
        """Return current delegated IPv6 prefixes on an appliance.

        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-prefixes-delegated

        Args:
            serial: Serial.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/prefixes/delegated"

        return await self._session.get(
            scope="appliance", operation_id="getDeviceAppliancePrefixesDelegated", path=path
        )

    async def get_device_appliance_prefixes_delegated_vlan_assignments(
        self, *, serial: str
    ) -> dict[str, Any] | None:
        """Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-prefixes-delegated-vlan-assignments

        Args:
            serial: Serial.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/prefixes/delegated/vlanAssignments"

        return await self._session.get(
            scope="appliance",
            operation_id="getDeviceAppliancePrefixesDelegatedVlanAssignments",
            path=path,
        )

    async def get_device_appliance_radio_settings(self, *, serial: str) -> dict[str, Any] | None:
        """Return the radio settings of an appliance.

        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-radio-settings

        Args:
            serial: Serial.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/radio/settings"

        return await self._session.get(
            scope="appliance", operation_id="getDeviceApplianceRadioSettings", path=path
        )

    async def update_device_appliance_radio_settings(
        self,
        *,
        serial: str,
        rf_profile_id: str | None = None,
        two_four_ghz_settings: dict | None = None,
        five_ghz_settings: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the radio settings of an appliance.

        https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-radio-settings

        Args:
            serial: Serial.
            rf_profile_id: The ID of an RF profile to assign to the device. If the value of this
              parameter is null, the appropriate basic RF profile (indoor or outdoor)
              will be assigned to the device. Assigning an RF profile will clear ALL
              manually configured overrides on the device (channel width, channel,
              power).
            two_four_ghz_settings: Manual radio settings for 2.4 GHz.
            five_ghz_settings: Manual radio settings for 5 GHz.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/radio/settings"

        payload = {}
        if rf_profile_id is not None:
            payload["rfProfileId"] = rf_profile_id
        if two_four_ghz_settings is not None:
            payload["twoFourGhzSettings"] = two_four_ghz_settings
        if five_ghz_settings is not None:
            payload["fiveGhzSettings"] = five_ghz_settings

        return await self._session.put(
            scope="appliance",
            operation_id="updateDeviceApplianceRadioSettings",
            path=path,
            json=payload,
        )

    async def get_device_appliance_uplinks_settings(self, *, serial: str) -> dict[str, Any] | None:
        """Return the uplink settings for an MX appliance.

        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-uplinks-settings

        Args:
            serial: Serial.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/uplinks/settings"

        return await self._session.get(
            scope="appliance", operation_id="getDeviceApplianceUplinksSettings", path=path
        )

    async def update_device_appliance_uplinks_settings(
        self, *, serial: str, interfaces: dict
    ) -> dict[str, Any] | None:
        """Update the uplink settings for an MX appliance.

        https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-uplinks-settings

        Args:
            serial: Serial.
            interfaces: Interface settings.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/uplinks/settings"

        payload = {}
        if interfaces is not None:
            payload["interfaces"] = interfaces

        return await self._session.put(
            scope="appliance",
            operation_id="updateDeviceApplianceUplinksSettings",
            path=path,
            json=payload,
        )

    async def create_device_appliance_vmx_authentication_token(
        self, *, serial: str
    ) -> dict[str, Any] | None:
        """Generate a new vMX authentication token.

        https://developer.cisco.com/meraki/api-v1/#!create-device-appliance-vmx-authentication-token

        Args:
            serial: Serial.

        """
        serial = urllib.parse.quote(str(serial), safe="")
        path = f"/devices/{serial}/appliance/vmx/authenticationToken"

        return await self._session.post(
            scope="appliance", operation_id="createDeviceApplianceVmxAuthenticationToken", path=path
        )

    def get_network_appliance_client_security_events(
        self,
        *,
        network_id: str,
        client_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List the security events for a client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-client-security-events

        Args:
            network_id: Network ID.
            client_id: Client ID.
            t0: The beginning of the timespan for the data. Data is gathered after the specified t0
              value. The maximum lookback period is 791 days from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 791 days. The default is 31 days.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sort_order: Sorted order of security events based on event detection time. Order options
              are 'ascending' or 'descending'. Default is ascending order.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        path = f"/networks/{network_id}/appliance/clients/{client_id}/security/events"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if sort_order is not None:
            params["sortOrder"] = sort_order

        return self._session.get_pages(
            scope="appliance",
            operation_id="getNetworkApplianceClientSecurityEvents",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_network_appliance_connectivity_monitoring_destinations(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the connectivity testing destinations for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-connectivity-monitoring-destinations

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/connectivityMonitoringDestinations"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceConnectivityMonitoringDestinations",
            path=path,
        )

    async def update_network_appliance_connectivity_monitoring_destinations(
        self, *, network_id: str, destinations: list | None = None
    ) -> dict[str, Any] | None:
        """Update the connectivity testing destinations for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-connectivity-monitoring-destinations

        Args:
            network_id: Network ID.
            destinations: The list of connectivity monitoring destinations.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/connectivityMonitoringDestinations"

        payload = {}
        if destinations is not None:
            payload["destinations"] = destinations

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceConnectivityMonitoringDestinations",
            path=path,
            json=payload,
        )

    async def get_network_appliance_content_filtering(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the content filtering settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/contentFiltering"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceContentFiltering", path=path
        )

    async def update_network_appliance_content_filtering(
        self,
        *,
        network_id: str,
        allowed_url_patterns: list | None = None,
        blocked_url_patterns: list | None = None,
        blocked_url_categories: list | None = None,
        url_category_list_size: str | None = None,
    ) -> dict[str, Any] | None:
        """Update the content filtering settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-content-filtering

        Args:
            network_id: Network ID.
            allowed_url_patterns: A list of URL patterns that are allowed.
            blocked_url_patterns: A list of URL patterns that are blocked.
            blocked_url_categories: A list of URL categories to block.
            url_category_list_size: URL category list size which is either 'topSites' or 'fullList'.

        """
        if url_category_list_size is not None:
            options = ["fullList", "topSites"]
            assert url_category_list_size in options, (
                f'"url_category_list_size" cannot be "{url_category_list_size}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/contentFiltering"

        payload = {}
        if allowed_url_patterns is not None:
            payload["allowedUrlPatterns"] = allowed_url_patterns
        if blocked_url_patterns is not None:
            payload["blockedUrlPatterns"] = blocked_url_patterns
        if blocked_url_categories is not None:
            payload["blockedUrlCategories"] = blocked_url_categories
        if url_category_list_size is not None:
            payload["urlCategoryListSize"] = url_category_list_size

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceContentFiltering",
            path=path,
            json=payload,
        )

    async def get_network_appliance_content_filtering_categories(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List all available content filtering categories for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering-categories

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/contentFiltering/categories"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceContentFilteringCategories",
            path=path,
        )

    async def get_network_appliance_firewall_cellular_firewall_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the cellular firewall rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-cellular-firewall-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/cellularFirewallRules"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceFirewallCellularFirewallRules",
            path=path,
        )

    async def update_network_appliance_firewall_cellular_firewall_rules(
        self, *, network_id: str, rules: list | None = None
    ) -> dict[str, Any] | None:
        """Update the cellular firewall rules of an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-cellular-firewall-rules

        Args:
            network_id: Network ID.
            rules: An ordered array of the firewall rules (not including the default rule).

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/cellularFirewallRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallCellularFirewallRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_firewalled_services(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List the appliance services and their accessibility rules.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-services

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/firewalledServices"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceFirewallFirewalledServices",
            path=path,
        )

    async def get_network_appliance_firewall_firewalled_service(
        self, *, network_id: str, service: str
    ) -> dict[str, Any] | None:
        """Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP').

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-service

        Args:
            network_id: Network ID.
            service: Service.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        service = urllib.parse.quote(str(service), safe="")
        path = f"/networks/{network_id}/appliance/firewall/firewalledServices/{service}"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceFirewallFirewalledService",
            path=path,
        )

    async def update_network_appliance_firewall_firewalled_service(
        self, *, network_id: str, service: str, access: str, allowed_ips: list | None = None
    ) -> dict[str, Any] | None:
        """Updates the accessibility settings for the given service ('ICMP', 'web', or 'SNMP').

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-firewalled-service

        Args:
            network_id: Network ID.
            service: Service.
            access: A string indicating the rule for which IPs are allowed to use the specified
              service. Acceptable values are "blocked" (no remote IPs can access the
              service), "restricted" (only allowed IPs can access the service), and
              "unrestriced" (any remote IP can access the service). This field is
              required.
            allowed_ips: An array of allowed CIDRs that can access the service. This field is
              required if "access" is set to "restricted". Otherwise this field is
              ignored.

        """
        if access is not None:
            options = ["blocked", "restricted", "unrestricted"]
            assert access in options, (
                f'"access" cannot be "{access}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        service = urllib.parse.quote(str(service), safe="")
        path = f"/networks/{network_id}/appliance/firewall/firewalledServices/{service}"

        payload = {}
        if access is not None:
            payload["access"] = access
        if allowed_ips is not None:
            payload["allowedIps"] = allowed_ips

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallFirewalledService",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_inbound_cellular_firewall_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the inbound cellular firewall rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-cellular-firewall-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/inboundCellularFirewallRules"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceFirewallInboundCellularFirewallRules",
            path=path,
        )

    async def update_network_appliance_firewall_inbound_cellular_firewall_rules(
        self, *, network_id: str, rules: list | None = None
    ) -> dict[str, Any] | None:
        """Update the inbound cellular firewall rules of an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-inbound-cellular-firewall-rules

        Args:
            network_id: Network ID.
            rules: An ordered array of the firewall rules (not including the default rule).

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/inboundCellularFirewallRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallInboundCellularFirewallRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_inbound_firewall_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the inbound firewall rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-firewall-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/inboundFirewallRules"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceFirewallInboundFirewallRules",
            path=path,
        )

    async def update_network_appliance_firewall_inbound_firewall_rules(
        self, *, network_id: str, rules: list | None = None, syslog_default_rule: bool | None = None
    ) -> dict[str, Any] | None:
        """Update the inbound firewall rules of an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-inbound-firewall-rules

        Args:
            network_id: Network ID.
            rules: An ordered array of the firewall rules (not including the default rule).
            syslog_default_rule: Log the special default rule (boolean value - enable only if you've
              configured a syslog server) (optional).

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/inboundFirewallRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules
        if syslog_default_rule is not None:
            payload["syslogDefaultRule"] = syslog_default_rule

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallInboundFirewallRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_l3_firewall_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the L3 firewall rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-3-firewall-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/l3FirewallRules"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceFirewallL3FirewallRules", path=path
        )

    async def update_network_appliance_firewall_l3_firewall_rules(
        self, *, network_id: str, rules: list | None = None, syslog_default_rule: bool | None = None
    ) -> dict[str, Any] | None:
        """Update the L3 firewall rules of an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-3-firewall-rules

        Args:
            network_id: Network ID.
            rules: An ordered array of the firewall rules (not including the default rule).
            syslog_default_rule: Log the special default rule (boolean value - enable only if you've
              configured a syslog server) (optional).

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/l3FirewallRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules
        if syslog_default_rule is not None:
            payload["syslogDefaultRule"] = syslog_default_rule

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallL3FirewallRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_l7_firewall_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List the MX L7 firewall rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/l7FirewallRules"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceFirewallL7FirewallRules", path=path
        )

    async def update_network_appliance_firewall_l7_firewall_rules(
        self, *, network_id: str, rules: list | None = None
    ) -> dict[str, Any] | None:
        """Update the MX L7 firewall rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules

        Args:
            network_id: Network ID.
            rules: An ordered array of the MX L7 firewall rules.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/l7FirewallRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallL7FirewallRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_l7_firewall_rules_application_categories(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the L7 firewall application categories and their associated applications for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules-application-categories

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/l7FirewallRules/applicationCategories"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceFirewallL7FirewallRulesApplicationCategories",
            path=path,
        )

    async def update_network_appliance_firewall_multicast_forwarding(
        self, *, network_id: str, rules: list
    ) -> dict[str, Any] | None:
        """Update static multicast forward rules for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-multicast-forwarding

        Args:
            network_id: Network ID.
            rules: Static multicast forwarding rules. Pass an empty array to clear all rules.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/multicastForwarding"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallMulticastForwarding",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_one_to_many_nat_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the 1:Many NAT mapping rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-many-nat-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/oneToManyNatRules"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceFirewallOneToManyNatRules",
            path=path,
        )

    async def update_network_appliance_firewall_one_to_many_nat_rules(
        self, *, network_id: str, rules: list
    ) -> dict[str, Any] | None:
        """Set the 1:Many NAT mapping rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-many-nat-rules

        Args:
            network_id: Network ID.
            rules: An array of 1:Many nat rules.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/oneToManyNatRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallOneToManyNatRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_one_to_one_nat_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the 1:1 NAT mapping rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-one-nat-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/oneToOneNatRules"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceFirewallOneToOneNatRules", path=path
        )

    async def update_network_appliance_firewall_one_to_one_nat_rules(
        self, *, network_id: str, rules: list
    ) -> dict[str, Any] | None:
        """Set the 1:1 NAT mapping rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-one-nat-rules

        Args:
            network_id: Network ID.
            rules: An array of 1:1 nat rules.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/oneToOneNatRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallOneToOneNatRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_port_forwarding_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the port forwarding rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-port-forwarding-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/portForwardingRules"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceFirewallPortForwardingRules",
            path=path,
        )

    async def update_network_appliance_firewall_port_forwarding_rules(
        self, *, network_id: str, rules: list
    ) -> dict[str, Any] | None:
        """Update the port forwarding rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-port-forwarding-rules

        Args:
            network_id: Network ID.
            rules: An array of port forwarding params.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/portForwardingRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallPortForwardingRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_firewall_settings(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the firewall settings for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-settings

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/settings"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceFirewallSettings", path=path
        )

    async def update_network_appliance_firewall_settings(
        self, *, network_id: str, spoofing_protection: dict | None = None
    ) -> dict[str, Any] | None:
        """Update the firewall settings for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-settings

        Args:
            network_id: Network ID.
            spoofing_protection: Spoofing protection settings.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/firewall/settings"

        payload = {}
        if spoofing_protection is not None:
            payload["spoofingProtection"] = spoofing_protection

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceFirewallSettings",
            path=path,
            json=payload,
        )

    async def get_network_appliance_ports(self, *, network_id: str) -> dict[str, Any] | None:
        """List per-port VLAN settings for all ports of a MX.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ports

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/ports"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkAppliancePorts", path=path
        )

    async def get_network_appliance_port(
        self, *, network_id: str, port_id: str
    ) -> dict[str, Any] | None:
        """Return per-port VLAN settings for a single MX port.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-port

        Args:
            network_id: Network ID.
            port_id: Port ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        port_id = urllib.parse.quote(str(port_id), safe="")
        path = f"/networks/{network_id}/appliance/ports/{port_id}"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkAppliancePort", path=path
        )

    async def update_network_appliance_port(
        self,
        *,
        network_id: str,
        port_id: str,
        enabled: bool | None = None,
        drop_untagged_traffic: bool | None = None,
        type_: str | None = None,
        vlan: int | None = None,
        allowed_vlans: str | None = None,
        access_policy: str | None = None,
    ) -> dict[str, Any] | None:
        """Update the per-port VLAN settings for a single MX port.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port

        Args:
            network_id: Network ID.
            port_id: Port ID.
            enabled: The status of the port.
            drop_untagged_traffic: Trunk port can Drop all Untagged traffic. When true, no VLAN is
              required. Access ports cannot have dropUntaggedTraffic set to true.
            type_: The type of the port: 'access' or 'trunk'.
            vlan: Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access
              mode.
            allowed_vlans: Comma-delimited list of the VLAN ID's allowed on the port, or 'all' to
              permit all VLAN's on the port.
            access_policy: The name of the policy. Only applicable to Access ports. Valid values
              are: 'open', '8021x-radius', 'mac-radius', 'hybris-radius' for MX64 or Z3
              or any MX supporting the per port authentication feature. Otherwise,
              'open' is the only valid value and 'open' is the default value if the
              field is missing.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        port_id = urllib.parse.quote(str(port_id), safe="")
        path = f"/networks/{network_id}/appliance/ports/{port_id}"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if drop_untagged_traffic is not None:
            payload["dropUntaggedTraffic"] = drop_untagged_traffic
        if type_ is not None:
            payload["type"] = type_
        if vlan is not None:
            payload["vlan"] = vlan
        if allowed_vlans is not None:
            payload["allowedVlans"] = allowed_vlans
        if access_policy is not None:
            payload["accessPolicy"] = access_policy

        return await self._session.put(
            scope="appliance", operation_id="updateNetworkAppliancePort", path=path, json=payload
        )

    async def get_network_appliance_prefixes_delegated_statics(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List static delegated prefixes for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-prefixes-delegated-statics

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/prefixes/delegated/statics"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkAppliancePrefixesDelegatedStatics", path=path
        )

    async def create_network_appliance_prefixes_delegated_static(
        self, *, network_id: str, prefix: str, origin: dict, description: str | None = None
    ) -> dict[str, Any] | None:
        """Add a static delegated prefix from a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-prefixes-delegated-static

        Args:
            network_id: Network ID.
            prefix: A static IPv6 prefix.
            origin: The origin of the prefix.
            description: A name or description for the prefix.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/prefixes/delegated/statics"

        payload = {}
        if prefix is not None:
            payload["prefix"] = prefix
        if origin is not None:
            payload["origin"] = origin
        if description is not None:
            payload["description"] = description

        return await self._session.post(
            scope="appliance",
            operation_id="createNetworkAppliancePrefixesDelegatedStatic",
            path=path,
            json=payload,
        )

    async def get_network_appliance_prefixes_delegated_static(
        self, *, network_id: str, static_delegated_prefix_id: str
    ) -> dict[str, Any] | None:
        """Return a static delegated prefix from a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-prefixes-delegated-static

        Args:
            network_id: Network ID.
            static_delegated_prefix_id: Static delegated prefix ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        static_delegated_prefix_id = urllib.parse.quote(str(static_delegated_prefix_id), safe="")
        path = f"/networks/{network_id}/appliance/prefixes/delegated/statics/{static_delegated_prefix_id}"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkAppliancePrefixesDelegatedStatic", path=path
        )

    async def update_network_appliance_prefixes_delegated_static(
        self,
        *,
        network_id: str,
        static_delegated_prefix_id: str,
        prefix: str | None = None,
        origin: dict | None = None,
        description: str | None = None,
    ) -> dict[str, Any] | None:
        """Update a static delegated prefix from a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-prefixes-delegated-static

        Args:
            network_id: Network ID.
            static_delegated_prefix_id: Static delegated prefix ID.
            prefix: A static IPv6 prefix.
            origin: The origin of the prefix.
            description: A name or description for the prefix.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        static_delegated_prefix_id = urllib.parse.quote(str(static_delegated_prefix_id), safe="")
        path = f"/networks/{network_id}/appliance/prefixes/delegated/statics/{static_delegated_prefix_id}"

        payload = {}
        if prefix is not None:
            payload["prefix"] = prefix
        if origin is not None:
            payload["origin"] = origin
        if description is not None:
            payload["description"] = description

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkAppliancePrefixesDelegatedStatic",
            path=path,
            json=payload,
        )

    async def delete_network_appliance_prefixes_delegated_static(
        self, *, network_id: str, static_delegated_prefix_id: str
    ) -> None:
        """Delete a static delegated prefix from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-prefixes-delegated-static

        Args:
            network_id: Network ID.
            static_delegated_prefix_id: Static delegated prefix ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        static_delegated_prefix_id = urllib.parse.quote(str(static_delegated_prefix_id), safe="")
        path = f"/networks/{network_id}/appliance/prefixes/delegated/statics/{static_delegated_prefix_id}"

        return await self._session.delete(
            scope="appliance",
            operation_id="deleteNetworkAppliancePrefixesDelegatedStatic",
            path=path,
        )

    async def get_network_appliance_rf_profiles(self, *, network_id: str) -> dict[str, Any] | None:
        """List the RF profiles for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-rf-profiles

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/rfProfiles"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceRfProfiles", path=path
        )

    async def create_network_appliance_rf_profile(
        self,
        *,
        network_id: str,
        name: str,
        two_four_ghz_settings: dict | None = None,
        five_ghz_settings: dict | None = None,
        per_ssid_settings: dict | None = None,
    ) -> dict[str, Any] | None:
        """Creates new RF profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-rf-profile

        Args:
            network_id: Network ID.
            name: The name of the new profile. Must be unique. This param is required on creation.
            two_four_ghz_settings: Settings related to 2.4Ghz band.
            five_ghz_settings: Settings related to 5Ghz band.
            per_ssid_settings: Per-SSID radio settings by number.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/rfProfiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if two_four_ghz_settings is not None:
            payload["twoFourGhzSettings"] = two_four_ghz_settings
        if five_ghz_settings is not None:
            payload["fiveGhzSettings"] = five_ghz_settings
        if per_ssid_settings is not None:
            payload["perSsidSettings"] = per_ssid_settings

        return await self._session.post(
            scope="appliance",
            operation_id="createNetworkApplianceRfProfile",
            path=path,
            json=payload,
        )

    async def get_network_appliance_rf_profile(
        self, *, network_id: str, rf_profile_id: str
    ) -> dict[str, Any] | None:
        """Return a RF profile.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-rf-profile

        Args:
            network_id: Network ID.
            rf_profile_id: Rf profile ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        rf_profile_id = urllib.parse.quote(str(rf_profile_id), safe="")
        path = f"/networks/{network_id}/appliance/rfProfiles/{rf_profile_id}"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceRfProfile", path=path
        )

    async def update_network_appliance_rf_profile(
        self,
        *,
        network_id: str,
        rf_profile_id: str,
        name: str | None = None,
        two_four_ghz_settings: dict | None = None,
        five_ghz_settings: dict | None = None,
        per_ssid_settings: dict | None = None,
    ) -> dict[str, Any] | None:
        """Updates specified RF profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-rf-profile

        Args:
            network_id: Network ID.
            rf_profile_id: Rf profile ID.
            name: The name of the new profile. Must be unique.
            two_four_ghz_settings: Settings related to 2.4Ghz band.
            five_ghz_settings: Settings related to 5Ghz band.
            per_ssid_settings: Per-SSID radio settings by number.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        rf_profile_id = urllib.parse.quote(str(rf_profile_id), safe="")
        path = f"/networks/{network_id}/appliance/rfProfiles/{rf_profile_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if two_four_ghz_settings is not None:
            payload["twoFourGhzSettings"] = two_four_ghz_settings
        if five_ghz_settings is not None:
            payload["fiveGhzSettings"] = five_ghz_settings
        if per_ssid_settings is not None:
            payload["perSsidSettings"] = per_ssid_settings

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceRfProfile",
            path=path,
            json=payload,
        )

    async def delete_network_appliance_rf_profile(
        self, *, network_id: str, rf_profile_id: str
    ) -> None:
        """Delete a RF Profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-rf-profile

        Args:
            network_id: Network ID.
            rf_profile_id: Rf profile ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        rf_profile_id = urllib.parse.quote(str(rf_profile_id), safe="")
        path = f"/networks/{network_id}/appliance/rfProfiles/{rf_profile_id}"

        return await self._session.delete(
            scope="appliance", operation_id="deleteNetworkApplianceRfProfile", path=path
        )

    async def update_network_appliance_sdwan_internet_policies(
        self, *, network_id: str, wan_traffic_uplink_preferences: list | None = None
    ) -> dict[str, Any] | None:
        """Update SDWAN internet traffic preferences for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-sdwan-internet-policies

        Args:
            network_id: Network ID.
            wan_traffic_uplink_preferences: policies with respective traffic filters for an MX
              network.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/sdwan/internetPolicies"

        payload = {}
        if wan_traffic_uplink_preferences is not None:
            payload["wanTrafficUplinkPreferences"] = wan_traffic_uplink_preferences

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceSdwanInternetPolicies",
            path=path,
            json=payload,
        )

    def get_network_appliance_security_events(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List the security events for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-events

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. Data is gathered after the specified t0
              value. The maximum lookback period is 365 days from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 365 days. The default is 31 days.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sort_order: Sorted order of security events based on event detection time. Order options
              are 'ascending' or 'descending'. Default is ascending order.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/security/events"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if sort_order is not None:
            params["sortOrder"] = sort_order

        return self._session.get_pages(
            scope="appliance",
            operation_id="getNetworkApplianceSecurityEvents",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_network_appliance_security_intrusion(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Returns all supported intrusion settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-intrusion

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/security/intrusion"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceSecurityIntrusion", path=path
        )

    async def update_network_appliance_security_intrusion(
        self,
        *,
        network_id: str,
        mode: str | None = None,
        ids_rulesets: str | None = None,
        protected_networks: dict | None = None,
    ) -> dict[str, Any] | None:
        """Set the supported intrusion settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-intrusion

        Args:
            network_id: Network ID.
            mode: Set mode to 'disabled'/'detection'/'prevention' (optional - omitting will leave
              current config unchanged).
            ids_rulesets: Set the detection ruleset 'connectivity'/'balanced'/'security' (optional -
              omitting will leave current config unchanged). Default value is 'balanced'
              if none currently saved.
            protected_networks: Set the included/excluded networks from the intrusion engine
              (optional - omitting will leave current config unchanged). This is
              available only in 'passthrough' mode.

        """
        if mode is not None:
            options = ["detection", "disabled", "prevention"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'
        if ids_rulesets is not None:
            options = ["balanced", "connectivity", "security"]
            assert ids_rulesets in options, (
                f'"ids_rulesets" cannot be "{ids_rulesets}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/security/intrusion"

        payload = {}
        if mode is not None:
            payload["mode"] = mode
        if ids_rulesets is not None:
            payload["idsRulesets"] = ids_rulesets
        if protected_networks is not None:
            payload["protectedNetworks"] = protected_networks

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceSecurityIntrusion",
            path=path,
            json=payload,
        )

    async def get_network_appliance_security_malware(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Returns all supported malware settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-malware

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/security/malware"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceSecurityMalware", path=path
        )

    async def update_network_appliance_security_malware(
        self,
        *,
        network_id: str,
        mode: str,
        allowed_urls: list | None = None,
        allowed_files: list | None = None,
    ) -> dict[str, Any] | None:
        """Set the supported malware settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-malware

        Args:
            network_id: Network ID.
            mode: Set mode to 'enabled' to enable malware prevention, otherwise 'disabled'.
            allowed_urls: The urls that should be permitted by the malware detection engine. If
              omitted, the current config will remain unchanged. This is available only
              if your network supports AMP allow listing.
            allowed_files: The sha256 digests of files that should be permitted by the malware
              detection engine. If omitted, the current config will remain unchanged.
              This is available only if your network supports AMP allow listing.

        """
        if mode is not None:
            options = ["disabled", "enabled"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'

        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/security/malware"

        payload = {}
        if mode is not None:
            payload["mode"] = mode
        if allowed_urls is not None:
            payload["allowedUrls"] = allowed_urls
        if allowed_files is not None:
            payload["allowedFiles"] = allowed_files

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceSecurityMalware",
            path=path,
            json=payload,
        )

    async def get_network_appliance_settings(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the appliance settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-settings

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/settings"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceSettings", path=path
        )

    async def update_network_appliance_settings(
        self,
        *,
        network_id: str,
        client_tracking_method: str | None = None,
        deployment_mode: str | None = None,
        dynamic_dns: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the appliance settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-settings

        Args:
            network_id: Network ID.
            client_tracking_method: Client tracking method of a network.
            deployment_mode: Deployment mode of a network.
            dynamic_dns: Dynamic DNS settings for a network.

        """
        if client_tracking_method is not None:
            options = ["IP address", "MAC address", "Unique client identifier"]
            assert client_tracking_method in options, (
                f'"client_tracking_method" cannot be "{client_tracking_method}", & must be set to one of: {options}'
            )
        if deployment_mode is not None:
            options = ["passthrough", "routed"]
            assert deployment_mode in options, (
                f'"deployment_mode" cannot be "{deployment_mode}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/settings"

        payload = {}
        if client_tracking_method is not None:
            payload["clientTrackingMethod"] = client_tracking_method
        if deployment_mode is not None:
            payload["deploymentMode"] = deployment_mode
        if dynamic_dns is not None:
            payload["dynamicDns"] = dynamic_dns

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceSettings",
            path=path,
            json=payload,
        )

    async def get_network_appliance_single_lan(self, *, network_id: str) -> dict[str, Any] | None:
        """Return single LAN configuration.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-single-lan

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/singleLan"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceSingleLan", path=path
        )

    async def update_network_appliance_single_lan(
        self,
        *,
        network_id: str,
        subnet: str | None = None,
        appliance_ip: str | None = None,
        ipv6: dict | None = None,
        mandatory_dhcp: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update single LAN configuration.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-single-lan

        Args:
            network_id: Network ID.
            subnet: The subnet of the single LAN configuration.
            appliance_ip: The appliance IP address of the single LAN.
            ipv6: IPv6 configuration on the VLAN.
            mandatory_dhcp: Mandatory DHCP will enforce that clients connecting to this LAN must use
              the IP address assigned by the DHCP server. Clients who use a static IP
              address won't be able to associate. Only available on firmware versions
              17.0 and above.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/singleLan"

        payload = {}
        if subnet is not None:
            payload["subnet"] = subnet
        if appliance_ip is not None:
            payload["applianceIp"] = appliance_ip
        if ipv6 is not None:
            payload["ipv6"] = ipv6
        if mandatory_dhcp is not None:
            payload["mandatoryDhcp"] = mandatory_dhcp

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceSingleLan",
            path=path,
            json=payload,
        )

    async def get_network_appliance_ssids(self, *, network_id: str) -> dict[str, Any] | None:
        """List the MX SSIDs in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ssids

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/ssids"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceSsids", path=path
        )

    async def get_network_appliance_ssid(
        self, *, network_id: str, number: str
    ) -> dict[str, Any] | None:
        """Return a single MX SSID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ssid

        Args:
            network_id: Network ID.
            number: Number.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        path = f"/networks/{network_id}/appliance/ssids/{number}"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceSsid", path=path
        )

    async def update_network_appliance_ssid(
        self,
        *,
        network_id: str,
        number: str,
        name: str | None = None,
        enabled: bool | None = None,
        default_vlan_id: int | None = None,
        auth_mode: str | None = None,
        psk: str | None = None,
        radius_servers: list | None = None,
        encryption_mode: str | None = None,
        wpa_encryption_mode: str | None = None,
        visible: bool | None = None,
        dhcp_enforced_deauthentication: dict | None = None,
        dot11w: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the attributes of an MX SSID.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-ssid

        Args:
            network_id: Network ID.
            number: Number.
            name: The name of the SSID.
            enabled: Whether or not the SSID is enabled.
            default_vlan_id: The VLAN ID of the VLAN associated to this SSID. This parameter is only
              valid if the network is in routed mode.
            auth_mode: The association control method for the SSID ('open', 'psk', '8021x-meraki' or
              '8021x-radius').
            psk: The passkey for the SSID. This param is only valid if the authMode is 'psk'.
            radius_servers: The RADIUS 802.1x servers to be used for authentication. This param is
              only valid if the authMode is '8021x-radius'.
            encryption_mode: The psk encryption mode for the SSID ('wep' or 'wpa'). This param is
              only valid if the authMode is 'psk'.
            wpa_encryption_mode: The types of WPA encryption. ('WPA1 and WPA2', 'WPA2 only', 'WPA3
              Transition Mode' or 'WPA3 only'). This param is only valid if (1) the
              authMode is 'psk' & the encryptionMode is 'wpa' OR (2) the authMode is
              '8021x-meraki' OR (3) the authMode is '8021x-radius'.
            visible: Boolean indicating whether the MX should advertise or hide this SSID.
            dhcp_enforced_deauthentication: DHCP Enforced Deauthentication enables the
              disassociation of wireless clients in addition to Mandatory DHCP. This
              param is only valid on firmware versions >= MX 17.0 where the associated
              LAN has Mandatory DHCP Enabled.
            dot11w: The current setting for Protected Management Frames (802.11w).

        """
        if auth_mode is not None:
            options = ["8021x-meraki", "8021x-radius", "open", "psk"]
            assert auth_mode in options, (
                f'"auth_mode" cannot be "{auth_mode}", & must be set to one of: {options}'
            )
        if encryption_mode is not None:
            options = ["wep", "wpa"]
            assert encryption_mode in options, (
                f'"encryption_mode" cannot be "{encryption_mode}", & must be set to one of: {options}'
            )
        if wpa_encryption_mode is not None:
            options = ["WPA1 and WPA2", "WPA2 only", "WPA3 Transition Mode", "WPA3 only"]
            assert wpa_encryption_mode in options, (
                f'"wpa_encryption_mode" cannot be "{wpa_encryption_mode}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        number = urllib.parse.quote(str(number), safe="")
        path = f"/networks/{network_id}/appliance/ssids/{number}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if enabled is not None:
            payload["enabled"] = enabled
        if default_vlan_id is not None:
            payload["defaultVlanId"] = default_vlan_id
        if auth_mode is not None:
            payload["authMode"] = auth_mode
        if psk is not None:
            payload["psk"] = psk
        if radius_servers is not None:
            payload["radiusServers"] = radius_servers
        if encryption_mode is not None:
            payload["encryptionMode"] = encryption_mode
        if wpa_encryption_mode is not None:
            payload["wpaEncryptionMode"] = wpa_encryption_mode
        if visible is not None:
            payload["visible"] = visible
        if dhcp_enforced_deauthentication is not None:
            payload["dhcpEnforcedDeauthentication"] = dhcp_enforced_deauthentication
        if dot11w is not None:
            payload["dot11w"] = dot11w

        return await self._session.put(
            scope="appliance", operation_id="updateNetworkApplianceSsid", path=path, json=payload
        )

    async def get_network_appliance_static_routes(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List the static routes for an MX or teleworker network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-routes

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/staticRoutes"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceStaticRoutes", path=path
        )

    async def create_network_appliance_static_route(
        self,
        *,
        network_id: str,
        name: str,
        subnet: str,
        gateway_ip: str,
        gateway_vlan_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Add a static route for an MX or teleworker network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-static-route

        Args:
            network_id: Network ID.
            name: Name of the route.
            subnet: Subnet of the route.
            gateway_ip: Gateway IP address (next hop).
            gateway_vlan_id: Gateway VLAN ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/staticRoutes"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if gateway_ip is not None:
            payload["gatewayIp"] = gateway_ip
        if gateway_vlan_id is not None:
            payload["gatewayVlanId"] = gateway_vlan_id

        return await self._session.post(
            scope="appliance",
            operation_id="createNetworkApplianceStaticRoute",
            path=path,
            json=payload,
        )

    async def get_network_appliance_static_route(
        self, *, network_id: str, static_route_id: str
    ) -> dict[str, Any] | None:
        """Return a static route for an MX or teleworker network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-route

        Args:
            network_id: Network ID.
            static_route_id: Static route ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        path = f"/networks/{network_id}/appliance/staticRoutes/{static_route_id}"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceStaticRoute", path=path
        )

    async def update_network_appliance_static_route(
        self,
        *,
        network_id: str,
        static_route_id: str,
        name: str | None = None,
        subnet: str | None = None,
        gateway_ip: str | None = None,
        gateway_vlan_id: str | None = None,
        enabled: bool | None = None,
        fixed_ip_assignments: dict | None = None,
        reserved_ip_ranges: list | None = None,
    ) -> dict[str, Any] | None:
        """Update a static route for an MX or teleworker network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-static-route

        Args:
            network_id: Network ID.
            static_route_id: Static route ID.
            name: Name of the route.
            subnet: Subnet of the route.
            gateway_ip: Gateway IP address (next hop).
            gateway_vlan_id: Gateway VLAN ID.
            enabled: Whether the route should be enabled or not.
            fixed_ip_assignments: Fixed DHCP IP assignments on the route.
            reserved_ip_ranges: DHCP reserved IP ranges.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        path = f"/networks/{network_id}/appliance/staticRoutes/{static_route_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if gateway_ip is not None:
            payload["gatewayIp"] = gateway_ip
        if gateway_vlan_id is not None:
            payload["gatewayVlanId"] = gateway_vlan_id
        if enabled is not None:
            payload["enabled"] = enabled
        if fixed_ip_assignments is not None:
            payload["fixedIpAssignments"] = fixed_ip_assignments
        if reserved_ip_ranges is not None:
            payload["reservedIpRanges"] = reserved_ip_ranges

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceStaticRoute",
            path=path,
            json=payload,
        )

    async def delete_network_appliance_static_route(
        self, *, network_id: str, static_route_id: str
    ) -> None:
        """Delete a static route from an MX or teleworker network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-static-route

        Args:
            network_id: Network ID.
            static_route_id: Static route ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        static_route_id = urllib.parse.quote(str(static_route_id), safe="")
        path = f"/networks/{network_id}/appliance/staticRoutes/{static_route_id}"

        return await self._session.delete(
            scope="appliance", operation_id="deleteNetworkApplianceStaticRoute", path=path
        )

    async def get_network_appliance_traffic_shaping(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Display the traffic shaping settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceTrafficShaping", path=path
        )

    async def update_network_appliance_traffic_shaping(
        self, *, network_id: str, global_bandwidth_limits: dict | None = None
    ) -> dict[str, Any] | None:
        """Update the traffic shaping settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping

        Args:
            network_id: Network ID.
            global_bandwidth_limits: Global per-client bandwidth limit.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping"

        payload = {}
        if global_bandwidth_limits is not None:
            payload["globalBandwidthLimits"] = global_bandwidth_limits

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceTrafficShaping",
            path=path,
            json=payload,
        )

    async def get_network_appliance_traffic_shaping_custom_performance_classes(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List all custom performance classes for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-classes

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceTrafficShapingCustomPerformanceClasses",
            path=path,
        )

    async def create_network_appliance_traffic_shaping_custom_performance_class(
        self,
        *,
        network_id: str,
        name: str,
        max_latency: int | None = None,
        max_jitter: int | None = None,
        max_loss_percentage: int | None = None,
    ) -> dict[str, Any] | None:
        """Add a custom performance class for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-traffic-shaping-custom-performance-class

        Args:
            network_id: Network ID.
            name: Name of the custom performance class.
            max_latency: Maximum latency in milliseconds.
            max_jitter: Maximum jitter in milliseconds.
            max_loss_percentage: Maximum percentage of packet loss.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses"

        payload = {}
        if name is not None:
            payload["name"] = name
        if max_latency is not None:
            payload["maxLatency"] = max_latency
        if max_jitter is not None:
            payload["maxJitter"] = max_jitter
        if max_loss_percentage is not None:
            payload["maxLossPercentage"] = max_loss_percentage

        return await self._session.post(
            scope="appliance",
            operation_id="createNetworkApplianceTrafficShapingCustomPerformanceClass",
            path=path,
            json=payload,
        )

    async def get_network_appliance_traffic_shaping_custom_performance_class(
        self, *, network_id: str, custom_performance_class_id: str
    ) -> dict[str, Any] | None:
        """Return a custom performance class for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-class

        Args:
            network_id: Network ID.
            custom_performance_class_id: Custom performance class ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        custom_performance_class_id = urllib.parse.quote(str(custom_performance_class_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses/{custom_performance_class_id}"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceTrafficShapingCustomPerformanceClass",
            path=path,
        )

    async def update_network_appliance_traffic_shaping_custom_performance_class(
        self,
        *,
        network_id: str,
        custom_performance_class_id: str,
        name: str | None = None,
        max_latency: int | None = None,
        max_jitter: int | None = None,
        max_loss_percentage: int | None = None,
    ) -> dict[str, Any] | None:
        """Update a custom performance class for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-custom-performance-class

        Args:
            network_id: Network ID.
            custom_performance_class_id: Custom performance class ID.
            name: Name of the custom performance class.
            max_latency: Maximum latency in milliseconds.
            max_jitter: Maximum jitter in milliseconds.
            max_loss_percentage: Maximum percentage of packet loss.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        custom_performance_class_id = urllib.parse.quote(str(custom_performance_class_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses/{custom_performance_class_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if max_latency is not None:
            payload["maxLatency"] = max_latency
        if max_jitter is not None:
            payload["maxJitter"] = max_jitter
        if max_loss_percentage is not None:
            payload["maxLossPercentage"] = max_loss_percentage

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceTrafficShapingCustomPerformanceClass",
            path=path,
            json=payload,
        )

    async def delete_network_appliance_traffic_shaping_custom_performance_class(
        self, *, network_id: str, custom_performance_class_id: str
    ) -> None:
        """Delete a custom performance class from an MX network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-traffic-shaping-custom-performance-class

        Args:
            network_id: Network ID.
            custom_performance_class_id: Custom performance class ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        custom_performance_class_id = urllib.parse.quote(str(custom_performance_class_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses/{custom_performance_class_id}"

        return await self._session.delete(
            scope="appliance",
            operation_id="deleteNetworkApplianceTrafficShapingCustomPerformanceClass",
            path=path,
        )

    async def get_network_appliance_traffic_shaping_rules(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Display the traffic shaping settings rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-rules

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/rules"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceTrafficShapingRules", path=path
        )

    async def update_network_appliance_traffic_shaping_rules(
        self,
        *,
        network_id: str,
        default_rules_enabled: bool | None = None,
        rules: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the traffic shaping settings rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-rules

        Args:
            network_id: Network ID.
            default_rules_enabled: Whether default traffic shaping rules are enabled (true) or
              disabled (false). There are 4 default rules, which can be seen on your
              network's traffic shaping page. Note that default rules count against the
              rule limit of 8.
            rules: An array of traffic shaping rules. Rules are applied in the order that they are
              specified in. An empty list (or null) means no rules. Note that you are
              allowed a maximum of 8 rules.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/rules"

        payload = {}
        if default_rules_enabled is not None:
            payload["defaultRulesEnabled"] = default_rules_enabled
        if rules is not None:
            payload["rules"] = rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceTrafficShapingRules",
            path=path,
            json=payload,
        )

    async def get_network_appliance_traffic_shaping_uplink_bandwidth(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Returns the uplink bandwidth limits for your MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-bandwidth

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/uplinkBandwidth"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceTrafficShapingUplinkBandwidth",
            path=path,
        )

    async def update_network_appliance_traffic_shaping_uplink_bandwidth(
        self, *, network_id: str, bandwidth_limits: dict | None = None
    ) -> dict[str, Any] | None:
        """Updates the uplink bandwidth settings for your MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-bandwidth

        Args:
            network_id: Network ID.
            bandwidth_limits: A mapping of uplinks to their bandwidth settings (be sure to check
              which uplinks are supported for your network).

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/uplinkBandwidth"

        payload = {}
        if bandwidth_limits is not None:
            payload["bandwidthLimits"] = bandwidth_limits

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceTrafficShapingUplinkBandwidth",
            path=path,
            json=payload,
        )

    async def get_network_appliance_traffic_shaping_uplink_selection(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Show uplink selection settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-selection

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/uplinkSelection"

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceTrafficShapingUplinkSelection",
            path=path,
        )

    async def update_network_appliance_traffic_shaping_uplink_selection(
        self,
        *,
        network_id: str,
        active_active_auto_vpn_enabled: bool | None = None,
        default_uplink: str | None = None,
        load_balancing_enabled: bool | None = None,
        failover_and_failback: dict | None = None,
        wan_traffic_uplink_preferences: list | None = None,
        vpn_traffic_uplink_preferences: list | None = None,
    ) -> dict[str, Any] | None:
        """Update uplink selection settings for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection

        Args:
            network_id: Network ID.
            active_active_auto_vpn_enabled: Toggle for enabling or disabling active-active AutoVPN.
            default_uplink: The default uplink. Must be a WAN interface 'wanX'.
            load_balancing_enabled: Toggle for enabling or disabling load balancing.
            failover_and_failback: WAN failover and failback behavior.
            wan_traffic_uplink_preferences: Array of uplink preference rules for WAN traffic.
            vpn_traffic_uplink_preferences: Array of uplink preference rules for VPN traffic.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/uplinkSelection"

        payload = {}
        if active_active_auto_vpn_enabled is not None:
            payload["activeActiveAutoVpnEnabled"] = active_active_auto_vpn_enabled
        if default_uplink is not None:
            payload["defaultUplink"] = default_uplink
        if load_balancing_enabled is not None:
            payload["loadBalancingEnabled"] = load_balancing_enabled
        if failover_and_failback is not None:
            payload["failoverAndFailback"] = failover_and_failback
        if wan_traffic_uplink_preferences is not None:
            payload["wanTrafficUplinkPreferences"] = wan_traffic_uplink_preferences
        if vpn_traffic_uplink_preferences is not None:
            payload["vpnTrafficUplinkPreferences"] = vpn_traffic_uplink_preferences

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceTrafficShapingUplinkSelection",
            path=path,
            json=payload,
        )

    async def update_network_appliance_traffic_shaping_vpn_exclusions(
        self, *, network_id: str, custom: list | None = None, major_applications: list | None = None
    ) -> dict[str, Any] | None:
        """Update VPN exclusion rules for an MX network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-vpn-exclusions

        Args:
            network_id: Network ID.
            custom: Custom VPN exclusion rules. Pass an empty array to clear existing rules.
            major_applications: Major Application based VPN exclusion rules. Pass an empty array to
              clear existing rules.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/trafficShaping/vpnExclusions"

        payload = {}
        if custom is not None:
            payload["custom"] = custom
        if major_applications is not None:
            payload["majorApplications"] = major_applications

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceTrafficShapingVpnExclusions",
            path=path,
            json=payload,
        )

    async def get_network_appliance_uplinks_usage_history(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
    ) -> dict[str, Any] | None:
        """Get the sent and received bytes for each uplink of a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-uplinks-usage-history

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 10 minutes.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              60, 300, 600, 1800, 3600, 86400. The default is 60.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/uplinks/usageHistory"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution

        return await self._session.get(
            scope="appliance",
            operation_id="getNetworkApplianceUplinksUsageHistory",
            path=path,
            params=params,
        )

    async def get_network_appliance_vlans(self, *, network_id: str) -> dict[str, Any] | None:
        """List the VLANs for a Cisco Secure Router network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/vlans"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceVlans", path=path
        )

    async def create_network_appliance_vlan(
        self,
        *,
        network_id: str,
        id_: str,
        name: str,
        subnet: str | None = None,
        appliance_ip: str | None = None,
        group_policy_id: str | None = None,
        template_vlan_type: str | None = None,
        cidr: str | None = None,
        mask: int | None = None,
        ipv6: dict | None = None,
        dhcp_handling: str | None = None,
        dhcp_relay_server_ips: list | None = None,
        dhcp_lease_time: str | None = None,
        mandatory_dhcp: dict | None = None,
        dhcp_boot_options_enabled: bool | None = None,
        dhcp_boot_next_server: str | None = None,
        dhcp_boot_filename: str | None = None,
        dhcp_options: list | None = None,
    ) -> dict[str, Any] | None:
        """Add a VLAN.

        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan

        Args:
            network_id: Network ID.
            id_: The VLAN ID of the new VLAN (must be between 1 and 4094).
            name: The name of the new VLAN.
            subnet: The subnet of the VLAN.
            appliance_ip: The local IP of the appliance on the VLAN.
            group_policy_id: The id of the desired group policy to apply to the VLAN.
            template_vlan_type: Type of subnetting of the VLAN. Applicable only for template
              network.
            cidr: CIDR of the pool of subnets. Applicable only for template network. Each network
              bound to the template will automatically pick a subnet from this pool to
              build its own VLAN.
            mask: Mask used for the subnet of all bound to the template networks. Applicable only
              for template network.
            ipv6: IPv6 configuration on the VLAN.
            dhcp_handling: The appliance's handling of DHCP requests on this VLAN. One of: 'Run a
              DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP
              requests'.
            dhcp_relay_server_ips: The IPs (IPv4) of the DHCP servers that DHCP requests should be
              relayed to. CIDR/subnet notation and hostnames are not supported.
            dhcp_lease_time: The term of DHCP leases if the appliance is running a DHCP server on
              this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day'
              or '1 week'.
            mandatory_dhcp: Mandatory DHCP will enforce that clients connecting to this VLAN must
              use the IP address assigned by the DHCP server. Clients who use a static
              IP address won't be able to associate. Only available on firmware versions
              17.0 and above.
            dhcp_boot_options_enabled: Use DHCP boot options specified in other properties.
            dhcp_boot_next_server: DHCP boot option to direct boot clients to the server to load the
              boot file from.
            dhcp_boot_filename: DHCP boot option for boot filename.
            dhcp_options: The list of DHCP options that will be included in DHCP responses. Each
              object in the list should have "code", "type", and "value" properties.

        """
        if template_vlan_type is not None:
            options = ["same", "unique"]
            assert template_vlan_type in options, (
                f'"template_vlan_type" cannot be "{template_vlan_type}", & must be set to one of: {options}'
            )
        if dhcp_handling is not None:
            options = [
                "Do not respond to DHCP requests",
                "Relay DHCP to another server",
                "Run a DHCP server",
            ]
            assert dhcp_handling in options, (
                f'"dhcp_handling" cannot be "{dhcp_handling}", & must be set to one of: {options}'
            )
        if dhcp_lease_time is not None:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert dhcp_lease_time in options, (
                f'"dhcp_lease_time" cannot be "{dhcp_lease_time}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/vlans"

        payload = {}
        if id_ is not None:
            payload["id"] = id_
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if appliance_ip is not None:
            payload["applianceIp"] = appliance_ip
        if group_policy_id is not None:
            payload["groupPolicyId"] = group_policy_id
        if template_vlan_type is not None:
            payload["templateVlanType"] = template_vlan_type
        if cidr is not None:
            payload["cidr"] = cidr
        if mask is not None:
            payload["mask"] = mask
        if ipv6 is not None:
            payload["ipv6"] = ipv6
        if dhcp_handling is not None:
            payload["dhcpHandling"] = dhcp_handling
        if dhcp_relay_server_ips is not None:
            payload["dhcpRelayServerIps"] = dhcp_relay_server_ips
        if dhcp_lease_time is not None:
            payload["dhcpLeaseTime"] = dhcp_lease_time
        if mandatory_dhcp is not None:
            payload["mandatoryDhcp"] = mandatory_dhcp
        if dhcp_boot_options_enabled is not None:
            payload["dhcpBootOptionsEnabled"] = dhcp_boot_options_enabled
        if dhcp_boot_next_server is not None:
            payload["dhcpBootNextServer"] = dhcp_boot_next_server
        if dhcp_boot_filename is not None:
            payload["dhcpBootFilename"] = dhcp_boot_filename
        if dhcp_options is not None:
            payload["dhcpOptions"] = dhcp_options

        return await self._session.post(
            scope="appliance", operation_id="createNetworkApplianceVlan", path=path, json=payload
        )

    async def get_network_appliance_vlans_settings(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Returns the enabled status of VLANs for the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans-settings

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/vlans/settings"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceVlansSettings", path=path
        )

    async def update_network_appliance_vlans_settings(
        self, *, network_id: str, vlans_enabled: bool | None = None
    ) -> dict[str, Any] | None:
        """Enable/Disable VLANs for the given network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlans-settings

        Args:
            network_id: Network ID.
            vlans_enabled: Boolean indicating whether to enable (true) or disable (false) VLANs for
              the network.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/vlans/settings"

        payload = {}
        if vlans_enabled is not None:
            payload["vlansEnabled"] = vlans_enabled

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceVlansSettings",
            path=path,
            json=payload,
        )

    async def get_network_appliance_vlan(
        self, *, network_id: str, vlan_id: str
    ) -> dict[str, Any] | None:
        """Return a VLAN.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlan

        Args:
            network_id: Network ID.
            vlan_id: Vlan ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        vlan_id = urllib.parse.quote(str(vlan_id), safe="")
        path = f"/networks/{network_id}/appliance/vlans/{vlan_id}"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceVlan", path=path
        )

    async def update_network_appliance_vlan(
        self,
        *,
        network_id: str,
        vlan_id: str,
        name: str | None = None,
        subnet: str | None = None,
        appliance_ip: str | None = None,
        group_policy_id: str | None = None,
        vpn_nat_subnet: str | None = None,
        dhcp_handling: str | None = None,
        dhcp_relay_server_ips: list | None = None,
        dhcp_lease_time: str | None = None,
        dhcp_boot_options_enabled: bool | None = None,
        dhcp_boot_next_server: str | None = None,
        dhcp_boot_filename: str | None = None,
        fixed_ip_assignments: dict | None = None,
        reserved_ip_ranges: list | None = None,
        dns_nameservers: str | None = None,
        dhcp_options: list | None = None,
        template_vlan_type: str | None = None,
        cidr: str | None = None,
        mask: int | None = None,
        ipv6: dict | None = None,
        mandatory_dhcp: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a VLAN.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan

        Args:
            network_id: Network ID.
            vlan_id: Vlan ID.
            name: The name of the VLAN.
            subnet: The subnet of the VLAN.
            appliance_ip: The local IP of the appliance on the VLAN.
            group_policy_id: The id of the desired group policy to apply to the VLAN.
            vpn_nat_subnet: The translated VPN subnet if VPN and VPN subnet translation are enabled
              on the VLAN.
            dhcp_handling: The appliance's handling of DHCP requests on this VLAN. One of: 'Run a
              DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP
              requests'.
            dhcp_relay_server_ips: The IPs (IPv4) of the DHCP servers that DHCP requests should be
              relayed to. CIDR/subnet notation and hostnames are not supported.
            dhcp_lease_time: The term of DHCP leases if the appliance is running a DHCP server on
              this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day'
              or '1 week'.
            dhcp_boot_options_enabled: Use DHCP boot options specified in other properties.
            dhcp_boot_next_server: DHCP boot option to direct boot clients to the server to load the
              boot file from.
            dhcp_boot_filename: DHCP boot option for boot filename.
            fixed_ip_assignments: The DHCP fixed IP assignments on the VLAN. This should be an
              object that contains mappings from MAC addresses to objects that
              themselves each contain "ip" and "name" string fields. See the sample
              request/response for more details.
            reserved_ip_ranges: The DHCP reserved IP ranges on the VLAN.
            dns_nameservers: The DNS nameservers used for DHCP responses, either "upstream_dns",
              "google_dns", "opendns", or a newline seperated string of IP addresses or
              domain names.
            dhcp_options: The list of DHCP options that will be included in DHCP responses. Each
              object in the list should have "code", "type", and "value" properties.
            template_vlan_type: Type of subnetting of the VLAN. Applicable only for template
              network.
            cidr: CIDR of the pool of subnets. Applicable only for template network. Each network
              bound to the template will automatically pick a subnet from this pool to
              build its own VLAN.
            mask: Mask used for the subnet of all bound to the template networks. Applicable only
              for template network.
            ipv6: IPv6 configuration on the VLAN.
            mandatory_dhcp: Mandatory DHCP will enforce that clients connecting to this VLAN must
              use the IP address assigned by the DHCP server. Clients who use a static
              IP address won't be able to associate. Only available on firmware versions
              17.0 and above.

        """
        if dhcp_handling is not None:
            options = [
                "Do not respond to DHCP requests",
                "Relay DHCP to another server",
                "Run a DHCP server",
            ]
            assert dhcp_handling in options, (
                f'"dhcp_handling" cannot be "{dhcp_handling}", & must be set to one of: {options}'
            )
        if dhcp_lease_time is not None:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert dhcp_lease_time in options, (
                f'"dhcp_lease_time" cannot be "{dhcp_lease_time}", & must be set to one of: {options}'
            )
        if template_vlan_type is not None:
            options = ["same", "unique"]
            assert template_vlan_type in options, (
                f'"template_vlan_type" cannot be "{template_vlan_type}", & must be set to one of: {options}'
            )

        network_id = urllib.parse.quote(str(network_id), safe="")
        vlan_id = urllib.parse.quote(str(vlan_id), safe="")
        path = f"/networks/{network_id}/appliance/vlans/{vlan_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if subnet is not None:
            payload["subnet"] = subnet
        if appliance_ip is not None:
            payload["applianceIp"] = appliance_ip
        if group_policy_id is not None:
            payload["groupPolicyId"] = group_policy_id
        if vpn_nat_subnet is not None:
            payload["vpnNatSubnet"] = vpn_nat_subnet
        if dhcp_handling is not None:
            payload["dhcpHandling"] = dhcp_handling
        if dhcp_relay_server_ips is not None:
            payload["dhcpRelayServerIps"] = dhcp_relay_server_ips
        if dhcp_lease_time is not None:
            payload["dhcpLeaseTime"] = dhcp_lease_time
        if dhcp_boot_options_enabled is not None:
            payload["dhcpBootOptionsEnabled"] = dhcp_boot_options_enabled
        if dhcp_boot_next_server is not None:
            payload["dhcpBootNextServer"] = dhcp_boot_next_server
        if dhcp_boot_filename is not None:
            payload["dhcpBootFilename"] = dhcp_boot_filename
        if fixed_ip_assignments is not None:
            payload["fixedIpAssignments"] = fixed_ip_assignments
        if reserved_ip_ranges is not None:
            payload["reservedIpRanges"] = reserved_ip_ranges
        if dns_nameservers is not None:
            payload["dnsNameservers"] = dns_nameservers
        if dhcp_options is not None:
            payload["dhcpOptions"] = dhcp_options
        if template_vlan_type is not None:
            payload["templateVlanType"] = template_vlan_type
        if cidr is not None:
            payload["cidr"] = cidr
        if mask is not None:
            payload["mask"] = mask
        if ipv6 is not None:
            payload["ipv6"] = ipv6
        if mandatory_dhcp is not None:
            payload["mandatoryDhcp"] = mandatory_dhcp

        return await self._session.put(
            scope="appliance", operation_id="updateNetworkApplianceVlan", path=path, json=payload
        )

    async def delete_network_appliance_vlan(self, *, network_id: str, vlan_id: str) -> None:
        """Delete a VLAN from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan

        Args:
            network_id: Network ID.
            vlan_id: Vlan ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        vlan_id = urllib.parse.quote(str(vlan_id), safe="")
        path = f"/networks/{network_id}/appliance/vlans/{vlan_id}"

        return await self._session.delete(
            scope="appliance", operation_id="deleteNetworkApplianceVlan", path=path
        )

    async def get_network_appliance_vpn_bgp(self, *, network_id: str) -> dict[str, Any] | None:
        """Return a Hub BGP Configuration.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-bgp

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/vpn/bgp"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceVpnBgp", path=path
        )

    async def update_network_appliance_vpn_bgp(
        self,
        *,
        network_id: str,
        enabled: bool,
        as_number: int | None = None,
        ibgp_hold_timer: int | None = None,
        neighbors: list | None = None,
    ) -> dict[str, Any] | None:
        """Update a Hub BGP Configuration.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-bgp

        Args:
            network_id: Network ID.
            enabled: Boolean value to enable or disable the BGP configuration. When BGP is enabled,
              the asNumber (ASN) will be autopopulated with the preconfigured ASN at
              other Hubs or a default value if there is no ASN configured.
            as_number: An Autonomous System Number (ASN) is required if you are to run BGP and peer
              with another BGP Speaker outside of the Auto VPN domain. This ASN will be
              applied to the entire Auto VPN domain. The entire 4-byte ASN range is
              supported. So, the ASN must be an integer between 1 and 4294967295. When
              absent, this field is not updated. If no value exists then it defaults to
              64512.
            ibgp_hold_timer: The iBGP holdtimer in seconds. The iBGP holdtimer must be an integer
              between 12 and 240. When absent, this field is not updated. If no value
              exists then it defaults to 240.
            neighbors: List of BGP neighbors. This list replaces the existing set of neighbors. When
              absent, this field is not updated.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/vpn/bgp"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if as_number is not None:
            payload["asNumber"] = as_number
        if ibgp_hold_timer is not None:
            payload["ibgpHoldTimer"] = ibgp_hold_timer
        if neighbors is not None:
            payload["neighbors"] = neighbors

        return await self._session.put(
            scope="appliance", operation_id="updateNetworkApplianceVpnBgp", path=path, json=payload
        )

    async def get_network_appliance_vpn_site_to_site_vpn(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Return the site-to-site VPN settings of a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-site-to-site-vpn

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/vpn/siteToSiteVpn"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceVpnSiteToSiteVpn", path=path
        )

    async def update_network_appliance_vpn_site_to_site_vpn(
        self,
        *,
        network_id: str,
        mode: str,
        hubs: list | None = None,
        subnets: list | None = None,
        subnet: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the site-to-site VPN settings of a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn

        Args:
            network_id: Network ID.
            mode: The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'.
            hubs: The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is
              required.
            subnets: The list of subnets and their VPN presence.
            subnet: Configuration of subnet features.

        """
        if mode is not None:
            options = ["hub", "none", "spoke"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'

        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/vpn/siteToSiteVpn"

        payload = {}
        if mode is not None:
            payload["mode"] = mode
        if hubs is not None:
            payload["hubs"] = hubs
        if subnets is not None:
            payload["subnets"] = subnets
        if subnet is not None:
            payload["subnet"] = subnet

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceVpnSiteToSiteVpn",
            path=path,
            json=payload,
        )

    async def get_network_appliance_warm_spare(self, *, network_id: str) -> dict[str, Any] | None:
        """Return MX warm spare settings.

        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-warm-spare

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/warmSpare"

        return await self._session.get(
            scope="appliance", operation_id="getNetworkApplianceWarmSpare", path=path
        )

    async def update_network_appliance_warm_spare(
        self,
        *,
        network_id: str,
        enabled: bool,
        spare_serial: str | None = None,
        uplink_mode: str | None = None,
        virtual_ip1: str | None = None,
        virtual_ip2: str | None = None,
    ) -> dict[str, Any] | None:
        """Update MX warm spare settings.

        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-warm-spare

        Args:
            network_id: Network ID.
            enabled: Enable warm spare.
            spare_serial: Serial number of the warm spare appliance.
            uplink_mode: Uplink mode, either virtual or public.
            virtual_ip1: The WAN 1 shared IP.
            virtual_ip2: The WAN 2 shared IP.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/warmSpare"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if spare_serial is not None:
            payload["spareSerial"] = spare_serial
        if uplink_mode is not None:
            payload["uplinkMode"] = uplink_mode
        if virtual_ip1 is not None:
            payload["virtualIp1"] = virtual_ip1
        if virtual_ip2 is not None:
            payload["virtualIp2"] = virtual_ip2

        return await self._session.put(
            scope="appliance",
            operation_id="updateNetworkApplianceWarmSpare",
            path=path,
            json=payload,
        )

    async def swap_network_appliance_warm_spare(self, *, network_id: str) -> dict[str, Any] | None:
        """Swap MX primary and warm spare appliances.

        https://developer.cisco.com/meraki/api-v1/#!swap-network-appliance-warm-spare

        Args:
            network_id: Network ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/appliance/warmSpare/swap"

        return await self._session.post(
            scope="appliance", operation_id="swapNetworkApplianceWarmSpare", path=path
        )

    async def get_organization_appliance_dns_local_profiles(
        self, *, organization_id: str, profile_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Fetch the local DNS profiles used in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-dns-local-profiles

        Args:
            organization_id: Organization ID.
            profile_ids: Optional parameter to filter the results by profile IDs.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/profiles"

        params = {}
        if profile_ids is not None:
            params["profileIds[]"] = profile_ids

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceDnsLocalProfiles",
            path=path,
            params=params,
        )

    async def create_organization_appliance_dns_local_profile(
        self, *, organization_id: str, name: str
    ) -> dict[str, Any] | None:
        """Create a new local DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-local-profile

        Args:
            organization_id: Organization ID.
            name: Name of profile.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/profiles"

        payload = {}
        if name is not None:
            payload["name"] = name

        return await self._session.post(
            scope="appliance",
            operation_id="createOrganizationApplianceDnsLocalProfile",
            path=path,
            json=payload,
        )

    async def get_organization_appliance_dns_local_profiles_assignments(
        self,
        *,
        organization_id: str,
        profile_ids: list | None = None,
        network_ids: list | None = None,
    ) -> dict[str, Any] | None:
        """Fetch the local DNS profile assignments in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-dns-local-profiles-assignments

        Args:
            organization_id: Organization ID.
            profile_ids: Optional parameter to filter the results by profile IDs.
            network_ids: Optional parameter to filter the results by network IDs.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/profiles/assignments"

        params = {}
        if profile_ids is not None:
            params["profileIds[]"] = profile_ids
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceDnsLocalProfilesAssignments",
            path=path,
            params=params,
        )

    async def bulk_organization_appliance_dns_local_profiles_assignments_create(
        self, *, organization_id: str, items: list
    ) -> dict[str, Any] | None:
        """Assign the local DNS profile to networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-appliance-dns-local-profiles-assignments-create

        Args:
            organization_id: Organization ID.
            items: List containing the network ID and Profile ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = (
            f"/organizations/{organization_id}/appliance/dns/local/profiles/assignments/bulkCreate"
        )

        payload = {}
        if items is not None:
            payload["items"] = items

        return await self._session.post(
            scope="appliance",
            operation_id="bulkOrganizationApplianceDnsLocalProfilesAssignmentsCreate",
            path=path,
            json=payload,
        )

    async def create_organization_appliance_dns_local_profiles_assignments_bulk_delete(
        self, *, organization_id: str, items: list
    ) -> dict[str, Any] | None:
        """Unassign the local DNS profile to networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-local-profiles-assignments-bulk-delete

        Args:
            organization_id: Organization ID.
            items: List containing the assignment ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = (
            f"/organizations/{organization_id}/appliance/dns/local/profiles/assignments/bulkDelete"
        )

        payload = {}
        if items is not None:
            payload["items"] = items

        return await self._session.post(
            scope="appliance",
            operation_id="createOrganizationApplianceDnsLocalProfilesAssignmentsBulkDelete",
            path=path,
            json=payload,
        )

    async def update_organization_appliance_dns_local_profile(
        self, *, organization_id: str, profile_id: str, name: str
    ) -> dict[str, Any] | None:
        """Update a local DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-dns-local-profile

        Args:
            organization_id: Organization ID.
            profile_id: Profile ID.
            name: Name of profile.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/profiles/{profile_id}"

        payload = {}
        if name is not None:
            payload["name"] = name

        return await self._session.put(
            scope="appliance",
            operation_id="updateOrganizationApplianceDnsLocalProfile",
            path=path,
            json=payload,
        )

    async def delete_organization_appliance_dns_local_profile(
        self, *, organization_id: str, profile_id: str
    ) -> None:
        """Deletes a local DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-appliance-dns-local-profile

        Args:
            organization_id: Organization ID.
            profile_id: Profile ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/profiles/{profile_id}"

        return await self._session.delete(
            scope="appliance", operation_id="deleteOrganizationApplianceDnsLocalProfile", path=path
        )

    async def get_organization_appliance_dns_local_records(
        self, *, organization_id: str, profile_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Fetch the DNS records used in local DNS profiles.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-dns-local-records

        Args:
            organization_id: Organization ID.
            profile_ids: Optional parameter to filter the results by profile IDs.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/records"

        params = {}
        if profile_ids is not None:
            params["profileIds[]"] = profile_ids

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceDnsLocalRecords",
            path=path,
            params=params,
        )

    async def create_organization_appliance_dns_local_record(
        self, *, organization_id: str, hostname: str, address: str, profile: dict
    ) -> dict[str, Any] | None:
        """Create a new local DNS record.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-local-record

        Args:
            organization_id: Organization ID.
            hostname: Hostname for the DNS record.
            address: IP for the DNS record.
            profile: The profile the DNS record is associated with.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/records"

        payload = {}
        if hostname is not None:
            payload["hostname"] = hostname
        if address is not None:
            payload["address"] = address
        if profile is not None:
            payload["profile"] = profile

        return await self._session.post(
            scope="appliance",
            operation_id="createOrganizationApplianceDnsLocalRecord",
            path=path,
            json=payload,
        )

    async def update_organization_appliance_dns_local_record(
        self,
        *,
        organization_id: str,
        record_id: str,
        hostname: str | None = None,
        address: str | None = None,
        profile: dict | None = None,
    ) -> dict[str, Any] | None:
        """Updates a local DNS record.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-dns-local-record

        Args:
            organization_id: Organization ID.
            record_id: Record ID.
            hostname: Hostname for the DNS record.
            address: IP for the DNS record.
            profile: The profile the DNS record is associated with.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        record_id = urllib.parse.quote(str(record_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/records/{record_id}"

        payload = {}
        if hostname is not None:
            payload["hostname"] = hostname
        if address is not None:
            payload["address"] = address
        if profile is not None:
            payload["profile"] = profile

        return await self._session.put(
            scope="appliance",
            operation_id="updateOrganizationApplianceDnsLocalRecord",
            path=path,
            json=payload,
        )

    async def delete_organization_appliance_dns_local_record(
        self, *, organization_id: str, record_id: str
    ) -> None:
        """Deletes a local DNS record.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-appliance-dns-local-record

        Args:
            organization_id: Organization ID.
            record_id: Record ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        record_id = urllib.parse.quote(str(record_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/local/records/{record_id}"

        return await self._session.delete(
            scope="appliance", operation_id="deleteOrganizationApplianceDnsLocalRecord", path=path
        )

    async def get_organization_appliance_dns_split_profiles(
        self, *, organization_id: str, profile_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Fetch the split DNS profiles used in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-dns-split-profiles

        Args:
            organization_id: Organization ID.
            profile_ids: Optional parameter to filter the results by profile IDs.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/split/profiles"

        params = {}
        if profile_ids is not None:
            params["profileIds[]"] = profile_ids

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceDnsSplitProfiles",
            path=path,
            params=params,
        )

    async def create_organization_appliance_dns_split_profile(
        self, *, organization_id: str, name: str, hostnames: list, nameservers: dict
    ) -> dict[str, Any] | None:
        """Create a new split DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-split-profile

        Args:
            organization_id: Organization ID.
            name: Name of profile.
            hostnames: The hostname patterns to match for redirection. For more information on Split
              DNS hostname pattern formatting, please consult the Split DNS KB.
            nameservers: Contains the nameserver information for redirection.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/split/profiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if hostnames is not None:
            payload["hostnames"] = hostnames
        if nameservers is not None:
            payload["nameservers"] = nameservers

        return await self._session.post(
            scope="appliance",
            operation_id="createOrganizationApplianceDnsSplitProfile",
            path=path,
            json=payload,
        )

    async def get_organization_appliance_dns_split_profiles_assignments(
        self,
        *,
        organization_id: str,
        profile_ids: list | None = None,
        network_ids: list | None = None,
    ) -> dict[str, Any] | None:
        """Fetch the split DNS profile assignments in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-dns-split-profiles-assignments

        Args:
            organization_id: Organization ID.
            profile_ids: Optional parameter to filter the results by profile IDs.
            network_ids: Optional parameter to filter the results by network IDs.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/split/profiles/assignments"

        params = {}
        if profile_ids is not None:
            params["profileIds[]"] = profile_ids
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceDnsSplitProfilesAssignments",
            path=path,
            params=params,
        )

    async def create_organization_appliance_dns_split_profiles_assignments_bulk_create(
        self, *, organization_id: str, items: list
    ) -> dict[str, Any] | None:
        """Assign the split DNS profile to networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-split-profiles-assignments-bulk-create

        Args:
            organization_id: Organization ID.
            items: List containing the network ID and Profile ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = (
            f"/organizations/{organization_id}/appliance/dns/split/profiles/assignments/bulkCreate"
        )

        payload = {}
        if items is not None:
            payload["items"] = items

        return await self._session.post(
            scope="appliance",
            operation_id="createOrganizationApplianceDnsSplitProfilesAssignmentsBulkCreate",
            path=path,
            json=payload,
        )

    async def create_organization_appliance_dns_split_profiles_assignments_bulk_delete(
        self, *, organization_id: str, items: list
    ) -> dict[str, Any] | None:
        """Unassign the split DNS profile to networks in the organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-dns-split-profiles-assignments-bulk-delete

        Args:
            organization_id: Organization ID.
            items: List containing the assignment ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = (
            f"/organizations/{organization_id}/appliance/dns/split/profiles/assignments/bulkDelete"
        )

        payload = {}
        if items is not None:
            payload["items"] = items

        return await self._session.post(
            scope="appliance",
            operation_id="createOrganizationApplianceDnsSplitProfilesAssignmentsBulkDelete",
            path=path,
            json=payload,
        )

    async def update_organization_appliance_dns_split_profile(
        self,
        *,
        organization_id: str,
        profile_id: str,
        name: str | None = None,
        hostnames: list | None = None,
        nameservers: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a split DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-dns-split-profile

        Args:
            organization_id: Organization ID.
            profile_id: Profile ID.
            name: Name of profile.
            hostnames: The hostname patterns to match for redirection. For more information on Split
              DNS hostname pattern formatting, please consult the Split DNS KB.
            nameservers: Contains the nameserver information for redirection.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/split/profiles/{profile_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if hostnames is not None:
            payload["hostnames"] = hostnames
        if nameservers is not None:
            payload["nameservers"] = nameservers

        return await self._session.put(
            scope="appliance",
            operation_id="updateOrganizationApplianceDnsSplitProfile",
            path=path,
            json=payload,
        )

    async def delete_organization_appliance_dns_split_profile(
        self, *, organization_id: str, profile_id: str
    ) -> None:
        """Deletes a split DNS profile.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-appliance-dns-split-profile

        Args:
            organization_id: Organization ID.
            profile_id: Profile ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        profile_id = urllib.parse.quote(str(profile_id), safe="")
        path = f"/organizations/{organization_id}/appliance/dns/split/profiles/{profile_id}"

        return await self._session.delete(
            scope="appliance", operation_id="deleteOrganizationApplianceDnsSplitProfile", path=path
        )

    def get_organization_appliance_firewall_multicast_forwarding_by_network(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List Static Multicasting forwarding settings for MX networks.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-firewall-multicast-forwarding-by-network

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
            network_ids: Optional parameter to filter the results by network IDs.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/firewall/multicastForwarding/byNetwork"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(
            scope="appliance",
            operation_id="getOrganizationApplianceFirewallMulticastForwardingByNetwork",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_appliance_security_events(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        sort_order: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List the security events for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-events

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. Data is gathered after the specified t0
              value. The maximum lookback period is 365 days from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 365 days. The default is 31 days.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            sort_order: Sorted order of security events based on event detection time. Order options
              are 'ascending' or 'descending'. Default is ascending order.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if sort_order is not None:
            options = ["ascending", "descending"]
            assert sort_order in options, (
                f'"sort_order" cannot be "{sort_order}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/security/events"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if sort_order is not None:
            params["sortOrder"] = sort_order

        return self._session.get_pages(
            scope="appliance",
            operation_id="getOrganizationApplianceSecurityEvents",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_appliance_security_intrusion(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Returns all supported intrusion settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-intrusion

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/security/intrusion"

        return await self._session.get(
            scope="appliance", operation_id="getOrganizationApplianceSecurityIntrusion", path=path
        )

    async def update_organization_appliance_security_intrusion(
        self, *, organization_id: str, allowed_rules: list
    ) -> dict[str, Any] | None:
        """Sets supported intrusion settings for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-security-intrusion

        Args:
            organization_id: Organization ID.
            allowed_rules: Sets a list of specific SNORT signatures to allow.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/security/intrusion"

        payload = {}
        if allowed_rules is not None:
            payload["allowedRules"] = allowed_rules

        return await self._session.put(
            scope="appliance",
            operation_id="updateOrganizationApplianceSecurityIntrusion",
            path=path,
            json=payload,
        )

    def get_organization_appliance_traffic_shaping_vpn_exclusions_by_network(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Display VPN exclusion rules for MX networks.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-traffic-shaping-vpn-exclusions-by-network

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: Optional parameter to filter the results by network IDs.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/trafficShaping/vpnExclusions/byNetwork"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(
            scope="appliance",
            operation_id="getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_appliance_uplink_statuses(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        serials: list | None = None,
        iccids: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List the uplink status of every Meraki MX and Z series appliances in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplink-statuses

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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/uplink/statuses"

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

        return self._session.get_pages(
            scope="appliance",
            operation_id="getOrganizationApplianceUplinkStatuses",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_appliance_uplinks_statuses_overview(
        self, *, organization_id: str, network_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Returns an overview of uplink statuses.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplinks-statuses-overview

        Args:
            organization_id: Organization ID.
            network_ids: A list of network IDs. The returned devices will be filtered to only
              include these networks.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/uplinks/statuses/overview"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceUplinksStatusesOverview",
            path=path,
            params=params,
        )

    async def get_organization_appliance_uplinks_usage_by_network(
        self,
        *,
        organization_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
    ) -> dict[str, Any] | None:
        """Get the sent and received bytes for each uplink of all MX and Z networks within an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplinks-usage-by-network

        Args:
            organization_id: Organization ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 30 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 14 days. The default is 1 day.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/uplinks/usage/byNetwork"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceUplinksUsageByNetwork",
            path=path,
            params=params,
        )

    async def get_organization_appliance_vpn_site_to_site_ipsec_peers_slas(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Get the list of available IPsec SLA policies for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-site-to-site-ipsec-peers-slas

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/vpn/siteToSite/ipsec/peers/slas"

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceVpnSiteToSiteIpsecPeersSlas",
            path=path,
        )

    async def update_organization_appliance_vpn_site_to_site_ipsec_peers_slas(
        self, *, organization_id: str, items: list | None = None
    ) -> dict[str, Any] | None:
        """Update the IPsec SLA policies for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-site-to-site-ipsec-peers-slas

        Args:
            organization_id: Organization ID.
            items: List of IPsec SLA policies.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/vpn/siteToSite/ipsec/peers/slas"

        payload = {}
        if items is not None:
            payload["items"] = items

        return await self._session.put(
            scope="appliance",
            operation_id="updateOrganizationApplianceVpnSiteToSiteIpsecPeersSlas",
            path=path,
            json=payload,
        )

    def get_organization_appliance_vpn_stats(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Show VPN history stat for networks in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-stats

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 300. Default
              is 300.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: A list of Meraki network IDs to filter results to contain only specified
              networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/vpn/stats"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get_pages(
            scope="appliance",
            operation_id="getOrganizationApplianceVpnStats",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    def get_organization_appliance_vpn_statuses(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        network_ids: list | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Show VPN status for networks in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-statuses

        Args:
            organization_id: Organization ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 300. Default
              is 300.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            network_ids: A list of Meraki network IDs to filter results to contain only specified
              networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/vpn/statuses"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get_pages(
            scope="appliance",
            operation_id="getOrganizationApplianceVpnStatuses",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_appliance_vpn_third_party_v_p_n_peers(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Return the third party VPN peers for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-third-party-v-p-n-peers

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/vpn/thirdPartyVPNPeers"

        return await self._session.get(
            scope="appliance",
            operation_id="getOrganizationApplianceVpnThirdPartyVPNPeers",
            path=path,
        )

    async def update_organization_appliance_vpn_third_party_v_p_n_peers(
        self, *, organization_id: str, peers: list
    ) -> dict[str, Any] | None:
        """Update the third party VPN peers for an organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-v-p-n-peers

        Args:
            organization_id: Organization ID.
            peers: The list of VPN peers.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/vpn/thirdPartyVPNPeers"

        payload = {}
        if peers is not None:
            payload["peers"] = peers

        return await self._session.put(
            scope="appliance",
            operation_id="updateOrganizationApplianceVpnThirdPartyVPNPeers",
            path=path,
            json=payload,
        )

    async def get_organization_appliance_vpn_vpn_firewall_rules(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """Return the firewall rules for an organization's site-to-site VPN.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-vpn-firewall-rules

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/vpn/vpnFirewallRules"

        return await self._session.get(
            scope="appliance", operation_id="getOrganizationApplianceVpnVpnFirewallRules", path=path
        )

    async def update_organization_appliance_vpn_vpn_firewall_rules(
        self,
        *,
        organization_id: str,
        rules: list | None = None,
        syslog_default_rule: bool | None = None,
    ) -> dict[str, Any] | None:
        """Update the firewall rules of an organization's site-to-site VPN.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-vpn-firewall-rules

        Args:
            organization_id: Organization ID.
            rules: An ordered array of the firewall rules (not including the default rule).
            syslog_default_rule: Log the special default rule (boolean value - enable only if you've
              configured a syslog server) (optional).

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/appliance/vpn/vpnFirewallRules"

        payload = {}
        if rules is not None:
            payload["rules"] = rules
        if syslog_default_rule is not None:
            payload["syslogDefaultRule"] = syslog_default_rule

        return await self._session.put(
            scope="appliance",
            operation_id="updateOrganizationApplianceVpnVpnFirewallRules",
            path=path,
            json=payload,
        )
