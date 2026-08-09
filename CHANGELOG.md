# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

-

## v0.19.0

### Changed

#### Update to Meraki API v1.73.0

- Added campus gateway endpoints `delete_network_campus_gateway_cluster`, `provision_organization_campus_gateway_clusters`, `get_organization_campus_gateway_clients_usage_by_network_by_cluster`, `get_organization_campus_gateway_clusters_failover_targets`, `get_organization_campus_gateway_clusters_failover_targets_by_cluster`, `get_organization_campus_gateway_clusters_networks_overviews`, `get_organization_campus_gateway_clusters_ssids`, `get_organization_campus_gateway_clusters_tunnelable`, `get_organization_campus_gateway_connections`, and `get_organization_campus_gateway_connections_overview`.
- Added organization-wide wireless SSID profile endpoints `get_organization_wireless_ssids_profiles`, `create_organization_wireless_ssids_profile`, `update_organization_wireless_ssids_profile`, `delete_organization_wireless_ssids_profile`, `get_organization_wireless_ssids_profiles_overviews`, `get_organization_wireless_ssids_profiles_assignments`, `get_organization_wireless_ssids_profiles_assignments_by_network`, `create_organization_wireless_ssids_profiles_assignment`, and `delete_organization_wireless_ssids_profiles_assignments`.
- Added wireless client usage endpoints `get_organization_wireless_clients_usage_by_network`, `get_organization_wireless_clients_usage_by_network_by_ssid`, `get_organization_wireless_clients_usage_by_ssid`, and `get_organization_wireless_clients_connections_impacted_by_network_by_ssid`.
- Added network group endpoints `get_organization_networks_groups`, `create_organization_networks_group`, `update_organization_networks_group`, `delete_organization_networks_group`, `get_organization_networks_groups_overview_by_group`, `bulk_organization_networks_group_assign`, and `bulk_organization_networks_group_unassign`.
- Added assurance alert profile endpoints `get_organization_assurance_alerts_profiles`, `create_organization_assurance_alerts_profile`, `update_organization_assurance_alerts_profile`, and `delete_organization_assurance_alerts_profile`, plus `get_organization_assurance_impacted_device_wireless_by_network`.
- Added campus gateway support to existing endpoints: a `campus_gateway` parameter on `update_network_wireless_ssid`, a `campusGateway` product in `create_network_firmware_upgrades_rollback` and `get_network_firmware_upgrades` responses.
- Added `enabled` parameter to `create_network_appliance_static_route`, `mac` to `create_device_live_tools_mac_table`, and `feature_loss_acknowledgements` to `update_network_firmware_upgrades`.
- Added pagination parameters (`per_page`, `starting_after`, `ending_before`, `total_pages`, `direction`) to `get_network_sm_profiles`.
- Added `enabled` to webhook HTTP server responses and `strategy` to firmware `nextUpgrade` response schemas.
- Changed previously untyped responses to typed schemas: `get_network_traffic_shaping_dscp_tagging_options` now yields `GetNetworkTrafficShapingDscpTaggingOptionsResponseItem` items, `get_network_wireless_ssid_device_type_group_policies` and `update_network_wireless_ssid_device_type_group_policies` return `NetworkWirelessSsidDeviceTypeGroupPoliciesResponse` instead of `DictResponse`, and `attach_organization_sase_sites` / `detach_organization_sase_sites` return dedicated response schemas instead of `BatchOrganizationSaseConnectorsDeleteResponse` / `None`.
- Removed the `callback` parameter from `attach_organization_sase_sites` and `detach_organization_sase_sites`; `items` is now required on `attach_organization_sase_sites`.
- Removed the `Google Apps domain` splash page option from `update_network_wireless_ssid`.
- Removed MV14, MV24, MV34, MV54N, MV64, MV74, and MV94 video settings from `create_network_camera_quality_retention_profile` and `update_network_camera_quality_retention_profile`; the v1.73.0 spec no longer defines them.
- Removed `load_balancing` from the `uplink` parameter and response of `update_network_appliance_devices_redundancy`.

## v0.18.0

### Fixed

- Array fields in response schemas now accept `null` and coerce it to an empty list, instead of raising a validation error. This fixes, for example, `get_network_topology_link_layer` responses where `nodes[].discovered.lldp.systemCapabilities` is `null`. Schemas that declare list fields get a generated `coerce_null_lists` validator; field annotations are unchanged.

## v0.17.0

### Fixed

- Remove obsolete `extra_fields` overrides for `getDevice`, `updateDevice`, `getNetworkDevices` (`url`), and `getNetworkWirelessSsids` (`dot11w`, `dot11r`), which the v1.72.0 spec now defines natively. `dot11w` and `dot11r` are now typed nested objects (`WirelessDot11w`/`WirelessDot11r`) instead of `dict[str, Any]`, and `getNetworkWirelessSsids` reuses the shared `NetworkWirelessSsidResponse` schema.

### Changed

#### Update to Meraki API v1.72.0

- Added device syslog server endpoints `update_network_devices_syslog_servers`, `get_organization_devices_syslog_servers_by_network`, and `get_organization_devices_syslog_servers_roles_by_network`.
- Added `update_network_switch_stack` endpoint to rename a switch stack and set its complete member list.
- Added `security` parameter to `update_network_wireless_ssid` for configuring SSID security settings.
- Changed `type_` parameter of `create_organization_policy_object` to the `CreateOrganizationPolicyObjectType` literal (`adaptivePolicyIpv4Cidr`, `cidr`, `fqdn`); the `ipAndMask` type is dropped and the `cidr`, `mask`, and `ip` parameters are now deprecated.
- Added support for MV24 and MV94 camera models (and an `enhanced` `axisVideoQuality` option) in the video settings of `create_network_camera_quality_retention_profile` and `update_network_camera_quality_retention_profile`.
- Added assurance alert types `modular_supervisor_node_group_mismatch`, `stack_cable_auth_failure`, `stack_version_mismatch`, `telemetry_collector_cert_expiration`, and `telemetry_streaming_failure` to the `types` filter enums for the `get_organization_assurance_alerts*` endpoints.

## v0.16.0

### Fixed

- Remove `getOrganizationApplianceUplinkStatuses` endpoint `lastReportedAt` field override. `lastReportedAt` can be null in some cases.
- Mark `pipeline_ids` parameter of `get_organization_api_rest_provisioning_pipelines_jobs` and `product_type` parameter of `get_network_events` as required, matching actual API behavior (spec incorrectly marks them optional).

### Changed

#### Update to Meraki API v1.71.0

- Added appliance L3 interface endpoints `create_network_appliance_interfaces_l3`, `update_network_appliance_interfaces_l3`, `delete_network_appliance_interfaces_l3`, `get_organization_appliance_devices_interfaces_l3`, and `get_organization_appliance_devices_interfaces_ports_by_device`.
- Added appliance monitoring endpoints `get_organization_appliance_devices_ports_transceivers_readings_history_by_device` and `get_organization_appliance_interfaces_packets_overviews_by_device`.
- Added appliance Umbrella policy management endpoints `add_network_appliance_umbrella_policies`, `remove_network_appliance_umbrella_policies`, `exclusions_network_appliance_umbrella_domains`, and `protection_network_appliance_umbrella`.
- Added device live tools endpoints `create_device_live_tools_ports_status`, `get_device_live_tools_ports_status`, `create_device_live_tools_power_usage`, `get_device_live_tools_power_usage`, `create_device_live_tools_routing_table_lookup`, `get_device_live_tools_routing_table_lookup`, `create_device_live_tools_routing_table_summary`, and `get_device_live_tools_routing_table_summary`.
- Added `create_device_appliance_interfaces_ports_update` endpoint to trigger appliance interface port updates.
- Added `authentication` and `privacy` parameters to `update_network_snmp` for SNMPv3 user authentication and privacy settings.
- Added `enforce_locked_ip_sessions` parameter to `update_organization_login_security`.
- Added `privacy` parameter to `update_organization`.
- Added `user_consent` parameter to `update_network_wireless_ssid_splash_settings`.

## v0.15.2

### Fixed

- Mark `portId`, `enabled`, and `type` as required on the switch port response shared by `get_device_switch_ports`, `get_device_switch_port`, and `update_device_switch_port`. The spec marks every field nullable, but these fields are always returned.
- Mark `id` and `name` as required on the wireless RF profile response shared by `get_network_wireless_rf_profiles`, `get_network_wireless_rf_profile`, `create_network_wireless_rf_profile`, and `update_network_wireless_rf_profile`. The spec marks every field nullable, but an RF profile always has an ID and name.
- Mark `id` and `name` as required on the content filtering category items returned by `get_network_appliance_content_filtering`, `update_network_appliance_content_filtering`, and `get_network_appliance_content_filtering_categories`. Every category Meraki returns has both fields.
- Mark `policy`, `protocol`, `srcCidr`, `srcPort`, `destCidr`, `destPort`, and `syslogEnabled` as required on the appliance firewall rule items returned by the cellular, inbound cellular, inbound, L3, and VPN firewall rule endpoints (`get`/`update` variants). The spec marks every field nullable, but every rule has these fields populated.

## v0.15.1

### Fixed

- Mark `number`, `enabled`, and `type` as required on the appliance port response shared by `get_network_appliance_ports`, `get_network_appliance_port`, and `update_network_appliance_port`. The spec marks every field nullable, but these fields are always returned.

## v0.15.0

### Changed

#### Update to Meraki API v1.70.0

- Added organization-wide cellular data management endpoints `get_organization_devices_cellular_data_profiles`, `create_organization_devices_cellular_data_profile`, `update_organization_devices_cellular_data_profile`, `delete_organization_devices_cellular_data_profile`, `get_organization_devices_cellular_data_profiles_assignments`, `batch_organization_devices_cellular_data_profiles_assignments_create`, `bulk_organization_devices_cellular_data_profiles_assignments_delete`, `get_organization_devices_cellular_data_devices`, `get_organization_devices_cellular_data_usage_by_device`, and `get_organization_devices_cellular_data_usage_history_by_device_by_interval`.
- Added cellular geolocation, band, and tower endpoints `get_organization_devices_cellular_geolocations`, `update_device_cellular_geolocations`, `get_organization_devices_cellular_uplinks_bands_by_device`, `create_device_cellular_uplinks_bands_masks_update`, and `get_organization_devices_cellular_uplinks_towers_by_device`.
- Added appliance redundancy and VRF settings endpoints `get_organization_appliance_devices_redundancy_by_network`, `update_network_appliance_devices_redundancy`, `create_network_appliance_devices_redundancy_swap`, `get_organization_appliance_routing_vrfs_settings`, and `update_organization_appliance_routing_vrfs_settings`.
- Added port cycle live tools endpoints `create_device_live_tools_ports_cycle` and `get_device_live_tools_ports_cycle`.
- Added SASE integration endpoints `get_organization_sase_integration`, `create_organization_sase_integration`, and `delete_organization_sase_integration`.
- Removed `batch_organization_sase_connectors_create` and the cloud monitoring onboarding endpoints `create_organization_inventory_onboarding_cloud_monitoring_export_event`, `create_organization_inventory_onboarding_cloud_monitoring_import`, `create_organization_inventory_onboarding_cloud_monitoring_prepare`, `get_organization_inventory_onboarding_cloud_monitoring_imports`, and `get_organization_inventory_onboarding_cloud_monitoring_networks`.

### Fixed

- Duplicate generated Python parameters for endpoints where an optional top-level request body ID also appears in the URL, such as `update_organization_devices_cellular_data_profile`.

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
