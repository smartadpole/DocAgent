---
type: evaluation-contract
id: GOV-TOPIC-VISUAL-PRESENTATION-EVALUATION-001
status: active
rubric_revision: wiki-topic-presentation-semantic-rubric.v2
calibration_revision: wiki-topic-presentation-intent-calibration.v1
---

# Topic Visual Presentation Evaluation Contract

`contract-schema / semantic-content / visual-quality / delivery-findability / reader-utility` are independent. The deterministic sensor is `scripts/check_topic_visual_presentation.py`; semantic-content requires a builder-independent model judge and a trace using this rubric revision. A builder, author, `self`, or `same-agent` value is rejected.

The representative wiki single-page and real page-tree samples may have local HTML/PDF/desktop PNG/mobile PNG readback evidence. Their semantic-content and visual-quality remain `not-evaluated` until a builder-independent model judge/reviewer evaluates the exact bundle/build/manifest identity. Reader utility is explicitly `unproven`: this implementation agent is not allowed to self-certify it. Public delivery remains `blocked` without a controlled endpoint and live readback.

Portable structure, runtime artifact readback, semantic-content, visual-quality, delivery-findability and reader-utility are separate outcomes. A later independent evaluator must bind candidate hash, bundle revision, source snapshot, build id, manifest hash, verdict, disagreement handling and cannot-promote boundaries; no generic human veto exists.
