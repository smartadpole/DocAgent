#!/usr/bin/env python3
"""Check problem-focused visual presentation wiring."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = (
    "skills/problem-focused-visual-presentation/SKILL.md",
    "skills/problem-focused-visual-presentation/TRANSFER.md",
    "templates/problem-focused-lens-template.md",
    "views/README.md",
    "views/current/README.md",
    "views/snapshots/README.md",
    "views/lens-registry.md",
)

SKILL_TERMS = (
    "views/",
    "source pack",
    "背景框",
    "证据边界",
    "confirmed",
    "likely",
    "possible",
    "blocked",
    "export_profile",
    "print_profile",
    "equivalence_profile",
    "default_auto_exports",
    "conversation_png_preview",
    "templates/problem-focused-lens-template",
    "views/lens-registry",
)

TRANSFER_TERMS = (
    "views/current/",
    "views/snapshots/",
    "views/lens-registry",
    "PDF",
    "PNG",
    "同源一致性",
    "禁止复制",
)

TEMPLATE_TERMS = (
    "lens_id",
    "focus_object",
    "lens_type",
    "judgement_purpose",
    "source_pages",
    "source_scope",
    "generated_at",
    "source_revision",
    "evidence_boundary",
    "visual_structure",
    "export_profile",
    "print_profile",
    "equivalence_profile",
    "default_auto_exports",
    "conversation_png_preview",
    "refresh_trigger",
)

VIEW_TERMS = (
    "source pack",
    "证据边界",
    "current",
    "snapshot",
    "PDF",
    "PNG",
    "gitignore",
)

GITIGNORE_TERMS = (
    "views/.exports/",
    "views/exports/",
    "views/**/.exports/",
)


def read(repo: Path, rel: str, errors: list[str]) -> str:
    path = repo / rel
    if not path.exists():
        errors.append(f"{rel}: required problem-focused presentation file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(rel: str, text: str, terms: tuple[str, ...], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{rel}: missing problem-focused presentation term {term!r}")


def check_no_tracked_exports(repo: Path, errors: list[str]) -> None:
    for path in (repo / "views").rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in {".pdf", ".png", ".svg"}:
            errors.append(f"{path.relative_to(repo).as_posix()}: derived export should not be tracked")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        read(repo, rel, errors)

    skill = read(repo, "skills/problem-focused-visual-presentation/SKILL.md", errors)
    transfer = read(repo, "skills/problem-focused-visual-presentation/TRANSFER.md", errors)
    template = read(repo, "templates/problem-focused-lens-template.md", errors)
    views_readme = read(repo, "views/README.md", errors)
    registry = read(repo, "views/lens-registry.md", errors)
    gitignore = read(repo, ".gitignore", errors)
    check_all = read(repo, "scripts/check_all.py", errors)

    if skill:
        require_terms("skills/problem-focused-visual-presentation/SKILL.md", skill, SKILL_TERMS, errors)
    if transfer:
        require_terms("skills/problem-focused-visual-presentation/TRANSFER.md", transfer, TRANSFER_TERMS, errors)
    if template:
        require_terms("templates/problem-focused-lens-template.md", template, TEMPLATE_TERMS, errors)
    for rel, text in (("views/README.md", views_readme), ("views/lens-registry.md", registry)):
        if text:
            require_terms(rel, text, VIEW_TERMS, errors)
    if gitignore:
        require_terms(".gitignore", gitignore, GITIGNORE_TERMS, errors)
    if check_all and "problem-focused-visual-presentation" not in check_all:
        errors.append("scripts/check_all.py: missing problem-focused-visual-presentation check")

    check_no_tracked_exports(repo, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} problem-focused visual presentation issue(s)", file=sys.stderr)
        return 1

    print("OK: problem-focused visual presentation wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
