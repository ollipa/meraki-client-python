"""Update CHANGELOG.md with AI-generated Meraki OpenAPI entries."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

UNRELEASED_HEADING = "## Unreleased"
CHANGED_HEADING = "### Changed"


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Update changelog with AI-generated entries.")
    parser.add_argument(
        "--api-version",
        required=True,
        help="Target Meraki OpenAPI version (for example 1.68.0).",
    )
    parser.add_argument(
        "--changelog-path",
        type=Path,
        default=Path("CHANGELOG.md"),
        help="Path to the changelog file.",
    )
    parser.add_argument(
        "--ai-output-file",
        type=Path,
        default=None,
        help="Path to ai-inference response file.",
    )
    parser.add_argument(
        "--fallback-bullet",
        default="- Generated SDK update; review diff for endpoint, parameter, and schema changes.",
        help="Fallback bullet used when AI output is unavailable or unusable.",
    )
    return parser.parse_args()


def read_text_if_exists(file_path: Path | None) -> str:
    """Read file content if path exists, otherwise return empty string."""
    if file_path is None:
        return ""
    if not file_path.exists() or not file_path.is_file():
        return ""
    return file_path.read_text().strip()


def extract_bullets(ai_output: str) -> list[str]:
    """Extract markdown bullet lines from AI output."""
    if not ai_output:
        return []

    code_block_match = re.search(r"```(?:markdown|md)?\s*\n(.*?)\n```", ai_output, re.DOTALL)
    if code_block_match:
        ai_output = code_block_match.group(1).strip()

    bullets: list[str] = []
    for raw_line in ai_output.splitlines():
        line = raw_line.rstrip()
        if line.startswith("- "):
            bullets.append(line)
            continue
        if bullets and line.startswith("  "):
            bullets.append(line)

    while bullets and not bullets[-1].strip():
        bullets.pop()
    return bullets


def ensure_fallback_bullet(fallback_bullet: str) -> str:
    """Normalize fallback bullet format."""
    fallback_bullet = fallback_bullet.strip()
    if fallback_bullet.startswith("- "):
        return fallback_bullet
    return f"- {fallback_bullet}"


def get_unreleased_bounds(changelog: str) -> tuple[int, int, int]:
    """Return start, body_start and end indices for the Unreleased section."""
    start = changelog.find(UNRELEASED_HEADING)
    if start == -1:
        raise ValueError("Could not find `## Unreleased` in changelog.")

    body_start = start + len(UNRELEASED_HEADING)
    next_version_match = re.search(r"^## v", changelog[body_start:], re.MULTILINE)
    end = body_start + next_version_match.start() if next_version_match else len(changelog)
    return start, body_start, end


def build_version_subsection(api_version: str, bullets: list[str]) -> str:
    """Build a subsection for a specific Meraki API update."""
    lines = [f"#### Update to Meraki API v{api_version}", "", *bullets]
    return "\n".join(lines).rstrip()


def upsert_changed_section(unreleased_body: str, api_version: str, bullets: list[str]) -> str:
    """Insert or replace update subsection under `### Changed`."""
    subsection = build_version_subsection(api_version, bullets)

    if unreleased_body.strip() == "-":
        unreleased_body = ""

    changed_match = re.search(rf"(?m)^{re.escape(CHANGED_HEADING)}\s*$", unreleased_body)
    if changed_match is None:
        prefix = unreleased_body.rstrip()
        if prefix:
            return f"{prefix}\n\n{CHANGED_HEADING}\n\n{subsection}\n"
        return f"\n\n{CHANGED_HEADING}\n\n{subsection}\n"

    changed_header_end = changed_match.end()
    tail = unreleased_body[changed_header_end:]
    next_section_match = re.search(r"(?m)^### ", tail)
    changed_end = (
        changed_header_end + next_section_match.start()
        if next_section_match
        else len(unreleased_body)
    )

    before_changed = unreleased_body[:changed_header_end]
    changed_content = unreleased_body[changed_header_end:changed_end].strip("\n")
    after_changed = unreleased_body[changed_end:]

    subsection_pattern = re.compile(
        rf"(?ms)^#### Update to Meraki API v{re.escape(api_version)}\n.*?(?=^#### |^### |\Z)"
    )

    if subsection_pattern.search(changed_content):
        changed_content = subsection_pattern.sub(f"{subsection}\n", changed_content).strip("\n")
    elif changed_content:
        changed_content = f"{changed_content}\n\n{subsection}"
    else:
        changed_content = subsection

    rebuilt_changed = f"{before_changed}\n\n{changed_content}\n"
    if after_changed:
        rebuilt_changed = f"{rebuilt_changed}\n{after_changed.lstrip()}"
    return rebuilt_changed


def update_changelog(changelog: str, api_version: str, bullets: list[str]) -> str:
    """Update the Unreleased section and return full changelog content."""
    _, body_start, end = get_unreleased_bounds(changelog)
    unreleased_body = changelog[body_start:end]
    updated_body = upsert_changed_section(unreleased_body, api_version, bullets).rstrip()

    tail = changelog[end:]
    if tail:
        return f"{changelog[:body_start]}{updated_body}\n\n{tail.lstrip()}"
    return f"{changelog[:body_start]}{updated_body}\n"


def main() -> None:
    """Run changelog update flow."""
    args = parse_args()
    changelog = args.changelog_path.read_text()

    ai_output = read_text_if_exists(args.ai_output_file)
    bullets = extract_bullets(ai_output)
    if not bullets:
        bullets = [ensure_fallback_bullet(args.fallback_bullet)]

    updated = update_changelog(changelog, args.api_version, bullets)
    args.changelog_path.write_text(updated)


if __name__ == "__main__":
    main()
