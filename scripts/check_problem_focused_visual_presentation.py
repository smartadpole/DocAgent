#!/usr/bin/env python3
"""Validate problem-focused visual presentation source wiring."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "skills/problem-focused-visual-presentation/SKILL.md",
    "skills/problem-focused-visual-presentation/TRANSFER.md",
    "templates/problem-focused-lens-template.md",
    "views/README.md",
    "views/lens-registry.md",
    "views/current/README.md",
    "views/snapshots/README.md",
    ".gitignore",
)

REQUIRED_TERMS = {
    "skills/problem-focused-visual-presentation/SKILL.md": (
        "focus_object",
        "lens_type",
        "judgement_purpose",
        "source pack",
        "Source pack 守卫",
        "confirmed / likely / possible / blocked",
        "输出形态",
        "短答",
        "Markdown 真相源",
        "visual_structure",
        "用户价值优先",
        "矩阵和热力编码",
        "整格填色",
        "强对比",
        "照片和视觉证据排版",
        "photo_layout_strategy",
        "画幅家族",
        "自然比例证据网格",
        "object-fit: contain",
        "output_mode",
        "export_profile",
        "print_profile",
        "equivalence_profile",
        "default_auto_exports",
        "conversation_png_preview",
        "生成或更新持久 HTML lens",
        "最终回复必须用 Markdown 图片语法展示 PNG 预览",
        "禁止为对话展示单独手工重画 PNG",
        "same source manifest / render pipeline",
        "Browser 截图接口失败",
        "同源 HTML 导出 pipeline fallback",
        "canonical HTML / source / manifest",
        "canonical_policy",
        "snapshot_policy",
        "staleness_policy",
        "refresh_trigger",
    ),
    "skills/problem-focused-visual-presentation/TRANSFER.md": (
        "上游归一状态",
        "LifeOS",
        "已抽象反哺到上游源能力",
        "HTML lens 的 PDF / PNG ignored export 与对话 PNG 预览完成合同",
        "views/` 落位硬合同",
        "判断目的",
        "输出形态选择",
        "lens 类型字段",
        "用户价值优先",
        "矩阵 / 热力图视觉编码",
        "整格填色",
        "文字 / 背景对比",
        "照片 / 视觉证据排版",
        "HTML lens 硬完成合同",
        "同源一致性",
        "source manifest / render pipeline",
        "default_auto_exports",
        "conversation_png_preview",
        "LifeOS 对照覆盖矩阵",
        "工程化保护",
        "不复制 LifeOS",
        "views/current/",
        "views/snapshots/",
        "views/lens-registry.md",
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
        "default_auto_exports",
        "conversation_png_preview",
        "canonical_policy",
        "snapshot_policy",
        "staleness_policy",
        "refresh_trigger",
        "confirmed / likely / possible / blocked",
        "object-fit: contain",
        "矩阵 / 热力图",
        "单元格是否整格填色",
        "same source manifest / render pipeline",
    ),
    "views/README.md": (
        "current/",
        "snapshots/",
        "lens-registry.md",
        "exports/",
        "**/.exports/",
        "canonical HTML / source / manifest",
        "default_auto_exports",
        "conversation_png_preview",
    ),
    "views/lens-registry.md": (
        "Registry Fields",
        "lens_id",
        "focus_object",
        "lens_type",
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
        "default_auto_exports",
        "conversation_png_preview",
        "canonical_policy",
        "snapshot_policy",
        "staleness_policy",
        "refresh_trigger",
        "Current Lenses",
        "Snapshot Lenses",
    ),
    "views/snapshots/README.md": (
        "snapshot_of",
        "source revision",
        "证据边界",
        "views/current/",
    ),
    ".gitignore": (
        "views/exports/",
        "views/.exports/",
        "views/**/.exports/",
        "views/**/*.pdf",
        "views/**/*.png",
        "views/**/*.svg",
        "assets/views/",
    ),
}

LENS_REQUIRED_FIELDS = (
    "lens_id",
    "focus_object",
    "lens_type",
    "source_pages",
    "source_scope",
    "generated_at",
    "source_revision",
    "evidence_boundary",
    "context_frame",
    "output_mode",
    "export_profile",
    "print_profile",
    "equivalence_profile",
    "canonical_policy",
    "snapshot_policy",
    "staleness_policy",
    "refresh_trigger",
)

ENTRY_FILES = {
    "views/README.md",
    "views/lens-registry.md",
    "views/current/README.md",
    "views/snapshots/README.md",
}

HTML_EXPORT_REQUIRED_TERMS = (
    "@page",
    "@media print",
    "output_mode",
    "export_profile",
    "print_profile",
    "equivalence_profile",
    "default_auto_exports",
    "conversation_png_preview",
    "same source pack",
    "canonical HTML / source / manifest",
)

TRACKED_EXPORT_SUFFIXES = (".pdf", ".png", ".svg")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def tracked_files() -> list[str]:
    result = subprocess.run(
        ("git", "ls-files"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def check_required_files(errors: list[str]) -> None:
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"missing problem-focused visual presentation file: {rel_path}")


def check_required_terms(errors: list[str]) -> None:
    for rel_path, terms in REQUIRED_TERMS.items():
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel_path} missing required term: {term}")


def check_persistent_markdown_lenses(errors: list[str]) -> None:
    views_root = ROOT / "views"
    if not views_root.exists():
        return

    for path in sorted(views_root.rglob("*.md")):
        rel_path = rel(path)
        if rel_path in ENTRY_FILES:
            continue
        text = path.read_text(encoding="utf-8")
        for field in LENS_REQUIRED_FIELDS:
            if field not in text:
                errors.append(f"{rel_path} missing lens provenance field: {field}")
        if "/current/" in f"/{rel_path}/" and "snapshot_of" in text:
            errors.append(f"{rel_path} current lens should not declare snapshot_of")
        if "/snapshots/" in f"/{rel_path}/" and "snapshot_of" not in text:
            errors.append(f"{rel_path} snapshot lens must declare snapshot_of")


def check_html_export_profiles(errors: list[str]) -> None:
    views_root = ROOT / "views"
    if not views_root.exists():
        return

    for path in sorted(views_root.rglob("*.html")):
        if ".exports" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for term in HTML_EXPORT_REQUIRED_TERMS:
            if term not in text:
                errors.append(f"{rel(path)} missing HTML export term: {term}")


def check_html_photo_layout_strategy(errors: list[str]) -> None:
    views_root = ROOT / "views"
    if not views_root.exists():
        return

    for path in sorted(views_root.rglob("*.html")):
        if ".exports" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if "photo-grid" not in text:
            continue
        if "photo_layout_strategy" not in text:
            errors.append(f"{rel(path)} has a photo grid but no photo_layout_strategy")
        if "object-fit: contain" not in text:
            errors.append(f"{rel(path)} has a photo grid but no object-fit: contain")
        if "object-fit: cover" in text:
            errors.append(f"{rel(path)} uses object-fit: cover; evidence photos must not be cropped")
        if "grid-auto-rows" in text:
            errors.append(
                f"{rel(path)} uses grid-auto-rows; use aspect-family layout for evidence photos"
            )


def check_no_tracked_duplicate_exports(errors: list[str]) -> None:
    for rel_path in tracked_files():
        if not rel_path.lower().endswith(TRACKED_EXPORT_SUFFIXES):
            continue
        if rel_path.startswith("views/") or rel_path.startswith("assets/views/"):
            errors.append(
                f"tracked generated lens export is not allowed: {rel_path}; "
                "put PDF/PNG/SVG exports under a gitignored exports directory"
            )


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_required_terms(errors)
    check_persistent_markdown_lenses(errors)
    check_html_export_profiles(errors)
    check_html_photo_layout_strategy(errors)
    check_no_tracked_duplicate_exports(errors)

    if errors:
        print("Problem-focused visual presentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Problem-focused visual presentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
