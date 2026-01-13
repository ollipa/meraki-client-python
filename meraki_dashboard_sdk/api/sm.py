"""Sm API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.rest_session import RestSession


class Sm:
    """Sm class."""

    def __init__(self, session: RestSession) -> None:
        super(self).__init__()
        self._session = session

    def create_network_sm_bypass_activation_lock_attempt(
        self, networkId: str, ids: list
    ) -> dict[str, Any] | None:
        """Bypass activation lock attempt.

        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-bypass-activation-lock-attempt

        Args:
            networkId: Network ID.
            ids: The ids of the devices to attempt activation lock bypass.

        """
        kwargs = locals()

        metadata = {
            "tags": ["sm", "configure", "bypassActivationLockAttempts"],
            "operation": "create_network_sm_bypass_activation_lock_attempt",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/bypassActivationLockAttempts"

        body_params = [
            "ids",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_sm_bypass_activation_lock_attempt(
        self, networkId: str, attemptId: str
    ) -> dict[str, Any] | None:
        """Bypass activation lock attempt status.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-bypass-activation-lock-attempt

        Args:
            networkId: Network ID.
            attemptId: Attempt ID.

        """
        metadata = {
            "tags": ["sm", "configure", "bypassActivationLockAttempts"],
            "operation": "get_network_sm_bypass_activation_lock_attempt",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        attemptId = urllib.parse.quote(str(attemptId), safe="")
        resource = f"/networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}"

        return self._session.get(metadata, resource)

    def get_network_sm_devices(
        self, networkId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the devices enrolled in an SM network with various specified fields and filters.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-devices

        Args:
            networkId: Network ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            fields: Additional fields that will be displayed for each device.     The default fields
              are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and
              serialNumber. The additional fields are: ip,     systemType,
              availableDeviceCapacity, kioskAppName, biosVersion, lastConnected,
              missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail,
              ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson,
              deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
              simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt,
              batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
              isRooted, loginRequired, screenLockEnabled, screenLockDelay,
              autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent,
              diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock,
              usesHardwareKeystore, androidSecurityPatchVersion, cellular, and url.
            wifiMacs: Filter devices by wifi mac(s).
            serials: Filter devices by serial(s).
            ids: Filter devices by id(s).
            uuids: Filter devices by uuid(s).
            systemTypes: Filter devices by system type(s).
            scope: Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll)
              and a set of tags.
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

        metadata = {"tags": ["sm", "configure", "devices"], "operation": "get_network_sm_devices"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices"

        query_params = [
            "fields",
            "wifiMacs",
            "serials",
            "ids",
            "uuids",
            "systemTypes",
            "scope",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "fields",
            "wifiMacs",
            "serials",
            "ids",
            "uuids",
            "systemTypes",
            "scope",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def checkin_network_sm_devices(self, networkId: str, **kwargs: Any) -> dict[str, Any] | None:
        """Force check-in a set of devices.

        https://developer.cisco.com/meraki/api-v1/#!checkin-network-sm-devices

        Args:
            networkId: Network ID.
            wifiMacs: The wifiMacs of the devices to be checked-in.
            ids: The ids of the devices to be checked-in.
            serials: The serials of the devices to be checked-in.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the devices to be checked-in.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "devices"],
            "operation": "checkin_network_sm_devices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices/checkin"

        body_params = [
            "wifiMacs",
            "ids",
            "serials",
            "scope",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def update_network_sm_devices_fields(
        self, networkId: str, deviceFields: dict, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Modify the fields of a device.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-devices-fields

        Args:
            networkId: Network ID.
            deviceFields: The new fields of the device. Each field of this object is optional.
            wifiMac: The wifiMac of the device to be modified.
            id: The id of the device to be modified.
            serial: The serial of the device to be modified.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "devices", "fields"],
            "operation": "update_network_sm_devices_fields",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices/fields"

        body_params = [
            "wifiMac",
            "id",
            "serial",
            "deviceFields",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def lock_network_sm_devices(self, networkId: str, **kwargs: Any) -> dict[str, Any] | None:
        """Lock a set of devices.

        https://developer.cisco.com/meraki/api-v1/#!lock-network-sm-devices

        Args:
            networkId: Network ID.
            wifiMacs: The wifiMacs of the devices to be locked.
            ids: The ids of the devices to be locked.
            serials: The serials of the devices to be locked.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the devices to be locked.
            pin: The pin number for locking macOS devices (a six digit number). Required only for
              macOS devices.

        """
        kwargs.update(locals())

        metadata = {"tags": ["sm", "configure", "devices"], "operation": "lock_network_sm_devices"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices/lock"

        body_params = [
            "wifiMacs",
            "ids",
            "serials",
            "scope",
            "pin",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def modify_network_sm_devices_tags(
        self, networkId: str, tags: list, updateAction: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Add, delete, or update the tags of a set of devices.

        https://developer.cisco.com/meraki/api-v1/#!modify-network-sm-devices-tags

        Args:
            networkId: Network ID.
            tags: The tags to be added, deleted, or updated.
            updateAction: One of add, delete, or update. Only devices that have been modified will
              be returned.
            wifiMacs: The wifiMacs of the devices to be modified.
            ids: The ids of the devices to be modified.
            serials: The serials of the devices to be modified.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the devices to be modified.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "devices"],
            "operation": "modify_network_sm_devices_tags",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices/modifyTags"

        body_params = [
            "wifiMacs",
            "ids",
            "serials",
            "scope",
            "tags",
            "updateAction",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def move_network_sm_devices(
        self, networkId: str, newNetwork: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Move a set of devices to a new network.

        https://developer.cisco.com/meraki/api-v1/#!move-network-sm-devices

        Args:
            networkId: Network ID.
            newNetwork: The new network to which the devices will be moved.
            wifiMacs: The wifiMacs of the devices to be moved.
            ids: The ids of the devices to be moved.
            serials: The serials of the devices to be moved.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the devices to be moved.

        """
        kwargs.update(locals())

        metadata = {"tags": ["sm", "configure", "devices"], "operation": "move_network_sm_devices"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices/move"

        body_params = [
            "wifiMacs",
            "ids",
            "serials",
            "scope",
            "newNetwork",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def reboot_network_sm_devices(self, networkId: str, **kwargs: Any) -> dict[str, Any] | None:
        """Reboot a set of endpoints.

        https://developer.cisco.com/meraki/api-v1/#!reboot-network-sm-devices

        Args:
            networkId: Network ID.
            wifiMacs: The wifiMacs of the endpoints to be rebooted.
            ids: The ids of the endpoints to be rebooted.
            serials: The serials of the endpoints to be rebooted.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the endpoints to be rebooted.
            kextPaths: The KextPaths of the endpoints to be rebooted. Available for macOS 11+.
            notifyUser: Whether or not to notify the user before rebooting the endpoint. Available
              for macOS 11.3+.
            rebuildKernelCache: Whether or not to rebuild the kernel cache when rebooting the
              endpoint. Available for macOS 11+.
            requestRequiresNetworkTether: Whether or not the request requires network tethering.
              Available for macOS and supervised iOS or tvOS.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "devices"],
            "operation": "reboot_network_sm_devices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices/reboot"

        body_params = [
            "wifiMacs",
            "ids",
            "serials",
            "scope",
            "kextPaths",
            "notifyUser",
            "rebuildKernelCache",
            "requestRequiresNetworkTether",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def shutdown_network_sm_devices(self, networkId: str, **kwargs: Any) -> dict[str, Any] | None:
        """Shutdown a set of endpoints.

        https://developer.cisco.com/meraki/api-v1/#!shutdown-network-sm-devices

        Args:
            networkId: Network ID.
            wifiMacs: The wifiMacs of the endpoints to be shutdown.
            ids: The ids of the endpoints to be shutdown.
            serials: The serials of the endpoints to be shutdown.
            scope: The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a
              set of tags of the endpoints to be shutdown.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "devices"],
            "operation": "shutdown_network_sm_devices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices/shutdown"

        body_params = [
            "wifiMacs",
            "ids",
            "serials",
            "scope",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def wipe_network_sm_devices(self, networkId: str, **kwargs: Any) -> dict[str, Any] | None:
        """Wipe a device.

        https://developer.cisco.com/meraki/api-v1/#!wipe-network-sm-devices

        Args:
            networkId: Network ID.
            wifiMac: The wifiMac of the device to be wiped.
            id: The id of the device to be wiped.
            serial: The serial of the device to be wiped.
            pin: The pin number (a six digit value) for wiping a macOS device. Required only for
              macOS devices.

        """
        kwargs.update(locals())

        metadata = {"tags": ["sm", "configure", "devices"], "operation": "wipe_network_sm_devices"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/devices/wipe"

        body_params = [
            "wifiMac",
            "id",
            "serial",
            "pin",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_sm_device_cellular_usage_history(
        self, networkId: str, deviceId: str
    ) -> dict[str, Any] | None:
        """Return the client's daily cellular data usage history.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-cellular-usage-history

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "monitor", "devices", "cellularUsageHistory"],
            "operation": "get_network_sm_device_cellular_usage_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/cellularUsageHistory"

        return self._session.get(metadata, resource)

    def get_network_sm_device_certs(self, networkId: str, deviceId: str) -> dict[str, Any] | None:
        """List the certs on a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-certs

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices", "certs"],
            "operation": "get_network_sm_device_certs",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/certs"

        return self._session.get(metadata, resource)

    def get_network_sm_device_connectivity(
        self, networkId: str, deviceId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-connectivity

        Args:
            networkId: Network ID.
            deviceId: Device ID.
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

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "monitor", "devices", "connectivity"],
            "operation": "get_network_sm_device_connectivity",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/connectivity"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_sm_device_desktop_logs(
        self, networkId: str, deviceId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return historical records of various Systems Manager network connection details for desktop devices.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-desktop-logs

        Args:
            networkId: Network ID.
            deviceId: Device ID.
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

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "monitor", "devices", "desktopLogs"],
            "operation": "get_network_sm_device_desktop_logs",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/desktopLogs"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_sm_device_device_command_logs(
        self, networkId: str, deviceId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return historical records of commands sent to Systems Manager devices.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-command-logs

        Args:
            networkId: Network ID.
            deviceId: Device ID.
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

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "monitor", "devices", "deviceCommandLogs"],
            "operation": "get_network_sm_device_device_command_logs",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/deviceCommandLogs"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_sm_device_device_profiles(
        self, networkId: str, deviceId: str
    ) -> dict[str, Any] | None:
        """Get the installed profiles associated with a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-profiles

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices", "deviceProfiles"],
            "operation": "get_network_sm_device_device_profiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/deviceProfiles"

        return self._session.get(metadata, resource)

    def install_network_sm_device_apps(
        self, networkId: str, deviceId: str, appIds: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Install applications on a device.

        https://developer.cisco.com/meraki/api-v1/#!install-network-sm-device-apps

        Args:
            networkId: Network ID.
            deviceId: Device ID.
            appIds: ids of applications to be installed.
            force: By default, installation of an app which is believed to already be present on the
              device will be skipped. If you'd like to force the installation of the
              app, set this parameter to true.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "devices"],
            "operation": "install_network_sm_device_apps",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/installApps"

        body_params = [
            "appIds",
            "force",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_sm_device_network_adapters(
        self, networkId: str, deviceId: str
    ) -> dict[str, Any] | None:
        """List the network adapters of a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-network-adapters

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices", "networkAdapters"],
            "operation": "get_network_sm_device_network_adapters",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/networkAdapters"

        return self._session.get(metadata, resource)

    def get_network_sm_device_performance_history(
        self, networkId: str, deviceId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """Return historical records of various Systems Manager client metrics for desktop devices.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-performance-history

        Args:
            networkId: Network ID.
            deviceId: Device ID.
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

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "monitor", "devices", "performanceHistory"],
            "operation": "get_network_sm_device_performance_history",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/performanceHistory"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def refresh_network_sm_device_details(
        self, networkId: str, deviceId: str
    ) -> dict[str, Any] | None:
        """Refresh the details of a device.

        https://developer.cisco.com/meraki/api-v1/#!refresh-network-sm-device-details

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices"],
            "operation": "refresh_network_sm_device_details",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/refreshDetails"

        return self._session.post(metadata, resource)

    def get_network_sm_device_restrictions(
        self, networkId: str, deviceId: str
    ) -> dict[str, Any] | None:
        """List the restrictions on a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-restrictions

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices", "restrictions"],
            "operation": "get_network_sm_device_restrictions",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/restrictions"

        return self._session.get(metadata, resource)

    def get_network_sm_device_security_centers(
        self, networkId: str, deviceId: str
    ) -> dict[str, Any] | None:
        """List the security centers on a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-security-centers

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices", "securityCenters"],
            "operation": "get_network_sm_device_security_centers",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/securityCenters"

        return self._session.get(metadata, resource)

    def get_network_sm_device_softwares(
        self, networkId: str, deviceId: str
    ) -> dict[str, Any] | None:
        """Get a list of softwares associated with a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-softwares

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices", "softwares"],
            "operation": "get_network_sm_device_softwares",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/softwares"

        return self._session.get(metadata, resource)

    def unenroll_network_sm_device(self, networkId: str, deviceId: str) -> dict[str, Any] | None:
        """Unenroll a device.

        https://developer.cisco.com/meraki/api-v1/#!unenroll-network-sm-device

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices"],
            "operation": "unenroll_network_sm_device",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/unenroll"

        return self._session.post(metadata, resource)

    def uninstall_network_sm_device_apps(
        self, networkId: str, deviceId: str, appIds: list
    ) -> dict[str, Any] | None:
        """Uninstall applications on a device.

        https://developer.cisco.com/meraki/api-v1/#!uninstall-network-sm-device-apps

        Args:
            networkId: Network ID.
            deviceId: Device ID.
            appIds: ids of applications to be uninstalled.

        """
        kwargs = locals()

        metadata = {
            "tags": ["sm", "configure", "devices"],
            "operation": "uninstall_network_sm_device_apps",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/uninstallApps"

        body_params = [
            "appIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_sm_device_wlan_lists(
        self, networkId: str, deviceId: str
    ) -> dict[str, Any] | None:
        """List the saved SSID names on a device.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-wlan-lists

        Args:
            networkId: Network ID.
            deviceId: Device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "devices", "wlanLists"],
            "operation": "get_network_sm_device_wlan_lists",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        deviceId = urllib.parse.quote(str(deviceId), safe="")
        resource = f"/networks/{networkId}/sm/devices/{deviceId}/wlanLists"

        return self._session.get(metadata, resource)

    def get_network_sm_profiles(self, networkId: str, **kwargs: Any) -> dict[str, Any] | None:
        """List all profiles in a network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-profiles

        Args:
            networkId: Network ID.
            payloadTypes: Filter by payload types.

        """
        kwargs.update(locals())

        metadata = {"tags": ["sm", "configure", "profiles"], "operation": "get_network_sm_profiles"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/profiles"

        query_params = [
            "payloadTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "payloadTypes",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_network_sm_target_groups(self, networkId: str, **kwargs: Any) -> dict[str, Any] | None:
        """List the target groups in this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-groups

        Args:
            networkId: Network ID.
            withDetails: Boolean indicating if the the ids of the devices or users scoped by the
              target group should be included in the response.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "targetGroups"],
            "operation": "get_network_sm_target_groups",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/targetGroups"

        query_params = [
            "withDetails",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def create_network_sm_target_group(
        self, networkId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Add a target group.

        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-target-group

        Args:
            networkId: Network ID.
            name: The name of this target group.
            scope: The scope and tag options of the target group. Comma separated values beginning
              with one of withAny, withAll, withoutAny, withoutAll, all, none, followed
              by tags. Default to none if empty.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "targetGroups"],
            "operation": "create_network_sm_target_group",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/targetGroups"

        body_params = [
            "name",
            "scope",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_network_sm_target_group(
        self, networkId: str, targetGroupId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Return a target group.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-group

        Args:
            networkId: Network ID.
            targetGroupId: Target group ID.
            withDetails: Boolean indicating if the the ids of the devices or users scoped by the
              target group should be included in the response.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "targetGroups"],
            "operation": "get_network_sm_target_group",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        targetGroupId = urllib.parse.quote(str(targetGroupId), safe="")
        resource = f"/networks/{networkId}/sm/targetGroups/{targetGroupId}"

        query_params = [
            "withDetails",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def update_network_sm_target_group(
        self, networkId: str, targetGroupId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a target group.

        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-target-group

        Args:
            networkId: Network ID.
            targetGroupId: Target group ID.
            name: The name of this target group.
            scope: The scope and tag options of the target group. Comma separated values beginning
              with one of withAny, withAll, withoutAny, withoutAll, all, none, followed
              by tags. Default to none if empty.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "targetGroups"],
            "operation": "update_network_sm_target_group",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        targetGroupId = urllib.parse.quote(str(targetGroupId), safe="")
        resource = f"/networks/{networkId}/sm/targetGroups/{targetGroupId}"

        body_params = [
            "name",
            "scope",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_network_sm_target_group(self, networkId: str, targetGroupId: str) -> None:
        """Delete a target group from a network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-target-group

        Args:
            networkId: Network ID.
            targetGroupId: Target group ID.

        """
        metadata = {
            "tags": ["sm", "configure", "targetGroups"],
            "operation": "delete_network_sm_target_group",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        targetGroupId = urllib.parse.quote(str(targetGroupId), safe="")
        resource = f"/networks/{networkId}/sm/targetGroups/{targetGroupId}"

        return self._session.delete(metadata, resource)

    def get_network_sm_trusted_access_configs(
        self, networkId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List Trusted Access Configs.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-trusted-access-configs

        Args:
            networkId: Network ID.
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
            "tags": ["sm", "configure", "trustedAccessConfigs"],
            "operation": "get_network_sm_trusted_access_configs",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/trustedAccessConfigs"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_network_sm_user_access_devices(
        self, networkId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List User Access Devices and its Trusted Access Connections.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-access-devices

        Args:
            networkId: Network ID.
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
            "tags": ["sm", "configure", "userAccessDevices"],
            "operation": "get_network_sm_user_access_devices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/userAccessDevices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def delete_network_sm_user_access_device(self, networkId: str, userAccessDeviceId: str) -> None:
        """Delete a User Access Device.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        Args:
            networkId: Network ID.
            userAccessDeviceId: User access device ID.

        """
        metadata = {
            "tags": ["sm", "configure", "userAccessDevices"],
            "operation": "delete_network_sm_user_access_device",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        userAccessDeviceId = urllib.parse.quote(str(userAccessDeviceId), safe="")
        resource = f"/networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId}"

        return self._session.delete(metadata, resource)

    def get_network_sm_users(self, networkId: str, **kwargs: Any) -> dict[str, Any] | None:
        """List the owners in an SM network with various specified fields and filters.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-users

        Args:
            networkId: Network ID.
            ids: Filter users by id(s).
            usernames: Filter users by username(s).
            emails: Filter users by email(s).
            scope: Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and
              a set of tags.

        """
        kwargs.update(locals())

        metadata = {"tags": ["sm", "configure"], "operation": "get_network_sm_users"}
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/users"

        query_params = [
            "ids",
            "usernames",
            "emails",
            "scope",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "ids",
            "usernames",
            "emails",
            "scope",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_network_sm_user_device_profiles(
        self, networkId: str, userId: str
    ) -> dict[str, Any] | None:
        """Get the profiles associated with a user.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-device-profiles

        Args:
            networkId: Network ID.
            userId: User ID.

        """
        metadata = {
            "tags": ["sm", "configure", "deviceProfiles"],
            "operation": "get_network_sm_user_device_profiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        userId = urllib.parse.quote(str(userId), safe="")
        resource = f"/networks/{networkId}/sm/users/{userId}/deviceProfiles"

        return self._session.get(metadata, resource)

    def get_network_sm_user_softwares(self, networkId: str, userId: str) -> dict[str, Any] | None:
        """Get a list of softwares associated with a user.

        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-softwares

        Args:
            networkId: Network ID.
            userId: User ID.

        """
        metadata = {
            "tags": ["sm", "configure", "softwares"],
            "operation": "get_network_sm_user_softwares",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        userId = urllib.parse.quote(str(userId), safe="")
        resource = f"/networks/{networkId}/sm/users/{userId}/softwares"

        return self._session.get(metadata, resource)

    def get_organization_sm_admins_roles(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the Limited Access Roles for an organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-admins-roles

        Args:
            organizationId: Organization ID.
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

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "get_organization_sm_admins_roles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/admins/roles"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def create_organization_sm_admins_role(
        self, organizationId: str, name: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Create a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-admins-role

        Args:
            organizationId: Organization ID.
            name: The name of the Limited Access Role.
            scope: The scope of the Limited Access Role.
            tags: The tags of the Limited Access Role.

        """
        kwargs.update(locals())

        if "scope" in kwargs:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert kwargs["scope"] in options, (
                f'''"scope" cannot be "{kwargs["scope"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "create_organization_sm_admins_role",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/admins/roles"

        body_params = [
            "name",
            "scope",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_sm_admins_role(
        self, organizationId: str, roleId: str
    ) -> dict[str, Any] | None:
        """Return a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-admins-role

        Args:
            organizationId: Organization ID.
            roleId: Role ID.

        """
        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "get_organization_sm_admins_role",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        roleId = urllib.parse.quote(str(roleId), safe="")
        resource = f"/organizations/{organizationId}/sm/admins/roles/{roleId}"

        return self._session.get(metadata, resource)

    def update_organization_sm_admins_role(
        self, organizationId: str, roleId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Update a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-admins-role

        Args:
            organizationId: Organization ID.
            roleId: Role ID.
            name: The name of the Limited Access Role.
            scope: The scope of the Limited Access Role.
            tags: The tags of the Limited Access Role.

        """
        kwargs.update(locals())

        if "scope" in kwargs:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert kwargs["scope"] in options, (
                f'''"scope" cannot be "{kwargs["scope"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "update_organization_sm_admins_role",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        roleId = urllib.parse.quote(str(roleId), safe="")
        resource = f"/organizations/{organizationId}/sm/admins/roles/{roleId}"

        body_params = [
            "name",
            "scope",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def delete_organization_sm_admins_role(self, organizationId: str, roleId: str) -> None:
        """Delete a Limited Access Role.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-admins-role

        Args:
            organizationId: Organization ID.
            roleId: Role ID.

        """
        metadata = {
            "tags": ["sm", "configure", "admins", "roles"],
            "operation": "delete_organization_sm_admins_role",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        roleId = urllib.parse.quote(str(roleId), safe="")
        resource = f"/organizations/{organizationId}/sm/admins/roles/{roleId}"

        return self._session.delete(metadata, resource)

    def get_organization_sm_apns_cert(self, organizationId: str) -> dict[str, Any] | None:
        """Get the organization's APNS certificate.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-apns-cert

        Args:
            organizationId: Organization ID.

        """
        metadata = {
            "tags": ["sm", "configure", "apnsCert"],
            "operation": "get_organization_sm_apns_cert",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/apnsCert"

        return self._session.get(metadata, resource)

    def update_organization_sm_sentry_policies_assignments(
        self, organizationId: str, items: list
    ) -> dict[str, Any] | None:
        """Update an Organizations Sentry Policies using the provided list.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-sentry-policies-assignments

        Args:
            organizationId: Organization ID.
            items: Sentry Group Policies for the Organization keyed by Network Id.

        """
        kwargs = locals()

        metadata = {
            "tags": ["sm", "configure", "sentry", "policies", "assignments"],
            "operation": "update_organization_sm_sentry_policies_assignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/sentry/policies/assignments"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def get_organization_sm_sentry_policies_assignments_by_network(
        self, organizationId: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the Sentry Policies for an organization ordered in ascending order of priority.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-sentry-policies-assignments-by-network

        Args:
            organizationId: Organization ID.
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
            networkIds: Optional parameter to filter Sentry Policies by Network Id.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["sm", "configure", "sentry", "policies", "assignments", "byNetwork"],
            "operation": "get_organization_sm_sentry_policies_assignments_by_network",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/sentry/policies/assignments/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_sm_vpp_accounts(self, organizationId: str) -> dict[str, Any] | None:
        """List the VPP accounts in the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-accounts

        Args:
            organizationId: Organization ID.

        """
        metadata = {
            "tags": ["sm", "configure", "vppAccounts"],
            "operation": "get_organization_sm_vpp_accounts",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/vppAccounts"

        return self._session.get(metadata, resource)

    def get_organization_sm_vpp_account(
        self, organizationId: str, vppAccountId: str
    ) -> dict[str, Any] | None:
        """Get a hash containing the unparsed token of the VPP account with the given ID.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-account

        Args:
            organizationId: Organization ID.
            vppAccountId: Vpp account ID.

        """
        metadata = {
            "tags": ["sm", "configure", "vppAccounts"],
            "operation": "get_organization_sm_vpp_account",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        vppAccountId = urllib.parse.quote(str(vppAccountId), safe="")
        resource = f"/organizations/{organizationId}/sm/vppAccounts/{vppAccountId}"

        return self._session.get(metadata, resource)
