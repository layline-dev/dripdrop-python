#!/usr/bin/env python3
"""Patch-bump the package version in all hand-maintained version sources."""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text)


def current_version() -> str:
    match = re.search(r'^version = "([0-9]+\.[0-9]+\.[0-9]+)"$', read("pyproject.toml"), re.M)
    if not match:
        raise SystemExit("Could not find [project] version in pyproject.toml")
    return match.group(1)


def patch_bump(version: str) -> str:
    major, minor, patch = (int(part) for part in version.split("."))
    return f"{major}.{minor}.{patch + 1}"


def replace_exact(path: str, old: str, new: str) -> None:
    text = read(path)
    updated = text.replace(old, new)
    if updated == text:
        raise SystemExit(f"Expected version string not found in {path}: {old}")
    write(path, updated)


def main() -> None:
    old = current_version()
    new = sys.argv[1] if len(sys.argv) > 1 else patch_bump(old)
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", new):
        raise SystemExit(f"Version must be MAJOR.MINOR.PATCH, got: {new}")

    replace_exact("pyproject.toml", f'version = "{old}"', f'version = "{new}"')
    replace_exact("setup.py", f'VERSION = "{old}"', f'VERSION = "{new}"')
    replace_exact("openapi-generator-config.yaml", f"packageVersion: {old}", f"packageVersion: {new}")

    # README.md is generated metadata, but it is also the package long description.
    # Keep it aligned so the sdist/wheel metadata mentions the version being released.
    replace_exact("README.md", f"Package version: {old}", f"Package version: {new}")

    print(new)


if __name__ == "__main__":
    main()
