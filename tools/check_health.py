"""Health check: find unfinished/placeholder items so nothing silently goes stale.

Usage:
    python tools/check_health.py

Scans the markdown knowledge base for placeholders (NEED, pending, TODO, [..], to confirm)
and verifies the expected folder structure exists. Prints a report.
"""
from __future__ import annotations

import re
from pathlib import Path

from _common import ROOT

PLACEHOLDER = re.compile(
    r"(\bNEED\b|\bpending\b|to confirm|to create|\bTODO\b|\[CGPA\]|\(confirm\)|\(pending\))",
    re.IGNORECASE,
)

EXPECTED_DIRS = [
    "01-profile", "02-experience", "03-projects", "04-resume",
    "04-resume/tailored", "05-applications", "06-job-descriptions",
    "memory", "data", "tools",
]

SCAN_DIRS = ["01-profile", "02-experience", "03-projects", "05-applications", "06-job-descriptions"]


def main() -> None:
    print("== Structure ==")
    missing = [d for d in EXPECTED_DIRS if not (ROOT / d).is_dir()]
    if missing:
        for d in missing:
            print(f"  MISSING dir: {d}")
    else:
        print("  All expected folders present.")

    print("\n== Pending / placeholder items ==")
    total = 0
    for d in SCAN_DIRS:
        for md in sorted((ROOT / d).rglob("*.md")):
            hits = []
            for i, line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if PLACEHOLDER.search(line):
                    hits.append((i, line.strip()))
            if hits:
                total += len(hits)
                print(f"\n  {md.relative_to(ROOT)} ({len(hits)})")
                for i, line in hits[:8]:
                    snippet = line[:90] + ("..." if len(line) > 90 else "")
                    print(f"    L{i}: {snippet}")
                if len(hits) > 8:
                    print(f"    ... +{len(hits) - 8} more")
    print(f"\nTotal pending markers: {total}")
    if total == 0:
        print("Clean - nothing flagged.")


if __name__ == "__main__":
    main()
