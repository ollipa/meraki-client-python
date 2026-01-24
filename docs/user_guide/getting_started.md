# Getting Started

## Installation

Install the package from PyPI:

```shell
pip install meraki-client
```

Or with [uv](https://docs.astral.sh/uv/):

```shell
uv add meraki-client
```

## API Key Setup

1. Enable API access in your Meraki dashboard organization
2. [Obtain an API key](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/How-Tos/Cisco_Meraki_Dashboard_API)

Pass the API key to the client directly:

```python
from meraki_client import MerakiClient

client = MerakiClient(api_key="YOUR_KEY_HERE")
```

Or set it as an environment variable:

```shell
export MERAKI_DASHBOARD_API_KEY=YOUR_KEY_HERE
```

## Basic Usage

### Synchronous Client

```python
from meraki_client import MerakiClient

client = MerakiClient()

# Get all organizations
orgs = client.organizations.get_organizations().collect()

# Get a specific organization
org = client.organizations.get_organization(organization_id="123456")

# Get networks in an organization
networks = client.organizations.get_organization_networks(
    organization_id="123456"
).collect()
```

### Asynchronous Client

```python
from meraki_client.aio import AsyncMerakiClient

async with AsyncMerakiClient() as client:
    orgs = await client.organizations.get_organizations().collect()

    org = await client.organizations.get_organization(
        organization_id="123456"
    )
```

## Working with Responses

### Typed Response Schemas

API responses are returned as typed Pydantic models with full IDE autocompletion and type checking:

```python
org = client.organizations.get_organization(organization_id="123456")

# Typed fields with autocompletion
print(org.id)
print(org.name)
```

### Accessing Extra Fields

The Meraki API sometimes returns fields that are not documented in the OpenAPI specification.
These fields are still accessible on response objects since schemas are configured to allow extra fields.

Use `model_extra` to access any fields not defined in the schema:

```python
ssids = client.wireless.get_network_wireless_ssids(network_id="N_123")

for ssid in ssids:
    # Access documented fields normally
    print(ssid.name, ssid.enabled)

    # Access undocumented fields via model_extra
    if ssid.model_extra:
        print("Extra fields:", ssid.model_extra)
```

You can also convert the response to a dictionary to access all fields:

```python
org = client.organizations.get_organization(organization_id="123456")

# Convert to dict including extra fields
org_dict = org.model_dump()
```
