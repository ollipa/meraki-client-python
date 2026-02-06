# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Changed

- Format Meraki API error messages as a single line when logged or displayed in exceptions.

## v0.6.0

### Added

- Codegen: Support for adding missing fields via `[operationId.extra_fields]` in `spec_overrides.toml`.
- Add `dot11w` and `dot11r` fields to `getNetworkWirelessSsids` response (missing from OpenAPI spec).
- Documentation for accessing extra fields via `model_extra`.
- Add batch endpoints to API reference documentation.

### Changed

#### Update to Meraki API v1.67.0

- New endpoints: `get_organization_inventory_devices_eox_overview`, `get_network_moves`, `create_network_move`, `update_network_wireless_radio_rrm`, `get_organization_wireless_radio_rrm_by_network`.
- New parameter `eox_statuses` filter for `get_organization_inventory_devices`.
- New parameter `multicast_to_unicast_conversion` for `update_network_wireless_settings`.
- New response field `eox` in inventory device responses with EOX status information.
- New response field `useOobMgmt` in switch alternate management interface responses.
- New response field `alwaysAllowedServers` in switch DHCP server policy responses.
- Change Policy Object Group `object_ids` type from `list[int]` to `list[str]`.
- Remove `nac` API module (NAC certificates authorities CRL endpoints).

## v0.5.0

### Added

- Codegen: Support for marking response fields as required via `[operationId.required]` in `spec_overrides.toml`.
- Mark `id` as required for organization and network responses (`getOrganization`, `getOrganizations`, `getNetwork`, `getOrganizationNetworks`).
- Mark `organizationId` as required for network responses (`getNetwork`, `getOrganizationNetworks`).
- Mark `serial` as required for `getOrganizationDevices` response.

## v0.4.0

### Changed

- All list-returning GET endpoints now return `PaginatedResponse[T]` instead of `Schema | None`.
- Raise exception if pagination endpoint dict doesn't contain required keys.

## v0.3.0

### Changed

- Return empty list instead of None in list endpoints.

## v0.2.0

### Fixed

- Fix invalid URL when paginating.
- Fix recognizing schema params with type checkers.
- Fix handling of abbreviations when converting to snake-case.

## v0.1.0

### Added

- Initial release of meraki-client.
