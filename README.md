# Python client for Meraki Dashboard API

Python client for the [Meraki Dashboard API](https://developer.cisco.com/meraki/api-v1/). Auto-generated from the OpenAPI spec to stay current with the latest releases.

**Installation:**

```shell
pip install meraki-client
```

## Features

- Modern Python 3.11+ with full type annotations
- Sync and async clients built on httpx
- Pydantic models for requests and responses
- Automatic retries and pagination
- Full API coverage ([auto-generated from OpenAPI](https://api.meraki.com/api/v1/openapiSpec))

## Setup

1. Enable API access in your Meraki dashboard organization and [obtain an API key](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/How-Tos/Cisco_Meraki_Dashboard_API)

2. Pass the API key to the client, or set it as an environment variable:

   ```python
   client = MerakiClient(api_key="YOUR_KEY_HERE")
   ```

   ```shell
   export MERAKI_DASHBOARD_API_KEY=YOUR_KEY_HERE
   ```

## Usage

API calls follow the pattern `client.<scope>.<operation>()`, where scope maps to the OpenAPI tags (e.g., `organizations`, `networks`, `devices`).

### Synchronous

```python
from meraki_client import MerakiClient

client = MerakiClient()
org = client.organizations.get_organization(org_id)
```

### Asynchronous

```python
from meraki_client.aio import AsyncMerakiClient

async with AsyncMerakiClient() as client:
    orgs = await client.organizations.get_organization(org_id)
```

### Pagination

Paginated endpoints return lazy iterators. Iterate directly or call `collect()` to fetch all pages:

```python
# Iterate page by page
for device in client.organizations.get_organization_devices(organization_id=org_id, total_pages="all"):
    print(device["name"])

# Or collect all results at once
devices = client.organizations.get_organization_devices(organization_id=org_id, total_pages="all").collect()
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, testing, and code generation instructions.

## Disclaimer

This is an unofficial community project, not affiliated with or endorsed by Cisco. For the official Meraki Python SDK, see [meraki/dashboard-api-python](https://github.com/meraki/dashboard-api-python). This project was forked from the official Meraki Python SDK.
