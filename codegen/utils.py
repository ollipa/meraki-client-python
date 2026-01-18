"""Shared utility functions for code generation."""


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
