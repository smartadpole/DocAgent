#!/usr/bin/env python3
"""Check that tracked authored content is safe for a public-visible repository."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCAL_DENYLIST = ROOT / ".codex" / "local" / "public-repository-deny-terms.txt"
SKIP_PREFIXES = ("raw/", ".obsidian/plugins/")
REQUIRED_TERMS = {
    "AGENTS.md": (
        "本仓是公开可见仓库",
        "public-repository-content",
        "历史记录",
    ),
    ".codex/AGENTS.md": (
        "本仓公开可见",
        "public-repository-content",
    ),
    "governance/wiki-governance-system-contract.v1.md": (
        "## 公开仓库持久化边界",
        "public-safe persistence",
        "Persistence Decision",
    ),
    "governance/log-writing-rules.md": (
        "## 公开安全边界",
        "public-repository-content",
    ),
    "templates/log-entry-template.md": (
        "**公开边界**",
        "public-safe",
    ),
    "governance/instruction-adherence.md": (
        "公开仓库接收公司 / 私有工程上下文",
        "check_public_repository_content.py",
    ),
    "scripts/check_all.py": (
        "public-repository-content",
        "scripts/check_public_repository_content.py",
    ),
}

FORBIDDEN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "machine-specific absolute home path",
        re.compile(r"/(?:Users|home)/(?!<user>|<name>|USER|username)[A-Za-z0-9._-]+/"),
    ),
    (
        "internal company Git or email domain",
        re.compile(r"(?:git-app\.haidilao\.com|@[A-Za-z0-9.-]*haidilao\.)", re.IGNORECASE),
    ),
    (
        "credential embedded in URL",
        re.compile(r"https?://[^/\s:@]+:[^/\s@]+@", re.IGNORECASE),
    ),
    (
        "other-project public host",
        re.compile(r"hai-macbook-pro\.smartadpole\.com", re.IGNORECASE),
    ),
)


def tracked_files() -> list[str]:
    result = subprocess.run(
        ("git", "ls-files", "-z"),
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def read_authored_text(rel: str) -> str | None:
    if rel.startswith(SKIP_PREFIXES):
        return None
    path = ROOT / rel
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def local_deny_terms() -> list[str]:
    if not LOCAL_DENYLIST.exists():
        return []
    return [
        line.strip()
        for line in LOCAL_DENYLIST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def main() -> int:
    errors: list[str] = []

    for rel, terms in REQUIRED_TERMS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"{rel}: required public-repository guard file is missing")
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel}: missing public-repository guard term {term}")

    deny_terms = local_deny_terms()
    for rel in tracked_files():
        text = read_authored_text(rel)
        if text is None:
            continue
        for label, pattern in FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                errors.append(f"{rel}:{line_number(text, match.start())}: {label}")
        for index, term in enumerate(deny_terms, 1):
            offset = text.casefold().find(term.casefold())
            if offset >= 0:
                errors.append(
                    f"{rel}:{line_number(text, offset)}: local private-source deny term #{index}"
                )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} public-repository content issue(s)", file=sys.stderr)
        return 1

    suffix = (
        f"; local denylist terms checked: {len(deny_terms)}"
        if deny_terms
        else "; local denylist absent, semantic source-identity review remains manual"
    )
    print(f"OK: tracked authored content passed public-repository structural checks{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
