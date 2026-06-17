#!/usr/bin/env python3
"""Validate public HTML publish wiring."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "skills/public-html-publish/SKILL.md",
    "skills/public-html-publish/TRANSFER.md",
    "views/publication.md",
    "views/README.md",
    "skills/README.md",
    "README.md",
    ".gitignore",
)

REQUIRED_TERMS = {
    "skills/public-html-publish/SKILL.md": (
        "AcknowledgeBase",
        "public_url",
        "HTML-only",
        "host / prefix",
        "canonical path",
        "live readback",
        "denial readback",
        "multi-project",
        "multi-host",
        "blocked",
        "LifeOS",
    ),
    "skills/public-html-publish/TRANSFER.md": (
        "AcknowledgeBase",
        "LifeOS",
        "可以吸收",
        "禁止复制",
        "本仓库落位",
        "live readback",
        "public_url",
        "HTML-only",
        "blocked",
    ),
    "views/publication.md": (
        "publication-profile",
        "status: blocked",
        "AcknowledgeBase",
        "source root",
        "public_url 公式",
        "HTML Only",
        "Multi-Host Boundary",
        "Multi-Project Boundary",
        "不能声称公网完成",
    ),
    "views/README.md": (
        "views/publication",
        "public-html-publish",
        "public_url",
        "HTML-only",
    ),
    "skills/README.md": (
        "public-html-publish",
        "HTML 公开发布",
    ),
    "README.md": (
        "public-html-publish",
        "views/publication",
    ),
    ".gitignore": (
        "views/exports/",
        "views/**/.exports/",
        "views/**/*.pdf",
        "views/**/*.png",
        "views/**/*.svg",
    ),
}


def check_required_files(errors: list[str]) -> None:
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"missing public HTML publish file: {rel_path}")


def check_required_terms(errors: list[str]) -> None:
    for rel_path, terms in REQUIRED_TERMS.items():
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel_path} missing public HTML publish term: {term}")


def check_canonical_html(errors: list[str]) -> None:
    export_parts = {"exports", ".exports"}
    for path in (ROOT / "views").rglob("*.html"):
        rel = path.relative_to(ROOT)
        if export_parts.intersection(rel.parts):
            errors.append(f"canonical HTML must not live under export cache: {rel}")


def check_live_requested() -> int:
    print(
        "Public HTML publish live readback is blocked for this repository: "
        "views/publication.md has status=blocked and no host/deploy target is configured."
    )
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="run live public URL readback when configured")
    args = parser.parse_args()

    errors: list[str] = []
    check_required_files(errors)
    check_required_terms(errors)
    check_canonical_html(errors)

    if errors:
        print("Public HTML publish validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.live:
        return check_live_requested()

    print("Public HTML publish validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
