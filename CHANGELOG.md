# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

-

## v0.14.1

### Fixed

- Add spec overrides to fix updateDevice return type.

## v0.14.0

### Added

- Allow `required` spec overrides to apply to response `extra_fields`.

### Fixed

- Make timezone mandatory again in network responses.
- Respect nested response overrides when deduplicating reused nested schemas.
- Fixes to appliance vlan responses with spec overrides.

## v0.13.4

### Fixed

- Timezone not always present in network response.

## v0.13.3

### Fixed

- Add spec overrides to fix getOrganizationInventoryOnboardingCloudMonitoringNetworks and createOrganizationNetwork return types.

## v0.13.2

### Fixed

- Add spec overrides to fix OrganizationPolicyObjectsGroupResponse return type.

## v0.13.1

### Fixed

- Add spec overrides to fix OrganizationPolicyObjectResponse return type.

## v0.13.0

### Changed

#### Update to Meraki API v1.69.0

- Added organization-wide firewall ruleset endpoints `get_organization_policies_global_firewall_rulesets`, `create_organization_policies_global_firewall_ruleset`, `get_organization_policies_global_firewall_rulesets_rules`, `create_organization_policies_global_firewall_rulesets_rule`, `update_organization_policies_global_firewall_rulesets_rule`, `delete_organization_policies_global_firewall_rulesets_rule`, `update_organization_policies_global_firewall_ruleset`, and `delete_organization_policies_global_firewall_ruleset`.
- Added organization-wide group policy and policy object endpoints including `get_organization_policies_global_group_policies`, `create_organization_policies_global_group_policy`, `update_organization_policies_global_group_policy`, `delete_organization_policies_global_group_policy`, `get_organization_policy_objects`, `create_organization_policy_object`, `get_organization_policy_objects_groups`, `create_organization_policy_objects_group`, `get_organization_policy_object`, and `update_organization_policy_object`.
- Added organization-wide assignment endpoints `assign_organization_policies_global_group_policies_adaptive_policy_groups`, `remove_organization_policies_global_group_policies_adaptive_policy_groups`, `create_organization_policies_global_group_policies_firewall_rulesets_assignment`, `update_organization_policies_global_group_policies_firewall_rulesets_assignment`, `delete_organization_policies_global_group_policies_firewall_rulesets_assignment`, `assign_organization_policies_global_group_policies_appliance_vlans`, and `remove_organization_policies_global_group_policies_appliance_vlans`.
- Added SAML endpoints `get_organization_saml`, `update_organization_saml`, `get_organization_saml_idps`, `create_organization_saml_idp`, `get_organization_saml_idp`, `update_organization_saml_idp`, `delete_organization_saml_idp`, `get_organization_saml_roles`, `create_organization_saml_role`, `get_organization_saml_role`, `update_organization_saml_role`, and `delete_organization_saml_role`, plus SASE endpoints `get_organization_sase_connectors`, `batch_organization_sase_connectors_create`, `batch_organization_sase_connectors_delete`, `get_organization_sase_networks_eligible`, `get_organization_sase_regions`, `get_organization_sase_sites`, `attach_organization_sase_sites`, `detach_organization_sase_sites`, `update_organization_sase_site`, `get_organization_sase_sites_connectivity_history_by_site`, and `get_organization_sase_sites_connectivity_overview`.
- Added `update_network_appliance_uplinks_nat`, `get_organization_appliance_uplinks_nat_by_network`, `clip_device_camera`, `get_organization_api_rest_provisioning_pipelines_jobs`, and `get_organization_api_rest_provisioning_pipelines_jobs_overviews_by_pipeline`; `get_organization_appliance_security_intrusion` and `get_network_wireless_ssid_vpn` now return typed response models instead of `DictResponse`.

### Fixed

- Fixed duplicate generated Python parameters for endpoints where a required top-level request body ID also appears in the URL, such as `update_organization_sase_site`.

## v0.12.0

### Changed

- Codegen now deduplicates identical top-level response schemas and reuses a shared resource-style name when duplicate operations differ only by action, such as `NetworkWebhooksHttpServerResponse`.

### Fixed

- Fix spec overrides so response-only overrides no longer leak into request body parameter schemas, and correct response typing/required fields for network client, VLAN, organization, network, device, and webhook server responses.

## v0.11.1

### Added

- Added `inject_response_schema` codegen override for endpoints with bare `{type: object}` response schemas in the spec. Used to type `get_network_appliance_firewall_l3_firewall_rules`, which now returns `GetNetworkApplianceFirewallL3FirewallRulesResponse` instead of `DictResponse`.

### Fixed

- Fix automatic publishing.

## v0.11.0

### Changed

#### Update to Meraki API v1.68.0

- Added `connect_network_appliance_umbrella_account` and `disconnect_network_appliance_umbrella_account` endpoints to connect/disconnect a Cisco Umbrella account from a network.
- Added `get_organization_integrations_deployable` and `get_organization_integrations_deployed` endpoints to list available and active integrations for an organization.
- Added `get_organization_wireless_devices_provisioning_deployments`, `create_organization_wireless_devices_provisioning_deployment`, `update_organization_wireless_devices_provisioning_deployments`, and `delete_organization_wireless_devices_provisioning_deployment` endpoints for zero touch wireless AP provisioning deployments.
- Camera endpoints `get_device_camera_quality_and_retention`, `update_device_camera_quality_and_retention`, `get_device_camera_sense`, `update_device_camera_sense`, `get_device_camera_video_link`, `get_device_camera_wireless_profiles`, `update_device_camera_wireless_profiles`, and `update_organization_camera_onboarding_statuses` now return typed response schemas instead of `DictResponse`.
- Added `ecmpUplinkConfigs` field to appliance VPN peer responses (`get_network_appliance_vpn_bgp`, `update_network_appliance_vpn_bgp`).
- Added `vrf`, `vrfType`, and `ipVersion` fields to device multicast routing response.
- Added `model` field to network clients response; added `open-enhanced-with-radius` as a valid SSID `auth_mode` value.

## v0.10.3

### Fixed

- Required fields fixes for `get_organization`, `get_organizations`, `get_organization_networks`, `get_network`, `get_organization_admins`, `get_organization_appliance_uplink_statuses`, `get_device`, `get_organization_devices` responses.

## v0.10.2

### Changed

- Coerce numbers to strings automatically in response schemas.

## v0.10.1

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
