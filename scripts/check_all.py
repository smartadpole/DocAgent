#!/usr/bin/env python3
"""Run wiki quality-gate checks."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


CHECKS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("knowledge-linking", "knowledge linking graph", (sys.executable, "scripts/check_knowledge_linking.py")),
    ("harness-governance", "harness governance", (sys.executable, "scripts/check_harness_governance.py")),
    ("work-item-matrix", "work item governance matrix", (sys.executable, "scripts/check_work_item_matrix.py", "--strict")),
    (
        "testing-system-maturity",
        "testing system maturity",
        (sys.executable, "scripts/check_testing_system_maturity.py"),
    ),
    (
        "execution-contract-semantics",
        "execution contract semantics",
        (sys.executable, "scripts/check_execution_contract_semantics.py"),
    ),
    ("git-diff-whitespace", "git diff whitespace", ("git", "diff", "--check")),
    ("git-staged-diff-whitespace", "git staged diff whitespace", ("git", "diff", "--cached", "--check")),
)


def run_check(repo: Path, name: str, command: tuple[str, ...]) -> tuple[bool, str]:
    result = subprocess.run(
        command,
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    output = "\n".join(part.rstrip() for part in (result.stdout, result.stderr) if part.strip())
    header = f"== {name}: {'OK' if result.returncode == 0 else 'FAILED'} =="
    return result.returncode == 0, f"{header}\n{output}".rstrip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List checks without running them.")
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="KEYS",
        help="Run only comma-separated check keys. Use --list to see keys.",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    if args.list:
        for key, name, command in CHECKS:
            print(f"{key}: {name}: {' '.join(command)}")
        return 0

    selected_keys = {
        key.strip()
        for item in args.only
        for key in item.split(",")
        if key.strip()
    }
    known_keys = {key for key, _, _ in CHECKS}
    unknown_keys = sorted(selected_keys - known_keys)
    if unknown_keys:
        print(f"ERROR: unknown check key(s): {', '.join(unknown_keys)}", file=sys.stderr)
        print("Use --list to see available checks.", file=sys.stderr)
        return 2

    failed = False
    outputs: list[str] = []
    for key, name, command in CHECKS:
        if selected_keys and key not in selected_keys:
            continue
        ok, output = run_check(repo, name, command)
        outputs.append(output)
        failed = failed or not ok

    print("\n\n".join(outputs))
    if failed:
        print("\nFAILED: one or more quality-gate checks failed", file=sys.stderr)
        return 1
    if selected_keys:
        print("\nOK: selected wiki quality-gate checks passed")
    else:
        print("\nOK: all wiki quality-gate checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
