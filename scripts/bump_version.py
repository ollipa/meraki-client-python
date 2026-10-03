#!/usr/bin/env python3
"""Bump the version in pyproject.toml and CHANGELOG.md."""
# ruff: noqa: S603, S607

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
PYPROJECT = ROOT / "pyproject.toml"
CHANGELOG = ROOT / "CHANGELOG.md"
MAIN_BRANCH = "main"


def get_current_version() -> tuple[int, int, int]:
    """Get the current version from pyproject.toml."""
    content = PYPROJECT.read_text()
    match = re.search(r'^version = "(\d+)\.(\d+)\.(\d+)"', content, re.MULTILINE)
    if not match:
        raise ValueError("Could not find version in pyproject.toml")
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def bump_version(major: int, minor: int, patch: int, bump_type: str) -> tuple[int, int, int]:
    """Bump the version based on the bump type."""
    if bump_type == "major":
        return major + 1, 0, 0
    if bump_type == "minor":
        return major, minor + 1, 0
    return major, minor, patch + 1


def update_pyproject(new_version: str) -> None:
    """Update the version in pyproject.toml."""
    content = PYPROJECT.read_text()
    content = re.sub(r'^version = ".*"', f'version = "{new_version}"', content, flags=re.MULTILINE)
    PYPROJECT.write_text(content)


def update_changelog(new_version: str) -> None:
    """Update CHANGELOG.md: replace Unreleased with new version and add new Unreleased section."""
    content = CHANGELOG.read_text()
    content = content.replace("## Unreleased", f"## Unreleased\n\n-\n\n## v{new_version}")
    CHANGELOG.write_text(content)


def update_lockfile() -> None:
    """Sync dependencies with uv."""
    subprocess.run(["uv", "sync"], check=True, cwd=ROOT)


def run_codegen() -> None:
    """Run the code generator."""
    subprocess.run(["make", "generate"], check=True, cwd=ROOT)
    subprocess.run(["make", "lint"], check=True, cwd=ROOT)


def check_git_clean() -> None:
    """Check that git working directory is clean."""
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True,
        check=True,
        cwd=ROOT,
    )
    if result.stdout.strip():
        print("Error: Git working directory is not clean. Commit or stash changes first.")
        sys.exit(1)


def check_on_main_branch() -> None:
    """Check that main is checked out and in sync with origin/main."""
    branch = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True,
        check=True,
        cwd=ROOT,
    ).stdout.strip()
    if branch != MAIN_BRANCH:
        print(
            f"Error: Must be on '{MAIN_BRANCH}' branch to bump version (currently on '{branch}')."
        )
        sys.exit(1)

    subprocess.run(["git", "fetch", "origin", MAIN_BRANCH], check=True, cwd=ROOT)
    local, remote = (
        subprocess.run(
            ["git", "rev-parse", ref],
            capture_output=True,
            text=True,
            check=True,
            cwd=ROOT,
        ).stdout.strip()
        for ref in ("HEAD", f"origin/{MAIN_BRANCH}")
    )
    if local != remote:
        print(f"Error: Local '{MAIN_BRANCH}' is not in sync with 'origin/{MAIN_BRANCH}'.")
        sys.exit(1)


def get_head_sha() -> str:
    """Get the commit SHA of HEAD."""
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
        cwd=ROOT,
    ).stdout.strip()


def show_diff() -> None:
    """Show the git diff of changes."""
    subprocess.run(["git", "diff"], check=True, cwd=ROOT)


def confirm() -> bool:
    """Ask user to confirm the changes."""
    response = input("\nCommit these changes? [y/N] ")
    return response.lower() in ("y", "yes")


def git_commit(new_version: str) -> None:
    """Commit the version bump changes."""
    subprocess.run(["git", "add", "."], check=True, cwd=ROOT)
    subprocess.run(
        ["git", "commit", "-m", f"Bump version to v{new_version}"],
        check=True,
        cwd=ROOT,
    )


def git_push() -> None:
    """Push commits to remote."""
    subprocess.run(["git", "push"], check=True, cwd=ROOT)


def get_release_notes(version: str) -> str:
    """Extract changelog content for a specific version."""
    content = CHANGELOG.read_text()
    pattern = rf"## v{re.escape(version)}\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return ""
    return match.group(1).strip()


def create_github_release(version: str, target: str) -> bool:
    """Create a GitHub release at the target commit using gh CLI. Returns True if created."""
    notes = get_release_notes(version)
    print(f"\nRelease notes for v{version}:\n")
    print(notes)
    response = input("\nCreate GitHub release? [y/N] ")
    if response.lower() not in ("y", "yes"):
        return False
    subprocess.run(
        [
            "gh",
            "release",
            "create",
            f"v{version}",
            "--target",
            target,
            "--title",
            f"v{version}",
            "--notes",
            notes,
        ],
        check=True,
        cwd=ROOT,
    )
    return True


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Bump the project version")
    parser.add_argument("bump_type", choices=["major", "minor", "patch"], help="Version bump type")
    args = parser.parse_args()

    check_git_clean()
    check_on_main_branch()

    major, minor, patch = get_current_version()
    new_major, new_minor, new_patch = bump_version(major, minor, patch, args.bump_type)
    new_version = f"{new_major}.{new_minor}.{new_patch}"

    print(f"Bumping version: {major}.{minor}.{patch} -> {new_version}")

    update_pyproject(new_version)
    update_changelog(new_version)
    update_lockfile()
    run_codegen()

    show_diff()
    if not confirm():
        subprocess.run(
            ["git", "checkout", "."],
            check=True,
            cwd=ROOT,
        )
        print("Aborted.")
        sys.exit(1)

    git_commit(new_version)
    git_push()
    release_created = create_github_release(new_version, get_head_sha())
    print(f"\nBumped version to v{new_version}")
    if release_created:
        print(f"Created GitHub release v{new_version}")


if __name__ == "__main__":
    main()
