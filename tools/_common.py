"""Shared helpers for Career OS tools."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

# Repo root = parent of the tools/ directory
ROOT = Path(__file__).resolve().parents[1]

PROFILE_PATH = ROOT / "data" / "profile.json"


def load_profile() -> dict:
    """Load the structured profile (single source of truth for form-fill data)."""
    with open(PROFILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def run(cmd, cwd: Path | None = None, check: bool = False) -> subprocess.CompletedProcess:
    """Run a command, capturing text output. Returns the CompletedProcess."""
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=check,
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def read_text(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def slugify(text: str) -> str:
    keep = []
    for ch in text.lower().strip():
        if ch.isalnum():
            keep.append(ch)
        elif ch in " -_/":
            keep.append("-")
    slug = "".join(keep)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")
