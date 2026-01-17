"""Sm API endpoints."""

from __future__ import annotations

import urllib.parse
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from meraki_dashboard_sdk.aio.session import AsyncPaginatedResponse, Session


class Sm:
    """Sm class."""

    def __init__(self, session: Session) -> None:
        self._session = session

    async def create_network_sm_bypass_activation_lock_attempt(
        self, *, network_id: str, ids: list
    ) -> dict[str, Any] | None:
        """Bypass activation lock attempt.

        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-bypass-activation-lock-attempt

        Args:
            network_id: Network ID.
            ids: The ids of the devices to attempt activation lock bypass.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/bypassActivationLockAttempts"

        payload = {}
        if ids is not None:
            payload["ids"] = ids

        return await self._session.post(
            scope="sm",
            operation_id="createNetworkSmBypassActivationLockAttempt",
            path=path,
            json=payload,
        )

    async def get_network_sm_bypass_activation_lock_attempt(
        self, *, network_id: str, attempt_id: str
    ) -> dict[str, Any] | None:
        """Bypass activation lock attempt status.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-bypass-activation-lock-attempt

        Args:
            network_id: Network ID.
            attempt_id: Attempt ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        attempt_id = urllib.parse.quote(str(attempt_id), safe="")
        path = f"/networks/{network_id}/sm/bypassActivationLockAttempts/{attempt_id}"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmBypassActivationLockAttempt", path=path
        )

    async def get_network_sm_devices(
        self,
        *,
        network_id: str,
        fields: list | None = None,
        wifi_macs: list | None = None,
        serials: list | None = None,
        ids: list | None = None,
        uuids: list | None = None,
        system_types: list | None = None,
        scope: list | None = None,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List the devices enrolled in an SM network with various specified fields and filters.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-devices

        Args:
            network_id: Network ID.
            fields: Additional fields that will be displayed for each device. The default fields
              are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and
              serialNumber. The additional fields are: ip, systemType,
              availableDeviceCapacity, kioskAppName, biosVersion, lastConnected,
              missingAppsCount, userSuppliedAddress, location, lastUser, ownerEmail,
              ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson,
              deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
              simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt,
              batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
              isRooted, loginRequired, screenLockEnabled, screenLockDelay,
              autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent,
              diskEncryptionEnabled, hardwareEncryptionCaps, passCodeLock,
              usesHardwareKeystore, androidSecurityPatchVersion, cellular, and url.
            wifi_macs: Filter devices by wifi mac(s).
            serials: Filter devices by serial(s).
            ids: Filter devices by id(s).
            uuids: Filter devices by uuid(s).
            system_types: Filter devices by system type(s).
            scope: Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll)
              and a set of tags.
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices"

        params = {}
        if fields is not None:
            params["fields[]"] = fields
        if wifi_macs is not None:
            params["wifiMacs[]"] = wifi_macs
        if serials is not None:
            params["serials[]"] = serials
        if ids is not None:
            params["ids[]"] = ids
        if uuids is not None:
            params["uuids[]"] = uuids
        if system_types is not None:
            params["systemTypes[]"] = system_types
        if scope is not None:
            params["scope[]"] = scope
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="sm",
            operation_id="getNetworkSmDevices",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def checkin_network_sm_devices(
        self,
        *,
        network_id: str,
        wifi_macs: list | None = None,
        ids: list | None = None,
        serials: list | None = None,
        scope: list | None = None,
    ) -> dict[str, Any] | None:
        """Force check-in a set of devices.

        https://developer.cisco.com/meraki/api-v1/#!checkin-network-sm-devices

        Args:
            network_id: Network ID.
            wifi_macs: The wifiMacs of the devices to be checked-in.
            ids: The ids of the devices to be checked-in.
            serials: The serials of the devices to be checked-in.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the devices to be checked-in.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices/checkin"

        payload = {}
        if wifi_macs is not None:
            payload["wifiMacs"] = wifi_macs
        if ids is not None:
            payload["ids"] = ids
        if serials is not None:
            payload["serials"] = serials
        if scope is not None:
            payload["scope"] = scope

        return await self._session.post(
            scope="sm", operation_id="checkinNetworkSmDevices", path=path, json=payload
        )

    async def update_network_sm_devices_fields(
        self,
        *,
        network_id: str,
        device_fields: dict,
        wifi_mac: str | None = None,
        id_: str | None = None,
        serial: str | None = None,
    ) -> dict[str, Any] | None:
        """Modify the fields of a device.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-devices-fields

        Args:
            network_id: Network ID.
            wifi_mac: The wifiMac of the device to be modified.
            id_: The id of the device to be modified.
            serial: The serial of the device to be modified.
            device_fields: The new fields of the device. Each field of this object is optional.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices/fields"

        payload = {}
        if wifi_mac is not None:
            payload["wifiMac"] = wifi_mac
        if id_ is not None:
            payload["id"] = id_
        if serial is not None:
            payload["serial"] = serial
        if device_fields is not None:
            payload["deviceFields"] = device_fields

        return await self._session.put(
            scope="sm", operation_id="updateNetworkSmDevicesFields", path=path, json=payload
        )

    async def lock_network_sm_devices(
        self,
        *,
        network_id: str,
        wifi_macs: list | None = None,
        ids: list | None = None,
        serials: list | None = None,
        scope: list | None = None,
        pin: int | None = None,
    ) -> dict[str, Any] | None:
        """Lock a set of devices.

        https://developer.cisco.com/meraki/api-v1/#!lock-network-sm-devices

        Args:
            network_id: Network ID.
            wifi_macs: The wifiMacs of the devices to be locked.
            ids: The ids of the devices to be locked.
            serials: The serials of the devices to be locked.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the devices to be locked.
            pin: The pin number for locking macOS devices (a six digit number). Required only for
              macOS devices.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices/lock"

        payload = {}
        if wifi_macs is not None:
            payload["wifiMacs"] = wifi_macs
        if ids is not None:
            payload["ids"] = ids
        if serials is not None:
            payload["serials"] = serials
        if scope is not None:
            payload["scope"] = scope
        if pin is not None:
            payload["pin"] = pin

        return await self._session.post(
            scope="sm", operation_id="lockNetworkSmDevices", path=path, json=payload
        )

    async def modify_network_sm_devices_tags(
        self,
        *,
        network_id: str,
        tags: list,
        update_action: str,
        wifi_macs: list | None = None,
        ids: list | None = None,
        serials: list | None = None,
        scope: list | None = None,
    ) -> dict[str, Any] | None:
        """Add, delete, or update the tags of a set of devices.

        https://developer.cisco.com/meraki/api-v1/#!modify-network-sm-devices-tags

        Args:
            network_id: Network ID.
            wifi_macs: The wifiMacs of the devices to be modified.
            ids: The ids of the devices to be modified.
            serials: The serials of the devices to be modified.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the devices to be modified.
            tags: The tags to be added, deleted, or updated.
            update_action: One of add, delete, or update. Only devices that have been modified will
              be returned.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices/modifyTags"

        payload = {}
        if wifi_macs is not None:
            payload["wifiMacs"] = wifi_macs
        if ids is not None:
            payload["ids"] = ids
        if serials is not None:
            payload["serials"] = serials
        if scope is not None:
            payload["scope"] = scope
        if tags is not None:
            payload["tags"] = tags
        if update_action is not None:
            payload["updateAction"] = update_action

        return await self._session.post(
            scope="sm", operation_id="modifyNetworkSmDevicesTags", path=path, json=payload
        )

    async def move_network_sm_devices(
        self,
        *,
        network_id: str,
        new_network: str,
        wifi_macs: list | None = None,
        ids: list | None = None,
        serials: list | None = None,
        scope: list | None = None,
    ) -> dict[str, Any] | None:
        """Move a set of devices to a new network.

        https://developer.cisco.com/meraki/api-v1/#!move-network-sm-devices

        Args:
            network_id: Network ID.
            wifi_macs: The wifiMacs of the devices to be moved.
            ids: The ids of the devices to be moved.
            serials: The serials of the devices to be moved.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the devices to be moved.
            new_network: The new network to which the devices will be moved.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices/move"

        payload = {}
        if wifi_macs is not None:
            payload["wifiMacs"] = wifi_macs
        if ids is not None:
            payload["ids"] = ids
        if serials is not None:
            payload["serials"] = serials
        if scope is not None:
            payload["scope"] = scope
        if new_network is not None:
            payload["newNetwork"] = new_network

        return await self._session.post(
            scope="sm", operation_id="moveNetworkSmDevices", path=path, json=payload
        )

    async def reboot_network_sm_devices(
        self,
        *,
        network_id: str,
        wifi_macs: list | None = None,
        ids: list | None = None,
        serials: list | None = None,
        scope: list | None = None,
        kext_paths: list | None = None,
        notify_user: bool | None = None,
        rebuild_kernel_cache: bool | None = None,
        request_requires_network_tether: bool | None = None,
    ) -> dict[str, Any] | None:
        """Reboot a set of endpoints.

        https://developer.cisco.com/meraki/api-v1/#!reboot-network-sm-devices

        Args:
            network_id: Network ID.
            wifi_macs: The wifiMacs of the endpoints to be rebooted.
            ids: The ids of the endpoints to be rebooted.
            serials: The serials of the endpoints to be rebooted.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the endpoints to be rebooted.
            kext_paths: The KextPaths of the endpoints to be rebooted. Available for macOS 11+.
            notify_user: Whether or not to notify the user before rebooting the endpoint. Available
              for macOS 11.3+.
            rebuild_kernel_cache: Whether or not to rebuild the kernel cache when rebooting the
              endpoint. Available for macOS 11+.
            request_requires_network_tether: Whether or not the request requires network tethering.
              Available for macOS and supervised iOS or tvOS.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices/reboot"

        payload = {}
        if wifi_macs is not None:
            payload["wifiMacs"] = wifi_macs
        if ids is not None:
            payload["ids"] = ids
        if serials is not None:
            payload["serials"] = serials
        if scope is not None:
            payload["scope"] = scope
        if kext_paths is not None:
            payload["kextPaths"] = kext_paths
        if notify_user is not None:
            payload["notifyUser"] = notify_user
        if rebuild_kernel_cache is not None:
            payload["rebuildKernelCache"] = rebuild_kernel_cache
        if request_requires_network_tether is not None:
            payload["requestRequiresNetworkTether"] = request_requires_network_tether

        return await self._session.post(
            scope="sm", operation_id="rebootNetworkSmDevices", path=path, json=payload
        )

    async def shutdown_network_sm_devices(
        self,
        *,
        network_id: str,
        wifi_macs: list | None = None,
        ids: list | None = None,
        serials: list | None = None,
        scope: list | None = None,
    ) -> dict[str, Any] | None:
        """Shutdown a set of endpoints.

        https://developer.cisco.com/meraki/api-v1/#!shutdown-network-sm-devices

        Args:
            network_id: Network ID.
            wifi_macs: The wifiMacs of the endpoints to be shutdown.
            ids: The ids of the endpoints to be shutdown.
            serials: The serials of the endpoints to be shutdown.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the endpoints to be shutdown.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices/shutdown"

        payload = {}
        if wifi_macs is not None:
            payload["wifiMacs"] = wifi_macs
        if ids is not None:
            payload["ids"] = ids
        if serials is not None:
            payload["serials"] = serials
        if scope is not None:
            payload["scope"] = scope

        return await self._session.post(
            scope="sm", operation_id="shutdownNetworkSmDevices", path=path, json=payload
        )

    async def wipe_network_sm_devices(
        self,
        *,
        network_id: str,
        wifi_mac: str | None = None,
        id_: str | None = None,
        serial: str | None = None,
        pin: int | None = None,
    ) -> dict[str, Any] | None:
        """Wipe a device.

        https://developer.cisco.com/meraki/api-v1/#!wipe-network-sm-devices

        Args:
            network_id: Network ID.
            wifi_mac: The wifiMac of the device to be wiped.
            id_: The id of the device to be wiped.
            serial: The serial of the device to be wiped.
            pin: The pin number (a six digit value) for wiping a macOS device. Required only for
              macOS devices.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/devices/wipe"

        payload = {}
        if wifi_mac is not None:
            payload["wifiMac"] = wifi_mac
        if id_ is not None:
            payload["id"] = id_
        if serial is not None:
            payload["serial"] = serial
        if pin is not None:
            payload["pin"] = pin

        return await self._session.post(
            scope="sm", operation_id="wipeNetworkSmDevices", path=path, json=payload
        )

    async def get_network_sm_device_cellular_usage_history(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """Return the client's daily cellular data usage history.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-cellular-usage-history

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/cellularUsageHistory"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmDeviceCellularUsageHistory", path=path
        )

    async def get_network_sm_device_certs(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """List the certs on a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-certs

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/certs"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmDeviceCerts", path=path
        )

    async def get_network_sm_device_connectivity(
        self,
        *,
        network_id: str,
        device_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-connectivity

        Args:
            network_id: Network ID.
            device_id: Device ID.
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/connectivity"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="sm",
            operation_id="getNetworkSmDeviceConnectivity",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_network_sm_device_desktop_logs(
        self,
        *,
        network_id: str,
        device_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Return historical records of various Systems Manager network connection details for desktop devices.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-desktop-logs

        Args:
            network_id: Network ID.
            device_id: Device ID.
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/desktopLogs"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="sm",
            operation_id="getNetworkSmDeviceDesktopLogs",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_network_sm_device_device_command_logs(
        self,
        *,
        network_id: str,
        device_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Return historical records of commands sent to Systems Manager devices.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-command-logs

        Args:
            network_id: Network ID.
            device_id: Device ID.
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/deviceCommandLogs"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="sm",
            operation_id="getNetworkSmDeviceDeviceCommandLogs",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_network_sm_device_device_profiles(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """Get the installed profiles associated with a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-profiles

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/deviceProfiles"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmDeviceDeviceProfiles", path=path
        )

    async def install_network_sm_device_apps(
        self, *, network_id: str, device_id: str, app_ids: list, force: bool | None = None
    ) -> dict[str, Any] | None:
        """Install applications on a device.

        https://developer.cisco.com/meraki/api-v1/#!install-network-sm-device-apps

        Args:
            network_id: Network ID.
            device_id: Device ID.
            app_ids: ids of applications to be installed.
            force: By default, installation of an app which is believed to already be present on the
              device will be skipped. If you'd like to force the installation of the
              app, set this parameter to true.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/installApps"

        payload = {}
        if app_ids is not None:
            payload["appIds"] = app_ids
        if force is not None:
            payload["force"] = force

        return await self._session.post(
            scope="sm", operation_id="installNetworkSmDeviceApps", path=path, json=payload
        )

    async def get_network_sm_device_network_adapters(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """List the network adapters of a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-network-adapters

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/networkAdapters"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmDeviceNetworkAdapters", path=path
        )

    async def get_network_sm_device_performance_history(
        self,
        *,
        network_id: str,
        device_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """Return historical records of various Systems Manager client metrics for desktop devices.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-performance-history

        Args:
            network_id: Network ID.
            device_id: Device ID.
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
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/performanceHistory"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="sm",
            operation_id="getNetworkSmDevicePerformanceHistory",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def refresh_network_sm_device_details(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """Refresh the details of a device.

        https://developer.cisco.com/meraki/api-v1/#!refresh-network-sm-device-details

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/refreshDetails"

        return await self._session.post(
            scope="sm", operation_id="refreshNetworkSmDeviceDetails", path=path
        )

    async def get_network_sm_device_restrictions(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """List the restrictions on a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-restrictions

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/restrictions"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmDeviceRestrictions", path=path
        )

    async def get_network_sm_device_security_centers(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """List the security centers on a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-security-centers

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/securityCenters"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmDeviceSecurityCenters", path=path
        )

    async def get_network_sm_device_softwares(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """Get a list of softwares associated with a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-softwares

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/softwares"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmDeviceSoftwares", path=path
        )

    async def unenroll_network_sm_device(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """Unenroll a device.

        https://developer.cisco.com/meraki/api-v1/#!unenroll-network-sm-device

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/unenroll"

        return await self._session.post(
            scope="sm", operation_id="unenrollNetworkSmDevice", path=path
        )

    async def uninstall_network_sm_device_apps(
        self, *, network_id: str, device_id: str, app_ids: list
    ) -> dict[str, Any] | None:
        """Uninstall applications on a device.

        https://developer.cisco.com/meraki/api-v1/#!uninstall-network-sm-device-apps

        Args:
            network_id: Network ID.
            device_id: Device ID.
            app_ids: ids of applications to be uninstalled.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/uninstallApps"

        payload = {}
        if app_ids is not None:
            payload["appIds"] = app_ids

        return await self._session.post(
            scope="sm", operation_id="uninstallNetworkSmDeviceApps", path=path, json=payload
        )

    async def get_network_sm_device_wlan_lists(
        self, *, network_id: str, device_id: str
    ) -> dict[str, Any] | None:
        """List the saved SSID names on a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-wlan-lists

        Args:
            network_id: Network ID.
            device_id: Device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        device_id = urllib.parse.quote(str(device_id), safe="")
        path = f"/networks/{network_id}/sm/devices/{device_id}/wlanLists"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmDeviceWlanLists", path=path
        )

    async def get_network_sm_profiles(
        self, *, network_id: str, payload_types: list | None = None
    ) -> dict[str, Any] | None:
        """List all profiles in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-profiles

        Args:
            network_id: Network ID.
            payload_types: Filter by payload types.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/profiles"

        params = {}
        if payload_types is not None:
            params["payloadTypes[]"] = payload_types

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmProfiles", path=path, params=params
        )

    async def get_network_sm_target_groups(
        self, *, network_id: str, with_details: bool | None = None
    ) -> dict[str, Any] | None:
        """List the target groups in this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-groups

        Args:
            network_id: Network ID.
            with_details: Boolean indicating if the the ids of the devices or users scoped by the
              target group should be included in the response.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/targetGroups"

        params = {}
        if with_details is not None:
            params["withDetails"] = with_details

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmTargetGroups", path=path, params=params
        )

    async def create_network_sm_target_group(
        self, *, network_id: str, name: str | None = None, scope: str | None = None
    ) -> dict[str, Any] | None:
        """Add a target group.

        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-target-group

        Args:
            network_id: Network ID.
            name: The name of this target group.
            scope: The scope and tag options of the target group. Comma separated values beginning
              with one of withAny, withAll, withoutAny, withoutAll, all, none, followed
              by tags. Default to none if empty.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/targetGroups"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scope is not None:
            payload["scope"] = scope

        return await self._session.post(
            scope="sm", operation_id="createNetworkSmTargetGroup", path=path, json=payload
        )

    async def get_network_sm_target_group(
        self, *, network_id: str, target_group_id: str, with_details: bool | None = None
    ) -> dict[str, Any] | None:
        """Return a target group.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-group

        Args:
            network_id: Network ID.
            target_group_id: Target group ID.
            with_details: Boolean indicating if the the ids of the devices or users scoped by the
              target group should be included in the response.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        target_group_id = urllib.parse.quote(str(target_group_id), safe="")
        path = f"/networks/{network_id}/sm/targetGroups/{target_group_id}"

        params = {}
        if with_details is not None:
            params["withDetails"] = with_details

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmTargetGroup", path=path, params=params
        )

    async def update_network_sm_target_group(
        self,
        *,
        network_id: str,
        target_group_id: str,
        name: str | None = None,
        scope: str | None = None,
    ) -> dict[str, Any] | None:
        """Update a target group.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-target-group

        Args:
            network_id: Network ID.
            target_group_id: Target group ID.
            name: The name of this target group.
            scope: The scope and tag options of the target group. Comma separated values beginning
              with one of withAny, withAll, withoutAny, withoutAll, all, none, followed
              by tags. Default to none if empty.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        target_group_id = urllib.parse.quote(str(target_group_id), safe="")
        path = f"/networks/{network_id}/sm/targetGroups/{target_group_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scope is not None:
            payload["scope"] = scope

        return await self._session.put(
            scope="sm", operation_id="updateNetworkSmTargetGroup", path=path, json=payload
        )

    async def delete_network_sm_target_group(
        self, *, network_id: str, target_group_id: str
    ) -> None:
        """Delete a target group from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-target-group

        Args:
            network_id: Network ID.
            target_group_id: Target group ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        target_group_id = urllib.parse.quote(str(target_group_id), safe="")
        path = f"/networks/{network_id}/sm/targetGroups/{target_group_id}"

        return await self._session.delete(
            scope="sm", operation_id="deleteNetworkSmTargetGroup", path=path
        )

    async def get_network_sm_trusted_access_configs(
        self,
        *,
        network_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List Trusted Access Configs.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-trusted-access-configs

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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/trustedAccessConfigs"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="sm",
            operation_id="getNetworkSmTrustedAccessConfigs",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_network_sm_user_access_devices(
        self,
        *,
        network_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List User Access Devices and its Trusted Access Connections.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-access-devices

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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/userAccessDevices"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="sm",
            operation_id="getNetworkSmUserAccessDevices",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def delete_network_sm_user_access_device(
        self, *, network_id: str, user_access_device_id: str
    ) -> None:
        """Delete a User Access Device.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        Args:
            network_id: Network ID.
            user_access_device_id: User access device ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        user_access_device_id = urllib.parse.quote(str(user_access_device_id), safe="")
        path = f"/networks/{network_id}/sm/userAccessDevices/{user_access_device_id}"

        return await self._session.delete(
            scope="sm", operation_id="deleteNetworkSmUserAccessDevice", path=path
        )

    async def get_network_sm_users(
        self,
        *,
        network_id: str,
        ids: list | None = None,
        usernames: list | None = None,
        emails: list | None = None,
        scope: list | None = None,
    ) -> dict[str, Any] | None:
        """List the owners in an SM network with various specified fields and filters.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-users

        Args:
            network_id: Network ID.
            ids: Filter users by id(s).
            usernames: Filter users by username(s).
            emails: Filter users by email(s).
            scope: Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and
              a set of tags.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        path = f"/networks/{network_id}/sm/users"

        params = {}
        if ids is not None:
            params["ids[]"] = ids
        if usernames is not None:
            params["usernames[]"] = usernames
        if emails is not None:
            params["emails[]"] = emails
        if scope is not None:
            params["scope[]"] = scope

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmUsers", path=path, params=params
        )

    async def get_network_sm_user_device_profiles(
        self, *, network_id: str, user_id: str
    ) -> dict[str, Any] | None:
        """Get the profiles associated with a user.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-device-profiles

        Args:
            network_id: Network ID.
            user_id: User ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        user_id = urllib.parse.quote(str(user_id), safe="")
        path = f"/networks/{network_id}/sm/users/{user_id}/deviceProfiles"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmUserDeviceProfiles", path=path
        )

    async def get_network_sm_user_softwares(
        self, *, network_id: str, user_id: str
    ) -> dict[str, Any] | None:
        """Get a list of softwares associated with a user.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-softwares

        Args:
            network_id: Network ID.
            user_id: User ID.

        """
        network_id = urllib.parse.quote(str(network_id), safe="")
        user_id = urllib.parse.quote(str(user_id), safe="")
        path = f"/networks/{network_id}/sm/users/{user_id}/softwares"

        return await self._session.get(
            scope="sm", operation_id="getNetworkSmUserSoftwares", path=path
        )

    async def get_organization_sm_admins_roles(
        self,
        *,
        organization_id: str,
        per_page: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        total_pages: int | Literal["all"] = 1,
        direction: Literal["prev", "next"] = "next",
    ) -> AsyncPaginatedResponse[Any]:
        """List the Limited Access Roles for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-admins-roles

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
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/sm/admins/roles"

        params = {}
        if per_page is not None:
            params["perPage"] = per_page
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if ending_before is not None:
            params["endingBefore"] = ending_before

        return self._session.get_pages(
            scope="sm",
            operation_id="getOrganizationSmAdminsRoles",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def create_organization_sm_admins_role(
        self, *, organization_id: str, name: str, scope: str | None = None, tags: list | None = None
    ) -> dict[str, Any] | None:
        """Create a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            name: The name of the Limited Access Role.
            scope: The scope of the Limited Access Role.
            tags: The tags of the Limited Access Role.

        """
        if scope is not None:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert scope in options, (
                f'"scope" cannot be "{scope}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/sm/admins/roles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scope is not None:
            payload["scope"] = scope
        if tags is not None:
            payload["tags"] = tags

        return await self._session.post(
            scope="sm", operation_id="createOrganizationSmAdminsRole", path=path, json=payload
        )

    async def get_organization_sm_admins_role(
        self, *, organization_id: str, role_id: str
    ) -> dict[str, Any] | None:
        """Return a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        role_id = urllib.parse.quote(str(role_id), safe="")
        path = f"/organizations/{organization_id}/sm/admins/roles/{role_id}"

        return await self._session.get(
            scope="sm", operation_id="getOrganizationSmAdminsRole", path=path
        )

    async def update_organization_sm_admins_role(
        self,
        *,
        organization_id: str,
        role_id: str,
        name: str | None = None,
        scope: str | None = None,
        tags: list | None = None,
    ) -> dict[str, Any] | None:
        """Update a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.
            name: The name of the Limited Access Role.
            scope: The scope of the Limited Access Role.
            tags: The tags of the Limited Access Role.

        """
        if scope is not None:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert scope in options, (
                f'"scope" cannot be "{scope}", & must be set to one of: {options}'
            )

        organization_id = urllib.parse.quote(str(organization_id), safe="")
        role_id = urllib.parse.quote(str(role_id), safe="")
        path = f"/organizations/{organization_id}/sm/admins/roles/{role_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if scope is not None:
            payload["scope"] = scope
        if tags is not None:
            payload["tags"] = tags

        return await self._session.put(
            scope="sm", operation_id="updateOrganizationSmAdminsRole", path=path, json=payload
        )

    async def delete_organization_sm_admins_role(
        self, *, organization_id: str, role_id: str
    ) -> None:
        """Delete a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-admins-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        role_id = urllib.parse.quote(str(role_id), safe="")
        path = f"/organizations/{organization_id}/sm/admins/roles/{role_id}"

        return await self._session.delete(
            scope="sm", operation_id="deleteOrganizationSmAdminsRole", path=path
        )

    async def get_organization_sm_apns_cert(self, *, organization_id: str) -> dict[str, Any] | None:
        """Get the organization's APNS certificate.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-apns-cert

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/sm/apnsCert"

        return await self._session.get(
            scope="sm", operation_id="getOrganizationSmApnsCert", path=path
        )

    async def update_organization_sm_sentry_policies_assignments(
        self, *, organization_id: str, items: list
    ) -> dict[str, Any] | None:
        """Update an Organizations Sentry Policies using the provided list.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-sentry-policies-assignments

        Args:
            organization_id: Organization ID.
            items: Sentry Group Policies for the Organization keyed by Network Id.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/sm/sentry/policies/assignments"

        payload = {}
        if items is not None:
            payload["items"] = items

        return await self._session.put(
            scope="sm",
            operation_id="updateOrganizationSmSentryPoliciesAssignments",
            path=path,
            json=payload,
        )

    async def get_organization_sm_sentry_policies_assignments_by_network(
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
        """List the Sentry Policies for an organization ordered in ascending order of priority.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-sentry-policies-assignments-by-network

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
            network_ids: Optional parameter to filter Sentry Policies by Network Id.
            total_pages: use with per_page to get total results up to total_pages * per_page; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/sm/sentry/policies/assignments/byNetwork"

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
            scope="sm",
            operation_id="getOrganizationSmSentryPoliciesAssignmentsByNetwork",
            path=path,
            params=params,
            total_pages=total_pages,
            direction=direction,
        )

    async def get_organization_sm_vpp_accounts(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List the VPP accounts in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-accounts

        Args:
            organization_id: Organization ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/sm/vppAccounts"

        return await self._session.get(
            scope="sm", operation_id="getOrganizationSmVppAccounts", path=path
        )

    async def get_organization_sm_vpp_account(
        self, *, organization_id: str, vpp_account_id: str
    ) -> dict[str, Any] | None:
        """Get a hash containing the unparsed token of the VPP account with the given ID.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-account

        Args:
            organization_id: Organization ID.
            vpp_account_id: Vpp account ID.

        """
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        vpp_account_id = urllib.parse.quote(str(vpp_account_id), safe="")
        path = f"/organizations/{organization_id}/sm/vppAccounts/{vpp_account_id}"

        return await self._session.get(
            scope="sm", operation_id="getOrganizationSmVppAccount", path=path
        )
