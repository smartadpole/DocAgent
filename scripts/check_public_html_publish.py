#!/usr/bin/env python3
"""Validate the repository-local public HTML publication contract."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "views" / "publication.md"
REQUIRED_FILES = (
    ".gitignore",
    "governance/public-html-publish-rules.md",
    "skills/public-html-publish/SKILL.md",
    "skills/public-html-publish/TRANSFER.md",
    "templates/public-html-publication-template.md",
    "views/README.md",
    "views/publication.md",
)
SKILL_TERMS = (
    "public_url",
    "HTML",
    "host / prefix",
    "canonical path",
    "live readback",
    "denial readback",
    "multi-project",
    "multi-host",
)
PROFILE_TERMS = (
    "status: blocked",
    "host: none",
    "本仓没有已发布页面",
    "不借用其他工程",
)


def check_static(errors: list[str]) -> None:
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"missing required file: {rel_path}")

    if PROFILE.exists():
        text = PROFILE.read_text(encoding="utf-8")
        for term in PROFILE_TERMS:
            if term not in text:
                errors.append(f"views/publication.md missing blocked-profile term: {term}")
        if "smartadpole.com" in text or "PUBLIC_HTML_SHARE_SECRET" in text:
            errors.append("views/publication.md must not retain another project's host or secret contract")

    for rel_path in ("skills/public-html-publish/SKILL.md", "skills/public-html-publish/TRANSFER.md"):
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in SKILL_TERMS:
            if term not in text:
                errors.append(f"{rel_path} missing public HTML publish term: {term}")

    gitignore = ROOT / ".gitignore"
    if gitignore.exists():
        text = gitignore.read_text(encoding="utf-8")
        for term in ("views/**/.exports/", "views/**/*.pdf", "views/**/*.png", "views/**/*.svg"):
            if term not in text:
                errors.append(f".gitignore missing generated export guard: {term}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="report the blocked live-publication boundary")
    parser.add_argument("--url", action="store_true", help="report the blocked public-URL boundary")
    args = parser.parse_args()

    errors: list[str] = []
    check_static(errors)
    if errors:
        print("Public HTML publish validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if args.live or args.url:
        print(
            "BLOCKED: this repository has no configured public host or published page; "
            "no public URL can be generated or live-read back.",
            file=sys.stderr,
        )
        return 2

    print("Public HTML publish static contract passed; repository publication status is blocked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
