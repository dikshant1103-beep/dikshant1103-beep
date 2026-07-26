#!/usr/bin/env python3
"""Render README.md from README.tmpl.md + projects.toml + live GitHub data.

Everything between the WORK:START / WORK:END markers in the template is
replaced with a table of the featured projects, each row carrying its primary
language and the month it was last pushed. Prose stays in the template; the
project list stays in projects.toml; nothing here needs editing to add a repo.

Deliberately stdlib-only — tomllib and urllib ship with the runner's Python, so
the workflow needs no pip install step and cannot break on a dependency bump.

    python scripts/render_readme.py            # write README.md
    python scripts/render_readme.py --check    # exit 1 if it would change
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tomllib
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

IST = timezone(timedelta(hours=5, minutes=30))  # runners are UTC; the reader isn't
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OWNER = "dikshant1103-beep"
START, END = "<!-- WORK:START -->", "<!-- WORK:END -->"
API = "https://api.github.com/repos/{owner}/{repo}"


def fetch(repo: str) -> dict:
    """Repo metadata, or {} when the API is unreachable or the repo is private.

    A failed lookup must degrade to a row without metadata rather than break
    the whole README — a profile page that renders stale beats one that 404s.
    """
    req = urllib.request.Request(
        API.format(owner=OWNER, repo=repo),
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-readme-refresh",
            **(
                {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
                if os.environ.get("GITHUB_TOKEN")
                else {}
            ),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.load(resp)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"  ! {repo}: {exc}", file=sys.stderr)
        return {}


def month(iso: str | None) -> str:
    if not iso:
        return "—"
    try:
        return datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%b %Y")
    except ValueError:
        return "—"


def render_table(projects: list[dict]) -> str:
    rows = [
        "| Project | | Built with | Last push |",
        "|---|---|---|---|",
    ]
    for p in projects:
        meta = fetch(p["repo"])
        url = meta.get("html_url") or f"https://github.com/{OWNER}/{p['repo']}"
        title = f"**[{p['name']}]({url})**"
        if p.get("live"):
            title += f" · [live]({p['live']})"
        lang = meta.get("language") or "—"
        rows.append(f"| {title} | {p['blurb']} | {lang} | {month(meta.get('pushed_at'))} |")
        print(f"  · {p['repo']:<22} {lang:<12} {month(meta.get('pushed_at'))}")
    stamp = datetime.now(IST).strftime("%d %b %Y")
    rows.append("")
    rows.append(f"<sub>Table regenerated from the GitHub API — last run {stamp}.</sub>")
    return "\n".join(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if README would change")
    args = ap.parse_args()

    template = (ROOT / "README.tmpl.md").read_text()
    if START not in template or END not in template:
        print(f"template is missing {START} / {END}", file=sys.stderr)
        return 2
    with (ROOT / "projects.toml").open("rb") as fh:
        projects = tomllib.load(fh)["project"]

    print(f"rendering {len(projects)} projects:")
    head, _, rest = template.partition(START)
    _, _, tail = rest.partition(END)
    rendered = f"{head}{START}\n{render_table(projects)}\n{END}{tail}"

    target = ROOT / "README.md"
    current = target.read_text() if target.exists() else ""
    if rendered == current:
        print("README.md already current — nothing to write")
        return 0
    if args.check:
        print("README.md is out of date")
        return 1
    target.write_text(rendered)
    print(f"wrote {target} ({len(rendered)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
