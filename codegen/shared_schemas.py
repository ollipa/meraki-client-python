"""Generic schemas shared across all scopes.

Deduplicated schemas are otherwise named after the first operation or field that uses them,
so their names change whenever a new endpoint with the same structure appears earlier in the
spec. Small, generic structures get fixed names here instead.
"""

from dataclasses import dataclass
from typing import Any

SHARED_SCOPE = "shared"


@dataclass(frozen=True)
class SharedSchema:
    """A generic schema with a fixed class name."""

    name: str
    description: str
    schema: dict[str, Any]


def _object_schema(*, required: bool, **properties: str) -> dict[str, Any]:
    """Build an object schema with scalar properties, all required or all optional."""
    schema: dict[str, Any] = {
        "type": "object",
        "properties": {name: {"type": type_} for name, type_ in properties.items()},
    }
    if required:
        schema["required"] = list(properties)
    return schema


SHARED_SCHEMAS = (
    SharedSchema(
        name="SuccessResponse",
        description="Result of an operation.",
        schema=_object_schema(required=False, success="boolean"),
    ),
    SharedSchema(
        name="EnabledSetting",
        description="Setting that can be enabled or disabled.",
        schema=_object_schema(required=False, enabled="boolean"),
    ),
    SharedSchema(
        name="EnabledSettingStrict",
        description="Setting that can be enabled or disabled.",
        schema=_object_schema(required=True, enabled="boolean"),
    ),
    SharedSchema(
        name="IdRef",
        description="Reference to an object by ID.",
        schema=_object_schema(required=False, id="string"),
    ),
    SharedSchema(
        name="IdRefStrict",
        description="Reference to an object by ID.",
        schema=_object_schema(required=True, id="string"),
    ),
    SharedSchema(
        name="NameRef",
        description="Reference to an object by name.",
        schema=_object_schema(required=False, name="string"),
    ),
    SharedSchema(
        name="IdNameRef",
        description="Reference to an object by ID and name.",
        schema=_object_schema(required=False, id="string", name="string"),
    ),
    SharedSchema(
        name="IdNameRefStrict",
        description="Reference to an object by ID and name.",
        schema=_object_schema(required=True, id="string", name="string"),
    ),
)
