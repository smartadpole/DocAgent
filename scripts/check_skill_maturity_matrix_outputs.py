#!/usr/bin/env python3
"""Validate synchronized skill maturity matrix outputs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "views" / "current" / "governance" / "skill-maturity-matrix.html"
MD = ROOT / "views" / "current" / "governance" / "skill-maturity-diagnostics.md"
DETAIL_HTML = ROOT / "views" / "current" / "governance" / "skill-maturity-diagnostics.html"
JSON_DATA = ROOT / "views" / "current" / "governance" / "skill-maturity-matrix.data.json"


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def meta_content(html_text: str, name: str) -> str:
    match = re.search(rf'<meta name="{re.escape(name)}" content="([^"]*)">', html_text)
    return match.group(1) if match else ""


def frontmatter_value(md_text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", md_text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def main() -> int:
    missing = [path for path in (HTML, MD, DETAIL_HTML, JSON_DATA) if not path.is_file()]
    if missing:
        return fail("missing synchronized skill maturity output(s): " + ", ".join(str(path) for path in missing))

    html_text = HTML.read_text(encoding="utf-8")
    md_text = MD.read_text(encoding="utf-8")
    detail_html_text = DETAIL_HTML.read_text(encoding="utf-8")
    data = json.loads(JSON_DATA.read_text(encoding="utf-8"))

    for expected in ("skill-maturity-diagnostics.md", "skill-maturity-diagnostics.html", "skill-maturity-matrix.data.json"):
        if expected not in html_text:
            return fail(f"HTML output does not link {expected}")

    if "[[views/current/governance/skill-maturity-matrix.html]]" not in md_text:
        return fail("Markdown diagnostics do not link the HTML matrix")
    if "views/current/governance/skill-maturity-matrix.data.json" not in md_text:
        return fail("Markdown diagnostics do not link the JSON data")
    if "views/current/governance/skill-maturity-diagnostics.html" not in md_text:
        return fail("Markdown diagnostics do not link the rendered HTML diagnostics")

    html_generated = meta_content(html_text, "generated_at")
    html_revision = meta_content(html_text, "source_revision")
    detail_generated = meta_content(detail_html_text, "generated_at")
    detail_revision = meta_content(detail_html_text, "source_revision")
    md_generated = frontmatter_value(md_text, "generated_at")
    md_revision = frontmatter_value(md_text, "source_revision")
    if not html_generated or not html_revision or not detail_generated or not detail_revision:
        return fail("HTML output is missing generated_at or source_revision metadata")
    if html_generated != data.get("generated_at") or html_generated != md_generated or html_generated != detail_generated:
        return fail("generated timestamp drift between HTML, rendered diagnostics, Markdown, and JSON outputs")
    if html_revision != data.get("source_revision") or html_revision != md_revision or html_revision != detail_revision:
        return fail("source revision drift between HTML, rendered diagnostics, Markdown, and JSON outputs")

    outputs = data.get("outputs", {})
    expected_outputs = {
        "html": "views/current/governance/skill-maturity-matrix.html",
        "diagnostics_md": "views/current/governance/skill-maturity-diagnostics.md",
        "diagnostics_html": "views/current/governance/skill-maturity-diagnostics.html",
        "data_json": "views/current/governance/skill-maturity-matrix.data.json",
    }
    if outputs != expected_outputs:
        return fail(f"JSON outputs block drifted: {outputs!r}")

    projects = data.get("projects", [])
    skills = data.get("skills", [])
    diagnostics = data.get("diagnostics", [])
    if not projects or not skills:
        return fail("JSON data has no projects or skills")
    expected_diagnostics = len(projects) * len(skills)
    if len(diagnostics) != expected_diagnostics:
        return fail(f"diagnostic coverage mismatch: {len(diagnostics)} != {expected_diagnostics}")
    required_fields = {
        "skill",
        "project",
        "status",
        "score",
        "max_score",
        "score_gap",
        "leaders",
        "signals",
        "fingerprint",
        "missing_leader_signals",
        "required_leader_fingerprint",
        "recommended_direction",
    }
    for index, item in enumerate(diagnostics):
        missing_fields = sorted(required_fields - set(item))
        if missing_fields:
            return fail(f"diagnostic item {index} missing fields: {', '.join(missing_fields)}")
        anchor = item.get("anchor")
        if not anchor:
            return fail(f"diagnostic item {index} missing anchor")
        if f'href="./skill-maturity-diagnostics.html#{anchor}"' not in html_text:
            return fail(f"matrix output does not link diagnostic anchor: {anchor}")
        if f'id="{anchor}"' not in detail_html_text:
            return fail(f"rendered diagnostics missing anchor: {anchor}")

    print("OK: skill maturity HTML, Markdown diagnostics, and JSON data are synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
