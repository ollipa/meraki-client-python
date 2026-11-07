#!/usr/bin/env python3
"""Print the CHANGELOG.md section for a release version."""

import argparse
import re
import sys
from pathlib import Path

CHANGELOG = Path(__file__).parent.parent / "CHANGELOG.md"


def get_release_notes(version: str, changelog: Path = CHANGELOG) -> str:
    """Extract changelog content for a specific version."""
    content = changelog.read_text()
    pattern = rf"^## v{re.escape(version)}\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    if not match:
        return ""
    return match.group(1).strip()


def has_entries(notes: str) -> bool:
    """Return whether changelog notes contain at least one non-empty list entry."""
    return re.search(r"^- +\S", notes, re.MULTILINE) is not None


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="Release version without the v prefix, e.g. 0.23.0")
    args = parser.parse_args()

    notes = get_release_notes(args.version)
    if not has_entries(notes):
        print(f"No changelog entries found for v{args.version}.", file=sys.stderr)
        sys.exit(1)
    print(notes)


if __name__ == "__main__":
    main()
