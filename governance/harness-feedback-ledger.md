---
type: governance-ledger
id: GOV-HARNESS-FEEDBACK-LEDGER-001
scope: shared
status: active
source_of_truth: true
updated: 2026-05-28
tags: [agent, harness, feedback, episode]
---

# Harness Feedback Ledger

这页记录当前 wiki 模板级 Harness 的 episode 数据、sensor backlog 和规则晋升队列。判断规则见 [[harness-evolution]]，执行路由见 [[response-mode-routing]]。

## 记录规则

- 只记录能反哺 Harness 的结构性信号，不记录普通项目流水。
- 用户纠偏优先记录原始纠偏点，再记录 agent 侧改动。
- 一条 episode 可以先是 `observed`，等有 sensor、模板或规则承接后再改为 `promoted`。
- 不能因为写入 ledger 就自动升级 [[AGENTS]]、[[POLICY]] 或关闭任何项目事项。

## Episode Ledger

| 日期 | Episode | 触发信号 | 响应模式 | 成本类型 | 已采取改动 | Sensor / Artifact | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-28 | wiki 独立治理 sensor 拆分 | 跨 `wiki`、`DocCustomeranalysis`、`DocFilmCommunity` 对比后发现 wiki 作为模板级 Harness 已有规则页，但 H5 ledger、指令遵循和入口结构检查仍集中在 `check_harness_governance.py`，缺少可单独运行的工作阶段 sensor | 规则升级 | 可优化成本 | 新增 `scripts/check_harness_feedback_ledger.py`、`scripts/check_instruction_adherence.py`、`scripts/check_project_docs.py`，接入 `scripts/check_all.py --list` 和 `.codex/AGENTS.md` 工作阶段检查；同步 [[instruction-adherence]]、[[harness-evolution]] 和本 ledger | `python3 scripts/check_all.py --only harness-feedback-ledger,instruction-adherence,project-docs` | active |
| 2026-05-28 | 主动对话和性能预算升级 | 用户要求把 wiki 智能体系统升级得更前沿、更智能，同时注意性能 | 规则升级 | 可优化成本 | 新增 [[proactive-dialogue-system]]、[[templates/guided-discovery-session-template]]，把场景自动判定、无感交流等级、每轮产物化和读取 / 问题 / 检查 / 产物大小预算写入 Harness | `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-05-26 | DocCustomeranalysis 测试成熟度与口径漂移反哺 | 用户要求吸收同定位工程最近完善的 harness 设计、测试环节规则和口径漂移治理 | 规则升级 | 可优化成本 | 新增 [[instruction-adherence]]、[[execution-contract-semantics]]、[[concepts/software-testing-acceptance-release]]、测试计划 / AP 层和对应 sensors | `python3 scripts/check_all.py --only testing-system-maturity,execution-contract-semantics,harness-governance` | promoted |
| 2026-05-25 | Codex Goals 转主控 / 子工程契约 | 用户要求基于 Goals 专题给出主控和子工程升级建议并落实 | 规则升级 | 可优化成本 | 新增 Goal Contract 模板，并把完成契约字段写入 Harness 接入、编码任务、回传包和 episode 模板 | [[templates/goal-contract-template]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-05-25 | 研发事项入口顺序和结构化 sensor | 用户指出规则分布虽清楚但维护者需要知道入口顺序，且 `work-item-matrix` 关键词检查未来可能脆弱 | 规则升级 | 可优化成本 | 在研发总控页新增维护者入口顺序；把 `work-item-matrix` 从关键词检查升级为文件、章节、表头、模板字段和入口链接结构检查 | [[projects/development/plan/README]] / `python3 scripts/check_all.py --only work-item-matrix` | promoted |
| 2026-05-25 | 响应效率治理入口 | 简单诊断容易直接进入完整治理闭环 | 规则升级 | 可优化成本 | 新增 [[response-mode-routing]]，拆分快速诊断、沉淀、验收、规则升级和子工程回传 | [[templates/harness-adoption-template]] | promoted |
| 2026-05-25 | DocCustomeranalysis Harness 反哺 | 用户指出同定位工程的 harness 设计和系统流程更健全 | 规则升级 | 可优化成本 | 新增 [[harness-evolution]]、本 ledger、episode / evolution 模板、`.codex/AGENTS.md` 和统一检查脚本 | `python3 scripts/check_all.py --only harness-governance` | promoted |

## Sensor Backlog

| 候选项 | 触发来源 | 拟补 sensor / 模板 | 当前状态 |
| --- | --- | --- | --- |
| H5 ledger 独立 sensor | wiki 独立治理 sensor 拆分 | `scripts/check_harness_feedback_ledger.py` 检查四张表、状态词表、active episode、sensor backlog 和 promotion 来源回链 | active |
| 指令遵循独立 sensor | wiki 独立治理 sensor 拆分 | `scripts/check_instruction_adherence.py` 检查 [[instruction-adherence]]、ledger、`.codex/AGENTS.md` 和 `scripts/check_all.py` 的执行覆盖接线 | active |
| Markdown / wikilink / frontmatter 检查 | 多入口文档库容易出现链接和元数据漂移 | `scripts/check_project_docs.py` 检查入口页、治理 frontmatter 和本地 wikilink | active |
| 技能质量检查 | 技能页可能复制项目事实或缺少触发 / 输出边界 | 后续可补技能结构检查 | observed |
| 模板完整性检查 | 新增模板后可能忘记挂入口或字段漂移 | 当前由 `check_harness_governance.py` 覆盖 Harness 模板入口 | active |
| 研发事项结构检查 | 关键词式 wiring 检查可能随着字段增加变脆 | 当前由 `check_work_item_matrix.py` 检查矩阵列顺序、模板字段、章节、表头和入口链接 | active |
| 测试成熟度检查 | 测试计划、AP、报告、fixture / oracle 和发布 runbook 容易漂移 | 当前由 `check_testing_system_maturity.py` 覆盖入口、模板字段和 AP 基本结构 | active |
| 执行合同语义检查 | 非目标、上层规则或证据说明容易漂移成隐形待办 | 当前由 `check_execution_contract_semantics.py` 覆盖入口 wiring 和可见污染模式 | active |
| 主动对话产物化检查 | 引导式设计容易只停在聊天，或为了智能化扩大读取和结构成本 | 当前由 `check_harness_governance.py` 检查 [[proactive-dialogue-system]]、[[templates/guided-discovery-session-template]]、性能预算和入口 wiring | active |
| 规则降级 / 删除提醒 | 自然语言规则可能继续膨胀 | 周期复盘时用 [[templates/harness-evolution-review-template]] 标记 stale / noisy 规则 | observed |

## Rule Promotion Queue

| 候选规则 | 来自 episode | 晋升目标 | 状态 |
| --- | --- | --- | --- |
| 模板级 H5 不能只靠聚合式 harness 检查；ledger、instruction-adherence 和入口结构应可按工作阶段独立运行 | wiki 独立治理 sensor 拆分 | `scripts/check_harness_feedback_ledger.py` / `scripts/check_instruction_adherence.py` / `scripts/check_project_docs.py` / `scripts/check_all.py --list` | active |
| 长时任务先写 Goal Contract，主控定义完成契约，子工程回传证据 | Codex Goals 转主控 / 子工程契约 | [[response-mode-routing]] / [[WORKFLOW]] / [[templates/goal-contract-template]] | promoted |
| 工作阶段跑专项 sensor，收尾和提交前跑完整门禁 | DocCustomeranalysis Harness 反哺 | [[harness-evolution]] / `scripts/check_all.py` | promoted |
| H5 episode 不直接晋升硬规则，先进入 ledger 和复盘 | DocCustomeranalysis Harness 反哺 | [[harness-evolution]] | promoted |
| 规则不能只停在自然语言，重复失守要升级为模板字段、sensor、技能或最终证明 | DocCustomeranalysis Harness 反哺 | [[response-mode-routing]] / [[WORKFLOW]] / `scripts/check_harness_governance.py` | active |
| 已有规则执行失守先进入触发矩阵、模板字段、sensor、门禁或最终证明 | DocCustomeranalysis 测试成熟度与口径漂移反哺 | [[instruction-adherence]] / `scripts/check_harness_governance.py` | promoted |
| 执行合同必须单值，非目标、参考规则和上层证据不能漂成隐形待办 | DocCustomeranalysis 测试成熟度与口径漂移反哺 | [[execution-contract-semantics]] / `scripts/check_execution_contract_semantics.py` | promoted |
| 测试报告必须引用事项页计划或 AP，环境按证据面路由而不是阶梯上推 | DocCustomeranalysis 测试成熟度与口径漂移反哺 | [[projects/development/plan/test-acceptance-planning-model]] / `scripts/check_testing_system_maturity.py` | promoted |
| 研发事项日常维护先走总控页入口顺序，治理层只在改变默认规则时修改 | 研发事项入口顺序和结构化 sensor | [[projects/development/plan/README]] / [[WORKFLOW]] | promoted |
| 主动对话先自动判定场景包和置信度，再用少量问题、明确假设和性能预算推进产物化 | 主动对话和性能预算升级 | [[proactive-dialogue-system]] / [[templates/guided-discovery-session-template]] / `scripts/check_harness_governance.py` | promoted |

## Rule Prune Queue

| 候选清理 | 原因 | 当前状态 |
| --- | --- | --- |
| `check_harness_governance.py` 承担所有细节检查 | 已拆出 ledger、instruction-adherence 和 project-docs 专项 sensor，聚合检查后续只保留 wiring / 模板 / Harness 主干 | active |
| 多处手写检查脚本清单 | 已由 `scripts/check_all.py --list` 和 `--only` 承接 | observed |
| 已被 sensor 覆盖的重复自然语言规则 | 避免入口页继续膨胀 | observed |
| `work-item-matrix` 旧关键词堆叠 | 已改为结构化检查，后续优先补字段 / 表头 / 章节断言 | promoted |
