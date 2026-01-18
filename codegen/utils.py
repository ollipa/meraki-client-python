"""Shared utility functions for code generation."""

import re

from codegen.constants import RESERVED_NAMES

_CAMEL_TO_SNAKE_RE = re.compile(r"(?<!^)(?=[A-Z])")


def to_snake_case(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case."""
    return _CAMEL_TO_SNAKE_RE.sub("_", name).lower()


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
