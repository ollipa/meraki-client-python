"""ActionBatchNac API endpoints."""

import urllib
from typing import Any


class ActionBatchNac:
    """ActionBatchNac class."""

    def __init__(self) -> None:
        pass

    def create_organization_nac_certificates_authorities_crl(
        self, organization_id: str, caId: str, content: str, isDelta: bool
    ) -> dict[str, Any]:
        """Create a new CRL (either base or delta) for an existing CA.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-certificates-authorities-crl

        Args:
            organization_id: Organization ID.
            caId: ID of the CRL issuer.
            content: CRL content in PEM format.
            isDelta: Whether it's a delta CRL or not.

        """
        kwargs = locals()

        metadata = {
            "tags": ["nac", "configure", "certificates", "authorities", "crls"],
            "operation": "create_organization_nac_certificates_authorities_crl",
        }
        organization_id = urllib.parse.quote(organization_id, safe="")
        resource = f"/organizations/{organization_id}/nac/certificates/authorities/crls"

        body_params = [
            "caId",
            "content",
            "isDelta",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {"resource": resource, "operation": "create", "body": payload}
        return action
