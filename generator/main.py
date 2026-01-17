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
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal, TextIO, TypeAlias, TypeVar, assert_never
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

from generator.log_config import setup_logging
from generator.schemas import BatchableAction

setup_logging()
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


@dataclass
class FunctionDefinition:
    """Function definition parameters."""

    # List of (snake, orig)
    body_params: list[tuple[str, str]] = field(default_factory=list)
    # List of (snake, options)
    assert_blocks: list[tuple[str, list[str]]] = field(default_factory=list)
    # List of descriptions
    param_descriptions: list[str] = field(default_factory=list)
    # List of required arguments
    required_args: list[str] = field(default_factory=list)
    # List of optional arguments
    optional_args: list[str] = field(default_factory=list)
    # List of query parameters
    query_params: list[tuple[str, str]] = field(default_factory=list)
    # List of path parameters
    path_params: list[str] = field(default_factory=list)


@dataclass
class ModuleInfo:
    """Module information for template generation."""

    snake_name: str
    class_name: str
    attr_name: str


@dataclass
class Templates:
    """Ninja templates."""

    batch_class_template: jinja2.Template
    batch_function_template: jinja2.Template
    batch_init_template: jinja2.Template
    class_template: jinja2.Template
    function_template: jinja2.Template
    init_template: jinja2.Template
    session_template: jinja2.Template


PathsType: TypeAlias = dict[str, dict[Literal["get", "put", "post", "delete"], Operation]]


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


def generate_library(
    spec: OpenAPI, batchable_actions: list[BatchableAction], version_number: str, api_version: str
) -> None:
    """Generate the Meraki Python library using the public OpenAPI specification."""
    batchable_action_summaries = [action.summary for action in batchable_actions]

    recreate_output_directory()
    copy_static_files()

    # Collect all operations by scope
    scopes: dict[str, PathsType] = {}
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
            if method in ["options", "head", "trace", "patch"]:
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

    templates = init_templates()

    # Collect module info for __init__.py generation
    modules = sorted(
        [
            ModuleInfo(
                snake_name=to_snake_case(scope),
                class_name=scope[:1].upper() + scope[1:],
                attr_name=to_snake_case(scope),
            )
            for scope in scopes
        ],
        key=lambda m: m.snake_name,
    )

    # Generate __init__.py from template
    with open(f"{OUTPUT_DIR}/__init__.py", "w") as f:
        f.write(
            templates.init_template.render(
                modules=modules,
                version=version_number,
                api_version=api_version,
                is_async=False,
            )
        )
    with open(f"{OUTPUT_DIR}/aio/__init__.py", "w") as f:
        f.write(
            templates.init_template.render(
                modules=modules, version=version_number, api_version=api_version, is_async=True
            )
        )

    # Generate session.py from template
    with open(f"{OUTPUT_DIR}/session.py", "w") as f:
        f.write(templates.session_template.render(is_async=False))
    with open(f"{OUTPUT_DIR}/aio/session.py", "w") as f:
        f.write(templates.session_template.render(is_async=True))

    def generate_scope(scope: str, paths: PathsType) -> ModuleInfo | None:
        """Generate a single scope's modules.

        Returns:
            ModuleInfo if scope has batch endpoints, None otherwise.

        """
        module_name = to_snake_case(scope)
        with (
            open(f"{OUTPUT_DIR}/api/{module_name}.py", "w") as output,
            open(f"{OUTPUT_DIR}/aio/api/{module_name}.py", "w") as async_output,
        ):
            batch_content = generate_module(
                scope=scope,
                paths=paths,
                spec=spec,
                batchable_action_summaries=batchable_action_summaries,
                output=output,
                async_output=async_output,
                templates=templates,
            )

        if batch_content:
            with open(f"{OUTPUT_DIR}/api/batch/{module_name}.py", "w") as batch_output:
                batch_output.write(batch_content)
            return ModuleInfo(
                snake_name=module_name,
                class_name=scope[:1].upper() + scope[1:],
                attr_name=module_name,
            )
        return None

    batch_modules: list[ModuleInfo] = []
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(generate_scope, scope, paths): scope for scope, paths in scopes.items()
        }
        for future in as_completed(futures):
            scope = futures[future]
            try:
                batch_module = future.result()
                if batch_module:
                    batch_modules.append(batch_module)
            except Exception:
                log.exception(f"Failed to generate {scope}")
                raise
            log.info(f"Generated {scope}")

    # Generate batch __init__.py from template
    batch_modules.sort(key=lambda m: m.snake_name)
    with open(f"{OUTPUT_DIR}/api/batch/__init__.py", "w") as f:
        f.write(templates.batch_init_template.render(modules=batch_modules))


def generate_module(
    *,
    scope: str,
    paths: PathsType,
    spec: OpenAPI,
    batchable_action_summaries: list[str],
    output: TextIO,
    async_output: TextIO,
    templates: Templates,
) -> str | None:
    """Generate a module for a scope.

    Returns:
        Batch module content if scope has batch endpoints, None otherwise.

    """
    class_name = scope[:1].upper() + scope[1:]
    output.write(templates.class_template.render(class_name=class_name, is_async=False))
    async_output.write(templates.class_template.render(class_name=class_name, is_async=True))

    batch_content: list[str] = []

    # Generate API & Asyncio API functions
    for path, methods in paths.items():
        for method, endpoint in methods.items():
            operation_id = endpoint.operationId
            if not operation_id:
                log.warning(f"Operation ID is missing for path: {path}")
                continue

            description = sanitize_description(str(endpoint.summary))
            resource_path = convert_path_params(path)
            function_definition = FunctionDefinition()
            is_paginated = collect_params(
                spec, operation_id, endpoint.parameters or [], function_definition
            )
            collect_request_body_params(
                spec, operation_id, endpoint.requestBody, function_definition
            )
            if is_paginated:
                collect_pagination_params(operation_id, function_definition)
            call_line = get_call_line(
                method=method,
                scope=scope,
                operation_id=operation_id,
                is_paginated=is_paginated,
                has_query_params=bool(function_definition.query_params),
                has_body_params=bool(function_definition.body_params),
            )
            return_type = get_return_type(method=method, is_paginated=is_paginated)

            # Construct function definition string
            all_args = function_definition.required_args + function_definition.optional_args
            definition = ", *, " + ", ".join(all_args) if all_args else ""

            output.write(
                templates.function_template.render(
                    operation=to_snake_case(operation_id),
                    function_definition=definition,
                    description=description,
                    doc_url=docs_url(operation_id),
                    descriptions=function_definition.param_descriptions,
                    assert_blocks=function_definition.assert_blocks,
                    resource=resource_path,
                    query_params=function_definition.query_params,
                    body_params=function_definition.body_params,
                    path_params=function_definition.path_params,
                    call_line=call_line,
                    return_type=return_type,
                )
            )
            async_output.write(
                templates.function_template.render(
                    operation=to_snake_case(operation_id),
                    function_definition=definition,
                    description=description,
                    doc_url=docs_url(operation_id),
                    descriptions=function_definition.param_descriptions,
                    assert_blocks=function_definition.assert_blocks,
                    resource=resource_path,
                    query_params=function_definition.query_params,
                    body_params=function_definition.body_params,
                    path_params=function_definition.path_params,
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

                batch_content.append(
                    templates.batch_function_template.render(
                        operation=to_snake_case(operation_id),
                        function_definition=definition,
                        description=description,
                        doc_url=docs_url(operation_id),
                        descriptions=function_definition.param_descriptions,
                        assert_blocks=function_definition.assert_blocks,
                        resource=resource_path,
                        query_params=function_definition.query_params,
                        body_params=function_definition.body_params,
                        path_params=function_definition.path_params,
                        call_line="return action  # noqa: RET504",
                        batch_operation=batch_operation,
                        return_type="dict[str, Any]",
                    )
                )

    if batch_content:
        return templates.batch_class_template.render(class_name=class_name) + "".join(batch_content)
    return None


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


def copy_static_files() -> None:
    """Copy static files from generator/static/ to the output directory."""
    static_dir = Path(SCRIPT_DIR) / "static"
    for src in static_dir.rglob("*.py"):
        relative_path = src.relative_to(static_dir)
        dst = Path(OUTPUT_DIR) / relative_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def init_templates() -> Templates:
    """Initialize the templates."""
    jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)  # noqa: S701
    return Templates(
        batch_class_template=read_template("batch_class_template.py", jinja_env),
        batch_function_template=read_template("batch_function_template.py", jinja_env),
        batch_init_template=read_template("batch_init_template.py", jinja_env),
        class_template=read_template("class_template.py", jinja_env),
        function_template=read_template("function_template.py", jinja_env),
        init_template=read_template("init_template.py", jinja_env),
        session_template=read_template("session_template.py", jinja_env),
    )


def read_template(template_name: str, jinja_env: jinja2.Environment) -> jinja2.Template:
    """Read a template from the template directory."""
    with open(
        os.path.join(TEMPLATE_DIR, f"{template_name}.jinja2"), encoding="utf-8", newline=None
    ) as fp:
        return jinja_env.from_string(fp.read())


def collect_params(
    spec: OpenAPI,
    operation_id: str,
    parameters: list[Parameter | Reference],
    function_definition: FunctionDefinition,
) -> bool:
    """Collect path and query parameters.

    Args:
        spec: The OpenAPI specification object.
        operation_id: The operation ID.
        parameters: The parameters list.
        function_definition: The function definition object.

    Returns:
        True if the operation is paginated, False otherwise.

    """
    is_paginated = False
    for param in parameters:
        if isinstance(param, Reference):
            param = resolve_ref(spec, param, Parameter)  # noqa: PLW2901
            if not param:
                log.warning(f"Failed to resolve parameter reference: {param}")
                continue

        param_name = param.name
        snake_name = sanitize_param_name(to_snake_case(param_name))

        param_schema = param.param_schema
        if not param_schema:
            log.warning(f"No schema found for parameter: {param_name}")
            continue
        if isinstance(param_schema, Reference):
            param_schema = resolve_ref(spec, param_schema, Schema)
            if not param_schema:
                log.error(f"Failed to resolve schema reference: {param_schema}")
                continue

        py_type = get_python_type(param_schema.type or DataType.STRING)

        if param.param_in == ParameterLocation.QUERY:
            key = param_name
            if param_schema.type == DataType.ARRAY:
                # Query parameter syntax for arrays is param[]=value
                key += "[]"
            function_definition.query_params.append((snake_name, key))
        elif param.param_in == ParameterLocation.PATH:
            function_definition.path_params.append(snake_name)
        else:
            log.error(
                f"Unsupported parameter location '{param.param_in}' for operation: {operation_id}"
            )
            continue

        # Add description
        function_definition.param_descriptions.append(
            format_param_description(
                snake_name, param.description or param_schema.description or ""
            )
        )

        if snake_name == "per_page":
            is_paginated = True

        if param.required or param.param_in == ParameterLocation.PATH:
            function_definition.required_args.append(f"{snake_name}: {py_type}")
        else:
            function_definition.optional_args.append(f"{snake_name}: {py_type} | None = None")
        if param_schema.enum:
            function_definition.assert_blocks.append((snake_name, param_schema.enum))

    return is_paginated


def collect_request_body_params(
    spec: OpenAPI,
    operation_id: str,
    request_body: RequestBody | Reference | None,
    function_definition: FunctionDefinition,
) -> None:
    """Collect request body parameters."""
    if isinstance(request_body, Reference):
        request_body = resolve_ref(spec, request_body, RequestBody)

    if not request_body:
        return

    json_content = request_body.content.get("application/json")
    if not json_content:
        log.warning(f"No JSON content found in request body for operation: {operation_id}")
        return

    content_schema = json_content.media_type_schema
    if isinstance(content_schema, Reference):
        content_schema = resolve_ref(spec, content_schema, Schema)
    if not content_schema:
        log.warning(f"No schema found in request body for operation: {operation_id}")
        return

    properties = content_schema.properties or {}
    for property_name, property_schema in properties.items():
        snake_name = sanitize_param_name(to_snake_case(property_name))
        if isinstance(property_schema, Reference):
            property_schema = resolve_ref(spec, property_schema, Schema)  # noqa: PLW2901
            if not property_schema:
                log.error(f"Failed to resolve schema reference: {property_schema}")
                continue

        function_definition.body_params.append((snake_name, property_name))

        if (
            property_name == "scheduleId"
            and operation_id == "deleteOrganizationDevicesPacketCaptureSchedule"
        ):
            # Schedule ID is duplicate of path param in this operation
            continue

        function_definition.param_descriptions.append(
            format_param_description(
                snake_name,
                property_schema.description or "",
            )
        )

        py_type = get_python_type(property_schema.type or DataType.STRING)
        required_properties = content_schema.required or []
        if property_name in required_properties:
            function_definition.required_args.append(f"{snake_name}: {py_type}")
        else:
            function_definition.optional_args.append(f"{snake_name}: {py_type} | None = None")

        if property_schema.enum:
            function_definition.assert_blocks.append((snake_name, property_schema.enum))


def collect_pagination_params(operation_id: str, function_definition: FunctionDefinition) -> None:
    """Collect pagination parameters."""
    function_definition.optional_args.append("total_pages: int | Literal['all'] = 1")

    function_definition.param_descriptions.append(
        format_param_description(
            "total_pages",
            "use with per_page to get total results"
            ' up to total_pages * per_page; -1 or "all" for all pages',
        )
    )

    if operation_id in REVERSE_PAGINATION:
        function_definition.optional_args.append("direction: Literal['prev' | 'next'] = 'prev'")
    else:
        function_definition.optional_args.append("direction: Literal['prev' | 'next'] = 'next'")

    function_definition.param_descriptions.append(
        format_param_description(
            "direction",
            'direction to paginate, either "next" or "prev" (default) page'
            if operation_id in REVERSE_PAGINATION
            else 'direction to paginate, either "next" (default) or "prev" page',
        )
    )

    if operation_id == "getNetworkEvents":
        function_definition.optional_args.append("event_log_end_time: str | None = None")
        function_definition.param_descriptions.append(
            format_param_description(
                "event_log_end_time",
                "ISO8601 Zulu/UTC time, to use in conjunction with starting_after, "
                "to retrieve events within a time window",
            )
        )


def get_call_line(
    *,
    method: Literal["get", "put", "post", "delete"],
    scope: str,
    operation_id: str,
    has_query_params: bool,
    is_paginated: bool,
    has_body_params: bool,
) -> str:
    """Get the call line for a function."""
    match method:
        case "get":
            if operation_id == "getNetworkEvents":
                return (
                    "return self._session.get_pages"
                    "(scope=scope, operation_id=operation_id, path=path, params=params, "
                    "total_pages=total_pages, direction=direction, event_log_end_time=event_log_end_time)"
                )
            if is_paginated:
                return (
                    f'return self._session.get_pages(scope="{scope}", '
                    'operation_id="{operation_id}", path=path, params=params, '
                    "total_pages=total_pages, direction=direction)"
                )
            if has_query_params:
                return (
                    f'return self._session.get(scope="{scope}", '
                    'operation_id="{operation_id}", path=path, params=params)'
                )
            return f'return self._session.get(scope="{scope}", operation_id="{operation_id}", path=path)'
        case "post":
            if has_body_params:
                return (
                    f'return self._session.post(scope="{scope}", '
                    'operation_id="{operation_id}", path=path, json=payload)'
                )
            return f'return self._session.post(scope="{scope}", operation_id="{operation_id}", path=path)'
        case "put":
            if has_body_params:
                return (
                    f'return self._session.put(scope="{scope}", '
                    'operation_id="{operation_id}", path=path, json=payload)'
                )
            return f'return self._session.put(scope="{scope}", operation_id="{operation_id}", path=path)'
        case "delete":
            return f'return self._session.delete(scope="{scope}", operation_id="{operation_id}", path=path)'
        case _:
            assert_never(method)


def get_return_type(*, method: Literal["get", "put", "post", "delete"], is_paginated: bool) -> str:
    """Get the return type for a function."""
    if method == "delete":
        return "None"
    if method == "get" and is_paginated:
        return "Generator[Any, None, None]"
    return "dict[str, Any] | None"


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
