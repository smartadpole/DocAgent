---
type: governance-ledger
id: GOV-HARNESS-FEEDBACK-LEDGER-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-25
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
| 2026-07-23 | 融合入口新任务烟测通过 | 新任务 `019f8e86-943e-74e1-9c67-0bca7d4ca92a` 首轮“你好”经 `read_thread` 读回完整 final answer，包含首段协作维护者定位、`可以从这几个方向开始：`、`1.` 到 `4.` 编号方向和 `推荐第一步：这轮想解决什么`；`wait_threads` 摘要会压平 Markdown，不作为格式判定源 | 验收关闭 | 必要成本 | 将测试线程命名为 `wiki fused greeting smoke test passed`；把 readback 作为最终验证证据，确认首次接触和常规引导融合入口通过 | `codex_app.create_thread` / `codex_app.read_thread` / `python3 scripts/check_all.py` | promoted |
| 2026-07-23 | 融合入口编号列表被压缩 | 新任务 `019f8e84-3a98-7ab3-b1b8-1c153a413e9b` 首轮“你好”保留了首段和推荐语，但把 4 个方向压缩成无编号一行，未稳定保留用户认可的常规引导形态 | 规则升级 | 可优化成本 | 将 P0 骨架从“默认直接使用”升级为“唯一合格回复”；要求逐字接近输出、保留换行、`1.` 到 `4.` 编号、`可以从这几个方向开始：` 和 `推荐第一步：`；sensor 增加 4 条编号 literal | `codex_app.create_thread` / [[AGENTS]] / `python3 scripts/check_all.py --only harness-governance` | active |
| 2026-07-23 | 融合入口骨架被压缩 | 新任务 `019f8e81-f6ca-7cd1-9a8e-8175d74390cb` 首轮“你好”虽然输出协作维护者和四个方向，但把推荐第一步提前、压缩编号列表，未稳定保留用户认可的融合入口形态 | 规则升级 | 可优化成本 | 将完整融合入口骨架上提到根 AGENTS P0 冷启动规则，要求默认直接使用并保留段落顺序、编号列表、`可以从这几个方向开始：` 和 `推荐第一步：` 两个锚点；sensor 增加锚点检查 | `codex_app.create_thread` / [[AGENTS]] / `python3 scripts/check_all.py --only harness-governance` | active |
| 2026-07-23 | 首次接触和常规引导不应割裂 | 用户指出首次接触和常规引导应该在一起，并给出“wiki / 软件工程知识库的协作维护者 + 四个常规方向 + 这轮想解决什么”的目标口径 | 规则升级 | 可优化成本 | 将 P0 冷启动从“四标签逐项输出”改为“首次接触 + 常规引导融合入口”；四项设定可在首段自然覆盖，随后给常规方向和推荐第一步；sensor 改查融合入口、常规引导、协作维护者和“这轮想解决什么” | `python3 scripts/check_all.py --only harness-governance` / [[proactive-dialogue-system]] | active |
| 2026-07-23 | 首次接触与常规引导新任务烟测通过 | 用户要求设置 Goal 并由 agent 自己开新对话测试，直到拿到首次引导和常规引导 | 验收关闭 | 必要成本 | 创建新 Codex 任务 `019f8e75-7479-7292-88e9-cab93543d709`；首轮只发“你好”，返回可见 `系统角色 / 用户目标 / 协作方式 / 第一步成果` 四项；第二轮明确进入项目运行层，返回入口、项目主控、Gate / FP / EP / TASK、风险、证据和下一步决策的常规引导 | `codex_app.create_thread` / `codex_app.wait_threads` / `python3 scripts/check_all.py` | promoted |
| 2026-07-23 | 首次接触四项设定未显式输出 | 截图显示 agent 对“你好”仍只给出“协作维护者”定位和梳理状态、写规则、实现、验收、收尾、提交等使用过程菜单，没有在可见正文中逐项输出系统角色、用户目标、协作方式和第一步成果 | 规则升级 | 可优化成本 | 将首次接触升级为根 AGENTS 顶部 P0 冷启动规则，要求四个标签必须逐项可见输出；禁止把状态梳理、写规则、实现、验收、收尾、提交作为首次接触默认方向；sensor 增加 P0 和逐项输出检查词 | `python3 scripts/check_all.py --only harness-governance` / [[AGENTS]] / [[proactive-dialogue-system]] | active |
| 2026-07-23 | 首次接触 onboarding 被实现为运行菜单 | 截图显示新对话对“你好”已部分规避 Git / TASK 等术语，但仍推荐“检查当前项目状态”“下达实现或收尾指令”，没有显式设定系统角色、用户目标、协作方式和第一步成果 | 规则升级 | 可优化成本 | 在首次接触最低回复中增加可复用参考回复骨架，并禁止把检查当前项目状态、实现或收尾指令作为首次接触默认方向；sensor 检查这些 guard 词 | `python3 scripts/check_all.py --only harness-governance` / [[proactive-dialogue-system]] | active |
| 2026-07-23 | 首次接触与使用过程引导串层 | 截图显示 agent 对“你好”输出路径、分支、dirty、projects/README、TASK / EP / Gate 和收尾等使用过程信息，没有突出首次接触 onboarding | 规则升级 | 可优化成本 | 将首次问候入口重命名并拆分为“首次接触 onboarding”和“使用过程项目引导”；首次接触禁止主动暴露运行层信息，sensor 检查 onboarding 四要素和禁用术语 | `python3 scripts/check_all.py --only harness-governance` / [[proactive-dialogue-system]] | active |
| 2026-07-23 | 首次问候为了定位身份触发读文件和命令 | 截图显示一个“你好”工作 28 秒，读取文件并执行命令后仍未回复 | 规则升级 | 应避免成本 | 将首次问候收紧为零工具 / 零读盘 / 零命令快速回复路径；身份不确定时把“定位工程身份”列为选项而不是先读取；sensor 检查冷启动入口和主动对话页的性能预算词 | `python3 scripts/check_all.py --only harness-governance` / [[proactive-dialogue-system]] | active |
| 2026-07-23 | 首次问候规则没有进入冷启动必读层 | 用户指出新开对话不生效，只有当前对话因上下文存在才生效 | 规则升级 | 可优化成本 | 将首次问候最低回复形态上提到根 [[AGENTS]] 和 [[.codex/AGENTS]]，并让 `check_harness_governance.py` 检查冷启动 greeting guard | `python3 scripts/check_all.py --only harness-governance` / [[AGENTS]] | active |
| 2026-07-23 | 首次问候退化成闲聊分叉 | 截图显示 agent 对“你好”只回答“继续处理 wiki 还是先聊点别的”，没有工程身份、推进方向或推荐分块 | 规则升级 | 可优化成本 | 在 [[proactive-dialogue-system]] 增加首次问候最低回复形态，要求工程身份、主体推进能力、2 到 4 个可选推进方向和推荐下一步；在 [[response-mode-routing]] 和 sensor 中锁定该形态 | `python3 scripts/check_all.py --only harness-governance` / [[proactive-dialogue-system]] | active |
| 2026-07-23 | 首次问候应进入轻量项目引导 | 用户指出 clone 工程后说“你好”时，希望 agent 能引导用户推进项目，并可按对话分块呈现 wiki / agent 体系建设 | 规则升级 | 可优化成本 | 更新 [[proactive-dialogue-system]] 和 [[response-mode-routing]]，新增首次问候入口、可选推进方向和 wiki / agent 体系分块呈现；避免把问候直接升级为 Goal / 全量调研 / 写 log | `python3 scripts/check_all.py --only harness-governance` / [[proactive-dialogue-system]] | active |
| 2026-07-23 | 逐 topic 清单不等于治理体系完成 | 用户指出上一轮只把所有 topic 做成能力吸收 manifest 和 sensor，仍没有全面整改 wiki 的 agent、workflow、memory、harness、skill 等治理体系 | 规则升级 | 必要成本 | 新增 [[wiki-governance-system-contract.v1]]、[[templates/governance-system-upgrade-contract-template]] 和 `scripts/check_governance_system_rectification.py`，并把全面整改完成定义接入 agent adapter、WORKFLOW、memory、harness、skills、templates、ledger 和 check_all | `python3 scripts/check_all.py --only governance-system-rectification` / [[wiki-governance-system-contract.v1]] | active |
| 2026-06-25 | 复盘 archive 与 sensor 闭环升级 | 用户要求把 Harness 复盘触发、档案落位、文件爆炸控制、行动分流、自演进和本地 sensor 接成可验证闭环 | 规则升级 | 可优化成本 | 建立 `projects/retrospectives/<year>/` 与 `indexes/` 结构，更新 [[projects/retrospectives/README]]、[[projects/design/topics/retrospective-archive-storage-structure]]、[[skills/retrospective-capability/SKILL]]、[[templates/project-retrospective-template]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]] 和 `scripts/check_retrospective_system.py` | `python3 scripts/check_all.py --only retrospective-system` | active |
| 2026-06-22 | Agent Harness L5 验证补强 | 用户指出上一轮仍把真实运行质量、多 agent 运行质量和外部 Git 状态写成未验证边界，要求必须验证到 L5 | 验收关闭 | 必要成本 | 新增 `scripts/check_agent_harness_l5.py` 和 [[projects/development/reports/2026-06-22-agent-harness-l5-validation]]，把 Goal dry-run、Run Capsule dry-run、Subproject Git Preflight live readback、Harness Evolution route 和最终回复证明接到 `check_all`；同步规则升级入口 | `python3 scripts/check_all.py --only agent-harness-l5` | active |
| 2026-06-22 | 整体 Agent Harness 模块接入 | 用户要求不是只迁移 skills，而是把入口规则、响应模式、运行合同、任务编排、写入边界、沉淀路由、sensor 门禁、复盘自演进和最终交付合同接入目标工程 | 规则升级 | 可优化成本 | 新增 [[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]；升级 Goal / Run / Loop 模板、Loop skill、入口规则和 `check_harness_governance.py` / `check_loop_engineering.py` | `python3 scripts/check_all.py --only harness-governance,loop-engineering` | active |
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
| 复盘 archive 结构检查 | 复盘 archive 与 sensor 闭环升级 | `scripts/check_retrospective_system.py` 检查 archive root 不平铺正文、年份目录、by-year 收录、模板字段、显式复盘规则和行动分流 | active |
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
| Agent Harness core wiring | 编排、状态约束和治理分级容易只停在自然语言 | `check_harness_governance.py` 检查 [[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]、入口和模板字段 | active |
| Agent Harness L5 validation | 结构 wiring 容易被误写成真实运行质量 | `scripts/check_agent_harness_l5.py` 检查代表性 Goal / Run / Git preflight / ledger route 和 L5 final proof 报告 | active |
| 治理体系全面整改 gate | 逐 topic 清单不等于治理体系完成 | `scripts/check_governance_system_rectification.py` 检查 [[wiki-governance-system-contract.v1]]、agent adapter、WORKFLOW、memory、harness、skill、template、ledger、topic adoption 和 `check_all` 接线 | active |

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
| 多 agent / 子工程任务必须由 Orchestrator 定义 Run Capsule，Worker 只交证据，Evaluator 做合流裁决；涉及代码前先做 Subproject Git Preflight | 整体 Agent Harness 模块接入 | [[agent-orchestration]] / [[templates/run-capsule-template]] / `scripts/check_harness_governance.py` | active |
| 规则、模板、sensor、log、复盘和 Goal 的强度先做 P0 / P1 / P2 / P3 分级，避免所有偏差都升级成硬规则 | 整体 Agent Harness 模块接入 | [[agent-governance-strategy]] / [[POLICY]] / [[WORKFLOW]] | active |
| 行动依赖权限、远程、dirty / diverged、预算或人工确认时先做 state constraint reasoning | 整体 Agent Harness 模块接入 | [[state-constraint-reasoning]] / [[WORKFLOW]] / [[POLICY]] | active |
| L5 不等于泛称“已验证”；必须给用户可见的命令、结果、commit / push readback、不能上推边界和例外原因 | Agent Harness L5 验证补强 | [[instruction-adherence]] / `scripts/check_agent_harness_l5.py` / 本轮验证报告 | active |
| 全面整改不能用局部 coverage 代替系统能力落地；必须逐层写入 owner、模板、memory、harness、skill、sensor 和 closeout proof | 逐 topic 清单不等于治理体系完成 | [[wiki-governance-system-contract.v1]] / [[templates/governance-system-upgrade-contract-template]] / `scripts/check_governance_system_rectification.py` | active |

## Rule Prune Queue

| 候选清理 | 原因 | 当前状态 |
| --- | --- | --- |
| `check_harness_governance.py` 承担所有细节检查 | 已拆出 ledger、instruction-adherence 和 project-docs 专项 sensor，聚合检查后续只保留 wiring / 模板 / Harness 主干 | active |
| 多处手写检查脚本清单 | 已由 `scripts/check_all.py --list` 和 `--only` 承接 | observed |
| 已被 sensor 覆盖的重复自然语言规则 | 避免入口页继续膨胀 | observed |
| `work-item-matrix` 旧关键词堆叠 | 已改为结构化检查，后续优先补字段 / 表头 / 章节断言 | promoted |
