"""Tests for response schema validation behavior."""

import pytest
from pydantic import ValidationError

from meraki_client.schemas import GetNetworkTopologyLinkLayerResponse
from meraki_client.schemas._networks import NetworksLldp2


def _topology_response(system_capabilities: object) -> dict[str, object]:
    return {
        "nodes": [
            {
                "derivedId": "aabbccddeeff",
                "mac": "AA:BB:CC:DD:EE:FF",
                "type": "discovered",
                "root": False,
                "discovered": {
                    "lldp": {
                        "systemName": "switch01",
                        "chassisId": "12345",
                        "systemDescription": "Extreme Networks Switch Engine",
                        "systemCapabilities": system_capabilities,
                        "managementAddress": None,
                    },
                    "cdp": None,
                },
            }
        ],
        "links": None,
        "errors": None,
    }


def test_null_array_becomes_empty_list() -> None:
    """The API returns null for arrays such as systemCapabilities, which must not fail."""
    response = GetNetworkTopologyLinkLayerResponse.model_validate(_topology_response(None))

    node = response.nodes[0]
    assert node.discovered is not None
    assert node.discovered.lldp is not None
    assert node.discovered.lldp.system_capabilities == []
    assert response.links == []
    assert response.errors == []


def test_array_values_are_preserved() -> None:
    """Coercing null must not affect responses that contain array values."""
    response = GetNetworkTopologyLinkLayerResponse.model_validate(
        _topology_response(["router", "switch"])
    )

    node = response.nodes[0]
    assert node.discovered is not None
    assert node.discovered.lldp is not None
    assert node.discovered.lldp.system_capabilities == ["router", "switch"]


def test_missing_array_defaults_to_empty_list() -> None:
    assert NetworksLldp2.model_validate({}).system_capabilities == []


def test_null_array_serializes_as_empty_list() -> None:
    lldp = NetworksLldp2.model_validate({"systemCapabilities": None})

    assert lldp.model_dump(by_alias=True)["systemCapabilities"] == []


def test_non_array_array_value_still_fails() -> None:
    """Only null is coerced, other invalid values remain validation errors."""
    with pytest.raises(ValidationError) as exc_info:
        NetworksLldp2.model_validate({"systemCapabilities": 5})

    assert exc_info.value.errors()[0]["type"] == "list_type"
