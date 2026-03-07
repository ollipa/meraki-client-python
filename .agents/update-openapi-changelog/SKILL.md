---
name: update-openapi-changelog
description: Generates accurate changelog bullets for Meraki OpenAPI spec updates by analyzing the generated code diff, then writes them into CHANGELOG.md. Use when reviewing or processing an OpenAPI update PR, when asked to fill in changelog bullets for a spec bump, or when CHANGELOG.md contains a TODO placeholder from an automated OpenAPI update.
---

# Update OpenAPI Changelog

Use this skill when CHANGELOG.md has a TODO placeholder from an automated OpenAPI version bump, or when you need to write changelog bullets for a generated SDK update.

## Workflow

### 1. Identify versions

```bash
# New version (already written by the update workflow)
cat .api-version

# Old version (from the previous commit)
git show HEAD~1:.api-version 2>/dev/null || git log --oneline | head -5
```

### 2. Collect the generated diff

Limit the diff to generated output only — this keeps the context focused:

```bash
git diff HEAD~1 -- meraki_client/ tests/generated/ docs/api_reference/ ':(exclude)meraki_client/aio/'
```

`meraki_client/aio/` mirrors `meraki_client/_api/` exactly, so excluding it avoids duplicate noise.

If the diff is very large (> ~500 lines), summarize it by focusing on:

- New/deleted files (new or removed endpoint modules)
- Added/removed function signatures
- Added/removed parameters and response fields

### 3. Generate bullets

Use the following prompt exactly. Fill in `old_api_version`, `new_api_version`, and `generated_diff` from the steps above.

```
[system]
You write concise, accurate changelog bullets for a generated Python SDK.
Never invent changes that are not supported by the provided diff context.

[user]
We are updating Meraki OpenAPI from v{{old_api_version}} to v{{new_api_version}}.

Generated code diff context:
{{generated_diff}}

Draft changelog bullets for:
#### Update to Meraki API v{{new_api_version}}

Requirements:
- Return ONLY markdown bullet lines that begin with "- ".
- Return 3-8 bullets.
- Focus on user-visible SDK changes from generated code.
- Prioritize:
  - added or removed endpoints
  - added or removed request parameters
  - added or removed response fields
  - removed modules
- Use operation IDs or snake_case names exactly as shown in the diff.
- If unsure, omit the item.
- No headings, no prose, no code fences.
```

### 4. Apply bullets to CHANGELOG.md

Edit `CHANGELOG.md`. Place the bullets under `### Changed` in the `## Unreleased` section:

```markdown
### Changed

#### Update to Meraki API v<new_api_version>

- <bullet 1>
- <bullet 2>
```

## Quality bar

- Do not describe internal codegen machinery — only user-visible SDK surface changes.
- If the diff shows no meaningful user-visible changes, write a single bullet: `- No user-visible SDK changes in this spec update.`
