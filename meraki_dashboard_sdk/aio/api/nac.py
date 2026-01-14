"""Nac API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncNac:
    """Nac class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def create_organization_nac_certificates_authorities_crl(
        self, *, organization_id: str, ca_id: str, content: str, is_delta: bool
    ) -> dict[str, Any] | None:
        """Create a new CRL (either base or delta) for an existing CA.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-certificates-authorities-crl

        Args:
            organization_id: Organization ID.
            ca_id: ID of the CRL issuer.
            content: CRL content in PEM format.
            is_delta: Whether it's a delta CRL or not.

        """
        metadata = {
            "tags": ["nac", "configure", "certificates", "authorities", "crls"],
            "operation": "create_organization_nac_certificates_authorities_crl",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/nac/certificates/authorities/crls"

        payload = {}
        if ca_id is not None:
            payload["caId"] = ca_id
        if content is not None:
            payload["content"] = content
        if is_delta is not None:
            payload["isDelta"] = is_delta

        return self._session.post(metadata, resource, payload)
