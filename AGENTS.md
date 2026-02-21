# Agent Instructions

## Repository Purpose

This project provides a Python client for the Meraki Dashboard API.
The client is generated from Meraki's OpenAPI specification.

Key implications:

- All code in `meraki_client/` is generated.
- Generated tests live in `tests/generated/`.
- API reference docs under `docs/api_reference/` are generated.
- Source-of-truth for generation logic is in `codegen/`.

## Repository Map

- `codegen/`: generator implementation, templates, and spec overrides.
  - `main.py`: generation entry point.
  - `templates/`: Jinja2 templates for SDK, tests, and docs output.
  - `spec_overrides.toml`: OpenAPI workarounds and override config.
  - `static/`: files copied directly into generated output.
- `meraki_client/`: generated SDK package.
  - `_api/`: generated sync endpoint modules by scope.
  - `aio/_api/`: generated async endpoint modules by scope.
  - `schemas/`: generated response schemas.
- `tests/`: integration tests.
  - `tests/generated/`: generated API tests.
  - `tests/test_*.py`: manual tests.
- `docs/`: MkDocs content, including generated API reference pages.

## Environment and Tooling

- Python: Minimum version defined in `.python-version`.
- Package/dependency manager: `uv`.
- Lint/format: `ruff`.
- Type checking: `ty`.
- Docs: Zensical + mkdocstrings.

## Code Generation

This project uses code generation to create Python SDK from the Meraki Dashboard OpenAPI specification.

After making changes to codegen templates or logic, regenerate the SDK:

```bash
make generate
```

## Verification

To verify changes, run linters and type checking (never run tests unprompted):

```bash
make lint
```

## Changelog Updates

When making behavior changes, generated output changes, or user-visible fixes, update `CHANGELOG.md`.

- Add entries under `## Unreleased` in the appropriate section.
- Keep entries concise and describe impact (what changed for SDK users/maintainers).

Types of changes:

- `Added` for new functionality or features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## Spec Overrides Guidance

When adding new override functionality add a detection check that emits a warning when the spec appears fixed, so maintainers know the override may be obsolete.
