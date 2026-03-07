"""Shared utility functions for code generation."""

import json
import os
import re
import tomllib
from dataclasses import dataclass, field
from typing import Any

from codegen.constants import RESERVED_NAMES, SPEC_OVERRIDES_FILE

_LOWER_UPPER_RE = re.compile(r"([a-z0-9])([A-Z])")
_ACRONYM_RE = re.compile(r"([A-Z]+)([A-Z][a-z])")


def to_snake_case(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case, preserving acronyms."""
    name = _LOWER_UPPER_RE.sub(r"\1_\2", name)
    # Insert underscore between acronym and next word: VPNPeers -> VPN_Peers
    name = _ACRONYM_RE.sub(r"\1_\2", name)
    return name.lower()


def capitalize_first(name: str) -> str:
    """Capitalize the first character, leaving the rest unchanged."""
    return name[:1].upper() + name[1:] if name else ""


def escape_reserved_name(name: str) -> str:
    """Append underscore if name is a Python keyword or builtin."""
    return f"{name}_" if name in RESERVED_NAMES else name


def sanitize_text(text: str) -> str:
    """Clean up text from OpenAPI spec.

    - Replaces non-breaking spaces with regular spaces
    - Normalizes whitespace
    - Ensures text ends with a period
    """
    text = text.replace("\u00a0", " ").replace("\u2007", " ").replace("\u202f", " ")
    text = " ".join(text.split())
    if not text.endswith("."):
        text += "."
    return text


@dataclass
class SpecOverrides:
    """All spec overrides loaded from TOML configuration."""

    force_array_response: set[str] = field(default_factory=set)
    force_paginated: set[str] = field(default_factory=set)
    force_paginated_items_schema: set[str] = field(default_factory=set)
    optional_response: set[str] = field(default_factory=set)
    skip_tests: set[str] = field(default_factory=set)
    response_fields: dict[str, dict[str, str]] = field(default_factory=dict)
    required_fields: dict[str, set[str]] = field(default_factory=dict)
    extra_fields: dict[str, dict[str, str]] = field(default_factory=dict)
    inject_response_schema: dict[str, dict[str, Any]] = field(default_factory=dict)


def load_spec_overrides() -> SpecOverrides:
    """Load spec overrides from TOML configuration file."""
    if not os.path.exists(SPEC_OVERRIDES_FILE):
        return SpecOverrides()

    with open(SPEC_OVERRIDES_FILE, "rb") as f:
        data = tomllib.load(f)

    response_fields: dict[str, dict[str, str]] = {}
    required_fields: dict[str, set[str]] = {}
    extra_fields: dict[str, dict[str, str]] = {}
    inject_response_schema: dict[str, dict[str, Any]] = {}
    for key, value in data.items():
        if isinstance(value, dict):
            if "response" in value:
                response_fields[key] = value["response"]
            if "required" in value:
                required_fields[key] = set(value["required"])
            if "extra_fields" in value:
                extra_fields[key] = value["extra_fields"]
            if "inject_response_schema" in value:
                inject_response_schema[key] = json.loads(value["inject_response_schema"])

    return SpecOverrides(
        force_array_response=set(data.get("force_array_response", [])),
        force_paginated=set(data.get("force_paginated", [])),
        force_paginated_items_schema=set(data.get("force_paginated_items_schema", [])),
        optional_response=set(data.get("optional_response", [])),
        skip_tests=set(data.get("skip_tests", [])),
        response_fields=response_fields,
        required_fields=required_fields,
        extra_fields=extra_fields,
        inject_response_schema=inject_response_schema,
    )
