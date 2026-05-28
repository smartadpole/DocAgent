#!/usr/bin/env python3
"""Check wiki entrypoint structure and local wikilink hygiene."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_ENTRYPOINTS = (
    "README.md",
    "INDEX.md",
    "AGENTS.md",
    ".codex/AGENTS.md",
    "governance/README.md",
    "projects/README.md",
    "projects/STRUCTURE.md",
    "templates/README.md",
    "skills/README.md",
    "log.md",
)
ENTRYPOINT_TERMS = (
    "response-mode-routing",
    "harness-evolution",
)
GOVERNANCE_PAGES = (
    "governance/response-mode-routing.md",
    "governance/proactive-dialogue-system.md",
    "governance/instruction-adherence.md",
    "governance/execution-contract-semantics.md",
    "governance/harness-evolution.md",
    "governance/harness-feedback-ledger.md",
    "governance/WORKFLOW.md",
    "governance/POLICY.md",
)
WIKILINK_RE = re.compile(r"!?\[\[([^\]|\n]+)(?:\|[^\]\n]+)?\]\]")
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
EXAMPLE_WIKILINK_TARGETS = {
    "wikilink",
    "双向链接",
    "page",
    "page#heading",
    "page#^block-id",
}


def markdown_files(repo: Path) -> list[Path]:
    return [
        path
        for path in repo.rglob("*.md")
        if ".git" not in path.parts and ".obsidian" not in path.parts
    ]


def build_link_index(repo: Path) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = {}
    for path in markdown_files(repo):
        rel = path.relative_to(repo)
        keys = {
            rel.as_posix(),
            rel.with_suffix("").as_posix(),
            rel.name,
            rel.stem,
        }
        for key in keys:
            index.setdefault(key, []).append(rel)
    return index


def link_exists(repo: Path, index: dict[str, list[Path]], target: str) -> bool:
    normalized = target.strip().split("#", 1)[0].strip()
    raw = target.strip()
    if raw in EXAMPLE_WIKILINK_TARGETS:
        return True
    if not normalized:
        return True
    if normalized.startswith(("http://", "https://", "mailto:")):
        return True
    if normalized in index:
        return True
    if f"{normalized}.md" in index:
        return True
    path = repo / normalized
    if path.exists():
        return True
    md_path = repo / f"{normalized}.md"
    return md_path.exists()


def check_entrypoints(repo: Path, errors: list[str]) -> None:
    for rel in REQUIRED_ENTRYPOINTS:
        path = repo / rel
        if not path.exists():
            errors.append(f"{rel}: required wiki entrypoint is missing")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"{rel}: required wiki entrypoint is empty")
        if not any(line.startswith("# ") for line in text.splitlines()):
            errors.append(f"{rel}: missing top-level title")
    for rel in ("README.md", "INDEX.md", "governance/README.md", "templates/README.md", "skills/README.md"):
        text = (repo / rel).read_text(encoding="utf-8")
        for term in ENTRYPOINT_TERMS:
            if term not in text:
                errors.append(f"{rel}: missing entrypoint routing term {term}")


def check_governance_frontmatter(repo: Path, errors: list[str]) -> None:
    for rel in GOVERNANCE_PAGES:
        path = repo / rel
        if not path.exists():
            errors.append(f"{rel}: required governance page is missing")
            continue
        text = path.read_text(encoding="utf-8")
        if rel == "governance/WORKFLOW.md":
            continue
        if not FRONTMATTER_RE.match(text):
            errors.append(f"{rel}: missing frontmatter")
            continue
        if "source_of_truth" not in text:
            errors.append(f"{rel}: missing governance metadata term source_of_truth")
        if "status: active" not in text and "status: confirmed" not in text:
            errors.append(f"{rel}: missing governance metadata status term")


def check_wikilinks(repo: Path, errors: list[str]) -> None:
    index = build_link_index(repo)
    for path in markdown_files(repo):
        rel = path.relative_to(repo)
        text = path.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            if not link_exists(repo, index, target):
                errors.append(f"{rel}: unresolved wikilink [[{target}]]")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    check_entrypoints(repo, errors)
    check_governance_frontmatter(repo, errors)
    check_wikilinks(repo, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} project documentation issue(s)", file=sys.stderr)
        return 1

    print("OK: wiki entrypoints, governance metadata, and wikilinks checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
