"""WirelessController API endpoints."""

import urllib

from meraki_dashboard_sdk.rest_session import RestSession


class WirelessController:
    """WirelessController class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
        self._session = session

    def get_organization_wireless_controller_availabilities_change_history(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List connectivity data of wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-availabilities-change-history

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wirelessController", "monitor", "availabilities", "changeHistory"],
            "operation": "get_organization_wireless_controller_availabilities_change_history",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/wirelessController/availabilities/changeHistory"
        )

        query_params = [
            "serials",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_clients_overview_history_by_device_by_interval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List wireless client counts of wireless LAN controllers over time in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-clients-overview-history-by-device-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter wireless LAN controllers by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "clients",
                "overview",
                "history",
                "byDevice",
                "byInterval",
            ],
            "operation": "get_organization_wireless_controller_clients_overview_history_by_device_by_interval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/clients/overview/history/byDevice/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "resolution",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_controller_connections(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List all access points associated with wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-connections

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter access points by network ID. This filter uses multiple exact matches.
        - controllerSerials (array): Optional parameter to filter access points by its controller cloud ID. This filter uses multiple exact matches.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wirelessController", "monitor", "connections"],
            "operation": "get_organization_wireless_controller_connections",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/connections"

        query_params = [
            "networkIds",
            "controllerSerials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "controllerSerials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_controller_devices_interfaces_l2_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List wireless LAN controller layer 2 interfaces in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-2-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wirelessController", "monitor", "devices", "interfaces", "l2", "byDevice"],
            "operation": "get_organization_wireless_controller_devices_interfaces_l2_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/wirelessController/devices/interfaces/l2/byDevice"
        )

        query_params = [
            "serials",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_devices_interfaces_l2_statuses_change_history_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List wireless LAN controller layer 2 interfaces history status in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-2-statuses-change-history-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - includeInterfacesWithoutChanges (boolean): By default, interfaces without changes are omitted from the response for brevity. If you want to include the interfaces even if they have no changes, set to true. (default: false)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "devices",
                "interfaces",
                "l2",
                "statuses",
                "changeHistory",
                "byDevice",
            ],
            "operation": "get_organization_wireless_controller_devices_interfaces_l2_statuses_change_history_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/interfaces/l2/statuses/changeHistory/byDevice"

        query_params = [
            "serials",
            "includeInterfacesWithoutChanges",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_devices_interfaces_l2_usage_history_by_interval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List wireless LAN controller layer 2 interfaces history usage in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-2-usage-history-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "devices",
                "interfaces",
                "l2",
                "usage",
                "history",
                "byInterval",
            ],
            "operation": "get_organization_wireless_controller_devices_interfaces_l2_usage_history_by_interval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/interfaces/l2/usage/history/byInterval"

        query_params = [
            "serials",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_devices_interfaces_l3_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List wireless LAN controller layer 3 interfaces in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-3-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wirelessController", "monitor", "devices", "interfaces", "l3", "byDevice"],
            "operation": "get_organization_wireless_controller_devices_interfaces_l3_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = (
            f"/organizations/{organizationId}/wirelessController/devices/interfaces/l3/byDevice"
        )

        query_params = [
            "serials",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_devices_interfaces_l3_statuses_change_history_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List wireless LAN controller layer 3 interfaces history status in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-3-statuses-change-history-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - includeInterfacesWithoutChanges (boolean): By default, interfaces without changes are omitted from the response for brevity. If you want to include the interfaces even if they have no changes, set to true. (default: false)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "devices",
                "interfaces",
                "l3",
                "statuses",
                "changeHistory",
                "byDevice",
            ],
            "operation": "get_organization_wireless_controller_devices_interfaces_l3_statuses_change_history_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/interfaces/l3/statuses/changeHistory/byDevice"

        query_params = [
            "serials",
            "includeInterfacesWithoutChanges",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_devices_interfaces_l3_usage_history_by_interval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List wireless LAN controller layer 3 interfaces history usage in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-3-usage-history-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "devices",
                "interfaces",
                "l3",
                "usage",
                "history",
                "byInterval",
            ],
            "operation": "get_organization_wireless_controller_devices_interfaces_l3_usage_history_by_interval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/interfaces/l3/usage/history/byInterval"

        query_params = [
            "serials",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_devices_interfaces_packets_overview_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """Retrieve the packet counters for the interfaces of a Wireless LAN controller.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-packets-overview-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - names (array): Optional parameter to filter wireless LAN controller by its interface name. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 day after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 1 day. The default is 1 hour.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "devices",
                "interfaces",
                "packets",
                "overview",
                "byDevice",
            ],
            "operation": "get_organization_wireless_controller_devices_interfaces_packets_overview_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/interfaces/packets/overview/byDevice"

        query_params = [
            "serials",
            "names",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "names",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_controller_devices_interfaces_usage_history_by_interval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """Retrieve the traffic for the interfaces of a Wireless LAN controller.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-usage-history-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - names (array): Optional parameter to filter wireless LAN controller by its interface name. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "devices",
                "interfaces",
                "usage",
                "history",
                "byInterval",
            ],
            "operation": "get_organization_wireless_controller_devices_interfaces_usage_history_by_interval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/interfaces/usage/history/byInterval"

        query_params = [
            "serials",
            "names",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "names",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_wireless_controller_devices_redundancy_failover_history(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List the failover events of wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-redundancy-failover-history

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "devices",
                "redundancy",
                "failover",
                "history",
            ],
            "operation": "get_organization_wireless_controller_devices_redundancy_failover_history",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/redundancy/failover/history"

        query_params = [
            "serials",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_devices_redundancy_statuses(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List redundancy details of wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-redundancy-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud IDs. This filter uses multiple exact matches.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wirelessController", "monitor", "devices", "redundancy", "statuses"],
            "operation": "get_organization_wireless_controller_devices_redundancy_statuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/redundancy/statuses"

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

    def get_organization_wireless_controller_devices_system_utilization_history_by_interval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List cpu utilization data of wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-system-utilization-history-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "wirelessController",
                "monitor",
                "devices",
                "system",
                "utilization",
                "history",
                "byInterval",
            ],
            "operation": "get_organization_wireless_controller_devices_system_utilization_history_by_interval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/devices/system/utilization/history/byInterval"

        query_params = [
            "serials",
            "t0",
            "t1",
            "timespan",
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

    def get_organization_wireless_controller_overview_by_device(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """List the overview information of wireless LAN controllers in an organization and it is updated every minute.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-overview-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter wireless LAN controllers by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter wireless LAN controller by its cloud ID. This filter uses multiple exact matches.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["wirelessController", "monitor", "overview", "byDevice"],
            "operation": "get_organization_wireless_controller_overview_by_device",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wirelessController/overview/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
