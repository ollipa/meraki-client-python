"""A script that generates the Meraki Python library using the public OpenAPI specification."""

import argparse
import asyncio
import os
import re
import shutil
import sys
import textwrap
from pathlib import Path
from typing import Any

import httpx
import jinja2
import tomllib

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = Path(SCRIPT_DIR).parent
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, "templates")
OUTPUT_DIR = "meraki_dashboard_sdk"

REVERSE_PAGINATION = ["getNetworkEvents", "getOrganizationConfigurationChanges"]
INDENT_WIDTH = 12
DOCSTRING_LINE_WIDTH = 100 - INDENT_WIDTH


def format_param_description(name: str, description: str) -> str:
    """Format a parameter description for Google-style docstring with line wrapping."""
    if not description.endswith("."):
        description += "."
    first_line = f"{name}: {description}"
    if len(first_line) <= DOCSTRING_LINE_WIDTH:
        return first_line

    # Wrap to multiple lines with 4-space continuation indent
    wrapper = textwrap.TextWrapper(
        width=DOCSTRING_LINE_WIDTH,
        initial_indent="",
        subsequent_indent=" " * (INDENT_WIDTH + 2),
    )
    return wrapper.fill(first_line)


def get_client_version() -> str:
    """Read the client version from pyproject.toml."""
    pyproject_path = PROJECT_ROOT / "pyproject.toml"
    with pyproject_path.open("rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["project"]["version"]


# Helper function to resolve $ref references in OASv3
def resolve_ref(spec: dict[str, Any], ref: str) -> dict[str, Any] | None:
    """Resolve a $ref reference in OASv3 spec.

    Example: #/components/schemas/Network -> spec['components']['schemas']['Network']
    """
    if not ref.startswith("#/"):
        return None

    parts = ref[2:].split("/")  # Remove '#/' and split
    result = spec
    for part in parts:
        if isinstance(result, dict) and part in result:
            result = result[part]
        else:
            return None
    return result


# Helper function to get schema from OASv3 parameter or requestBody
def get_schema_from_item(item: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any] | None:
    """Extract schema from an OASv3 parameter or requestBody content item.

    Handles both inline schemas and $ref references.
    """
    if "schema" in item:
        schema = item["schema"]
        # If it's a $ref, resolve it
        if "$ref" in schema:
            resolved = resolve_ref(spec, schema["$ref"])
            if resolved:
                return resolved
        return schema
    return None


def generate_pagination_parameters(operation: str) -> dict[str, dict[str, str]]:
    """Helper function to return pagination parameters depending on endpoint."""
    ret = {
        "total_pages": {
            "type": "integer or string",
            "description": (
                "use with perPage to get total results up "
                'to total_pages*perPage; -1 or "all" for all pages'
            ),
        },
        "direction": {
            "type": "string",
            "description": (
                'direction to paginate, either "next" or "prev" (default) page'
                if operation in REVERSE_PAGINATION
                else 'direction to paginate, either "next" (default) or "prev" page'
            ),
        },
    }
    if operation == "getNetworkEvents":
        ret["event_log_end_time"] = {
            "type": "string",
            "description": "ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, "
            "to retrieve events within a time window",
        }
    return ret


def docs_url(operation: str) -> str:
    """Returns full link to endpoint's documentation on Developer Hub."""
    base_url = "https://developer.cisco.com/meraki/api-v1/#!"
    ret = ""
    for letter in operation:
        if letter.islower():
            ret += letter
        else:
            ret += f"-{letter.lower()}"
    return base_url + ret


def to_snake_case(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case."""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def return_params(
    operation: str, params: dict[str, Any], param_filters: list[str]
) -> dict[str, Any]:
    """Helper function to return the right params; used in parse_params."""
    # Return parameters based on matching input filters
    if not param_filters:
        return params
    ret = {}
    if "required" in param_filters:
        ret.update({k: v for k, v in params.items() if v.get("required")})
    if "pagination" in param_filters:
        ret.update(generate_pagination_parameters(operation) if "perPage" in params else {})
    if "optional" in param_filters:
        ret.update({k: v for k, v in params.items() if "required" in v and not v["required"]})
    if "path" in param_filters:
        ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "path"})
    if "query" in param_filters:
        ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "query"})
    if "body" in param_filters:
        ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "body"})
    if "array" in param_filters:
        ret.update({k: v for k, v in params.items() if "in" in v and v["type"] == "array"})
    if "enum" in param_filters:
        ret.update({k: v for k, v in params.items() if "enum" in v})
    return ret


def parse_request_body(request_body: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    """Parse requestBody from OASv3 specification.

    In OASv3, requestBody has a 'content' object with media types (e.g., 'application/json').
    """
    if not request_body:
        return {}

    params = {}

    # OASv3 requestBody has a 'content' object
    if "content" in request_body:
        # Usually we want application/json
        content = request_body["content"]
        json_content = content.get("application/json", {})

        if json_content:
            schema = get_schema_from_item(json_content, spec)
            if schema and "properties" in schema:
                # Get required fields from schema
                required_fields = schema.get("required", [])

                # Parse each property
                for prop_name, prop_schema in schema["properties"].items():
                    # Resolve $ref if present
                    if "$ref" in prop_schema:
                        resolved = resolve_ref(spec, prop_schema["$ref"])
                        if resolved:
                            prop_schema = resolved  # noqa: PLW2901

                    params[prop_name] = {
                        "required": prop_name in required_fields,
                        "in": "body",
                        "type": prop_schema.get("type", "object"),
                        "description": prop_schema.get("description", ""),
                    }

                    # Handle enum
                    if "enum" in prop_schema:
                        params[prop_name]["enum"] = prop_schema["enum"]

                    # Handle array type
                    if prop_schema.get("type") == "array":
                        params[prop_name]["type"] = "array"
                        if "items" in prop_schema:
                            items = prop_schema["items"]
                            if "$ref" in items:
                                resolved = resolve_ref(spec, items["$ref"])
                                if resolved:
                                    params[prop_name]["items"] = resolved

    return params


def parse_params(
    operation: str,
    parameters: list[dict[str, Any]],
    request_body: dict[str, Any],
    spec: dict[str, Any],
    param_filters: list[str] | None = None,
) -> dict[str, Any]:
    """Parse parameters from OASv3 specification.

    In OASv3, body parameters are in requestBody, not in parameters with in='body'.
    """
    if param_filters is None:
        param_filters = []

    # Create dict with information on endpoint's parameters
    params = {}

    # Parse path and query parameters (these are still in 'parameters')
    if parameters:
        for p in parameters:
            name = p["name"]
            param_in = p.get("in", "query")  # 'path', 'query', 'header', 'cookie'

            # Get schema (OASv3 uses 'schema' directly, not nested in 'schema.properties')
            schema = get_schema_from_item(p, spec)

            if schema:
                # OASv3: schema is directly on the parameter, not nested
                param_type = schema.get("type", "string")

                params[name] = {
                    "required": p.get("required", False),
                    "in": param_in,
                    "type": param_type,
                    "description": schema.get("description", p.get("description", "")),
                }

                # Handle enum
                if "enum" in schema:
                    params[name]["enum"] = schema["enum"]

                # Handle array type
                if param_type == "array" and "items" in schema:
                    items = schema["items"]
                    if "$ref" in items:
                        resolved = resolve_ref(spec, items["$ref"])
                        if resolved:
                            params[name]["items"] = resolved
            else:
                # Fallback: use parameter directly if no schema
                params[name] = {
                    "required": p.get("required", False),
                    "in": param_in,
                    "type": p.get("type", "string"),
                    "description": p.get("description", ""),
                }
                if "enum" in p:
                    params[name]["enum"] = p["enum"]

    # Parse requestBody (OASv3 specific)
    if request_body:
        body_params = parse_request_body(request_body, spec)
        params.update(body_params)

    # Add custom library parameters to handle pagination
    if "perPage" in params:
        params.update(generate_pagination_parameters(operation))

    # Return parameters based on matching input filters
    return return_params(operation, params, param_filters)


async def generate_library(spec: dict[str, Any], version_number: str, api_version: str) -> None:  # noqa: PLR0912, PLR0915
    """Generate the Meraki Python library using the public OpenAPI specification."""
    # Supported scopes list will include organizations, networks, devices, and all product types.
    supported_scopes = [
        "organizations",
        "networks",
        "devices",
        "appliance",
        "camera",
        "cellularGateway",
        "insight",
        "sm",
        "switch",
        "wireless",
        "sensor",
        "administered",
        "licensing",
        "secureConnect",
        "campusGateway",
        "nac",
        "spaces",
        "wirelessController",
    ]
    tags = spec["tags"]
    paths = spec["paths"]
    # Scopes used when generating the library will depend on the provided version of the API spec.
    scopes = {tag["name"]: {} for tag in tags if tag["name"] in supported_scopes}

    batchable_action_summaries = [action["summary"] for action in spec["x-batchable-actions"]]

    # Delete output directory and recreate it
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    subdirs = [
        OUTPUT_DIR,
        f"{OUTPUT_DIR}/api",
        f"{OUTPUT_DIR}/api/batch",
        f"{OUTPUT_DIR}/aio",
        f"{OUTPUT_DIR}/aio/api",
    ]
    for directory in subdirs:
        os.makedirs(directory, exist_ok=True)

    # Copy static files from generator/static/
    static_dir = os.path.join(SCRIPT_DIR, "static")
    non_generated = [
        "__init__.py",
        "config.py",
        "exceptions.py",
        "common.py",
        "response_handler.py",
        "rest_session.py",
        "api/__init__.py",
        "aio/__init__.py",
        "aio/rest_session.py",
        "aio/api/__init__.py",
        "api/batch/__init__.py",
    ]
    for file in non_generated:
        src = os.path.join(static_dir, file)
        dst = os.path.join(OUTPUT_DIR, file)
        shutil.copy2(src, dst)

        # Update versions in __init__.py
        if file == "__init__.py":
            with open(dst, encoding="utf-8") as f:  # noqa: ASYNC230
                contents = f.read()
            # Update __version__
            start = contents.find("__version__ = ")
            end = contents.find("\n", start)
            contents = f"{contents[:start]}__version__ = '{version_number}'{contents[end:]}"
            # Update __api_version__
            start = contents.find("__api_version__ = ")
            end = contents.find("\n", start)
            contents = f"{contents[:start]}__api_version__ = '{api_version}'{contents[end:]}"
            with open(dst, "w", encoding="utf-8") as f:  # noqa: ASYNC230
                f.write(contents)

    # Organize data from OpenAPI specification
    operations = []  # list of operation IDs
    for path, methods in paths.items():
        # method is the HTTP action, e.g. get, put, etc.
        for method in methods:
            # endpoint is the method for that specific path
            endpoint = methods[method]

            # the endpoint has tags
            tags = endpoint["tags"]

            # the endpoint has an operationId
            operation = endpoint["operationId"]

            # add the operation ID to the list
            operations.append(operation)

            # the endpoint has a scope defined by the first tag
            scope = tags[0]

            # Needs documentation
            if path not in scopes[scope]:
                scopes[scope][path] = {method: endpoint}
            # Needs documentation
            else:
                scopes[scope][path][method] = endpoint

    # Inform the user of the number of operations found
    print(f"Total of {len(operations)} endpoints found from OpenAPI spec...")

    # Generate API libraries
    # We will use newline=None to ensure that line breaks are handled correctly,
    # especially when generating on Windows and using git autocrlf true
    jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)  # noqa: S701

    # Iterate through the scopes creating standard, asyncio and batch modules for each
    for scope, section in scopes.items():
        print(f"...generating {scope}")
        module_name = to_snake_case(scope)

        # Generate the standard module
        with open(  # noqa: ASYNC230
            f"{OUTPUT_DIR}/api/{module_name}.py", "w", encoding="utf-8", newline=None
        ) as output:
            with open(  # noqa: ASYNC230
                os.path.join(TEMPLATE_DIR, "class_template.jinja2"),
                encoding="utf-8",
                newline=None,
            ) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                output.write(
                    template.render(
                        class_name=scope[0].upper() + scope[1:],
                    )
                )

            # Generate Asyncio API libraries
            async_output = open(  # noqa: ASYNC230, SIM115
                f"{OUTPUT_DIR}/aio/api/{module_name}.py", "w", encoding="utf-8", newline=None
            )
            with open(  # noqa: ASYNC230
                os.path.join(TEMPLATE_DIR, "async_class_template.jinja2"),
                encoding="utf-8",
                newline=None,
            ) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                async_output.write(
                    template.render(
                        class_name=scope[0].upper() + scope[1:],
                    )
                )

            # Generate Action Batch API libraries
            batch_output = open(  # noqa: ASYNC230, SIM115
                f"{OUTPUT_DIR}/api/batch/{module_name}.py",
                "w",
                encoding="utf-8",
                newline=None,
            )
            with open(  # noqa: ASYNC230
                os.path.join(TEMPLATE_DIR, "batch_class_template.jinja2"),
                encoding="utf-8",
                newline=None,
            ) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                batch_output.write(template.render(class_name=scope[0].upper() + scope[1:]))

            # Generate API & Asyncio API functions
            for path, methods in section.items():
                for method, endpoint in methods.items():
                    # Get metadata
                    tags = endpoint["tags"]
                    operation = endpoint["operationId"]
                    description = str(endpoint["summary"])
                    if not description.endswith("."):
                        description += "."

                    # OASv3: parameters are for path/query/header/cookie, requestBody is separate
                    parameters = endpoint.get("parameters", None)
                    request_body = endpoint.get("requestBody", None)

                    # Function definition
                    definition = ""
                    parsed_params = parse_params(
                        operation, parameters, request_body, spec, "required"
                    )
                    if parsed_params:
                        for p, values in parsed_params.items():
                            if values["type"] == "array":
                                definition += f", {p}: list"
                            elif values["type"] == "number":
                                definition += f", {p}: float"
                            elif values["type"] == "integer":
                                definition += f", {p}: int"
                            elif values["type"] == "boolean":
                                definition += f", {p}: bool"
                            elif values["type"] == "object":
                                definition += f", {p}: dict"
                            elif values["type"] == "string":
                                definition += f", {p}: str"

                        all_parsed_params = parse_params(operation, parameters, request_body, spec)
                        if "perPage" in all_parsed_params:
                            if operation in REVERSE_PAGINATION:
                                definition += ", total_pages=1, direction='prev'"
                            else:
                                definition += ", total_pages=1, direction='next'"
                            if operation == "getNetworkEvents":
                                definition += ", event_log_end_time=None"

                        optional_params = parse_params(
                            operation, parameters, request_body, spec, ["optional"]
                        )
                        if optional_params:
                            definition += ", **kwargs: Any"

                    # Docstring
                    param_descriptions = []
                    all_params = parse_params(
                        operation,
                        parameters,
                        request_body,
                        spec,
                        ["required", "pagination", "optional"],
                    )
                    if all_params:
                        for p, values in all_params.items():
                            param_descriptions.append(
                                format_param_description(p, values["description"])
                            )

                    # Combine keyword args with locals
                    kwarg_line = ""
                    optional_params = parse_params(
                        operation, parameters, request_body, spec, ["optional"]
                    )
                    if optional_params:
                        kwarg_line = "kwargs.update(locals())"
                    else:
                        query_body_array = parse_params(
                            operation,
                            parameters,
                            request_body,
                            spec,
                            ["query", "array", "body"],
                        )
                        if query_body_array:
                            kwarg_line = "kwargs = locals()"

                    # Assert valid values for enum
                    enum_params = parse_params(operation, parameters, request_body, spec, ["enum"])
                    assert_blocks = []
                    if enum_params:
                        for p, values in enum_params.items():
                            assert_blocks.append((p, values["enum"]))

                    # Function body for GET endpoints
                    query_params = array_params = body_params = path_params = {}
                    is_paginated = False
                    if method == "get":
                        query_params = parse_params(
                            operation, parameters, request_body, spec, "query"
                        )
                        array_params = parse_params(
                            operation, parameters, request_body, spec, "array"
                        )
                        path_params = parse_params(
                            operation, parameters, request_body, spec, "path"
                        )
                        pagination_params = parse_params(
                            operation, parameters, request_body, spec, "pagination"
                        )
                        if query_params or array_params:
                            if pagination_params:
                                is_paginated = True
                                if operation == "getNetworkEvents":
                                    call_line = (
                                        "return self._session.get_pages"
                                        "(metadata, resource, params, "
                                        "total_pages, direction, event_log_end_time)"
                                    )
                                else:
                                    call_line = (
                                        "return self._session.get_pages"
                                        "(metadata, resource, params, "
                                        "total_pages, direction)"
                                    )
                            else:
                                call_line = "return self._session.get(metadata, resource, params)"
                        else:
                            call_line = "return self._session.get(metadata, resource)"

                    # Function body for POST/PUT endpoints
                    elif method in ["post", "put"]:
                        body_params = parse_params(
                            operation, parameters, request_body, spec, "body"
                        )
                        path_params = parse_params(
                            operation, parameters, request_body, spec, "path"
                        )
                        if body_params:
                            call_line = (
                                f"return self._session.{method}(metadata, resource, payload)"
                            )
                        else:
                            call_line = f"return self._session.{method}(metadata, resource)"

                    # Function body for DELETE endpoints
                    elif method == "delete":
                        path_params = parse_params(
                            operation, parameters, request_body, spec, "path"
                        )
                        call_line = "return self._session.delete(metadata, resource)"
                    else:
                        raise ValueError(f"Unsupported method: {method}")

                    # Determine return type
                    if method == "delete":
                        return_type = "None"
                    elif method == "get" and is_paginated:
                        return_type = "Generator[Any, None, None]"
                    else:
                        return_type = "dict[str, Any] | None"

                    # Add function to files
                    with open(  # noqa: ASYNC230
                        os.path.join(TEMPLATE_DIR, "function_template.jinja2"),
                        encoding="utf-8",
                        newline=None,
                    ) as fp:
                        function_template = fp.read()
                        template = jinja_env.from_string(function_template)
                        output.write(
                            "\n\n"
                            + template.render(
                                operation=to_snake_case(operation),
                                function_definition=definition,
                                description=description,
                                doc_url=docs_url(operation),
                                descriptions=param_descriptions,
                                kwarg_line=kwarg_line,
                                all_params=list(all_params.keys()),
                                assert_blocks=assert_blocks,
                                tags=tags,
                                resource=path,
                                query_params=query_params,
                                array_params=array_params,
                                body_params=body_params,
                                path_params=path_params,
                                call_line=call_line,
                                return_type=return_type,
                            )
                        )
                        async_output.write(
                            "\n\n"
                            + template.render(
                                operation=to_snake_case(operation),
                                function_definition=definition,
                                description=description,
                                doc_url=docs_url(operation),
                                descriptions=param_descriptions,
                                kwarg_line=kwarg_line,
                                all_params=list(all_params.keys()),
                                assert_blocks=assert_blocks,
                                tags=tags,
                                resource=path,
                                query_params=query_params,
                                array_params=array_params,
                                body_params=body_params,
                                path_params=path_params,
                                call_line=call_line,
                                return_type=return_type,
                            )
                        )

            # Generate API action batch functions
            for path, methods in section.items():
                for method, endpoint in methods.items():
                    if endpoint["description"] in batchable_action_summaries:
                        # Get metadata
                        tags = endpoint["tags"]
                        operation = endpoint["operationId"]
                        description = str(endpoint["summary"])
                        if not description.endswith("."):
                            description += "."

                        # OASv3: parameters are for path/query/header/cookie
                        # and requestBody is separate
                        parameters = endpoint.get("parameters", None)
                        request_body = endpoint.get("requestBody", None)

                        # Function definition
                        definition = ""
                        parsed_params = parse_params(
                            operation, parameters, request_body, spec, "required"
                        )
                        if parsed_params:
                            for p, values in parsed_params.items():
                                if values["type"] == "array":
                                    definition += f", {p}: list"
                                elif values["type"] == "number":
                                    definition += f", {p}: float"
                                elif values["type"] == "integer":
                                    definition += f", {p}: int"
                                elif values["type"] == "boolean":
                                    definition += f", {p}: bool"
                                elif values["type"] == "object":
                                    definition += f", {p}: dict"
                                elif values["type"] == "string":
                                    definition += f", {p}: str"

                            all_parsed_params = parse_params(
                                operation, parameters, request_body, spec
                            )
                            if "perPage" in all_parsed_params:
                                if operation in REVERSE_PAGINATION:
                                    definition += ", total_pages=1, direction='prev'"
                                else:
                                    definition += ", total_pages=1, direction='next'"
                                if operation == "getNetworkEvents":
                                    definition += ", event_log_end_time=None"

                            optional_params = parse_params(
                                operation, parameters, request_body, spec, ["optional"]
                            )
                            if optional_params:
                                definition += ", **kwargs: Any"

                        # Docstring
                        param_descriptions = []
                        all_params = parse_params(
                            operation,
                            parameters,
                            request_body,
                            spec,
                            ["required", "pagination", "optional"],
                        )
                        if all_params:
                            for p, values in all_params.items():
                                param_descriptions.append(
                                    format_param_description(p, values["description"])
                                )

                        # Combine keyword args with locals
                        kwarg_line = ""
                        optional_params = parse_params(
                            operation, parameters, request_body, spec, ["optional"]
                        )
                        if optional_params:
                            kwarg_line = "kwargs.update(locals())"
                        else:
                            query_body_array = parse_params(
                                operation,
                                parameters,
                                request_body,
                                spec,
                                ["query", "array", "body"],
                            )
                            if query_body_array:
                                kwarg_line = "kwargs = locals()"

                        # Assert valid values for enum
                        enum_params = parse_params(
                            operation, parameters, request_body, spec, ["enum"]
                        )
                        assert_blocks = []
                        if enum_params:
                            for p, values in enum_params.items():
                                assert_blocks.append((p, values["enum"]))

                        # Function body for GET endpoints
                        query_params = array_params = body_params = {}

                        # Function body for POST/PUT endpoints
                        if method in {"post", "put"}:
                            body_params = parse_params(
                                operation, parameters, request_body, spec, "body"
                            )
                            batch_operation = "create" if method == "post" else "update"

                        # Function body for DELETE endpoints
                        elif method == "delete":
                            batch_operation = "destroy"
                        else:
                            raise ValueError(f"Unsupported method: {method}")

                        # Function return statement
                        call_line = "return action"

                        # Add function to files
                        with open(  # noqa: ASYNC230
                            os.path.join(TEMPLATE_DIR, "batch_function_template.jinja2"),
                            encoding="utf-8",
                            newline=None,
                        ) as fp:
                            function_template = fp.read()
                            template = jinja_env.from_string(function_template)
                            batch_output.write(
                                "\n\n"
                                + template.render(
                                    operation=to_snake_case(operation),
                                    function_definition=definition,
                                    description=description,
                                    doc_url=docs_url(operation),
                                    descriptions=param_descriptions,
                                    kwarg_line=kwarg_line,
                                    all_params=list(all_params.keys()),
                                    assert_blocks=assert_blocks,
                                    tags=tags,
                                    resource=path,
                                    query_params=query_params,
                                    array_params=array_params,
                                    body_params=body_params,
                                    call_line=call_line,
                                    batch_operation=batch_operation,
                                )
                            )


async def main() -> None:
    """Main function to parse command line arguments and generate the library."""
    parser = argparse.ArgumentParser(
        description="Generate the Meraki Python library using the public OpenAPI specification."
    )
    parser.add_argument(
        "-v",
        "--version",
        dest="api_version",
        required=True,
        help="API version tag to use (e.g., v1.66.0)",
    )
    args = parser.parse_args()

    api_version = str(args.api_version)
    if not api_version.startswith("v"):
        api_version = f"v{api_version}"

    client_version = get_client_version()
    print(f"Client version: {client_version}")
    print(f"API version: {api_version}")

    # Retrieve OpenAPI specification
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                "https://raw.githubusercontent.com/meraki/openapi"
                f"/refs/tags/{api_version}/openapi/spec3.json"
            )
            response.raise_for_status()
        except httpx.HTTPError as e:
            sys.exit(f"Error retrieving OpenAPI specification: {e}")

    await generate_library(response.json(), client_version, api_version)


if __name__ == "__main__":
    asyncio.run(main())
