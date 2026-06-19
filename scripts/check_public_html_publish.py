#!/usr/bin/env python3
"""Validate public HTML publish wiring and live readback for Software Wiki."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import secrets
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
PROJECT_LABEL = "Software Wiki"
PUBLIC_HOST = "https://hai-macbook-pro.smartadpole.com"
PUBLIC_PREFIX = "/wiki/views"
SHARE_SEGMENT = "share"
SAMPLE_HTML = Path("current/public-html-publish-status.html")
SECRET_ENV_FILE = ROOT / ".codex" / "local" / "public-html-share.env"
SECRET_KEYS = ("PUBLIC_HTML_SHARE_SECRET", "LIFEOS_PUBLIC_SHARE_SECRET")
REQUIRED_FILES = ('.gitignore', 'governance/public-html-publish-rules.md', 'skills/public-html-publish/SKILL.md', 'skills/public-html-publish/TRANSFER.md', 'templates/public-html-publication-template.md', 'views/README.md', 'views/current/public-html-publish-status.html', 'views/publication.md')
REQUIRED_TERMS = (
    "public_url",
    "HTML",
    "share-only",
    "host / prefix",
    "canonical path",
    "live readback",
    "denial readback",
    "multi-project",
    "multi-host",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_or_create_secret() -> str:
    if SECRET_ENV_FILE.exists():
        for line in SECRET_ENV_FILE.read_text(encoding="utf-8").splitlines():
            for key in SECRET_KEYS:
                if line.startswith(f"{key}="):
                    return line.split("=", 1)[1].strip()
    SECRET_ENV_FILE.parent.mkdir(parents=True, exist_ok=True)
    secret = secrets.token_hex(32)
    SECRET_ENV_FILE.write_text(
        "# Local only. Do not commit.\n"
        f"PUBLIC_HTML_SHARE_SECRET={secret}\n",
        encoding="utf-8",
    )
    return secret


def share_slug(secret: str, rel_path: str) -> str:
    return hmac.new(secret.encode("utf-8"), rel_path.encode("utf-8"), hashlib.sha256).hexdigest()[:24]


def share_name(secret: str, rel_path: str) -> str:
    stem = rel_path[:-5] if rel_path.endswith(".html") else rel_path
    return quote(f"{stem}--{share_slug(secret, rel_path)}.html", safe="/-_.~")


def public_url_for(rel_path: str) -> str:
    return f"{PUBLIC_HOST}{PUBLIC_PREFIX}/{SHARE_SEGMENT}/{share_name(read_or_create_secret(), rel_path)}"


def fetch(url: str) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return response.status, response.read(120_000).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read(20_000).decode("utf-8", errors="replace")
    except urllib.error.URLError as exc:
        return 0, str(exc)


def title_from_html(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "<title>" not in text or "</title>" not in text:
        return ""
    return text.split("<title>", 1)[1].split("</title>", 1)[0]


def check_static(errors: list[str]) -> None:
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"missing required file: {rel_path}")

    sample = ROOT / "views" / SAMPLE_HTML
    if not sample.exists():
        errors.append(f"missing sample HTML: views/{SAMPLE_HTML.as_posix()}")
    elif ".exports" in sample.parts or any(part.startswith(".") for part in sample.relative_to(ROOT / "views").parts):
        errors.append(f"sample HTML must be canonical and non-hidden: views/{SAMPLE_HTML.as_posix()}")

    publication_paths = [Path("views/publication.md")]
    configured_profile = Path("views/publication.md")
    if configured_profile not in publication_paths:
        publication_paths.append(configured_profile)
    for profile in publication_paths:
        path = ROOT / profile
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in ("status: live", PUBLIC_HOST, PUBLIC_PREFIX, "share-only", "live readback", "denial readback"):
            if term not in text:
                errors.append(f"{profile.as_posix()} missing live publication term: {term}")

    for rel_path in ("skills/public-html-publish/SKILL.md", "skills/public-html-publish/TRANSFER.md"):
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in REQUIRED_TERMS:
            if term not in text:
                errors.append(f"{rel_path} missing public HTML publish term: {term}")

    gitignore = ROOT / ".gitignore"
    if gitignore.exists():
        text = gitignore.read_text(encoding="utf-8")
        for term in ("views/**/.exports/", "views/**/*.pdf", "views/**/*.png", "views/**/*.svg"):
            if term not in text:
                errors.append(f".gitignore missing generated export guard: {term}")
        if ".codex/local" not in text and ".codex/local/*.env" not in text:
            errors.append(".gitignore missing local secret guard: .codex/local/*.env")

    views_root = ROOT / "views"
    if views_root.exists():
        for path in views_root.rglob("*.html"):
            parts = path.relative_to(views_root).parts
            if ".exports" in parts or any(part.startswith(".") for part in parts):
                continue
            if not share_name(read_or_create_secret(), path.relative_to(views_root).as_posix()).endswith(".html"):
                errors.append(f"public share name is not HTML: {rel(path)}")


def check_live(errors: list[str]) -> None:
    sample = ROOT / "views" / SAMPLE_HTML
    rel_path = SAMPLE_HTML.as_posix()
    url = public_url_for(rel_path)
    status, body = fetch(url)
    if status != 200:
        errors.append(f"public URL did not return 200: {url} -> {status}; {body[:200]}")
    else:
        title = title_from_html(sample)
        if title and title not in body:
            errors.append(f"public URL body does not contain local title {title!r}: {url}")

    direct_url = f"{PUBLIC_HOST}{PUBLIC_PREFIX}/{rel_path}"
    direct_status, _ = fetch(direct_url)
    if direct_status != 404:
        errors.append(f"direct canonical path must not be public: {direct_url} -> {direct_status}")

    dir_status, _ = fetch(f"{PUBLIC_HOST}{PUBLIC_PREFIX}/")
    if dir_status != 404:
        errors.append(f"directory/root path must not be public: {PUBLIC_HOST}{PUBLIC_PREFIX}/ -> {dir_status}")

    export_url = f"{PUBLIC_HOST}{PUBLIC_PREFIX}/.exports/public-html-publish-status/index.html"
    export_status, _ = fetch(export_url)
    if export_status != 404:
        errors.append(f"export cache path must not be public: {export_url} -> {export_status}")

    if not errors:
        print(url)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="run public URL and denial readback")
    parser.add_argument("--url", action="store_true", help="print sample public URL")
    args = parser.parse_args()

    if args.url:
        print(public_url_for(SAMPLE_HTML.as_posix()))
        return 0

    errors: list[str] = []
    check_static(errors)
    if not errors and args.live:
        check_live(errors)

    if errors:
        print("Public HTML publish validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if args.live:
        print(f"Public HTML publish live validation passed for {PROJECT_LABEL}.")
    else:
        print(f"Public HTML publish validation passed for {PROJECT_LABEL}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
