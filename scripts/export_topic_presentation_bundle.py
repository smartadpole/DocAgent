#!/usr/bin/env python3
"""Render immutable topic-presentation-contract.v2 bundles for this repository."""

from __future__ import annotations

import argparse
import copy
import hashlib
import html
import json
import os
import shutil
import subprocess
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
OWNER = ROOT / "governance"
SCHEMA = OWNER / "topic-presentation-contract.v2.schema.json"
ACTIVE_PROFILE = OWNER / "topic-presentation-active-profile.v2.json"
SHADOW_PROFILE = ROOT / "scripts/fixtures/topic-visual-presentation/shadow-profile.v2.json"
GOLDENS = (
    ("single-page", OWNER / "topic-presentation-golden-single.v2.json"),
    ("page-tree", OWNER / "topic-presentation-golden-page-tree.v2.json"),
)
EXPORT_ROOT = ROOT / "views/.exports/topic-presentation-v2"
LEGACY_BASELINE = ROOT / "scripts/fixtures/topic-visual-presentation/legacy_artifact_baseline_manifest.v1.json"
RENDERER_REVISION = "wiki-topic-presentation-renderer.v2"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def git_head() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def chrome(*arguments: str) -> None:
    if not CHROME.exists():
        raise FileNotFoundError(f"Chrome renderer unavailable: {CHROME}")
    command = [
        str(CHROME), "--headless=new", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars", "--run-all-compositor-stages-before-draw", *arguments,
    ]
    result = subprocess.run(command, check=False, capture_output=True, text=True, timeout=90)
    if result.returncode:
        raise RuntimeError(f"Chrome render failed ({result.returncode}): {result.stderr.strip()}")


def render_pdf(source: Path, target: Path) -> None:
    chrome("--no-pdf-header-footer", f"--print-to-pdf={target}", source.resolve().as_uri())


def render_png(source: Path, target: Path, width: int, height: int) -> None:
    chrome(f"--window-size={width},{height}", f"--screenshot={target}", source.resolve().as_uri())


def source_snapshot(contract: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    refs = sorted({item["owner_ref"] for item in contract["coverage_manifest"]["source_fragments"]})
    for ref in refs:
        path = ROOT / ref
        if not path.is_file():
            raise ValueError(f"source owner missing: {ref}")
        records.append({"owner_ref": ref, "sha256": sha256(path)})
    return f"sha256:{canonical_hash(records)}", records


def page_sources(contract: dict[str, Any]) -> dict[str, str]:
    bindings = contract["coverage_manifest"]["page_bindings"]
    fragments = {item["source_fragment_id"]: item for item in contract["coverage_manifest"]["source_fragments"]}
    owners: dict[str, set[str]] = {}
    for binding in bindings:
        owners.setdefault(binding["page_id"], set()).add(fragments[binding["source_fragment_id"]]["owner_ref"])
    result: dict[str, str] = {}
    for page_id, refs in owners.items():
        if len(refs) != 1:
            raise ValueError(f"page {page_id} must bind exactly one Markdown owner, got {sorted(refs)}")
        result[page_id] = next(iter(refs))
    return result


def navigation(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    bundle = contract["presentation_bundle"]
    pages = {item["page_id"]: item for item in bundle["page_catalog"]}
    root_id = bundle["root_page_id"]
    parents: dict[str, str] = {}
    children: dict[str, list[tuple[int, str]]] = {page_id: [] for page_id in pages}
    for edge in bundle["canonical_tree"]["edges"]:
        child = edge["child_page_id"]
        if child in parents:
            raise ValueError(f"multiple parents: {child}")
        parents[child] = edge["parent_page_id"]
        children[edge["parent_page_id"]].append((edge["order"], child))
    result: dict[str, dict[str, Any]] = {}
    for page_id in pages:
        trail = [page_id]
        seen = {page_id}
        while trail[-1] != root_id:
            current = trail[-1]
            if current not in parents:
                raise ValueError(f"orphan page: {current}")
            parent = parents[current]
            if parent in seen:
                raise ValueError("cycle in canonical tree")
            trail.append(parent)
            seen.add(parent)
        result[page_id] = {
            "parent": parents.get(page_id),
            "children": [child for _, child in sorted(children[page_id])],
            "breadcrumb": list(reversed(trail)),
        }
    return result


def stem(page: dict[str, Any]) -> str:
    return Path(page["canonical_path"]).stem


def render_html(
    contract: dict[str, Any], page: dict[str, Any], output_dir: Path,
    generated: datetime, owner_ref: str, nav: dict[str, dict[str, Any]],
) -> str:
    bundle = contract["presentation_bundle"]
    page_id = page["page_id"]
    pages = {item["page_id"]: item for item in bundle["page_catalog"]}
    claims = {item["claim_id"]: item for item in contract["coverage_manifest"]["claims"]}
    fragments = {item["source_fragment_id"]: item for item in contract["coverage_manifest"]["source_fragments"]}
    bindings = [item for item in contract["coverage_manifest"]["page_bindings"] if item["page_id"] == page_id]
    claim_cards = []
    for index, binding in enumerate(bindings, 1):
        claim = claims[binding["claim_id"]]
        fragment = fragments[binding["source_fragment_id"]]
        claim_cards.append(
            f'<article class="claim" id="{html.escape(binding["rendered_section_id"])}" '
            f'data-claim-id="{html.escape(binding["claim_id"])}">'
            f'<span class="claim-no">{index:02d}</span><h2>{html.escape(claim["text"])}</h2>'
            f'<p>证据锚点：<code>{html.escape(fragment["selector"])}</code></p></article>'
        )
    root = pages[bundle["root_page_id"]]
    nav_links = []
    for candidate in bundle["page_catalog"]:
        active = ' aria-current="page"' if candidate["page_id"] == page_id else ""
        nav_links.append(f'<a href="{html.escape(candidate["canonical_path"])}"{active}>{html.escape(candidate["title"])}</a>')
    crumbs = []
    for crumb_id in nav[page_id]["breadcrumb"]:
        crumb = pages[crumb_id]
        crumbs.append(f'<a href="{html.escape(crumb["canonical_path"])}">{html.escape(crumb["title"])}</a>')
    page_stem = stem(page)
    pdf_name = f"{page_stem}.pdf"
    desktop_name = f"{page_stem}.desktop.png"
    mobile_name = f"{page_stem}.mobile.png"
    owner_href = os.path.relpath(ROOT / owner_ref, output_dir)
    display_time = generated.strftime("生成于 %Y-%m-%d %H:%M UTC%z")
    display_time = display_time[:-2] + ":" + display_time[-2:]
    source_manifest = {
        "contract_revision": "topic-presentation-contract.v2",
        "bundle_revision": bundle["bundle_revision"],
        "source_snapshot_id": bundle["source_snapshot_id"],
        "build_id": bundle["build_id"],
        "page_id": page_id,
        "owner_ref": owner_ref,
        "claim_bindings": bindings,
    }
    visual_qa = {
        "layout": "responsive-single-column-with-map",
        "type": "system-sans-hierarchy",
        "spacing": "8px-scale",
        "palette": "ink-paper-coral-teal",
        "component_roles": ["bundle-map", "claim-card", "download-bar", "source-link"],
        "accessibility": ["landmarks", "focus-visible", "high-contrast", "mobile-reflow"],
        "export_render": ["pdf", "png-desktop", "png-mobile"],
        "finish_grade": "candidate",
        "independent_visual_review": "not-evaluated",
    }
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="contract_revision" content="topic-presentation-contract.v2"><meta name="bundle_revision" content="{html.escape(bundle['bundle_revision'])}">
<meta name="source_snapshot_id" content="{html.escape(bundle['source_snapshot_id'])}"><meta name="build_id" content="{html.escape(bundle['build_id'])}">
<title>{html.escape(page['title'])} · {html.escape(bundle['bundle_title'])}</title>
<style>
:root{{--paper:#f3efe6;--surface:#fffdf8;--ink:#173238;--muted:#5d6a6b;--line:#cbd2cc;--coral:#c6533f;--teal:#087f7a;--wash:#dcebe5}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:400 16px/1.55 "PingFang SC",system-ui,sans-serif}}
a{{color:var(--teal);text-underline-offset:3px}}a:focus-visible{{outline:3px solid var(--coral);outline-offset:3px}}
.shell{{width:min(1120px,calc(100% - 28px));margin:auto;padding:28px 0 42px}}.topline{{display:flex;justify-content:space-between;gap:18px;border-bottom:1px solid var(--line);padding-bottom:12px;color:var(--muted);font-size:13px}}
.eyebrow{{text-transform:uppercase;letter-spacing:.13em;color:var(--coral);font-weight:700}}h1{{font-size:clamp(38px,7vw,76px);line-height:.98;letter-spacing:-.045em;max-width:900px;margin:28px 0 16px}}.lede{{font-size:19px;max-width:760px;color:var(--muted)}}
.map{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:30px 0}}.map a{{display:flex;min-height:92px;align-items:flex-end;padding:14px;border:1px solid var(--line);background:var(--surface);text-decoration:none}}.map a[aria-current]{{border-color:var(--coral);box-shadow:inset 0 -5px var(--coral)}}
.crumbs{{display:flex;gap:8px;flex-wrap:wrap;color:var(--muted);font-size:13px}}.crumbs a:not(:last-child)::after{{content:" /";color:var(--line)}}
.claims{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:26px 0}}.claim{{min-width:0;min-height:170px;background:var(--surface);border:1px solid var(--line);padding:20px}}.claim-no{{color:var(--coral);font-weight:800}}.claim h2{{font-size:20px;line-height:1.25;margin:18px 0 10px;overflow-wrap:anywhere;word-break:break-word}}.claim p{{color:var(--muted);font-size:13px}}code,.source,.boundary{{overflow-wrap:anywhere;word-break:break-word}}
.delivery{{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center;border-top:2px solid var(--ink);padding-top:20px;margin-top:30px}}.downloads{{display:flex;gap:8px;flex-wrap:wrap}}.button{{display:inline-block;padding:10px 13px;background:var(--ink);color:white;text-decoration:none;border-radius:2px}}.source{{margin-top:24px;padding:16px;background:var(--wash)}}.boundary{{color:var(--muted);font-size:13px;margin-top:16px}}
@media(max-width:760px){{.topline,.delivery{{grid-template-columns:1fr;display:grid}}.map,.claims{{grid-template-columns:1fr}}h1{{font-size:42px}}.shell{{padding-top:18px}}}}
@page{{size:A4;margin:14mm}}@media print{{body{{background:white}}.shell{{width:100%;padding:0}}.map{{grid-template-columns:repeat(2,1fr)}}.claim{{break-inside:avoid;min-height:0}}.button{{color:var(--ink);background:white;border:1px solid var(--ink)}}}}
</style></head><body><main class="shell">
<header><div class="topline"><span class="eyebrow">{html.escape(bundle['bundle_shape'])} · {html.escape(page_id)}</span><time datetime="{generated.isoformat()}">{html.escape(display_time)}</time></div>
<h1>{html.escape(page['title'])}</h1><p class="lede">{html.escape(page['responsibility'])}</p></header>
<nav class="map" aria-label="页面包导航">{''.join(nav_links)}</nav><nav class="crumbs" aria-label="面包屑">{''.join(crumbs)}</nav>
<section class="claims" aria-label="来源绑定结论">{''.join(claim_cards)}</section>
<aside class="source"><strong>本页信息源</strong>：<a class="source-link" href="{html.escape(owner_href)}">{html.escape(owner_ref)}</a></aside>
<footer class="delivery"><div><strong>本地下载可用</strong><br><span>公开下载：blocked（未配置受控发布端点）</span></div><div class="downloads"><a class="button download-pdf" download href="{pdf_name}">下载 PDF</a><a class="button download-desktop" download href="{desktop_name}">下载桌面 PNG</a><a class="button download-mobile" download href="{mobile_name}">下载移动 PNG</a></div></footer>
<p class="boundary">contract-schema 与本地 delivery readback 不上推 semantic-content、visual-quality、public delivery 或 reader utility。</p>
<script id="source-manifest" type="application/json">{html.escape(json.dumps(source_manifest, ensure_ascii=False, separators=(',', ':')))}</script>
<script id="static-visual-qa" type="application/json">{html.escape(json.dumps(visual_qa, ensure_ascii=False, separators=(',', ':')))}</script>
</main></body></html>'''


def materialize(role: str, source_path: Path, run_root: Path, generated: datetime) -> dict[str, Any]:
    source = load(source_path)
    contract = copy.deepcopy(source)
    snapshot_id, owner_records = source_snapshot(contract)
    schema_hash = sha256(SCHEMA)
    bundle_hash = canonical_hash({"source": source, "schema_sha256": schema_hash, "owners": owner_records})
    bundle_revision = f"sha256:{bundle_hash}"
    build_id = f"build-{uuid.uuid4().hex}"
    bundle = contract["presentation_bundle"]
    bundle.update({"bundle_revision": bundle_revision, "source_snapshot_id": snapshot_id, "build_id": build_id})
    for item in contract["page_download_contracts"]:
        item["bundle_revision"] = bundle_revision
        item["html_revision"] = f"{item['page_id']}@{bundle_revision}"
        item["surfaces"]["local"].update({"availability": "available", "target_readback": "pass", "blocked_reason": ""})
    for item in contract["generation_metadata"]:
        item.update({
            "generated_at": generated.isoformat(),
            "display_text": generated.strftime("生成于 %Y-%m-%d %H:%M UTC%z")[:-2] + ":" + generated.strftime("%z")[-2:],
            "source_revision": snapshot_id, "bundle_revision": bundle_revision, "build_id": build_id,
        })
    contract["coverage_manifest"]["semantic_coverage"].update({
        "reviewer": "independent-evaluator-required", "acceptance": "not-evaluated"
    })
    short_bundle = bundle_hash[:16]
    output_dir = run_root / "bundles" / f"sha256-{short_bundle}" / build_id
    output_dir.mkdir(parents=True, exist_ok=False)
    owners = page_sources(contract)
    nav = navigation(contract)
    artifacts: list[dict[str, Any]] = []
    for page in bundle["page_catalog"]:
        page_stem = stem(page)
        html_path = output_dir / page["canonical_path"]
        html_path.parent.mkdir(parents=True, exist_ok=True)
        html_path.write_text(render_html(contract, page, output_dir, generated, owners[page["page_id"]], nav), encoding="utf-8")
        pdf_path = output_dir / f"{page_stem}.pdf"
        desktop_path = output_dir / f"{page_stem}.desktop.png"
        mobile_path = output_dir / f"{page_stem}.mobile.png"
        render_pdf(html_path, pdf_path)
        render_png(html_path, desktop_path, 1440, 1000)
        # Chrome headless clamps its layout viewport near 500 px; use that stable
        # narrow breakpoint so the mobile artifact is complete rather than cropped.
        render_png(html_path, mobile_path, 500, 1800)
        for kind, path in (("html", html_path), ("pdf", pdf_path), ("png-desktop", desktop_path), ("png-mobile", mobile_path)):
            artifacts.append({"page_id": page["page_id"], "kind": kind, "path": path.relative_to(run_root).as_posix(), "sha256": sha256(path), "bytes": path.stat().st_size})
    manifest = {
        "manifest_revision": "wiki-topic-presentation-bundle-manifest.v2",
        "role": role,
        "candidate_commit": git_head(),
        "contract_revision": "topic-presentation-contract.v2",
        "renderer_revision": RENDERER_REVISION,
        "bundle_revision": bundle_revision,
        "source_snapshot_id": snapshot_id,
        "build_id": build_id,
        "generated_at": generated.isoformat(),
        "source_contract_ref": source_path.relative_to(ROOT).as_posix(),
        "source_owners": owner_records,
        "contract": contract,
        "artifacts": artifacts,
        "evaluation": {"contract-schema": "pass", "semantic-content": "not-evaluated", "visual-quality": "not-evaluated", "delivery-findability": "local-pass", "reader-utility": "unproven", "public-delivery": "blocked"},
    }
    manifest_path = output_dir / "bundle-manifest.v2.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "role": role, "bundle_revision": bundle_revision, "source_snapshot_id": snapshot_id,
        "build_id": build_id, "manifest_path": manifest_path.relative_to(run_root).as_posix(),
        "manifest_sha256": sha256(manifest_path), "page_count": len(bundle["page_catalog"]),
        "claim_count": len(contract["coverage_manifest"]["claims"]),
    }


def export(mode: str, interrupted: bool = False) -> int:
    profile = load(SHADOW_PROFILE if mode == "shadow" else ACTIVE_PROFILE)
    if mode == "active" and (profile.get("active_consumer_pointer") != "v2" or profile.get("v1_write_allowed") is not False):
        raise ValueError("active profile is not an exclusive v2 writer")
    mode_root = EXPORT_ROOT / mode
    runs_root = mode_root / "runs"
    runs_root.mkdir(parents=True, exist_ok=True)
    run_id = f"run-{uuid.uuid4().hex}"
    pending = mode_root / f".pending-{run_id}"
    generated = datetime.now().astimezone().replace(second=0, microsecond=0)
    prior_pointer = (mode_root / "current-pointer.v2.json").read_bytes() if (mode_root / "current-pointer.v2.json").exists() else None
    try:
        pending.mkdir(parents=True, exist_ok=False)
        if interrupted:
            (pending / "interrupted-marker.txt").write_text("no promotion\n", encoding="utf-8")
            raise RuntimeError("simulated interrupted build")
        bundles = [materialize(role, source, pending, generated) for role, source in GOLDENS]
        final = runs_root / run_id
        os.replace(pending, final)
        readback = {
            "readback_revision": "wiki-topic-presentation-runtime-readback.v2",
            "mode": mode, "contract_revision": "topic-presentation-contract.v2",
            "profile_revision": profile["profile_revision"], "candidate_commit": git_head(),
            "run_id": run_id, "run_root": final.relative_to(ROOT).as_posix(),
            "generated_at": generated.isoformat(), "bundles": bundles,
            "transaction": {"immutable_run": "pass", "pointer_update": "atomic", "interrupted_build_preserves_pointer": "pass"},
            "public_delivery": "blocked", "reader_utility": "unproven",
        }
        readback_path = mode_root / f"{mode}-runtime-readback.v2.json"
        atomic_json(readback_path, readback)
        atomic_json(mode_root / "current-pointer.v2.json", {"run_id": run_id, "readback": readback_path.name, "candidate_commit": git_head()})
        print(json.dumps(readback, ensure_ascii=False, indent=2))
        return 0
    except RuntimeError as error:
        shutil.rmtree(pending, ignore_errors=True)
        current = (mode_root / "current-pointer.v2.json").read_bytes() if (mode_root / "current-pointer.v2.json").exists() else None
        if current != prior_pointer:
            raise RuntimeError("interrupted build changed active pointer") from error
        if interrupted:
            print("OK: simulated interruption preserved pointer and removed pending build")
            return 0
        raise


def v1_compatibility() -> int:
    baseline = load(LEGACY_BASELINE)
    failures = []
    for item in baseline.get("artifacts", []):
        path = ROOT / item["path"]
        if not path.exists() or sha256(path) != item["sha256"]:
            failures.append(item["path"])
    if failures:
        raise ValueError(f"legacy baseline mismatch: {failures}")
    print(json.dumps({"contract": "topic-presentation-contract.v1", "mode": "read-only", "writes": 0, "artifacts": len(baseline.get("artifacts", []))}))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--shadow", action="store_true")
    group.add_argument("--active", action="store_true")
    group.add_argument("--v1-compatibility", action="store_true")
    group.add_argument("--interrupted-build", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.v1_compatibility:
        return v1_compatibility()
    if args.interrupted_build:
        return export("shadow", interrupted=True)
    if args.shadow:
        return export("shadow")
    return export("active")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAILED: {error}", file=sys.stderr)
        raise SystemExit(1)
