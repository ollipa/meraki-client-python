"""Nac API endpoints."""

from __future__ import annotations

import urllib.parse
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from meraki_client.session import Session


class Nac:
    """Nac class."""

    def __init__(self, session: Session) -> None:
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
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        path = f"/organizations/{organization_id}/nac/certificates/authorities/crls"

        payload = {}
        if ca_id is not None:
            payload["caId"] = ca_id
        if content is not None:
            payload["content"] = content
        if is_delta is not None:
            payload["isDelta"] = is_delta

        return self._session.post(
            scope="nac",
            operation_id="createOrganizationNacCertificatesAuthoritiesCrl",
            path=path,
            json=payload,
        )
