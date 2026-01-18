"""Pydantic schema generation from OpenAPI specification."""

from __future__ import annotations

import json
import logging
import re
import textwrap
from dataclasses import dataclass
from enum import Enum, auto
from typing import TYPE_CHECKING, Any, Literal, overload

from openapi_pydantic.v3.v3_0 import OpenAPI, Operation, Reference
from pydantic.alias_generators import to_snake

from codegen.constants import RESERVED_NAMES

if TYPE_CHECKING:
    from codegen.main import Templates

log = logging.getLogger("codegen")

SCHEMA_DOCSTRING_WIDTH = 96
MAX_CLASS_NAME_LENGTH = 80


class SchemaStatus(Enum):
    """Result status for schema generation."""

    GENERATED = auto()  # New schema was created
    DEDUPED = auto()  # Schema already existed (same definition)
    SKIPPED = auto()  # Schema couldn't be generated (no properties, wrong type, etc.)


@dataclass
class SchemaResult:
    """Result of schema generation."""

    status: SchemaStatus
    class_name: str | None = None
    is_array: bool = False
    item_class_names: list[str] | None = None


@dataclass
class SchemaRegistry:
    """Registry of generated response schemas."""

    schema_names: set[str]
    item_schema_map: dict[str, list[str]]
    untyped_response_ops: set[str]


@dataclass
class GenerationContext:
    """Context for schema generation carrying shared state."""

    schemas: dict[str, str]
    schema_to_scope: dict[str, str]
    schema_fingerprints: dict[str, str]
    scope: str
    depth: int = 0

    def nested(self) -> GenerationContext:
        """Create a new context for nested schema generation."""
        return GenerationContext(
            schemas=self.schemas,
            schema_to_scope=self.schema_to_scope,
            schema_fingerprints=self.schema_fingerprints,
            scope=self.scope,
            depth=self.depth + 1,
        )


def get_response_schema_name(operation_id: str) -> str:
    """Get the response schema class name for an operation."""
    return operation_id[0].upper() + operation_id[1:] + "Response"


def generate_response_schemas(
    spec: OpenAPI, templates: Templates, output_dir: str
) -> SchemaRegistry:
    """Generate Pydantic response schemas from OpenAPI specification."""
    schemas: dict[str, str] = {}
    schema_to_scope: dict[str, str] = {}
    schema_fingerprints: dict[str, str] = {}
    item_schema_map: dict[str, list[str]] = {}
    untyped_response_operations: set[str] = set()

    for path_item in spec.paths.values():
        operations: dict[Literal["get", "put", "post"], Operation | None] = {
            "get": path_item.get,
            "put": path_item.put,
            "post": path_item.post,
        }
        for operation in operations.values():
            if not operation or not operation.operationId:
                continue

            operation_id = operation.operationId
            scope = operation.tags[0] if operation.tags else None
            if not scope:
                log.warning(f"Operation {operation_id} has no tags")
                continue

            response_schema = _extract_response_schema(operation)
            if not response_schema:
                continue

            class_name = get_response_schema_name(operation_id)
            ctx = GenerationContext(
                schemas=schemas,
                schema_to_scope=schema_to_scope,
                schema_fingerprints=schema_fingerprints,
                scope=scope,
            )
            result = _generate_schema_class(
                ctx,
                class_name=class_name,
                schema=response_schema,
                description=f"Response for {operation_id} operation.",
            )
            if result.status != SchemaStatus.SKIPPED:
                if result.item_class_names:
                    item_schema_map[class_name] = result.item_class_names
            else:
                untyped_response_operations.add(operation_id)

    _write_schema_files(
        schemas=schemas,
        schema_to_scope=schema_to_scope,
        templates=templates,
        output_dir=output_dir,
    )
    return SchemaRegistry(
        schema_names=set(schemas.keys()),
        item_schema_map=item_schema_map,
        untyped_response_ops=untyped_response_operations,
    )


def _extract_response_schema(operation: Operation) -> dict[str, Any] | None:
    """Extract the response schema from the operation's 2xx response."""
    found_schema: dict[str, Any] | None = None
    found_status: str | None = None

    for status_code, response in operation.responses.items():
        if not status_code.startswith("2"):
            continue
        if isinstance(response, Reference):
            raise ValueError(
                f"Operation {operation.operationId} has a reference response for {status_code}"
            )

        content = response.content
        if not content:
            if status_code not in ["202", "204"]:
                log.warning(f"Operation {operation.operationId} has no content for {status_code}")
            continue

        json_content = content.get("application/json")
        if not json_content:
            log.warning(f"Operation {operation.operationId} has no JSON content for {status_code}")
            continue

        schema = json_content.media_type_schema
        if not schema:
            log.warning(f"Operation {operation.operationId} has no schema for {status_code}")
            continue
        if isinstance(schema, Reference):
            raise ValueError(
                f"Operation {operation.operationId} has a reference schema for {status_code}"
            )
        if found_schema is not None:
            raise ValueError(
                f"Operation {operation.operationId} has multiple 2xx responses "
                f"with schemas: {found_status} and {status_code}"
            )
        found_schema = schema.model_dump(exclude_none=True)
        found_status = status_code

    return found_schema


def _generate_schema_class(
    ctx: GenerationContext,
    *,
    class_name: str,
    schema: dict[str, Any],
    description: str | None = None,
) -> SchemaResult:
    """Generate a Pydantic model class from an OpenAPI schema."""
    schema_type = schema.get("type")
    docstring = schema.get("description") or description or f"Schema for {class_name}."

    if schema_type == "array":
        return _generate_array_schema(
            ctx, class_name=class_name, schema=schema, docstring=docstring
        )

    if schema_type == "object" or "properties" in schema:
        return _generate_object_schema(
            ctx, class_name=class_name, schema=schema, docstring=docstring
        )
    log.warning(f"Skipping schema generation for {class_name} because it has no properties")
    return SchemaResult(status=SchemaStatus.SKIPPED)


def _generate_array_schema(
    ctx: GenerationContext,
    *,
    class_name: str,
    schema: dict[str, Any],
    docstring: str,
) -> SchemaResult:
    """Generate a RootModel schema for array responses."""
    items_schema = schema.get("items", {})
    should_generate_nested = items_schema.get("type") == "object"
    inner_type, nested_class = _resolve_inner_type(
        ctx,
        inner_schema=items_schema,
        nested_class_name=class_name + "Item",
        should_generate_nested=should_generate_nested,
    )
    return _build_root_model_result(
        ctx,
        class_name=class_name,
        root_type=f"list[{inner_type}]",
        docstring=docstring,
        is_array=True,
        nested_class=nested_class,
    )


def _generate_dict_schema(
    ctx: GenerationContext,
    *,
    class_name: str,
    value_schema: dict[str, Any],
    docstring: str,
) -> SchemaResult:
    """Generate a RootModel schema for dict/map responses with additionalProperties."""
    should_generate_nested = bool(
        value_schema.get("type") == "object" and value_schema.get("properties")
    )
    inner_type, nested_class = _resolve_inner_type(
        ctx,
        inner_schema=value_schema,
        nested_class_name=class_name + "Value",
        should_generate_nested=should_generate_nested,
    )
    return _build_root_model_result(
        ctx,
        class_name=class_name,
        root_type=f"dict[str, {inner_type}]",
        docstring=docstring,
        is_array=False,
        nested_class=nested_class,
    )


def _resolve_inner_type(
    ctx: GenerationContext,
    *,
    inner_schema: dict[str, Any],
    nested_class_name: str,
    should_generate_nested: bool,
) -> tuple[str, str | None]:
    """Resolve the inner type for a RootModel container.

    Returns (type_string, nested_class_name_if_generated).
    """
    if should_generate_nested:
        result = _generate_schema_class(
            ctx.nested(), class_name=nested_class_name, schema=inner_schema
        )
        if result.status != SchemaStatus.SKIPPED:
            return f'"{nested_class_name}"', nested_class_name
        return "dict[str, Any]", None

    return _get_simple_type(inner_schema), None


def _build_root_model_result(
    ctx: GenerationContext,
    *,
    class_name: str,
    root_type: str,
    docstring: str,
    is_array: bool,
    nested_class: str | None,
) -> SchemaResult:
    """Build and register a RootModel schema, returning the result."""
    doc_lines = _format_docstring(docstring)
    body = "" if doc_lines else "    pass\n"
    definition = f"class {class_name}(RootModel[{root_type}]):\n{doc_lines}{body}"

    status = _register_schema(ctx, name=class_name, definition=definition)
    return SchemaResult(
        status=status,
        class_name=class_name,
        is_array=is_array,
        item_class_names=[nested_class] if nested_class else None,
    )


def _generate_object_schema(
    ctx: GenerationContext,
    *,
    class_name: str,
    schema: dict[str, Any],
    docstring: str,
) -> SchemaResult:
    """Generate a _BaseSchema class for object responses."""
    properties = schema.get("properties", {})

    if not properties:
        additional_props = schema.get("additionalProperties")
        if not isinstance(additional_props, dict):
            log.debug(
                f"Skipping schema generation for {class_name} because it has no additional properties"
            )
            return SchemaResult(status=SchemaStatus.SKIPPED)
        return _generate_dict_schema(
            ctx, class_name=class_name, value_schema=additional_props, docstring=docstring
        )

    lines = [f"class {class_name}(_BaseSchema):"]
    if docstring:
        lines.extend(_format_docstring(docstring, as_lines=True))

    required = set(schema.get("required", []))
    item_class_names: list[str] = []

    for prop_name, prop_schema in properties.items():
        field_def, field_type = _generate_field(
            ctx,
            parent_class=class_name,
            prop_name=prop_name,
            prop_schema=prop_schema,
            is_required=prop_name in required,
        )
        lines.append(f"    {field_def}")

        if (
            prop_schema.get("type") == "array"
            and prop_schema.get("items", {}).get("type") == "object"
            and prop_schema.get("items", {}).get("properties")
            and field_type.startswith("list[")
        ):
            item_class_names.append(field_type[5:-1])

    status = _register_schema(ctx, name=class_name, definition="\n".join(lines) + "\n")
    return SchemaResult(
        status=status,
        class_name=class_name,
        is_array=False,
        item_class_names=item_class_names or None,
    )


def _register_schema(ctx: GenerationContext, *, name: str, definition: str) -> SchemaStatus:
    """Register a schema. Returns GENERATED if new, DEDUPED if already exists."""
    if name in ctx.schemas:
        existing_scope = ctx.schema_to_scope.get(name)
        if existing_scope != ctx.scope:
            raise ValueError(
                f"Schema name collision: '{name}' already exists in scope "
                f"'{existing_scope}', cannot add to scope '{ctx.scope}'"
            )
        if ctx.schemas[name] != definition:
            raise ValueError(
                f"Schema collision: '{name}' in scope '{ctx.scope}' has conflicting definitions"
            )
        return SchemaStatus.DEDUPED

    ctx.schemas[name] = definition
    ctx.schema_to_scope[name] = ctx.scope
    return SchemaStatus.GENERATED


def _generate_field(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    prop_schema: dict[str, Any],
    is_required: bool,
) -> tuple[str, str]:
    """Generate a field definition for a Pydantic model."""
    snake_name = _sanitize_field_name(prop_name)
    py_type = _get_python_type(
        ctx, parent_class=parent_class, prop_name=prop_name, schema=prop_schema
    )
    needs_alias = snake_name != prop_name
    is_nullable = prop_schema.get("nullable", False)

    if is_required:
        type_annotation = f"{py_type} | None" if is_nullable else py_type
        if needs_alias:
            return f'{snake_name}: {type_annotation} = Field(alias="{prop_name}")', py_type
        return f"{snake_name}: {type_annotation}", py_type

    if needs_alias:
        return f'{snake_name}: {py_type} | None = Field(default=None, alias="{prop_name}")', py_type
    return f"{snake_name}: {py_type} | None = None", py_type


def _get_python_type(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    schema: dict[str, Any],
) -> str:
    """Get Python type annotation from OpenAPI schema."""
    schema_type = schema.get("type")

    if schema_type in ("string", "integer", "number", "boolean"):
        return _get_simple_type(schema)

    if schema_type == "array":
        return _get_array_type(ctx, parent_class=parent_class, prop_name=prop_name, schema=schema)

    if schema_type == "object":
        return _get_object_type(ctx, parent_class=parent_class, prop_name=prop_name, schema=schema)

    return "Any"


def _get_simple_type(schema: dict[str, Any]) -> str:
    """Get Python type for simple (non-class) schema types."""
    schema_type = schema.get("type")
    type_map = {"string": "str", "integer": "int", "number": "float", "boolean": "bool"}
    if schema_type in type_map:
        return type_map[schema_type]
    if schema_type == "array":
        item_type = _get_simple_type(schema.get("items", {}))
        return f"list[{item_type}]"
    if schema_type == "object":
        return "dict[str, Any]"
    return "Any"


def _get_array_type(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    schema: dict[str, Any],
) -> str:
    """Get Python type for array schema."""
    items = schema.get("items", {})

    if items.get("type") == "object" and items.get("properties"):
        fingerprint = _compute_fingerprint(items, ctx.scope)
        if fingerprint in ctx.schema_fingerprints:
            return f"list[{ctx.schema_fingerprints[fingerprint]}]"

        nested_ctx = ctx.nested()
        nested_class = _build_nested_class_name(
            nested_ctx, parent_class=parent_class, prop_name=prop_name, is_array=True
        )
        _generate_schema_class(nested_ctx, class_name=nested_class, schema=items)
        ctx.schema_fingerprints[fingerprint] = nested_class

        return f"list[{nested_class}]"

    item_type = _get_simple_type(items)
    return f"list[{item_type}]"


def _get_object_type(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    schema: dict[str, Any],
) -> str:
    """Get Python type for object schema."""
    props = schema.get("properties")

    if not props:
        return "dict[str, Any]"

    fingerprint = _compute_fingerprint(schema, ctx.scope)
    if fingerprint in ctx.schema_fingerprints:
        return ctx.schema_fingerprints[fingerprint]

    nested_ctx = ctx.nested()
    nested_class = _build_nested_class_name(
        nested_ctx, parent_class=parent_class, prop_name=prop_name, is_array=False
    )
    _generate_schema_class(nested_ctx, class_name=nested_class, schema=schema)
    ctx.schema_fingerprints[fingerprint] = nested_class

    return nested_class


def _build_nested_class_name(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    is_array: bool,
) -> str:
    """Build a nested class name with scope-aware shortening."""
    prop_pascal = prop_name[0].upper() + prop_name[1:]
    suffix = "Item" if is_array else ""
    full_name = _sanitize_class_name(parent_class + prop_pascal + suffix)

    should_shorten = ctx.depth >= 2 or len(full_name) > MAX_CLASS_NAME_LENGTH
    if not should_shorten:
        return full_name

    scope_prefix = ctx.scope[0].upper() + ctx.scope[1:]
    parent_context = ""
    if "Response" in parent_class:
        parent_context = parent_class.split("Response", 1)[-1]
        parent_context = re.sub(r"(Items?Item\d*|Item\d*)$", "", parent_context)

    base_short_name = _sanitize_class_name(f"{scope_prefix}{parent_context}{prop_pascal}{suffix}")

    if base_short_name not in ctx.schemas:
        return base_short_name

    for i in range(2, 100):
        numbered_name = f"{base_short_name}{i}"
        if numbered_name not in ctx.schemas:
            return numbered_name

    return full_name


def _sanitize_field_name(name: str) -> str:
    """Sanitize a field name to be a valid Python identifier."""
    if name and (name[0].isdigit() or name.replace(".", "").replace("-", "").isdigit()):
        return "n_" + name.replace(".", "_").replace("-", "_")
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
    return f"{snake}_" if snake in RESERVED_NAMES else snake


def _sanitize_class_name(name: str) -> str:
    """Sanitize a class name. Prefixes with 'N' if it starts with a digit."""
    return "N" + name if name and name[0].isdigit() else name


@overload
def _format_docstring(doc: str, *, as_lines: Literal[True]) -> list[str]: ...


@overload
def _format_docstring(doc: str, *, as_lines: Literal[False] = False) -> str: ...


def _format_docstring(doc: str, *, as_lines: bool = False) -> str | list[str]:
    """Format a docstring for a schema class with proper line wrapping."""
    if not doc:
        return [] if as_lines else ""

    doc = _sanitize_text(doc)
    indent = "    "
    max_single_line = SCHEMA_DOCSTRING_WIDTH - len(indent) - 6

    if len(doc) <= max_single_line:
        line = f'{indent}"""{doc}"""'
        return [line, ""] if as_lines else f"{line}\n\n"

    wrapper = textwrap.TextWrapper(
        width=SCHEMA_DOCSTRING_WIDTH - len(indent),
        initial_indent="",
        subsequent_indent="",
    )
    wrapped_lines = wrapper.wrap(doc)

    lines = [f'{indent}"""{wrapped_lines[0]}']
    lines.extend(f"{indent}{wrapped}" for wrapped in wrapped_lines[1:])
    lines.append(f'{indent}"""')
    lines.append("")

    return lines if as_lines else "\n".join(lines) + "\n"


def _sanitize_text(text: str) -> str:
    """Clean up text from OpenAPI spec."""
    text = text.replace("\u00a0", " ").replace("\u2007", " ").replace("\u202f", " ")
    text = " ".join(text.split())
    if not text.endswith("."):
        text += "."
    return text


def _compute_fingerprint(schema: dict[str, Any], scope: str) -> str:
    """Compute a fingerprint for schema deduplication within a scope."""
    normalized = _normalize_schema(schema)
    return f"{scope}:{json.dumps(normalized, sort_keys=True)}"


def _normalize_schema(schema: dict[str, Any], *, is_required: bool = False) -> dict[str, Any]:
    """Normalize schema to only include fields that affect generated code structure."""
    result: dict[str, Any] = {}

    if "type" in schema:
        result["type"] = schema["type"]

    if is_required and schema.get("nullable"):
        result["nullable"] = True

    required_set = set(schema.get("required", []))
    if required_set:
        result["required"] = sorted(required_set)

    if "properties" in schema:
        result["properties"] = {
            name: _normalize_schema(prop_schema, is_required=name in required_set)
            for name, prop_schema in sorted(schema["properties"].items())
        }

    if "items" in schema:
        result["items"] = _normalize_schema(schema["items"])

    if "enum" in schema:
        result["enum"] = sorted(schema["enum"]) if schema["enum"] else []

    if "additionalProperties" in schema:
        ap = schema["additionalProperties"]
        result["additionalProperties"] = _normalize_schema(ap) if isinstance(ap, dict) else ap

    return result


def _write_schema_files(
    *,
    schemas: dict[str, str],
    schema_to_scope: dict[str, str],
    templates: Templates,
    output_dir: str,
) -> None:
    """Write per-module schema files and a main __init__.py that re-exports all."""
    schemas_by_scope: dict[str, dict[str, str]] = {}
    for class_name, class_def in schemas.items():
        scope = schema_to_scope.get(class_name, "common")
        schemas_by_scope.setdefault(scope, {})[class_name] = class_def

    with open(f"{output_dir}/schemas/_base.py", "w") as f:
        f.write(templates.schema_base_template.render())

    all_exports: dict[str, list[str]] = {}
    for scope, scope_schemas in schemas_by_scope.items():
        module_name = to_snake(scope)
        sorted_schemas = sorted(scope_schemas.keys())
        all_exports[module_name] = sorted(sorted_schemas)

        schema_definitions = [scope_schemas[name] for name in sorted_schemas]
        with open(f"{output_dir}/schemas/{module_name}.py", "w") as f:
            f.write(
                templates.schema_module_template.render(
                    scope=module_name,
                    schema_definitions=schema_definitions,
                )
            )

    sorted_exports = dict(sorted(all_exports.items()))
    all_schemas = sorted(name for names in all_exports.values() for name in names)
    with open(f"{output_dir}/schemas/__init__.py", "w") as f:
        f.write(
            templates.schema_init_template.render(
                exports=sorted_exports,
                all_schemas=all_schemas,
            )
        )
