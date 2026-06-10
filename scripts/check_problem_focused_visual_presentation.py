#!/usr/bin/env python3
"""Validate problem-focused visual presentation source wiring."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "skills/problem-focused-visual-presentation/SKILL.md",
    "skills/problem-focused-visual-presentation/TRANSFER.md",
    "templates/problem-focused-lens-template.md",
    "views/README.md",
    "views/lens-registry.md",
)

REQUIRED_TERMS = {
    "skills/problem-focused-visual-presentation/SKILL.md": (
        "focus_object",
        "lens_type",
        "confirmed / likely / possible / blocked",
        "Source pack 守卫",
        "用户价值优先",
        "照片和视觉证据排版",
        "photo_layout_strategy",
        "object-fit: contain",
        "visual_structure",
        "export_profile",
        "print_profile",
        "equivalence_profile",
        "canonical_policy",
        "snapshot_policy",
        "staleness_policy",
        "refresh_trigger",
    ),
    "skills/problem-focused-visual-presentation/TRANSFER.md": (
        "上游归一状态",
        "LifeOS",
        "已抽象反哺到上游源能力",
        "lens 类型字段",
        "用户价值优先",
        "照片 / 视觉证据排版",
        "持久化字段",
        "工程化保护",
        "不复制 LifeOS",
    ),
    "templates/problem-focused-lens-template.md": (
        "lens_id",
        "focus_object",
        "lens_type",
        "judgement_purpose",
        "source_pages",
        "source_scope",
        "generated_at",
        "source_revision",
        "evidence_boundary",
        "context_frame",
        "output_mode",
        "visual_structure",
        "photo_layout_strategy",
        "export_profile",
        "print_profile",
        "equivalence_profile",
        "canonical_policy",
        "snapshot_policy",
        "staleness_policy",
        "refresh_trigger",
        "confirmed / likely / possible / blocked",
        "object-fit: contain",
    ),
    "views/lens-registry.md": (
        "Registry Fields",
        "focus_object",
        "lens_type",
        "source_pages",
        "source_scope",
        "generated_at",
        "evidence_boundary",
        "context_frame",
        "visual_structure",
        "photo_layout_strategy",
        "export_profile",
        "print_profile",
        "equivalence_profile",
        "canonical_policy",
        "snapshot_policy",
        "staleness_policy",
        "refresh_trigger",
        "Current Lenses",
        "Snapshot Lenses",
    ),
}


def main() -> int:
    errors: list[str] = []
    for rel_path in REQUIRED_FILES:
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"missing problem-focused visual presentation file: {rel_path}")

    for rel_path, terms in REQUIRED_TERMS.items():
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel_path} missing required term: {term}")

    if errors:
        print("Problem-focused visual presentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Problem-focused visual presentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
