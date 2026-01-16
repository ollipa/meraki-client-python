"""A script that generates the Meraki Python library using the public OpenAPI specification."""

import argparse
import json
import logging
import os
import re
import shutil
import sys
import textwrap
import tomllib
from pathlib import Path
from typing import Any, Literal, TypeVar, assert_never
from urllib.parse import unquote

import httpx
import jinja2
from openapi_pydantic.v3.v3_0 import (
    DataType,
    OpenAPI,
    Operation,
    Parameter,
    ParameterLocation,
    Reference,
    RequestBody,
    Schema,
)
from pydantic import BaseModel

from generator.schemas import BatchableAction

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("codegen")

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = Path(SCRIPT_DIR).parent
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, "templates")
OUTPUT_DIR = "meraki_dashboard_sdk"

REVERSE_PAGINATION = ["getNetworkEvents", "getOrganizationConfigurationChanges"]
INDENT_WIDTH = 12
DOCSTRING_LINE_WIDTH = 100 - INDENT_WIDTH

# Python keywords and builtins that cannot be used as parameter names
RESERVED_NAMES = {
    # Keywords
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
    # Commonly problematic builtins
    "type",
    "id",
    "list",
    "dict",
    "set",
    "str",
    "int",
    "float",
    "bool",
    "object",
    "filter",
    "format",
    "hash",
    "input",
    "open",
    "range",
    "zip",
}


def main() -> None:
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
    log.info(f"Client version: {client_version}")
    log.info(f"API version: {api_version}")

    spec = get_openapi_specification(api_version)
    batchable_actions = [
        BatchableAction.model_validate(action) for action in spec["x-batchable-actions"]
    ]
    generate_library(OpenAPI.model_validate(spec), batchable_actions, client_version, api_version)


def get_client_version() -> str:
    """Read the client version from pyproject.toml."""
    pyproject_path = PROJECT_ROOT / "pyproject.toml"
    with pyproject_path.open("rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["project"]["version"]


def get_openapi_specification(api_version: str) -> dict[str, Any]:
    """Retrieve the OpenAPI specification from GitHub repository.

    Caches the specification locally to avoid unnecessary network requests.

    Args:
        api_version: The API version to retrieve the specification for.

    Returns:
        The OpenAPI specification as a dictionary.

    """
    spec_path = PROJECT_ROOT / ".cache" / f"spec-{api_version}.json"
    if spec_path.exists():
        log.info("Using cached OpenAPI specification")
        with spec_path.open("r") as f:
            return json.load(f)

    spec_path.parent.mkdir(parents=True, exist_ok=True)

    log.info("Downloading OpenAPI specification from GitHub repository")
    try:
        with httpx.stream(
            "GET",
            f"https://raw.githubusercontent.com/meraki/openapi/refs/tags/{api_version}/openapi/spec3.json",
        ) as response:
            response.raise_for_status()
            with spec_path.open("w") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk.decode("utf-8"))
    except httpx.HTTPError as e:
        sys.exit(f"Error retrieving OpenAPI specification: {e}")

    return json.load(spec_path.open("r"))


def generate_library(  # noqa: PLR0915
    spec: OpenAPI, batchable_actions: list[BatchableAction], version_number: str, api_version: str
) -> None:
    """Generate the Meraki Python library using the public OpenAPI specification."""
    batchable_action_summaries = [action.summary for action in batchable_actions]

    recreate_output_directory()
    copy_static_files(version_number, api_version)

    # Collect all operations by scope
    scopes: dict[
        str,
        dict[
            str,
            dict[
                Literal["get", "put", "post", "delete", "patch"],
                Operation,
            ],
        ],
    ] = {}
    operation_count = 0
    for path, path_item in spec.paths.items():
        operations: dict[
            Literal["get", "put", "post", "delete", "patch", "options", "head", "trace"],
            Operation | None,
        ] = {
            "get": path_item.get,
            "put": path_item.put,
            "post": path_item.post,
            "delete": path_item.delete,
            "patch": path_item.patch,
            "options": path_item.options,
            "head": path_item.head,
            "trace": path_item.trace,
        }
        for method, operation in operations.items():
            if not operation:
                continue
            if method in ["options", "head", "trace"]:
                log.warning(f"Unsupported method: {method} for path: {path}")
                continue
            # First tag is the scope
            scope = operation.tags[0] if operation.tags else None
            if not scope:
                log.warning(f"Path {path} has no tags")
                continue
            scopes.setdefault(scope, {}).setdefault(path, {})[method] = operation
            operation_count += 1

    log.info(
        f"Total of {len(scopes)} scopes and {operation_count} operations found from OpenAPI spec"
    )

    jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)  # noqa: S701

    # Iterate through the scopes creating standard, asyncio and batch modules for each
    for scope, paths in scopes.items():
        log.info(f"...generating {scope}")
        module_name = to_snake_case(scope)

        # Generate the standard module
        with open(
            f"{OUTPUT_DIR}/api/{module_name}.py", "w", encoding="utf-8", newline=None
        ) as output:
            with open(
                os.path.join(TEMPLATE_DIR, "class_template.jinja2"),
                encoding="utf-8",
                newline=None,
            ) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                output.write(
                    template.render(
                        class_name=scope[:1].upper() + scope[1:],
                    )
                )

            # Generate Asyncio API libraries
            async_output = open(  # noqa:  SIM115
                f"{OUTPUT_DIR}/aio/api/{module_name}.py", "w", encoding="utf-8", newline=None
            )
            with open(
                os.path.join(TEMPLATE_DIR, "async_class_template.jinja2"),
                encoding="utf-8",
                newline=None,
            ) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                async_output.write(
                    template.render(
                        class_name=scope[:1].upper() + scope[1:],
                    )
                )

            # Generate Action Batch API libraries
            batch_output = open(  # noqa:  SIM115
                f"{OUTPUT_DIR}/api/batch/{module_name}.py",
                "w",
                encoding="utf-8",
                newline=None,
            )
            with open(
                os.path.join(TEMPLATE_DIR, "batch_class_template.jinja2"),
                encoding="utf-8",
                newline=None,
            ) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                batch_output.write(template.render(class_name=scope[:1].upper() + scope[1:]))

            # Generate API & Asyncio API functions
            for path, methods in paths.items():
                for method, endpoint in methods.items():
                    tags = endpoint.tags or []
                    operation_id = endpoint.operationId
                    if not operation_id:
                        log.warning(f"Operation ID is missing for path: {path}")
                        continue

                    description = sanitize_description(str(endpoint.summary))
                    parameters = endpoint.parameters or []
                    request_body = endpoint.requestBody
                    if isinstance(request_body, Reference):
                        request_body = resolve_ref(spec, request_body, RequestBody)
                        if not request_body:
                            log.warning(f"Failed to resolve request body reference: {request_body}")
                            continue

                    # Resource path - convert all path params to snake_case
                    resource_path = convert_path_params(path)

                    param_descriptions: list[str] = []

                    # Function definition construction
                    positional_args: list[str] = []
                    keyword_args: list[str] = []
                    query_params: list[tuple[str, str]] = []  # list of (snake, orig)
                    path_params: list[str] = []
                    assert_blocks: list[tuple[str, list[str]]] = []  # list of (snake, options)

                    is_paginated = False
                    for param in parameters:
                        if isinstance(param, Reference):
                            param = resolve_ref(spec, param, Parameter)  # noqa: PLW2901
                            if not param:
                                log.warning(f"Failed to resolve parameter reference: {param}")
                                continue

                        name = param.name
                        snake_name = sanitize_param_name(to_snake_case(param.name))

                        param_schema = param.param_schema
                        if not param_schema:
                            log.warning(f"No schema found for parameter: {param.name}")
                            continue
                        if isinstance(param_schema, Reference):
                            param_schema = resolve_ref(spec, param_schema, Schema)
                            if not param_schema:
                                log.warning(f"Failed to resolve schema reference: {param_schema}")
                                continue

                        py_type = get_python_type(param_schema.type or DataType.STRING)

                        # Add to params maps
                        if param.param_in == ParameterLocation.QUERY:
                            key = name
                            if param_schema.type == DataType.ARRAY:
                                key += "[]"  # TODO: Check what this does
                            query_params.append((snake_name, key))
                        elif param.param_in == ParameterLocation.PATH:
                            path_params.append(snake_name)

                        # Add description
                        param_descriptions.append(
                            format_param_description(
                                snake_name, param.description or param_schema.description or ""
                            )
                        )

                        if snake_name == "per_page":
                            is_paginated = True

                        # Add to signature
                        if param.required or param.param_in == ParameterLocation.PATH:
                            positional_args.append(f"{snake_name}: {py_type}")
                        else:
                            # Optional
                            default_val = "None"
                            type_annot = f"{py_type} | None"
                            # Handle pagination defaults
                            if snake_name == "total_pages":
                                default_val = "1"
                                type_annot = py_type
                            elif snake_name == "direction":
                                default_val = (
                                    "'prev'" if operation_id in REVERSE_PAGINATION else "'next'"
                                )
                                type_annot = py_type

                            keyword_args.append(f"{snake_name}: {type_annot} = {default_val}")
                        if param_schema.enum:
                            assert_blocks.append((snake_name, param_schema.enum))

                    body_params: list[tuple[str, str]] = []  # list of (snake, orig)

                    # TODO: Move this to a function
                    if request_body:
                        json_content = request_body.content.get("application/json")
                        if not json_content:
                            raise ValueError(
                                f"No JSON content found for request body: {request_body}"
                            )
                        content_schema = json_content.media_type_schema
                        if not content_schema:
                            raise ValueError(f"No schema found for request body: {request_body}")
                        if isinstance(content_schema, Reference):
                            content_schema = resolve_ref(spec, content_schema, Schema)
                            if not content_schema:
                                raise ValueError(
                                    f"Failed to resolve schema reference: {content_schema}"
                                )
                        properties = content_schema.properties or {}
                        for property_name, property_schema in properties.items():
                            snake_name = sanitize_param_name(to_snake_case(property_name))
                            if isinstance(property_schema, Reference):
                                property_schema = resolve_ref(spec, property_schema, Schema)  # noqa: PLW2901
                                if not property_schema:
                                    raise ValueError(
                                        f"Failed to resolve schema reference: {property_schema}"
                                    )
                            if property_schema.type == DataType.ARRAY:
                                body_params.append(
                                    (
                                        snake_name,
                                        property_name,
                                    )
                                )
                            else:
                                body_params.append(
                                    (
                                        snake_name,
                                        property_name,
                                    )
                                )

                            if (
                                property_name == "scheduleId"
                                and operation_id == "deleteOrganizationDevicesPacketCaptureSchedule"
                            ):
                                # Schedule ID is duplicate of path param in this operation
                                continue

                            param_descriptions.append(
                                format_param_description(
                                    snake_name,
                                    property_schema.description or "",
                                )
                            )
                            py_type = get_python_type(property_schema.type or DataType.STRING)
                            required_properties = content_schema.required or []
                            if property_name in required_properties:
                                positional_args.append(f"{snake_name}: {py_type}")
                            else:
                                # Optional
                                default_val = "None"
                                type_annot = f"{py_type} | None"
                                keyword_args.append(f"{snake_name}: {type_annot} = {default_val}")

                            if property_schema.enum:
                                assert_blocks.append((snake_name, property_schema.enum))

                    if method == "get":
                        if is_paginated:
                            keyword_args.append("total_pages: int | Literal['all'] = 1")
                            if operation_id in REVERSE_PAGINATION:
                                keyword_args.append("direction: Literal['prev' | 'next'] = 'prev'")
                            else:
                                keyword_args.append("direction: Literal['prev' | 'next'] = 'next'")
                            param_descriptions.append(
                                format_param_description(
                                    "total_pages",
                                    "use with per_page to get total results"
                                    ' up to total_pages * per_page; -1 or "all" for all pages',
                                )
                            )
                            param_descriptions.append(
                                format_param_description(
                                    "direction",
                                    'direction to paginate, either "next" or "prev" (default) page'
                                    if operation_id in REVERSE_PAGINATION
                                    else 'direction to paginate, either "next" (default) or "prev" page',
                                )
                            )
                            if operation_id == "getNetworkEvents":
                                keyword_args.append("event_log_end_time: str | None = None")
                                param_descriptions.append(
                                    format_param_description(
                                        "event_log_end_time",
                                        "ISO8601 Zulu/UTC time, to use in conjunction with starting_after, "
                                        "to retrieve events within a time window",
                                    )
                                )
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
                        elif query_params:
                            call_line = "return self._session.get(metadata, resource, params)"
                        else:
                            call_line = "return self._session.get(metadata, resource)"

                    # Function body for POST/PUT endpoints
                    elif method in ["post", "put"]:
                        if body_params:
                            call_line = (
                                f"return self._session.{method}(metadata, resource, payload)"
                            )
                        else:
                            call_line = f"return self._session.{method}(metadata, resource)"

                    # Function body for DELETE endpoints
                    elif method == "delete":
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

                    # Construct function definition string
                    all_args = positional_args + keyword_args
                    definition = ", *, " + ", ".join(all_args) if all_args else ""

                    # Add function to files
                    with open(
                        os.path.join(TEMPLATE_DIR, "function_template.jinja2"),
                        encoding="utf-8",
                        newline=None,
                    ) as fp:
                        function_template = fp.read()
                        template = jinja_env.from_string(function_template)
                        output.write(
                            "\n\n"
                            + template.render(
                                operation=to_snake_case(operation_id),
                                function_definition=definition,
                                description=description,
                                doc_url=docs_url(operation_id),
                                descriptions=param_descriptions,
                                assert_blocks=assert_blocks,
                                tags=tags,
                                resource=resource_path,
                                query_params=query_params,
                                body_params=body_params,
                                path_params=path_params,
                                call_line=call_line,
                                return_type=return_type,
                            )
                        )
                        async_output.write(
                            "\n\n"
                            + template.render(
                                operation=to_snake_case(operation_id),
                                function_definition=definition,
                                description=description,
                                doc_url=docs_url(operation_id),
                                descriptions=param_descriptions,
                                assert_blocks=assert_blocks,
                                tags=tags,
                                resource=resource_path,
                                query_params=query_params,
                                body_params=body_params,
                                path_params=path_params,
                                call_line=call_line,
                                return_type=return_type,
                            )
                        )

                    if endpoint.description in batchable_action_summaries:
                        match method:
                            case "post":
                                batch_operation = "create"
                            case "put":
                                batch_operation = "update"
                            case "delete":
                                batch_operation = "destroy"
                            case _:
                                raise ValueError(f"Unsupported batch operation method: {method}")

                        # Function return statement
                        call_line = "return action  # noqa: RET504"

                        # Add function to files
                        with open(
                            os.path.join(TEMPLATE_DIR, "batch_function_template.jinja2"),
                            encoding="utf-8",
                            newline=None,
                        ) as fp:
                            function_template = fp.read()
                            template = jinja_env.from_string(function_template)
                            batch_output.write(
                                "\n\n"
                                + template.render(
                                    operation=to_snake_case(operation_id),
                                    function_definition=definition,
                                    description=description,
                                    doc_url=docs_url(operation_id),
                                    descriptions=param_descriptions,
                                    assert_blocks=assert_blocks,
                                    tags=tags,
                                    resource=resource_path,
                                    query_params=query_params,
                                    body_params=body_params,
                                    path_params=path_params,
                                    call_line=call_line,
                                    batch_operation=batch_operation,
                                    return_type="dict[str, Any]",
                                )
                            )


def recreate_output_directory() -> None:
    """Recreate the output directory."""
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


def copy_static_files(version_number: str, api_version: str) -> None:
    """Copy static files from generator/static/ to the output directory."""
    static_dir = os.path.join(SCRIPT_DIR, "static")
    static_files = [
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
    for file in static_files:
        src = os.path.join(static_dir, file)
        dst = os.path.join(OUTPUT_DIR, file)
        shutil.copy2(src, dst)

        # Update versions in __init__.py
        if file == "__init__.py":
            with open(dst, encoding="utf-8") as f:
                contents = f.read()
            # Update __version__
            start = contents.find("__version__ = ")
            end = contents.find("\n", start)
            contents = f"{contents[:start]}__version__ = '{version_number}'{contents[end:]}"
            # Update __api_version__
            start = contents.find("__api_version__ = ")
            end = contents.find("\n", start)
            contents = f"{contents[:start]}__api_version__ = '{api_version}'{contents[end:]}"
            with open(dst, "w", encoding="utf-8") as f:
                f.write(contents)


def sanitize_description(text: str) -> str:
    """Clean up description text from OpenAPI spec."""
    # Replace NO-BREAK SPACE (U+00A0) and other problematic whitespace with regular space
    text = text.replace("\u00a0", " ").replace("\u2007", " ").replace("\u202f", " ")
    # Strip leading/trailing whitespace and normalize internal whitespace
    text = " ".join(text.split())
    # Add a period if it doesn't end with one
    if not text.endswith("."):
        text += "."
    return text


def format_param_description(name: str, description: str) -> str:
    """Format a parameter description for Google-style docstring with line wrapping."""
    description = sanitize_description(description)
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


_T = TypeVar("_T")


def resolve_ref(
    spec: OpenAPI,
    ref: Reference,
    expected_type: type[_T],
    _seen: set[str] | None = None,
) -> _T | None:
    """Resolve a $ref reference in OASv3 spec.

    Example: #/components/schemas/Network -> spec.components.schemas['Network']

    Args:
        spec: The OpenAPI specification object.
        ref: The Reference object to resolve.
        expected_type: The expected type of the resolved object.
        _seen: Internal set to track resolved refs and avoid infinite recursion.

    Returns:
        The resolved object if it matches expected_type, None otherwise.

    """
    ref_str = ref.ref
    if not ref_str.startswith("#/"):
        # Ignore external refs
        return None

    # Track seen refs to avoid infinite recursion
    if _seen is None:
        _seen = set()
    if ref_str in _seen:
        return None
    _seen = _seen | {ref_str}

    # Decode and split path
    parts = [unquote(p) for p in ref_str[2:].split("/")]

    result: Any = spec
    for part in parts:
        if isinstance(result, dict):
            if part in result:
                result = result[part]
            else:
                return None
        elif isinstance(result, BaseModel):
            # Try attribute access first
            if hasattr(result, part):
                result = getattr(result, part)
            else:
                # Check if any field has this as an alias
                found = False
                for field_name, field_info in type(result).model_fields.items():
                    if field_info.alias == part:
                        result = getattr(result, field_name)
                        found = True
                        break
                if not found:
                    return None
        else:
            return None

    # Recursively resolve if result is also a Reference
    if isinstance(result, Reference):
        return resolve_ref(spec, result, expected_type, _seen)

    if isinstance(result, expected_type):
        return result
    return None


def docs_url(operation_id: str) -> str:
    """Returns full link to endpoint's documentation on Developer Hub."""
    base_url = "https://developer.cisco.com/meraki/api-v1/#!"
    ret = ""
    for letter in operation_id:
        if letter.islower():
            ret += letter
        else:
            ret += f"-{letter.lower()}"
    return base_url + ret


def to_snake_case(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case."""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def sanitize_param_name(name: str) -> str:
    """Append underscore to reserved Python keywords/builtins."""
    if name in RESERVED_NAMES:
        return f"{name}_"
    return name


def convert_path_params(path: str) -> str:
    """Convert all {paramName} in path to {param_name} (snake_case, sanitized)."""

    def replace_param(match: re.Match[str]) -> str:
        param = match.group(1)
        return f"{{{sanitize_param_name(to_snake_case(param))}}}"

    return re.sub(r"\{(\w+)\}", replace_param, path)


def get_python_type(data_type: DataType) -> str:
    """Get Python type for a data type."""
    match data_type:
        case DataType.ARRAY:
            return "list"
        case DataType.NUMBER:
            return "float"
        case DataType.INTEGER:
            return "int"
        case DataType.BOOLEAN:
            return "bool"
        case DataType.OBJECT:
            return "dict"
        case DataType.STRING:
            return "str"
        case _:
            assert_never(data_type)


if __name__ == "__main__":
    main()
