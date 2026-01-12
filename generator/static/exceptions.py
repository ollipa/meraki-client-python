"""Exceptions for the SDK."""

import requests


class APIKeyError(Exception):
    """Exception raised for unsupported API key."""

    def __init__(self) -> None:
        self.message = "Meraki API key needs to be defined"
        super(self).__init__(self.message)

    def __repr__(self) -> str:
        return self.message


class APIResponseError(Exception):
    """Exception class raised from HTTP class methods.

    Used as a single catch-all error for any possible requests exception error that might happen
    during communication with Meraki API to simplify caller coding.
    """

    def __init__(self, obj_name: str, status_code: int, error_msg: str) -> None:
        self.obj_name = obj_name
        self.status_code = status_code
        self.reason = error_msg

    def exc_message(self) -> str:
        """Return the exception message."""
        return (
            f'HTTP call within object "{self.obj_name}" failed. Status code is "{self.status_code}". '
            f'Error message is: "{self.reason}".'
        )

    def json(self) -> dict[str, str]:
        """Return the exception message in JSON format."""
        return {"error": self.reason, "status_code": self.status_code}

    def __str__(self) -> str:
        return self.exc_message()


class APIError(Exception):
    """Exception raised for API errors."""

    def __init__(self, metadata: dict[str, str], response: requests.Response) -> None:
        """Initialize the APIError."""
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        self.status = (
            self.response.status_code
            if self.response is not None and self.response.status_code
            else None
        )
        self.reason = (
            self.response.reason if self.response is not None and self.response.reason else None
        )
        try:
            self.message = (
                self.response.json() if self.response is not None and self.response.json() else None
            )
        except ValueError:
            self.message = self.response.content[:100].decode("UTF-8").strip()
            if isinstance(self.message, str) and self.status == 404 and self.reason == "Not Found":
                self.message += "please wait a minute if the key or org was just newly created."
        super(self).__init__(
            f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
        )

    def __repr__(self) -> str:
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"


class AsyncAPIError(Exception):
    """Exception raised for asynchronous API errors."""

    def __init__(self, metadata: dict[str, str], response: requests.Response, message: str) -> None:
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        self.status = response.status if response is not None and response.status else None
        self.reason = response.reason if response is not None and response.reason else None
        self.message = message
        if isinstance(self.message, str):
            self.message = self.message.strip()
            if self.status == 404 and self.reason == "Not Found":
                self.message += "please wait a minute if the key or org was just newly created."

        super().__init__(
            f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
        )

    def __repr__(self) -> str:
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"


class SessionInputError(Exception):
    """Exception raised for unsupported session inputs."""

    def __init__(self, argument: str, value: str, message: str, doc_link: str) -> None:
        self.argument = argument
        self.value = value
        self.message = message
        self.doc_link = doc_link

        super().__init__(f"{self.message} {self.doc_link}")
