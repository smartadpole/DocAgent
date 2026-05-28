---
type: trace
id: TRACE-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-28
tags: [trace, project]
---

# 需求演进链

这页是项目层里“需求如何收敛成当前实现口径”的主入口。

- 详细记录规则见 [[trace-writing-rules]]。
- 默认模板见 [[templates/trace-entry-template]]。

上游：[[projects/README]]、[[projects/requirements]]、[[projects/design/README]]  \
横向：[[projects/decisions]]、[[projects/development/README]]、[[projects/development/execution/worklog]]  \
下游：[[projects/releases]]、[[projects/incidents/README]]

## 这页负责什么

- 记录一轮需求的原始意图
- 记录中途新增约束、范围收敛和修补性需求
- 记录哪些方案被采用、哪些方案被放弃
- 记录当前真正生效的最终范围
- 把需求页、设计页、决策页和开发页串成一条可回看的主链

## 这页不负责什么

- 不按日期组织整轮对话历史，那是 [[log]]
- 不只记录最终拍板结果，那是 [[projects/decisions]]
- 不沉淀项目长期稳定背景，那是 [[projects/memory/README]]
- 不重复写完整设计正文或开发流水

## 当前主题

### TRACE-003 计划型问题的系统状态模型与约束传播方法

- **原始意图**：
  - 用户指出自己缺的不是“多记一个前置条件”，而是把新信息放进整个系统里做状态与约束传播推演的能力。
  - 这类缺口不仅会出现在搬家，也会出现在旅行、办证、采购、部署、上线、看病和签合同等所有依赖权限、资源、时间窗或外部确认的计划型问题里。
- **收敛后的可执行需求**：
  - 把“先更新状态变量、做约束传播、判可执行性，再更新计划”升级为当前 wiki 的正式方法。
  - 研究层要系统调研自动规划、时间约束网络、约束规划 / 调度、项目调度、MBSE / Statecharts 和系统思维各自提供什么能力。
  - 治理层要补一个跨场景可复用的方法入口，并把它接进响应模式、主动对话和 discovery 模板。
- **关键决策变化**：
  - **主收敛**：不把这次问题只沉淀成一篇“思考反思”，而是正式新增 [[state-constraint-reasoning]] 作为计划型问题的方法真相源。
  - **结构分层**：外部知识进入 [[articles/2026-05-28-state-constraint-planning-research]]，稳定方法进入 [[concepts/state-constraint-planning]]，可执行默认进入治理页和模板。
  - **执行改口**：今后遇到明显依赖权限、资源、时间窗或外部确认的计划型问题，默认先做状态变量和约束传播，不直接写动作安排。
- **最终范围**：
  - 生效入口：[[state-constraint-reasoning]]
  - 知识沉淀：[[articles/2026-05-28-state-constraint-planning-research]]、[[concepts/state-constraint-planning]]
  - 同步入口：[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[templates/guided-discovery-session-template]]
- **假设与未决项**：
  - 本轮先完成方法入口、研究卡片和模板落位，不额外引入新的 sensor。
  - 后续若再次出现“意图直接写成计划”的失守，再按 [[instruction-adherence]] 和 [[harness-feedback-ledger]] 判断是否补检查项或更强模板字段。
- **关联页面**：
  - [[articles/2026-05-28-state-constraint-planning-research]]
  - [[concepts/state-constraint-planning]]
  - [[state-constraint-reasoning]]
  - [[response-mode-routing]]
  - [[proactive-dialogue-system]]
  - [[projects/decisions]]
- **迭代**：

#### 2026-05-28

- **记录人**：sunhao
- **角色**：agent
- **本轮变化**：
  - **主收敛**：把“系统状态模型意识缺失”从单次生活规划反思上升为跨场景可复用方法，并进入治理层。
  - **研究补齐**：补做自动规划、时间约束网络、约束规划 / 调度、项目调度、MBSE / Statecharts 和系统思维的组合调研。
  - **模板落地**：给引导式设计模板增加状态模型、约束传播和可执行性判断字段，减少以后只写动作清单。
- **当前实现口径**：
  - 新信息进入系统后，默认先归类为事实、意图、约束、假设、动作候选或阻塞，再做状态变量更新与约束传播。
  - 没有通过可执行性判断的动作，不直接写进正式安排或当前计划。

#### 2026-05-28 报告资产化

- **记录人**：sunhao
- **角色**：agent
- **本轮变化**：
  - **主纠偏**：确认这些模板写法属于知识库专题成果，而不是当前 wiki 的系统模板层。
  - **专题收口**：新增 [[articles/2026-05-28-state-constraint-template-pack]]，集中承接超简版、生活版和工程版三类模板样式。
  - **边界收回**：撤回 `templates/` 中那组状态推演报告资产引用，只在治理页和概念页保留专题成果入口。
- **当前实现口径**：
  - 状态与约束推演有正式治理方法，但模板写法当前仍属于专题成果，不默认进入系统模板层。
  - 后续同类问题可优先复用专题成果页里的三类样式；只有跨场景高频稳定后，再考虑晋升为系统模板。

### TRACE-002 Agent Harness 与响应效率治理升级

- **原始意图**：
  - 综合 Harness Engineering 调研，把当前 wiki 升级成更智能、更高效的 Agent Harness。
  - 至少要处理好响应效率治理问题，避免简单诊断默认进入完整重治理闭环。
- **收敛后的可执行需求**：
  - 将响应模式路由从知识沉淀候选升级为正式治理机制。
  - 明确每轮先判快速诊断、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传或批处理。
  - 保持治理完整性不降级：快速 checkpoint 不能替代验收关闭，重治理闭环也不能伪装成仍在分析。
  - 为新系统接入准备 Harness 模板，明确单一信息源、写权限、验证层级、handoff 和 feedback sensor。
- **关键决策变化**：
  - **主收敛**：新增 [[response-mode-routing]] 作为响应效率治理的单一信息源，而不是把长规则直接塞进 [[AGENTS]]。
  - **规则吸收**：[[AGENTS]]、[[WORKFLOW]] 和 [[POLICY]] 只承接短入口和硬边界；详细模式表、读取预算和模式切换放在 [[response-mode-routing]]。
  - **技能分支**：[[skills/issue-analysis/SKILL]] 增加快速根因链和完整沉淀链的分支，防止所有问题都走同一条重路径。
- **最终范围**：
  - 生效入口：[[response-mode-routing]]。
  - H5 自演进入口：[[harness-evolution]] 和 [[harness-feedback-ledger]]。
  - 同步入口：[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]。
  - 执行支撑：[[skills/issue-analysis/SKILL]]、[[templates/harness-adoption-template]]、[[templates/harness-episode-package-template]]、[[templates/harness-evolution-review-template]]、`scripts/check_all.py`、`scripts/check_harness_governance.py`。
  - 来源分析继续保留在 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]。
- **假设与未决项**：
  - 本轮先完成 H5、ledger 和首个 Harness wiring sensor。
  - 下一步优先把 Markdown / wikilink、frontmatter、技能质量和模板完整性检查继续扩展进统一门禁，减少自然语言规则继续膨胀。
- **关联页面**：
  - [[concepts/harness-engineering]]
  - [[articles/2026-05-25-harness-engineering-research]]
  - [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]
  - [[response-mode-routing]]
  - [[AGENTS]]
  - [[WORKFLOW]]
  - [[POLICY]]
  - [[harness-evolution]]
  - [[harness-feedback-ledger]]
  - [[skills/issue-analysis/SKILL]]
  - [[templates/harness-adoption-template]]
  - [[templates/harness-episode-package-template]]
  - [[templates/harness-evolution-review-template]]
  - [[projects/decisions]]
- **迭代**：

#### 2026-05-25

- **记录人**：sunhao
- **角色**：agent
- **本轮变化**：
  - **主收敛**：把“先快后重”从文章候选升级为正式响应模式路由。
  - **结构选择**：新增独立治理页，避免 [[AGENTS]] 继续膨胀成百科全书。
  - **模板补齐**：新增 Harness 接入模板，给后续系统接入提供可复制骨架。
- **当前实现口径**：
  - 简单定位先给最小可信 checkpoint；只有触发沉淀、验收、规则升级或授权实现时，才升级到对应完整读取和回写链。
  - 响应效率优化不得绕过证据分层、权限边界、非默认值验证、人工确认和提交闭环。

#### 2026-05-25 H5 与 sensor 吸收

- **记录人**：sunhao
- **角色**：agent
- **本轮变化**：
  - **来源对照**：从 `DocCustomeranalysis` 只吸收系统层 Harness 能力，包括 H5 自演进、episode ledger、统一本地门禁、工作阶段专项 sensor、Codex 本地适配和复盘模板。
  - **事实剥离**：没有吸收下游项目的业务 issue、运行环境、测试报告状态、141 / 149 边界或 GitLab 平台假设。
  - **首个 sensor**：新增 `scripts/check_all.py` 和 `scripts/check_harness_governance.py`，先检查响应路由、H5 ledger、模板、入口 wiring 和本地适配。
- **当前实现口径**：
  - 用户纠偏、检查失败、模式切换和重复失守先写成 Harness episode；只有重复、影响面大或可脚本化时才晋升为规则。
  - 本库的门禁真相源是 `scripts/check_all.py`；CI 或平台配置只作为后续适配层。

#### 2026-05-25 研发事项、验收和台账吸收

- **记录人**：sunhao
- **角色**：agent
- **本轮变化**：
  - **主链升级**：把 `DocCustomeranalysis` 中已验证的 `Gate -> FP -> EP -> TASK` 事项设计抽象为当前 wiki 默认模型。
  - **关系节点补齐**：risk、Issue、test、验收、报告和服务台账不再散落为平行清单，而是作为事项关闭守卫和反馈节点。
  - **模板和 sensor**：新增 EP、TASK、Issue 模板与入口，并把 `work-item-matrix` 接入 `scripts/check_all.py`。
- **当前实现口径**：
  - 研发拆解不能停在轻量 TODO 或单独 FP；正式执行闭环需要说明父 Gate、FP、EP、TASK、关闭证据、回归守卫和不上推边界。
  - Issue 是案件档案，报告是每次验证记录；服务台账是运行实例事实的单一信息源。
  - 子工程沟通同样按 Gate / FP / EP / TASK 下发和回传；实现工程只生产代码、配置、测试和运行证据，主控侧负责吸收回写和关闭裁决。
  - 维护者日常入口顺序收口到 [[projects/development/plan/README]]；`work-item-matrix` sensor 改为结构化检查，避免靠关键词堆叠维持一致性。

### TRACE-001 文档系统分层与项目运行链路

- **原始意图**：
  - 把当前 Obsidian + Codex 文档系统整理成一个可演化的知识库，并能支撑项目推进。
  - 让项目材料从产品梳理、技术选型、架构设计一路支撑到 agent 开发，而不是只停在资料整理。
- **收敛后的可执行需求**：
  - 用 `README`、`INDEX`、`BRAIN`、`POLICY`、`projects/` 和 `log` 建立分层清晰的文档系统。
  - 在项目层明确需求、设计、决策、开发、发布、事故和项目记忆的职责边界。
  - 为项目推进补一条“需求如何收敛成实现”的演进链，不让关键约束和范围变化只留在聊天历史里。
- **关键决策变化**：
  - **主收敛**：早期重点是把 `[[log]]` 从动作流水改成按对话组织的主题化历史，但后来确认它仍然只回答“这轮对话在解决什么”，不承担完整需求演进链。
  - 在保留现有分层的前提下，新增 [[projects/trace]] 作为项目运行层主文件，而不是把 trace 混进 `[[log]]`、`[[projects/decisions]]` 或 `projects/memory/`。
- **最终范围**：
  - `[[log]]` 继续承担对话级主题化历史。
  - [[projects/trace]] 承担需求、约束、修补和最终实现口径之间的结构化串联。
  - 项目层入口、结构说明、流程页和规则页同步承认这条 trace 链路。
- **假设与未决项**：
  - 当前先用单文件主链，后续只有在主题明显增多时再拆分子页或模板。
  - 如果未来出现多个并行需求主题，再评估是否需要把每个主题拆成独立 trace 子页。
- **关联页面**：
  - [[README]]
  - [[INDEX]]
  - [[AGENTS]]
  - [[WORKFLOW]]
  - [[projects/README]]
  - [[projects/STRUCTURE]]
  - [[projects/meetings/README]]
  - [[projects/meetings/worklog]]
  - [[projects/requirements]]
  - [[projects/design/README]]
  - [[projects/decisions]]
- **迭代**：

#### 2026-04-12

- **记录人**：sunhao
- **角色**：agent
- **本轮变化**：
  - **主收敛**：明确区分 `[[log]]` 和需求演进 trace 的职责边界。
  - 把收尾模式补成显式协议，避免收尾时继续扩需求。
  - 正式新增 [[projects/trace]]，补齐项目推进里的需求演进主链。
- **当前实现口径**：
  - 新主题先在需求、设计和决策页形成最小可执行内容，再把原始意图、关键变化和最终范围串回这页。
  - 后续每轮进入项目推进的对话，都应判断是否需要续写已有 trace 主题，而不是只补 `[[log]]`。

#### 2026-04-13

- **记录人**：sunhao
- **角色**：agent
- **本轮变化**：
  - **主收敛**：把正式会议材料从开发 worklog 里拆出到 `projects/meetings/`，避免会议纪要和实现流水混写。
  - **主补充**：把会议组织规则、会前材料、会后分流和记录模板补进治理层和项目入口。
- **当前实现口径**：
  - 正式会议默认走 `projects/meetings/README.md` 和 `projects/meetings/worklog.md`。
  - 如果会议结果已经稳定成拍板、需求变化或实现动作，再分别回写到 `projects/decisions.md`、`projects/trace.md` 或 `projects/development/execution/worklog.md`。
  - `projects/development/execution/worklog.md` 继续只承接开发过程中的排障、联调、验证和临时同步。
