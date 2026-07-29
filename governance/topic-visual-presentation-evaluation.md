---
type: evaluation-contract
id: GOV-TOPIC-VISUAL-PRESENTATION-EVALUATION-001
status: active
rubric_revision: topic-presentation-semantic-rubric.v1
calibration_revision: wiki-topic-presentation-intent-calibration.v1
---

# Topic Visual Presentation Evaluation Contract

`contract-schema / semantic-content / visual-quality / delivery-findability / reader-utility` are independent. The deterministic sensor is `scripts/check_topic_visual_presentation.py`; semantic-content requires a builder-independent model judge and a trace using this rubric revision. A builder, author, `self`, or `same-agent` value is rejected.

The representative wiki sample has HTML/PDF/PNG readback evidence. Its semantic independent judge and reader utility are explicitly `unproven`: this implementation agent is not allowed to self-certify them. A later independent evaluator must append candidate hash, input refs, verdict, disagreement handling and cannot-promote boundaries; no generic human veto exists.
