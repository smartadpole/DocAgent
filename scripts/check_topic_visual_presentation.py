#!/usr/bin/env python3
"""Validate the repo-local topic-presentation-contract.v2 implementation."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OWNER = ROOT / "governance"
SCHEMA = OWNER / "topic-presentation-contract.v2.schema.json"
PROFILE = OWNER / "topic-presentation-active-profile.v2.json"
INVENTORY = OWNER / "topic-presentation-verification-inventory.v2.json"
GOLDENS = (
    OWNER / "topic-presentation-golden-single.v2.json",
    OWNER / "topic-presentation-golden-page-tree.v2.json",
)
EXPORTER = ROOT / "scripts/export_topic_presentation_bundle.py"
ACTIVE_ROOT = ROOT / "views/.exports/topic-presentation-v2/active"
ACTIVE_READBACK = ACTIVE_ROOT / "active-runtime-readback.v2.json"
LEGACY_BASELINE = ROOT / "scripts/fixtures/topic-visual-presentation/legacy_artifact_baseline_manifest.v1.json"
TOP_KEYS = {
    "contract_revision", "presentation_bundle_decision", "presentation_bundle",
    "coverage_manifest", "page_download_contracts", "generation_metadata",
}
FORMATS = {"pdf", "png-desktop", "png-mobile"}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_head() -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()


def ensure(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def unique(items: list[Any]) -> bool:
    return len(items) == len(set(items))


def validate_contract(contract: dict[str, Any], *, source_check: bool = True) -> list[str]:
    errors: list[str] = []
    ensure(errors, set(contract) == TOP_KEYS, f"schema: top-level keys differ: {sorted(set(contract) ^ TOP_KEYS)}")
    if set(contract) != TOP_KEYS:
        return errors
    ensure(errors, contract["contract_revision"] == "topic-presentation-contract.v2", "schema: wrong contract revision")
    decision = contract["presentation_bundle_decision"]
    bundle = contract["presentation_bundle"]
    shape = decision.get("bundle_shape")
    ensure(errors, shape in {"single-page", "page-tree"}, "schema: invalid bundle shape")
    ensure(errors, bundle.get("bundle_shape") == shape, "schema: decision/bundle shape mismatch")
    ensure(errors, bundle.get("contract_revision") == "topic-presentation-contract.v2", "schema: bundle revision mismatch")
    ensure(errors, decision.get("materialization") in {"inline", "ephemeral", "current", "snapshot"}, "schema: invalid materialization")
    ensure(errors, decision.get("split_benefit") in {"low", "medium", "high"}, "schema: invalid split benefit")
    ensure(errors, decision.get("navigation_cost") in {"low", "medium", "high"}, "schema: invalid navigation cost")
    pages = bundle.get("page_catalog", [])
    page_ids = [item.get("page_id") for item in pages]
    ensure(errors, bool(pages) and unique(page_ids), "tree: missing or duplicate page_id")
    root_id = bundle.get("root_page_id")
    ensure(errors, root_id in page_ids, "tree: root page missing")
    ensure(errors, len(pages) <= decision.get("page_count_budget", 0), "tree: page count exceeds budget")
    edges = bundle.get("canonical_tree", {}).get("edges", [])
    ensure(errors, bundle.get("canonical_tree", {}).get("edge_source") == "edges", "tree: edges are not canonical source")
    parents: dict[str, str] = {}
    children: dict[str, list[str]] = {page_id: [] for page_id in page_ids}
    for edge in edges:
        parent, child = edge.get("parent_page_id"), edge.get("child_page_id")
        ensure(errors, parent in page_ids and child in page_ids and parent != child, f"tree: invalid edge {parent}->{child}")
        if child in parents:
            errors.append(f"tree: multiple parents for {child}")
        parents[child] = parent
        if parent in children:
            children[parent].append(child)
    if shape == "single-page":
        ensure(errors, len(pages) == 1 and not edges, "tree: single-page must have one page and zero edges")
        ensure(errors, decision.get("split_guard") == "fail", "decision: cohesive single page must reject split")
    else:
        ensure(errors, len(pages) > 1 and len(edges) == len(pages) - 1, "tree: page-tree must have n-1 edges")
        ensure(errors, decision.get("split_guard") == "pass", "decision: page-tree split guard not passed")
        ensure(errors, bool(decision.get("independent_module_boundaries")), "decision: page-tree lacks independent boundaries")
        reached: set[str] = set()
        queue = [root_id]
        while queue:
            node = queue.pop(0)
            if node in reached:
                errors.append("tree: cycle detected")
                break
            reached.add(node)
            queue.extend(children.get(node, []))
        ensure(errors, reached == set(page_ids), f"tree: orphan/unreachable pages {sorted(set(page_ids) - reached)}")
    coverage = contract["coverage_manifest"]
    units = {item.get("unit_id") for item in coverage.get("information_units", [])}
    claims = {item.get("claim_id"): item for item in coverage.get("claims", [])}
    fragments = {item.get("source_fragment_id"): item for item in coverage.get("source_fragments", [])}
    sections = {item.get("rendered_section_id"): item for item in coverage.get("rendered_sections", [])}
    bindings = coverage.get("page_bindings", [])
    ensure(errors, None not in units and len(units) == len(coverage.get("information_units", [])), "coverage: duplicate/missing units")
    ensure(errors, None not in claims and len(claims) == len(coverage.get("claims", [])), "coverage: duplicate/missing claims")
    ensure(errors, None not in fragments and len(fragments) == len(coverage.get("source_fragments", [])), "coverage: duplicate/missing fragments")
    ensure(errors, None not in sections and len(sections) == len(coverage.get("rendered_sections", [])), "coverage: duplicate/missing sections")
    quads = []
    bound_units = []
    page_owners: dict[str, set[str]] = {page_id: set() for page_id in page_ids}
    for binding in bindings:
        quad = tuple(binding.get(key) for key in ("unit_id", "claim_id", "source_fragment_id", "rendered_section_id"))
        quads.append(quad)
        bound_units.append(binding.get("unit_id"))
        ensure(errors, binding.get("page_id") in page_ids, "coverage: binding page missing")
        ensure(errors, binding.get("unit_id") in units, "coverage: binding unit missing")
        ensure(errors, binding.get("claim_id") in claims, "coverage: binding claim missing")
        ensure(errors, binding.get("source_fragment_id") in fragments, "coverage: binding fragment missing")
        ensure(errors, binding.get("rendered_section_id") in sections, "coverage: binding section missing")
        if binding.get("claim_id") in claims:
            ensure(errors, claims[binding["claim_id"]].get("unit_id") == binding.get("unit_id"), "coverage: claim/unit mismatch")
        if binding.get("rendered_section_id") in sections:
            ensure(errors, sections[binding["rendered_section_id"]].get("page_id") == binding.get("page_id"), "coverage: section/page mismatch")
        if binding.get("source_fragment_id") in fragments and binding.get("page_id") in page_owners:
            page_owners[binding["page_id"]].add(fragments[binding["source_fragment_id"]].get("owner_ref", ""))
    ensure(errors, unique(quads), "coverage: duplicate claim binding")
    ensure(errors, set(bound_units) == units and len(bound_units) == len(units), "coverage: every unit must bind exactly once")
    structural = coverage.get("structural_coverage", {})
    ensure(errors, set(structural.get("expected_unit_ids", [])) == units, "coverage: expected units mismatch")
    ensure(errors, set(structural.get("bound_unit_ids", [])) == units, "coverage: bound units mismatch")
    ensure(errors, structural.get("uncovered_unit_ids") == [] and structural.get("invalid_bindings") == [], "coverage: tracked candidate has unresolved bindings")
    ensure(errors, structural.get("acceptance") == "pass", "coverage: structural acceptance not pass")
    semantic = coverage.get("semantic_coverage", {})
    ensure(errors, semantic.get("acceptance") == "not-evaluated", "evaluation: builder candidate cannot self-pass semantic")
    ensure(errors, semantic.get("reviewer") == "independent-evaluator-required", "evaluation: independent reviewer boundary missing")
    for page_id, owners in page_owners.items():
        ensure(errors, len(owners) == 1 and all(ref.endswith(".md") for ref in owners), f"source: page {page_id} must have exactly one Markdown owner")
    if source_check:
        for fragment in fragments.values():
            ref, needle = fragment.get("owner_ref", ""), fragment.get("rendered_text", "")
            source = ROOT / ref
            ensure(errors, source.is_file(), f"source: owner missing {ref}")
            if source.is_file():
                ensure(errors, bool(needle) and needle in source.read_text(encoding="utf-8"), f"source: selector text missing {ref}::{needle}")
    download_ids = [item.get("page_id") for item in contract["page_download_contracts"]]
    ensure(errors, set(download_ids) == set(page_ids) and unique(download_ids), "delivery: one download contract required per page")
    for item in contract["page_download_contracts"]:
        ensure(errors, {artifact.get("format") for artifact in item.get("artifacts", [])} == FORMATS, "delivery: PDF/desktop/mobile artifacts required")
        ensure(errors, item.get("surfaces", {}).get("local", {}).get("delivery_adapter") == "local-export-resolver", "delivery: local resolver missing")
        ensure(errors, item.get("surfaces", {}).get("public", {}).get("availability") == "blocked", "delivery: public must remain blocked without endpoint")
    generation_ids = [item.get("page_id") for item in contract["generation_metadata"]]
    ensure(errors, set(generation_ids) == set(page_ids) and unique(generation_ids), "time: one generation record required per page")
    ensure(errors, all(item.get("precision") == "minute" for item in contract["generation_metadata"]), "time: precision must be minute")
    return errors


def verify_legacy() -> list[str]:
    errors: list[str] = []
    baseline = load(LEGACY_BASELINE)
    for item in baseline.get("artifacts", []):
        path = ROOT / item["path"]
        ensure(errors, path.is_file(), f"legacy: missing {item['path']}")
        if path.is_file():
            ensure(errors, sha256(path) == item["sha256"], f"legacy: grandfather changed {item['path']}")
    return errors


def portable() -> list[str]:
    errors: list[str] = []
    for path in (SCHEMA, PROFILE, INVENTORY, EXPORTER, *GOLDENS):
        ensure(errors, path.is_file(), f"portable: missing {path.relative_to(ROOT)}")
    if errors:
        return errors
    schema = load(SCHEMA)
    ensure(errors, schema.get("$id") == "wiki://topic-presentation/topic-presentation-contract.v2.schema.json", "schema: repo-local id missing")
    ensure(errors, schema.get("additionalProperties") is False, "schema: top-level additionalProperties must be false")
    profile = load(PROFILE)
    ensure(errors, profile.get("contract_revision") == "topic-presentation-contract.v2", "profile: wrong contract")
    ensure(errors, profile.get("activation_state") == "active" and profile.get("active_consumer_pointer") == "v2", "profile: v2 not active")
    ensure(errors, profile.get("v1_write_allowed") is False, "profile: v1 writer not frozen")
    ensure(errors, profile.get("schema_sha256") == sha256(SCHEMA), "profile: schema hash mismatch")
    ensure(errors, profile.get("dependency_inventory_sha256") == sha256(INVENTORY), "profile: inventory hash mismatch")
    ensure(errors, profile.get("public_delivery") == "blocked" and profile.get("reader_utility") == "unproven", "profile: evidence boundary promoted")
    inventory = load(INVENTORY)
    surfaces = inventory.get("active_writer_surfaces", []) + inventory.get("routing_and_discovery_surfaces", []) + inventory.get("legacy_read_only_surfaces", [])
    ensure(errors, unique(surfaces), "inventory: duplicate surface")
    for rel in surfaces:
        ensure(errors, (ROOT / rel).is_file(), f"inventory: missing surface {rel}")
    for rel, terms in inventory.get("required_terms", {}).items():
        path = ROOT / rel
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for term in terms:
                ensure(errors, term in text, f"inventory: {rel} missing {term}")
    ensure(errors, inventory.get("portable_gate", {}).get("exports_required") is False, "portable: exports must not be required")
    for golden in GOLDENS:
        errors.extend(f"{golden.name}: {error}" for error in validate_contract(load(golden)))
    errors.extend(verify_legacy())
    active_text = "\n".join(
        (ROOT / rel).read_text(encoding="utf-8", errors="ignore")
        for rel in inventory.get("active_writer_surfaces", [])
        if (ROOT / rel).is_file() and not rel.startswith("scripts/")
    )
    ensure(errors, "active_consumer_pointer=v1" not in active_text, "compatibility: active v1 pointer residual")
    ensure(errors, "dual-write" not in active_text.lower() or "禁止 dual-write" in active_text or "no dual-write" in active_text.lower(), "compatibility: dual-write residual")
    return errors


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"not PNG: {path}")
    return struct.unpack(">II", data[16:24])


def png_trailing_uniform_ratio(path: Path) -> float:
    """Measure the bottom uniform-color tail of an RGB/RGBA PNG."""
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"not PNG: {path}")
    position = 8
    compressed = bytearray()
    width = height = color_type = bit_depth = interlace = 0
    while position < len(data):
        length = struct.unpack(">I", data[position:position + 4])[0]
        kind = data[position + 4:position + 8]
        chunk = data[position + 8:position + 8 + length]
        position += 12 + length
        if kind == b"IHDR":
            width, height, bit_depth, color_type, _, _, interlace = struct.unpack(">IIBBBBB", chunk)
        elif kind == b"IDAT":
            compressed.extend(chunk)
        elif kind == b"IEND":
            break
    channels = {2: 3, 6: 4}.get(color_type)
    if bit_depth != 8 or channels is None or interlace != 0:
        raise ValueError("blank-tail sensor requires non-interlaced 8-bit RGB/RGBA PNG")
    raw = zlib.decompress(bytes(compressed))
    stride = width * channels
    previous = bytearray(stride)
    rows: list[bytearray] = []
    cursor = 0
    for _ in range(height):
        filter_type = raw[cursor]
        cursor += 1
        current = bytearray(raw[cursor:cursor + stride])
        cursor += stride
        for offset in range(stride):
            left = current[offset - channels] if offset >= channels else 0
            above = previous[offset]
            upper_left = previous[offset - channels] if offset >= channels else 0
            if filter_type == 1:
                predictor = left
            elif filter_type == 2:
                predictor = above
            elif filter_type == 3:
                predictor = (left + above) // 2
            elif filter_type == 4:
                estimate = left + above - upper_left
                distances = (abs(estimate - left), abs(estimate - above), abs(estimate - upper_left))
                predictor = (left, above, upper_left)[distances.index(min(distances))]
            elif filter_type == 0:
                predictor = 0
            else:
                raise ValueError(f"unsupported PNG filter: {filter_type}")
            current[offset] = (current[offset] + predictor) & 0xFF
        rows.append(current)
        previous = current
    background = rows[-1][-channels:-channels + 3] if channels == 4 else rows[-1][-3:]
    sample_step = max(channels, (stride // 64 // channels) * channels)
    tail_rows = 0
    for row in reversed(rows):
        samples = (row[offset:offset + 3] for offset in range(0, stride, sample_step))
        if all(max(abs(sample[channel] - background[channel]) for channel in range(3)) <= 3 for sample in samples if len(sample) == 3):
            tail_rows += 1
        else:
            break
    return tail_rows / height if height else 1.0


def runtime(regenerate: bool) -> list[str]:
    errors = portable()
    if errors:
        return errors
    if regenerate:
        result = subprocess.run([sys.executable, str(EXPORTER), "--active"], cwd=ROOT, text=True, capture_output=True)
        ensure(errors, result.returncode == 0, f"runtime: regeneration failed: {result.stderr.strip()}")
    ensure(errors, ACTIVE_READBACK.is_file(), "runtime: active readback missing")
    if errors:
        return errors
    readback = load(ACTIVE_READBACK)
    ensure(errors, readback.get("mode") == "active" and readback.get("contract_revision") == "topic-presentation-contract.v2", "runtime: wrong mode/contract")
    ensure(errors, readback.get("candidate_commit") == git_head(), "runtime: readback HEAD mismatch")
    ensure(errors, readback.get("public_delivery") == "blocked" and readback.get("reader_utility") == "unproven", "runtime: evidence boundary promoted")
    run_root = ROOT / readback.get("run_root", "missing")
    ensure(errors, run_root.is_dir(), "runtime: immutable run root missing")
    for bundle_ref in readback.get("bundles", []):
        manifest_path = run_root / bundle_ref.get("manifest_path", "missing")
        ensure(errors, manifest_path.is_file(), f"runtime: manifest missing {manifest_path}")
        if not manifest_path.is_file():
            continue
        ensure(errors, sha256(manifest_path) == bundle_ref.get("manifest_sha256"), "runtime: manifest hash mismatch")
        manifest = load(manifest_path)
        for key in ("bundle_revision", "source_snapshot_id", "build_id"):
            ensure(errors, manifest.get(key) == bundle_ref.get(key), f"runtime: {key} identity mismatch")
        ensure(errors, manifest.get("candidate_commit") == git_head(), "runtime: manifest HEAD mismatch")
        contract = manifest.get("contract", {})
        ensure(errors, contract.get("presentation_bundle", {}).get("bundle_revision") == manifest.get("bundle_revision"), "runtime: contract bundle mismatch")
        ensure(errors, contract.get("presentation_bundle", {}).get("source_snapshot_id") == manifest.get("source_snapshot_id"), "runtime: contract source mismatch")
        ensure(errors, contract.get("presentation_bundle", {}).get("build_id") == manifest.get("build_id"), "runtime: contract build mismatch")
        ensure(errors, manifest.get("evaluation", {}).get("semantic-content") == "not-evaluated", "runtime: semantic self-promotion")
        ensure(errors, manifest.get("evaluation", {}).get("visual-quality") == "not-evaluated", "runtime: visual self-promotion")
        ensure(errors, manifest.get("evaluation", {}).get("reader-utility") == "unproven", "runtime: reader utility self-promotion")
        pages = {page["page_id"]: page for page in contract.get("presentation_bundle", {}).get("page_catalog", [])}
        page_artifacts: dict[str, dict[str, Path]] = {page_id: {} for page_id in pages}
        for artifact in manifest.get("artifacts", []):
            path = run_root / artifact.get("path", "missing")
            ensure(errors, path.is_file(), f"runtime: artifact missing {artifact.get('path')}")
            if path.is_file():
                ensure(errors, sha256(path) == artifact.get("sha256"), f"runtime: artifact hash mismatch {artifact.get('path')}")
                ensure(errors, path.stat().st_size == artifact.get("bytes"), f"runtime: artifact byte count mismatch {artifact.get('path')}")
                page_artifacts.setdefault(artifact["page_id"], {})[artifact["kind"]] = path
        bindings_by_page: dict[str, list[str]] = {page_id: [] for page_id in pages}
        for binding in contract.get("coverage_manifest", {}).get("page_bindings", []):
            bindings_by_page.setdefault(binding["page_id"], []).append(binding["claim_id"])
        for page_id, artifacts in page_artifacts.items():
            ensure(errors, set(artifacts) == {"html", "pdf", "png-desktop", "png-mobile"}, f"runtime: incomplete page artifacts {page_id}")
            if "html" not in artifacts:
                continue
            text = artifacts["html"].read_text(encoding="utf-8")
            ensure(errors, len(re.findall(r'class="source-link"', text)) == 1, f"runtime: {page_id} must expose one source link")
            ensure(errors, len(re.findall(r'href="[^"]+\.md"', text)) == 1, f"runtime: {page_id} must expose only current owner Markdown link")
            ensure(errors, all(token in text for token in ("download-pdf", "download-desktop", "download-mobile")), f"runtime: download controls missing {page_id}")
            ensure(errors, bool(re.search(r'<time datetime="\d{4}-\d\d-\d\dT\d\d:\d\d:00[+-]\d\d:\d\d">', text)), f"runtime: minute timezone timestamp missing {page_id}")
            ensure(errors, "公开下载：blocked" in text, f"runtime: public blocked label missing {page_id}")
            ensure(errors, "/Users/" not in text and "views/.exports" not in text, f"runtime: local path leaked {page_id}")
            for claim_id in bindings_by_page.get(page_id, []):
                ensure(errors, f'data-claim-id="{claim_id}"' in text, f"runtime: hidden/missing claim {claim_id}")
            if "png-desktop" in artifacts:
                desktop_width, desktop_height = png_dimensions(artifacts["png-desktop"])
                ensure(errors, desktop_width == 1440 and desktop_height >= 500, f"runtime: desktop PNG size mismatch {page_id}")
                ensure(errors, png_trailing_uniform_ratio(artifacts["png-desktop"]) <= 0.20, f"runtime: desktop PNG blank tail exceeds 20% {page_id}")
            if "png-mobile" in artifacts:
                mobile_width, mobile_height = png_dimensions(artifacts["png-mobile"])
                ensure(errors, mobile_width == 500 and mobile_height >= 700, f"runtime: mobile PNG size mismatch {page_id}")
                ensure(errors, png_trailing_uniform_ratio(artifacts["png-mobile"]) <= 0.20, f"runtime: mobile PNG blank tail exceeds 20% {page_id}")
            if "pdf" in artifacts:
                info = subprocess.run(["pdfinfo", str(artifacts["pdf"])], capture_output=True, text=True)
                match = re.search(r"^Pages:\s+(\d+)", info.stdout, re.M)
                ensure(errors, info.returncode == 0 and match is not None, f"runtime: PDF unreadable {page_id}")
                ensure(errors, match is not None and int(match.group(1)) == 1, f"runtime: PDF must be one page without orphan tail {page_id}")
                if match is not None and int(match.group(1)) == 1:
                    with tempfile.TemporaryDirectory(prefix="wiki-topic-pdf-tail-") as temporary:
                        prefix = Path(temporary) / "page"
                        raster = subprocess.run(["pdftoppm", "-png", "-r", "120", str(artifacts["pdf"]), str(prefix)], capture_output=True, text=True)
                        page_png = prefix.with_name("page-1.png")
                        ensure(errors, raster.returncode == 0 and page_png.is_file(), f"runtime: PDF raster readback failed {page_id}")
                        if page_png.is_file():
                            ensure(errors, png_trailing_uniform_ratio(page_png) <= 0.20, f"runtime: PDF blank tail exceeds 20% {page_id}")
    return errors


def export_snapshot() -> dict[str, str]:
    if not (ROOT / "views/.exports").exists():
        return {}
    return {path.relative_to(ROOT).as_posix(): sha256(path) for path in (ROOT / "views/.exports").rglob("*") if path.is_file()}


def v1_compatibility() -> list[str]:
    errors = portable()
    before = export_snapshot()
    result = subprocess.run([sys.executable, str(EXPORTER), "--v1-compatibility"], cwd=ROOT, text=True, capture_output=True)
    after = export_snapshot()
    ensure(errors, result.returncode == 0, f"compatibility: v1 readback failed {result.stderr.strip()}")
    ensure(errors, before == after, "compatibility: v1 check wrote runtime artifacts")
    ensure(errors, '"writes": 0' in result.stdout, "compatibility: zero-write proof missing")
    return errors


def negative_suite() -> list[str]:
    errors = portable()
    base = load(GOLDENS[1])
    mutations: list[tuple[str, dict[str, Any]]] = []
    item = copy.deepcopy(base); item["presentation_bundle"]["page_catalog"].append(copy.deepcopy(item["presentation_bundle"]["page_catalog"][0])); mutations.append(("duplicate-page", item))
    item = copy.deepcopy(base); item["presentation_bundle"]["canonical_tree"]["edges"].append({"parent_page_id": "contract-template", "child_page_id": "evaluation-contract", "order": 9}); mutations.append(("multiple-parent", item))
    item = copy.deepcopy(base); item["presentation_bundle"]["canonical_tree"]["edges"].pop(); mutations.append(("orphan", item))
    item = copy.deepcopy(base); item["coverage_manifest"]["page_bindings"].pop(); mutations.append(("fake-coverage", item))
    item = copy.deepcopy(base); item["coverage_manifest"]["semantic_coverage"]["acceptance"] = "pass"; item["coverage_manifest"]["semantic_coverage"]["reviewer"] = "builder"; mutations.append(("self-semantic-pass", item))
    item = copy.deepcopy(base); item["page_download_contracts"][0]["artifacts"] = item["page_download_contracts"][0]["artifacts"][:1]; mutations.append(("missing-png", item))
    item = copy.deepcopy(base); item["page_download_contracts"][0]["surfaces"]["public"]["availability"] = "available"; mutations.append(("fake-public", item))
    item = copy.deepcopy(base); item["generation_metadata"][0]["precision"] = "second"; mutations.append(("wrong-time-precision", item))
    item = copy.deepcopy(base); item["coverage_manifest"]["source_fragments"][1]["owner_ref"] = "governance/topic-visual-presentation-rules.md"; mutations.append(("many-owner-links", item))
    item = copy.deepcopy(base); item["presentation_bundle_decision"]["split_guard"] = "fail"; mutations.append(("tree-without-split-proof", item))
    for name, mutation in mutations:
        ensure(errors, bool(validate_contract(mutation, source_check=False)), f"negative: mutation passed {name}")
    pointer = ACTIVE_ROOT / "current-pointer.v2.json"
    prior = pointer.read_bytes() if pointer.exists() else None
    result = subprocess.run([sys.executable, str(EXPORTER), "--interrupted-build"], cwd=ROOT, text=True, capture_output=True)
    current = pointer.read_bytes() if pointer.exists() else None
    ensure(errors, result.returncode == 0 and prior == current, "negative: interrupted shadow build changed active pointer")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("portable-structure", "runtime-artifact-readback", "negative-suite", "v1-compatibility"), default="portable-structure")
    parser.add_argument("--regenerate", action="store_true")
    args = parser.parse_args()
    if args.mode == "portable-structure":
        errors = portable()
    elif args.mode == "runtime-artifact-readback":
        errors = runtime(args.regenerate)
    elif args.mode == "negative-suite":
        errors = negative_suite()
    else:
        errors = v1_compatibility()
    if errors:
        print("FAILED: topic presentation v2", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: topic presentation v2 {args.mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
