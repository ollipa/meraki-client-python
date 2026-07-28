"""Pydantic schema generation from OpenAPI specification."""

from __future__ import annotations

import json
import logging
import re
import textwrap
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import TYPE_CHECKING, Any, Literal, NamedTuple, overload

from openapi_pydantic.v3.v3_0 import OpenAPI, Operation, Reference

from codegen.utils import (
    SpecOverrides,
    capitalize_first,
    escape_reserved_name,
    load_spec_overrides,
    sanitize_text,
    to_snake_case,
)

if TYPE_CHECKING:
    from codegen.main import Templates

log = logging.getLogger("codegen")

SCHEMA_DOCSTRING_WIDTH = 96
MAX_CLASS_NAME_LENGTH = 80
TYPE_MAP = {"string": "str", "integer": "int", "number": "float", "boolean": "bool"}
FORMAT_MAP = {
    "date-time": "datetime",
    "date": "date",
    "time": "time",
    "byte": "str",  # base64 encoded, keep as string
    "float": "float",  # redundant with type: number
}
IDENTIFIER_PARTS_RE = re.compile(r"[A-Z]+(?=[A-Z][a-z0-9]|$)|[A-Z]?[a-z0-9]+")


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
class RequestBodyParamSchema:
    """Schema info for a request body parameter."""

    class_name: str
    is_list: bool = False
    is_dict: bool = False
    item_class_name: str | None = None


@dataclass(frozen=True)
class PreparedResponseSchema:
    """Prepared response schema ready for naming and generation."""

    operation_id: str
    scope: str
    schema: dict[str, Any]


@dataclass(frozen=True)
class PreparedResponseItemSchema:
    """Prepared response item schema ready for naming and generation."""

    operation_id: str
    scope: str
    schema: dict[str, Any]
    name_suffix: str
    field_path: tuple[str, ...] = ()
    include_extra_fields: bool = True


@dataclass(frozen=True)
class ResponseSchemaPlan:
    """Planned response schema generation details for an operation."""

    schema: dict[str, Any]
    class_name: str
    description: str


@dataclass
class NestedOverrideState:
    """Accumulated relative overrides for a deduplicated nested schema."""

    response_fields: dict[str, str] = field(default_factory=dict)
    required_fields: set[str] = field(default_factory=set)
    extra_fields: dict[str, str] = field(default_factory=dict)

    def has_overrides(self) -> bool:
        """Return whether this state contains any effective overrides."""
        return bool(self.response_fields or self.required_fields or self.extra_fields)


@dataclass(frozen=True)
class PlannedResponseSchemas:
    """Planned response and response-item schema generation details."""

    response_plans: dict[str, ResponseSchemaPlan]
    response_item_plans: dict[str, ResponseSchemaPlan]


@dataclass
class SchemaRegistry:
    """Registry of generated response schemas."""

    schema_names: set[str]
    response_schemas: dict[str, str]
    response_item_schemas: dict[str, list[str]]
    untyped_response_ops: set[str]
    # Map of (operation_id, property_name) -> RequestBodyParamSchema
    request_body_schemas: dict[tuple[str, str], RequestBodyParamSchema]
    # Set of response schema names that are list types
    list_response_schemas: set[str]


@dataclass
class SchemaGenerationState:
    """Mutable state accumulated while generating schemas."""

    schemas: dict[str, str] = field(default_factory=dict)
    schema_to_scope: dict[str, str] = field(default_factory=dict)
    schema_fingerprints: dict[str, str] = field(default_factory=dict)
    nested_override_states: dict[str, NestedOverrideState] = field(default_factory=dict)
    response_schemas: dict[str, str] = field(default_factory=dict)
    response_item_schemas: dict[str, list[str]] = field(default_factory=dict)
    untyped_response_operations: set[str] = field(default_factory=set)
    request_body_schemas: dict[tuple[str, str], RequestBodyParamSchema] = field(
        default_factory=dict
    )
    list_response_schemas: set[str] = field(default_factory=set)


@dataclass
class GenerationContext:
    """Context for schema generation carrying shared state."""

    schemas: dict[str, str]
    schema_to_scope: dict[str, str]
    schema_fingerprints: dict[str, str]
    nested_override_states: dict[str, NestedOverrideState]
    scope: str
    depth: int = 0
    operation_id: str | None = None
    field_path: tuple[str, ...] = ()
    spec_overrides: SpecOverrides | None = None
    consumed_overrides: set[tuple[str, str]] | None = None
    consumed_required_overrides: set[tuple[str, str]] | None = None
    planned_response_item_plan: ResponseSchemaPlan | None = None
    allow_schema_overwrite: bool = False

    def nested(self, path_segment: str | None = None) -> GenerationContext:
        """Create a new context for nested schema generation."""
        new_path = (*self.field_path, path_segment) if path_segment else self.field_path
        return GenerationContext(
            schemas=self.schemas,
            schema_to_scope=self.schema_to_scope,
            schema_fingerprints=self.schema_fingerprints,
            nested_override_states=self.nested_override_states,
            scope=self.scope,
            depth=self.depth + 1,
            operation_id=self.operation_id,
            field_path=new_path,
            spec_overrides=self.spec_overrides,
            consumed_overrides=self.consumed_overrides,
            consumed_required_overrides=self.consumed_required_overrides,
            planned_response_item_plan=self.planned_response_item_plan,
            allow_schema_overwrite=self.allow_schema_overwrite,
        )

    def with_planned_response_item_plan(
        self, planned_response_item_plan: ResponseSchemaPlan | None
    ) -> GenerationContext:
        """Create a new context with a planned top-level response item schema."""
        return GenerationContext(
            schemas=self.schemas,
            schema_to_scope=self.schema_to_scope,
            schema_fingerprints=self.schema_fingerprints,
            nested_override_states=self.nested_override_states,
            scope=self.scope,
            depth=self.depth,
            operation_id=self.operation_id,
            field_path=self.field_path,
            spec_overrides=self.spec_overrides,
            consumed_overrides=self.consumed_overrides,
            consumed_required_overrides=self.consumed_required_overrides,
            planned_response_item_plan=planned_response_item_plan,
            allow_schema_overwrite=self.allow_schema_overwrite,
        )


class TypeResult(NamedTuple):
    """Result of type resolution, optionally including nested item class."""

    type_str: str
    item_class: str | None = None


class FieldResult(NamedTuple):
    """Generated field definition, with the nested item class it introduced, if any."""

    definition: str
    item_class: str | None = None
    is_list: bool = False


def get_response_schema_name(operation_id: str) -> str:
    """Get the response schema class name for an operation."""
    return f"{capitalize_first(operation_id)}Response"


def get_request_param_schema_name(operation_id: str, property_name: str) -> str:
    """Get the request body parameter schema class name."""
    parts = re.split(r"[/_]", property_name)
    sanitized_prop = "".join(capitalize_first(p) if p else "" for p in parts)
    return f"{capitalize_first(operation_id)}{sanitized_prop}"


def _plan_response_schemas(spec: OpenAPI, spec_overrides: SpecOverrides) -> PlannedResponseSchemas:
    """Plan canonical response and response-item schema names before generating code."""
    prepared_responses: list[PreparedResponseSchema] = []
    prepared_response_items: list[PreparedResponseItemSchema] = []

    for path_item in spec.paths.values():
        operations: dict[Literal["get", "put", "post", "delete"], Operation | None] = {
            "get": path_item.get,
            "put": path_item.put,
            "post": path_item.post,
            "delete": path_item.delete,
        }
        for method, operation in operations.items():
            if not operation or not operation.operationId:
                continue

            operation_id = operation.operationId
            scope = operation.tags[0] if operation.tags else None
            if not scope:
                continue

            response_schema = _prepare_response_schema(
                operation=operation,
                operation_id=operation_id,
                spec_overrides=spec_overrides,
            )
            if response_schema is None:
                continue

            prepared_responses.append(
                PreparedResponseSchema(
                    operation_id=operation_id,
                    scope=scope,
                    schema=response_schema,
                )
            )
            prepared_item = _prepare_response_item_schema(
                method=method,
                operation_id=operation_id,
                scope=scope,
                response_schema=response_schema,
            )
            if prepared_item is not None:
                prepared_response_items.append(prepared_item)

    response_groups: dict[str, list[PreparedResponseSchema]] = {}
    for prepared in prepared_responses:
        fingerprint = _compute_response_schema_fingerprint(
            operation_id=prepared.operation_id,
            scope=prepared.scope,
            schema=prepared.schema,
            spec_overrides=spec_overrides,
        )
        response_groups.setdefault(fingerprint, []).append(prepared)

    used_class_names: set[str] = set()
    response_plans: dict[str, ResponseSchemaPlan] = {}
    canonical_object_plans: dict[str, ResponseSchemaPlan] = {}
    for grouped_responses in response_groups.values():
        class_name = _get_grouped_response_schema_name(grouped_responses, used_class_names)
        description = _build_response_schema_description(class_name, grouped_responses)
        used_class_names.add(class_name)

        for prepared in grouped_responses:
            plan = ResponseSchemaPlan(
                schema=prepared.schema,
                class_name=class_name,
                description=description,
            )
            response_plans[prepared.operation_id] = plan
            if _is_object_schema(prepared.schema):
                fingerprint = _compute_response_schema_fingerprint(
                    operation_id=prepared.operation_id,
                    scope=prepared.scope,
                    schema=prepared.schema,
                    spec_overrides=spec_overrides,
                )
                canonical_object_plans[fingerprint] = plan

    response_item_plans = _build_response_item_plans(
        prepared_response_items=prepared_response_items,
        response_plans=response_plans,
        spec_overrides=spec_overrides,
        used_class_names=used_class_names,
        canonical_object_plans=canonical_object_plans,
    )
    return PlannedResponseSchemas(
        response_plans=response_plans,
        response_item_plans=response_item_plans,
    )


def _prepare_response_schema(
    *, operation: Operation, operation_id: str, spec_overrides: SpecOverrides
) -> dict[str, Any] | None:
    """Extract and normalize a response schema for planning or generation."""
    response_schema = _extract_response_schema(operation)
    if response_schema is None:
        return None

    response_schema = _apply_inject_response_schema(
        operation_id, response_schema, spec_overrides.inject_response_schema
    )
    response_schema = _apply_force_array_response(
        operation_id, response_schema, spec_overrides.force_array_response
    )
    return _normalize_paginated_response_schema(
        operation_id=operation_id,
        schema=response_schema,
        force_paginated_items_schema=spec_overrides.force_paginated_items_schema,
    )


def _prepare_response_item_schema(
    *,
    method: Literal["get", "put", "post", "delete"],
    operation_id: str,
    scope: str,
    response_schema: dict[str, Any],
) -> PreparedResponseItemSchema | None:
    """Prepare a top-level response item schema for canonical naming."""
    items_schema = response_schema.get("items")
    if isinstance(items_schema, dict) and _has_nested_properties(items_schema):
        return PreparedResponseItemSchema(
            operation_id=operation_id,
            scope=scope,
            schema=items_schema,
            name_suffix="Item",
        )

    if method != "get":
        return None

    item_schema = _get_paginated_wrapper_item_schema(response_schema)
    if item_schema is None or not _has_nested_properties(item_schema):
        return None

    return PreparedResponseItemSchema(
        operation_id=operation_id,
        scope=scope,
        schema=item_schema,
        name_suffix="ItemsItem",
        field_path=("items",),
        include_extra_fields=False,
    )


def _compute_response_schema_fingerprint(
    *,
    operation_id: str,
    scope: str,
    schema: dict[str, Any],
    spec_overrides: SpecOverrides,
    field_path: tuple[str, ...] = (),
    include_extra_fields: bool = True,
) -> str:
    """Compute a response fingerprint, including applicable operation overrides."""
    normalized = {
        "scope": scope,
        "schema": _normalize_schema(schema),
        "response_fields": _normalize_override_map(
            spec_overrides.response_fields.get(operation_id, {}),
            field_path=field_path,
        ),
        "required_fields": _normalize_override_set(
            spec_overrides.required_fields.get(operation_id, set()),
            field_path=field_path,
        ),
        "extra_fields": (
            dict(sorted(spec_overrides.extra_fields.get(operation_id, {}).items()))
            if include_extra_fields and not field_path
            else {}
        ),
    }
    return json.dumps(normalized, sort_keys=True)


def _build_response_item_plans(
    *,
    prepared_response_items: list[PreparedResponseItemSchema],
    response_plans: dict[str, ResponseSchemaPlan],
    spec_overrides: SpecOverrides,
    used_class_names: set[str],
    canonical_object_plans: dict[str, ResponseSchemaPlan],
) -> dict[str, ResponseSchemaPlan]:
    """Plan canonical response item schema names before generating code."""
    response_item_plans: dict[str, ResponseSchemaPlan] = {}
    item_groups: dict[str, list[PreparedResponseItemSchema]] = {}

    for prepared in prepared_response_items:
        fingerprint = _compute_response_schema_fingerprint(
            operation_id=prepared.operation_id,
            scope=prepared.scope,
            schema=prepared.schema,
            spec_overrides=spec_overrides,
            field_path=prepared.field_path,
            include_extra_fields=prepared.include_extra_fields,
        )
        canonical_object_plan = canonical_object_plans.get(fingerprint)
        if canonical_object_plan is not None:
            response_item_plans[prepared.operation_id] = ResponseSchemaPlan(
                schema=prepared.schema,
                class_name=canonical_object_plan.class_name,
                description=canonical_object_plan.description,
            )
            continue

        item_groups.setdefault(fingerprint, []).append(prepared)

    for grouped_items in item_groups.values():
        first_item = grouped_items[0]
        default_name = response_plans[first_item.operation_id].class_name + first_item.name_suffix
        class_name = _make_unique_class_name(default_name, used_class_names)
        used_class_names.add(class_name)
        plan = ResponseSchemaPlan(
            schema=first_item.schema,
            class_name=class_name,
            description=f"Schema for {class_name}.",
        )
        for prepared in grouped_items:
            response_item_plans[prepared.operation_id] = plan

    return response_item_plans


def _normalize_override_map(
    overrides: dict[str, str], *, field_path: tuple[str, ...]
) -> dict[str, str]:
    """Normalize field override paths relative to a schema fingerprint scope."""
    if not field_path:
        return dict(sorted(overrides.items()))

    prefix = ".".join(field_path) + "."
    normalized = {
        path[len(prefix) :]: override_type
        for path, override_type in overrides.items()
        if path.startswith(prefix)
    }
    return dict(sorted(normalized.items()))


def _normalize_override_set(overrides: set[str], *, field_path: tuple[str, ...]) -> list[str]:
    """Normalize required-field override paths relative to a schema fingerprint scope."""
    if not field_path:
        return sorted(overrides)

    prefix = ".".join(field_path) + "."
    return sorted(path[len(prefix) :] for path in overrides if path.startswith(prefix))


def _get_applicable_nested_override_state(ctx: GenerationContext) -> NestedOverrideState:
    """Get override state applicable to a nested schema, relative to its own root."""
    if not ctx.operation_id or ctx.spec_overrides is None:
        return NestedOverrideState()

    response_fields = _normalize_override_map(
        ctx.spec_overrides.response_fields.get(ctx.operation_id, {}),
        field_path=ctx.field_path,
    )
    required_fields = set(
        _normalize_override_set(
            ctx.spec_overrides.required_fields.get(ctx.operation_id, set()),
            field_path=ctx.field_path,
        )
    )
    extra_fields = (
        dict(sorted(ctx.spec_overrides.extra_fields.get(ctx.operation_id, {}).items()))
        if ctx.depth <= 1 and not ctx.field_path
        else {}
    )
    return NestedOverrideState(
        response_fields=response_fields,
        required_fields=required_fields,
        extra_fields=extra_fields,
    )


def _merge_nested_override_state(
    existing: NestedOverrideState | None, current: NestedOverrideState
) -> tuple[NestedOverrideState, bool]:
    """Merge nested override state, erroring on conflicting type declarations."""
    if existing is None:
        return (
            NestedOverrideState(
                response_fields=dict(current.response_fields),
                required_fields=set(current.required_fields),
                extra_fields=dict(current.extra_fields),
            ),
            current.has_overrides(),
        )

    merged = NestedOverrideState(
        response_fields=dict(existing.response_fields),
        required_fields=set(existing.required_fields),
        extra_fields=dict(existing.extra_fields),
    )
    changed = False

    for field_path, override_type in current.response_fields.items():
        existing_type = merged.response_fields.get(field_path)
        if existing_type is not None and existing_type != override_type:
            raise ValueError(
                f"Conflicting nested response override for field '{field_path}': "
                f"'{existing_type}' vs '{override_type}'"
            )
        if existing_type is None:
            merged.response_fields[field_path] = override_type
            changed = True

    for field_name, field_type in current.extra_fields.items():
        existing_type = merged.extra_fields.get(field_name)
        if existing_type is not None and existing_type != field_type:
            raise ValueError(
                f"Conflicting nested extra_field override for field '{field_name}': "
                f"'{existing_type}' vs '{field_type}'"
            )
        if existing_type is None:
            merged.extra_fields[field_name] = field_type
            changed = True

    previous_required_count = len(merged.required_fields)
    merged.required_fields.update(current.required_fields)
    if len(merged.required_fields) != previous_required_count:
        changed = True

    return merged, changed


def _build_relative_spec_overrides(override_state: NestedOverrideState) -> SpecOverrides:
    """Build a synthetic SpecOverrides object from relative nested override state."""
    operation_id = "__nested_override__"
    return SpecOverrides(
        response_fields=(
            {operation_id: dict(override_state.response_fields)}
            if override_state.response_fields
            else {}
        ),
        required_fields=(
            {operation_id: set(override_state.required_fields)}
            if override_state.required_fields
            else {}
        ),
        extra_fields=(
            {operation_id: dict(override_state.extra_fields)} if override_state.extra_fields else {}
        ),
    )


def _with_relative_nested_overrides(
    ctx: GenerationContext,
    override_state: NestedOverrideState,
    *,
    allow_schema_overwrite: bool,
) -> GenerationContext:
    """Create a context that applies relative overrides from the nested schema root."""
    return GenerationContext(
        schemas=ctx.schemas,
        schema_to_scope=ctx.schema_to_scope,
        schema_fingerprints=ctx.schema_fingerprints,
        nested_override_states=ctx.nested_override_states,
        scope=ctx.scope,
        depth=ctx.depth,
        operation_id="__nested_override__",
        field_path=(),
        spec_overrides=_build_relative_spec_overrides(override_state),
        consumed_overrides=set(),
        consumed_required_overrides=set(),
        planned_response_item_plan=ctx.planned_response_item_plan,
        allow_schema_overwrite=allow_schema_overwrite,
    )


def _get_grouped_response_schema_name(
    grouped_responses: list[PreparedResponseSchema], used_class_names: set[str]
) -> str:
    """Choose a canonical response schema name for a deduped group."""
    operation_ids = [prepared.operation_id for prepared in grouped_responses]
    shared_name = _get_shared_response_schema_name(operation_ids)
    if shared_name and shared_name not in used_class_names:
        return shared_name

    default_name = get_response_schema_name(operation_ids[0])
    return _make_unique_class_name(default_name, used_class_names)


def _get_shared_response_schema_name(operation_ids: list[str]) -> str | None:
    """Derive a shared resource-style response name when CRUD tails match."""
    if len(operation_ids) < 2:
        return None

    identifier_parts = [_split_identifier_parts(operation_id) for operation_id in operation_ids]
    if any(len(parts) < 2 for parts in identifier_parts):
        return None

    shared_suffix = identifier_parts[0][1:]
    if not shared_suffix:
        return None
    if not all(parts[1:] == shared_suffix for parts in identifier_parts[1:]):
        return None

    return "".join(shared_suffix) + "Response"


def _build_response_schema_description(
    class_name: str, grouped_responses: list[PreparedResponseSchema]
) -> str:
    """Build a stable docstring for a response schema group."""
    if len(grouped_responses) == 1:
        operation_id = grouped_responses[0].operation_id
        if class_name == get_response_schema_name(operation_id):
            return f"Response for {operation_id} operation."
    return f"Schema for {class_name}."


def _split_identifier_parts(name: str) -> list[str]:
    """Split a camelCase/PascalCase identifier into component words."""
    parts = IDENTIFIER_PARTS_RE.findall(capitalize_first(name))
    return parts or [capitalize_first(name)]


def _make_unique_class_name(base_name: str, used_class_names: set[str]) -> str:
    """Return a class name that is unique within the planned response schema set."""
    if base_name not in used_class_names:
        return base_name

    for i in range(2, 100):
        candidate = f"{base_name}{i}"
        if candidate not in used_class_names:
            return candidate

    raise ValueError(f"Could not generate unique class name for {base_name}")


def generate_response_schemas(
    spec: OpenAPI, templates: Templates, output_dir: str
) -> SchemaRegistry:
    """Generate Pydantic response and request body schemas from OpenAPI specification."""
    state = SchemaGenerationState()

    spec_overrides = load_spec_overrides()
    consumed_overrides: set[tuple[str, str]] = set()
    consumed_required_overrides: set[tuple[str, str]] = set()
    spec_operation_ids: set[str] = set()
    planned_response_schemas = _plan_response_schemas(spec, spec_overrides)

    for path_item in spec.paths.values():
        operations: dict[Literal["get", "put", "post", "delete"], Operation | None] = {
            "get": path_item.get,
            "put": path_item.put,
            "post": path_item.post,
            "delete": path_item.delete,
        }
        for method, operation in operations.items():
            if not operation or not operation.operationId:
                continue

            operation_id = operation.operationId
            spec_operation_ids.add(operation_id)
            scope = operation.tags[0] if operation.tags else None
            if not scope:
                log.warning(f"Operation {operation_id} has no tags")
                continue

            ctx = GenerationContext(
                schemas=state.schemas,
                schema_to_scope=state.schema_to_scope,
                schema_fingerprints=state.schema_fingerprints,
                nested_override_states=state.nested_override_states,
                scope=scope,
                operation_id=operation_id,
                spec_overrides=spec_overrides,
                consumed_overrides=consumed_overrides,
                consumed_required_overrides=consumed_required_overrides,
            )

            # Generate response schemas
            response_plan = planned_response_schemas.response_plans.get(operation_id)
            if response_plan:
                response_schema = response_plan.schema
                class_name = response_plan.class_name
                response_ctx = ctx.with_planned_response_item_plan(
                    planned_response_schemas.response_item_plans.get(operation_id)
                )
                if method == "get":
                    item_schema = _get_paginated_wrapper_item_schema(response_schema)
                    if item_schema is not None:
                        item_plan = planned_response_schemas.response_item_plans.get(operation_id)
                        item_class_name = (
                            item_plan.class_name
                            if item_plan is not None
                            else class_name + "ItemsItem"
                        )
                        item_result = _generate_schema_class(
                            response_ctx.nested("items"),
                            class_name=item_class_name,
                            schema=item_schema,
                            description=(
                                item_plan.description
                                if item_plan is not None
                                else f"Schema for {item_class_name}."
                            ),
                        )
                        if item_result.status != SchemaStatus.SKIPPED:
                            state.response_item_schemas[operation_id] = [
                                item_result.class_name or item_class_name
                            ]
                            continue

                result = _generate_schema_class(
                    response_ctx,
                    class_name=class_name,
                    schema=response_schema,
                    description=response_plan.description,
                )
                if result.status != SchemaStatus.SKIPPED:
                    state.response_schemas[operation_id] = class_name
                    if result.item_class_names:
                        state.response_item_schemas[operation_id] = result.item_class_names
                    if result.is_array:
                        state.list_response_schemas.add(class_name)
                else:
                    state.untyped_response_operations.add(operation_id)

            # Generate request body schemas
            _generate_request_body_schemas(
                ctx,
                operation=operation,
                request_body_schemas=state.request_body_schemas,
            )

    _validate_spec_overrides(
        spec_overrides,
        consumed_overrides,
        consumed_required_overrides,
        spec_operation_ids,
    )

    _write_schema_files(
        schemas=state.schemas,
        schema_to_scope=state.schema_to_scope,
        templates=templates,
        output_dir=output_dir,
    )
    return SchemaRegistry(
        schema_names=set(state.schemas.keys()),
        response_schemas=state.response_schemas,
        response_item_schemas=state.response_item_schemas,
        untyped_response_ops=state.untyped_response_operations,
        request_body_schemas=state.request_body_schemas,
        list_response_schemas=state.list_response_schemas,
    )


def _generate_request_body_schemas(
    ctx: GenerationContext,
    *,
    operation: Operation,
    request_body_schemas: dict[tuple[str, str], RequestBodyParamSchema],
) -> None:
    """Generate schemas for request body parameters that are objects or arrays."""
    operation_id = operation.operationId
    if not operation_id:
        return

    request_body = operation.requestBody
    if not request_body:
        return

    if isinstance(request_body, Reference):
        raise ValueError(f"Operation {operation_id} has a reference request body")

    json_content = request_body.content.get("application/json")
    if not json_content:
        raise ValueError(f"Operation {operation_id} has no JSON content")

    content_schema = json_content.media_type_schema
    if isinstance(content_schema, Reference) or not content_schema:
        raise ValueError(f"Operation {operation_id} has no schema or schema is a reference")

    # Response-specific overrides (required_fields, response_fields, extra_fields) must not
    # influence request body parameter schemas.
    req_ctx = GenerationContext(
        schemas=ctx.schemas,
        schema_to_scope=ctx.schema_to_scope,
        schema_fingerprints=ctx.schema_fingerprints,
        nested_override_states=ctx.nested_override_states,
        scope=ctx.scope,
        operation_id=ctx.operation_id,
        spec_overrides=None,
        consumed_overrides=ctx.consumed_overrides,
        consumed_required_overrides=ctx.consumed_required_overrides,
    )

    properties = content_schema.properties or {}
    for property_name, property_schema in properties.items():
        if isinstance(property_schema, Reference):
            raise ValueError(f"Operation {operation_id} has a reference property: {property_name}")

        schema_dict = property_schema.model_dump(exclude_none=True)
        base_class_name = get_request_param_schema_name(operation_id, property_name)

        param_schema = _generate_request_body_param_schema(
            req_ctx,
            base_class_name=base_class_name,
            schema_dict=schema_dict,
            property_name=property_name,
        )
        if param_schema:
            request_body_schemas[(operation_id, property_name)] = param_schema


def _generate_request_body_param_schema(
    ctx: GenerationContext,
    *,
    base_class_name: str,
    schema_dict: dict[str, Any],
    property_name: str,
) -> RequestBodyParamSchema | None:
    """Generate schema for a single request body parameter if it's a complex type."""
    schema_type = schema_dict.get("type")

    if schema_type == "object":
        return _generate_request_body_object_schema(
            ctx,
            base_class_name=base_class_name,
            schema_dict=schema_dict,
            property_name=property_name,
        )
    if schema_type == "array":
        return _generate_request_body_array_schema(
            ctx,
            base_class_name=base_class_name,
            schema_dict=schema_dict,
            property_name=property_name,
        )
    return None


def _generate_request_body_object_schema(
    ctx: GenerationContext,
    *,
    base_class_name: str,
    schema_dict: dict[str, Any],
    property_name: str,
) -> RequestBodyParamSchema | None:
    """Generate schema for an object-type request body parameter."""
    if schema_dict.get("properties"):
        result = _generate_schema_class(ctx, class_name=base_class_name, schema=schema_dict)
        if result.status != SchemaStatus.SKIPPED:
            return RequestBodyParamSchema(class_name=result.class_name or base_class_name)
        return None

    additional_props = schema_dict.get("additionalProperties")
    if isinstance(additional_props, dict) and _has_nested_properties(additional_props):
        value_class_name = base_class_name + "Value"
        result = _generate_schema_class(
            ctx,
            class_name=value_class_name,
            schema=additional_props,
            description=f"Value schema for {property_name}.",
        )
        if result.status != SchemaStatus.SKIPPED:
            return RequestBodyParamSchema(
                class_name=f"dict[str, {result.class_name or value_class_name}]",
                is_dict=True,
                item_class_name=result.class_name or value_class_name,
            )
    return None


def _generate_request_body_array_schema(
    ctx: GenerationContext,
    *,
    base_class_name: str,
    schema_dict: dict[str, Any],
    property_name: str,
) -> RequestBodyParamSchema | None:
    """Generate schema for an array-type request body parameter."""
    items = schema_dict.get("items", {})
    if not _has_nested_properties(items):
        return None

    item_class_name = base_class_name + "Item"
    result = _generate_schema_class(
        ctx,
        class_name=item_class_name,
        schema=items,
        description=f"Item schema for {property_name}.",
    )
    if result.status != SchemaStatus.SKIPPED:
        return RequestBodyParamSchema(
            class_name=f"list[{result.class_name or item_class_name}]",
            is_list=True,
            item_class_name=result.class_name or item_class_name,
        )
    return None


def _apply_inject_response_schema(
    operation_id: str, schema: dict[str, Any], inject_response_schema: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    """Apply inject_response_schema override if needed.

    For endpoints where spec has a bare {type: object} with no properties.
    Logs warning if endpoint appears to be fixed in spec.
    """
    if operation_id not in inject_response_schema:
        return schema

    if schema.get("properties"):
        log.warning(
            f"{operation_id} in inject_response_schema already has properties in spec - "
            "spec may be fixed, check if override still needed"
        )
        return schema

    return inject_response_schema[operation_id]


def _apply_force_array_response(
    operation_id: str, schema: dict[str, Any], force_array_response: set[str]
) -> dict[str, Any]:
    """Apply force_array_response override if needed.

    For endpoints where spec says object but API returns array.
    Logs warning if endpoint appears to be fixed in spec.
    """
    if operation_id not in force_array_response:
        return schema

    if schema.get("type") == "array":
        log.warning(
            f"{operation_id} in force_array_response already has array schema - "
            "spec may be fixed, check if override still needed"
        )
        return schema

    # Wrap object schema in array
    return {"type": "array", "items": schema}


def _normalize_paginated_response_schema(
    *,
    operation_id: str,
    schema: dict[str, Any],
    force_paginated_items_schema: set[str],
) -> dict[str, Any]:
    """Normalize malformed paginated response schema shapes.

    Some endpoints incorrectly define paginated responses as:
        array[object{items: array[...], meta: object}]
    even though the API response body is the wrapper object itself.

    The SDK pagination layer already handles wrapper extraction, so client-visible
    response models should use the nested `items` schema directly.
    """
    if operation_id not in force_paginated_items_schema:
        return schema

    if schema.get("type") != "array":
        log.warning(
            f"{operation_id} in force_paginated_items_schema no longer has array response schema - "
            "spec may be fixed, check if override still needed"
        )
        return schema

    wrapper_schema = schema.get("items")
    if not isinstance(wrapper_schema, dict):
        log.warning(
            f"{operation_id} in force_paginated_items_schema has non-object array item schema - "
            "spec may be fixed, check if override still needed"
        )
        return schema

    wrapper_type = wrapper_schema.get("type")
    wrapper_props = wrapper_schema.get("properties")
    if wrapper_type != "object" or not isinstance(wrapper_props, dict):
        log.warning(
            f"{operation_id} in force_paginated_items_schema has unexpected wrapper schema - "
            "spec may be fixed, check if override still needed"
        )
        return schema

    # Only unwrap when the wrapper is clearly pagination metadata.
    if "items" not in wrapper_props or set(wrapper_props).difference({"items", "meta"}):
        log.warning(
            f"{operation_id} in force_paginated_items_schema has unexpected wrapper fields - "
            "spec may be fixed, check if override still needed"
        )
        return schema

    items_schema = wrapper_props.get("items")
    if not isinstance(items_schema, dict) or items_schema.get("type") != "array":
        log.warning(
            f"{operation_id} in force_paginated_items_schema has unexpected nested items schema - "
            "spec may be fixed, check if override still needed"
        )
        return schema

    log.debug(
        f"{operation_id} response schema is wrapped as array[{{items, meta}}] in spec; "
        "using nested items schema for generated response models"
    )
    return items_schema


def _get_paginated_wrapper_item_schema(schema: dict[str, Any]) -> dict[str, Any] | None:
    """Return paginated wrapper item schema for object{items,meta} responses."""
    if schema.get("type") != "object":
        return None

    properties = schema.get("properties")
    if not isinstance(properties, dict) or "items" not in properties:
        return None

    # Match wrapper-only schemas like {items, meta}.
    if set(properties).difference({"items", "meta"}):
        return None

    items_schema = properties.get("items")
    if not isinstance(items_schema, dict) or items_schema.get("type") != "array":
        return None

    item_schema = items_schema.get("items")
    return item_schema if isinstance(item_schema, dict) else None


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
    should_generate_nested = _has_nested_properties(value_schema)
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
        item_plan = (
            ctx.planned_response_item_plan
            if ctx.depth == 0 and not ctx.field_path and ctx.planned_response_item_plan is not None
            else None
        )
        planned_class_name = item_plan.class_name if item_plan is not None else nested_class_name
        result = _generate_schema_class(
            ctx.nested(),
            class_name=planned_class_name,
            schema=inner_schema,
            description=item_plan.description if item_plan is not None else None,
        )
        if result.status != SchemaStatus.SKIPPED:
            generated_class_name = result.class_name or planned_class_name
            return f'"{generated_class_name}"', generated_class_name
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
                f"Skipping schema generation for {class_name} "
                "because it has no properties or additional properties"
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
    list_field_names: list[str] = []

    for prop_name, prop_schema in properties.items():
        is_required_in_spec = prop_name in required
        is_force_required = _is_field_force_required(
            ctx, prop_name, is_required_in_spec=is_required_in_spec
        )
        field = _generate_field(
            ctx,
            parent_class=class_name,
            prop_name=prop_name,
            prop_schema=prop_schema,
            is_required=is_required_in_spec or is_force_required,
        )
        lines.append(f"    {field.definition}")
        if field.item_class:
            item_class_names.append(field.item_class)
        if field.is_list:
            list_field_names.append(_sanitize_field_name(prop_name))

    # Add extra fields from overrides (fields missing from spec but present in API responses)
    for field_name, field_type in _get_extra_fields(ctx, set(properties.keys())):
        is_force_required = _is_field_force_required(ctx, field_name, is_required_in_spec=False)
        lines.append(
            f"    {_format_field_definition(field_name, field_type, is_required=is_force_required)}"
        )
        if _is_plain_list(field_type, is_required=is_force_required, is_nullable=False):
            list_field_names.append(_sanitize_field_name(field_name))

    # The API returns null for some array fields, coerce those to an empty list
    if list_field_names:
        names = ", ".join(f'"{name}"' for name in list_field_names)
        lines.extend(
            [
                "",
                f'    @field_validator({names}, mode="before")',
                "    @classmethod",
                "    def coerce_null_lists(cls, value: Any) -> Any:",
                '        """Convert null array values from the API to empty lists."""',
                "        return [] if value is None else value",
            ]
        )

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
            if ctx.allow_schema_overwrite:
                ctx.schemas[name] = definition
                ctx.schema_to_scope[name] = ctx.scope
                return SchemaStatus.GENERATED
            raise ValueError(
                f"Schema collision: '{name}' in scope '{ctx.scope}' has conflicting definitions"
            )
        return SchemaStatus.DEDUPED

    ctx.schemas[name] = definition
    ctx.schema_to_scope[name] = ctx.scope
    return SchemaStatus.GENERATED


def _get_field_override(
    ctx: GenerationContext, prop_name: str, prop_schema: dict[str, Any]
) -> str | None:
    """Check if there's a type override for this field and return the override type."""
    if not ctx.operation_id or ctx.spec_overrides is None or ctx.consumed_overrides is None:
        return None

    response_fields = ctx.spec_overrides.response_fields.get(ctx.operation_id)
    if not response_fields:
        return None

    field_path = ".".join((*ctx.field_path, prop_name))
    override_type = response_fields.get(field_path)
    if not override_type:
        return None

    spec_type = _get_simple_type(prop_schema)
    if spec_type == override_type:
        log.warning(
            f"{ctx.operation_id}: field '{field_path}' override type '{override_type}' "
            "matches spec type - spec may have been fixed"
        )

    ctx.consumed_overrides.add((ctx.operation_id, field_path))
    return override_type


def _is_field_force_required(
    ctx: GenerationContext, prop_name: str, *, is_required_in_spec: bool
) -> bool:
    """Check if a field should be forced as required via spec override.

    Returns True if there's an override marking this field as required.
    Logs a warning if the field is already required in the spec.
    """
    if (
        not ctx.operation_id
        or ctx.spec_overrides is None
        or ctx.consumed_required_overrides is None
    ):
        return False

    required_fields = ctx.spec_overrides.required_fields.get(ctx.operation_id)
    if not required_fields:
        return False

    field_path = ".".join((*ctx.field_path, prop_name))
    if field_path not in required_fields:
        return False

    if is_required_in_spec:
        log.warning(
            f"{ctx.operation_id}: field '{field_path}' is marked as required in override "
            "but is already required in spec - spec may have been fixed"
        )

    ctx.consumed_required_overrides.add((ctx.operation_id, field_path))
    return True


def _get_extra_fields(
    ctx: GenerationContext, existing_properties: set[str]
) -> list[tuple[str, str]]:
    """Get extra field definitions to add from spec overrides.

    Returns list of (field_name, type_annotation) tuples for fields not in existing_properties.
    Applies to top-level response schemas: depth=0 for object responses, depth<=1 for array items.
    Logs warning if a field already exists in the spec.
    """
    if not ctx.operation_id or ctx.spec_overrides is None or ctx.depth > 1 or ctx.field_path:
        return []

    extra_fields = ctx.spec_overrides.extra_fields.get(ctx.operation_id)
    if not extra_fields:
        return []

    result: list[tuple[str, str]] = []
    for field_name, field_type in extra_fields.items():
        if field_name in existing_properties:
            log.warning(
                f"{ctx.operation_id}: extra_field '{field_name}' already exists in spec - "
                "use 'response' override to change its type instead"
            )
        else:
            result.append((field_name, field_type))

    return result


def _consume_schema_overrides(ctx: GenerationContext, schema: dict[str, Any]) -> None:
    """Traverse a schema to consume applicable response and required overrides."""
    properties = schema.get("properties", {})
    if not properties:
        return

    required = set(schema.get("required", []))
    for prop_name, prop_schema in properties.items():
        is_required_in_spec = prop_name in required
        _get_field_override(ctx, prop_name, prop_schema)
        _is_field_force_required(ctx, prop_name, is_required_in_spec=is_required_in_spec)

        if prop_schema.get("type") == "array":
            items = prop_schema.get("items", {})
            if _has_nested_properties(items):
                _consume_schema_overrides(ctx.nested(prop_name), items)
            continue

        if (prop_schema.get("type") == "object" or "properties" in prop_schema) and prop_schema.get(
            "properties"
        ):
            _consume_schema_overrides(ctx.nested(prop_name), prop_schema)

    for field_name, _field_type in _get_extra_fields(ctx, set(properties.keys())):
        _is_field_force_required(ctx, field_name, is_required_in_spec=False)


def _format_field_definition(
    prop_name: str, type_str: str, *, is_required: bool, is_nullable: bool = False
) -> str:
    """Format a field definition for both spec-defined and extra fields."""
    snake_name = _sanitize_field_name(prop_name)
    needs_alias = snake_name != prop_name
    is_list = type_str.startswith("list[")
    alias_args = f'validation_alias="{prop_name}", serialization_alias="{prop_name}"'

    if is_required:
        type_annotation = f"{type_str} | None" if is_nullable else type_str
        if needs_alias:
            return f"{snake_name}: {type_annotation} = Field({alias_args})"
        return f"{snake_name}: {type_annotation}"

    if needs_alias:
        if is_list:
            return f"{snake_name}: {type_str} = Field(default_factory=list, {alias_args})"
        return f"{snake_name}: {type_str} | None = Field(default=None, {alias_args})"
    if is_list:
        return f"{snake_name}: {type_str} = Field(default_factory=list)"
    return f"{snake_name}: {type_str} | None = None"


def _generate_field(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    prop_schema: dict[str, Any],
    is_required: bool,
) -> FieldResult:
    """Generate a field definition for a Pydantic model."""
    override_type = _get_field_override(ctx, prop_name, prop_schema)
    if override_type:
        type_str = override_type
        item_class = None
    else:
        type_str, item_class = _get_python_type(
            ctx, parent_class=parent_class, prop_name=prop_name, schema=prop_schema
        )

    is_nullable = prop_schema.get("nullable", False)
    return FieldResult(
        definition=_format_field_definition(
            prop_name, type_str, is_required=is_required, is_nullable=is_nullable
        ),
        item_class=item_class,
        is_list=_is_plain_list(type_str, is_required=is_required, is_nullable=is_nullable),
    )


def _is_plain_list(type_str: str, *, is_required: bool, is_nullable: bool) -> bool:
    """Whether the field is annotated as a list that cannot hold None."""
    return type_str.startswith("list[") and not (is_required and is_nullable)


def _get_python_type(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    schema: dict[str, Any],
) -> TypeResult:
    """Get Python type annotation from OpenAPI schema."""
    schema_type = schema.get("type")

    if schema_type in ("string", "integer", "number", "boolean"):
        return TypeResult(_get_simple_type(schema))

    if schema_type == "array":
        return _get_array_type(ctx, parent_class=parent_class, prop_name=prop_name, schema=schema)

    if schema_type == "object":
        return _get_object_type(ctx, parent_class=parent_class, prop_name=prop_name, schema=schema)

    log.warning(f"Unknown schema type: {schema_type}")
    return TypeResult("Any")


def _ensure_deduped_nested_schema(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    schema: dict[str, Any],
    is_array: bool,
) -> str:
    """Generate or refresh a structurally deduplicated nested schema."""
    nested_ctx = ctx.nested(prop_name)
    fingerprint = _compute_fingerprint(schema, ctx.scope)
    current_state = _get_applicable_nested_override_state(nested_ctx)
    merged_state, changed = _merge_nested_override_state(
        nested_ctx.nested_override_states.get(fingerprint), current_state
    )
    nested_ctx.nested_override_states[fingerprint] = merged_state

    existing_class = nested_ctx.schema_fingerprints.get(fingerprint)
    if existing_class is not None:
        if changed and merged_state.has_overrides():
            _generate_schema_class(
                _with_relative_nested_overrides(
                    nested_ctx, merged_state, allow_schema_overwrite=True
                ),
                class_name=existing_class,
                schema=schema,
            )
        if current_state.has_overrides():
            _consume_schema_overrides(nested_ctx, schema)
        return existing_class

    nested_class = _build_nested_class_name(
        nested_ctx, parent_class=parent_class, prop_name=prop_name, is_array=is_array
    )
    generation_ctx = (
        _with_relative_nested_overrides(nested_ctx, merged_state, allow_schema_overwrite=False)
        if merged_state.has_overrides()
        else nested_ctx
    )
    _generate_schema_class(generation_ctx, class_name=nested_class, schema=schema)
    nested_ctx.schema_fingerprints[fingerprint] = nested_class

    if current_state.has_overrides():
        _consume_schema_overrides(nested_ctx, schema)

    return nested_class


def _get_simple_type(schema: dict[str, Any]) -> str:
    """Get Python type for simple (non-class) schema types."""
    schema_type = schema.get("type")
    schema_format = schema.get("schema_format") or schema.get("format")
    if schema_format and schema_format not in FORMAT_MAP:
        log.warning(f"Unknown schema format: {schema_format}")
    if schema_type == "string" and schema_format in FORMAT_MAP:
        return FORMAT_MAP[schema_format]
    if schema_type in TYPE_MAP:
        return TYPE_MAP[schema_type]
    if schema_type == "array":
        item_type = _get_simple_type(schema.get("items", {}))
        return f"list[{item_type}]"
    if schema_type == "object":
        return "dict[str, Any]"
    log.warning(f"Unknown schema type: {schema_type}")
    return "Any"


def _get_array_type(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    schema: dict[str, Any],
) -> TypeResult:
    """Get Python type for array schema."""
    items = schema.get("items", {})

    if _has_nested_properties(items):
        nested_class = _ensure_deduped_nested_schema(
            ctx,
            parent_class=parent_class,
            prop_name=prop_name,
            schema=items,
            is_array=True,
        )
        return TypeResult(f"list[{nested_class}]", nested_class)

    item_type = _get_simple_type(items)
    return TypeResult(f"list[{item_type}]")


def _get_object_type(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    schema: dict[str, Any],
) -> TypeResult:
    """Get Python type for object schema."""
    props = schema.get("properties")

    if not props:
        return TypeResult("dict[str, Any]")

    nested_class = _ensure_deduped_nested_schema(
        ctx,
        parent_class=parent_class,
        prop_name=prop_name,
        schema=schema,
        is_array=False,
    )
    return TypeResult(nested_class)


def _build_nested_class_name(
    ctx: GenerationContext,
    *,
    parent_class: str,
    prop_name: str,
    is_array: bool,
) -> str:
    """Build a nested class name with scope-aware shortening."""
    prop_pascal = capitalize_first(prop_name)
    suffix = "Item" if is_array else ""
    full_name = _sanitize_class_name(parent_class + prop_pascal + suffix)

    should_shorten = ctx.depth >= 2 or len(full_name) > MAX_CLASS_NAME_LENGTH
    if not should_shorten:
        return full_name

    scope_prefix = capitalize_first(ctx.scope)
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


def _is_object_schema(schema: dict[str, Any]) -> bool:
    """Check if schema generates an object model class."""
    return schema.get("type") == "object" or "properties" in schema


def _has_nested_properties(schema: dict[str, Any]) -> bool:
    """Check if schema is an object with properties requiring a generated class."""
    return schema.get("type") == "object" and bool(schema.get("properties"))


def _sanitize_field_name(name: str) -> str:
    """Sanitize a field name to be a valid Python identifier."""
    if name and (name[0].isdigit() or name.replace(".", "").replace("-", "").isdigit()):
        return "n_" + name.replace(".", "_").replace("-", "_").replace("/", "_")
    if "/" in name:
        return escape_reserved_name(name.replace("/", "_").lower())
    return escape_reserved_name(to_snake_case(name))


def _sanitize_class_name(name: str) -> str:
    """Sanitize a class name to be a valid Python identifier."""
    parts = re.split(r"[/_]", name)
    name = "".join(capitalize_first(p) if p else "" for p in parts)
    return "N" + name if name and name[0].isdigit() else name


@overload
def _format_docstring(doc: str, *, as_lines: Literal[True]) -> list[str]: ...


@overload
def _format_docstring(doc: str, *, as_lines: Literal[False] = False) -> str: ...


def _format_docstring(doc: str, *, as_lines: bool = False) -> str | list[str]:
    """Format a docstring for a schema class with proper line wrapping."""
    if not doc:
        return [] if as_lines else ""

    doc = sanitize_text(doc)
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


def _compute_fingerprint(schema: dict[str, Any], scope: str) -> str:
    """Compute a fingerprint for schema deduplication within a scope."""
    normalized = _normalize_schema(schema)
    return f"{scope}:{json.dumps(normalized, sort_keys=True)}"


def _normalize_schema(schema: dict[str, Any], *, is_required: bool = False) -> dict[str, Any]:
    """Normalize schema to only include fields that affect generated code structure."""
    result: dict[str, Any] = {}

    if "type" in schema:
        result["type"] = schema["type"]

    schema_format = schema.get("schema_format") or schema.get("format")
    if schema_format:
        result["format"] = schema_format

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


def _validate_spec_overrides(
    spec_overrides: SpecOverrides,
    consumed_overrides: set[tuple[str, str]],
    consumed_required_overrides: set[tuple[str, str]],
    spec_operation_ids: set[str],
) -> None:
    """Validate that all spec overrides reference valid operations and fields."""
    # Validate force_array_response
    for operation_id in spec_overrides.force_array_response:
        if operation_id not in spec_operation_ids:
            raise ValueError(
                f"force_array_response references unknown operation '{operation_id}'. "
                "Check that the operationId exists in the OpenAPI spec."
            )

    # Validate force_paginated
    for operation_id in spec_overrides.force_paginated:
        if operation_id not in spec_operation_ids:
            raise ValueError(
                f"force_paginated references unknown operation '{operation_id}'. "
                "Check that the operationId exists in the OpenAPI spec."
            )

    # Validate force_paginated_items_schema
    for operation_id in spec_overrides.force_paginated_items_schema:
        if operation_id not in spec_operation_ids:
            raise ValueError(
                f"force_paginated_items_schema references unknown operation '{operation_id}'. "
                "Check that the operationId exists in the OpenAPI spec."
            )

    # Validate response field overrides
    for operation_id, fields in spec_overrides.response_fields.items():
        if operation_id not in spec_operation_ids:
            raise ValueError(
                f"Response field override references unknown operation '{operation_id}'. "
                "Check that the operationId exists in the OpenAPI spec."
            )

        for field_path in fields:
            if (operation_id, field_path) not in consumed_overrides:
                raise ValueError(
                    f"Response field override for '{operation_id}' field '{field_path}' was not applied. "
                    "Check that the field path exists in the response schema."
                )

    # Validate required field overrides
    for operation_id, fields in spec_overrides.required_fields.items():
        if operation_id not in spec_operation_ids:
            raise ValueError(
                f"Required field override references unknown operation '{operation_id}'. "
                "Check that the operationId exists in the OpenAPI spec."
            )

        for field_path in fields:
            if (operation_id, field_path) not in consumed_required_overrides:
                raise ValueError(
                    f"Required field override for '{operation_id}' field '{field_path}' was not applied. "
                    "Check that the field path exists in the response schema."
                )

    # Validate extra field overrides (only check operation exists, fields are always added)
    for operation_id in spec_overrides.extra_fields:
        if operation_id not in spec_operation_ids:
            raise ValueError(
                f"Extra field override references unknown operation '{operation_id}'. "
                "Check that the operationId exists in the OpenAPI spec."
            )

    # Validate inject_response_schema overrides
    for operation_id in spec_overrides.inject_response_schema:
        if operation_id not in spec_operation_ids:
            raise ValueError(
                f"inject_response_schema references unknown operation '{operation_id}'. "
                "Check that the operationId exists in the OpenAPI spec."
            )


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
        scope = schema_to_scope[class_name]
        schemas_by_scope.setdefault(scope, {})[class_name] = class_def

    with open(f"{output_dir}/schemas/_base.py", "w") as f:
        f.write(templates.schema_base_template.render())

    all_exports: dict[str, list[str]] = {}
    for scope, scope_schemas in schemas_by_scope.items():
        module_name = to_snake_case(scope)
        sorted_schemas = sorted(scope_schemas.keys())
        all_exports[module_name] = sorted(sorted_schemas)

        schema_definitions = [scope_schemas[name] for name in sorted_schemas]
        with open(f"{output_dir}/schemas/_{module_name}.py", "w") as f:
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
