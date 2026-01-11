# Meraki Dashboard API Python SDK

Python client for the [Meraki Dashboard API](https://developer.cisco.com/meraki/api-v1/). Auto-generated from the OpenAPI spec to stay current with the latest releases.

**Installation:**

```shell
pip install meraki-dashboard-sdk
```

## Features

- Modern Python 3.10+ with full type annotations
- Sync and async clients built on httpx
- Pydantic models for requests and responses
- Automatic retries and pagination
- Full API coverage ([auto-generated from OpenAPI](https://api.meraki.com/api/v1/openapiSpec))

## Setup

1. Enable API access in your Meraki dashboard organization and [obtain an API key](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/How-Tos/Cisco_Meraki_Dashboard_API)

2. Pass the API key to the client, or set it as an environment variable:

   ```python
   dashboard = meraki.MerakiClient(api_key="YOUR_KEY_HERE")
   ```

   ```shell
   export MERAKI_DASHBOARD_API_KEY=YOUR_KEY_HERE
   ```

## Usage

```python
from meraki import MerakiClient

client = MerakiClient()
orgs = await client.organizations.get_organizations()
```

API calls follow the pattern `client.<scope>.<operation>()`, where scope maps to the OpenAPI tags (e.g., `organizations`, `networks`, `devices`).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Disclaimer

This is an unofficial community project, not affiliated with or endorsed by Cisco. For the official Meraki Python SDK, see [meraki/dashboard-api-python](https://github.com/meraki/dashboard-api-python). This project was forked from the official Meraki Python SDK.
