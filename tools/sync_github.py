"""Sync GitHub repos -> inventory, and report what changed since last run.

Usage:
    python tools/sync_github.py

Outputs:
    03-projects/github-inventory.md   (human-readable table)
    03-projects/_github-state.json    (snapshot for change detection)
Prints added / removed / updated repos so the inventory never goes stale.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime

from _common import ROOT, run, write_text

FIELDS = "name,description,primaryLanguage,isPrivate,isFork,pushedAt,stargazerCount,url"
INVENTORY = ROOT / "03-projects" / "github-inventory.md"
STATE = ROOT / "03-projects" / "_github-state.json"


def fetch_repos() -> list[dict]:
    res = run(["gh", "repo", "list", "--limit", "500", "--json", FIELDS])
    if res.returncode != 0:
        print("ERROR: `gh repo list` failed. Is GitHub CLI authenticated? (`gh auth status`)")
        print(res.stderr.strip())
        sys.exit(1)
    return json.loads(res.stdout)


def lang(repo: dict) -> str:
    pl = repo.get("primaryLanguage")
    return pl["name"] if pl else "-"


def build_inventory_md(repos: list[dict]) -> str:
    pub = sum(1 for r in repos if not r["isPrivate"])
    priv = sum(1 for r in repos if r["isPrivate"])
    forks = sum(1 for r in repos if r["isFork"])
    lines = [
        "# GitHub Inventory - Shivam990q",
        "",
        f"Auto-generated {datetime.now():%Y-%m-%d %H:%M}. "
        f"Total: {len(repos)} repos ({pub} public, {priv} private, {forks} forks).",
        "",
        "> Regenerate anytime: `python tools/sync_github.py`",
        "",
        "| Repo | Lang | Vis | Fork | Stars | Updated | Description |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in sorted(repos, key=lambda x: x["pushedAt"], reverse=True):
        vis = "priv" if r["isPrivate"] else "pub"
        fork = "fork" if r["isFork"] else ""
        upd = (r["pushedAt"] or "").split("T")[0]
        desc = (r.get("description") or "").replace("\r", " ").replace("\n", " ").replace("|", "/")
        lines.append(
            f"| [{r['name']}]({r['url']}) | {lang(r)} | {vis} | {fork} | "
            f"{r['stargazerCount']} | {upd} | {desc} |"
        )
    return "\n".join(lines) + "\n"


def load_state() -> dict:
    if STATE.exists():
        with open(STATE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def main() -> None:
    repos = fetch_repos()
    current = {r["name"]: r["pushedAt"] for r in repos}
    previous = load_state()

    added = [n for n in current if n not in previous]
    removed = [n for n in previous if n not in current]
    updated = [n for n in current if n in previous and current[n] != previous[n]]

    write_text(INVENTORY, build_inventory_md(repos))
    write_text(STATE, json.dumps(current, indent=2, sort_keys=True) + "\n")

    print(f"Synced {len(repos)} repos -> {INVENTORY.relative_to(ROOT)}")
    if not previous:
        print("First run: saved baseline state (no diff to report).")
        return
    if added:
        print(f"\nNEW repos ({len(added)}): " + ", ".join(sorted(added)))
    if removed:
        print(f"\nREMOVED repos ({len(removed)}): " + ", ".join(sorted(removed)))
    if updated:
        print(f"\nUPDATED (new commits) ({len(updated)}): " + ", ".join(sorted(updated)))
    if not (added or removed or updated):
        print("No changes since last sync.")
    if added:
        print("\n-> Review NEW repos and add notable ones to 03-projects/_CURATED.md")


if __name__ == "__main__":
    main()
