#!/usr/bin/env python3
"""Check Harness feedback ledger structure and status vocabulary."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


LEDGER = "governance/harness-feedback-ledger.md"

SECTION_HEADERS = {
    "Episode Ledger": (
        "日期",
        "Episode",
        "触发信号",
        "响应模式",
        "成本类型",
        "已采取改动",
        "Sensor / Artifact",
        "状态",
    ),
    "Sensor Backlog": ("候选项", "触发来源", "拟补 sensor / 模板", "当前状态"),
    "Rule Promotion Queue": ("候选规则", "来自 episode", "晋升目标", "状态"),
    "Rule Prune Queue": ("候选清理", "原因", "当前状态"),
}

RESPONSE_MODES = {
    "快速诊断",
    "引导式设计",
    "知识沉淀",
    "Issue 分析 + 沉淀",
    "验收关闭",
    "规则升级",
    "子工程实现 / 回传",
    "批处理",
}
COST_TYPES = {"必要成本", "可优化成本", "应避免成本"}
STATUSES = {"observed", "active", "promoted", "promoted-removed", "blocked"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass(frozen=True)
class Table:
    section: str
    rows: tuple[tuple[str, ...], ...]


def split_table_row(line: str) -> tuple[str, ...]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]

    cells: list[str] = []
    buf: list[str] = []
    escaped = False
    for char in stripped:
        if char == "|" and not escaped:
            cells.append("".join(buf).strip())
            buf = []
            continue
        buf.append(char)
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
    cells.append("".join(buf).strip())
    return tuple(cells)


def section_lines(text: str, section: str) -> list[str]:
    heading = f"## {section}"
    lines = text.splitlines()
    start = next((idx + 1 for idx, line in enumerate(lines) if line.strip() == heading), None)
    if start is None:
        return []
    end = next((idx for idx in range(start, len(lines)) if lines[idx].startswith("## ")), len(lines))
    return lines[start:end]


def parse_table(text: str, section: str, errors: list[str]) -> Table | None:
    lines = [line for line in section_lines(text, section) if line.strip()]
    if not lines:
        errors.append(f"{LEDGER}: missing section ## {section}")
        return None

    table_start = next((idx for idx, line in enumerate(lines) if line.lstrip().startswith("|")), None)
    if table_start is None:
        errors.append(f"{LEDGER}: ## {section} has no markdown table")
        return None

    table_lines = [line for line in lines[table_start:] if line.lstrip().startswith("|")]
    if len(table_lines) < 2:
        errors.append(f"{LEDGER}: ## {section} table is incomplete")
        return None

    expected = SECTION_HEADERS[section]
    header = split_table_row(table_lines[0])
    if header != expected:
        errors.append(f"{LEDGER}: ## {section} header mismatch; expected {expected}, got {header}")

    rows: list[tuple[str, ...]] = []
    for line in table_lines[2:]:
        cells = split_table_row(line)
        if len(cells) != len(expected):
            errors.append(f"{LEDGER}: ## {section} row has {len(cells)} cells; expected {len(expected)}: {line}")
            continue
        rows.append(cells)
    if not rows:
        errors.append(f"{LEDGER}: ## {section} table has no data rows")
    return Table(section=section, rows=tuple(rows))


def require_nonempty(table: Table, errors: list[str]) -> None:
    for row_index, row in enumerate(table.rows, start=1):
        for column, value in zip(SECTION_HEADERS[table.section], row):
            if not value:
                errors.append(f"{LEDGER}: ## {table.section} row {row_index} column {column} is empty")


def check_episode_table(table: Table, errors: list[str]) -> None:
    for row_index, row in enumerate(table.rows, start=1):
        date, episode, _trigger, mode, cost, _action, artifact, status = row
        if not DATE_RE.match(date):
            errors.append(f"{LEDGER}: Episode Ledger row {row_index} has invalid date {date}")
        if mode not in RESPONSE_MODES:
            errors.append(f"{LEDGER}: Episode Ledger row {row_index} has unknown response mode {mode}")
        if cost not in COST_TYPES:
            errors.append(f"{LEDGER}: Episode Ledger row {row_index} has unknown cost type {cost}")
        if status not in STATUSES:
            errors.append(f"{LEDGER}: Episode Ledger row {row_index} has unknown status {status}")
        if status in {"active", "promoted"} and not any(token in artifact for token in ("`", "[[")):
            errors.append(f"{LEDGER}: Episode Ledger row {row_index} lacks linked artifact: {episode}")


def check_status_column(table: Table, errors: list[str]) -> None:
    status_index = len(SECTION_HEADERS[table.section]) - 1
    for row_index, row in enumerate(table.rows, start=1):
        status = row[status_index]
        if status not in STATUSES:
            errors.append(f"{LEDGER}: ## {table.section} row {row_index} has unknown status {status}")


def check_cross_section_expectations(tables: dict[str, Table], errors: list[str]) -> None:
    episode_names = {row[1] for row in tables["Episode Ledger"].rows}
    backlog_names = {row[0] for row in tables["Sensor Backlog"].rows}
    promotion_sources = {row[1] for row in tables["Rule Promotion Queue"].rows}

    if not any(row[-1] == "active" for row in tables["Episode Ledger"].rows):
        errors.append(f"{LEDGER}: Episode Ledger should keep at least one active episode")
    for required in (
        "H5 ledger 独立 sensor",
        "指令遵循独立 sensor",
        "Markdown / wikilink / frontmatter 检查",
    ):
        if required not in backlog_names:
            errors.append(f"{LEDGER}: Sensor Backlog must track {required}")
    for script_name in (
        "check_harness_feedback_ledger.py",
        "check_instruction_adherence.py",
        "check_project_docs.py",
    ):
        if not any(script_name in row[2] for row in tables["Sensor Backlog"].rows):
            errors.append(f"{LEDGER}: Sensor Backlog must reference {script_name}")

    for source in promotion_sources:
        if source not in episode_names:
            errors.append(f"{LEDGER}: Rule Promotion Queue source {source} is not present in Episode Ledger")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    path = repo / LEDGER
    if not path.exists():
        print(f"ERROR: {LEDGER}: required ledger file is missing", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    tables: dict[str, Table] = {}

    for section in SECTION_HEADERS:
        table = parse_table(text, section, errors)
        if table is None:
            continue
        require_nonempty(table, errors)
        if section == "Episode Ledger":
            check_episode_table(table, errors)
        else:
            check_status_column(table, errors)
        tables[section] = table

    if len(tables) == len(SECTION_HEADERS):
        check_cross_section_expectations(tables, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} harness feedback ledger issue(s)", file=sys.stderr)
        return 1

    episode_count = len(tables["Episode Ledger"].rows)
    backlog_count = len(tables["Sensor Backlog"].rows)
    print(f"OK: harness feedback ledger checked ({episode_count} episode row(s), {backlog_count} sensor backlog row(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
