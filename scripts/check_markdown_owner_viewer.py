#!/usr/bin/env python3
"""Validate the shared markdown owner viewer for current HTML lenses."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
CURRENT_VIEWS = ROOT / "views" / "current"
VIEWER_PATH = CURRENT_VIEWS / "markdown-owner-viewer.html"
VIEWER_NAME = "markdown-owner-viewer.html"
MD_HREF = re.compile(r"""(?<![\w-])href=(?P<q>['"])(?P<href>[^'"]+?\.md)(?P=q)""")


def fail(message: str) -> None:
    raise AssertionError(message)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def normalize_md_target(source_html: Path, href: str) -> str | None:
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return None
    candidate = (source_html.parent / href).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        return None
    if candidate.suffix == ".md" and candidate.exists():
        return rel(candidate)
    return None


def current_html_files() -> list[Path]:
    return sorted(
        path
        for path in CURRENT_VIEWS.rglob("*.html")
        if ".exports" not in path.parts and path.resolve() != VIEWER_PATH.resolve()
    )


def extract_source_pack(html: str) -> dict[str, object]:
    marker = "const sourcePack = "
    start = html.find(marker)
    if start < 0:
        fail("viewer missing embedded sourcePack")
    start += len(marker)
    end = html.find(";\n    const fallbackShareUrl", start)
    if end < 0:
        fail("viewer sourcePack terminator not found")
    try:
        payload = json.loads(html[start:end])
    except json.JSONDecodeError as exc:
        fail(f"viewer sourcePack is invalid JSON: {exc}")
    if not isinstance(payload, dict):
        fail("viewer sourcePack must be an object")
    return payload


def check_browser_scripts(path: Path, html: str) -> None:
    scripts = re.findall(r"<script(?P<attrs>[^>]*)>(?P<body>.*?)</script>", html, flags=re.DOTALL | re.IGNORECASE)
    for index, (attrs, script) in enumerate(scripts, 1):
        type_match = re.search(r"""type=['"]([^'"]+)['"]""", attrs, flags=re.IGNORECASE)
        if type_match and type_match.group(1).lower() not in {
            "text/javascript",
            "application/javascript",
            "module",
        }:
            continue
        result = subprocess.run(
            (
                "node",
                "-e",
                "const vm=require('vm');"
                "const fs=require('fs');"
                "new vm.Script(fs.readFileSync(0,'utf8'));",
            ),
            input=script,
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout).strip()
            fail(f"{rel(path)} script {index} is not browser-parseable JavaScript:\n{detail}")


def check_viewer() -> tuple[set[str], list[str]]:
    if not VIEWER_PATH.exists():
        fail(f"missing viewer: {rel(VIEWER_PATH)}")
    html = VIEWER_PATH.read_text(encoding="utf-8")
    for snippet in (
        "lens-markdown-owner-viewer-current",
        "Owner Page Viewer",
        "share-only 模式不公开 raw markdown",
        '<button type="button" class="owner-link"',
        "data-owner-path",
        "replaceState",
    ):
        if snippet not in html:
            fail(f"viewer missing required snippet: {snippet}")
    check_browser_scripts(VIEWER_PATH, html)
    source_pack = extract_source_pack(html)
    items = source_pack.get("items")
    if not isinstance(items, dict):
        fail("viewer sourcePack.items must be an object")
    for owner_path, item in items.items():
        if not (ROOT / owner_path).exists():
            fail(f"viewer packed missing owner file: {owner_path}")
        if not isinstance(item, dict) or not str(item.get("markdown", "")).strip():
            fail(f"viewer packed empty markdown for owner: {owner_path}")
    return set(items), [f"viewer OK ({len(items)} packed owners)"]


def check_current_html(packed: set[str]) -> list[str]:
    owners: set[str] = set()
    direct_md: list[str] = []
    missing_viewer_links: list[str] = []
    for html_path in current_html_files():
        html = html_path.read_text(encoding="utf-8")
        check_browser_scripts(html_path, html)
        for match in MD_HREF.finditer(html):
            target = normalize_md_target(html_path, match.group("href"))
            if target:
                direct_md.append(f"{rel(html_path)} -> {target}")
        for href in re.findall(r"""(?<![\w-])href=['"]([^'"]*markdown-owner-viewer\.html[^'"]*)['"]""", html):
            params = parse_qs(urlparse(href).query)
            target = params.get("path", [""])[0]
            if not target:
                if href.endswith(VIEWER_NAME):
                    continue
                missing_viewer_links.append(f"{rel(html_path)} -> {href}")
                continue
            owners.add(target)
            if "v=" not in href:
                missing_viewer_links.append(f"{rel(html_path)} missing v= for {target}")
            if "data-share-href=" not in html:
                missing_viewer_links.append(f"{rel(html_path)} missing data-share-href")
    if direct_md:
        fail("current HTML still links raw markdown:\n" + "\n".join(direct_md))
    if missing_viewer_links:
        fail("invalid viewer links:\n" + "\n".join(missing_viewer_links))
    missing = sorted(owners - packed)
    if missing:
        fail("viewer source pack missing linked owners:\n" + "\n".join(missing))
    return [f"current HTML OK ({len(owners)} owner links)"]


def main() -> int:
    try:
        packed, messages = check_viewer()
        messages.extend(check_current_html(packed))
    except AssertionError as exc:
        print(f"Markdown owner viewer validation failed: {exc}", file=sys.stderr)
        return 1
    print("Markdown owner viewer validation passed.")
    for message in messages:
        print(f"- {message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
