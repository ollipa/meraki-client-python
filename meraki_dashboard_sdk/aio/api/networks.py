"""Networks API endpoints."""

import urllib

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncNetworks:
    """Networks class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_network(self, networkId: str):
        """Return a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network

        - networkId (string): Network ID

        """
        metadata = {"tags": ["networks", "configure"], "operation": "get_network"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}"

        return self._session.get(metadata, resource)

    def update_network(self, networkId: str, **kwargs):
        """Update a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network

        - networkId (string): Network ID
        - name (string): The name of the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - tags (array): A list of tags to be applied to the network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break.
        - notes (string): Add any notes or additional information about this network here.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "update_network"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}"

        body_params = [
            "name",
            "timeZone",
            "tags",
            "enrollmentString",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network(self, networkId: str):
        """Delete a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network

        - networkId (string): Network ID

        """
        metadata = {"tags": ["networks", "configure"], "operation": "delete_network"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}"

        return self._session.delete(metadata, resource)

    def get_network_alerts_history(self, networkId: str, total_pages=1, direction="next", **kwargs):
        """Return the alert history for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-history

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "alerts", "history"],
            "operation": "get_network_alerts_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/alerts/history"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_alerts_settings(self, networkId: str):
        """Return the alert configuration for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-settings

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "alerts", "settings"],
            "operation": "get_network_alerts_settings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/alerts/settings"

        return self._session.get(metadata, resource)

    def update_network_alerts_settings(self, networkId: str, **kwargs):
        """Update the alert configuration for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-alerts-settings

        - networkId (string): Network ID
        - defaultDestinations (object): The network-wide destinations for all alerts on the network.
        - alerts (array): Alert-specific configuration for each type. Only alerts that pertain to the network can be updated.
        - muting (object): Mute alerts under certain conditions

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "alerts", "settings"],
            "operation": "update_network_alerts_settings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/alerts/settings"

        body_params = [
            "defaultDestinations",
            "alerts",
            "muting",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def bind_network(self, networkId: str, configTemplateId: str, **kwargs):
        """Bind a network to a template.

        https://developer.cisco.com/meraki/api-v1/#!bind-network

        - networkId (string): Network ID
        - configTemplateId (string): The ID of the template to which the network should be bound.
        - autoBind (boolean): Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model. Defaults to false if left unspecified. This option only affects switch networks and switch templates. Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "bind_network"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/bind"

        body_params = [
            "configTemplateId",
            "autoBind",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_bluetooth_clients(
        self, networkId: str, total_pages=1, direction="next", **kwargs
    ):
        """List the Bluetooth clients seen by APs in this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-clients

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - includeConnectivityHistory (boolean): Include the connectivity history for this client

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "bluetoothClients"],
            "operation": "get_network_bluetooth_clients",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/bluetoothClients"

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

    def get_network_bluetooth_client(self, networkId: str, bluetoothClientId: str, **kwargs):
        """Return a Bluetooth client.

        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-client

        - networkId (string): Network ID
        - bluetoothClientId (string): Bluetooth client ID
        - includeConnectivityHistory (boolean): Include the connectivity history for this client
        - connectivityHistoryTimespan (integer): The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "bluetoothClients"],
            "operation": "get_network_bluetooth_client",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        bluetoothClientId = urllib.parse.quote(str(bluetoothClientId), safe="")
        resource = f"/networks/{networkId}/bluetoothClients/{bluetoothClientId}"

        query_params = [
            "includeConnectivityHistory",
            "connectivityHistoryTimespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_clients(self, networkId: str, total_pages=1, direction="next", **kwargs):
        """List the clients that have used this network in the timespan.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - statuses (array): Filters clients based on status. Can be one of 'Online' or 'Offline'.
        - ip (string): Filters clients based on a partial or full match for the ip address field.
        - ip6 (string): Filters clients based on a partial or full match for the ip6 address field.
        - ip6Local (string): Filters clients based on a partial or full match for the ip6Local address field.
        - mac (string): Filters clients based on a partial or full match for the mac address field.
        - os (string): Filters clients based on a partial or full match for the os (operating system) field.
        - pskGroup (string): Filters clients based on partial or full match for the iPSK name field.
        - description (string): Filters clients based on a partial or full match for the description field.
        - vlan (string): Filters clients based on the full match for the VLAN field.
        - namedVlan (string): Filters clients based on the partial or full match for the named VLAN field.
        - recentDeviceConnections (array): Filters clients based on recent connection type. Can be one of 'Wired' or 'Wireless'.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "monitor", "clients"], "operation": "get_network_clients"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients"

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
        self, networkId: str, clients: str, total_pages=1, direction="next", **kwargs
    ):
        """Return the application usage data for clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-application-usage

        - networkId (string): Network ID
        - clients (string): A list of client keys, MACs or IPs separated by comma.
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - ssidNumber (integer): An SSID number to include. If not specified, events for all SSIDs will be returned.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients/applicationUsage"

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
        self, networkId: str, total_pages=1, direction="next", **kwargs
    ):
        """Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-bandwidth-usage-history

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "clients", "bandwidthUsageHistory"],
            "operation": "get_network_clients_bandwidth_usage_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients/bandwidthUsageHistory"

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

    def get_network_clients_overview(self, networkId: str, **kwargs):
        """Return overview statistics for network clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-overview

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "clients", "overview"],
            "operation": "get_network_clients_overview",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients/overview"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def provision_network_clients(self, networkId: str, clients: list, devicePolicy: str, **kwargs):
        """Provisions a client with a name and policy.

        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        - networkId (string): Network ID
        - clients (array): The array of clients to provision
        - devicePolicy (string): The policy to apply to the specified client. Can be 'Group policy', 'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
        - groupPolicyId (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
        - policiesBySecurityAppliance (object): An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)
        - policiesBySsid (object): An object, describing the policy-connection associations for each active SSID within the network. Keys should be the number of enabled SSIDs, mapping to an object describing the client's policy

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients/provision"

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
        self, networkId: str, clients: str, total_pages=1, direction="next", **kwargs
    ):
        """Return the usage histories for clients.

        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-usage-histories

        - networkId (string): Network ID
        - clients (string): A list of client keys, MACs or IPs separated by comma.
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - ssidNumber (integer): An SSID number to include. If not specified, events for all SSIDs will be returned.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients/usageHistories"

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

    def get_network_client(self, networkId: str, clientId: str):
        """Return the client associated with the given identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client

        - networkId (string): Network ID
        - clientId (string): Client ID

        """
        metadata = {"tags": ["networks", "monitor", "clients"], "operation": "get_network_client"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/clients/{clientId}"

        return self._session.get(metadata, resource)

    def get_network_client_policy(self, networkId: str, clientId: str):
        """Return the policy assigned to a client on the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-policy

        - networkId (string): Network ID
        - clientId (string): Client ID

        """
        metadata = {
            "tags": ["networks", "configure", "clients", "policy"],
            "operation": "get_network_client_policy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/clients/{clientId}/policy"

        return self._session.get(metadata, resource)

    def update_network_client_policy(
        self, networkId: str, clientId: str, devicePolicy: str, **kwargs
    ):
        """Update the policy assigned to a client on the network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-client-policy

        - networkId (string): Network ID
        - clientId (string): Client ID
        - devicePolicy (string): The policy to assign. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'. Required.
        - groupPolicyId (string): [Optional] If 'devicePolicy' is set to 'Group policy' this param is used to specify the group policy ID.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "clients", "policy"],
            "operation": "update_network_client_policy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/clients/{clientId}/policy"

        body_params = [
            "devicePolicy",
            "groupPolicyId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_client_splash_authorization_status(self, networkId: str, clientId: str):
        """Return the splash authorization for a client, for each SSID they've associated with through splash.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-splash-authorization-status

        - networkId (string): Network ID
        - clientId (string): Client ID

        """
        metadata = {
            "tags": ["networks", "configure", "clients", "splashAuthorizationStatus"],
            "operation": "get_network_client_splash_authorization_status",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus"

        return self._session.get(metadata, resource)

    def update_network_client_splash_authorization_status(
        self, networkId: str, clientId: str, ssids: dict
    ):
        """Update a client's splash authorization.

        https://developer.cisco.com/meraki/api-v1/#!update-network-client-splash-authorization-status

        - networkId (string): Network ID
        - clientId (string): Client ID
        - ssids (object): The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "clients", "splashAuthorizationStatus"],
            "operation": "update_network_client_splash_authorization_status",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus"

        body_params = [
            "ssids",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_client_traffic_history(
        self, networkId: str, clientId: str, total_pages=1, direction="next", **kwargs
    ):
        """Return the client's network traffic data over time.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-traffic-history

        - networkId (string): Network ID
        - clientId (string): Client ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "clients", "trafficHistory"],
            "operation": "get_network_client_traffic_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/clients/{clientId}/trafficHistory"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_client_usage_history(self, networkId: str, clientId: str):
        """Return the client's daily usage history.

        https://developer.cisco.com/meraki/api-v1/#!get-network-client-usage-history

        - networkId (string): Network ID
        - clientId (string): Client ID

        """
        metadata = {
            "tags": ["networks", "monitor", "clients", "usageHistory"],
            "operation": "get_network_client_usage_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/clients/{clientId}/usageHistory"

        return self._session.get(metadata, resource)

    def get_network_devices(self, networkId: str):
        """List the devices in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-devices

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "get_network_devices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/devices"

        return self._session.get(metadata, resource)

    def claim_network_devices(self, networkId: str, serials: list, **kwargs):
        """Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed).

        https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

        - networkId (string): Network ID
        - serials (array): A list of serials of devices to claim
        - addAtomically (boolean): Whether to claim devices atomically. If true, all devices will be claimed or none will be claimed. Default is true.
        - detailsByDevice (array): Optional details for claimed devices (currently only used for Catalyst devices)

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "claim_network_devices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/devices/claim"

        body_params = [
            "serials",
            "detailsByDevice",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def vmx_network_devices_claim(self, networkId: str, size: str):
        """Claim a vMX into a network.

        https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim

        - networkId (string): Network ID
        - size (string): The size of the vMX you claim. It can be one of: small, medium, large, xlarge, 100

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/devices/claim/vmx"

        body_params = [
            "size",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def remove_network_devices(self, networkId: str, serial: str):
        """Remove a single device.

        https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

        - networkId (string): Network ID
        - serial (string): The serial of a device

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "devices"],
            "operation": "remove_network_devices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/devices/remove"

        body_params = [
            "serial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_events(
        self, networkId: str, total_pages=1, direction="prev", event_log_end_time=None, **kwargs
    ):
        """List the events for the network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-events

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" or "prev" (default) page
        - event_log_end_time (string): ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, to retrieve events within a time window
        - productType (string): The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, wirelessController, campusGateway, and secureConnect
        - includedEventTypes (array): A list of event types. The returned events will be filtered to only include events with these types.
        - excludedEventTypes (array): A list of event types. The returned events will be filtered to exclude events with these types.
        - deviceMac (string): The MAC address of the Meraki device which the list of events will be filtered with
        - deviceSerial (string): The serial of the Meraki device which the list of events will be filtered with
        - deviceName (string): The name of the Meraki device which the list of events will be filtered with
        - clientIp (string): The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks.
        - clientMac (string): The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks.
        - clientName (string): The name, or partial name, of the client which the list of events will be filtered with
        - smDeviceMac (string): The MAC address of the Systems Manager device which the list of events will be filtered with
        - smDeviceName (string): The name of the Systems Manager device which the list of events will be filtered with
        - eventDetails (string): The details of the event(Catalyst device only) which the list of events will be filtered with
        - eventSeverity (string): The severity of the event(Catalyst device only) which the list of events will be filtered with
        - isCatalyst (boolean): Boolean indicating that whether it is a Catalyst device. For Catalyst device, eventDetails and eventSeverity can be used to filter events.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/events"

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

    def get_network_events_event_types(self, networkId: str):
        """List the event type to human-readable description.

        https://developer.cisco.com/meraki/api-v1/#!get-network-events-event-types

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "monitor", "events", "eventTypes"],
            "operation": "get_network_events_event_types",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/events/eventTypes"

        return self._session.get(metadata, resource)

    def get_network_firmware_upgrades(self, networkId: str):
        """Get firmware upgrade information for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades"],
            "operation": "get_network_firmware_upgrades",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades"

        return self._session.get(metadata, resource)

    def update_network_firmware_upgrades(self, networkId: str, **kwargs):
        """Update firmware upgrade information for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

        - networkId (string): Network ID
        - upgradeWindow (object): Upgrade window for devices in network
        - timezone (string): The timezone for the network
        - products (object): Contains information about the network to update

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades"],
            "operation": "update_network_firmware_upgrades",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades"

        body_params = [
            "upgradeWindow",
            "timezone",
            "products",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def create_network_firmware_upgrades_rollback(self, networkId: str, reasons: list, **kwargs):
        """Rollback a Firmware Upgrade For A Network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

        - networkId (string): Network ID
        - reasons (array): Reasons for the rollback
        - product (string): Product type to rollback (if the network is a combined network)
        - time (string): Scheduled time for the rollback
        - toVersion (object): Version to downgrade to (if the network has firmware flexibility)

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/rollbacks"

        body_params = [
            "product",
            "time",
            "reasons",
            "toVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_events(self, networkId: str):
        """Get the Staged Upgrade Event from a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-events

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "get_network_firmware_upgrades_staged_events",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/events"

        return self._session.get(metadata, resource)

    def create_network_firmware_upgrades_staged_event(self, networkId: str, stages: list, **kwargs):
        """Create a Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-event

        - networkId (string): Network ID
        - stages (array): All firmware upgrade stages in the network with their start time.
        - products (object): Contains firmware upgrade version information

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "create_network_firmware_upgrades_staged_event",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/events"

        body_params = [
            "products",
            "stages",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_network_firmware_upgrades_staged_events(self, networkId: str, stages: list):
        """Update the Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-events

        - networkId (string): Network ID
        - stages (array): All firmware upgrade stages in the network with their start time.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "update_network_firmware_upgrades_staged_events",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/events"

        body_params = [
            "stages",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def defer_network_firmware_upgrades_staged_events(self, networkId: str):
        """Postpone by 1 week all pending staged upgrade stages for a network.

        https://developer.cisco.com/meraki/api-v1/#!defer-network-firmware-upgrades-staged-events

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "defer_network_firmware_upgrades_staged_events",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/events/defer"

        return self._session.post(metadata, resource)

    def rollbacks_network_firmware_upgrades_staged_events(
        self, networkId: str, stages: list, **kwargs
    ):
        """Rollback a Staged Upgrade Event for a network.

        https://developer.cisco.com/meraki/api-v1/#!rollbacks-network-firmware-upgrades-staged-events

        - networkId (string): Network ID
        - stages (array): All completed or in-progress stages in the network with their new start times. All pending stages will be canceled
        - reasons (array): The reason for rolling back the staged upgrade

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "events"],
            "operation": "rollbacks_network_firmware_upgrades_staged_events",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/events/rollbacks"

        body_params = [
            "stages",
            "reasons",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_groups(self, networkId: str):
        """List of Staged Upgrade Groups in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-groups

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "get_network_firmware_upgrades_staged_groups",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/groups"

        return self._session.get(metadata, resource)

    def create_network_firmware_upgrades_staged_group(
        self, networkId: str, name: str, isDefault: bool, **kwargs
    ):
        """Create a Staged Upgrade Group for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group

        - networkId (string): Network ID
        - name (string): Name of the Staged Upgrade Group. Length must be 1 to 255 characters
        - isDefault (boolean): Boolean indicating the default Group. Any device that does not have a group explicitly assigned will upgrade with this group
        - description (string): Description of the Staged Upgrade Group. Length must be 1 to 255 characters
        - assignedDevices (object): The devices and Switch Stacks assigned to the Group

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "create_network_firmware_upgrades_staged_group",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/groups"

        body_params = [
            "name",
            "description",
            "isDefault",
            "assignedDevices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_firmware_upgrades_staged_group(self, networkId: str, groupId: str):
        """Get a Staged Upgrade Group from a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-group

        - networkId (string): Network ID
        - groupId (string): Group ID

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "get_network_firmware_upgrades_staged_group",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}"

        return self._session.get(metadata, resource)

    def update_network_firmware_upgrades_staged_group(
        self, networkId: str, groupId: str, name: str, isDefault: bool, **kwargs
    ):
        """Update a Staged Upgrade Group for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-group

        - networkId (string): Network ID
        - groupId (string): Group ID
        - name (string): Name of the Staged Upgrade Group. Length must be 1 to 255 characters
        - isDefault (boolean): Boolean indicating the default Group. Any device that does not have a group explicitly assigned will upgrade with this group
        - description (string): Description of the Staged Upgrade Group. Length must be 1 to 255 characters
        - assignedDevices (object): The devices and Switch Stacks assigned to the Group

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "update_network_firmware_upgrades_staged_group",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}"

        body_params = [
            "name",
            "description",
            "isDefault",
            "assignedDevices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_firmware_upgrades_staged_group(self, networkId: str, groupId: str):
        """Delete a Staged Upgrade Group.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-firmware-upgrades-staged-group

        - networkId (string): Network ID
        - groupId (string): Group ID

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "groups"],
            "operation": "delete_network_firmware_upgrades_staged_group",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}"

        return self._session.delete(metadata, resource)

    def get_network_firmware_upgrades_staged_stages(self, networkId: str):
        """Order of Staged Upgrade Groups in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-stages

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "stages"],
            "operation": "get_network_firmware_upgrades_staged_stages",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/stages"

        return self._session.get(metadata, resource)

    def update_network_firmware_upgrades_staged_stages(self, networkId: str, **kwargs):
        """Assign Staged Upgrade Group order in the sequence.

        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-stages

        - networkId (string): Network ID
        - _json (array): Array of Staged Upgrade Groups

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "firmwareUpgrades", "staged", "stages"],
            "operation": "update_network_firmware_upgrades_staged_stages",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/firmwareUpgrades/staged/stages"

        body_params = [
            "_json",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_floor_plans(self, networkId: str):
        """List the floor plans that belong to your network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plans

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "get_network_floor_plans",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/floorPlans"

        return self._session.get(metadata, resource)

    def create_network_floor_plan(self, networkId: str, name: str, imageContents: str, **kwargs):
        """Upload a floor plan.

        https://developer.cisco.com/meraki/api-v1/#!create-network-floor-plan

        - networkId (string): Network ID
        - name (string): The name of your floor plan.
        - imageContents (string): The file contents (a base 64 encoded string) of your image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in.
        - center (object): The longitude and latitude of the center of your floor plan. The 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
        - bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
        - bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
        - topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
        - topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
        - floorNumber (number): The floor number of the floors within the building

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "create_network_floor_plan",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/floorPlans"

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

    def batch_network_floor_plans_auto_locate_jobs(self, networkId: str, jobs: list):
        """Schedule auto locate jobs for one or more floor plans in a network.

        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-auto-locate-jobs

        - networkId (string): Network ID
        - jobs (array): The list of auto locate jobs to be scheduled. Up to 100 jobs can be provided in a request.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "batch_network_floor_plans_auto_locate_jobs",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/floorPlans/autoLocate/jobs/batch"

        body_params = [
            "jobs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def cancel_network_floor_plans_auto_locate_job(self, networkId: str, jobId: str):
        """Cancel a scheduled or running auto locate job.

        https://developer.cisco.com/meraki/api-v1/#!cancel-network-floor-plans-auto-locate-job

        - networkId (string): Network ID
        - jobId (string): Job ID

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "cancel_network_floor_plans_auto_locate_job",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        jobId = urllib.parse.quote(str(jobId), safe="")
        resource = f"/networks/{networkId}/floorPlans/autoLocate/jobs/{jobId}/cancel"

        return self._session.post(metadata, resource)

    def publish_network_floor_plans_auto_locate_job(self, networkId: str, jobId: str, **kwargs):
        """Update the status of a finished auto locate job to be published, and update device locations.

        https://developer.cisco.com/meraki/api-v1/#!publish-network-floor-plans-auto-locate-job

        - networkId (string): Network ID
        - jobId (string): Job ID
        - devices (array): The list of devices to publish positions for

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "publish_network_floor_plans_auto_locate_job",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        jobId = urllib.parse.quote(str(jobId), safe="")
        resource = f"/networks/{networkId}/floorPlans/autoLocate/jobs/{jobId}/publish"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def recalculate_network_floor_plans_auto_locate_job(self, networkId: str, jobId: str, **kwargs):
        """Trigger auto locate recalculation for a job, and optionally set anchors.

        https://developer.cisco.com/meraki/api-v1/#!recalculate-network-floor-plans-auto-locate-job

        - networkId (string): Network ID
        - jobId (string): Job ID
        - devices (array): The list of devices to update anchor positions for

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "autoLocate", "jobs"],
            "operation": "recalculate_network_floor_plans_auto_locate_job",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        jobId = urllib.parse.quote(str(jobId), safe="")
        resource = f"/networks/{networkId}/floorPlans/autoLocate/jobs/{jobId}/recalculate"

        body_params = [
            "devices",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def batch_network_floor_plans_devices_update(self, networkId: str, assignments: list):
        """Update floorplan assignments for a batch of devices.

        https://developer.cisco.com/meraki/api-v1/#!batch-network-floor-plans-devices-update

        - networkId (string): Network ID
        - assignments (array): List of floorplan assignments to update. Up to 100 floor plan assignments can be provided in a request.

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "floorPlans", "devices"],
            "operation": "batch_network_floor_plans_devices_update",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/floorPlans/devices/batchUpdate"

        body_params = [
            "assignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_floor_plan(self, networkId: str, floorPlanId: str):
        """Find a floor plan by ID.

        https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plan

        - networkId (string): Network ID
        - floorPlanId (string): Floor plan ID

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "get_network_floor_plan",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        floorPlanId = urllib.parse.quote(str(floorPlanId), safe="")
        resource = f"/networks/{networkId}/floorPlans/{floorPlanId}"

        return self._session.get(metadata, resource)

    def update_network_floor_plan(self, networkId: str, floorPlanId: str, **kwargs):
        """Update a floor plan's geolocation and other meta data.

        https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

        - networkId (string): Network ID
        - floorPlanId (string): Floor plan ID
        - name (string): The name of your floor plan.
        - center (object): The longitude and latitude of the center of your floor plan. If you want to change the geolocation data of your floor plan, either the 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
        - bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
        - bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
        - topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
        - topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
        - floorNumber (number): The floor number of the floors within the building
        - imageContents (string): The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields ('center, 'topLeftCorner', etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "update_network_floor_plan",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        floorPlanId = urllib.parse.quote(str(floorPlanId), safe="")
        resource = f"/networks/{networkId}/floorPlans/{floorPlanId}"

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

    def delete_network_floor_plan(self, networkId: str, floorPlanId: str):
        """Destroy a floor plan.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

        - networkId (string): Network ID
        - floorPlanId (string): Floor plan ID

        """
        metadata = {
            "tags": ["networks", "configure", "floorPlans"],
            "operation": "delete_network_floor_plan",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        floorPlanId = urllib.parse.quote(str(floorPlanId), safe="")
        resource = f"/networks/{networkId}/floorPlans/{floorPlanId}"

        return self._session.delete(metadata, resource)

    def get_network_group_policies(self, networkId: str):
        """List the group policies in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-group-policies

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "get_network_group_policies",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/groupPolicies"

        return self._session.get(metadata, resource)

    def create_network_group_policy(self, networkId: str, name: str, **kwargs):
        """Create a group policy.

        https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

        - networkId (string): Network ID
        - name (string): The name for your group policy. Required.
        - scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

        - bandwidth (object):     The bandwidth settings for clients bound to your group policy.

        - firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

        - contentFiltering (object): The content filtering settings for your group policy
        - splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
        - vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
        - bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/groupPolicies"

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

    def get_network_group_policy(self, networkId: str, groupPolicyId: str):
        """Display a group policy.

        https://developer.cisco.com/meraki/api-v1/#!get-network-group-policy

        - networkId (string): Network ID
        - groupPolicyId (string): Group policy ID

        """
        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "get_network_group_policy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        groupPolicyId = urllib.parse.quote(str(groupPolicyId), safe="")
        resource = f"/networks/{networkId}/groupPolicies/{groupPolicyId}"

        return self._session.get(metadata, resource)

    def update_network_group_policy(self, networkId: str, groupPolicyId: str, **kwargs):
        """Update a group policy.

        https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

        - networkId (string): Network ID
        - groupPolicyId (string): Group policy ID
        - name (string): The name for your group policy.
        - scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

        - bandwidth (object):     The bandwidth settings for clients bound to your group policy.

        - firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

        - contentFiltering (object): The content filtering settings for your group policy
        - splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
        - vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
        - bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        groupPolicyId = urllib.parse.quote(str(groupPolicyId), safe="")
        resource = f"/networks/{networkId}/groupPolicies/{groupPolicyId}"

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

    def delete_network_group_policy(self, networkId: str, groupPolicyId: str, **kwargs):
        """Delete a group policy.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

        - networkId (string): Network ID
        - groupPolicyId (string): Group policy ID
        - force (boolean): If true, the system deletes the GP even if there are active clients using the GP. After deletion, active clients that were assigned to that Group Policy will be left without any policy applied. Default is false.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "groupPolicies"],
            "operation": "delete_network_group_policy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        groupPolicyId = urllib.parse.quote(str(groupPolicyId), safe="")
        resource = f"/networks/{networkId}/groupPolicies/{groupPolicyId}"

        return self._session.delete(metadata, resource)

    def get_network_health_alerts(self, networkId: str):
        """Return all global alerts on this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-health-alerts

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "health", "alerts"],
            "operation": "get_network_health_alerts",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/health/alerts"

        return self._session.get(metadata, resource)

    def get_network_meraki_auth_users(self, networkId: str):
        """List the authorized users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a MX network).

        https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-users

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "get_network_meraki_auth_users",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/merakiAuthUsers"

        return self._session.get(metadata, resource)

    def create_network_meraki_auth_user(
        self, networkId: str, email: str, authorizations: list, **kwargs
    ):
        """Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap).

        https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

        - networkId (string): Network ID
        - email (string): Email address of the user
        - authorizations (array): Authorization zones and expiration dates for the user.
        - name (string): Name of the user. Only required If the user is not a Dashboard administrator.
        - password (string): The password for this user account. Only required If the user is not a Dashboard administrator.
        - accountType (string): Authorization type for user. Can be 'Guest' or '802.1X' for wireless networks, or 'Client VPN' for MX networks. Defaults to '802.1X'.
        - emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
        - isAdmin (boolean): Whether or not the user is a Dashboard administrator.

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/merakiAuthUsers"

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

    def get_network_meraki_auth_user(self, networkId: str, merakiAuthUserId: str):
        """Return the Meraki Auth splash guest, RADIUS, or client VPN user.

        https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-user

        - networkId (string): Network ID
        - merakiAuthUserId (string): Meraki auth user ID

        """
        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "get_network_meraki_auth_user",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        merakiAuthUserId = urllib.parse.quote(str(merakiAuthUserId), safe="")
        resource = f"/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}"

        return self._session.get(metadata, resource)

    def delete_network_meraki_auth_user(self, networkId: str, merakiAuthUserId: str, **kwargs):
        """Delete an 802.1X RADIUS user, or deauthorize and optionally delete a splash guest or client VPN user.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

        - networkId (string): Network ID
        - merakiAuthUserId (string): Meraki auth user ID
        - delete (boolean): If the ID supplied is for a splash guest or client VPN user, and that user is not authorized for any other networks in the organization, then also delete the user. 802.1X RADIUS users are always deleted regardless of this optional attribute.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "delete_network_meraki_auth_user",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        merakiAuthUserId = urllib.parse.quote(str(merakiAuthUserId), safe="")
        resource = f"/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}"

        return self._session.delete(metadata, resource)

    def update_network_meraki_auth_user(self, networkId: str, merakiAuthUserId: str, **kwargs):
        """Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated).

        https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

        - networkId (string): Network ID
        - merakiAuthUserId (string): Meraki auth user ID
        - name (string): Name of the user. Only allowed If the user is not Dashboard administrator.
        - password (string): The password for this user account. Only allowed If the user is not Dashboard administrator.
        - emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
        - authorizations (array): Authorization zones and expiration dates for the user.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "merakiAuthUsers"],
            "operation": "update_network_meraki_auth_user",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        merakiAuthUserId = urllib.parse.quote(str(merakiAuthUserId), safe="")
        resource = f"/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}"

        body_params = [
            "name",
            "password",
            "emailPasswordToUser",
            "authorizations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_mqtt_brokers(self, networkId: str):
        """List the MQTT brokers for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-brokers

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "get_network_mqtt_brokers",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/mqttBrokers"

        return self._session.get(metadata, resource)

    def create_network_mqtt_broker(self, networkId: str, name: str, host: str, port: int, **kwargs):
        """Add an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

        - networkId (string): Network ID
        - name (string): Name of the MQTT broker.
        - host (string): Host name/IP address where the MQTT broker runs.
        - port (integer): Host port though which the MQTT broker can be reached.
        - security (object): Security settings of the MQTT broker.
        - authentication (object): Authentication settings of the MQTT broker

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "create_network_mqtt_broker",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/mqttBrokers"

        body_params = [
            "name",
            "host",
            "port",
            "security",
            "authentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_mqtt_broker(self, networkId: str, mqttBrokerId: str):
        """Return an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-broker

        - networkId (string): Network ID
        - mqttBrokerId (string): Mqtt broker ID

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "get_network_mqtt_broker",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        mqttBrokerId = urllib.parse.quote(str(mqttBrokerId), safe="")
        resource = f"/networks/{networkId}/mqttBrokers/{mqttBrokerId}"

        return self._session.get(metadata, resource)

    def update_network_mqtt_broker(self, networkId: str, mqttBrokerId: str, **kwargs):
        """Update an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

        - networkId (string): Network ID
        - mqttBrokerId (string): Mqtt broker ID
        - name (string): Name of the MQTT broker.
        - host (string): Host name/IP address where the MQTT broker runs.
        - port (integer): Host port though which the MQTT broker can be reached.
        - security (object): Security settings of the MQTT broker.
        - authentication (object): Authentication settings of the MQTT broker

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "update_network_mqtt_broker",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        mqttBrokerId = urllib.parse.quote(str(mqttBrokerId), safe="")
        resource = f"/networks/{networkId}/mqttBrokers/{mqttBrokerId}"

        body_params = [
            "name",
            "host",
            "port",
            "security",
            "authentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_mqtt_broker(self, networkId: str, mqttBrokerId: str):
        """Delete an MQTT broker.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

        - networkId (string): Network ID
        - mqttBrokerId (string): Mqtt broker ID

        """
        metadata = {
            "tags": ["networks", "configure", "mqttBrokers"],
            "operation": "delete_network_mqtt_broker",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        mqttBrokerId = urllib.parse.quote(str(mqttBrokerId), safe="")
        resource = f"/networks/{networkId}/mqttBrokers/{mqttBrokerId}"

        return self._session.delete(metadata, resource)

    def get_network_netflow(self, networkId: str):
        """Return the NetFlow traffic reporting settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-netflow

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "netflow"],
            "operation": "get_network_netflow",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/netflow"

        return self._session.get(metadata, resource)

    def update_network_netflow(self, networkId: str, **kwargs):
        """Update the NetFlow traffic reporting settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-netflow

        - networkId (string): Network ID
        - reportingEnabled (boolean): Boolean indicating whether NetFlow traffic reporting is enabled (true) or disabled (false).
        - collectorIp (string): The IPv4 address of the NetFlow collector.
        - collectorPort (integer): The port that the NetFlow collector will be listening on.
        - etaEnabled (boolean): Boolean indicating whether Encrypted Traffic Analytics is enabled (true) or disabled (false).
        - etaDstPort (integer): The port that the Encrypted Traffic Analytics collector will be listening on.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "netflow"],
            "operation": "update_network_netflow",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/netflow"

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
        self, networkId: str, total_pages=1, direction="next", **kwargs
    ):
        """Get the channel utilization over each radio for all APs in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-network-health-channel-utilization

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "monitor", "networkHealth", "channelUtilization"],
            "operation": "get_network_network_health_channel_utilization",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/networkHealth/channelUtilization"

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

    def get_network_pii_pii_keys(self, networkId: str, **kwargs):
        """List the keys required to access Personally Identifiable Information (PII) for a given identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-pii-keys

        - networkId (string): Network ID
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "pii", "piiKeys"],
            "operation": "get_network_pii_pii_keys",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/pii/piiKeys"

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

    def get_network_pii_requests(self, networkId: str):
        """List the PII requests for this network or organization.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-requests

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "requests"],
            "operation": "get_network_pii_requests",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/pii/requests"

        return self._session.get(metadata, resource)

    def create_network_pii_request(self, networkId: str, **kwargs):
        """Submit a new delete or restrict processing PII request.

        https://developer.cisco.com/meraki/api-v1/#!create-network-pii-request

        - networkId (string): Network ID
        - type (string): One of "delete" or "restrict processing"
        - datasets (array): The datasets related to the provided key that should be deleted. Only applies to "delete" requests. The value "all" will be expanded to all datasets applicable to this type. The datasets by applicable to each type are: mac (usage, events, traffic), email (users, loginAttempts), username (users, loginAttempts), bluetoothMac (client, connectivity), smDeviceId (device), smUserId (user)
        - username (string): The username of a network log in. Only applies to "delete" requests.
        - email (string): The email of a network user account. Only applies to "delete" requests.
        - mac (string): The MAC of a network client device. Applies to both "restrict processing" and "delete" requests.
        - smDeviceId (string): The sm_device_id of a Systems Manager device. The only way to "restrict processing" or "delete" a Systems Manager device. Must include "device" in the dataset for a "delete" request to destroy the device.
        - smUserId (string): The sm_user_id of a Systems Manager user. The only way to "restrict processing" or "delete" a Systems Manager user. Must include "user" in the dataset for a "delete" request to destroy the user.

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/pii/requests"

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

    def get_network_pii_request(self, networkId: str, requestId: str):
        """Return a PII request.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-request

        - networkId (string): Network ID
        - requestId (string): Request ID

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "requests"],
            "operation": "get_network_pii_request",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        requestId = urllib.parse.quote(str(requestId), safe="")
        resource = f"/networks/{networkId}/pii/requests/{requestId}"

        return self._session.get(metadata, resource)

    def delete_network_pii_request(self, networkId: str, requestId: str):
        """Delete a restrict processing PII request.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-pii-request

        - networkId (string): Network ID
        - requestId (string): Request ID

        """
        metadata = {
            "tags": ["networks", "configure", "pii", "requests"],
            "operation": "delete_network_pii_request",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        requestId = urllib.parse.quote(str(requestId), safe="")
        resource = f"/networks/{networkId}/pii/requests/{requestId}"

        return self._session.delete(metadata, resource)

    def get_network_pii_sm_devices_for_key(self, networkId: str, **kwargs):
        """Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-devices-for-key

        - networkId (string): Network ID
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "pii", "smDevicesForKey"],
            "operation": "get_network_pii_sm_devices_for_key",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/pii/smDevicesForKey"

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

    def get_network_pii_sm_owners_for_key(self, networkId: str, **kwargs):
        """Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier.

        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-owners-for-key

        - networkId (string): Network ID
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "pii", "smOwnersForKey"],
            "operation": "get_network_pii_sm_owners_for_key",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/pii/smOwnersForKey"

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
        self, networkId: str, total_pages=1, direction="next", **kwargs
    ):
        """Get policies for all clients with policies.

        https://developer.cisco.com/meraki/api-v1/#!get-network-policies-by-client

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "policies", "byClient"],
            "operation": "get_network_policies_by_client",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/policies/byClient"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_settings(self, networkId: str):
        """Return the settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-settings

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "settings"],
            "operation": "get_network_settings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/settings"

        return self._session.get(metadata, resource)

    def update_network_settings(self, networkId: str, **kwargs):
        """Update the settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        - networkId (string): Network ID
        - localStatusPageEnabled (boolean): Enables / disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
        - remoteStatusPageEnabled (boolean): Enables / disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if localStatusPageEnabled is set to true
        - localStatusPage (object): A hash of Local Status page(s)' authentication options applied to the Network.
        - securePort (object): A hash of SecureConnect options applied to the Network.
        - namedVlans (object): A hash of Named VLANs options applied to the Network.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "settings"],
            "operation": "update_network_settings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/settings"

        body_params = [
            "localStatusPageEnabled",
            "remoteStatusPageEnabled",
            "localStatusPage",
            "securePort",
            "namedVlans",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_snmp(self, networkId: str):
        """Return the SNMP settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-snmp

        - networkId (string): Network ID

        """
        metadata = {"tags": ["networks", "configure", "snmp"], "operation": "get_network_snmp"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/snmp"

        return self._session.get(metadata, resource)

    def update_network_snmp(self, networkId: str, **kwargs):
        """Update the SNMP settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-snmp

        - networkId (string): Network ID
        - access (string): The type of SNMP access. Can be one of 'none' (disabled), 'community' (V1/V2c), or 'users' (V3).
        - communityString (string): The SNMP community string. Only relevant if 'access' is set to 'community'.
        - users (array): The list of SNMP users. Only relevant if 'access' is set to 'users'.

        """
        kwargs.update(locals())

        if "access" in kwargs:
            options = ["community", "none", "users"]
            assert kwargs["access"] in options, (
                f'''"access" cannot be "{kwargs["access"]}", & must be set to one of: {options}'''
            )

        metadata = {"tags": ["networks", "configure", "snmp"], "operation": "update_network_snmp"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/snmp"

        body_params = [
            "access",
            "communityString",
            "users",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_splash_login_attempts(self, networkId: str, **kwargs):
        """List the splash login attempts for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-splash-login-attempts

        - networkId (string): Network ID
        - ssidNumber (integer): Only return the login attempts for the specified SSID
        - loginIdentifier (string): The username, email, or phone number used during login
        - timespan (integer): The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/splashLoginAttempts"

        query_params = [
            "ssidNumber",
            "loginIdentifier",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def split_network(self, networkId: str):
        """Split a combined network into individual networks for each type of device.

        https://developer.cisco.com/meraki/api-v1/#!split-network

        - networkId (string): Network ID

        """
        metadata = {"tags": ["networks", "configure"], "operation": "split_network"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/split"

        return self._session.post(metadata, resource)

    def get_network_syslog_servers(self, networkId: str):
        """List the syslog servers for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-syslog-servers

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "syslogServers"],
            "operation": "get_network_syslog_servers",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/syslogServers"

        return self._session.get(metadata, resource)

    def update_network_syslog_servers(self, networkId: str, servers: list):
        """Update the syslog servers for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-syslog-servers

        - networkId (string): Network ID
        - servers (array): A list of the syslog servers for this network

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "syslogServers"],
            "operation": "update_network_syslog_servers",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/syslogServers"

        body_params = [
            "servers",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_topology_link_layer(self, networkId: str):
        """List the LLDP and CDP information for all discovered devices and connections in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-topology-link-layer

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "monitor", "topology", "linkLayer"],
            "operation": "get_network_topology_link_layer",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/topology/linkLayer"

        return self._session.get(metadata, resource)

    def get_network_traffic(self, networkId: str, **kwargs):
        """Return the traffic analysis data for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
        - deviceType (string): Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'. When using 'combined', for each rule the data will come from the device type with the most usage.

        """
        kwargs.update(locals())

        if "deviceType" in kwargs:
            options = ["appliance", "combined", "switch", "wireless"]
            assert kwargs["deviceType"] in options, (
                f'''"deviceType" cannot be "{kwargs["deviceType"]}", & must be set to one of: {options}'''
            )

        metadata = {"tags": ["networks", "monitor", "traffic"], "operation": "get_network_traffic"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/traffic"

        query_params = [
            "t0",
            "timespan",
            "deviceType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def get_network_traffic_analysis(self, networkId: str):
        """Return the traffic analysis settings for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-analysis

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "trafficAnalysis"],
            "operation": "get_network_traffic_analysis",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/trafficAnalysis"

        return self._session.get(metadata, resource)

    def update_network_traffic_analysis(self, networkId: str, **kwargs):
        """Update the traffic analysis settings for a network.

            https://developer.cisco.com/meraki/api-v1/#!update-network-traffic-analysis

            - networkId (string): Network ID
            - mode (string):     The traffic analysis mode for the network. Can be one of 'disabled' (do not collect traffic types),
        'basic' (collect generic traffic categories), or 'detailed' (collect destination hostnames).

            - customPieChartItems (array): The list of items that make up the custom pie chart for traffic reporting.

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
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/trafficAnalysis"

        body_params = [
            "mode",
            "customPieChartItems",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_network_traffic_shaping_application_categories(self, networkId: str):
        """Returns the application categories for traffic shaping rules.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-application-categories

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "trafficShaping", "applicationCategories"],
            "operation": "get_network_traffic_shaping_application_categories",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/trafficShaping/applicationCategories"

        return self._session.get(metadata, resource)

    def get_network_traffic_shaping_dscp_tagging_options(self, networkId: str):
        """Returns the available DSCP tagging options for your traffic shaping rules.

        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-dscp-tagging-options

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "trafficShaping", "dscpTaggingOptions"],
            "operation": "get_network_traffic_shaping_dscp_tagging_options",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/trafficShaping/dscpTaggingOptions"

        return self._session.get(metadata, resource)

    def unbind_network(self, networkId: str, **kwargs):
        """Unbind a network from a template.

        https://developer.cisco.com/meraki/api-v1/#!unbind-network

        - networkId (string): Network ID
        - retainConfigs (boolean): Optional boolean to retain all the current configs given by the template.

        """
        kwargs.update(locals())

        metadata = {"tags": ["networks", "configure"], "operation": "unbind_network"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/unbind"

        body_params = [
            "retainConfigs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profiles(self, networkId: str):
        """List VLAN profiles for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profiles

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "get_network_vlan_profiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/vlanProfiles"

        return self._session.get(metadata, resource)

    def create_network_vlan_profile(
        self, networkId: str, name: str, vlanNames: list, vlanGroups: list, iname: str
    ):
        """Create a VLAN profile for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-vlan-profile

        - networkId (string): Network ID
        - name (string): Name of the profile, string length must be from 1 to 255 characters
        - vlanNames (array): An array of named VLANs
        - vlanGroups (array): An array of VLAN groups
        - iname (string): IName of the profile

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "create_network_vlan_profile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/vlanProfiles"

        body_params = [
            "name",
            "vlanNames",
            "vlanGroups",
            "iname",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profiles_assignments_by_device(
        self, networkId: str, total_pages=1, direction="next", **kwargs
    ):
        """Get the assigned VLAN Profiles for devices in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profiles-assignments-by-device

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - serials (array): Optional parameter to filter devices by serials. All devices returned belong to serial numbers that are an exact match.
        - productTypes (array): Optional parameter to filter devices by product types.
        - stackIds (array): Optional parameter to filter devices by Switch Stack ids.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles", "assignments", "byDevice"],
            "operation": "get_network_vlan_profiles_assignments_by_device",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/vlanProfiles/assignments/byDevice"

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
        self, networkId: str, serials: list, stackIds: list, **kwargs
    ):
        """Update the assigned VLAN Profile for devices in a network.

        https://developer.cisco.com/meraki/api-v1/#!reassign-network-vlan-profiles-assignments

        - networkId (string): Network ID
        - serials (array): Array of Device Serials
        - stackIds (array): Array of Switch Stack IDs
        - vlanProfile (object): The VLAN Profile

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles", "assignments"],
            "operation": "reassign_network_vlan_profiles_assignments",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/vlanProfiles/assignments/reassign"

        body_params = [
            "vlanProfile",
            "serials",
            "stackIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_vlan_profile(self, networkId: str, iname: str):
        """Get an existing VLAN profile of a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profile

        - networkId (string): Network ID
        - iname (string): Iname

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "get_network_vlan_profile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/networks/{networkId}/vlanProfiles/{iname}"

        return self._session.get(metadata, resource)

    def update_network_vlan_profile(
        self, networkId: str, iname: str, name: str, vlanNames: list, vlanGroups: list
    ):
        """Update an existing VLAN profile of a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-vlan-profile

        - networkId (string): Network ID
        - iname (string): Iname
        - name (string): Name of the profile, string length must be from 1 to 255 characters
        - vlanNames (array): An array of named VLANs
        - vlanGroups (array): An array of VLAN groups

        """
        kwargs = locals()

        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "update_network_vlan_profile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/networks/{networkId}/vlanProfiles/{iname}"

        body_params = [
            "name",
            "vlanNames",
            "vlanGroups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_vlan_profile(self, networkId: str, iname: str):
        """Delete a VLAN profile of a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-vlan-profile

        - networkId (string): Network ID
        - iname (string): Iname

        """
        metadata = {
            "tags": ["networks", "configure", "vlanProfiles"],
            "operation": "delete_network_vlan_profile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/networks/{networkId}/vlanProfiles/{iname}"

        return self._session.delete(metadata, resource)

    def get_network_webhooks_http_servers(self, networkId: str):
        """List the HTTP servers for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-servers

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "get_network_webhooks_http_servers",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/webhooks/httpServers"

        return self._session.get(metadata, resource)

    def create_network_webhooks_http_server(self, networkId: str, name: str, url: str, **kwargs):
        """Add an HTTP server to a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-http-server

        - networkId (string): Network ID
        - name (string): A name for easy reference to the HTTP server
        - url (string): The URL of the HTTP server. Once set, cannot be updated.
        - sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        - payloadTemplate (object): The payload template to use when posting data to the HTTP server.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "create_network_webhooks_http_server",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/webhooks/httpServers"

        body_params = [
            "name",
            "url",
            "sharedSecret",
            "payloadTemplate",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_http_server(self, networkId: str, httpServerId: str):
        """Return an HTTP server for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-server

        - networkId (string): Network ID
        - httpServerId (string): Http server ID

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "get_network_webhooks_http_server",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        httpServerId = urllib.parse.quote(str(httpServerId), safe="")
        resource = f"/networks/{networkId}/webhooks/httpServers/{httpServerId}"

        return self._session.get(metadata, resource)

    def update_network_webhooks_http_server(self, networkId: str, httpServerId: str, **kwargs):
        """Update an HTTP server.

        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-http-server

        - networkId (string): Network ID
        - httpServerId (string): Http server ID
        - name (string): A name for easy reference to the HTTP server
        - sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        - payloadTemplate (object): The payload template to use when posting data to the HTTP server.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "update_network_webhooks_http_server",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        httpServerId = urllib.parse.quote(str(httpServerId), safe="")
        resource = f"/networks/{networkId}/webhooks/httpServers/{httpServerId}"

        body_params = [
            "name",
            "sharedSecret",
            "payloadTemplate",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_webhooks_http_server(self, networkId: str, httpServerId: str):
        """Delete an HTTP server from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-http-server

        - networkId (string): Network ID
        - httpServerId (string): Http server ID

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "httpServers"],
            "operation": "delete_network_webhooks_http_server",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        httpServerId = urllib.parse.quote(str(httpServerId), safe="")
        resource = f"/networks/{networkId}/webhooks/httpServers/{httpServerId}"

        return self._session.delete(metadata, resource)

    def get_network_webhooks_payload_templates(self, networkId: str):
        """List the webhook payload templates for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-templates

        - networkId (string): Network ID

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "get_network_webhooks_payload_templates",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/webhooks/payloadTemplates"

        return self._session.get(metadata, resource)

    def create_network_webhooks_payload_template(self, networkId: str, name: str, **kwargs):
        """Create a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-payload-template

        - networkId (string): Network ID
        - name (string): The name of the new template
        - body (string): The liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
        - headers (array): The liquid template used with the webhook headers.
        - bodyFile (string): A Base64 encoded file containing liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
        - headersFile (string): A Base64 encoded file containing the liquid template used with the webhook headers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "create_network_webhooks_payload_template",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/webhooks/payloadTemplates"

        body_params = [
            "name",
            "body",
            "headers",
            "bodyFile",
            "headersFile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_payload_template(self, networkId: str, payloadTemplateId: str):
        """Get the webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-template

        - networkId (string): Network ID
        - payloadTemplateId (string): Payload template ID

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "get_network_webhooks_payload_template",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        payloadTemplateId = urllib.parse.quote(str(payloadTemplateId), safe="")
        resource = f"/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}"

        return self._session.get(metadata, resource)

    def delete_network_webhooks_payload_template(self, networkId: str, payloadTemplateId: str):
        """Destroy a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-payload-template

        - networkId (string): Network ID
        - payloadTemplateId (string): Payload template ID

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "delete_network_webhooks_payload_template",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        payloadTemplateId = urllib.parse.quote(str(payloadTemplateId), safe="")
        resource = f"/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}"

        return self._session.delete(metadata, resource)

    def update_network_webhooks_payload_template(
        self, networkId: str, payloadTemplateId: str, **kwargs
    ):
        """Update a webhook payload template for a network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-payload-template

        - networkId (string): Network ID
        - payloadTemplateId (string): Payload template ID
        - name (string): The name of the template
        - body (string): The liquid template used for the body of the webhook message.
        - headers (array): The liquid template used with the webhook headers.
        - bodyFile (string): A file containing liquid template used for the body of the webhook message.
        - headersFile (string): A file containing the liquid template used with the webhook headers.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "payloadTemplates"],
            "operation": "update_network_webhooks_payload_template",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        payloadTemplateId = urllib.parse.quote(str(payloadTemplateId), safe="")
        resource = f"/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}"

        body_params = [
            "name",
            "body",
            "headers",
            "bodyFile",
            "headersFile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def create_network_webhooks_webhook_test(self, networkId: str, url: str, **kwargs):
        """Send a test webhook for a network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-webhook-test

        - networkId (string): Network ID
        - url (string): The URL where the test webhook will be sent
        - sharedSecret (string): The shared secret the test webhook will send. Optional. Defaults to HTTP server's shared secret. Otherwise, defaults to an empty string.
        - payloadTemplateId (string): The ID of the payload template of the test webhook. Defaults to the HTTP server's template ID if one exists for the given URL, or Generic template ID otherwise
        - payloadTemplateName (string): The name of the payload template.
        - alertTypeId (string): The type of alert which the test webhook will send. Optional. Defaults to power_supply_down.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "webhooks", "webhookTests"],
            "operation": "create_network_webhooks_webhook_test",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/webhooks/webhookTests"

        body_params = [
            "url",
            "sharedSecret",
            "payloadTemplateId",
            "payloadTemplateName",
            "alertTypeId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_webhooks_webhook_test(self, networkId: str, webhookTestId: str):
        """Return the status of a webhook test for a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-webhook-test

        - networkId (string): Network ID
        - webhookTestId (string): Webhook test ID

        """
        metadata = {
            "tags": ["networks", "configure", "webhooks", "webhookTests"],
            "operation": "get_network_webhooks_webhook_test",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        webhookTestId = urllib.parse.quote(str(webhookTestId), safe="")
        resource = f"/networks/{networkId}/webhooks/webhookTests/{webhookTestId}"

        return self._session.get(metadata, resource)
