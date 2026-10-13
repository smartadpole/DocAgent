#!/usr/bin/env python3
"""Discover conditional agent guidance without loading it into every task.

The aggregate reader is for offline source-wiring sensors only. It is not a
runtime prompt loader. Root guards are checked separately by inspect_entry.
"""
from __future__ import annotations

import argparse
from pathlib import Path

AREAS = {
    area: f"governance/agent-guidance-{area}.md"
    for area in ("knowledge", "execution", "governance", "presentation")
}


def resolve_area(repo: Path, area: str) -> Path:
    if area not in AREAS:
        raise ValueError(f"Unknown guidance area: {area}")
    return repo / AREAS[area]


def inspect_entry(repo: Path, text: str | None = None) -> list[str]:
    text = (repo / "AGENTS.md").read_text(encoding="utf-8") if text is None else text
    errors = []
    # A generous reviewed byte budget protects the always-loaded surface only.
    if len(text.encode("utf-8")) > 12000:
        errors.append("AGENTS.md: root entry exceeds 12000 bytes; route professional detail")
    for guard in ("默认本地提交", "未提交工作", "只读子工程", "原始问题", "不能替代", "部署环境"):
        if guard not in text:
            errors.append(f"AGENTS.md: missing always-on guard {guard}")
    for area, rel in AREAS.items():
        if f"[[{rel[:-3]}" not in text:
            errors.append(f"AGENTS.md: missing conditional route {area}")
        if not (repo / rel).is_file():
            errors.append(f"{rel}: missing conditional owner")
    return errors


def inspect_adapters(repo: Path) -> list[str]:
    expected = {'.codex/AGENTS.md': '# Codex Local Adapter\n\n@../AGENTS.md\n', 'CLAUDE.md': '@AGENTS.md\n'}
    return [f'{rel}: adapter must only import root rules' for rel, value in expected.items()
            if not (repo / rel).is_file() or (repo / rel).read_text(encoding='utf-8') != value]


def read_agent_sources(repo: Path, errors: list[str]) -> str:
    """Offline semantic wiring view; never recursively follows owner links."""
    root = (repo / "AGENTS.md").read_text(encoding="utf-8")
    errors.extend(inspect_entry(repo, root))
    errors.extend(inspect_adapters(repo))
    docs = [root]
    for rel in AREAS.values():
        if f"[[{rel[:-3]}" in root and (repo / rel).is_file():
            docs.append((repo / rel).read_text(encoding="utf-8"))
    return "\n".join(docs)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--area", choices=AREAS)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    if args.check:
        errors = inspect_entry(repo)
        print("\n".join(errors) if errors else "Agent entry and conditional routes: OK")
        return bool(errors)
    for area in ([args.area] if args.area else AREAS):
        path = resolve_area(repo, area)
        print(f"{area}: {path.relative_to(repo)}")
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                print(f"  {line[3:]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
