#!/usr/bin/env python3
"""Validate wiki topic-visual-presentation wiring, mutations and runtime evidence."""
from __future__ import annotations

import argparse, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "scripts/fixtures/topic-visual-presentation"
REQUIRED = (
    "skills/topic-visual-presentation/SKILL.md", "skills/topic-visual-presentation/TRANSFER.md",
    "concepts/topic-information-presentation.md", "templates/topic-presentation-template.md",
    "governance/topic-visual-presentation-rules.md", "governance/topic-visual-presentation-evaluation.md",
    "views/current/topic-visual-presentation-system.html", "views/lens-registry.md",
    "scripts/fixtures/topic-visual-presentation/legacy_artifact_baseline_manifest.v1.json",
)
PROFILE_FIELDS = ("repository", "need", "existing_skill", "local_owner_roots", "renderer", "design_system", "evidence_layers", "views_layer", "publication", "local_deltas", "compatibility", "sample_set", "validation")
EXEMPT_LEGACY = {"log.md", "views/current/markdown-owner-viewer.html", "views/current/problem-focused-visual-presentation-system-sample.html", "scripts/check_topic_visual_presentation.py", "scripts/check_project_docs.py", "scripts/fixtures/topic-visual-presentation/legacy_artifact_baseline_manifest.v1.json"}
OLD = re.compile(r"problem-focused-visual-presentation|problem-focused-lens-template|check_problem_focused_visual_presentation", re.I)
SELF = {"", "self", "builder", "author", "same-agent", "none", "n/a"}

def load(path): return json.loads(path.read_text(encoding="utf-8"))
def error_if(errors, condition, message):
    if condition: errors.append(message)

def validate(doc):
    errs=[]
    if doc.get("presentation_eligibility") != "admit": return errs
    intent=doc.get("intent_routing_contract", {})
    error_if(errs, intent.get("content_scope") not in {"topic", "problem-focus"}, "contract-schema: invalid content_scope")
    error_if(errs, not intent.get("confidence", {}).get("calibration_revision"), "contract-schema: missing calibration_revision")
    axes=doc.get("runtime_axes", {})
    error_if(errs, axes.get("task_state") not in {"understand","compare","decide","act","verify","review"}, "contract-schema: missing/invalid task_state")
    error_if(errs, axes.get("content_scope") not in {"topic", "problem-focus"}, "contract-schema: missing/invalid runtime content_scope")
    error_if(errs, axes.get("materialization") not in {"inline","ephemeral","current","snapshot"}, "contract-schema: missing/invalid materialization")
    source=doc.get("source_pack", {})
    error_if(errs, not source.get("sources") or not source.get("evidence_bindings"), "contract-schema: admit requires non-empty source_pack")
    rep=doc.get("representation", {})
    error_if(errs, rep.get("primary_format") != "html" or set(rep.get("same_source_exports", [])) != {"pdf", "png"}, "contract-schema: admit requires HTML plus PDF/PNG")
    error_if(errs, any(rep.get("export_readback", {}).get(k) != "pass" for k in ("html","pdf","png")), "contract-schema: missing export readback")
    sem=doc.get("evaluation", {}).get("semantic-content", {})
    judge=str(sem.get("independent_model_judge", "")).lower()
    error_if(errs, judge in SELF or not sem.get("rubric_revision") or not sem.get("trace_ref"), "semantic-content: self/missing judge trace")
    return errs

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--verify-runtime", action="store_true"); args=parser.parse_args(); errors=[]
    for rel in REQUIRED:
        error_if(errors, not (ROOT/rel).exists(), f"missing: {rel}")
    rules=(ROOT/"governance/topic-visual-presentation-rules.md").read_text(encoding="utf-8")
    for field in PROFILE_FIELDS:
        error_if(errors, f"  {field}:" not in rules, f"topic_presentation_profile missing {field}")
    profile_block=rules.split("topic_presentation_profile:", 1)[1].split("```", 1)[0] if "topic_presentation_profile:" in rules else ""
    error_if(errors, "  repository: wiki" not in profile_block, "topic_presentation_profile repository must be stable repo id wiki")
    error_if(errors, "/Users/" in profile_block or "repository: /" in profile_block, "topic_presentation_profile repository must not be checkout path")
    error_if(errors, "  need: required" not in profile_block and "  need: optional" not in profile_block and "  need: not-applicable" not in profile_block, "topic_presentation_profile invalid need")
    error_if(errors, "  views:" in profile_block, "topic_presentation_profile must use views_layer, not views")
    mutations = (
        profile_block.replace("  repository:", "  removed_repository:"),
        profile_block.replace("  repository: wiki", "  repository: /tmp/wiki"),
        profile_block.replace("  need: required", "  need: invented"),
        profile_block.replace("  views_layer:", "  views:"),
    )
    for index, mutated in enumerate(mutations, 1):
        valid = all(f"  {field}:" in mutated for field in PROFILE_FIELDS)
        valid = valid and "  repository: wiki" in mutated and "/Users/" not in mutated and "repository: /" not in mutated
        valid = valid and any(f"  need: {value}" in mutated for value in ("required", "optional", "not-applicable"))
        valid = valid and "  views:" not in mutated
        error_if(errors, valid, f"profile mutation {index} did not fail")
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".py", ".json", ".html"}: continue
        rel=path.relative_to(ROOT).as_posix()
        if rel in EXEMPT_LEGACY or rel.startswith(("archive/", "raw/", "inbox/", "assets/", ".obsidian/", "views/.exports/", "projects/development/reports/", "projects/retrospectives/")): continue
        text=path.read_text(encoding="utf-8", errors="ignore")
        if rel == "views/lens-registry.md" and "## Legacy grandfather artifacts" in text: text=text.split("## Legacy grandfather artifacts", 1)[0]
        if rel == "views/current/README.md": text="\n".join(line for line in text.splitlines() if "grandfathered legacy sample" not in line)
        if rel == "views/publication.md": text="\n".join(line for line in text.splitlines() if "legacy compatibility" not in line)
        if OLD.search(text): errors.append(f"legacy active residual: {rel}")
    for name, expected in (("positive-structure.v1.json", False), ("positive-problem-focus.v1.json", False), ("negative-empty-source-pack.v1.json", True), ("negative-missing-png-export.v1.json", True), ("negative-self-judged-semantic.v1.json", True)):
        outcome=bool(validate(load(FIX/name)))
        error_if(errors, outcome != expected, f"mutation mismatch: {name}")
    baseline=load(FIX/"legacy_artifact_baseline_manifest.v1.json")
    for item in baseline["artifacts"]:
        path=ROOT/item["path"]
        actual=hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else "missing"
        error_if(errors, actual != item["sha256"], f"legacy baseline changed: {item['path']}")
    if args.verify_runtime:
        export=ROOT/"views/.exports/topic-visual-presentation-system/export-readback.v1.json"
        error_if(errors, not export.exists(), "runtime evidence missing")
        if export.exists():
            data=load(export); error_if(errors, data.get("html") != "pass" or data.get("pdf") != "pass" or data.get("png") != "pass", "runtime export readback failed")
    if errors:
        print("FAILED: topic visual presentation", file=sys.stderr); print("\n".join(errors), file=sys.stderr); return 1
    print("OK: topic visual presentation wiring and mutation checks passed")
    return 0
if __name__ == "__main__": raise SystemExit(main())
