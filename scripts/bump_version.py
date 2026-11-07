#!/usr/bin/env python3
"""Bump the version and open a release pull request.

Merging the pull request publishes the release from CI (after approval of the
`pypi` environment) and creates the tag and GitHub release.
"""
# ruff: noqa: S603, S607

import argparse
import re
import subprocess
import sys
from pathlib import Path

from release_notes import get_release_notes, has_entries

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


def check_unreleased_notes() -> None:
    """Check that the Unreleased section of CHANGELOG.md has content."""
    content = CHANGELOG.read_text()
    match = re.search(r"^## Unreleased\n(.*?)(?=^## |\Z)", content, re.DOTALL | re.MULTILINE)
    if not match or not has_entries(match.group(1)):
        print("Error: The Unreleased section of CHANGELOG.md has no entries.")
        sys.exit(1)


def check_release_branch_free(branch: str) -> None:
    """Check that the release branch doesn't exist locally or on origin."""
    local = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"refs/heads/{branch}"],
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    remote = subprocess.run(
        ["git", "ls-remote", "--exit-code", "--heads", "origin", branch],
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    # ls-remote --exit-code returns 2 when the branch doesn't exist; anything else is an error.
    if remote.returncode not in (0, 2):
        print(f"Error: Could not check origin for branch '{branch}'.")
        sys.exit(1)
    if local.returncode == 0 or remote.returncode == 0:
        print(f"Error: Branch '{branch}' already exists locally or on origin.")
        sys.exit(1)


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


def show_diff() -> None:
    """Show the git diff of changes."""
    subprocess.run(["git", "diff"], check=True, cwd=ROOT)


def confirm() -> bool:
    """Ask user to confirm the changes."""
    response = input("\nCommit these changes and open a release PR? [y/N] ")
    return response.lower() in ("y", "yes")


def git_commit(branch: str, new_version: str) -> None:
    """Commit the version bump changes on a new release branch."""
    subprocess.run(["git", "switch", "-c", branch], check=True, cwd=ROOT)
    subprocess.run(["git", "add", "."], check=True, cwd=ROOT)
    subprocess.run(
        ["git", "commit", "-m", f"Bump version to v{new_version}"],
        check=True,
        cwd=ROOT,
    )


def open_release_pr(branch: str, new_version: str) -> None:
    """Push the release branch and open a pull request against main."""
    subprocess.run(["git", "push", "--set-upstream", "origin", branch], check=True, cwd=ROOT)
    body = (
        f"Release v{new_version}.\n\n"
        "Merging this PR publishes the release to PyPI after the `pypi` environment "
        "deployment is approved, then creates the tag and GitHub release.\n\n"
        f"## Release notes\n\n{get_release_notes(new_version, CHANGELOG)}\n"
    )
    subprocess.run(
        [
            "gh",
            "pr",
            "create",
            "--base",
            MAIN_BRANCH,
            "--head",
            branch,
            "--title",
            f"Release v{new_version}",
            "--body",
            body,
        ],
        check=True,
        cwd=ROOT,
    )


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Bump the project version")
    parser.add_argument("bump_type", choices=["major", "minor", "patch"], help="Version bump type")
    args = parser.parse_args()

    check_git_clean()
    check_on_main_branch()
    check_unreleased_notes()

    major, minor, patch = get_current_version()
    new_major, new_minor, new_patch = bump_version(major, minor, patch, args.bump_type)
    new_version = f"{new_major}.{new_minor}.{new_patch}"
    branch = f"release/v{new_version}"
    check_release_branch_free(branch)

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

    try:
        git_commit(branch, new_version)
    except subprocess.CalledProcessError:
        print(
            f"\nError: Failed to commit the version bump on '{branch}'. To start over, discard "
            f"the changes (`git reset --hard`), then `git switch {MAIN_BRANCH}` and "
            f"`git branch -D {branch}`."
        )
        sys.exit(1)
    try:
        open_release_pr(branch, new_version)
    except subprocess.CalledProcessError:
        print(
            f"\nError: Failed to push '{branch}' or open the pull request. The version bump is "
            f"committed on '{branch}'. Retry the push and `gh pr create --base {MAIN_BRANCH}` by "
            f"hand, or delete the branch (locally and on origin) and run this script again."
        )
        sys.exit(1)
    subprocess.run(["git", "switch", MAIN_BRANCH], check=True, cwd=ROOT)
    print(f"\nOpened release PR for v{new_version}. Merge it to publish.")


if __name__ == "__main__":
    main()
