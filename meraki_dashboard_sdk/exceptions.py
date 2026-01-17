"""Exceptions for the SDK."""

from typing import Any

import httpx
import pydantic


class _ErrorResponse(pydantic.BaseModel):
    """Error response from the API."""

    errors: list[str]


class MerakiException(Exception):
    """Base exception for all Meraki API exceptions."""

    def __init__(self, *args: Any, cause: dict[str, Any] | Exception | None = None) -> None:
        """Initialize MerakiError with cause.

        Args:
            *args: Arguments to pass to the exception.
            cause: Exception that caused the exception if available.

        """
        self.cause: dict[str, Any] | Exception | None = cause
        super().__init__(*args)


class MerakiHTTPError(MerakiException):
    """Request failed due to an unexpected HTTP status."""

    def __init__(
        self,
        *args: Any,
        cause: dict[str, Any] | Exception | None = None,
        response: httpx.Response | None = None,
    ) -> None:
        """Initialize MerakiHTTPError with cause.

        Args:
            *args: Arguments to pass to the exception.
            cause: Exception that caused the exception if available.
            response: HTTP Response object.

        """
        self.cause: dict[str, Any] | Exception | None = cause
        self.response: httpx.Response | None = response
        self.status_code: int | None = None
        self.reason: str | None = None
        self.errors: list[str] | None = None

        if response:
            self.status_code = response.status_code
            self.reason = response.reason_phrase
            try:
                self.errors = _ErrorResponse.model_validate_json(response.text).errors
            except pydantic.ValidationError:
                self.errors = None
        super().__init__(*args, cause=cause)

    def __str__(self) -> str:
        """Return the exception message."""
        if self.errors:
            errors = "\n".join(self.errors)
            return f"{self.__class__.__name__}: {self.status_code} {self.reason}\n{errors}"
        return f"{self.__class__.__name__}: {self.status_code} {self.reason}"


class InvalidRequestError(MerakiHTTPError):
    """API returned HTTP status 400."""


class UnauthorizedError(MerakiHTTPError):
    """API returned HTTP status 401."""


class PermissionDeniedError(MerakiHTTPError):
    """API returned HTTP status 403."""


class ResourceNotFoundError(MerakiHTTPError):
    """API returned HTTP status 404."""


class RateLimitError(MerakiHTTPError):
    """API returned HTTP status 429."""


class ServerError(MerakiHTTPError):
    """API returned HTTP status 5xx."""


class InvalidResponseError(MerakiException):
    """Request to API failed due to an invalid response payload."""


class MerakiConnectionError(MerakiException):
    """Connection failed to the API."""


def raise_http_error(response: httpx.Response) -> MerakiHTTPError:
    """Raise the appropriate HTTP error based on the response."""
    match response.status_code:
        case 400:
            return InvalidRequestError(response=response)
        case 401:
            return UnauthorizedError(response=response)
        case 403:
            return PermissionDeniedError(response=response)
        case 404:
            return ResourceNotFoundError(response=response)
        case 429:
            return RateLimitError(response=response)
        case status if 500 <= status < 600:
            return ServerError(response=response)
        case _:
            return MerakiHTTPError(response=response)
