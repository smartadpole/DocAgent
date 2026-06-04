---
type: governance-ledger
id: GOV-HARNESS-FEEDBACK-LEDGER-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-04
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
| 2026-06-04 | 跨工程迁移 meta-skill 过度模式化 | 用户指出“通用提示词、定制提示词、直接执行迁移、元技能维护这些都不要，只要一个通用提示词”，暴露前次修复把 meta-skill 变成多模式路由器，仍偏离了单一产物目标 | 技能升级 + Harness 反馈 | 可优化成本 | 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，把定位收敛为只生成通用迁移提示词，移除定制、直接执行和元技能维护模式；更新 `scripts/check_harness_governance.py`，改查唯一通用产物关键词 | [[skills/cross-project-skill-adoption-prompt/SKILL]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-06-04 | 新增知识关联依赖人工补链 | 用户追问新增知识是否自动和已有知识库形成网状关联，随后追问是否已落实成别人可学习使用的技能、是否完成调研沉淀，暴露当前流程需要从规则 / sensor 继续补到调研卡片和可复用 skill | 规则升级 + 技能升级 + Harness 反馈 | 可优化成本 | 新增 [[knowledge-linking-rules]]、[[skills/knowledge-linking/SKILL]] 和 [[articles/2026-06-04-knowledge-linking-mechanism-research]]，更新 [[WORKFLOW]]、[[POLICY]]、入口页和概念 / 文章模板；新增 `scripts/check_knowledge_linking.py` 并接入 `scripts/check_all.py --only knowledge-linking`，检查 `concepts/`、`articles/` 的出链、非 log 入链和入口 / 知识页回链 | [[knowledge-linking-rules]] / [[skills/knowledge-linking/SKILL]] / [[articles/2026-06-04-knowledge-linking-mechanism-research]] / `python3 scripts/check_all.py --only knowledge-linking` | promoted |
| 2026-06-04 | Meta-skill 维护请求被降级成单次生成 | 用户明确指出“不是单次生成，是重启 goal，修改 meta skill”，说明前一轮虽然升级了比较门，但最终回复仍把注意力滑回通用成稿，没有把 meta-skill 维护作为主交付 | 技能升级 + Goal Contract + Harness 反馈 | 可优化成本 | 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，新增元技能维护模式、任务模式四选一、维护请求优先路由和禁止用单次提示词替代文件修改 / sensor / ledger / log / commit；扩展 `scripts/check_harness_governance.py` 检查元技能维护关键词 | [[skills/cross-project-skill-adoption-prompt/SKILL]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-06-04 | 跨工程迁移提示词缺少示例基准比较 | 用户要求设置目标并升级 meta-skill，直到依据它生成的复盘迁移提示词比用户给出的示例更优秀，暴露现有 meta-skill 没有把用户示例转成可验证 baseline rubric | 技能升级 + Goal Contract + Harness 反馈 | 可优化成本 | 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，新增 Baseline 对比评分和 `generated >= baseline` 输出前裁决；更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，新增优于示例的判定标准；扩展 `scripts/check_harness_governance.py` 检查 baseline / 优于示例关键词 | [[skills/cross-project-skill-adoption-prompt/SKILL]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-06-04 | 跨工程迁移提示词通用模式污染 | 用户要求直接做通用提示词、不要特定工程定制，并指出越改越差，暴露 meta-skill 仍会被历史上下文里的目标工程名带偏，把通用任务书和定制落位混写 | 技能升级 + Harness 反馈 | 可优化成本 | 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，新增输出模式三选一、最新指令优先、通用版锁定、Golden Baseline 补丁原则和模式污染防线；更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，补通用版生成规则；扩展 `scripts/check_harness_governance.py` 检查通用版和 Golden Baseline 关键词 | [[skills/cross-project-skill-adoption-prompt/SKILL]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-06-03 | 跨工程迁移提示词任务书形态缺口 | 用户继续追问 meta-skill 已升级后为什么生成稿仍弱于手写版，暴露上次只修了覆盖矩阵，未强制最终提示词保留目标 agent 可逐项执行的任务书主干 | 技能升级 + Harness 反馈 | 可优化成本 | 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，新增任务书优先和对照样稿质量门；更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，补复盘迁移推荐提示词骨架；扩展 `scripts/check_harness_governance.py` 检查任务书形态关键词 | [[skills/cross-project-skill-adoption-prompt/SKILL]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-06-03 | 跨工程迁移提示词覆盖度不足 | 用户对比两段复盘体系迁移提示词后指出，第一段提示词弱于手写版本，暴露 meta-skill 只要求资料路径和结构自检，但没有强制源能力模块覆盖和目标工程差异化说明 | 技能升级 + Harness 反馈 | 可优化成本 | 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，补源能力覆盖矩阵、复合能力压缩防线和定制提示词差异化说明；更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，把复盘体系迁移最小模块清单写入源资料 | [[skills/cross-project-skill-adoption-prompt/SKILL]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-05-30 | 硬性治理过度和 log 提交税 | 用户追问当前 agent 治理方案是否合理，指出入口过度缩减可能伤能力、`log` 设置硬性条目不合理，并要求检查其他设计是否也有类似问题 | 规则升级 | 可优化成本 | 新增 [[agent-governance-strategy]]，把治理动作分成 P0 硬约束、P1 语义门、P2 流程和 P3 backlog；同步 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[instruction-adherence]]、[[log-writing-rules]]，把 `[[log]]`、产物化、完整检查和二阶反思改成资格判断 | [[agent-governance-strategy]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-05-29 | Finalizer 写入范围证明缺口 | 用户指出 agent 在被要求“只提交相关内容”后，仍沿事项归属链继续同步 EP / FP / status / log，finalizer 只证明外部残留被明示，不能证明主控内部写入范围符合最新收窄指令 | 知识沉淀 + Agent 工作复盘 | 可优化成本 | 新增 [[articles/2026-05-29-finalizer-write-scope-case]]，把问题归类为 Scope Lock / Scope Proof 缺口；本页补 sensor backlog 和晋升候选 | [[articles/2026-05-29-finalizer-write-scope-case]] | observed |
| 2026-05-28 | Agent 治理专题落位纠偏 | 用户指出“这不是项目开发，属于知识库”，纠正 agent 将专题误放入 `projects/design/topics/` 和 `projects/trace` 的路由错误 | 知识沉淀 | 可优化成本 | 撤回项目开发链路改动，改为新增 [[concepts/agent-governance]]，并从 [[concepts/README]]、[[INDEX]] 和治理入口回链 | [[concepts/agent-governance]] | observed |
| 2026-05-28 | 模板落位二分纠偏 | 用户指出不是一说模板就沉淀到 `templates/`，要区分知识库模板和系统治理模板 | 规则升级 | 可优化成本 | 更新 [[template-feedback-rules]]、[[AGENTS]]、`.codex/AGENTS.md`、[[WORKFLOW]]、[[POLICY]]、[[templates/README]] 和入口说明，明确知识库模板进专题成果，系统治理模板才进 `templates/` | [[template-feedback-rules]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-05-28 | 主动对话和性能预算升级 | 用户要求把 wiki 智能体系统升级得更前沿、更智能，同时注意性能 | 规则升级 | 可优化成本 | 新增 [[proactive-dialogue-system]]、[[templates/guided-discovery-session-template]]，把场景自动判定、无感交流等级、每轮产物化和读取 / 问题 / 检查 / 产物大小预算写入 Harness | `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-05-26 | DocCustomeranalysis 测试成熟度与口径漂移反哺 | 用户要求吸收同定位工程最近完善的 harness 设计、测试环节规则和口径漂移治理 | 规则升级 | 可优化成本 | 新增 [[instruction-adherence]]、[[execution-contract-semantics]]、[[concepts/software-testing-acceptance-release]]、测试计划 / AP 层和对应 sensors | `python3 scripts/check_all.py --only testing-system-maturity,execution-contract-semantics,harness-governance` | promoted |
| 2026-05-25 | Codex Goals 转主控 / 子工程契约 | 用户要求基于 Goals 专题给出主控和子工程升级建议并落实 | 规则升级 | 可优化成本 | 新增 Goal Contract 模板，并把完成契约字段写入 Harness 接入、编码任务、回传包和 episode 模板 | [[templates/goal-contract-template]] / `python3 scripts/check_all.py --only harness-governance` | promoted |
| 2026-05-25 | 研发事项入口顺序和结构化 sensor | 用户指出规则分布虽清楚但维护者需要知道入口顺序，且 `work-item-matrix` 关键词检查未来可能脆弱 | 规则升级 | 可优化成本 | 在研发总控页新增维护者入口顺序；把 `work-item-matrix` 从关键词检查升级为文件、章节、表头、模板字段和入口链接结构检查 | [[projects/development/plan/README]] / `python3 scripts/check_all.py --only work-item-matrix` | promoted |
| 2026-05-25 | 响应效率治理入口 | 简单诊断容易直接进入完整治理闭环 | 规则升级 | 可优化成本 | 新增 [[response-mode-routing]]，拆分快速诊断、沉淀、验收、规则升级和子工程回传 | [[templates/harness-adoption-template]] | promoted |
| 2026-05-25 | DocCustomeranalysis Harness 反哺 | 用户指出同定位工程的 harness 设计和系统流程更健全 | 规则升级 | 可优化成本 | 新增 [[harness-evolution]]、本 ledger、episode / evolution 模板、`.codex/AGENTS.md` 和统一检查脚本 | `python3 scripts/check_all.py --only harness-governance` | promoted |

## Sensor Backlog

| 候选项 | 触发来源 | 拟补 sensor / 模板 | 当前状态 |
| --- | --- | --- | --- |
| Markdown / wikilink / frontmatter 检查 | 多入口文档库容易出现链接和元数据漂移 | 后续可补 `scripts/check_project_docs.py` 或扩展 `check_harness_governance.py` | observed |
| 技能质量检查 | 技能页可能复制项目事实或缺少触发 / 输出边界 | 后续可补技能结构检查 | observed |
| 模板完整性检查 | 新增模板后可能忘记挂入口或字段漂移 | 当前由 `check_harness_governance.py` 覆盖 Harness 模板入口 | active |
| 研发事项结构检查 | 关键词式 wiring 检查可能随着字段增加变脆 | 当前由 `check_work_item_matrix.py` 检查矩阵列顺序、模板字段、章节、表头和入口链接 | active |
| 测试成熟度检查 | 测试计划、AP、报告、fixture / oracle 和发布 runbook 容易漂移 | 当前由 `check_testing_system_maturity.py` 覆盖入口、模板字段和 AP 基本结构 | active |
| 执行合同语义检查 | 非目标、上层规则或证据说明容易漂移成隐形待办 | 当前由 `check_execution_contract_semantics.py` 覆盖入口 wiring 和可见污染模式 | active |
| 主动对话产物化检查 | 引导式设计容易只停在聊天，或为了智能化扩大读取和结构成本 | 当前由 `check_harness_governance.py` 检查 [[proactive-dialogue-system]]、[[templates/guided-discovery-session-template]]、性能预算和入口 wiring | active |
| 治理策略分级检查 | `[[log]]`、产物化、完整检查、二阶反思、Goal Contract 或模板反哺容易被硬化成无条件仪式 | 当前由 `check_harness_governance.py` 检查 [[agent-governance-strategy]]、log eligibility 和入口 wiring | active |
| 知识关联检查 | 新增 `articles/` 或 `concepts/` 页面可能只靠最终回复或 `[[log]]` 被发现，缺少上位概念、邻接页面或入口回链 | 当前由 `scripts/check_knowledge_linking.py` 检查出链、非 log 入链和入口 / 知识页回链，并通过 `python3 scripts/check_all.py --only knowledge-linking` 运行 | active |
| 写入范围证明 / Scope Proof | 用户即时收窄写入范围后，finalizer 可能只证明 working tree clean 或 external residual 明示，无法证明本轮 diff 仍在允许范围内 | 后续可补 finalizer scope manifest 或 `--allowed-path` 检查：比较本轮 diff / latest commit 文件与用户最新写入白名单 | observed |
| 跨工程迁移提示词覆盖度检查 | 复合能力迁移提示词可能压缩掉源资料中的方法、档案、模板、skill、行动分流、治理自演进或验证要求 | 后续可补技能迁移 manifest 字段检查，确认 `TRANSFER.md` 和 meta-skill 输出结构都含覆盖矩阵 / 最小模块清单 | observed |
| 跨工程迁移提示词任务书形态检查 | 复合能力迁移提示词可能覆盖了资料路径和边界，但最终文本仍不像目标工程 agent 可执行的任务书 | 当前由 `check_harness_governance.py` 检查 cross-project meta-skill 和 retrospective transfer 中的任务书优先、对照样稿、推荐提示词骨架和最终交付要求 | active |
| 跨工程迁移提示词通用产物检查 | 通用迁移提示词可能被历史上下文中的目标工程名污染，混入具体工程小节、具体路径读取清单或仓库级落位建议，或被扩成定制 / 执行 / 元技能维护多模式 | 当前由 `check_harness_governance.py` 检查 meta-skill 的唯一通用产物、Golden Baseline 补丁原则和 retrospective transfer 的通用版生成规则 | active |
| 跨工程迁移提示词示例基准检查 | 用户提供强示例后，生成稿可能没有先完整覆盖示例就开始重写，导致越改越弱 | 当前由 `check_harness_governance.py` 检查 meta-skill 的 Baseline 对比评分、`generated >= baseline` 裁决和 retrospective transfer 的优于示例判定标准 | active |
| 规则降级 / 删除提醒 | 自然语言规则可能继续膨胀 | 周期复盘时用 [[templates/harness-evolution-review-template]] 标记 stale / noisy 规则 | observed |

## Rule Promotion Queue

| 候选规则 | 来自 episode | 晋升目标 | 状态 |
| --- | --- | --- | --- |
| 长时任务先写 Goal Contract，主控定义完成契约，子工程回传证据 | Codex Goals 转主控 / 子工程契约 | [[response-mode-routing]] / [[WORKFLOW]] / [[templates/goal-contract-template]] | promoted |
| 工作阶段跑专项 sensor，收尾和提交前跑完整门禁 | DocCustomeranalysis Harness 反哺 | [[harness-evolution]] / `scripts/check_all.py` | promoted |
| H5 episode 不直接晋升硬规则，先进入 ledger 和复盘 | DocCustomeranalysis Harness 反哺 | [[harness-evolution]] | promoted |
| 规则不能只停在自然语言，重复失守要升级为模板字段、sensor、技能或最终证明 | DocCustomeranalysis Harness 反哺 | [[response-mode-routing]] / [[WORKFLOW]] / `scripts/check_harness_governance.py` | active |
| 已有规则执行失守先进入触发矩阵、模板字段、sensor、门禁或最终证明 | DocCustomeranalysis 测试成熟度与口径漂移反哺 | [[instruction-adherence]] / `scripts/check_harness_governance.py` | promoted |
| 执行合同必须单值，非目标、参考规则和上层证据不能漂成隐形待办 | DocCustomeranalysis 测试成熟度与口径漂移反哺 | [[execution-contract-semantics]] / `scripts/check_execution_contract_semantics.py` | promoted |
| 测试报告必须引用事项页计划或 AP，环境按证据面路由而不是阶梯上推 | DocCustomeranalysis 测试成熟度与口径漂移反哺 | [[projects/development/plan/test-acceptance-planning-model]] / `scripts/check_testing_system_maturity.py` | promoted |
| 研发事项日常维护先走总控页入口顺序，治理层只在改变默认规则时修改 | 研发事项入口顺序和结构化 sensor | [[projects/development/plan/README]] / [[WORKFLOW]] | promoted |
| 主动对话先自动判定场景包和置信度，再用少量问题、明确假设和性能预算推进产物化 | 主动对话和性能预算升级 | [[proactive-dialogue-system]] / [[templates/guided-discovery-session-template]] / `scripts/check_harness_governance.py` | promoted |
| 防漏规则先做 P0 / P1 / P2 / P3 分级；`[[log]]`、产物化、完整检查和二阶反思先判资格，不默认变成每轮仪式 | 硬性治理过度和 log 提交税 | [[agent-governance-strategy]] / [[log-writing-rules]] / [[instruction-adherence]] / `scripts/check_harness_governance.py` | promoted |
| 提到模板时先区分知识库模板和系统治理模板，专题成果不自动进入 `templates/` | 模板落位二分纠偏 | [[template-feedback-rules]] / [[AGENTS]] / `.codex/AGENTS.md` / [[POLICY]] / [[WORKFLOW]] / [[templates/README]] | promoted |
| 用户收窄写入范围后，收尾必须证明 scope，而不只是证明 clean | Finalizer 写入范围证明缺口 | finalizer scope manifest / [[instruction-adherence]] / [[response-mode-routing]] | active |

## Rule Prune Queue

| 候选清理 | 原因 | 当前状态 |
| --- | --- | --- |
| 多处手写检查脚本清单 | 已由 `scripts/check_all.py --list` 和 `--only` 承接 | observed |
| 已被 sensor 覆盖的重复自然语言规则 | 避免入口页继续膨胀 | observed |
| 被 log eligibility 覆盖的“所有文件变更都必须写 log”旧表述 | 已收窄为必做资格判断，不再作为每轮硬性条目 | promoted |
| `work-item-matrix` 旧关键词堆叠 | 已改为结构化检查，后续优先补字段 / 表头 / 章节断言 | promoted |
