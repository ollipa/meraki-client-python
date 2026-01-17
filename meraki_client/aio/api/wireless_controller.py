"""WirelessController API endpoints."""

from __future__ import annotations

import urllib.parse
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from meraki_client.aio.session import AsyncPaginatedResponse, Session


class WirelessController:
    """WirelessController class."""

    def __init__(self, session: Session) -> None:
        self._session = session

    async def get_organization_wireless_controller_availabilities_change_history(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List connectivity data of wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-availabilities-change-history

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/availabilities/changeHistory"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerAvailabilitiesChangeHistory",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_clients_overview_history_by_device_by_interval(
        self,
        *,
        organization_id: str,
        network_ids: list | None = None,
        serials: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        resolution: int | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List wireless client counts of wireless LAN controllers over time in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-clients-overview-history-by-device-by-interval

        Args:
            organization_id: Organization ID.
            network_ids: Optional parameter to filter wireless LAN controllers by network ID. This
              filter uses multiple exact matches.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              300, 600, 1200, 3600, 14400, 86400. The default is 86400.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/clients/overview/history/byDevice/byInterval"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
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
        if resolution is not None:
            params["resolution"] = resolution

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerClientsOverviewHistoryByDeviceByInterval",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_connections(
        self,
        *,
        organization_id: str,
        network_ids: list | None = None,
        controller_serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List all access points associated with wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-connections

        Args:
            organization_id: Organization ID.
            network_ids: Optional parameter to filter access points by network ID. This filter uses
              multiple exact matches.
            controller_serials: Optional parameter to filter access points by its controller cloud
              ID. This filter uses multiple exact matches.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/connections"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if controller_serials is not None:
            params["controllerSerials[]"] = controller_serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerConnections",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_interfaces_l2_by_device(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List wireless LAN controller layer 2 interfaces in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-2-by-device

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/interfaces/l2/byDevice"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesInterfacesL2ByDevice",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_interfaces_l2_statuses_change_history_by_device(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        include_interfaces_without_changes: bool | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List wireless LAN controller layer 2 interfaces history status in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-2-statuses-change-history-by-device

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            include_interfaces_without_changes: By default, interfaces without changes are omitted
              from the response for brevity. If you want to include the interfaces even
              if they have no changes, set to true. (default: false).
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/interfaces/l2/statuses/changeHistory/byDevice"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
        if include_interfaces_without_changes is not None:
            params["includeInterfacesWithoutChanges"] = include_interfaces_without_changes
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesInterfacesL2StatusesChangeHistoryByDevice",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_interfaces_l2_usage_history_by_interval(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List wireless LAN controller layer 2 interfaces history usage in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-2-usage-history-by-interval

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/interfaces/l2/usage/history/byInterval"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesInterfacesL2UsageHistoryByInterval",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_interfaces_l3_by_device(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List wireless LAN controller layer 3 interfaces in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-3-by-device

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/interfaces/l3/byDevice"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesInterfacesL3ByDevice",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_interfaces_l3_statuses_change_history_by_device(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        include_interfaces_without_changes: bool | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List wireless LAN controller layer 3 interfaces history status in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-3-statuses-change-history-by-device

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            include_interfaces_without_changes: By default, interfaces without changes are omitted
              from the response for brevity. If you want to include the interfaces even
              if they have no changes, set to true. (default: false).
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/interfaces/l3/statuses/changeHistory/byDevice"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
        if include_interfaces_without_changes is not None:
            params["includeInterfacesWithoutChanges"] = include_interfaces_without_changes
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesInterfacesL3StatusesChangeHistoryByDevice",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_interfaces_l3_usage_history_by_interval(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List wireless LAN controller layer 3 interfaces history usage in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-l-3-usage-history-by-interval

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/interfaces/l3/usage/history/byInterval"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesInterfacesL3UsageHistoryByInterval",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_interfaces_packets_overview_by_device(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        names: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Retrieve the packet counters for the interfaces of a Wireless LAN controller.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-packets-overview-by-device

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            names: Optional parameter to filter wireless LAN controller by its interface name. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 1 day
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 1 day after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 1 day. The default is 1 hour.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/interfaces/packets/overview/byDevice"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
        if names is not None:
            params["names[]"] = names
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesInterfacesPacketsOverviewByDevice",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_interfaces_usage_history_by_interval(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        names: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Retrieve the traffic for the interfaces of a Wireless LAN controller.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-interfaces-usage-history-by-interval

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            names: Optional parameter to filter wireless LAN controller by its interface name. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/interfaces/usage/history/byInterval"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
        if names is not None:
            params["names[]"] = names
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesInterfacesUsageHistoryByInterval",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_redundancy_failover_history(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List the failover events of wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-redundancy-failover-history

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/redundancy/failover/history"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesRedundancyFailoverHistory",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_redundancy_statuses(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List redundancy details of wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-redundancy-statuses

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud IDs. This
              filter uses multiple exact matches.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/redundancy/statuses"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesRedundancyStatuses",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_devices_system_utilization_history_by_interval(
        self,
        *,
        organization_id: str,
        serials: list | None = None,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List cpu utilization data of wireless LAN controllers in an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-devices-system-utilization-history-by-interval

        Args:
            organization_id: Organization ID.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
            t0: The beginning of the timespan for the data. The maximum lookback period is 31 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 31 days. The default is 7 days.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/devices/system/utilization/history/byInterval"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
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

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerDevicesSystemUtilizationHistoryByInterval",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_wireless_controller_overview_by_device(
        self,
        *,
        organization_id: str,
        network_ids: list | None = None,
        serials: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List the overview information of wireless LAN controllers in an organization and it is updated every minute.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-controller-overview-by-device

        Args:
            organization_id: Organization ID.
            network_ids: Optional parameter to filter wireless LAN controllers by network ID. This
              filter uses multiple exact matches.
            serials: Optional parameter to filter wireless LAN controller by its cloud ID. This
              filter uses multiple exact matches.
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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/wirelessController/overview/byDevice"

        params = {}
        if network_ids is not None:
            params["networkIds[]"] = network_ids
        if serials is not None:
            params["serials[]"] = serials
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="wirelessController",
            operation_id="getOrganizationWirelessControllerOverviewByDevice",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )
