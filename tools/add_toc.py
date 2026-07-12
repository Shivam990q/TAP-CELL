"""Add a clickable Table of Contents with explicit anchors to a markdown file.

Usage:
    python tools/add_toc.py 05-applications/josh-technology/josh-technology-frontend-PREP.md

- Inserts `<a id="sec-N"></a>` before each heading (levels 1-6) and a TOC block right after
  the first (title) heading, between <!-- TOC START --> / <!-- TOC END --> markers.
- Idempotent: re-running regenerates cleanly (strips old anchors/TOC first).
- Uses numeric anchors so jumps work in GitHub, VS Code preview, and Kiro alike.
- Skips headings inside fenced code blocks.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from _common import ROOT

ANCHOR_RE = re.compile(r'^<a id="sec-\d+"></a>\s*$')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')
TOC_START = "<!-- TOC START -->"
TOC_END = "<!-- TOC END -->"


def strip_previous(lines: list[str]) -> list[str]:
    out, in_toc = [], False
    for ln in lines:
        if ln.strip() == TOC_START:
            in_toc = True
            continue
        if ln.strip() == TOC_END:
            in_toc = False
            continue
        if in_toc:
            continue
        if ANCHOR_RE.match(ln):
            continue
        out.append(ln)
    return out


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python tools/add_toc.py <markdown file>")
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    if not path.exists():
        print(f"Not found: {path}")
        sys.exit(1)

    lines = strip_previous(path.read_text(encoding="utf-8").splitlines())

    # Pass 1: collect headings (skip fenced code blocks)
    headings = []  # (line_index, level, text)
    in_code = False
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEADING_RE.match(ln)
        if m:
            headings.append((i, len(m.group(1)), m.group(2)))

    if not headings:
        print("No headings found.")
        return

    # Assign ids
    ids = {idx: f"sec-{n+1}" for n, (idx, _, _) in enumerate(headings)}
    min_level = min(lvl for _, lvl, _ in headings[1:]) if len(headings) > 1 else headings[0][1]

    # Build TOC (all headings except the title = headings[0])
    toc = [TOC_START, "## Table of Contents", ""]
    for idx, lvl, text in headings[1:]:
        indent = "  " * max(0, lvl - min_level)
        clean = text.replace("[", "").replace("]", "")
        toc.append(f"{indent}- [{clean}](#{ids[idx]})")
    toc += ["", TOC_END, ""]

    # Pass 2: rebuild with anchors + inject TOC after the title heading
    out = []
    hset = {idx: (lvl, text) for idx, lvl, text in headings}
    title_idx = headings[0][0]
    for i, ln in enumerate(lines):
        if i in hset:
            out.append(f'<a id="{ids[i]}"></a>')
            out.append(ln)
            if i == title_idx:
                out.append("")
                out.extend(toc)
        else:
            out.append(ln)

    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(f"TOC added: {len(headings) - 1} entries -> {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
