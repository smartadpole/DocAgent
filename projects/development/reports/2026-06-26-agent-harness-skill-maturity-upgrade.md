---
type: test_report
id: REPORT-2026-06-26-AGENT-HARNESS-SKILL-MATURITY
status: passed
updated: 2026-06-26
tags: [agent-harness, skill-maturity, loop-engineering, research-capability]
---

# Agent Harness 和技能成熟度升级验收报告

## 验证对象

- 对象类型：agent / harness / memory / skill / template / sensor / report 体系升级。
- 目标：让 wiki 在跨工程技能成熟度矩阵中进入前列，同时保持 wiki 作为研究资产、知识治理、图文呈现、公开发布和 agent 运行合同知识库的设计定位。
- 不做项：不硬升 project-context-entry、work-item-auto-decomposition、customer-group-db-readback、backlog-management、lifeos-management；performance-bandwidth-analysis 只抽象方法，不新建空 skill。
- 证据边界：本报告证明本地结构、sensor 和外部矩阵复核；不证明真实公网 live readback、业务 runtime validation、生产发布或人工视觉最终拍板。

## Goal Contract

- Objective：升级 wiki 的 whole Agent Harness System，而不是只升级 `skills/`。
- Expected final state：核心可迁移能力不再停留在 partial / none；至少 5 项达到 mature / leader；通用 / 可迁移总分达到主控阈值；本地专项 sensor 和完整检查通过。
- Acceptance criteria：research-capability、cross-project-governance-audit、problem-focused-visual-presentation、goal-contract、loop-engineering、issue-analysis、documentation-maintenance、public-html-publish 均达到 adopted / mature / leader，且 score_gap <= 5。
- Evidence layers：local validation、sensor、git preflight、external matrix refresh、diff readback。
- Closure boundary：矩阵分数、Worker 自述、check_all 通过都不能单独关闭目标；必须同时满足 wiki 设计一致性和不硬升项目绑定技能。

## Loop Contract

| Field | Value |
| --- | --- |
| Discovery source | 用户目标、AcknowledgeBase `agent-evidence-v12` 矩阵、wiki 本地 sensor、主控 evaluator 回传 |
| Run queue | Phase 1A research checker -> Goal / Loop / Run Capsule -> cross-project audit -> visual / public / issue / docs -> final validation |
| Worker topology | wiki implementation thread + 主控 evaluator；后续由主控接管最小补丁并独立验收 |
| Evaluator oracle | 本地 `check_all` 专项、完整 `check_all`、`git diff --check`、外部矩阵刷新 |
| Persistence routing | 技能 / 模板 / sensor 改动进入对应 owner；执行证据进入本报告；主题记录进入 `log.md`；一次性矩阵分数不进入 memory |
| Next-run decision | stop after commit；公网 live readback 和真实业务 runtime validation 另案触发 |
| Stop / blocked conditions | dirty `.obsidian/` 不纳入提交；AcknowledgeBase 生成文件不纳入 wiki 提交；缺公网条件不得写公开已验证 |

## Whole Agent Harness System Coverage

| Layer | Files touched / reviewed | Upgrade decision | Evidence | Remaining boundary |
| --- | --- | --- | --- | --- |
| Agent entry | `AGENTS.md` reviewed by existing checks | no structural rewrite | `harness-governance` OK | no new agent entry rule needed |
| Harness governance | `governance/agent-governance-strategy.md` | upgraded cross-audit guard | cross-project audit sensor OK | no runtime validation |
| Memory / persistence | `skills/README.md`, this report, `log.md` | execution evidence goes to report/log, stable facts only to memory | report and log written | no one-off score in memory |
| Goal / Loop / Run Capsule | `skills/goal-contract`, `skills/loop-engineering`, templates | matured contract fields | loop/skill checks OK | actual task closure still evaluator-owned |
| Skills | research, cross-audit, issue, visual, public | upgraded core transferable skills | matrix core rows adopted/mature/leader | project-bound skills rejected/adapted only |
| Templates | research intake, goal, loop, run capsule, visual, public, cross-audit | added reusable contract fields | skill-maturity OK | templates are scaffolds, not facts |
| Sensors / checks | research, cross-audit, L5, check_all | added/used field checks | all required sensors OK | sensors prove wiring, not runtime |
| Views / public publish | visual/public skills and templates | preserved sample/readback boundaries | visual leader, public mature | live public readback not rerun here |
| Reports / log / trace | this report, `log.md` | execution proof and history captured | report/log updated | no project trace change required |

## Matrix Refresh Result

External matrix refresh was run from AcknowledgeBase generated outputs for readback only. The generated AcknowledgeBase files are not part of this wiki change.

| Core skill | Matrix status | Score | Gap | Boundary |
| --- | ---: | ---: | ---: | --- |
| research-capability | leader | 46/49 | 3 | decision asset contract now detected |
| cross-project-governance-audit | leader | 55/55 | 0 | file/sensor audit, no runtime validation |
| problem-focused-visual-presentation | leader | 52/52 | 0 | visual sample/sensor, no new human design approval |
| goal-contract | mature | 60/63 | 3 | contract proof, not task completion by itself |
| loop-engineering | mature | 50/52 | 2 | control-plane proof, not unattended automation |
| issue-analysis | leader | 41/41 | 0 | issue method proof, not closing a real issue |
| documentation-maintenance | mature | 55/56 | 1 | docs wiring proof |
| public-html-publish | mature | 57/61 | 4 | static/profile proof; live readback still separate |

Summary for Software/wiki: leader 4, mature 5, adopted 3, partial 1, none 5; general / transferable score 597/614.

## Validation Commands

- `python3 scripts/check_all.py --only research-capability,skill-maturity,loop-engineering,problem-focused-visual-presentation,public-html-publish,documentation-maintenance,harness-governance`：passed
- `python3 scripts/check_all.py --only agent-harness-l5,cross-project-governance-audit`：passed
- `python3 scripts/check_all.py --only cross-project-governance-audit`：passed
- `git diff --check`：passed
- External matrix refresh：passed for readback; generated AcknowledgeBase outputs are excluded from wiki commit.

## Unverified Boundaries

- Public HTML live readback was not rerun as a live/public claim in this report.
- No production service, business runtime, or end-to-end user workflow was exercised.
- Visual presentation reached matrix / static QA proof; independent human design approval remains manual-confirmation when required.
- Project-bound skills remain rejected / adapted by design and should not be upgraded for score alone.
