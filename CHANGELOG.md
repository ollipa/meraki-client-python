# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Fixed

- Fix required device fields for getOrganizationDevices, getOrganizationInventoryDevices and getOrganizationDevicesStatuses operations.

## v0.10.0

### Added

- Codegen: Add `force_paginated_items_schema` in `spec_overrides.toml` for endpoints where
  paginated responses are incorrectly modeled as `array[{items, meta}]` in OpenAPI.
- Add `response`, `status_code`, and `status_reason` fields to `InvalidResponseError`.
- Codegen: Generate enum request params as `Literal[...]` type hints so type checkers can
  validate allowed values at development time.

### Changed

- Codegen: Skip generating top-level paginated wrapper schemas with only `items`/`meta` fields;
  generate only item schemas used by `PaginatedResponse[T]`.
- Codegen: Treat GET endpoints with top-level `items`/`meta` responses as paginated and return
  `PaginatedResponse[T]`.
- Codegen: `force_paginated` no longer injects `total_pages`/`direction` args when the endpoint
  does not already declare pagination params in the spec.
- Session: Track page metadata on paginated results via `PaginatedResponse.meta` and
  `PaginatedResponse.meta_pages` (and async equivalent).

### Fixed

- Fix invalid cause in MerakiHTTPError.
- Fixed array item object parameter types for array of objects query parameters.

## v0.9.0

### Added

- Allow specifying operations where response can be `None` in spec overrides.

## v0.8.0

### Changed

- Return `None` only for endpoints that have no schema.

## v0.7.0

### Changed

- Change default type for lists to empty list instead of `None`.
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
