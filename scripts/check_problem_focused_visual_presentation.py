#!/usr/bin/env python3
"""Check problem-focused visual presentation wiring."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = (
    "skills/problem-focused-visual-presentation/SKILL.md",
    "skills/problem-focused-visual-presentation/TRANSFER.md",
    "governance/problem-focused-visual-presentation-rules.md",
    "templates/problem-focused-lens-template.md",
    "views/README.md",
    "views/current/README.md",
    "views/snapshots/README.md",
    "views/lens-registry.md",
    "skills/problem-focused-visual-presentation/reference/page-paradigm-library.md",
    "skills/problem-focused-visual-presentation/reference/component-semantic-manifest.md",
    "skills/problem-focused-visual-presentation/reference/visual-finish-rubric.md",
    "views/current/problem-focused-visual-presentation-system-sample.html",
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
    "focus_object",
    "lens_type",
    "judgement_purpose",
    "persistent_or_temporary",
    "export_required",
    "Source truth -> Content contract -> Visual strategy",
    "art_direction_brief",
    "information_topology",
    "layout_morphology_plan",
    "topic_visual_language",
    "primary_visual_metaphor",
    "anti_information_listing_strategy",
    "page_paradigm",
    "component_semantic_manifest",
    "static_visual_qa",
    "visual_strength_gate",
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
    "静态视觉 QA",
    "Human rubric",
    "禁止复制",
)

TEMPLATE_TERMS = (
    "lens_id",
    "focus_object",
    "lens_type",
    "judgement_purpose",
    "source_pack",
    "source_pages",
    "source_scope",
    "generated_at",
    "source_revision",
    "evidence_boundary",
    "persistent_or_temporary",
    "export_required",
    "visual_structure",
    "art_direction_brief",
    "information_topology",
    "layout_morphology_plan",
    "primary_visual_metaphor",
    "anti_information_listing_strategy",
    "page_paradigm",
    "component_semantic_manifest",
    "human_rubric",
    "result_cluster_diagnosis",
    "export_profile",
    "print_profile",
    "equivalence_profile",
    "default_auto_exports",
    "conversation_png_preview",
    "refresh_trigger",
    "Static Visual QA",
    "layout_frame",
    "visual_acceptance_result",
)

VIEW_TERMS = (
    "source pack",
    "证据边界",
    "current",
    "snapshot",
    "PDF",
    "PNG",
    "gitignore",
    "static_visual_qa",
    "同源",
)

GITIGNORE_TERMS = (
    "views/.exports/",
    "views/exports/",
    "views/**/.exports/",
)

GOVERNANCE_TERMS = (
    "problem-focused-visual-presentation",
    "source pack",
    "evidence_boundary",
    "views/lens-registry",
    "导出",
    "不上推",
    "Source truth -> Content contract -> Visual strategy",
    "视觉策略必填项",
    "Static Visual QA",
    "同源 PDF",
)

REFERENCE_TERMS = {
    "skills/problem-focused-visual-presentation/reference/page-paradigm-library.md": (
        "Page Paradigm Library",
        "matrix",
        "concept map",
        "operations map",
    ),
    "skills/problem-focused-visual-presentation/reference/component-semantic-manifest.md": (
        "Component Semantic Manifest",
        "semantic_role",
        "visual_weight",
        "export_fallback",
    ),
    "skills/problem-focused-visual-presentation/reference/visual-finish-rubric.md": (
        "Visual Finish Rubric",
        "finish_grade",
        "rendered_visual_review",
        "visual_acceptance_result",
    ),
}

LENS_REQUIRED_METADATA = (
    "lens_id",
    "focus_object",
    "lens_type",
    "judgement_purpose",
    "source_pack",
    "evidence_boundary",
    "output_mode",
    "persistent_or_temporary",
    "export_required",
    "visual_strategy",
    "component_semantic_manifest",
    "static_visual_qa",
    "export_profile",
)

STATIC_VISUAL_QA_FIELDS = (
    "layout_frame",
    "type_scale",
    "spacing_rhythm",
    "semantic_palette",
    "component_roles",
    "accessibility_checks",
    "export_render_check",
    "finish_grade",
    "visual_strength_gate",
    "hierarchy_amplitude_gate",
    "component_variety_gate",
    "color_budget_single_hero_gate",
    "adjustment_loop",
    "rendered_visual_review",
    "review_artifact",
    "visual_acceptance_result",
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
    result = subprocess.run(
        ("git", "ls-files", "views"),
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        errors.append("git ls-files views: unable to inspect tracked exports")
        return
    for rel in result.stdout.splitlines():
        if Path(rel).suffix.lower() in {".pdf", ".png", ".svg"}:
            errors.append(f"{rel}: derived export should not be tracked")


def read_lens_manifest(rel: str, text: str, errors: list[str]) -> dict[str, object] | None:
    if "problem-focused-lens-metadata" not in text:
        return None
    match = re.search(
        r'<script[^>]+id=["\']problem-focused-lens-metadata["\'][^>]*>(.*?)</script>',
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if not match:
        errors.append(f"{rel}: problem-focused lens metadata script is missing")
        return None
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        errors.append(f"{rel}: lens metadata JSON is invalid: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{rel}: lens metadata must be a JSON object")
        return None
    return data


def check_lens_metadata(repo: Path, verify_exports: bool, errors: list[str]) -> None:
    for root in (repo / "views" / "current", repo / "views" / "snapshots"):
        if not root.exists():
            continue
        for path in root.rglob("*.html"):
            rel = path.relative_to(repo).as_posix()
            text = path.read_text(encoding="utf-8")
            data = read_lens_manifest(rel, text, errors)
            if data is None:
                continue
            for field in LENS_REQUIRED_METADATA:
                if field not in data:
                    errors.append(f"{rel}: lens metadata missing {field!r}")
            source_pack = data.get("source_pack")
            if not isinstance(source_pack, dict):
                errors.append(f"{rel}: source_pack must be an object")
            else:
                for field in ("read", "unread_related", "updated_at", "evidence", "inferences", "cannot_prove"):
                    if field not in source_pack:
                        errors.append(f"{rel}: source_pack missing {field!r}")
            qa = data.get("static_visual_qa")
            if not isinstance(qa, dict):
                errors.append(f"{rel}: static_visual_qa must be an object")
            else:
                for field in STATIC_VISUAL_QA_FIELDS:
                    if field not in qa:
                        errors.append(f"{rel}: static_visual_qa missing {field!r}")
                if verify_exports:
                    review_artifact = qa.get("review_artifact")
                    if isinstance(review_artifact, str):
                        artifact = repo / review_artifact
                        if not artifact.exists():
                            errors.append(f"{rel}: review_artifact does not exist: {review_artifact}")
                    else:
                        errors.append(f"{rel}: review_artifact must be a path string")
            if "不能替代" not in text and "cannot replace" not in text:
                errors.append(f"{rel}: missing single-source / cannot-replace boundary")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify-exports",
        action="store_true",
        help="Also verify ignored review/export artifacts referenced by lens metadata exist locally.",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        read(repo, rel, errors)

    skill = read(repo, "skills/problem-focused-visual-presentation/SKILL.md", errors)
    transfer = read(repo, "skills/problem-focused-visual-presentation/TRANSFER.md", errors)
    governance = read(repo, "governance/problem-focused-visual-presentation-rules.md", errors)
    template = read(repo, "templates/problem-focused-lens-template.md", errors)
    views_readme = read(repo, "views/README.md", errors)
    registry = read(repo, "views/lens-registry.md", errors)
    gitignore = read(repo, ".gitignore", errors)
    check_all = read(repo, "scripts/check_all.py", errors)

    if skill:
        require_terms("skills/problem-focused-visual-presentation/SKILL.md", skill, SKILL_TERMS, errors)
    if transfer:
        require_terms("skills/problem-focused-visual-presentation/TRANSFER.md", transfer, TRANSFER_TERMS, errors)
    if governance:
        require_terms("governance/problem-focused-visual-presentation-rules.md", governance, GOVERNANCE_TERMS, errors)
    if template:
        require_terms("templates/problem-focused-lens-template.md", template, TEMPLATE_TERMS, errors)
    for rel, terms in REFERENCE_TERMS.items():
        text = read(repo, rel, errors)
        if text:
            require_terms(rel, text, terms, errors)
    for rel, text in (("views/README.md", views_readme), ("views/lens-registry.md", registry)):
        if text:
            require_terms(rel, text, VIEW_TERMS, errors)
    if gitignore:
        require_terms(".gitignore", gitignore, GITIGNORE_TERMS, errors)
    if check_all and "problem-focused-visual-presentation" not in check_all:
        errors.append("scripts/check_all.py: missing problem-focused-visual-presentation check")

    check_no_tracked_exports(repo, errors)
    check_lens_metadata(repo, args.verify_exports, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} problem-focused visual presentation issue(s)", file=sys.stderr)
        return 1

    print("OK: problem-focused visual presentation wiring checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
