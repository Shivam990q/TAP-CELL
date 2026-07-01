"""Compile a resume .tex with Tectonic and verify it fits on one page.

Usage:
    python tools/build_resume.py 04-resume/tailored/josh-tech-frontend-2027.tex
    python tools/build_resume.py <tex> --pages 1 --preview

- Compiles with tectonic, reads the log for the page count.
- Fails (exit 1) if page count != expected (default 1).
- With --preview, renders preview-1.png (and more) next to the PDF via pdftoppm.
- Cleans up the .log afterwards.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _common import ROOT, run


FA_STUB = "\n".join(
    r"\providecommand{\fa%s}{\textbullet}" % n
    for n in ["MapMarker", "Phone", "Envelope", "Linkedin", "Github", "Globe", "Map"]
)


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def _run_tectonic(tex: Path):
    res = run(["tectonic", "--keep-logs", str(tex)], cwd=tex.parent)
    log = tex.with_suffix(".log")
    text = _read(log) if log.exists() else ""
    combined = text + "\n" + res.stderr + "\n" + res.stdout
    m = re.search(r"\((\d+)\s+page", combined)
    if log.exists():
        log.unlink()
    return (int(m.group(1)) if m else -1), combined, res


def compile_tex(tex: Path):
    """Return (page_count, stubbed). Falls back to a FontAwesome-stubbed copy if the
    real compile fails locally (tectonic can't load FA fonts on some setups)."""
    pages, combined, res = _run_tectonic(tex)
    if res.returncode == 0 and pages != -1:
        return pages, False

    src = _read(tex)
    if r"\usepackage{fontawesome5}" in src:
        tmp = tex.with_name(tex.stem + "__localverify.tex")
        tmp.write_text(src.replace(r"\usepackage{fontawesome5}", FA_STUB),
                       encoding="utf-8", newline="\n")
        try:
            pages2, _, res2 = _run_tectonic(tmp)
            tmp_pdf = tmp.with_suffix(".pdf")
            if res2.returncode == 0 and tmp_pdf.exists():
                tmp_pdf.replace(tex.with_suffix(".pdf"))
                return pages2, True
        finally:
            for junk in (tmp, tmp.with_suffix(".pdf")):
                if junk.exists():
                    junk.unlink()

    print("COMPILE FAILED:")
    for line in combined.splitlines()[-25:]:
        print("  " + line)
    return -1, False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("tex", help="path to .tex (relative to repo root or absolute)")
    ap.add_argument("--pages", type=int, default=1, help="expected page count (default 1)")
    ap.add_argument("--preview", action="store_true", help="render PNG preview(s)")
    ap.add_argument("--dpi", type=int, default=130)
    args = ap.parse_args()

    tex = Path(args.tex)
    if not tex.is_absolute():
        tex = (ROOT / tex).resolve()
    if not tex.exists():
        print(f"Not found: {tex}")
        sys.exit(1)

    pages, stubbed = compile_tex(tex)
    pdf = tex.with_suffix(".pdf")
    if pages == -1:
        sys.exit(1)

    ok = pages == args.pages
    status = "OK" if ok else "WARNING"
    note = "  [icons stubbed locally; real FontAwesome icons render on Overleaf]" if stubbed else ""
    print(f"[{status}] {tex.name}: {pages} page(s) (expected {args.pages}) -> {pdf.name}{note}")

    if args.preview and pdf.exists():
        for old in pdf.parent.glob("preview*.png"):
            old.unlink()
        run(["pdftoppm", "-png", "-r", str(args.dpi), str(pdf), str(pdf.parent / "preview")])
        previews = sorted(p.name for p in pdf.parent.glob("preview*.png"))
        print("  preview: " + ", ".join(previews))

    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
