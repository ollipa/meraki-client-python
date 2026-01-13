"""Licensing API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncLicensing:
    """Licensing class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_administered_licensing_subscription_entitlements(self) -> dict[str, Any] | None:
        """Retrieve the list of purchasable entitlements.

        https://developer.cisco.com/meraki/api-v1/#!get-administered-licensing-subscription-entitlements

        Args:
            skus: Filter to entitlements with the specified SKUs.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["licensing", "configure", "subscription", "entitlements"],
            "operation": "get_administered_licensing_subscription_entitlements",
        }
        resource = f"/administered/licensing/subscription/entitlements"

        query_params = [
            "skus",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "skus",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def get_administered_licensing_subscription_subscriptions(
        self, organizationIds: list, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List available subscriptions.

        https://developer.cisco.com/meraki/api-v1/#!get-administered-licensing-subscription-subscriptions

        Args:
            organizationIds: Organizations to get associated subscriptions for.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            subscriptionIds: List of subscription ids to fetch.
            statuses: List of statuses that returned subscriptions can have.
            productTypes: List of product types that returned subscriptions need to have
              entitlements for.
            skus: List of SKUs that returned subscriptions need to have entitlements for.
            name: Search for subscription name.
            startDate: Filter subscriptions by start date, ISO 8601 format. To filter with a range
              of dates, use 'startDate[<option>]=?' in the request. Accepted options
              include lt, gt, lte, gte.
            endDate: Filter subscriptions by end date, ISO 8601 format. To filter with a range of
              dates, use 'endDate[<option>]=?' in the request. Accepted options include
              lt, gt, lte, gte.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["licensing", "configure", "subscription", "subscriptions"],
            "operation": "get_administered_licensing_subscription_subscriptions",
        }
        resource = f"/administered/licensing/subscription/subscriptions"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "subscriptionIds",
            "organizationIds",
            "statuses",
            "productTypes",
            "skus",
            "name",
            "startDate",
            "endDate",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "subscriptionIds",
            "organizationIds",
            "statuses",
            "productTypes",
            "skus",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def claim_administered_licensing_subscription_subscriptions(
        self, claimKey: str, organizationId: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Claim a subscription into an organization.

        https://developer.cisco.com/meraki/api-v1/#!claim-administered-licensing-subscription-subscriptions

        Args:
            claimKey: The subscription's claim key.
            organizationId: The id of the organization claiming the subscription.
            validate: Check if the provided claim key is valid and can be claimed into the
              organization.
            name: Friendly name to identify the subscription.
            description: Extra details or notes about the subscription.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["licensing", "configure", "subscription", "subscriptions"],
            "operation": "claim_administered_licensing_subscription_subscriptions",
        }
        resource = f"/administered/licensing/subscription/subscriptions/claim"

        body_params = [
            "claimKey",
            "organizationId",
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def validate_administered_licensing_subscription_subscriptions_claim_key(
        self, claimKey: str
    ) -> dict[str, Any] | None:
        """Find a subscription by claim key.

        https://developer.cisco.com/meraki/api-v1/#!validate-administered-licensing-subscription-subscriptions-claim-key

        Args:
            claimKey: The subscription's claim key.

        """
        kwargs = locals()

        metadata = {
            "tags": ["licensing", "configure", "subscription", "subscriptions", "claimKey"],
            "operation": "validate_administered_licensing_subscription_subscriptions_claim_key",
        }
        resource = f"/administered/licensing/subscription/subscriptions/claimKey/validate"

        body_params = [
            "claimKey",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_administered_licensing_subscription_subscriptions_compliance_statuses(
        self, organizationIds: list, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Get compliance status for requested subscriptions.

        https://developer.cisco.com/meraki/api-v1/#!get-administered-licensing-subscription-subscriptions-compliance-statuses

        Args:
            organizationIds: Organizations to get subscription compliance information for.
            subscriptionIds: Subscription ids.

        """
        kwargs.update(locals())

        metadata = {
            "tags": [
                "licensing",
                "configure",
                "subscription",
                "subscriptions",
                "compliance",
                "statuses",
            ],
            "operation": "get_administered_licensing_subscription_subscriptions_compliance_statuses",
        }
        resource = f"/administered/licensing/subscription/subscriptions/compliance/statuses"

        query_params = [
            "organizationIds",
            "subscriptionIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "organizationIds",
            "subscriptionIds",
        ]
        for k in kwargs:
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    def bind_administered_licensing_subscription_subscription(
        self, subscription_id: str, **kwargs: Any
    ) -> dict[str, Any] | None:
        """Bind networks to a subscription.

        https://developer.cisco.com/meraki/api-v1/#!bind-administered-licensing-subscription-subscription

        Args:
            subscription_id: Subscription ID.
            validate: Check if the provided networks can be bound to the subscription. Returns any
              licensing problems and does not commit the results.
            networkIds: List of network ids to bind to the subscription.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["licensing", "configure", "subscription", "subscriptions"],
            "operation": "bind_administered_licensing_subscription_subscription",
        }
        subscription_id = urllib.parse.quote(str(subscription_id), safe="")
        resource = f"/administered/licensing/subscription/subscriptions/{subscription_id}/bind"

        body_params = [
            "networkIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def get_organization_licensing_coterm_licenses(
        self, organization_id: str, total_pages=1, direction="next", **kwargs: Any
    ) -> Generator[Any, None, None]:
        """List the licenses in a coterm organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-licensing-coterm-licenses

        Args:
            organization_id: Organization ID.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.
            perPage: The number of entries per page returned. Acceptable range is 3 - 1000. Default
              is 1000.
            startingAfter: A token used by the server to indicate the start of the page. Often this
              is a timestamp or an ID but it is not limited to those. This parameter
              should not be defined by client applications. The link for the first,
              last, prev, or next page in the HTTP Link header should define it.
            endingBefore: A token used by the server to indicate the end of the page. Often this is
              a timestamp or an ID but it is not limited to those. This parameter should
              not be defined by client applications. The link for the first, last, prev,
              or next page in the HTTP Link header should define it.
            invalidated: Filter for licenses that are invalidated.
            expired: Filter for licenses that are expired.

        """
        kwargs.update(locals())

        metadata = {
            "tags": ["licensing", "configure", "coterm", "licenses"],
            "operation": "get_organization_licensing_coterm_licenses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/licensing/coterm/licenses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "invalidated",
            "expired",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def move_organization_licensing_coterm_licenses(
        self, organization_id: str, destination: dict, licenses: list
    ) -> dict[str, Any] | None:
        """Moves a license to a different organization (coterm only).

        https://developer.cisco.com/meraki/api-v1/#!move-organization-licensing-coterm-licenses

        Args:
            organization_id: Organization ID.
            destination: Destination data for the license move.
            licenses: The list of licenses to move.

        """
        kwargs = locals()

        metadata = {
            "tags": ["licensing", "configure", "coterm", "licenses"],
            "operation": "move_organization_licensing_coterm_licenses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/licensing/coterm/licenses/move"

        body_params = [
            "destination",
            "licenses",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
