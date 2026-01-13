"""Networks API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.rest_session import RestSession


class Networks:
    """Networks class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
        self._session = session

    def get_network(self, network_id: str) -> dict[str, Any] | None:
        """Return a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "get_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}"

        return self._session.get(metadata, resource)

    def update_network(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Update a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network

        Args:
            network_id: Network ID.
            name: The name of the network.
            timeZone: The timezone of the network. For a list of allowed timezones, please see the
              'TZ' column in the table in <a target='_blank'
              href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this
              article.</a>.
            tags: A list of tags to be applied to the network.
            enrollmentString: A unique identifier which can be used for device enrollment or easy
              access through the Meraki SM Registration page or the Self Service Portal.
              Please note that changing this field may cause existing bookmarks to
              break.
            notes: Add any notes or additional information about this network here.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "update_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}"

        body_params = [
            "name",
            "timeZone",
            "tags",
            "enrollmentString",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network(self, network_id: str) -> None:
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
        self, network_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the alert history for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-history

        Args:
            network_id: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 100.
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
            "tags": ["networks", "monitor", "alerts", "history"],
            "operation": "get_network_alerts_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/alerts/history"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_alerts_settings(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the alert configuration for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-alerts-settings

        Args:
            network_id: Network ID.
            defaultDestinations: The network-wide destinations for all alerts on the network.
            alerts: Alert-specific configuration for each type. Only alerts that pertain to the
              network can be updated.
            muting: Mute alerts under certain conditions.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "alerts", "settings"],
            "operation": "update_network_alerts_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/alerts/settings"

        body_params = [
            "defaultDestinations",
            "alerts",
            "muting",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def bind_network(
        self, network_id: str, configTemplateId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Bind a network to a template.

        https://developer.cisco.com/meraki/api-v1/#!bind-network

        Args:
            network_id: Network ID.
            configTemplateId: The ID of the template to which the network should be bound.
            autoBind: Optional boolean indicating whether the network's switches should
              automatically bind to profiles of the same model. Defaults to false if
              left unspecified. This option only affects switch networks and switch
              templates. Auto-bind is not valid unless the switch template has at least
              one profile and has at most one profile per switch model.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "bind_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/bind"

        body_params = [
            "configTemplateId",
            "autoBind",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_bluetooth_clients(
        self, network_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the Bluetooth clients seen by APs in this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-clients

        Args:
            network_id: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 7 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 7 days. The default is 1 day.
            perPage: The number of entries per page returned. Acceptable range is 5 - 1000. Default
              is 10.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            includeConnectivityHistory: Include the connectivity history for this client.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "bluetoothClients"],
            "operation": "get_network_bluetooth_clients",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/bluetoothClients"

        query_params = [
            "t0",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "includeConnectivityHistory",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_bluetooth_client(
        self, network_id: str, bluetooth_client_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return a Bluetooth client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-client

        Args:
            network_id: Network ID.
            bluetooth_client_id: Bluetooth client ID.
            includeConnectivityHistory: Include the connectivity history for this client.
            connectivityHistoryTimespan: The timespan, in seconds, for the connectivityHistory data.
              By default 1 day, 86400, will be used.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "bluetoothClients"],
            "operation": "get_network_bluetooth_client",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        bluetooth_client_id = urllib.parse.quote(str(bluetooth_client_id), safe="")
        resource = f"/networks/{network_id}/bluetoothClients/{bluetooth_client_id}"

        query_params = [
            "includeConnectivityHistory",
            "connectivityHistoryTimespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_clients(
        self, network_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the clients that have used this network in the timespan.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients

        Args:
            network_id: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.
            perPage: The number of entries per page returned. Acceptable range is 3 - 5000. Default
              is 10.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            statuses: Filters clients based on status. Can be one of 'Online' or 'Offline'.
            ip: Filters clients based on a partial or full match for the ip address field.
            ip6: Filters clients based on a partial or full match for the ip6 address field.
            ip6Local: Filters clients based on a partial or full match for the ip6Local address
              field.
            mac: Filters clients based on a partial or full match for the mac address field.
            os: Filters clients based on a partial or full match for the os (operating system)
              field.
            pskGroup: Filters clients based on partial or full match for the iPSK name field.
            description: Filters clients based on a partial or full match for the description field.
            vlan: Filters clients based on the full match for the VLAN field.
            namedVlan: Filters clients based on the partial or full match for the named VLAN field.
            recentDeviceConnections: Filters clients based on recent connection type. Can be one of
              'Wired' or 'Wireless'.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "monitor", "clients"], "operation": "get_network_clients"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients"

        query_params = [
            "t0",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "statuses",
            "ip",
            "ip6",
            "ip6Local",
            "mac",
            "os",
            "pskGroup",
            "description",
            "vlan",
            "namedVlan",
            "recentDeviceConnections",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "statuses",
            "recentDeviceConnections",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_clients_application_usage(
        self, network_id: str, clients: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the application usage data for clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-application-usage

        Args:
            network_id: Network ID.
            clients: A list of client keys, MACs or IPs separated by comma.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            ssidNumber: An SSID number to include. If not specified, events for all SSIDs will be
              returned.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.

        """
        kwargs.update(locals())

        if "ssidNumber" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssidNumber"] in options, (
                f'''"ssidNumber" cannot be "{kwargs["ssidNumber"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "monitor", "clients", "applicationUsage"],
            "operation": "get_network_clients_application_usage",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/applicationUsage"

        query_params = [
            "clients",
            "ssidNumber",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_clients_bandwidth_usage_history(
        self, network_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-bandwidth-usage-history

        Args:
            network_id: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 30 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
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
            "tags": ["networks", "monitor", "clients", "bandwidthUsageHistory"],
            "operation": "get_network_clients_bandwidth_usage_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/bandwidthUsageHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_clients_overview(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
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
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "clients", "overview"],
            "operation": "get_network_clients_overview",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/overview"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def provision_network_clients(
        self, network_id: str, clients: list, devicePolicy: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Provisions a client with a name and policy.

        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        Args:
            network_id: Network ID.
            clients: The array of clients to provision.
            devicePolicy: The policy to apply to the specified client. Can be 'Group policy',
              'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
            groupPolicyId: The ID of the desired group policy to apply to the client. Required if
              'devicePolicy' is set to "Group policy". Otherwise this is ignored.
            policiesBySecurityAppliance: An object, describing what the policy-connection
              association is for the security appliance. (Only relevant if the security
              appliance is actually within the network).
            policiesBySsid: An object, describing the policy-connection associations for each active
              SSID within the network. Keys should be the number of enabled SSIDs,
              mapping to an object describing the client's policy.

        """
        kwargs.update(locals())

        if "devicePolicy" in kwargs:
            options = ["Allowed", "Blocked", "Group policy", "Normal", "Per connection"]
            assert kwargs["devicePolicy"] in options, (
                f'''"devicePolicy" cannot be "{kwargs["devicePolicy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "clients"],
            "operation": "provision_network_clients",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/provision"

        body_params = [
            "clients",
            "devicePolicy",
            "groupPolicyId",
            "policiesBySecurityAppliance",
            "policiesBySsid",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_clients_usage_histories(
        self, network_id: str, clients: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the usage histories for clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-usage-histories

        Args:
            network_id: Network ID.
            clients: A list of client keys, MACs or IPs separated by comma.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            ssidNumber: An SSID number to include. If not specified, events for all SSIDs will be
              returned.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.

        """
        kwargs.update(locals())

        if "ssidNumber" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssidNumber"] in options, (
                f'''"ssidNumber" cannot be "{kwargs["ssidNumber"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "monitor", "clients", "usageHistories"],
            "operation": "get_network_clients_usage_histories",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/clients/usageHistories"

        query_params = [
            "clients",
            "ssidNumber",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_client(self, network_id: str, client_id: str) -> dict[str, Any] | None:
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

    def get_network_client_policy(self, network_id: str, client_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, client_id: str, devicePolicy: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the policy assigned to a client on the network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-client-policy

        Args:
            network_id: Network ID.
            client_id: Client ID.
            devicePolicy: The policy to assign. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group
              policy'. Required.
            groupPolicyId: [Optional] If 'devicePolicy' is set to 'Group policy' this param is used
              to specify the group policy ID.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "clients", "policy"],
            "operation": "update_network_client_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/policy"

        body_params = [
            "devicePolicy",
            "groupPolicyId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_client_splash_authorization_status(
        self, network_id: str, client_id: str
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
        self, network_id: str, client_id: str, ssids: dict
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
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "clients", "splashAuthorizationStatus"],
            "operation": "update_network_client_splash_authorization_status",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus"

        body_params = [
            "ssids",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_client_traffic_history(
        self, network_id: str, client_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return the client's network traffic data over time.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-traffic-history

        Args:
            network_id: Network ID.
            client_id: Client ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000.
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
            "tags": ["networks", "monitor", "clients", "trafficHistory"],
            "operation": "get_network_client_traffic_history",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        client_id = urllib.parse.quote(str(client_id), safe="")
        resource = f"/networks/{network_id}/clients/{client_id}/trafficHistory"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_client_usage_history(
        self, network_id: str, client_id: str
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

    def get_network_devices(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, serials: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed).

        https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

        Args:
            network_id: Network ID.
            serials: A list of serials of devices to claim.
            addAtomically: Whether to claim devices atomically. If true, all devices will be claimed
              or none will be claimed. Default is true.
            detailsByDevice: Optional details for claimed devices (currently only used for Catalyst
              devices).

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "claim_network_devices",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/claim"

        body_params = [
            "serials",
            "detailsByDevice",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def vmx_network_devices_claim(self, network_id: str, size: str) -> dict[str, Any] | None:
        """Claim a vMX into a network.

        https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim

        Args:
            network_id: Network ID.
            size: The size of the vMX you claim. It can be one of: small, medium, large, xlarge,
              100.

        """
        kwargs = locals()

        if "size" in kwargs:
            options = ["100", "large", "medium", "small", "xlarge"]
            assert kwargs["size"] in options, (
                f'''"size" cannot be "{kwargs["size"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "devices", "claim"],
            "operation": "vmx_network_devices_claim",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/claim/vmx"

        body_params = [
            "size",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def remove_network_devices(self, network_id: str, serial: str) -> dict[str, Any] | None:
        """Remove a single device.

        https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

        Args:
            network_id: Network ID.
            serial: The serial of a device.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "remove_network_devices",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/devices/remove"

        body_params = [
            "serial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_events(
        self,
        network_id: str,
        total_pages=1,
        direction="prev",
        event_log_end_time=None,
        **kwargs: Any,
    ) -> Generator[Any, None, None]:
        """List the events for the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-events

        Args:
            network_id: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" or "prev" (default) page.
            event_log_end_time: ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, to
              retrieve events within a time window.
            productType: The product type to fetch events for. This parameter is required for
              networks with multiple device types. Valid types are wireless, appliance,
              switch, systemsManager, camera, cellularGateway, wirelessController,
              campusGateway, and secureConnect.
            includedEventTypes: A list of event types. The returned events will be filtered to only
              include events with these types.
            excludedEventTypes: A list of event types. The returned events will be filtered to
              exclude events with these types.
            deviceMac: The MAC address of the Meraki device which the list of events will be
              filtered with.
            deviceSerial: The serial of the Meraki device which the list of events will be filtered
              with.
            deviceName: The name of the Meraki device which the list of events will be filtered
              with.
            clientIp: The IP of the client which the list of events will be filtered with. Only
              supported for track-by-IP networks.
            clientMac: The MAC address of the client which the list of events will be filtered with.
              Only supported for track-by-MAC networks.
            clientName: The name, or partial name, of the client which the list of events will be
              filtered with.
            smDeviceMac: The MAC address of the Systems Manager device which the list of events will
              be filtered with.
            smDeviceName: The name of the Systems Manager device which the list of events will be
              filtered with.
            eventDetails: The details of the event(Catalyst device only) which the list of events
              will be filtered with.
            eventSeverity: The severity of the event(Catalyst device only) which the list of events
              will be filtered with.
            isCatalyst: Boolean indicating that whether it is a Catalyst device. For Catalyst
              device, eventDetails and eventSeverity can be used to filter events.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 10.
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

        if "productType" in kwargs:
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
            assert kwargs["productType"] in options, (
                f'''"productType" cannot be "{kwargs["productType"]}", & must be set to one of: {options}'''
            )

        metadata = {"tags": ["networks", "monitor", "events"], "operation": "get_network_events"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/events"

        query_params = [
            "productType",
            "includedEventTypes",
            "excludedEventTypes",
            "deviceMac",
            "deviceSerial",
            "deviceName",
            "clientIp",
            "clientMac",
            "clientName",
            "smDeviceMac",
            "smDeviceName",
            "eventDetails",
            "eventSeverity",
            "isCatalyst",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "includedEventTypes",
            "excludedEventTypes",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(
            metadata, resource, params, total_pages, direction, event_log_end_time
        )

    def get_network_events_event_types(self, network_id: str) -> dict[str, Any] | None:
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

    def get_network_firmware_upgrades(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update firmware upgrade information for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

        Args:
            network_id: Network ID.
            upgradeWindow: Upgrade window for devices in network.
            timezone: The timezone for the network.
            products: Contains information about the network to update.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades"],
            "operation": "update_network_firmware_upgrades",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades"

        body_params = [
            "upgradeWindow",
            "timezone",
            "products",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def create_network_firmware_upgrades_rollback(
        self, network_id: str, reasons: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Rollback a Firmware Upgrade For A Network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

        Args:
            network_id: Network ID.
            reasons: Reasons for the rollback.
            product: Product type to rollback (if the network is a combined network).
            time: Scheduled time for the rollback.
            toVersion: Version to downgrade to (if the network has firmware flexibility).

        """
        kwargs.update(locals())

        if "product" in kwargs:
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
            assert kwargs["product"] in options, (
                f'''"product" cannot be "{kwargs["product"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "rollbacks"],
            "operation": "create_network_firmware_upgrades_rollback",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/rollbacks"

        body_params = [
            "product",
            "time",
            "reasons",
            "toVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_events(self, network_id: str) -> dict[str, Any] | None:
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

    def create_network_firmware_upgrades_staged_event(
        self, network_id: str, stages: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-event

        Args:
            network_id: Network ID.
            stages: All firmware upgrade stages in the network with their start time.
            products: Contains firmware upgrade version information.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "create_network_firmware_upgrades_staged_event",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/events"

        body_params = [
            "products",
            "stages",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_network_firmware_upgrades_staged_events(
        self, network_id: str, stages: list
    ) -> dict[str, Any] | None:
        """Update the Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-events

        Args:
            network_id: Network ID.
            stages: All firmware upgrade stages in the network with their start time.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "update_network_firmware_upgrades_staged_events",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/events"

        body_params = [
            "stages",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def defer_network_firmware_upgrades_staged_events(
        self, network_id: str
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
        self, network_id: str, stages: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Rollback a Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!rollbacks-network-firmware-upgrades-staged-events

        Args:
            network_id: Network ID.
            stages: All completed or in-progress stages in the network with their new start times.
              All pending stages will be canceled.
            reasons: The reason for rolling back the staged upgrade.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "rollbacks_network_firmware_upgrades_staged_events",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/events/rollbacks"

        body_params = [
            "stages",
            "reasons",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_groups(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, name: str, isDefault: bool, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a Staged Upgrade Group for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            name: Name of the Staged Upgrade Group. Length must be 1 to 255 characters.
            isDefault: Boolean indicating the default Group. Any device that does not have a group
              explicitly assigned will upgrade with this group.
            description: Description of the Staged Upgrade Group. Length must be 1 to 255
              characters.
            assignedDevices: The devices and Switch Stacks assigned to the Group.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "create_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups"

        body_params = [
            "name",
            "description",
            "isDefault",
            "assignedDevices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_group(
        self, network_id: str, group_id: str
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
        self, network_id: str, group_id: str, name: str, isDefault: bool, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a Staged Upgrade Group for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-group

        Args:
            network_id: Network ID.
            group_id: Group ID.
            name: Name of the Staged Upgrade Group. Length must be 1 to 255 characters.
            isDefault: Boolean indicating the default Group. Any device that does not have a group
              explicitly assigned will upgrade with this group.
            description: Description of the Staged Upgrade Group. Length must be 1 to 255
              characters.
            assignedDevices: The devices and Switch Stacks assigned to the Group.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "update_network_firmware_upgrades_staged_group",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_id = urllib.parse.quote(str(group_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}"

        body_params = [
            "name",
            "description",
            "isDefault",
            "assignedDevices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_firmware_upgrades_staged_group(self, network_id: str, group_id: str) -> None:
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

    def get_network_firmware_upgrades_staged_stages(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Assign Staged Upgrade Group order in the sequence.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-stages

        Args:
            network_id: Network ID.
            _json: Array of Staged Upgrade Groups.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "stages"],
            "operation": "update_network_firmware_upgrades_staged_stages",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/firmwareUpgrades/staged/stages"

        body_params = [
            "_json",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_floor_plans(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, name: str, imageContents: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Upload a floor plan.

        https://developer.cisco.com/meraki/api-v1/#!create-network-floor-plan

        Args:
            network_id: Network ID.
            name: The name of your floor plan.
            imageContents: The file contents (a base 64 encoded string) of your image. Supported
              formats are PNG, GIF, and JPG. Note that all images are saved as PNG
              files, regardless of the format they are uploaded in.
            center: The longitude and latitude of the center of your floor plan. The 'center' or two
              adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be
              specified. If 'center' is specified, the floor plan is placed over that
              point with no rotation. If two adjacent corners are specified, the floor
              plan is rotated to line up with the two specified points. The aspect ratio
              of the floor plan's image is preserved regardless of which corners/center
              are specified. (This means if that more than two corners are specified,
              only two corners may be used to preserve the floor plan's aspect ratio.).
              No two points can have the same latitude, longitude pair.
            bottomLeftCorner: The longitude and latitude of the bottom left corner of your floor
              plan.
            bottomRightCorner: The longitude and latitude of the bottom right corner of your floor
              plan.
            topLeftCorner: The longitude and latitude of the top left corner of your floor plan.
            topRightCorner: The longitude and latitude of the top right corner of your floor plan.
            floorNumber: The floor number of the floors within the building.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "create_network_floor_plan",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans"

        body_params = [
            "name",
            "center",
            "bottomLeftCorner",
            "bottomRightCorner",
            "topLeftCorner",
            "topRightCorner",
            "floorNumber",
            "imageContents",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def batch_network_floor_plans_auto_locate_jobs(
        self, network_id: str, jobs: list
    ) -> dict[str, Any] | None:
        """Schedule auto locate jobs for one or more floor plans in a network.

        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-auto-locate-jobs

        Args:
            network_id: Network ID.
            jobs: The list of auto locate jobs to be scheduled. Up to 100 jobs can be provided in a
              request.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "batch_network_floor_plans_auto_locate_jobs",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/batch"

        body_params = [
            "jobs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def cancel_network_floor_plans_auto_locate_job(
        self, network_id: str, job_id: str
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
        self, network_id: str, job_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the status of a finished auto locate job to be published, and update device locations.

        https://developer.cisco.com/meraki/api-v1/#!publish-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.
            devices: The list of devices to publish positions for.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "publish_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        job_id = urllib.parse.quote(str(job_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/publish"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def recalculate_network_floor_plans_auto_locate_job(
        self, network_id: str, job_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Trigger auto locate recalculation for a job, and optionally set anchors.

        https://developer.cisco.com/meraki/api-v1/#!recalculate-network-floor-plans-auto-locate-job

        Args:
            network_id: Network ID.
            job_id: Job ID.
            devices: The list of devices to update anchor positions for.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "recalculate_network_floor_plans_auto_locate_job",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        job_id = urllib.parse.quote(str(job_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/autoLocate/jobs/{job_id}/recalculate"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def batch_network_floor_plans_devices_update(
        self, network_id: str, assignments: list
    ) -> dict[str, Any] | None:
        """Update floorplan assignments for a batch of devices.

        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-devices-update

        Args:
            network_id: Network ID.
            assignments: List of floorplan assignments to update. Up to 100 floor plan assignments
              can be provided in a request.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "devices"],
            "operation": "batch_network_floor_plans_devices_update",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/devices/batchUpdate"

        body_params = [
            "assignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_floor_plan(self, network_id: str, floor_plan_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, floor_plan_id: str, **kwargs: Any
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
            bottomLeftCorner: The longitude and latitude of the bottom left corner of your floor
              plan.
            bottomRightCorner: The longitude and latitude of the bottom right corner of your floor
              plan.
            topLeftCorner: The longitude and latitude of the top left corner of your floor plan.
            topRightCorner: The longitude and latitude of the top right corner of your floor plan.
            floorNumber: The floor number of the floors within the building.
            imageContents: The file contents (a base 64 encoded string) of your new image. Supported
              formats are PNG, GIF, and JPG. Note that all images are saved as PNG
              files, regardless of the format they are uploaded in. If you upload a new
              image, and you do NOT specify any new geolocation fields ('center,
              'topLeftCorner', etc), the floor plan will be recentered with no rotation
              in order to maintain the aspect ratio of your new image.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "update_network_floor_plan",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        floor_plan_id = urllib.parse.quote(str(floor_plan_id), safe="")
        resource = f"/networks/{network_id}/floorPlans/{floor_plan_id}"

        body_params = [
            "name",
            "center",
            "bottomLeftCorner",
            "bottomRightCorner",
            "topLeftCorner",
            "topRightCorner",
            "floorNumber",
            "imageContents",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_floor_plan(self, network_id: str, floor_plan_id: str) -> None:
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

    def get_network_group_policies(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a group policy.

                https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

                Args:
                    network_id: Network ID.
                    name: The name for your group policy. Required.
                    scheduling:     The schedule for the group policy. Schedules are applied to days of the
                      week. .
                    bandwidth:     The bandwidth settings for clients bound to your group policy.
        .
                    firewallAndTrafficShaping:     The firewall and traffic shaping rules and settings for
                      your policy. .
                    contentFiltering: The content filtering settings for your group policy.
                    splashAuthSettings: Whether clients bound to your policy will bypass splash
                      authorization or behave according to the network's rules. Can be one of
                      'network default' or 'bypass'. Only available if your network has a
                      wireless configuration.
                    vlanTagging: The VLAN tagging settings for your group policy. Only available if your
                      network has a wireless configuration.
                    bonjourForwarding: The Bonjour settings for your group policy. Only valid if your
                      network has a wireless configuration.

        """
        kwargs.update(locals())

        if "splashAuthSettings" in kwargs:
            options = ["bypass", "network default"]
            assert kwargs["splashAuthSettings"] in options, (
                f'''"splashAuthSettings" cannot be "{kwargs["splashAuthSettings"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "create_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies"

        body_params = [
            "name",
            "scheduling",
            "bandwidth",
            "firewallAndTrafficShaping",
            "contentFiltering",
            "splashAuthSettings",
            "vlanTagging",
            "bonjourForwarding",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_group_policy(
        self, network_id: str, group_policy_id: str
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
        self, network_id: str, group_policy_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a group policy.

                https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

                Args:
                    network_id: Network ID.
                    group_policy_id: Group policy ID.
                    name: The name for your group policy.
                    scheduling:     The schedule for the group policy. Schedules are applied to days of the
                      week. .
                    bandwidth:     The bandwidth settings for clients bound to your group policy.
        .
                    firewallAndTrafficShaping:     The firewall and traffic shaping rules and settings for
                      your policy. .
                    contentFiltering: The content filtering settings for your group policy.
                    splashAuthSettings: Whether clients bound to your policy will bypass splash
                      authorization or behave according to the network's rules. Can be one of
                      'network default' or 'bypass'. Only available if your network has a
                      wireless configuration.
                    vlanTagging: The VLAN tagging settings for your group policy. Only available if your
                      network has a wireless configuration.
                    bonjourForwarding: The Bonjour settings for your group policy. Only valid if your
                      network has a wireless configuration.

        """
        kwargs.update(locals())

        if "splashAuthSettings" in kwargs:
            options = ["bypass", "network default"]
            assert kwargs["splashAuthSettings"] in options, (
                f'''"splashAuthSettings" cannot be "{kwargs["splashAuthSettings"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "update_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_policy_id = urllib.parse.quote(str(group_policy_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        body_params = [
            "name",
            "scheduling",
            "bandwidth",
            "firewallAndTrafficShaping",
            "contentFiltering",
            "splashAuthSettings",
            "vlanTagging",
            "bonjourForwarding",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_group_policy(
        self, network_id: str, group_policy_id: str, **kwargs: Any
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
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "delete_network_group_policy",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        group_policy_id = urllib.parse.quote(str(group_policy_id), safe="")
        resource = f"/networks/{network_id}/groupPolicies/{group_policy_id}"

        return self._session.delete(metadata, resource)

    def get_network_health_alerts(self, network_id: str) -> dict[str, Any] | None:
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

    def get_network_meraki_auth_users(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, email: str, authorizations: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap).

        https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

        Args:
            network_id: Network ID.
            email: Email address of the user.
            authorizations: Authorization zones and expiration dates for the user.
            name: Name of the user. Only required If the user is not a Dashboard administrator.
            password: The password for this user account. Only required If the user is not a
              Dashboard administrator.
            accountType: Authorization type for user. Can be 'Guest' or '802.1X' for wireless
              networks, or 'Client VPN' for MX networks. Defaults to '802.1X'.
            emailPasswordToUser: Whether or not Meraki should email the password to user. Default is
              false.
            isAdmin: Whether or not the user is a Dashboard administrator.

        """
        kwargs.update(locals())

        if "accountType" in kwargs:
            options = ["802.1X", "Client VPN", "Guest"]
            assert kwargs["accountType"] in options, (
                f'''"accountType" cannot be "{kwargs["accountType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "create_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers"

        body_params = [
            "email",
            "name",
            "password",
            "accountType",
            "emailPasswordToUser",
            "isAdmin",
            "authorizations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_meraki_auth_user(
        self, network_id: str, meraki_auth_user_id: str
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

    def delete_network_meraki_auth_user(
        self, network_id: str, meraki_auth_user_id: str, **kwargs: Any
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
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "delete_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        meraki_auth_user_id = urllib.parse.quote(str(meraki_auth_user_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        return self._session.delete(metadata, resource)

    def update_network_meraki_auth_user(
        self, network_id: str, meraki_auth_user_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated).

        https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

        Args:
            network_id: Network ID.
            meraki_auth_user_id: Meraki auth user ID.
            name: Name of the user. Only allowed If the user is not Dashboard administrator.
            password: The password for this user account. Only allowed If the user is not Dashboard
              administrator.
            emailPasswordToUser: Whether or not Meraki should email the password to user. Default is
              false.
            authorizations: Authorization zones and expiration dates for the user.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "update_network_meraki_auth_user",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        meraki_auth_user_id = urllib.parse.quote(str(meraki_auth_user_id), safe="")
        resource = f"/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}"

        body_params = [
            "name",
            "password",
            "emailPasswordToUser",
            "authorizations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_mqtt_brokers(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, name: str, host: str, port: int, **kwargs: Any
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
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "create_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers"

        body_params = [
            "name",
            "host",
            "port",
            "security",
            "authentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_mqtt_broker(
        self, network_id: str, mqtt_broker_id: str
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
        self, network_id: str, mqtt_broker_id: str, **kwargs: Any
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
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "update_network_mqtt_broker",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        mqtt_broker_id = urllib.parse.quote(str(mqtt_broker_id), safe="")
        resource = f"/networks/{network_id}/mqttBrokers/{mqtt_broker_id}"

        body_params = [
            "name",
            "host",
            "port",
            "security",
            "authentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_mqtt_broker(self, network_id: str, mqtt_broker_id: str) -> None:
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

    def get_network_netflow(self, network_id: str) -> dict[str, Any] | None:
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

    def update_network_netflow(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Update the NetFlow traffic reporting settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-netflow

        Args:
            network_id: Network ID.
            reportingEnabled: Boolean indicating whether NetFlow traffic reporting is enabled (true)
              or disabled (false).
            collectorIp: The IPv4 address of the NetFlow collector.
            collectorPort: The port that the NetFlow collector will be listening on.
            etaEnabled: Boolean indicating whether Encrypted Traffic Analytics is enabled (true) or
              disabled (false).
            etaDstPort: The port that the Encrypted Traffic Analytics collector will be listening
              on.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "netflow"],
            "operation": "update_network_netflow",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/netflow"

        body_params = [
            "reportingEnabled",
            "collectorIp",
            "collectorPort",
            "etaEnabled",
            "etaDstPort",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_network_health_channel_utilization(
        self, network_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get the channel utilization over each radio for all APs in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-network-health-channel-utilization

        Args:
            network_id: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 1 day.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              600. The default is 600.
            perPage: The number of entries per page returned. Acceptable range is 3 - 100. Default
              is 10.
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
            "tags": ["networks", "monitor", "networkHealth", "channelUtilization"],
            "operation": "get_network_network_health_channel_utilization",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/networkHealth/channelUtilization"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_pii_pii_keys(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """List the keys required to access Personally Identifiable Information (PII) for a given identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-pii-keys

        Args:
            network_id: Network ID.
            username: The username of a Systems Manager user.
            email: The email of a network user account or a Systems Manager device.
            mac: The MAC of a network client device or a Systems Manager device.
            serial: The serial of a Systems Manager device.
            imei: The IMEI of a Systems Manager device.
            bluetoothMac: The MAC of a Bluetooth client.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "pii", "piiKeys"],
            "operation": "get_network_pii_pii_keys",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/piiKeys"

        query_params = [
            "username",
            "email",
            "mac",
            "serial",
            "imei",
            "bluetoothMac",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_pii_requests(self, network_id: str) -> dict[str, Any] | None:
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

    def create_network_pii_request(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Submit a new delete or restrict processing PII request.

        https://developer.cisco.com/meraki/api-v1/#!create-network-pii-request

        Args:
            network_id: Network ID.
            type: One of "delete" or "restrict processing".
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
            smDeviceId: The sm_device_id of a Systems Manager device. The only way to "restrict
              processing" or "delete" a Systems Manager device. Must include "device" in
              the dataset for a "delete" request to destroy the device.
            smUserId: The sm_user_id of a Systems Manager user. The only way to "restrict
              processing" or "delete" a Systems Manager user. Must include "user" in the
              dataset for a "delete" request to destroy the user.

        """
        kwargs.update(locals())

        if "type" in kwargs:
            options = ["delete", "restrict processing"]
            assert kwargs["type"] in options, (
                f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "pii", "requests"],
            "operation": "create_network_pii_request",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/requests"

        body_params = [
            "type",
            "datasets",
            "username",
            "email",
            "mac",
            "smDeviceId",
            "smUserId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_pii_request(self, network_id: str, request_id: str) -> dict[str, Any] | None:
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

    def delete_network_pii_request(self, network_id: str, request_id: str) -> None:
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
        self, network_id: str, **kwargs: Any
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
            bluetoothMac: The MAC of a Bluetooth client.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "pii", "smDevicesForKey"],
            "operation": "get_network_pii_sm_devices_for_key",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/smDevicesForKey"

        query_params = [
            "username",
            "email",
            "mac",
            "serial",
            "imei",
            "bluetoothMac",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_pii_sm_owners_for_key(
        self, network_id: str, **kwargs: Any
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
            bluetoothMac: The MAC of a Bluetooth client.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "pii", "smOwnersForKey"],
            "operation": "get_network_pii_sm_owners_for_key",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/pii/smOwnersForKey"

        query_params = [
            "username",
            "email",
            "mac",
            "serial",
            "imei",
            "bluetoothMac",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_policies_by_client(
        self, network_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get policies for all clients with policies.

        https://developer.cisco.com/meraki/api-v1/#!get-network-policies-by-client

        Args:
            network_id: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 50.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 31 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "policies", "byClient"],
            "operation": "get_network_policies_by_client",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/policies/byClient"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_settings(self, network_id: str) -> dict[str, Any] | None:
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

    def update_network_settings(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Update the settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        Args:
            network_id: Network ID.
            localStatusPageEnabled: Enables / disables the local device status pages (<a
              target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a
              target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a
              target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a
              target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>).
              Optional (defaults to false).
            remoteStatusPageEnabled: Enables / disables access to the device status page (<a
              target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set
              if localStatusPageEnabled is set to true.
            localStatusPage: A hash of Local Status page(s)' authentication options applied to the
              Network.
            securePort: A hash of SecureConnect options applied to the Network.
            namedVlans: A hash of Named VLANs options applied to the Network.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "settings"],
            "operation": "update_network_settings",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/settings"

        body_params = [
            "localStatusPageEnabled",
            "remoteStatusPageEnabled",
            "localStatusPage",
            "securePort",
            "namedVlans",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_snmp(self, network_id: str) -> dict[str, Any] | None:
        """Return the SNMP settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-snmp

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure", "snmp"], "operation": "get_network_snmp"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/snmp"

        return self._session.get(metadata, resource)

    def update_network_snmp(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Update the SNMP settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-snmp

        Args:
            network_id: Network ID.
            access: The type of SNMP access. Can be one of 'none' (disabled), 'community' (V1/V2c),
              or 'users' (V3).
            communityString: The SNMP community string. Only relevant if 'access' is set to
              'community'.
            users: The list of SNMP users. Only relevant if 'access' is set to 'users'.

        """
        kwargs.update(locals())

        if "access" in kwargs:
            options = ["community", "none", "users"]
            assert kwargs["access"] in options, (
                f'''"access" cannot be "{kwargs["access"]}", & must be set to one of: {options}'''
            )

        metadata = {"tags": ["networks", "configure", "snmp"], "operation": "update_network_snmp"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/snmp"

        body_params = [
            "access",
            "communityString",
            "users",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_splash_login_attempts(
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """List the splash login attempts for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-splash-login-attempts

        Args:
            network_id: Network ID.
            ssidNumber: Only return the login attempts for the specified SSID.
            loginIdentifier: The username, email, or phone number used during login.
            timespan: The timespan, in seconds, for the login attempts. The period will be from
              [timespan] seconds ago until now. The maximum timespan is 3 months.

        """
        kwargs.update(locals())

        if "ssidNumber" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssidNumber"] in options, (
                f'''"ssidNumber" cannot be "{kwargs["ssidNumber"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "monitor", "splashLoginAttempts"],
            "operation": "get_network_splash_login_attempts",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/splashLoginAttempts"

        query_params = [
            "ssidNumber",
            "loginIdentifier",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def split_network(self, network_id: str) -> dict[str, Any] | None:
        """Split a combined network into individual networks for each type of device.

        https://developer.cisco.com/meraki/api-v1/#!split-network

        Args:
            network_id: Network ID.

        """
        metadata = {"tags": ["networks", "configure"], "operation": "split_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/split"

        return self._session.post(metadata, resource)

    def get_network_syslog_servers(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, servers: list
    ) -> dict[str, Any] | None:
        """Update the syslog servers for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-syslog-servers

        Args:
            network_id: Network ID.
            servers: A list of the syslog servers for this network.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "syslogServers"],
            "operation": "update_network_syslog_servers",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/syslogServers"

        body_params = [
            "servers",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_topology_link_layer(self, network_id: str) -> dict[str, Any] | None:
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

    def get_network_traffic(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Return the traffic analysis data for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic

        Args:
            network_id: Network ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 30 days
              from today.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameter t0. The value must be in seconds and be
              less than or equal to 30 days.
            deviceType: Filter the data by device type: 'combined', 'wireless', 'switch' or
              'appliance'. Defaults to 'combined'. When using 'combined', for each rule
              the data will come from the device type with the most usage.

        """
        kwargs.update(locals())

        if "deviceType" in kwargs:
            options = ["appliance", "combined", "switch", "wireless"]
            assert kwargs["deviceType"] in options, (
                f'''"deviceType" cannot be "{kwargs["deviceType"]}", & must be set to one of: {options}'''
            )

        metadata = {"tags": ["networks", "monitor", "traffic"], "operation": "get_network_traffic"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/traffic"

        query_params = [
            "t0",
            "timespan",
            "deviceType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_traffic_analysis(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the traffic analysis settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-traffic-analysis

        Args:
            network_id: Network ID.
            mode:     The traffic analysis mode for the network. Can be one of 'disabled' (do not
              collect traffic types),     'basic' (collect generic traffic categories),
              or 'detailed' (collect destination hostnames). .
            customPieChartItems: The list of items that make up the custom pie chart for traffic
              reporting.

        """
        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["basic", "detailed", "disabled"]
            assert kwargs["mode"] in options, (
                f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["networks", "configure", "trafficAnalysis"],
            "operation": "update_network_traffic_analysis",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/trafficAnalysis"

        body_params = [
            "mode",
            "customPieChartItems",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_traffic_shaping_application_categories(
        self, network_id: str
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
        self, network_id: str
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

    def unbind_network(self, network_id: str, **kwargs: Any) -> dict[str, Any] | None:
        """Unbind a network from a template.

        https://developer.cisco.com/meraki/api-v1/#!unbind-network

        Args:
            network_id: Network ID.
            retainConfigs: Optional boolean to retain all the current configs given by the template.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "unbind_network"}
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/unbind"

        body_params = [
            "retainConfigs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profiles(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, name: str, vlanNames: list, vlanGroups: list, iname: str
    ) -> dict[str, Any] | None:
        """Create a VLAN profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-vlan-profile

        Args:
            network_id: Network ID.
            name: Name of the profile, string length must be from 1 to 255 characters.
            vlanNames: An array of named VLANs.
            vlanGroups: An array of VLAN groups.
            iname: IName of the profile.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "create_network_vlan_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/vlanProfiles"

        body_params = [
            "name",
            "vlanNames",
            "vlanGroups",
            "iname",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profiles_assignments_by_device(
        self, network_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Get the assigned VLAN Profiles for devices in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profiles-assignments-by-device

        Args:
            network_id: Network ID.
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
            serials: Optional parameter to filter devices by serials. All devices returned belong to
              serial numbers that are an exact match.
            productTypes: Optional parameter to filter devices by product types.
            stackIds: Optional parameter to filter devices by Switch Stack ids.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles", "assignments", "byDevice"],
            "operation": "get_network_vlan_profiles_assignments_by_device",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/assignments/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "serials",
            "productTypes",
            "stackIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "productTypes",
            "stackIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def reassign_network_vlan_profiles_assignments(
        self, network_id: str, serials: list, stackIds: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update the assigned VLAN Profile for devices in a network.

        https://developer.cisco.com/meraki/api-v1/#!reassign-network-vlan-profiles-assignments

        Args:
            network_id: Network ID.
            serials: Array of Device Serials.
            stackIds: Array of Switch Stack IDs.
            vlanProfile: The VLAN Profile.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles", "assignments"],
            "operation": "reassign_network_vlan_profiles_assignments",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/assignments/reassign"

        body_params = [
            "vlanProfile",
            "serials",
            "stackIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profile(self, network_id: str, iname: str) -> dict[str, Any] | None:
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
        self, network_id: str, iname: str, name: str, vlanNames: list, vlanGroups: list
    ) -> dict[str, Any] | None:
        """Update an existing VLAN profile of a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-vlan-profile

        Args:
            network_id: Network ID.
            iname: Iname.
            name: Name of the profile, string length must be from 1 to 255 characters.
            vlanNames: An array of named VLANs.
            vlanGroups: An array of VLAN groups.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "update_network_vlan_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/networks/{network_id}/vlanProfiles/{iname}"

        body_params = [
            "name",
            "vlanNames",
            "vlanGroups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_vlan_profile(self, network_id: str, iname: str) -> None:
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

    def get_network_webhooks_http_servers(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, name: str, url: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Add an HTTP server to a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-http-server

        Args:
            network_id: Network ID.
            name: A name for easy reference to the HTTP server.
            url: The URL of the HTTP server. Once set, cannot be updated.
            sharedSecret: A shared secret that will be included in POSTs sent to the HTTP server.
              This secret can be used to verify that the request was sent by Meraki.
            payloadTemplate: The payload template to use when posting data to the HTTP server.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "create_network_webhooks_http_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/httpServers"

        body_params = [
            "name",
            "url",
            "sharedSecret",
            "payloadTemplate",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_http_server(
        self, network_id: str, http_server_id: str
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
        self, network_id: str, http_server_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update an HTTP server.

        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-http-server

        Args:
            network_id: Network ID.
            http_server_id: Http server ID.
            name: A name for easy reference to the HTTP server.
            sharedSecret: A shared secret that will be included in POSTs sent to the HTTP server.
              This secret can be used to verify that the request was sent by Meraki.
            payloadTemplate: The payload template to use when posting data to the HTTP server.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "update_network_webhooks_http_server",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        http_server_id = urllib.parse.quote(str(http_server_id), safe="")
        resource = f"/networks/{network_id}/webhooks/httpServers/{http_server_id}"

        body_params = [
            "name",
            "sharedSecret",
            "payloadTemplate",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_webhooks_http_server(self, network_id: str, http_server_id: str) -> None:
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

    def get_network_webhooks_payload_templates(self, network_id: str) -> dict[str, Any] | None:
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
        self, network_id: str, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            name: The name of the new template.
            body: The liquid template used for the body of the webhook message. Either `body` or
              `bodyFile` must be specified.
            headers: The liquid template used with the webhook headers.
            bodyFile: A Base64 encoded file containing liquid template used for the body of the
              webhook message. Either `body` or `bodyFile` must be specified.
            headersFile: A Base64 encoded file containing the liquid template used with the webhook
              headers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "create_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates"

        body_params = [
            "name",
            "body",
            "headers",
            "bodyFile",
            "headersFile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_payload_template(
        self, network_id: str, payload_template_id: str
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

    def delete_network_webhooks_payload_template(
        self, network_id: str, payload_template_id: str
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

    def update_network_webhooks_payload_template(
        self, network_id: str, payload_template_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-payload-template

        Args:
            network_id: Network ID.
            payload_template_id: Payload template ID.
            name: The name of the template.
            body: The liquid template used for the body of the webhook message.
            headers: The liquid template used with the webhook headers.
            bodyFile: A file containing liquid template used for the body of the webhook message.
            headersFile: A file containing the liquid template used with the webhook headers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "update_network_webhooks_payload_template",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        payload_template_id = urllib.parse.quote(str(payload_template_id), safe="")
        resource = f"/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}"

        body_params = [
            "name",
            "body",
            "headers",
            "bodyFile",
            "headersFile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def create_network_webhooks_webhook_test(
        self, network_id: str, url: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Send a test webhook for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-webhook-test

        Args:
            network_id: Network ID.
            url: The URL where the test webhook will be sent.
            sharedSecret: The shared secret the test webhook will send. Optional. Defaults to HTTP
              server's shared secret. Otherwise, defaults to an empty string.
            payloadTemplateId: The ID of the payload template of the test webhook. Defaults to the
              HTTP server's template ID if one exists for the given URL, or Generic
              template ID otherwise.
            payloadTemplateName: The name of the payload template.
            alertTypeId: The type of alert which the test webhook will send. Optional. Defaults to
              power_supply_down.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "webhookTests"],
            "operation": "create_network_webhooks_webhook_test",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/webhooks/webhookTests"

        body_params = [
            "url",
            "sharedSecret",
            "payloadTemplateId",
            "payloadTemplateName",
            "alertTypeId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_webhook_test(
        self, network_id: str, webhook_test_id: str
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
