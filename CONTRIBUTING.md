# Contributing

## Development Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```shell
# Install dependencies
uv sync
```

## Code Generation

The SDK is auto-generated from Meraki's [OpenAPI specification](https://github.com/meraki/openapi). To regenerate the client code:

```shell
make generate
```

This command:

1. Downloads the OpenAPI spec for the specified version
2. Generates the `meraki_client` package with sync and async clients
3. Generates Pydantic response schemas
4. Generates integration tests in `tests/generated/`
5. Formats all generated code

See [meraki/openapi releases](https://github.com/meraki/openapi/tags) for available API versions. Generated API version can be changed in `.api-version` file.

### Project Structure

```
meraki_client/           # Generated client library
codegen/                 # Code generation
tests/
├── test_*.py            # Manual tests
└── generated/           # Auto-generated tests
```

### Spec Overrides

Some endpoints have bugs in the OpenAPI spec. Workarounds are configured in `codegen/spec_overrides.toml`. The generator validates that overrides reference existing operations and logs warnings when the spec appears fixed.

## Releasing

Releases go through a pull request; nothing is pushed to `main` directly.

1. On an up-to-date `main` with a clean working tree, run:

   ```shell
   uv run scripts/bump_version.py minor  # or major / patch
   ```

   This bumps the version, moves the `Unreleased` changelog entries under the new version heading, regenerates the SDK, and opens a `release/vX.Y.Z` pull request.

2. Review and merge the pull request.
3. The `Publish` workflow on `main` sees that the merge changed the version to one with no tag, builds the package, and waits for approval of the `pypi` environment. Approve the deployment in the workflow run to publish to PyPI. CI then creates the `vX.Y.Z` tag and GitHub release.

Notes:

- Only the push that changes the version releases; other merges while a release is pending don't publish. To retry a rejected or expired approval, re-run all jobs of the original workflow run. If tagging fails after the package was published, re-run the failed jobs.
- Don't create the tag or GitHub release by hand: CI then skips publishing without an error.

## Testing

Tests require a Meraki API key with access to an organization:

```shell
export MERAKI_DASHBOARD_API_KEY_TESTS=your_api_key
```

Optionally, specify test resources to avoid auto-discovery:

```shell
export ORGANIZATION_ID_TESTS=your_org_id
export NETWORK_ID_TESTS=your_network_id
export DEVICE_ID_TESTS=your_device_serial
```

### Running Tests

```shell
# Run read-only tests (safe)
make test

# Run mutating tests (creates/updates/deletes resources)
make test-mutating
```

### Writing Manual Tests

Manual tests for mutating operations should use the `mutating` marker:

```python
import pytest

pytestmark = pytest.mark.mutating

def test_create_network() -> None:
    # Test implementation
    ...
```

## Linting

```shell
# Run all checks (format, lint, typecheck, docs)
make lint
```

To auto-fix formatting issues:

```shell
uv run ruff format meraki_client codegen tests
uv run ruff check --fix meraki_client codegen tests
```

## Pull Requests

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `make lint` and `make test` (if possible)
5. Submit a pull request
