"""Networks API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncNetworks:
    """Networks class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_network(self, *, network_id: str) -> dict[str, Any] | None:
        """Return a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "get_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}"

        return self._session.get(metadata, resource)

    def update_network(
        self,
        *,
        network_id: str,
        name: str | None = None,
        time_zone: str | None = None,
        tags: list | None = None,
        enrollment_string: str | None = None,
        notes: str | None = None,
    ) -> dict[str, Any] | None:
        """Update a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network

        Args:
            network_id: Network ID.
            name: The name of the network.
            time_zone: The timezone of the network. For a list of allowed timezones, please see the
              'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article.</a>.
            tags: A list of tags to be applied to the network.
            enrollment_string: A unique identifier which can be used for device enrollment or easy
              access through the Meraki SM Registration page or the Self Service Portal.
              Please note that changing this field may cause existing bookmarks to
              break.
            notes: Add any notes or additional information about this network here.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "update_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if time_zone is not None:
            payload["timeZone"] = time_zone
        if tags is not None:
            payload["tags"] = tags
        if enrollment_string is not None:
            payload["enrollmentString"] = enrollment_string
        if notes is not None:
            payload["notes"] = notes

        return self._session.put(metadata, resource, payload)

    def delete_network(self, *, network_id: str) -> None:
        """Delete a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "delete_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}"

        return self._session.delete(metadata, resource)

    def get_network_alerts_history(
        self,
        *,
        network_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the alert history for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-history

        Args:
            network_id: Network ID.
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
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["networks", "monitor", "alerts", "history"],
            "operation": "get_network_alerts_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/alerts/history"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_alerts_settings(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the alert configuration for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-settings

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "alerts", "settings"],
            "operation": "get_network_alerts_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/alerts/settings"

        return self._session.get(metadata, resource)

    def update_network_alerts_settings(
        self,
        *,
        network_id: str,
        default_destinations: dict | None = None,
        alerts: list | None = None,
        muting: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the alert configuration for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-alerts-settings

        Args:
            network_id: Network ID.
            default_destinations: The network-wide destinations for all alerts on the network.
            alerts: Alert-specific configuration for each type. Only alerts that pertain to the
              network can be updated.
            muting: Mute alerts under certain conditions.

        """
        metadata = {
            "tags": ["networks", "configure", "alerts", "settings"],
            "operation": "update_network_alerts_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/alerts/settings"

        payload = {}
        if default_destinations is not None:
            payload["defaultDestinations"] = default_destinations
        if alerts is not None:
            payload["alerts"] = alerts
        if muting is not None:
            payload["muting"] = muting

        return self._session.put(metadata, resource, payload)

    def bind_network(
        self, *, network_id: str, config_template_id: str, auto_bind: bool | None = None
    ) -> dict[str, Any] | None:
        """Bind a network to a template.

        https://developer.cisco.com/meraki/api-v1/#!bind-network

        Args:
            network_id: Network ID.
            config_template_id: The ID of the template to which the network should be bound.
            auto_bind: Optional boolean indicating whether the network's switches should
              automatically bind to profiles of the same model. Defaults to false if
              left unspecified. This option only affects switch networks and switch
              templates. Auto-bind is not valid unless the switch template has at least
              one profile and has at most one profile per switch model.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "bind_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/bind"

        payload = {}
        if config_template_id is not None:
            payload["configTemplateId"] = config_template_id
        if auto_bind is not None:
            payload["autoBind"] = auto_bind

        return self._session.post(metadata, resource, payload)

    def get_network_bluetooth_clients(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        include_connectivity_history: bool | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the Bluetooth clients seen by APs in this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-clients

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 7 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 7 days. The default is 1 day.
            per_page: The number of entries per page returned. Acceptable range is 5 - 1000. Default
              is 10.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            include_connectivity_history: Include the connectivity history for this client.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["networks", "monitor", "bluetoothClients"],
            "operation": "get_network_bluetooth_clients",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/bluetoothClients"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if include_connectivity_history is not None:
            params["includeConnectivityHistory"] = include_connectivity_history

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_bluetooth_client(
        self,
        *,
        network_id: str,
        bluetooth_client_id: str,
        include_connectivity_history: bool | None = None,
        connectivity_history_timespan: int | None = None,
    ) -> dict[str, Any] | None:
        """Return a Bluetooth client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-client

        Args:
            network_id: Network ID.
            bluetooth_client_id: Bluetooth client ID.
            include_connectivity_history: Include the connectivity history for this client.
            connectivity_history_timespan: The timespan, in seconds, for the connectivityHistory
              data. By default 1 day, 86400, will be used.

        """
        metadata = {
            "tags": ["networks", "monitor", "bluetoothClients"],
            "operation": "get_network_bluetooth_client",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        bluetooth_client_id = urllib.parse.quote(str(bluetooth_client_id), safe="")
        resource = f"/networks/{network_id}/bluetoothClients/{bluetooth_client_id}"

        params = {}
        if include_connectivity_history is not None:
            params["includeConnectivityHistory"] = include_connectivity_history
        if connectivity_history_timespan is not None:
            params["connectivityHistoryTimespan"] = connectivity_history_timespan

        return self._session.get(metadata, resource, params)

    def get_network_clients(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        statuses: list | None = None,
        ip: str | None = None,
        ip6: str | None = None,
        ip6_local: str | None = None,
        mac: str | None = None,
        os: str | None = None,
        psk_group: str | None = None,
        description: str | None = None,
        vlan: str | None = None,
        named_vlan: str | None = None,
        recent_device_connections: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """List the clients that have used this network in the timespan.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.
            per_page: The number of entries per page returned. Acceptable range is 3 - 5000. Default
              is 10.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            statuses: Filters clients based on status. Can be one of 'Online' or 'Offline'.
            ip: Filters clients based on a partial or full match for the ip address field.
            ip6: Filters clients based on a partial or full match for the ip6 address field.
            ip6_local: Filters clients based on a partial or full match for the ip6Local address
              field.
            mac: Filters clients based on a partial or full match for the mac address field.
            os: Filters clients based on a partial or full match for the os (operating system)
              field.
            psk_group: Filters clients based on partial or full match for the iPSK name field.
            description: Filters clients based on a partial or full match for the description field.
            vlan: Filters clients based on the full match for the VLAN field.
            named_vlan: Filters clients based on the partial or full match for the named VLAN field.
            recent_device_connections: Filters clients based on recent connection type. Can be one
              of 'Wired' or 'Wireless'.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {"tags": ["networks", "monitor", "clients"], "operation": "get_network_clients"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if statuses is not None:
            params["statuses[]"] = statuses
        if ip is not None:
            params["ip"] = ip
        if ip6 is not None:
            params["ip6"] = ip6
        if ip6_local is not None:
            params["ip6Local"] = ip6_local
        if mac is not None:
            params["mac"] = mac
        if os is not None:
            params["os"] = os
        if psk_group is not None:
            params["pskGroup"] = psk_group
        if description is not None:
            params["description"] = description
        if vlan is not None:
            params["vlan"] = vlan
        if named_vlan is not None:
            params["namedVlan"] = named_vlan
        if recent_device_connections is not None:
            params["recentDeviceConnections[]"] = recent_device_connections

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_clients_application_usage(
        self,
        *,
        network_id: str,
        clients: str,
        ssid_number: int | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the application usage data for clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-application-usage

        Args:
            network_id: Network ID.
            clients: A list of client keys, MACs or IPs separated by comma.
            ssid_number: An SSID number to include. If not specified, events for all SSIDs will be
              returned.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if ssid_number is not None:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert ssid_number in options, (
                f'"ssid_number" cannot be "{ssid_number}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "monitor", "clients", "applicationUsage"],
            "operation": "get_network_clients_application_usage",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/applicationUsage"

        params = {}
        if clients is not None:
            params["clients"] = clients
        if ssid_number is not None:
            params["ssidNumber"] = ssid_number
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_clients_bandwidth_usage_history(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-bandwidth-usage-history

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 30 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
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
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["networks", "monitor", "clients", "bandwidthUsageHistory"],
            "operation": "get_network_clients_bandwidth_usage_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/bandwidthUsageHistory"

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

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_clients_overview(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
    ) -> dict[str, Any] | None:
        """Return overview statistics for network clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-overview

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              7200, 86400, 604800, 2592000. The default is 604800.

        """
        metadata = {
            "tags": ["networks", "monitor", "clients", "overview"],
            "operation": "get_network_clients_overview",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/overview"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution

        return self._session.get(metadata, resource, params)

    def provision_network_clients(
        self,
        *,
        network_id: str,
        clients: list,
        device_policy: str,
        group_policy_id: str | None = None,
        policies_by_security_appliance: dict | None = None,
        policies_by_ssid: dict | None = None,
    ) -> dict[str, Any] | None:
        """Provisions a client with a name and policy.

        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        Args:
            network_id: Network ID.
            clients: The array of clients to provision.
            device_policy: The policy to apply to the specified client. Can be 'Group policy',
              'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
            group_policy_id: The ID of the desired group policy to apply to the client. Required if
              'devicePolicy' is set to "Group policy". Otherwise this is ignored.
            policies_by_security_appliance: An object, describing what the policy-connection
              association is for the security appliance. (Only relevant if the security
              appliance is actually within the network).
            policies_by_ssid: An object, describing the policy-connection associations for each
              active SSID within the network. Keys should be the number of enabled
              SSIDs, mapping to an object describing the client's policy.

        """
        if device_policy is not None:
            options = ["Allowed", "Blocked", "Group policy", "Normal", "Per connection"]
            assert device_policy in options, (
                f'"device_policy" cannot be "{device_policy}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "clients"],
            "operation": "provision_network_clients",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/provision"

        payload = {}
        if clients is not None:
            payload["clients"] = clients
        if device_policy is not None:
            payload["devicePolicy"] = device_policy
        if group_policy_id is not None:
            payload["groupPolicyId"] = group_policy_id
        if policies_by_security_appliance is not None:
            payload["policiesBySecurityAppliance"] = policies_by_security_appliance
        if policies_by_ssid is not None:
            payload["policiesBySsid"] = policies_by_ssid

        return self._session.post(metadata, resource, payload)

    def get_network_clients_usage_histories(
        self,
        *,
        network_id: str,
        clients: str,
        ssid_number: int | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the usage histories for clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-usage-histories

        Args:
            network_id: Network ID.
            clients: A list of client keys, MACs or IPs separated by comma.
            ssid_number: An SSID number to include. If not specified, events for all SSIDs will be
              returned.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        if ssid_number is not None:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert ssid_number in options, (
                f'"ssid_number" cannot be "{ssid_number}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "monitor", "clients", "usageHistories"],
            "operation": "get_network_clients_usage_histories",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/usageHistories"

        params = {}
        if clients is not None:
            params["clients"] = clients
        if ssid_number is not None:
            params["ssidNumber"] = ssid_number
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_client(self, *, network_id: str, client_id: str) -> dict[str, Any] | None:
        """Return the client associated with the given identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client

        Args:
            network_id: Network ID.
            client_id: Client ID.

        """
        metadata = {"tags": ["networks", "monitor", "clients"], "operation": "get_network_client"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}"

        return self._session.get(metadata, resource)

    def get_network_client_policy(
        self, *, network_id: str, client_id: str
    ) -> dict[str, Any] | None:
        """Return the policy assigned to a client on the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-policy

        Args:
            network_id: Network ID.
            client_id: Client ID.

        """
        metadata = {
            "tags": ["networks", "configure", "clients", "policy"],
            "operation": "get_network_client_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/policy"

        return self._session.get(metadata, resource)

    def update_network_client_policy(
        self,
        *,
        network_id: str,
        client_id: str,
        device_policy: str,
        group_policy_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Update the policy assigned to a client on the network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-client-policy

        Args:
            network_id: Network ID.
            client_id: Client ID.
            device_policy: The policy to assign. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group
              policy'. Required.
            group_policy_id: [Optional] If 'devicePolicy' is set to 'Group policy' this param is
              used to specify the group policy ID.

        """
        metadata = {
            "tags": ["networks", "configure", "clients", "policy"],
            "operation": "update_network_client_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/policy"

        payload = {}
        if device_policy is not None:
            payload["devicePolicy"] = device_policy
        if group_policy_id is not None:
            payload["groupPolicyId"] = group_policy_id

        return self._session.put(metadata, resource, payload)

    def get_network_client_splash_authorization_status(
        self, *, network_id: str, client_id: str
    ) -> dict[str, Any] | None:
        """Return the splash authorization for a client, for each SSID they've associated with through splash.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-splash-authorization-status

        Args:
            network_id: Network ID.
            client_id: Client ID.

        """
        metadata = {
            "tags": ["networks", "configure", "clients", "splashAuthorizationStatus"],
            "operation": "get_network_client_splash_authorization_status",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus"

        return self._session.get(metadata, resource)

    def update_network_client_splash_authorization_status(
        self, *, network_id: str, client_id: str, ssids: dict
    ) -> dict[str, Any] | None:
        """Update a client's splash authorization.

        https://developer.cisco.com/meraki/api-v1/#!update-network-client-splash-authorization-status

        Args:
            network_id: Network ID.
            client_id: Client ID.
            ssids: The target SSIDs. Each SSID must be enabled and must have Click-through splash
              enabled. For each SSID where isAuthorized is true, the expiration time
              will automatically be set according to the SSID's splash frequency. Not
              all networks support configuring all SSIDs.

        """
        metadata = {
            "tags": ["networks", "configure", "clients", "splashAuthorizationStatus"],
            "operation": "update_network_client_splash_authorization_status",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus"

        payload = {}
        if ssids is not None:
            payload["ssids"] = ssids

        return self._session.put(metadata, resource, payload)

    def get_network_client_traffic_history(
        self,
        *,
        network_id: str,
        client_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Return the client's network traffic data over time.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-traffic-history

        Args:
            network_id: Network ID.
            client_id: Client ID.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["networks", "monitor", "clients", "trafficHistory"],
            "operation": "get_network_client_traffic_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/trafficHistory"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_client_usage_history(
        self, *, network_id: str, client_id: str
    ) -> dict[str, Any] | None:
        """Return the client's daily usage history.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-usage-history

        Args:
            network_id: Network ID.
            client_id: Client ID.

        """
        metadata = {
            "tags": ["networks", "monitor", "clients", "usageHistory"],
            "operation": "get_network_client_usage_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/usageHistory"

        return self._session.get(metadata, resource)

    def get_network_devices(self, *, network_id: str) -> dict[str, Any] | None:
        """List the devices in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-devices

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "get_network_devices",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices"

        return self._session.get(metadata, resource)

    def claim_network_devices(
        self,
        *,
        network_id: str,
        serials: list,
        add_atomically: bool | None = None,
        details_by_device: list | None = None,
    ) -> dict[str, Any] | None:
        """Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed).

        https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

        Args:
            network_id: Network ID.
            add_atomically: Whether to claim devices atomically. If true, all devices will be
              claimed or none will be claimed. Default is true.
            serials: A list of serials of devices to claim.
            details_by_device: Optional details for claimed devices (currently only used for
              Catalyst devices).

        """
        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "claim_network_devices",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/claim"

        params = {}
        if add_atomically is not None:
            params["addAtomically"] = add_atomically

        payload = {}
        if serials is not None:
            payload["serials"] = serials
        if details_by_device is not None:
            payload["detailsByDevice"] = details_by_device

        return self._session.post(metadata, resource, payload)

    def vmx_network_devices_claim(self, *, network_id: str, size: str) -> dict[str, Any] | None:
        """Claim a vMX into a network.

        https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim

        Args:
            network_id: Network ID.
            size: The size of the vMX you claim. It can be one of: small, medium, large, xlarge,
              100.

        """
        if size is not None:
            options = ["100", "large", "medium", "small", "xlarge"]
            assert size in options, f'"size" cannot be "{size}", & must be set to one of: {options}'

        metadata = {
            "tags": ["networks", "configure", "devices", "claim"],
            "operation": "vmx_network_devices_claim",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/claim/vmx"

        payload = {}
        if size is not None:
            payload["size"] = size

        return self._session.post(metadata, resource, payload)

    def remove_network_devices(self, *, network_id: str, serial: str) -> dict[str, Any] | None:
        """Remove a single device.

        https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

        Args:
            network_id: Network ID.
            serial: The serial of a device.

        """
        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "remove_network_devices",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/remove"

        payload = {}
        if serial is not None:
            payload["serial"] = serial

        return self._session.post(metadata, resource, payload)

    def get_network_events(
        self,
        *,
        network_id: str,
        product_type: str | None = None,
        included_event_types: list | None = None,
        excluded_event_types: list | None = None,
        device_mac: str | None = None,
        device_serial: str | None = None,
        device_name: str | None = None,
        client_ip: str | None = None,
        client_mac: str | None = None,
        client_name: str | None = None,
        sm_device_mac: str | None = None,
        sm_device_name: str | None = None,
        event_details: str | None = None,
        event_severity: str | None = None,
        is_catalyst: bool | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "prev",
        event_log_end_time: str | None = None,
    ) -> Generator[Any, None, None]:
        """List the events for the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-events

        Args:
            network_id: Network ID.
            product_type: The product type to fetch events for. This parameter is required for
              networks with multiple device types. Valid types are wireless, appliance,
              switch, systemsManager, camera, cellularGateway, wirelessController,
              campusGateway, and secureConnect.
            included_event_types: A list of event types. The returned events will be filtered to
              only include events with these types.
            excluded_event_types: A list of event types. The returned events will be filtered to
              exclude events with these types.
            device_mac: The MAC address of the Meraki device which the list of events will be
              filtered with.
            device_serial: The serial of the Meraki device which the list of events will be filtered
              with.
            device_name: The name of the Meraki device which the list of events will be filtered
              with.
            client_ip: The IP of the client which the list of events will be filtered with. Only
              supported for track-by-IP networks.
            client_mac: The MAC address of the client which the list of events will be filtered
              with. Only supported for track-by-MAC networks.
            client_name: The name, or partial name, of the client which the list of events will be
              filtered with.
            sm_device_mac: The MAC address of the Systems Manager device which the list of events
              will be filtered with.
            sm_device_name: The name of the Systems Manager device which the list of events will be
              filtered with.
            event_details: The details of the event(Catalyst device only) which the list of events
              will be filtered with.
            event_severity: The severity of the event(Catalyst device only) which the list of events
              will be filtered with.
            is_catalyst: Boolean indicating that whether it is a Catalyst device. For Catalyst
              device, eventDetails and eventSeverity can be used to filter events.
            per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 10.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" or "prev" (default) page.
            event_log_end_time: ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, to
              retrieve events within a time window.

        """
        if product_type is not None:
            options = [
                "appliance",
                "camera",
                "campusGateway",
                "cellularGateway",
                "secureConnect",
                "switch",
                "systemsManager",
                "wireless",
                "wirelessController",
            ]
            assert product_type in options, (
                f'"product_type" cannot be "{product_type}", & must be set to one of: {options}'
            )

        metadata = {"tags": ["networks", "monitor", "events"], "operation": "get_network_events"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/events"

        params = {}
        if product_type is not None:
            params["productType"] = product_type
        if included_event_types is not None:
            params["includedEventTypes[]"] = included_event_types
        if excluded_event_types is not None:
            params["excludedEventTypes[]"] = excluded_event_types
        if device_mac is not None:
            params["deviceMac"] = device_mac
        if device_serial is not None:
            params["deviceSerial"] = device_serial
        if device_name is not None:
            params["deviceName"] = device_name
        if client_ip is not None:
            params["clientIp"] = client_ip
        if client_mac is not None:
            params["clientMac"] = client_mac
        if client_name is not None:
            params["clientName"] = client_name
        if sm_device_mac is not None:
            params["smDeviceMac"] = sm_device_mac
        if sm_device_name is not None:
            params["smDeviceName"] = sm_device_name
        if event_details is not None:
            params["eventDetails"] = event_details
        if event_severity is not None:
            params["eventSeverity"] = event_severity
        if is_catalyst is not None:
            params["isCatalyst"] = is_catalyst
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            metadata, resource, params, total_pages, direction, event_log_end_time
        )

    def get_network_events_event_types(self, *, network_id: str) -> dict[str, Any] | None:
        """List the event type to human-readable description.

        https://developer.cisco.com/meraki/api-v1/#!get-network-events-event-types

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "monitor", "events", "eventTypes"],
            "operation": "get_network_events_event_types",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/events/eventTypes"

        return self._session.get(metadata, resource)

    def get_network_firmware_upgrades(self, *, network_id: str) -> dict[str, Any] | None:
        """Get firmware upgrade information for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades"],
            "operation": "get_network_firmware_upgrades",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades"

        return self._session.get(metadata, resource)

    def update_network_firmware_upgrades(
        self,
        *,
        network_id: str,
        upgrade_window: dict | None = None,
        timezone: str | None = None,
        products: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update firmware upgrade information for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

        Args:
            network_id: Network ID.
            upgrade_window: Upgrade window for devices in network.
            timezone: The timezone for the network.
            products: Contains information about the network to update.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades"],
            "operation": "update_network_firmware_upgrades",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades"

        payload = {}
        if upgrade_window is not None:
            payload["upgradeWindow"] = upgrade_window
        if timezone is not None:
            payload["timezone"] = timezone
        if products is not None:
            payload["products"] = products

        return self._session.put(metadata, resource, payload)

    def create_network_firmware_upgrades_rollback(
        self,
        *,
        network_id: str,
        reasons: list,
        product: str | None = None,
        time: str | None = None,
        to_version: dict | None = None,
    ) -> dict[str, Any] | None:
        """Rollback a Firmware Upgrade For A Network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

        Args:
            network_id: Network ID.
            product: Product type to rollback (if the network is a combined network).
            time: Scheduled time for the rollback.
            reasons: Reasons for the rollback.
            to_version: Version to downgrade to (if the network has firmware flexibility).

        """
        if product is not None:
            options = [
                "appliance",
                "camera",
                "cellularGateway",
                "secureConnect",
                "switch",
                "switchCatalyst",
                "wireless",
                "wirelessController",
            ]
            assert product in options, (
                f'"product" cannot be "{product}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "rollbacks"],
            "operation": "create_network_firmware_upgrades_rollback",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/rollbacks"

        payload = {}
        if product is not None:
            payload["product"] = product
        if time is not None:
            payload["time"] = time
        if reasons is not None:
            payload["reasons"] = reasons
        if to_version is not None:
            payload["toVersion"] = to_version

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_events(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Get the Staged Upgrade Event from a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-events

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "get_network_firmware_upgrades_staged_events",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/events"

        return self._session.get(metadata, resource)

    def update_network_firmware_upgrades_staged_events(
        self, *, network_id: str, stages: list
    ) -> dict[str, Any] | None:
        """Update the Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-events

        Args:
            network_id: Network ID.
            stages: All firmware upgrade stages in the network with their start time.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "update_network_firmware_upgrades_staged_events",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/events"

        payload = {}
        if stages is not None:
            payload["stages"] = stages

        return self._session.put(metadata, resource, payload)

    def create_network_firmware_upgrades_staged_event(
        self, *, network_id: str, stages: list, products: dict | None = None
    ) -> dict[str, Any] | None:
        """Create a Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-event

        Args:
            network_id: Network ID.
            products: Contains firmware upgrade version information.
            stages: All firmware upgrade stages in the network with their start time.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "create_network_firmware_upgrades_staged_event",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/events"

        payload = {}
        if products is not None:
            payload["products"] = products
        if stages is not None:
            payload["stages"] = stages

        return self._session.post(metadata, resource, payload)

    def defer_network_firmware_upgrades_staged_events(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Postpone by 1 week all pending staged upgrade stages for a network.

        https://developer.cisco.com/meraki/api-v1/#!defer-network-firmware-upgrades-staged-events

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "defer_network_firmware_upgrades_staged_events",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/events/defer"

        return self._session.post(metadata, resource)

    def rollbacks_network_firmware_upgrades_staged_events(
        self, *, network_id: str, stages: list, reasons: list | None = None
    ) -> dict[str, Any] | None:
        """Rollback a Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!rollbacks-network-firmware-upgrades-staged-events

        Args:
            network_id: Network ID.
            stages: All completed or in-progress stages in the network with their new start times.
              All pending stages will be canceled.
            reasons: The reason for rolling back the staged upgrade.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "rollbacks_network_firmware_upgrades_staged_events",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/events/rollbacks"

        payload = {}
        if stages is not None:
            payload["stages"] = stages
        if reasons is not None:
            payload["reasons"] = reasons

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_groups(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List of Staged Upgrade Groups in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-groups

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "get_network_firmware_upgrades_staged_groups",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups"

        return self._session.get(metadata, resource)

    def create_network_firmware_upgrades_staged_group(
        self,
        *,
        network_id: str,
        name: str,
        is_default: bool,
        description: str | None = None,
        assigned_devices: dict | None = None,
    ) -> dict[str, Any] | None:
        """Create a Staged Upgrade Group for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            name: Name of the Staged Upgrade Group. Length must be 1 to 255 characters.
            description: Description of the Staged Upgrade Group. Length must be 1 to 255
              characters.
            is_default: Boolean indicating the default Group. Any device that does not have a group
              explicitly assigned will upgrade with this group.
            assigned_devices: The devices and Switch Stacks assigned to the Group.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "create_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups"

        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if is_default is not None:
            payload["isDefault"] = is_default
        if assigned_devices is not None:
            payload["assignedDevices"] = assigned_devices

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_group(
        self, *, network_id: str, group_id: str
    ) -> dict[str, Any] | None:
        """Get a Staged Upgrade Group from a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            group_id: Group ID.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "get_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_id = urllib.parse.quote(str(group_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}"

        return self._session.get(metadata, resource)

    def update_network_firmware_upgrades_staged_group(
        self,
        *,
        network_id: str,
        group_id: str,
        name: str,
        is_default: bool,
        description: str | None = None,
        assigned_devices: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a Staged Upgrade Group for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            group_id: Group ID.
            name: Name of the Staged Upgrade Group. Length must be 1 to 255 characters.
            description: Description of the Staged Upgrade Group. Length must be 1 to 255
              characters.
            is_default: Boolean indicating the default Group. Any device that does not have a group
              explicitly assigned will upgrade with this group.
            assigned_devices: The devices and Switch Stacks assigned to the Group.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "update_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_id = urllib.parse.quote(str(group_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if is_default is not None:
            payload["isDefault"] = is_default
        if assigned_devices is not None:
            payload["assignedDevices"] = assigned_devices

        return self._session.put(metadata, resource, payload)

    def delete_network_firmware_upgrades_staged_group(
        self, *, network_id: str, group_id: str
    ) -> None:
        """Delete a Staged Upgrade Group.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            group_id: Group ID.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "delete_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_id = urllib.parse.quote(str(group_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}"

        return self._session.delete(metadata, resource)

    def get_network_firmware_upgrades_staged_stages(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Order of Staged Upgrade Groups in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-stages

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "stages"],
            "operation": "get_network_firmware_upgrades_staged_stages",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/stages"

        return self._session.get(metadata, resource)

    def update_network_firmware_upgrades_staged_stages(
        self, *, network_id: str, _json: list | None = None
    ) -> dict[str, Any] | None:
        """Assign Staged Upgrade Group order in the sequence.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-stages

        Args:
            network_id: Network ID.
            _json: Array of Staged Upgrade Groups.

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "stages"],
            "operation": "update_network_firmware_upgrades_staged_stages",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/stages"

        payload = {}
        if _json is not None:
            payload["_json"] = _json

        return self._session.put(metadata, resource, payload)

    def get_network_floor_plans(self, *, network_id: str) -> dict[str, Any] | None:
        """List the floor plans that belong to your network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plans

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "get_network_floor_plans",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans"

        return self._session.get(metadata, resource)

    def create_network_floor_plan(
        self,
        *,
        network_id: str,
        name: str,
        image_contents: str,
        center: dict | None = None,
        bottom_left_corner: dict | None = None,
        bottom_right_corner: dict | None = None,
        top_left_corner: dict | None = None,
        top_right_corner: dict | None = None,
        floor_number: float | None = None,
    ) -> dict[str, Any] | None:
        """Upload a floor plan.

        https://developer.cisco.com/meraki/api-v1/#!create-network-floor-plan

        Args:
            network_id: Network ID.
            name: The name of your floor plan.
            center: The longitude and latitude of the center of your floor plan. The 'center' or two
              adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be
              specified. If 'center' is specified, the floor plan is placed over that
              point with no rotation. If two adjacent corners are specified, the floor
              plan is rotated to line up with the two specified points. The aspect ratio
              of the floor plan's image is preserved regardless of which corners/center
              are specified. (This means if that more than two corners are specified,
              only two corners may be used to preserve the floor plan's aspect ratio.).
              No two points can have the same latitude, longitude pair.
            bottom_left_corner: The longitude and latitude of the bottom left corner of your floor
              plan.
            bottom_right_corner: The longitude and latitude of the bottom right corner of your floor
              plan.
            top_left_corner: The longitude and latitude of the top left corner of your floor plan.
            top_right_corner: The longitude and latitude of the top right corner of your floor plan.
            floor_number: The floor number of the floors within the building.
            image_contents: The file contents (a base 64 encoded string) of your image. Supported
              formats are PNG, GIF, and JPG. Note that all images are saved as PNG
              files, regardless of the format they are uploaded in.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "create_network_floor_plan",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans"

        payload = {}
        if name is not None:
            payload["name"] = name
        if center is not None:
            payload["center"] = center
        if bottom_left_corner is not None:
            payload["bottomLeftCorner"] = bottom_left_corner
        if bottom_right_corner is not None:
            payload["bottomRightCorner"] = bottom_right_corner
        if top_left_corner is not None:
            payload["topLeftCorner"] = top_left_corner
        if top_right_corner is not None:
            payload["topRightCorner"] = top_right_corner
        if floor_number is not None:
            payload["floorNumber"] = floor_number
        if image_contents is not None:
            payload["imageContents"] = image_contents

        return self._session.post(metadata, resource, payload)

    def batch_network_floor_plans_auto_locate_jobs(
        self, *, network_id: str, jobs: list
    ) -> dict[str, Any] | None:
        """Schedule auto locate jobs for one or more floor plans in a network.

        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-auto-locate-jobs

        Args:
            network_id: Network ID.
            jobs: The list of auto locate jobs to be scheduled. Up to 100 jobs can be provided in a
              request.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "batch_network_floor_plans_auto_locate_jobs",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/batch"

        payload = {}
        if jobs is not None:
            payload["jobs"] = jobs

        return self._session.post(metadata, resource, payload)

    def cancel_network_floor_plans_auto_locate_job(
        self, *, network_id: str, job_id: str
    ) -> dict[str, Any] | None:
        """Cancel a scheduled or running auto locate job.

        https://developer.cisco.com/meraki/api-v1/#!cancel-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "cancel_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        job_id = urllib.parse.quote(str(job_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/cancel"

        return self._session.post(metadata, resource)

    def publish_network_floor_plans_auto_locate_job(
        self, *, network_id: str, job_id: str, devices: list | None = None
    ) -> dict[str, Any] | None:
        """Update the status of a finished auto locate job to be published, and update device locations.

        https://developer.cisco.com/meraki/api-v1/#!publish-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.
            devices: The list of devices to publish positions for.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "publish_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        job_id = urllib.parse.quote(str(job_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/publish"

        payload = {}
        if devices is not None:
            payload["devices"] = devices

        return self._session.post(metadata, resource, payload)

    def recalculate_network_floor_plans_auto_locate_job(
        self, *, network_id: str, job_id: str, devices: list | None = None
    ) -> dict[str, Any] | None:
        """Trigger auto locate recalculation for a job, and optionally set anchors.

        https://developer.cisco.com/meraki/api-v1/#!recalculate-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.
            devices: The list of devices to update anchor positions for.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "recalculate_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        job_id = urllib.parse.quote(str(job_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/recalculate"

        payload = {}
        if devices is not None:
            payload["devices"] = devices

        return self._session.post(metadata, resource, payload)

    def batch_network_floor_plans_devices_update(
        self, *, network_id: str, assignments: list
    ) -> dict[str, Any] | None:
        """Update floorplan assignments for a batch of devices.

        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-devices-update

        Args:
            network_id: Network ID.
            assignments: List of floorplan assignments to update. Up to 100 floor plan assignments
              can be provided in a request.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "devices"],
            "operation": "batch_network_floor_plans_devices_update",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/devices/batchUpdate"

        payload = {}
        if assignments is not None:
            payload["assignments"] = assignments

        return self._session.post(metadata, resource, payload)

    def get_network_floor_plan(
        self, *, network_id: str, floor_plan_id: str
    ) -> dict[str, Any] | None:
        """Find a floor plan by ID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plan

        Args:
            network_id: Network ID.
            floor_plan_id: Floor plan ID.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "get_network_floor_plan",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        floor_plan_id = urllib.parse.quote(str(floor_plan_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/{floor_plan_id}"

        return self._session.get(metadata, resource)

    def update_network_floor_plan(
        self,
        *,
        network_id: str,
        floor_plan_id: str,
        name: str | None = None,
        center: dict | None = None,
        bottom_left_corner: dict | None = None,
        bottom_right_corner: dict | None = None,
        top_left_corner: dict | None = None,
        top_right_corner: dict | None = None,
        floor_number: float | None = None,
        image_contents: str | None = None,
    ) -> dict[str, Any] | None:
        """Update a floor plan's geolocation and other meta data.

        https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

        Args:
            network_id: Network ID.
            floor_plan_id: Floor plan ID.
            name: The name of your floor plan.
            center: The longitude and latitude of the center of your floor plan. If you want to
              change the geolocation data of your floor plan, either the 'center' or two
              adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be
              specified. If 'center' is specified, the floor plan is placed over that
              point with no rotation. If two adjacent corners are specified, the floor
              plan is rotated to line up with the two specified points. The aspect ratio
              of the floor plan's image is preserved regardless of which corners/center
              are specified. (This means if that more than two corners are specified,
              only two corners may be used to preserve the floor plan's aspect ratio.).
              No two points can have the same latitude, longitude pair.
            bottom_left_corner: The longitude and latitude of the bottom left corner of your floor
              plan.
            bottom_right_corner: The longitude and latitude of the bottom right corner of your floor
              plan.
            top_left_corner: The longitude and latitude of the top left corner of your floor plan.
            top_right_corner: The longitude and latitude of the top right corner of your floor plan.
            floor_number: The floor number of the floors within the building.
            image_contents: The file contents (a base 64 encoded string) of your new image.
              Supported formats are PNG, GIF, and JPG. Note that all images are saved as
              PNG files, regardless of the format they are uploaded in. If you upload a
              new image, and you do NOT specify any new geolocation fields ('center,
              'topLeftCorner', etc), the floor plan will be recentered with no rotation
              in order to maintain the aspect ratio of your new image.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "update_network_floor_plan",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        floor_plan_id = urllib.parse.quote(str(floor_plan_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/{floor_plan_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if center is not None:
            payload["center"] = center
        if bottom_left_corner is not None:
            payload["bottomLeftCorner"] = bottom_left_corner
        if bottom_right_corner is not None:
            payload["bottomRightCorner"] = bottom_right_corner
        if top_left_corner is not None:
            payload["topLeftCorner"] = top_left_corner
        if top_right_corner is not None:
            payload["topRightCorner"] = top_right_corner
        if floor_number is not None:
            payload["floorNumber"] = floor_number
        if image_contents is not None:
            payload["imageContents"] = image_contents

        return self._session.put(metadata, resource, payload)

    def delete_network_floor_plan(self, *, network_id: str, floor_plan_id: str) -> None:
        """Destroy a floor plan.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

        Args:
            network_id: Network ID.
            floor_plan_id: Floor plan ID.

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "delete_network_floor_plan",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        floor_plan_id = urllib.parse.quote(str(floor_plan_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/{floor_plan_id}"

        return self._session.delete(metadata, resource)

    def get_network_group_policies(self, *, network_id: str) -> dict[str, Any] | None:
        """List the group policies in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-group-policies

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "get_network_group_policies",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies"

        return self._session.get(metadata, resource)

    def create_network_group_policy(
        self,
        *,
        network_id: str,
        name: str,
        scheduling: dict | None = None,
        bandwidth: dict | None = None,
        firewall_and_traffic_shaping: dict | None = None,
        content_filtering: dict | None = None,
        splash_auth_settings: str | None = None,
        vlan_tagging: dict | None = None,
        bonjour_forwarding: dict | None = None,
    ) -> dict[str, Any] | None:
        """Create a group policy.

        https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

        Args:
            network_id: Network ID.
            name: The name for your group policy. Required.
            scheduling: The schedule for the group policy. Schedules are applied to days of the
              week.
            bandwidth: The bandwidth settings for clients bound to your group policy.
            firewall_and_traffic_shaping: The firewall and traffic shaping rules and settings for
              your policy.
            content_filtering: The content filtering settings for your group policy.
            splash_auth_settings: Whether clients bound to your policy will bypass splash
              authorization or behave according to the network's rules. Can be one of
              'network default' or 'bypass'. Only available if your network has a
              wireless configuration.
            vlan_tagging: The VLAN tagging settings for your group policy. Only available if your
              network has a wireless configuration.
            bonjour_forwarding: The Bonjour settings for your group policy. Only valid if your
              network has a wireless configuration.

        """
        if splash_auth_settings is not None:
            options = ["bypass", "network default"]
            assert splash_auth_settings in options, (
                f'"splash_auth_settings" cannot be "{splash_auth_settings}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "create_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scheduling is not None:
            payload["scheduling"] = scheduling
        if bandwidth is not None:
            payload["bandwidth"] = bandwidth
        if firewall_and_traffic_shaping is not None:
            payload["firewallAndTrafficShaping"] = firewall_and_traffic_shaping
        if content_filtering is not None:
            payload["contentFiltering"] = content_filtering
        if splash_auth_settings is not None:
            payload["splashAuthSettings"] = splash_auth_settings
        if vlan_tagging is not None:
            payload["vlanTagging"] = vlan_tagging
        if bonjour_forwarding is not None:
            payload["bonjourForwarding"] = bonjour_forwarding

        return self._session.post(metadata, resource, payload)

    def get_network_group_policy(
        self, *, network_id: str, group_policy_id: str
    ) -> dict[str, Any] | None:
        """Display a group policy.

        https://developer.cisco.com/meraki/api-v1/#!get-network-group-policy

        Args:
            network_id: Network ID.
            group_policy_id: Group policy ID.

        """
        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "get_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_policy_id = urllib.parse.quote(str(group_policy_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        return self._session.get(metadata, resource)

    def update_network_group_policy(
        self,
        *,
        network_id: str,
        group_policy_id: str,
        name: str | None = None,
        scheduling: dict | None = None,
        bandwidth: dict | None = None,
        firewall_and_traffic_shaping: dict | None = None,
        content_filtering: dict | None = None,
        splash_auth_settings: str | None = None,
        vlan_tagging: dict | None = None,
        bonjour_forwarding: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update a group policy.

        https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

        Args:
            network_id: Network ID.
            group_policy_id: Group policy ID.
            name: The name for your group policy.
            scheduling: The schedule for the group policy. Schedules are applied to days of the
              week.
            bandwidth: The bandwidth settings for clients bound to your group policy.
            firewall_and_traffic_shaping: The firewall and traffic shaping rules and settings for
              your policy.
            content_filtering: The content filtering settings for your group policy.
            splash_auth_settings: Whether clients bound to your policy will bypass splash
              authorization or behave according to the network's rules. Can be one of
              'network default' or 'bypass'. Only available if your network has a
              wireless configuration.
            vlan_tagging: The VLAN tagging settings for your group policy. Only available if your
              network has a wireless configuration.
            bonjour_forwarding: The Bonjour settings for your group policy. Only valid if your
              network has a wireless configuration.

        """
        if splash_auth_settings is not None:
            options = ["bypass", "network default"]
            assert splash_auth_settings in options, (
                f'"splash_auth_settings" cannot be "{splash_auth_settings}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "update_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_policy_id = urllib.parse.quote(str(group_policy_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scheduling is not None:
            payload["scheduling"] = scheduling
        if bandwidth is not None:
            payload["bandwidth"] = bandwidth
        if firewall_and_traffic_shaping is not None:
            payload["firewallAndTrafficShaping"] = firewall_and_traffic_shaping
        if content_filtering is not None:
            payload["contentFiltering"] = content_filtering
        if splash_auth_settings is not None:
            payload["splashAuthSettings"] = splash_auth_settings
        if vlan_tagging is not None:
            payload["vlanTagging"] = vlan_tagging
        if bonjour_forwarding is not None:
            payload["bonjourForwarding"] = bonjour_forwarding

        return self._session.put(metadata, resource, payload)

    def delete_network_group_policy(
        self, *, network_id: str, group_policy_id: str, force: bool | None = None
    ) -> None:
        """Delete a group policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

        Args:
            network_id: Network ID.
            group_policy_id: Group policy ID.
            force: If true, the system deletes the GP even if there are active clients using the GP.
              After deletion, active clients that were assigned to that Group Policy
              will be left without any policy applied. Default is false.

        """
        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "delete_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_policy_id = urllib.parse.quote(str(group_policy_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        params = {}
        if force is not None:
            params["force"] = force

        return self._session.delete(metadata, resource)

    def get_network_health_alerts(self, *, network_id: str) -> dict[str, Any] | None:
        """Return all global alerts on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-health-alerts

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "health", "alerts"],
            "operation": "get_network_health_alerts",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/health/alerts"

        return self._session.get(metadata, resource)

    def get_network_meraki_auth_users(self, *, network_id: str) -> dict[str, Any] | None:
        """List the authorized users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a MX network).

        https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-users

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "get_network_meraki_auth_users",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers"

        return self._session.get(metadata, resource)

    def create_network_meraki_auth_user(
        self,
        *,
        network_id: str,
        email: str,
        authorizations: list,
        name: str | None = None,
        password: str | None = None,
        account_type: str | None = None,
        email_password_to_user: bool | None = None,
        is_admin: bool | None = None,
    ) -> dict[str, Any] | None:
        """Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap).

        https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

        Args:
            network_id: Network ID.
            email: Email address of the user.
            name: Name of the user. Only required If the user is not a Dashboard administrator.
            password: The password for this user account. Only required If the user is not a
              Dashboard administrator.
            account_type: Authorization type for user. Can be 'Guest' or '802.1X' for wireless
              networks, or 'Client VPN' for MX networks. Defaults to '802.1X'.
            email_password_to_user: Whether or not Meraki should email the password to user. Default
              is false.
            is_admin: Whether or not the user is a Dashboard administrator.
            authorizations: Authorization zones and expiration dates for the user.

        """
        if account_type is not None:
            options = ["802.1X", "Client VPN", "Guest"]
            assert account_type in options, (
                f'"account_type" cannot be "{account_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "create_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers"

        payload = {}
        if email is not None:
            payload["email"] = email
        if name is not None:
            payload["name"] = name
        if password is not None:
            payload["password"] = password
        if account_type is not None:
            payload["accountType"] = account_type
        if email_password_to_user is not None:
            payload["emailPasswordToUser"] = email_password_to_user
        if is_admin is not None:
            payload["isAdmin"] = is_admin
        if authorizations is not None:
            payload["authorizations"] = authorizations

        return self._session.post(metadata, resource, payload)

    def get_network_meraki_auth_user(
        self, *, network_id: str, meraki_auth_user_id: str
    ) -> dict[str, Any] | None:
        """Return the Meraki Auth splash guest, RADIUS, or client VPN user.

        https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-user

        Args:
            network_id: Network ID.
            meraki_auth_user_id: Meraki auth user ID.

        """
        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "get_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        meraki_auth_user_id = urllib.parse.quote(str(meraki_auth_user_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        return self._session.get(metadata, resource)

    def update_network_meraki_auth_user(
        self,
        *,
        network_id: str,
        meraki_auth_user_id: str,
        name: str | None = None,
        password: str | None = None,
        email_password_to_user: bool | None = None,
        authorizations: list | None = None,
    ) -> dict[str, Any] | None:
        """Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated).

        https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

        Args:
            network_id: Network ID.
            meraki_auth_user_id: Meraki auth user ID.
            name: Name of the user. Only allowed If the user is not Dashboard administrator.
            password: The password for this user account. Only allowed If the user is not Dashboard
              administrator.
            email_password_to_user: Whether or not Meraki should email the password to user. Default
              is false.
            authorizations: Authorization zones and expiration dates for the user.

        """
        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "update_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        meraki_auth_user_id = urllib.parse.quote(str(meraki_auth_user_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if password is not None:
            payload["password"] = password
        if email_password_to_user is not None:
            payload["emailPasswordToUser"] = email_password_to_user
        if authorizations is not None:
            payload["authorizations"] = authorizations

        return self._session.put(metadata, resource, payload)

    def delete_network_meraki_auth_user(
        self, *, network_id: str, meraki_auth_user_id: str, delete: bool | None = None
    ) -> None:
        """Delete an 802.1X RADIUS user, or deauthorize and optionally delete a splash guest or client VPN user.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

        Args:
            network_id: Network ID.
            meraki_auth_user_id: Meraki auth user ID.
            delete: If the ID supplied is for a splash guest or client VPN user, and that user is
              not authorized for any other networks in the organization, then also
              delete the user. 802.1X RADIUS users are always deleted regardless of this
              optional attribute.

        """
        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "delete_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        meraki_auth_user_id = urllib.parse.quote(str(meraki_auth_user_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        params = {}
        if delete is not None:
            params["delete"] = delete

        return self._session.delete(metadata, resource)

    def get_network_mqtt_brokers(self, *, network_id: str) -> dict[str, Any] | None:
        """List the MQTT brokers for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-brokers

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "get_network_mqtt_brokers",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers"

        return self._session.get(metadata, resource)

    def create_network_mqtt_broker(
        self,
        *,
        network_id: str,
        name: str,
        host: str,
        port: int,
        security: dict | None = None,
        authentication: dict | None = None,
    ) -> dict[str, Any] | None:
        """Add an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

        Args:
            network_id: Network ID.
            name: Name of the MQTT broker.
            host: Host name/IP address where the MQTT broker runs.
            port: Host port though which the MQTT broker can be reached.
            security: Security settings of the MQTT broker.
            authentication: Authentication settings of the MQTT broker.

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "create_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers"

        payload = {}
        if name is not None:
            payload["name"] = name
        if host is not None:
            payload["host"] = host
        if port is not None:
            payload["port"] = port
        if security is not None:
            payload["security"] = security
        if authentication is not None:
            payload["authentication"] = authentication

        return self._session.post(metadata, resource, payload)

    def get_network_mqtt_broker(
        self, *, network_id: str, mqtt_broker_id: str
    ) -> dict[str, Any] | None:
        """Return an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "get_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers/{mqtt_broker_id}"

        return self._session.get(metadata, resource)

    def update_network_mqtt_broker(
        self,
        *,
        network_id: str,
        mqtt_broker_id: str,
        name: str | None = None,
        host: str | None = None,
        port: int | None = None,
        security: dict | None = None,
        authentication: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.
            name: Name of the MQTT broker.
            host: Host name/IP address where the MQTT broker runs.
            port: Host port though which the MQTT broker can be reached.
            security: Security settings of the MQTT broker.
            authentication: Authentication settings of the MQTT broker.

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "update_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers/{mqtt_broker_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if host is not None:
            payload["host"] = host
        if port is not None:
            payload["port"] = port
        if security is not None:
            payload["security"] = security
        if authentication is not None:
            payload["authentication"] = authentication

        return self._session.put(metadata, resource, payload)

    def delete_network_mqtt_broker(self, *, network_id: str, mqtt_broker_id: str) -> None:
        """Delete an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

        Args:
            network_id: Network ID.
            mqtt_broker_id: Mqtt broker ID.

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "delete_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers/{mqtt_broker_id}"

        return self._session.delete(metadata, resource)

    def get_network_netflow(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the NetFlow traffic reporting settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-netflow

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "netflow"],
            "operation": "get_network_netflow",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/netflow"

        return self._session.get(metadata, resource)

    def update_network_netflow(
        self,
        *,
        network_id: str,
        reporting_enabled: bool | None = None,
        collector_ip: str | None = None,
        collector_port: int | None = None,
        eta_enabled: bool | None = None,
        eta_dst_port: int | None = None,
    ) -> dict[str, Any] | None:
        """Update the NetFlow traffic reporting settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-netflow

        Args:
            network_id: Network ID.
            reporting_enabled: Boolean indicating whether NetFlow traffic reporting is enabled
              (true) or disabled (false).
            collector_ip: The IPv4 address of the NetFlow collector.
            collector_port: The port that the NetFlow collector will be listening on.
            eta_enabled: Boolean indicating whether Encrypted Traffic Analytics is enabled (true) or
              disabled (false).
            eta_dst_port: The port that the Encrypted Traffic Analytics collector will be listening
              on.

        """
        metadata = {
            "tags": ["networks", "configure", "netflow"],
            "operation": "update_network_netflow",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/netflow"

        payload = {}
        if reporting_enabled is not None:
            payload["reportingEnabled"] = reporting_enabled
        if collector_ip is not None:
            payload["collectorIp"] = collector_ip
        if collector_port is not None:
            payload["collectorPort"] = collector_port
        if eta_enabled is not None:
            payload["etaEnabled"] = eta_enabled
        if eta_dst_port is not None:
            payload["etaDstPort"] = eta_dst_port

        return self._session.put(metadata, resource, payload)

    def get_network_network_health_channel_utilization(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get the channel utilization over each radio for all APs in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-network-health-channel-utilization

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              600. The default is 600.
            per_page: The number of entries per page returned. Acceptable range is 3 - 100. Default
              is 10.
            starting_after: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            ending_before: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["networks", "monitor", "networkHealth", "channelUtilization"],
            "operation": "get_network_network_health_channel_utilization",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/networkHealth/channelUtilization"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_pii_pii_keys(
        self,
        *,
        network_id: str,
        username: str | None = None,
        email: str | None = None,
        mac: str | None = None,
        serial: str | None = None,
        imei: str | None = None,
        bluetooth_mac: str | None = None,
    ) -> dict[str, Any] | None:
        """List the keys required to access Personally Identifiable Information (PII) for a given identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-pii-keys

        Args:
            network_id: Network ID.
            username: The username of a Systems Manager user.
            email: The email of a network user account or a Systems Manager device.
            mac: The MAC of a network client device or a Systems Manager device.
            serial: The serial of a Systems Manager device.
            imei: The IMEI of a Systems Manager device.
            bluetooth_mac: The MAC of a Bluetooth client.

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "piiKeys"],
            "operation": "get_network_pii_pii_keys",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/piiKeys"

        params = {}
        if username is not None:
            params["username"] = username
        if email is not None:
            params["email"] = email
        if mac is not None:
            params["mac"] = mac
        if serial is not None:
            params["serial"] = serial
        if imei is not None:
            params["imei"] = imei
        if bluetooth_mac is not None:
            params["bluetoothMac"] = bluetooth_mac

        return self._session.get(metadata, resource, params)

    def get_network_pii_requests(self, *, network_id: str) -> dict[str, Any] | None:
        """List the PII requests for this network or organization.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-requests

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "requests"],
            "operation": "get_network_pii_requests",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/requests"

        return self._session.get(metadata, resource)

    def create_network_pii_request(
        self,
        *,
        network_id: str,
        type_: str | None = None,
        datasets: list | None = None,
        username: str | None = None,
        email: str | None = None,
        mac: str | None = None,
        sm_device_id: str | None = None,
        sm_user_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Submit a new delete or restrict processing PII request.

        https://developer.cisco.com/meraki/api-v1/#!create-network-pii-request

        Args:
            network_id: Network ID.
            type_: One of "delete" or "restrict processing".
            datasets: The datasets related to the provided key that should be deleted. Only applies
              to "delete" requests. The value "all" will be expanded to all datasets
              applicable to this type. The datasets by applicable to each type are: mac
              (usage, events, traffic), email (users, loginAttempts), username (users,
              loginAttempts), bluetoothMac (client, connectivity), smDeviceId (device),
              smUserId (user).
            username: The username of a network log in. Only applies to "delete" requests.
            email: The email of a network user account. Only applies to "delete" requests.
            mac: The MAC of a network client device. Applies to both "restrict processing" and
              "delete" requests.
            sm_device_id: The sm_device_id of a Systems Manager device. The only way to "restrict
              processing" or "delete" a Systems Manager device. Must include "device" in
              the dataset for a "delete" request to destroy the device.
            sm_user_id: The sm_user_id of a Systems Manager user. The only way to "restrict
              processing" or "delete" a Systems Manager user. Must include "user" in the
              dataset for a "delete" request to destroy the user.

        """
        if type_ is not None:
            options = ["delete", "restrict processing"]
            assert type_ in options, (
                f'"type_" cannot be "{type_}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "configure", "pii", "requests"],
            "operation": "create_network_pii_request",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/requests"

        payload = {}
        if type_ is not None:
            payload["type"] = type_
        if datasets is not None:
            payload["datasets"] = datasets
        if username is not None:
            payload["username"] = username
        if email is not None:
            payload["email"] = email
        if mac is not None:
            payload["mac"] = mac
        if sm_device_id is not None:
            payload["smDeviceId"] = sm_device_id
        if sm_user_id is not None:
            payload["smUserId"] = sm_user_id

        return self._session.post(metadata, resource, payload)

    def get_network_pii_request(self, *, network_id: str, request_id: str) -> dict[str, Any] | None:
        """Return a PII request.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-request

        Args:
            network_id: Network ID.
            request_id: Request ID.

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "requests"],
            "operation": "get_network_pii_request",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        request_id = urllib.parse.quote(str(request_id), safe="")
        resource = f"/networks/{network_id}/pii/requests/{request_id}"

        return self._session.get(metadata, resource)

    def delete_network_pii_request(self, *, network_id: str, request_id: str) -> None:
        """Delete a restrict processing PII request.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-pii-request

        Args:
            network_id: Network ID.
            request_id: Request ID.

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "requests"],
            "operation": "delete_network_pii_request",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        request_id = urllib.parse.quote(str(request_id), safe="")
        resource = f"/networks/{network_id}/pii/requests/{request_id}"

        return self._session.delete(metadata, resource)

    def get_network_pii_sm_devices_for_key(
        self,
        *,
        network_id: str,
        username: str | None = None,
        email: str | None = None,
        mac: str | None = None,
        serial: str | None = None,
        imei: str | None = None,
        bluetooth_mac: str | None = None,
    ) -> dict[str, Any] | None:
        """Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-devices-for-key

        Args:
            network_id: Network ID.
            username: The username of a Systems Manager user.
            email: The email of a network user account or a Systems Manager device.
            mac: The MAC of a network client device or a Systems Manager device.
            serial: The serial of a Systems Manager device.
            imei: The IMEI of a Systems Manager device.
            bluetooth_mac: The MAC of a Bluetooth client.

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "smDevicesForKey"],
            "operation": "get_network_pii_sm_devices_for_key",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/smDevicesForKey"

        params = {}
        if username is not None:
            params["username"] = username
        if email is not None:
            params["email"] = email
        if mac is not None:
            params["mac"] = mac
        if serial is not None:
            params["serial"] = serial
        if imei is not None:
            params["imei"] = imei
        if bluetooth_mac is not None:
            params["bluetoothMac"] = bluetooth_mac

        return self._session.get(metadata, resource, params)

    def get_network_pii_sm_owners_for_key(
        self,
        *,
        network_id: str,
        username: str | None = None,
        email: str | None = None,
        mac: str | None = None,
        serial: str | None = None,
        imei: str | None = None,
        bluetooth_mac: str | None = None,
    ) -> dict[str, Any] | None:
        """Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-owners-for-key

        Args:
            network_id: Network ID.
            username: The username of a Systems Manager user.
            email: The email of a network user account or a Systems Manager device.
            mac: The MAC of a network client device or a Systems Manager device.
            serial: The serial of a Systems Manager device.
            imei: The IMEI of a Systems Manager device.
            bluetooth_mac: The MAC of a Bluetooth client.

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "smOwnersForKey"],
            "operation": "get_network_pii_sm_owners_for_key",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/smOwnersForKey"

        params = {}
        if username is not None:
            params["username"] = username
        if email is not None:
            params["email"] = email
        if mac is not None:
            params["mac"] = mac
        if serial is not None:
            params["serial"] = serial
        if imei is not None:
            params["imei"] = imei
        if bluetooth_mac is not None:
            params["bluetoothMac"] = bluetooth_mac

        return self._session.get(metadata, resource, params)

    def get_network_policies_by_client(
        self,
        *,
        network_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        t0: str | None = None,
        timespan: float | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get policies for all clients with policies.

        https://developer.cisco.com/meraki/api-v1/#!get-network-policies-by-client

        Args:
            network_id: Network ID.
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
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["networks", "configure", "policies", "byClient"],
            "operation": "get_network_policies_by_client",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/policies/byClient"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_settings(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-settings

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "settings"],
            "operation": "get_network_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/settings"

        return self._session.get(metadata, resource)

    def update_network_settings(
        self,
        *,
        network_id: str,
        local_status_page_enabled: bool | None = None,
        remote_status_page_enabled: bool | None = None,
        local_status_page: dict | None = None,
        secure_port: dict | None = None,
        named_vlans: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update the settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        Args:
            network_id: Network ID.
            local_status_page_enabled: Enables / disables the local device status pages (<a
              target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a
              target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a
              target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a
              target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>).
              Optional (defaults to false).
            remote_status_page_enabled: Enables / disables access to the device status page (<a
              target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set
              if localStatusPageEnabled is set to true.
            local_status_page: A hash of Local Status page(s)' authentication options applied to the
              Network.
            secure_port: A hash of SecureConnect options applied to the Network.
            named_vlans: A hash of Named VLANs options applied to the Network.

        """
        metadata = {
            "tags": ["networks", "configure", "settings"],
            "operation": "update_network_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/settings"

        payload = {}
        if local_status_page_enabled is not None:
            payload["localStatusPageEnabled"] = local_status_page_enabled
        if remote_status_page_enabled is not None:
            payload["remoteStatusPageEnabled"] = remote_status_page_enabled
        if local_status_page is not None:
            payload["localStatusPage"] = local_status_page
        if secure_port is not None:
            payload["securePort"] = secure_port
        if named_vlans is not None:
            payload["namedVlans"] = named_vlans

        return self._session.put(metadata, resource, payload)

    def get_network_snmp(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the SNMP settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-snmp

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure", "snmp"], "operation": "get_network_snmp"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/snmp"

        return self._session.get(metadata, resource)

    def update_network_snmp(
        self,
        *,
        network_id: str,
        access: str | None = None,
        community_string: str | None = None,
        users: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the SNMP settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-snmp

        Args:
            network_id: Network ID.
            access: The type of SNMP access. Can be one of 'none' (disabled), 'community' (V1/V2c),
              or 'users' (V3).
            community_string: The SNMP community string. Only relevant if 'access' is set to
              'community'.
            users: The list of SNMP users. Only relevant if 'access' is set to 'users'.

        """
        if access is not None:
            options = ["community", "none", "users"]
            assert access in options, (
                f'"access" cannot be "{access}", & must be set to one of: {options}'
            )

        metadata = {"tags": ["networks", "configure", "snmp"], "operation": "update_network_snmp"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/snmp"

        payload = {}
        if access is not None:
            payload["access"] = access
        if community_string is not None:
            payload["communityString"] = community_string
        if users is not None:
            payload["users"] = users

        return self._session.put(metadata, resource, payload)

    def get_network_splash_login_attempts(
        self,
        *,
        network_id: str,
        ssid_number: int | None = None,
        login_identifier: str | None = None,
        timespan: int | None = None,
    ) -> dict[str, Any] | None:
        """List the splash login attempts for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-splash-login-attempts

        Args:
            network_id: Network ID.
            ssid_number: Only return the login attempts for the specified SSID.
            login_identifier: The username, email, or phone number used during login.
            timespan: The timespan, in seconds, for the login attempts. The period will be from
              [timespan] seconds ago until now. The maximum timespan is 3 months.

        """
        if ssid_number is not None:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert ssid_number in options, (
                f'"ssid_number" cannot be "{ssid_number}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["networks", "monitor", "splashLoginAttempts"],
            "operation": "get_network_splash_login_attempts",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/splashLoginAttempts"

        params = {}
        if ssid_number is not None:
            params["ssidNumber"] = ssid_number
        if login_identifier is not None:
            params["loginIdentifier"] = login_identifier
        if timespan is not None:
            params["timespan"] = timespan

        return self._session.get(metadata, resource, params)

    def split_network(self, *, network_id: str) -> dict[str, Any] | None:
        """Split a combined network into individual networks for each type of device.

        https://developer.cisco.com/meraki/api-v1/#!split-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "split_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/split"

        return self._session.post(metadata, resource)

    def get_network_syslog_servers(self, *, network_id: str) -> dict[str, Any] | None:
        """List the syslog servers for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-syslog-servers

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "syslogServers"],
            "operation": "get_network_syslog_servers",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/syslogServers"

        return self._session.get(metadata, resource)

    def update_network_syslog_servers(
        self, *, network_id: str, servers: list
    ) -> dict[str, Any] | None:
        """Update the syslog servers for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-syslog-servers

        Args:
            network_id: Network ID.
            servers: A list of the syslog servers for this network.

        """
        metadata = {
            "tags": ["networks", "configure", "syslogServers"],
            "operation": "update_network_syslog_servers",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/syslogServers"

        payload = {}
        if servers is not None:
            payload["servers"] = servers

        return self._session.put(metadata, resource, payload)

    def get_network_topology_link_layer(self, *, network_id: str) -> dict[str, Any] | None:
        """List the LLDP and CDP information for all discovered devices and connections in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-topology-link-layer

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "monitor", "topology", "linkLayer"],
            "operation": "get_network_topology_link_layer",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/topology/linkLayer"

        return self._session.get(metadata, resource)

    def get_network_traffic(
        self,
        *,
        network_id: str,
        t0: str | None = None,
        timespan: float | None = None,
        device_type: str | None = None,
    ) -> dict[str, Any] | None:
        """Return the traffic analysis data for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 30 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 30 days.
            device_type: Filter the data by device type: 'combined', 'wireless', 'switch' or
              'appliance'. Defaults to 'combined'. When using 'combined', for each rule
              the data will come from the device type with the most usage.

        """
        if device_type is not None:
            options = ["appliance", "combined", "switch", "wireless"]
            assert device_type in options, (
                f'"device_type" cannot be "{device_type}", & must be set to one of: {options}'
            )

        metadata = {"tags": ["networks", "monitor", "traffic"], "operation": "get_network_traffic"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/traffic"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if timespan is not None:
            params["timespan"] = timespan
        if device_type is not None:
            params["deviceType"] = device_type

        return self._session.get(metadata, resource, params)

    def get_network_traffic_analysis(self, *, network_id: str) -> dict[str, Any] | None:
        """Return the traffic analysis settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-analysis

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "trafficAnalysis"],
            "operation": "get_network_traffic_analysis",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/trafficAnalysis"

        return self._session.get(metadata, resource)

    def update_network_traffic_analysis(
        self,
        *,
        network_id: str,
        mode: str | None = None,
        custom_pie_chart_items: list | None = None,
    ) -> dict[str, Any] | None:
        """Update the traffic analysis settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-traffic-analysis

        Args:
            network_id: Network ID.
            mode: The traffic analysis mode for the network. Can be one of 'disabled' (do not
              collect traffic types), 'basic' (collect generic traffic categories), or
              'detailed' (collect destination hostnames).
            custom_pie_chart_items: The list of items that make up the custom pie chart for traffic
              reporting.

        """
        if mode is not None:
            options = ["basic", "detailed", "disabled"]
            assert mode in options, f'"mode" cannot be "{mode}", & must be set to one of: {options}'

        metadata = {
            "tags": ["networks", "configure", "trafficAnalysis"],
            "operation": "update_network_traffic_analysis",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/trafficAnalysis"

        payload = {}
        if mode is not None:
            payload["mode"] = mode
        if custom_pie_chart_items is not None:
            payload["customPieChartItems"] = custom_pie_chart_items

        return self._session.put(metadata, resource, payload)

    def get_network_traffic_shaping_application_categories(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Returns the application categories for traffic shaping rules.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-application-categories

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "trafficShaping", "applicationCategories"],
            "operation": "get_network_traffic_shaping_application_categories",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/trafficShaping/applicationCategories"

        return self._session.get(metadata, resource)

    def get_network_traffic_shaping_dscp_tagging_options(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """Returns the available DSCP tagging options for your traffic shaping rules.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-dscp-tagging-options

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "trafficShaping", "dscpTaggingOptions"],
            "operation": "get_network_traffic_shaping_dscp_tagging_options",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/trafficShaping/dscpTaggingOptions"

        return self._session.get(metadata, resource)

    def unbind_network(
        self, *, network_id: str, retain_configs: bool | None = None
    ) -> dict[str, Any] | None:
        """Unbind a network from a template.

        https://developer.cisco.com/meraki/api-v1/#!unbind-network

        Args:
            network_id: Network ID.
            retain_configs: Optional boolean to retain all the current configs given by the
              template.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "unbind_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/unbind"

        payload = {}
        if retain_configs is not None:
            payload["retainConfigs"] = retain_configs

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profiles(self, *, network_id: str) -> dict[str, Any] | None:
        """List VLAN profiles for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profiles

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "get_network_vlan_profiles",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/vlanProfiles"

        return self._session.get(metadata, resource)

    def create_network_vlan_profile(
        self, *, network_id: str, name: str, vlan_names: list, vlan_groups: list, iname: str
    ) -> dict[str, Any] | None:
        """Create a VLAN profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-vlan-profile

        Args:
            network_id: Network ID.
            name: Name of the profile, string length must be from 1 to 255 characters.
            vlan_names: An array of named VLANs.
            vlan_groups: An array of VLAN groups.
            iname: IName of the profile.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "create_network_vlan_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/vlanProfiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if vlan_names is not None:
            payload["vlanNames"] = vlan_names
        if vlan_groups is not None:
            payload["vlanGroups"] = vlan_groups
        if iname is not None:
            payload["iname"] = iname

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profiles_assignments_by_device(
        self,
        *,
        network_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        serials: list | None = None,
        product_types: list | None = None,
        stack_ids: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Get the assigned VLAN Profiles for devices in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profiles-assignments-by-device

        Args:
            network_id: Network ID.
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
            serials: Optional parameter to filter devices by serials. All devices returned belong to
              serial numbers that are an exact match.
            product_types: Optional parameter to filter devices by product types.
            stack_ids: Optional parameter to filter devices by Switch Stack ids.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles", "assignments", "byDevice"],
            "operation": "get_network_vlan_profiles_assignments_by_device",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/assignments/byDevice"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before
        if serials is not None:
            params["serials[]"] = serials
        if product_types is not None:
            params["productTypes[]"] = product_types
        if stack_ids is not None:
            params["stackIds[]"] = stack_ids

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def reassign_network_vlan_profiles_assignments(
        self, *, network_id: str, serials: list, stack_ids: list, vlan_profile: dict | None = None
    ) -> dict[str, Any] | None:
        """Update the assigned VLAN Profile for devices in a network.

        https://developer.cisco.com/meraki/api-v1/#!reassign-network-vlan-profiles-assignments

        Args:
            network_id: Network ID.
            vlan_profile: The VLAN Profile.
            serials: Array of Device Serials.
            stack_ids: Array of Switch Stack IDs.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles", "assignments"],
            "operation": "reassign_network_vlan_profiles_assignments",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/assignments/reassign"

        payload = {}
        if vlan_profile is not None:
            payload["vlanProfile"] = vlan_profile
        if serials is not None:
            payload["serials"] = serials
        if stack_ids is not None:
            payload["stackIds"] = stack_ids

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profile(self, *, network_id: str, iname: str) -> dict[str, Any] | None:
        """Get an existing VLAN profile of a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profile

        Args:
            network_id: Network ID.
            iname: Iname.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "get_network_vlan_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/{iname}"

        return self._session.get(metadata, resource)

    def update_network_vlan_profile(
        self, *, network_id: str, iname: str, name: str, vlan_names: list, vlan_groups: list
    ) -> dict[str, Any] | None:
        """Update an existing VLAN profile of a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-vlan-profile

        Args:
            network_id: Network ID.
            iname: Iname.
            name: Name of the profile, string length must be from 1 to 255 characters.
            vlan_names: An array of named VLANs.
            vlan_groups: An array of VLAN groups.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "update_network_vlan_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/{iname}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if vlan_names is not None:
            payload["vlanNames"] = vlan_names
        if vlan_groups is not None:
            payload["vlanGroups"] = vlan_groups

        return self._session.put(metadata, resource, payload)

    def delete_network_vlan_profile(self, *, network_id: str, iname: str) -> None:
        """Delete a VLAN profile of a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-vlan-profile

        Args:
            network_id: Network ID.
            iname: Iname.

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "delete_network_vlan_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/{iname}"

        return self._session.delete(metadata, resource)

    def get_network_webhooks_http_servers(self, *, network_id: str) -> dict[str, Any] | None:
        """List the HTTP servers for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-servers

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "get_network_webhooks_http_servers",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/httpServers"

        return self._session.get(metadata, resource)

    def create_network_webhooks_http_server(
        self,
        *,
        network_id: str,
        name: str,
        url: str,
        shared_secret: str | None = None,
        payload_template: dict | None = None,
    ) -> dict[str, Any] | None:
        """Add an HTTP server to a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-http-server

        Args:
            network_id: Network ID.
            name: A name for easy reference to the HTTP server.
            url: The URL of the HTTP server. Once set, cannot be updated.
            shared_secret: A shared secret that will be included in POSTs sent to the HTTP server.
              This secret can be used to verify that the request was sent by Meraki.
            payload_template: The payload template to use when posting data to the HTTP server.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "create_network_webhooks_http_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/httpServers"

        payload = {}
        if name is not None:
            payload["name"] = name
        if url is not None:
            payload["url"] = url
        if shared_secret is not None:
            payload["sharedSecret"] = shared_secret
        if payload_template is not None:
            payload["payloadTemplate"] = payload_template

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_http_server(
        self, *, network_id: str, http_server_id: str
    ) -> dict[str, Any] | None:
        """Return an HTTP server for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-server

        Args:
            network_id: Network ID.
            http_server_id: Http server ID.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "get_network_webhooks_http_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        http_server_id = urllib.parse.quote(str(http_server_id), safe="")
        resource = f"/networks/{network_id}/webhooks/httpServers/{http_server_id}"

        return self._session.get(metadata, resource)

    def update_network_webhooks_http_server(
        self,
        *,
        network_id: str,
        http_server_id: str,
        name: str | None = None,
        shared_secret: str | None = None,
        payload_template: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update an HTTP server.

        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-http-server

        Args:
            network_id: Network ID.
            http_server_id: Http server ID.
            name: A name for easy reference to the HTTP server.
            shared_secret: A shared secret that will be included in POSTs sent to the HTTP server.
              This secret can be used to verify that the request was sent by Meraki.
            payload_template: The payload template to use when posting data to the HTTP server.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "update_network_webhooks_http_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        http_server_id = urllib.parse.quote(str(http_server_id), safe="")
        resource = f"/networks/{network_id}/webhooks/httpServers/{http_server_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if shared_secret is not None:
            payload["sharedSecret"] = shared_secret
        if payload_template is not None:
            payload["payloadTemplate"] = payload_template

        return self._session.put(metadata, resource, payload)

    def delete_network_webhooks_http_server(self, *, network_id: str, http_server_id: str) -> None:
        """Delete an HTTP server from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-http-server

        Args:
            network_id: Network ID.
            http_server_id: Http server ID.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "delete_network_webhooks_http_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        http_server_id = urllib.parse.quote(str(http_server_id), safe="")
        resource = f"/networks/{network_id}/webhooks/httpServers/{http_server_id}"

        return self._session.delete(metadata, resource)

    def get_network_webhooks_payload_templates(self, *, network_id: str) -> dict[str, Any] | None:
        """List the webhook payload templates for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-templates

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "get_network_webhooks_payload_templates",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates"

        return self._session.get(metadata, resource)

    def create_network_webhooks_payload_template(
        self,
        *,
        network_id: str,
        name: str,
        body: str | None = None,
        headers: list | None = None,
        body_file: str | None = None,
        headers_file: str | None = None,
    ) -> dict[str, Any] | None:
        """Create a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            name: The name of the new template.
            body: The liquid template used for the body of the webhook message. Either `body` or
              `bodyFile` must be specified.
            headers: The liquid template used with the webhook headers.
            body_file: A Base64 encoded file containing liquid template used for the body of the
              webhook message. Either `body` or `bodyFile` must be specified.
            headers_file: A Base64 encoded file containing the liquid template used with the webhook
              headers.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "create_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates"

        payload = {}
        if name is not None:
            payload["name"] = name
        if body is not None:
            payload["body"] = body
        if headers is not None:
            payload["headers"] = headers
        if body_file is not None:
            payload["bodyFile"] = body_file
        if headers_file is not None:
            payload["headersFile"] = headers_file

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_payload_template(
        self, *, network_id: str, payload_template_id: str
    ) -> dict[str, Any] | None:
        """Get the webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            payload_template_id: Payload template ID.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "get_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        payload_template_id = urllib.parse.quote(str(payload_template_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}"

        return self._session.get(metadata, resource)

    def update_network_webhooks_payload_template(
        self,
        *,
        network_id: str,
        payload_template_id: str,
        name: str | None = None,
        body: str | None = None,
        headers: list | None = None,
        body_file: str | None = None,
        headers_file: str | None = None,
    ) -> dict[str, Any] | None:
        """Update a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            payload_template_id: Payload template ID.
            name: The name of the template.
            body: The liquid template used for the body of the webhook message.
            headers: The liquid template used with the webhook headers.
            body_file: A file containing liquid template used for the body of the webhook message.
            headers_file: A file containing the liquid template used with the webhook headers.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "update_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        payload_template_id = urllib.parse.quote(str(payload_template_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if body is not None:
            payload["body"] = body
        if headers is not None:
            payload["headers"] = headers
        if body_file is not None:
            payload["bodyFile"] = body_file
        if headers_file is not None:
            payload["headersFile"] = headers_file

        return self._session.put(metadata, resource, payload)

    def delete_network_webhooks_payload_template(
        self, *, network_id: str, payload_template_id: str
    ) -> None:
        """Destroy a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            payload_template_id: Payload template ID.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "delete_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        payload_template_id = urllib.parse.quote(str(payload_template_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}"

        return self._session.delete(metadata, resource)

    def create_network_webhooks_webhook_test(
        self,
        *,
        network_id: str,
        url: str,
        shared_secret: str | None = None,
        payload_template_id: str | None = None,
        payload_template_name: str | None = None,
        alert_type_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Send a test webhook for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-webhook-test

        Args:
            network_id: Network ID.
            url: The URL where the test webhook will be sent.
            shared_secret: The shared secret the test webhook will send. Optional. Defaults to HTTP
              server's shared secret. Otherwise, defaults to an empty string.
            payload_template_id: The ID of the payload template of the test webhook. Defaults to the
              HTTP server's template ID if one exists for the given URL, or Generic
              template ID otherwise.
            payload_template_name: The name of the payload template.
            alert_type_id: The type of alert which the test webhook will send. Optional. Defaults to
              power_supply_down.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "webhookTests"],
            "operation": "create_network_webhooks_webhook_test",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/webhookTests"

        payload = {}
        if url is not None:
            payload["url"] = url
        if shared_secret is not None:
            payload["sharedSecret"] = shared_secret
        if payload_template_id is not None:
            payload["payloadTemplateId"] = payload_template_id
        if payload_template_name is not None:
            payload["payloadTemplateName"] = payload_template_name
        if alert_type_id is not None:
            payload["alertTypeId"] = alert_type_id

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_webhook_test(
        self, *, network_id: str, webhook_test_id: str
    ) -> dict[str, Any] | None:
        """Return the status of a webhook test for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-webhook-test

        Args:
            network_id: Network ID.
            webhook_test_id: Webhook test ID.

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "webhookTests"],
            "operation": "get_network_webhooks_webhook_test",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        webhook_test_id = urllib.parse.quote(str(webhook_test_id), safe="")
        resource = f"/networks/{network_id}/webhooks/webhookTests/{webhook_test_id}"

        return self._session.get(metadata, resource)
