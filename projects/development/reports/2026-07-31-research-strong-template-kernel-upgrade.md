---
type: test_report
id: REPORT-2026-07-31-RESEARCH-STRONG-TEMPLATE-KERNEL
status: passed-local
updated: 2026-07-31
tags: [research-capability, template-kernel, evaluator, skill-maturity]
---

# 调研能力 Strong Template Kernel 升级验证

## 验证对象与计划来源

- 验证对象：wiki 本地 research profile、聚合技能、技术执行分支、治理合同、模板、结构化 validator、正负 fixture、入口与持久化 owner。
- 合同版本：`research-contract.v1`。
- 用户合同：把 wiki 升级为 `strong template-kernel absorption`，完整承接可迁移研究合同、运行闭环和评价机制；AcknowledgeBase 保留上游设计与领域知识，不在 wiki 建第二事实源。
- 设计来源：[[projects/design/topics/implementation-engineering-template-system]] 的完整 Template Kernel 与 `research-intelligence-pack`。
- 轻量测试计划：结构接线、正向合同、四个负向边界、直接 case 校验、相关回归、完整门禁和 Git 收尾读回。
- 不关闭对象：本报告不关闭 TASK / EP / FP / Gate，不证明任意未来研究 case 的语义质量、读者效用、采购 / 合规批准或生产采用。

## 吸收裁决

| 能力 | 缺口类型 | 处理 | 本地 owner | 不吸收边界 |
| --- | --- | --- | --- | --- |
| medium profile 与完整 Template Kernel 冲突 | true-gap | upgrade | `.codex/research-capability-profile.md` | 不夺取上游 design owner |
| R2+ Source Plan / coverage | true-gap | upgrade | [[skills/research-capability/SKILL]]、research templates | 不复制 source project case |
| Evidence Delta Re-open | true-gap | adapt / upgrade | skill、governance、contract / report template | 不复制领域正文和原始材料 |
| local / PoC / runtime evidence 与 Adopt 绑定 | true-gap | upgrade | [[research-capability-rules]]、adoption contract、validator | 不替代验收、采购、合规或人工批准 |
| 13 个研究子技能目录 | recognition / signal-only | merge | 聚合技能 + method route map | 不平铺空 skill |
| 正负行为边界 | true-gap | complete | `scripts/check_research_capability.py` + fixtures | fixture 不等于真实 outcome corpus |

## 核心用例与结果

| 用例 | 输入 / 变体 | Oracle | 结果 |
| --- | --- | --- | --- |
| 正向 R3 Trial | source plan、coverage、反证齐全；无本地 PoC | 允许 Trial，禁止越级 Adopt | passed |
| 正向 Evidence Delta Adopt | R2、L1、local validation、独立 review、结论重算 | 允许 design-scope Adopt | passed |
| 负向 R3 无 Source Plan | `checkpoint=blocked`、coverage 为空 | 必须命中 source-plan / coverage 错误 | passed |
| 负向 Adopt 无验证 | L1 存在，但 local validation 与 outcome review 缺失 | 必须拒绝 Adopt | passed |
| 负向 Production Adopt 无 runtime readback | L1、local validation 和 outcome review 存在，但生产 claim 无 runtime readback | 必须拒绝 production Adopt | passed |
| 负向 Evidence Delta 未重开 | 新材料存在，但无外部核验、反证、传播和结论重算 | 必须命中 Evidence Delta 错误 | passed |

## 分层验证结论

- local validation：`research-capability` 专项 sensor 和结构化 fixture 已通过。
- service-side validation：不适用；本能力没有独立在线服务。
- end-to-end validation：完成“profile -> skill / governance / template -> JSON contract validator -> positive / negative oracle -> check_all”本地链路；尚无真实外部研究 case 的独立 evaluator outcome。
- manual boundary：研究语义正确性、读者效用、采购 / 合规 / 安全和生产采用仍需对应 owner 或独立 reviewer。

## 验证命令

- `python3 scripts/check_all.py --only public-repository-content`
- `python3 scripts/check_all.py --only research-capability`
- `python3 scripts/check_research_capability.py --case scripts/fixtures/research-capability/positive-r3-trial.v1.json`
- `python3 scripts/check_all.py --only skill-maturity,transferable-skill-baseline,documentation-maintenance,implementation-template-system,acknowledge-topic-adoption,public-repository-content`
- `python3 scripts/check_all.py`
- `git diff --check`

## 上游 Handback 边界

```yaml
acknowledge_topic_update_required: true
upstream_write_authorization: false
design-owner: existing
system-layer_delta: wiki research profile moved from medium to strong-template-kernel with executable contract fixtures
local_conformance: targeted and full local quality gates passed; commit readback is reported at closeout
forbidden: source domain content, project facts, historical cases, source paths, runtime records
cannot_promote: local green does not mean upstream conformance updated or external research outcome passed
recovery_condition: explicit authorization to update the upstream conformance owner
```

## Persistence Decision

`artifact-needed`：owner 为 [[skills/research-capability/SKILL]]、[[research-capability-rules]]、现有 research templates 和本地 validator；本报告记录验证与上游 handback，不成为第二套 Research OS 正文。
