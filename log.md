# 活动记录

> 历史不重写；新记录按时间降序插在前面，并按日期下的对话组织。

`[[log]]` 只负责承接历史记录。

- 详细记录规则见 [[log-writing-rules]]。
- 默认模板见 [[templates/log-entry-template]]。

## 2026-05-25

### 完整吸收 Gate / FP / EP / TASK 研发事项体系

- **记录人**：sunhao
- **用户意图**：在前一轮吸收 H5 Harness 后，继续完整吸收 `DocCustomeranalysis` 中更成熟的 Gate、FP、EP、TASK、Issue、risk、test、项目验收、测试、服务台账和子工程沟通规则，并固化为当前 wiki 的默认工程设计。
- **主题**：
  1. 正式研发事项主链升级为 `Gate -> FP -> EP -> TASK`，不再只靠 FP / TODO / 报告表达执行闭环。
  2. risk、Issue、test、验收、报告和服务台账作为关系节点和关闭守卫，而不是平行堆放的清单。
  3. Issue 是案件档案，报告是每次验证记录，服务台账是运行实例事实单一信息源。
  4. 子工程只读上下文、受控回写和无写权限回传都必须按 EP / TASK / Issue / 报告 / 服务台账边界沟通。
- **关键动作**：
  1. **补事项模型**：更新 [[projects/development/plan/work-item-system-model]]，新增 [[projects/development/plan/task-design-model]]、[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]] 和 [[projects/development/issues/README]]。
  2. **补模板**：新增 [[templates/development-execution-package-template]]、[[templates/development-task-template]] 和 [[templates/development-issue-template]]，升级 [[templates/development-work-item-matrix-template]]、[[templates/development-test-report-template]] 和 [[templates/service-registry-template]]。
  3. **同步入口和治理**：更新 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[README]]、[[INDEX]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/development/README]]、[[projects/development/plan/README]]、[[projects/development/execution/README]]、Gate、FP、risk、报告和台账入口。
  4. **补子工程沟通**：升级 [[projects/development/execution/developer-execution-workflow]]、[[templates/developer-task-brief-template]] 和 [[templates/code-handoff-template]]，让任务下发、代码回传、验收评审和受控回写都使用 EP / TASK 主链。
  5. **新增 sensor**：新增并扩展 `scripts/check_work_item_matrix.py`，接入 `scripts/check_all.py`，让事项矩阵、模板、入口和子工程回传 wiring 可检查。
- **二阶反思**：这轮说明“完整吸收”不能只靠口头记忆；高价值工程设计必须同时落到模型、模板、入口、治理规则、子工程协作契约和本地 sensor，后续才能在新任务中自然执行。
- **影响页面**：[[projects/development/plan/work-item-system-model]]、[[projects/development/plan/task-design-model]]、[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/issues/README]]、[[projects/development/reports/README]]、[[projects/service-registry]]、[[templates/development-work-item-matrix-template]]、[[templates/development-execution-package-template]]、[[templates/development-task-template]]、[[templates/development-issue-template]]、[[templates/development-test-report-template]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]]、[[templates/service-registry-template]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[README]]、[[INDEX]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/trace]]、[[projects/decisions]]、[[log]]、`scripts/check_work_item_matrix.py`、`scripts/check_all.py`。

### 将 Codex Goals 转成主控和子工程协作契约

- **记录人**：sunhao
- **用户意图**：基于刚沉淀的 Codex Goals 专题，判断自有主控工程和子工程是否有升级建议，并把可执行的部分直接落实到当前模板库。
- **主题**：
  1. 长时任务升级点不是让 agent 无限后台运行，而是先写清线程级完成契约。
  2. 主控侧负责定义最终状态、验证面、约束、状态关闭条件和人工确认边界。
  3. 子工程侧负责按主控契约执行实现、本地验证、失败项、未验证边界和可吸收回传。
- **关键动作**：
  1. **新增模板**：新增 [[templates/goal-contract-template]]，把最终状态、验证面、约束、迭代策略、阻塞停止条件和主控 / 子工程分工收成可复制骨架。
  2. **升级协作模板**：更新 [[templates/harness-adoption-template]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]] 和 [[templates/harness-episode-package-template]]，加入 Goal Contract 字段和完成判断。
  3. **同步规则和入口**：更新 [[response-mode-routing]]、[[WORKFLOW]]、[[AGENTS]]、[[POLICY]]、[[README]]、[[INDEX]]、[[templates/README]] 和 [[concepts/harness-engineering]]，明确 Goal Contract 不替代验收关闭。
  4. **补 sensor 和 ledger**：更新 `scripts/check_harness_governance.py` 和 [[harness-feedback-ledger]]，让 Goal Contract 的关键入口和模板字段进入 Harness 检查。
- **二阶反思**：这轮说明 Goals 最适合先转成模板字段和 sensor，而不是直接新增一组重规则；主控和子工程之间真正需要固化的是“谁定义完成、谁生产证据、谁关闭状态”。
- **影响页面**：[[templates/goal-contract-template]]、[[templates/harness-adoption-template]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]]、[[templates/harness-episode-package-template]]、[[response-mode-routing]]、[[WORKFLOW]]、[[AGENTS]]、[[POLICY]]、[[README]]、[[INDEX]]、[[templates/README]]、[[concepts/harness-engineering]]、[[harness-feedback-ledger]]、[[log]]。

### 吸收 DocCustomeranalysis 的 H5 Harness 与本地门禁

- **记录人**：sunhao
- **用户意图**：把 `DocCustomeranalysis` 中更健全的 Harness 设计和整体系统流程抽象吸收到当前 wiki 模板库里，因为两者定位一致，但不能复制下游项目事实。
- **主题**：
  1. 当前 wiki 已有响应模式路由，但缺少 H5 自演进、episode ledger 和可执行 sensor 闭环。
  2. 可复用的是系统层能力：episode 数据、晋升 / 降级机制、统一本地门禁、工作阶段专项检查、Codex 本地入口和复盘模板。
  3. 不反哺的是下游项目业务 issue、运行环境、具体测试报告、141 / 149 边界、GitLab 平台假设和一次性状态。
- **关键动作**：
  1. **新增 H5 治理入口**：新增 [[harness-evolution]] 和 [[harness-feedback-ledger]]，让用户纠偏、检查失败、模式切换和重复失守先沉淀为 episode，再决定是否晋升规则。
  2. **新增模板和本地适配**：新增 [[templates/harness-episode-package-template]]、[[templates/harness-evolution-review-template]] 和 `.codex/AGENTS.md`。
  3. **新增统一门禁**：新增 `scripts/check_all.py` 和 `scripts/check_harness_governance.py`，先覆盖 Harness wiring、模板、入口链接和 H5 ledger。
  4. **同步入口和项目链路**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[concepts/harness-engineering]]、[[templates/README]]、[[skills/README]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/decisions]] 和 [[projects/trace]]。
- **二阶反思**：这轮说明“更健全”不是继续堆自然语言规则，而是把规则的生命线做出来：episode -> ledger -> sensor / template / skill -> 必要时再升规则；后续要优先扩展 Markdown / wikilink、frontmatter、技能质量和模板完整性 sensor。
- **影响页面**：[[harness-evolution]]、[[harness-feedback-ledger]]、[[response-mode-routing]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[README]]、[[INDEX]]、[[governance/README]]、[[concepts/harness-engineering]]、[[skills/README]]、[[templates/README]]、[[templates/harness-episode-package-template]]、[[templates/harness-evolution-review-template]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/decisions]]、[[projects/trace]]、[[log]]、`.codex/AGENTS.md`、`scripts/check_all.py`、`scripts/check_harness_governance.py`。

### 调研 Codex Goals 并沉淀为长时任务完成契约专题

- **记录人**：sunhao
- **用户意图**：围绕用户提供的本地译文材料，调研 Codex Goals 这个专题，并把它整理成可回看的知识沉淀，而不是只停留在一次对话解释。
- **主题**：
  1. Codex Goals 的本质是线程级持久目标和完成契约，不是全局 memory，也不是仓库级规则。
  2. 强 Goal 的关键在于把结果、证据、约束、边界、迭代策略和阻塞停止条件写清楚。
  3. Goals 对性能调优、flaky test 调查、复杂迁移和研究复现这类“终点明确、路径不明确”的长时任务特别有价值。
- **关键动作**：
  1. **归档来源**：把用户提供的微信 HTML 和资源目录归档到 `raw/codex-goals/`，保留本地原始材料，避免后续结论失去证据源。
  2. **新增专题卡片**：新增 [[articles/2026-05-25-codex-goals-research]]，整理 Goals 的定义、适用场景、强弱写法、生命周期控制、和 Agent Harness 的关系，以及可直接复用的 Goal 模板。
  3. **新增概念页**：新增 [[concepts/codex-goals]]，把 Codex Goals 收口为线程级完成契约的概念单一信息源。
  4. **补入口链接**：更新 [[INDEX]] 和 [[concepts/README]]，把 Codex Goals 纳入研发方法和概念入口，方便后续回链。
- **二阶反思**：这轮沉淀说明“长期委托给 Agent 的任务”不能只靠更长 prompt；后续如果要把这类能力进一步制度化，重点应放在可审计完成条件和证据检查，而不是再叠一层模糊规则。
- **影响页面**：[[articles/2026-05-25-codex-goals-research]]、[[concepts/codex-goals]]、[[INDEX]]、[[concepts/README]]、[[log]]、`raw/codex-goals/`。

### 将响应模式路由升级为 wiki Harness 默认机制

- **记录人**：sunhao
- **用户意图**：综合 Harness 设计，对当前 wiki 做一轮正式升级，让它更智能、更高效，并且至少把 agent 响应效率治理问题处理成可执行规则，而不是继续停留在候选反思。
- **主题**：
  1. 响应效率治理的关键是先判模式、先给 checkpoint，再决定是否进入沉淀、验收、规则升级或实现回传。
  2. [[AGENTS]] 继续保持短入口和硬约束，详细模式表、读取预算和切换规则由 [[response-mode-routing]] 做单一信息源。
  3. 快速诊断不能替代验收关闭，重治理闭环也不能伪装成仍在分析。
  4. 新系统接入 Agent Harness 需要模板化主控关系、单一信息源、写权限、验证层级、handoff 和 feedback sensor。
- **关键动作**：
  1. **新增治理入口**：新增 [[response-mode-routing]]，正式定义快速诊断、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传和批处理模式。
  2. **同步硬规则和流程**：更新 [[AGENTS]]、[[WORKFLOW]] 和 [[POLICY]]，让每轮先判响应模式，并明确快速诊断默认不写状态、不关闭 TODO / FP / Gate、不替代验收。
  3. **升级技能与模板**：更新 [[skills/issue-analysis/SKILL]]，增加快速根因链和完整沉淀链分支；新增 [[templates/harness-adoption-template]] 并挂入 [[templates/README]]。
  4. **同步入口和项目链路**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[concepts/harness-engineering]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/trace]] 和 [[projects/decisions]]。
  5. **更新来源分析边界**：把 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]] 从候选反思更新为来源分析和升级参考，生效入口改指 [[response-mode-routing]]。
- **二阶反思**：这轮暴露的不是缺少更多规则，而是需要把规则变成 Harness 里的路由器和反馈传感器；下一步不应继续堆入口正文，应优先补 wikilink、frontmatter、技能质量和模板完整性检查。
- **影响页面**：[[response-mode-routing]]、[[templates/harness-adoption-template]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[README]]、[[INDEX]]、[[governance/README]]、[[skills/README]]、[[skills/issue-analysis/SKILL]]、[[templates/README]]、[[concepts/harness-engineering]]、[[articles/2026-05-25-agent-response-efficiency-governance-reflection]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/trace]]、[[projects/decisions]]、[[log]]。

### 沉淀 Agent 系统升级参考方案

- **记录人**：sunhao
- **用户意图**：把关于 wiki、重治理主控工程和子工程如何升级为健全且高效的 Agent Harness 的综合判断沉淀到文档中，作为后续升级参考方案，而不是只留在对话里。
- **主题**：
  1. 后续升级关键不是继续加规则，而是建立可路由、可验证、可观测、可减载的 Agent Harness。
  2. wiki 应作为模板级 Harness，优先沉淀模式路由、系统接入模板和 feedback sensor，而不是扩写成厚重规则库。
  3. 重治理主控工程应保留治理完整性，但把快速根因链、完整沉淀链和验收关闭链显式分层。
  4. 子工程应作为实现和证据生产者，按主控裁决读取、局部实现、分层验证和 handoff 回传，不越权关闭主控状态。
- **关键动作**：
  1. **扩展升级参考**：更新 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]，新增“系统升级参考方案”，写入总目标、统一执行路由、wiki / 重治理主控工程 / 子工程分系统建议、黄金准则和三步落地顺序。
  2. **保持候选边界**：明确该方案当前仍是知识沉淀和规则候选，不直接修改 [[WORKFLOW]]、[[AGENTS]]、[[POLICY]] 或技能页。
  3. **补后续动作**：在同页后续动作中加入系统接入模板和 feedback sensor 优先级，避免后续只继续堆自然语言规则。
- **二阶反思**：这次沉淀再次确认效率治理的关键不是削弱主控证据闭环，而是把“先快后重”写成可执行路由；下一步如果要真正生效，应进入规则升级模式并同步入口、技能、模板和检查脚本。
- **影响页面**：[[articles/2026-05-25-agent-response-efficiency-governance-reflection]]、[[log]]。

### 调研 Harness Engineering 并沉淀为知识库专题

- **记录人**：sunhao
- **用户意图**：围绕用户提供的两份 Harness Engineering 本地材料做全面深入调研，形成可回看的专题沉淀，而不是只在对话里给出概念解释。
- **主题**：
  1. Harness Engineering 的核心不是提示词，而是 `Agent = Model + Harness` 这一工程系统视角。
  2. 有效 Harness 由规格、上下文、规则、Skill、Workflow、Sub Agent、脚本反馈、MCP / 工具、Memory 和可观测演化共同组成。
  3. OpenAI、LangChain、Vercel、本地 JK Launcher 案例和 X 图文都指向同一条实践线：少堆料，多用工程判断，把可判定约束下沉成脚本或反馈传感器。
- **关键动作**：
  1. **归档来源**：把用户提供的两份 HTML 归档到 `raw/harness-engineering/`，并把 X 图文里的关键图片归档到 `assets/harness-engineering/`。
  2. **新增专题卡片**：新增 [[articles/2026-05-25-harness-engineering-research]]，系统整理定义、组件地图、案例信号、成熟度模型、落地顺序、反模式和对当前文档库的启发。
  3. **新增概念页**：新增 [[concepts/harness-engineering]]，作为 Harness Engineering 的概念单一信息源。
  4. **补入口链接**：更新 [[INDEX]] 和 [[concepts/README]]，把专题和概念纳入研发方法入口。
- **二阶反思**：这次专题与当前文档库已有七层模型高度相关，但本轮仍属于知识沉淀，不直接改 [[AGENTS]]、[[WORKFLOW]] 或 [[POLICY]]；后续若要吸收为执行机制，应优先补链接检查、frontmatter 检查等 feedback sensor，而不是继续加规则正文。
- **影响页面**：[[articles/2026-05-25-harness-engineering-research]]、[[concepts/harness-engineering]]、[[INDEX]]、[[concepts/README]]、[[log]]、`raw/harness-engineering/`、`assets/harness-engineering/`。

### 纠正 agent 响应效率治理反思的层级归属

- **记录人**：sunhao
- **用户意图**：指出前一轮把 agent 响应效率治理反思放进 `projects/development/plan/` 是错误归类，并继续要求对重治理主控工程慢的问题做全面、客观分析，目标是功能完善且高效，而不是简单把治理闭环砍掉。
- **主题**：
  1. 重治理主控工程的慢主要来自主控治理链路过重，不是默认检查脚本本身慢。
  2. 当前模板库缺少针对单个简单问题的“快速诊断模式”，只有批量材料处理的轻量模式。
  3. issue 分析 + 沉淀本身是合理需求；真正要拆分的是必要成本、可优化成本和应避免成本。
  4. 该结论当前只应进入知识沉淀层，不能伪装成项目研发待办或已生效硬规则。
- **关键动作**：
  1. **迁移沉淀页**：把原 `projects/development/plan/agent-response-efficiency-upgrade-plan` 改迁到 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]，作为知识沉淀和规则候选。
  2. **撤回项目化挂载**：清理 [[projects/development/plan/README]]、[[projects/development/execution/todo]] 和 [[projects/status]] 中关于该事项的项目计划、待办和状态入口。
  3. **保留知识入口**：更新 [[INDEX]]，把该反思挂到设计思路 / 知识沉淀入口，而不是研发方法入口。
  4. **补全面分析**：扩展 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]，加入必要成本、可优化成本、应避免成本、五类响应模式、判定表和阶段性反馈目标，明确“慢的核心工作有必要，但当前慢法仍可优化”。
- **当前边界**：本轮仍没有修改 [[AGENTS]]、[[WORKFLOW]] 或 [[POLICY]] 的硬规则；如果后续要正式引入快速诊断模式，需要另起规则升级流程。
- **影响页面**：[[articles/2026-05-25-agent-response-efficiency-governance-reflection]]、[[projects/development/plan/README]]、[[projects/development/execution/todo]]、[[projects/status]]、[[INDEX]]、[[log]]。

## 2026-05-12

### 从重治理主控工程抽象吸收技能层和 issue-analysis 技能

- **记录人**：sunhao
- **用户意图**：继续检查重治理主控工程中可反哺当前模板库的技能和规则，吸收项目内 agent 技能层与问题分析方法，同时避免把下游项目事实、运行状态和业务链路带入模板库。
- **主题**：
  1. 下游项目新增的 `skills/` 层属于可复用系统结构，适合进入模板库，作为项目内 agent 分析流程、判断框架和输出格式的主入口。
  2. `issue-analysis` 技能中的事实源分层、最小根因链、计数 / 状态单位归一、跨工程分工、三层验证和回写守卫具备通用性。
  3. 下游项目里的具体业务 pipeline、服务实例、表名、运行 ID、handoff 路径和一次性事故材料属于项目材料，不进入模板技能正文。
- **关键动作**：
  1. **新增技能层**：新增 [[skills/README]]，把项目内 agent 技能和 [[templates/README]]、治理层、项目事实源区分开。
  2. **新增问题分析技能**：新增 [[skills/issue-analysis/SKILL]]，抽象沉淀主控侧 issue / incident 分析流程，覆盖问题框、上下文读取、事实源地图、状态单位归一、最小根因链、责任边界、跨工程分工、联测方案、回写守卫和禁止项。
  3. **补技能模板**：新增 [[templates/skill-template]] 并挂入 [[templates/README]]，让后续项目内技能有可复制骨架，避免每次从空白页起步。
  4. **同步入口和规则**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[BRAIN]]、[[POLICY]] 和 [[template-feedback-rules]]，把技能层纳入七层模型、读取顺序、路由规则、反哺范围和项目材料红线。
- **不反哺内容**：具体业务链路、服务名、数据表、运行 ID、服务实例、生产状态、TODO / Gate / 测试结论、本地路径和一次性 handoff 不进入当前模板库。
- **模板检查结果**：新增 [[templates/skill-template]]；技能正文只保留可复用流程和回写守卫，未复制第二份项目状态、TODO、测试报告或服务台账正文。
- **协作契约检查结果**：技能层仍遵守主控文档库与子工程的只读上下文和受控回写边界；技能可指导读取子工程 `AGENTS.md`、技能和 handoff，但默认不直接修改子工程。
- **影响页面**：[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[BRAIN]]、[[POLICY]]、[[template-feedback-rules]]、[[skills/README]]、[[skills/issue-analysis/SKILL]]、[[templates/README]]、[[templates/skill-template]]、[[log]]。

## 2026-05-09

### 从重治理主控工程抽象吸收研发治理规则

- **记录人**：sunhao
- **用户意图**：检查重治理主控工程中是否存在可反哺当前模板库的规则，并只吸收抽象后的系统层信息，不带入下游项目事实。
- **主题**：
  1. 下游项目暴露出运行服务治理、源码审计、跨工程 handoff 和验收证据分层四类可复用规则。
  2. 服务 IP、端口、代码提交、业务 TODO、具体测试报告和项目状态属于下游项目材料，不进入当前模板库。
  3. 反哺时优先更新既有主入口、规则页和模板页，避免复制第二份正文。
- **关键动作**：
  1. **运行治理**：新增 [[projects/service-registry]] 和 [[templates/service-registry-template]]，把服务实例台账、服务组 / 组件层级、健康检查、配置 profile、数据目录和脱敏字段口径抽象为可选项目层结构。
  2. **源码审计**：新增 [[projects/codebase/source-code-audit-workflow]] 和 [[templates/source-code-audit-report-template]]，固化 L0 到 L3 的源码工程解读等级、证据矩阵、自动推进和终态自审边界。
  3. **验收规则**：更新 [[POLICY]]、[[projects/development/reports/README]] 和 [[templates/development-test-report-template]]，吸收验收对象分层、`local validation` / `service-side validation` / `end-to-end validation`、非默认参数验证、人工确认项和报告双向关联规则。
  4. **跨工程协作**：更新 [[projects/development/execution/developer-execution-workflow]]、[[templates/code-handoff-template]] 和 [[templates/developer-task-brief-template]]，强化只读上下文、受控回写、handoff 入库、独立抽插和下游吸收边界。
  5. **入口同步**：更新 [[README]]、[[INDEX]]、[[AGENTS]]、[[WORKFLOW]]、[[BRAIN]]、[[template-feedback-rules]]、[[projects/README]]、[[projects/STRUCTURE]] 和 [[projects/codebase/README]]，补齐新页面类型的主入口、上下游关系、读取顺序和反哺边界。
- **不反哺内容**：下游项目中的具体服务实例、IP / 端口、进程、提交号、业务 TODO、测试结论、灰度状态、项目技术拍板和一次性排障过程均保留在下游项目，不写入当前模板库。
- **模板检查结果**：新增服务实例台账条目模板和源码审计报告模板；既有测试报告、编码任务执行单和代码工程回传包模板已同步扩展，项目页只链接模板，不维护第二份模板正文。
- **协作契约检查结果**：主控文档库与实现工程仍按“只读上下文 + 代码工程回传包 + 本库侧吸收”作为默认模式；直接回写本库或修改子工程都必须有明确授权。
- **影响页面**：[[README]]、[[INDEX]]、[[AGENTS]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[template-feedback-rules]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/service-registry]]、[[projects/codebase/README]]、[[projects/codebase/source-code-audit-workflow]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/reports/README]]、[[templates/README]]、[[templates/service-registry-template]]、[[templates/source-code-audit-report-template]]、[[templates/code-handoff-template]]、[[templates/developer-task-brief-template]]、[[templates/development-test-report-template]]、[[log]]。

## 2026-05-07

### 固化新应用探索从调研到研发的轻量路径

- **记录人**：sunhao
- **用户意图**：把“探索全新桌面端 / web / app 时，先轻量调研和收敛，再进入项目研发结构”的判断沉淀下来，并尽量固化成后续可复用的 agent 能力。
- **主题**：
  1. 全新应用探索不应一开始就铺满完整 `projects/`、设计包和研发拆解。
  2. 多个候选方向应先走证据层和知识沉淀层，用材料、摘要、概念和候选比较验证问题。
  3. 只有某个方向明确成为当前要推进的应用，才进入项目层并逐步补需求、trace、设计专题、决策、架构包和研发事项。
- **关键动作**：
  1. **主流程**：在 [[WORKFLOW]] 中新增 `1.9.0 新应用探索模式`，明确 discovery、轻量项目、完整研发三种交付状态和推荐演进链。
  2. **主入口**：更新 [[README]]、[[INDEX]]、[[projects/README]] 和 [[projects/STRUCTURE]]，把新应用探索路径挂到入口、项目极简模式和结构说明里。
  3. **主路由**：更新 [[BRAIN]]、[[POLICY]] 和 [[AGENTS]]，把“多方向探索先轻量路由，选定当前项目后再进项目层”固化成共享背景、路由规则和 agent 执行约束。
  4. **本地技能**：新增本地 Codex skill `app-discovery`，只保留触发条件、轻量工作流和输出形态，详细流程仍以当前文档库为单一信息源。
- **影响页面**：[[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[log]]。

## 2026-05-06

### 纠正模板库和具体工程之间的吸收方向

- **记录人**：sunhao
- **用户意图**：纠正前一轮把“模板到项目吸收边界”写成当前模板库主流程的视角错误，明确当前库是上游模板库，未来吸收应当是从具体工程中抽象系统层信息回到模板库。
- **主题**：
  1. 当前库是上游模板，不是具体项目；下游项目的不吸收清单只能作为反哺边界参考。
  2. 吸收方向固定为“具体工程 / 下游项目 -> 抽象系统层信息 -> 模板库”。
  3. 模板库不维护下游项目已吸收到哪个上游 commit、项目侧同步状态或项目侧不吸收决定。
- **关键动作**：
  1. **主纠偏**：从 [[WORKFLOW]] 中移除“模板到项目吸收模式”，回到模板反哺模式的单一方向。
  2. **主边界**：更新 [[template-feedback-rules]]，把下游非吸收清单定位为下游处理项目材料边界的参考，而不是模板库主流程。
  3. **主约束**：更新 [[AGENTS]]，要求具体工程提供的不吸收清单只用于辅助判断反哺边界，不在当前库维护项目侧同步记录。
- **影响页面**：[[WORKFLOW]]、[[template-feedback-rules]]、[[AGENTS]]、[[log]]。

### 补清模板到具体项目的吸收边界

- **记录人**：sunhao
- **用户意图**：确认从上游模板库吸收内容时，哪些内容不适合进入当前具体项目，并检查当前工程是否存在把模板示例或上游项目事实误当成项目事实的问题。
- **主题**：
  1. 从模板库吸收更新时，也要区分系统能力和模板 / 项目事实。
  2. 占位项目、示例功能点、示例 TODO、示例 Gate、示例报告、示例风险和示例执行数据不能成为目标项目事实。
  3. 目标项目应记录已吸收到的上游 commit 或版本，后续只比较新变化，避免重复吸收。
- **关键动作**：
  1. **主边界**：更新 [[template-feedback-rules]]，新增模板到项目的吸收边界，明确只吸收结构、规则、流程、模板骨架和协作契约。
  2. **主约束**：更新 [[AGENTS]]，要求具体项目吸收上游模板库时也要执行模板到项目的边界判断。
  3. **主流程**：更新 [[WORKFLOW]]，新增模板到项目吸收模式，要求记录上游 commit / 版本、吸收项和不吸收项。
- **影响页面**：[[template-feedback-rules]]、[[AGENTS]]、[[WORKFLOW]]、[[log]]。

### 把每轮结束前的二阶反思固化成学习机制

- **记录人**：sunhao
- **用户意图**：要求 agent 具备举一反三能力，能够在每次对话结束时主动反思当前问题、抽象到更高层面，并从多轮对话中持续完善系统，而不是同类问题反复等用户提醒。
- **主题**：
  1. 对话收尾不应只做结果提交，还要判断本轮暴露的是单点问题还是同类流程缺口。
  2. 可复用教训应主动回写到规则、流程、模板、协作边界或共享背景，不应只留在会话里。
  3. 二阶反思要受 [[POLICY]] 约束：可自动改既有流程和执行约束，但新增高优先级规则或改变自动写入边界时必须升级。
- **关键动作**：
  1. **主背景**：更新 [[BRAIN]]，把“系统应从每轮对话中持续学习并做二阶反思”写入共同工作方式。
  2. **主边界**：更新 [[POLICY]]，允许 agent 在收尾或被指出重复 / 同类问题时自动做二阶反思并更新既有流程、执行约束、模板入口或 [[log]]，同时保留高优先级规则的冲突升级边界。
  3. **主执行**：更新 [[AGENTS]] 和 [[WORKFLOW]]，把二阶反思加入会话级规则和收尾顺序，要求检查同类漏检、流程缺口、模板缺口、协作契约缺口和记忆路由缺口。
- **影响页面**：[[BRAIN]]、[[POLICY]]、[[AGENTS]]、[[WORKFLOW]]、[[log]]。

### 把模板和跨工程协作漏检沉淀为结构变更必检项

- **记录人**：sunhao
- **用户意图**：追问为什么相关模板和主控 / 实现工程协作边界要等用户指出后才补，要求把这类漏检转成以后不会再发生的机制。
- **主题**：
  1. 前一轮采纳项目层规则时只检查了目录和规则正文，没有把可复制模板和跨工程协作契约当成同级必检项。
  2. 新增项目层结构、事项类型、执行流程或报告类型时，必须同轮检查 `templates/` 和模板入口。
  3. 只要规则涉及当前文档库和实现工程 / 子模块协作，必须同轮写清任务下发、证据回传、写权限、状态关闭和冲突升级。
- **关键动作**：
  1. **主约束**：更新 [[AGENTS]]，把项目层结构变更时的模板完整性检查、跨工程协作边界检查写成 agent 必须遵守的硬约束。
  2. **主流程**：更新 [[WORKFLOW]]，把模板检查和主控 / 实现工程协作契约检查加入新增模块、目录和高频文件类型的固定步骤。
  3. **主反哺**：更新 [[template-feedback-rules]]，要求跨项目反哺时记录模板检查结果和协作契约检查结果，不能只写结构和规则。
- **影响页面**：[[AGENTS]]、[[WORKFLOW]]、[[template-feedback-rules]]、[[log]]。

### 补齐研发协作模板并明确主控与实现工程边界

- **记录人**：sunhao
- **用户意图**：检查项目层规则采纳后，相关模板目录和模板文件是否齐全，以及现有规则是否覆盖当前文档主控系统和实现工程子模块之间的协作。
- **主题**：
  1. 研发层新增结构已经有目录和入口，但模板层没有同步补齐，且部分模板正文散在开发页里。
  2. 主控系统和实现工程之间已有回传包、写权限模式和反馈闭环，但需要把协作边界显式写清。
  3. 模板正文应回到 [[templates/README]] 及其模板页，项目页只保留入口链接，避免两份正文漂移。
- **关键动作**：
  1. **主模板**：新增功能点、事项矩阵、TODO、Gate、测试报告、风险、开发过程记录、编码任务执行单、代码工程回传包和工程反馈模板，并统一挂到 [[templates/README]]。
  2. **主收口**：把 [[projects/development/feature-points/README]]、[[projects/development/execution/todo]]、[[projects/development/gates/README]]、[[projects/development/reports/README]]、[[projects/development/risks/README]]、[[projects/development/execution/worklog]]、[[projects/development/execution/developer-execution-workflow]] 和 [[projects/development/execution/engineering-feedback-loop]] 里的内联模板正文收回成模板链接。
  3. **主协作**：在 [[projects/development/execution/developer-execution-workflow]] 中补清主控系统和实现工程的任务下发、开发执行、测试反馈、回传吸收和冲突升级边界。
  4. **主入口**：更新 [[README]]、[[INDEX]]、[[WORKFLOW]]、[[projects/status]] 和 [[projects/memory/policy-links]]，让模板入口和功能点模板口径回到单一信息源。
- **影响页面**：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[templates/README]]、[[templates/development-feature-point-template]]、[[templates/development-work-item-matrix-template]]、[[templates/development-todo-template]]、[[templates/development-gate-template]]、[[templates/development-test-report-template]]、[[templates/development-risk-template]]、[[templates/development-worklog-entry-template]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]]、[[templates/engineering-feedback-template]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/execution/todo]]、[[projects/development/execution/worklog]]、[[projects/development/feature-points/README]]、[[projects/development/gates/README]]、[[projects/development/reports/README]]、[[projects/development/risks/README]]、[[projects/status]]、[[projects/memory/policy-links]]、[[log]]。

### 抽象采纳项目层研发规则而不同步项目事实

- **记录人**：sunhao
- **用户意图**：在已经沉淀跨项目反哺红线后，重新处理“从下游项目采纳新设计”的任务，重点采纳项目层面的通用规则更新，同时避免再次把具体项目事实同步进模板库。
- **主题**：
  1. 只把研发计划、执行、阶段门、实现、报告和风险这些可复用项目层结构抽象回模板。
  2. 把需求、目标、功能点、TODO、反馈、证据、风险和 Gate 准出的关系沉淀成通用事项模型。
  3. 明确不采纳下游项目里的具体业务范围、结果表、字段、运行证据、具体 Gate 内容和测试结论。
- **关键动作**：
  1. **主结构**：把开发层扩展为 [[projects/development/plan/README]]、[[projects/development/execution/README]]、[[projects/development/gates/README]]、[[projects/development/implementation/README]]、[[projects/development/reports/README]] 和 [[projects/development/risks/README]]，并把原开发流水迁到 [[projects/development/execution/worklog]]。
  2. **主模型**：新增 [[projects/development/plan/work-item-system-model]]、[[projects/development/execution/todo]]、[[projects/development/execution/developer-execution-workflow]] 和 [[projects/development/execution/engineering-feedback-loop]]，收口研发事项关系、TODO 关闭守卫、工程协作回传和反馈纠偏。
  3. **主方法**：新增 [[concepts/progressive-design-freeze]]，只保留阶段门滚动冻结的方法定义、冻结节奏和候选功能点提升标准，不带入下游项目应用页。
  4. **主同步**：更新 [[README]]、[[INDEX]]、[[AGENTS]]、[[WORKFLOW]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]] 和 [[projects/development/feature-points/README]]，让新项目层结构进入入口、读取顺序、同步规则和交付检查。
- **影响页面**：[[README]]、[[INDEX]]、[[AGENTS]]、[[WORKFLOW]]、[[concepts/README]]、[[concepts/progressive-design-freeze]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/development/README]]、[[projects/development/plan/README]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/execution/README]]、[[projects/development/execution/todo]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/execution/worklog]]、[[projects/development/gates/README]]、[[projects/development/implementation/README]]、[[projects/development/reports/README]]、[[projects/development/risks/README]]、[[projects/development/feature-points/README]]、[[log]]。

### 把跨项目误同步教训沉淀成反哺红线

- **记录人**：sunhao
- **用户意图**：在完全删除错误同步提交后，要求把这次误把具体项目事实同步进模板库的教训沉淀成规则，避免以后再次发生。
- **主题**：
  1. “采纳某项目设计”不能再被默认执行成整库同步或原样搬运项目设计页。
  2. 跨项目反哺必须先列候选分类和不反哺边界，再写入抽象后的系统层信息。
  3. 结果表、字段、灰度范围、项目 TODO、Gate、测试报告和代码审计结论这类内容默认属于项目材料，不进入模板库。
- **关键动作**：
  1. **主红线**：更新 [[template-feedback-rules]]，新增跨项目采纳红线，禁止整库同步、整目录复制、先写入再筛选。
  2. **主边界**：更新 [[POLICY]]，把跨项目采纳的自动写入边界收紧为先列候选、先做事实剥离。
  3. **主约束**：更新 [[AGENTS]]，把禁止原样同步下游项目设计写成 agent 执行约束。
- **影响页面**：[[template-feedback-rules]]、[[POLICY]]、[[AGENTS]]、[[log]]。

## 2026-04-25

### 重新定义模板反哺的系统层范围并补齐规则类反哺

- **记录人**：sunhao
- **用户意图**：纠正前一次反哺时对“可复用系统层信息”的定义过窄问题，明确只要是规则就默认进入反哺候选并必须判断，并把 DocFilmCommunity 中遗漏的规则、流程、写法和记忆路由抽象回模板库。
- **主题**：
  1. 重新定义模板反哺的系统层范围。
  2. 区分可复用系统信息和具体项目材料。
  3. 补齐 DocFilmCommunity 中已经验证的规则类反哺。
- **关键动作**：
  1. **主规则**：更新 [[template-feedback-rules]]，把可反哺系统层信息扩展为结构、流程、规则、记忆系统、写法格式、模板、自动化契约和治理说明，并明确“只要它是规则，就默认进入反哺候选”。
  2. **主边界**：在 [[template-feedback-rules]] 中补清项目材料范围，要求抽掉项目事实、业务状态、技术拍板和一次性结论，只保留可跨项目复用的系统规则。
  3. **主回填**：把 DocFilmCommunity 中关于 [[log]] 标题、同日记录复核、并列项编号、[[projects/trace]] 同轮同步和来源材料格式转换不进 trace 的规则，回写到 [[log-writing-rules]]、[[trace-writing-rules]]、[[templates/log-entry-template]]、[[templates/trace-entry-template]]、[[AGENTS]]、[[POLICY]] 和 [[WORKFLOW]]。
  4. **主同步**：补回“标签：内容”默认加粗、决策标题保持稳定、决策摘要不引入复杂 block id，以及完整架构包到研发拆解时的回链、验证、发布和交付前检查规则。
  5. **主防线**：补清“规则默认反哺”只是默认进入候选，不代表原样写入；写入前必须通过抽象、事实剥离、冲突、单一信息源和规则体积检查，后续证明不通用时要收窄、降级或退役。
  6. **主入口**：同步更新 [[README]]、[[INDEX]] 和 [[governance/README]] 中的模板反哺入口描述，避免入口页继续把反哺范围收窄成结构和模板。
- **影响页面**：
  1. [[template-feedback-rules]]
  2. [[log-writing-rules]]
  3. [[trace-writing-rules]]
  4. [[templates/log-entry-template]]
  5. [[templates/trace-entry-template]]
  6. [[AGENTS]]
  7. [[POLICY]]
  8. [[WORKFLOW]]
  9. [[README]]
  10. [[INDEX]]
  11. [[governance/README]]
  12. [[log]]

### 移除 `[[log]]` 记录标题里的旧固定前缀

- **记录人**：sunhao
- **用户意图**：检查模板库里是否仍然遗漏旧版 `[[log]]` 标题前缀，并按最新设计移除这段固定前缀。
- **主题**：
  1. 清理 `[[log]]` 历史记录标题里的旧前缀。
  2. 同步日志模板和日志写法规则。
- **关键动作**：
  1. **主修正**：批量移除 [[log]] 中所有三级标题开头的旧固定前缀，保留原本标题内容。
  2. **主同步**：更新 [[templates/log-entry-template]] 和 [[log-writing-rules]]，明确三级标题直接写一句话标题，不再加旧版固定前缀。
- **影响页面**：[[log]]、[[templates/log-entry-template]]、[[log-writing-rules]]。

### 把 DocFilmCommunity 的系统级进化反哺回 wiki 模板

- **记录人**：sunhao
- **用户意图**：解决不同项目各自演化后如何反哺模板库的问题，并把 DocFilmCommunity 中已经验证过的系统性规则、结构和模板抽象回当前 wiki 模板，但不带入具体项目事实。
- **主题**：
  1. 建立跨项目模板反哺机制。
  2. 抽象 DocFilmCommunity 的结构性演进。
  3. 同步项目层、设计层、会议层、决策写法和研发拆解流程。
- **关键动作**：
  1. **主机制**：新增 [[template-feedback-rules]]，明确下游项目反哺模板时要先区分项目事实和系统能力，再按结构、流程、规则、模板和知识沉淀分流。
  2. **主结构**：新增 [[projects/codebase/README]] 与代码基线子页，补入现实实现审计、冲突收口和复用边界；新增 [[projects/design/topics/README]]，承接未拍板设计专题和后续储备。
  3. **主设计包**：把设计层扩展成完整架构包，补齐 [[projects/design/backend-frontend-structure]]、[[projects/design/permission-boundary]]、[[projects/design/write-boundary]]、[[projects/design/deployment]] 和 [[projects/design/runtime-quality]]。
  4. **主流程**：更新 [[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]] 和项目入口，补上模板反哺模式、代码基线读取顺序、设计专题路由、完整架构包到功能点拆解、会议去重和决策写法骨架。
  5. **主模板**：新增 [[templates/decision-entry-template]]，并收紧 [[templates/meeting-entry-template]] 中会议行动项、会后回写和单条记录内去重的写法。
- **影响页面**：
  1. [[template-feedback-rules]]
  2. [[README]]
  3. [[INDEX]]
  4. [[governance/README]]
  5. [[BRAIN]]
  6. [[POLICY]]
  7. [[WORKFLOW]]
  8. [[AGENTS]]
  9. [[projects/README]]
  10. [[projects/STRUCTURE]]
  11. [[projects/status]]
  12. [[projects/codebase/README]]
  13. [[projects/design/README]]
  14. [[projects/design/topics/README]]
  15. [[projects/decisions]]
  16. [[projects/development/README]]
  17. [[projects/development/feature-points/README]]
  18. [[projects/meetings/README]]
  19. [[templates/decision-entry-template]]
  20. [[templates/meeting-entry-template]]
  21. [[log]]

## 2026-04-14
## 2026-04-13
### 确认会议记录默认是一会一条，预读材料则单独成页

- **记录人**：sunhao
- **用户意图**：确认正式会议到底是按“每个会议一个文件”组织，还是默认在同一个会议时间线里按条目记录，并厘清准备、会议记录和结论是否放在一起；同时确认如果明天要把会议问题发给对方提前看，该怎么组织。
- **主题**：
  1. 明确正式会议的默认承载方式。
  2. 明确单场会议内部的内容组织方式。
  3. 明确会前需要对外共享时的材料落点。
- **关键动作**：
  1. **主澄清**：在 [[projects/meetings/README]] 里补充规则，明确默认一场会不单独生成一个文件，而是在 [[projects/meetings/worklog]] 里写成一条记录。
  2. **主收口**：确认准备材料、会议纪要、结论和行动项默认放在同一条会议记录里，只有特别大的会议才再单独拆页。
  3. **主分流**：如果会前要发给对方提前看，优先单独开一页可分享的会前材料 / 议程页，不把预读材料只埋在 [[projects/meetings/worklog]] 的长时间线里。
- **影响页面**：[[projects/meetings/README]]、[[projects/meetings/worklog]]、[[templates/meeting-entry-template]]、[[log]]。

## 2026-04-13
### 把会议记录骨架提炼成可复用模板页

- **记录人**：sunhao
- **用户意图**：在已经拆出会议主入口和会议记录页之后，希望把单场会议的记录骨架再提炼成模板页，后续新增正式会议时可以直接复制使用。
- **主题**：
  1. 把会议记录骨架抽成模板。
  2. 让会议记录入口和模板互相可达。
- **关键动作**：
  1. **主新增**：新增 [[templates/meeting-entry-template]]，把正式会议记录的字段骨架、分流口径和使用说明沉淀成可复制模板。
  2. **主联通**：更新 [[templates/README]]、[[projects/meetings/worklog]] 和 [[governance/WORKFLOW]]，让模板从模板入口、会议记录页和治理流程里都能直接找到。
- **影响页面**：[[templates/meeting-entry-template]]、[[templates/README]]、[[projects/meetings/worklog]]、[[governance/WORKFLOW]]、[[log]]。

### 把正式会议从开发 worklog 拆出到专门会议入口

- **记录人**：sunhao
- **用户意图**：项目管理期间会议会很多，希望把正式会议材料、会议纪要和行动项单独收口，不再和开发过程流水混在一起，同时把会议管理的规则和流程沉淀成稳定入口。
- **主题**：
  1. 把正式会议从开发 worklog 中拆出独立层。
  2. 给会议材料、纪要、行动项和会后分流建立固定入口。
  3. 把会议组织规则和流程写进治理层与项目层。
- **关键动作**：
  1. **主新增**：创建 [[projects/meetings/README]] 和 [[projects/meetings/worklog]]，把正式会议入口、记录模板和时间线记录单独收口。
  2. **主同步**：更新 [[projects/README]]、[[projects/STRUCTURE]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/status]]、[[projects/memory/README]]、[[INDEX]] 和 [[README]]，让项目主入口、结构页和常用入口都能直接找到会议层。
  3. **主治理**：在 [[governance/WORKFLOW]] 和 [[AGENTS]] 里补上会议材料的收集、记录、分流和阅读顺序，并用 [[projects/decisions]]、[[projects/trace]] 记录这次结构拆分。
- **影响页面**：[[projects/meetings/README]]、[[projects/meetings/worklog]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/status]]、[[projects/memory/README]]、[[governance/README]]、[[governance/WORKFLOW]]、[[AGENTS]]、[[projects/decisions]]、[[projects/trace]]、[[INDEX]]、[[README]]、[[log]]。

### 把 Obsidian 的依赖说明写清楚

- **记录人**：sunhao
- **用户意图**：确认这套文档库是否能脱离 Obsidian 使用，避免把 `[[wikilink]]` 体系误写成可选功能。
- **主题**：
  1. 澄清 Obsidian 对内部导航的实际作用。
  2. 让入口页把“正文可读”和“链接可用”分开说清。
- **关键动作**：
  1. **主修正**：更新 [[README]] 和 [[INDEX]]，把 Obsidian 描述为这套库的原生阅读 / 编辑入口，并明确不用 Obsidian 时 `[[wikilink]]` 导航不能完整生效。
  2. **主收口**：把“普通 Markdown 阅读器也能读正文”与“完整链接网络依赖 Obsidian”分开表述，避免使用者误解为只是体验差异。
- **影响页面**：[[README]]、[[INDEX]]、[[log]]。

## 2026-04-13
### 把 commit message 的语言规则写进维护约束

- **用户意图**：明确协作时的提交信息规范，正文内容可以继续用中文，但 commit message 必须统一用英文。
- **主题**：
  1. 把 commit message 语言要求提升为维护约束。
  2. 保留正文和说明可中文的现有写作习惯。
- **关键动作**：
  1. **主更新**：在 [[AGENTS]] 的会话级规则里补充 commit message 必须使用英文的约束。
  2. **主澄清**：说明正文、说明和文档内容仍然可以使用中文，不影响既有写作习惯。
- **影响页面**：[[AGENTS]]、[[log]]。

## 2026-04-13
### 把已经处理过的 PRD 源稿从 `raw` 迁出，明确处理后内容只留在知识库层

- **用户意图**：确认 PRD 教程在经过整理后不应继续占用 `raw/`，而应该回到知识库层；只有还没处理的原始材料才继续留在 `raw/`。
- **主题**：
  1. 纠正 PRD 教程的分层归属。
  2. 强化 `raw/` 与知识库层的边界。
- **关键动作**：
  1. **主迁出**：把 [[archive/2026-04-13-prd-writing-guide-source]] 从 `raw/` 迁出，让这份已经处理过的源稿不再占用 `raw/`。
  2. **主对齐**：同步更新 [[concepts/prd-writing]] 和 [[articles/2026-04-13-prd-writing-guide]] 的来源链接，改指向历史草稿而不是 `raw/`。
  3. **主收紧**：在 [[raw/README]] 里补一句更明确的维护原则，说明已经整理成摘要、概念页、索引页或历史版本的内容，不应继续留在 `raw/`。
- **影响页面**：[[archive/2026-04-13-prd-writing-guide-source]]、[[concepts/prd-writing]]、[[articles/2026-04-13-prd-writing-guide]]、[[raw/README]]、[[log]]。

## 2026-04-13
### 把 PRD 指导重排成可复用的方法入口，并接入项目需求和设计流程

- **用户意图**：把新增加的 PRD 指导从一篇偏长的原始材料整理成可复用的方法入口，让它不只“能看”，还要能反向指导项目层的需求、设计和开发。
- **主题**：
  1. 重排 PRD 原始稿并去重。
  2. 抽出 PRD 写作方法页和摘要卡片。
  3. 把 PRD 方法接到项目需求、设计和 workflow。
- **关键动作**：
  1. **主整理**：重写 [[archive/2026-04-13-prd-writing-guide-source]]，按定义、常见误区、标准结构、思考顺序、专业细节、模板、自检和落库路径重新组织，删掉原稿里重复铺陈和来回兜圈的部分。
  2. **主沉淀**：新增 [[concepts/prd-writing]] 和 [[articles/2026-04-13-prd-writing-guide]]，把 PRD 写作方法沉淀成稳定概念页和摘要卡片。
  3. **主接线**：在 [[projects/README]]、[[projects/requirements]]、[[projects/design/README]]、[[WORKFLOW]] 和 [[INDEX]] 中补上 PRD 方法入口与项目落点，让需求页和设计页可以直接引用。
- **影响页面**：[[archive/2026-04-13-prd-writing-guide-source]]、[[concepts/prd-writing]]、[[articles/2026-04-13-prd-writing-guide]]、[[projects/README]]、[[projects/requirements]]、[[projects/design/README]]、[[WORKFLOW]]、[[INDEX]]、[[concepts/README]]、[[log]]。

## 2026-04-12
### 继续把项目层和治理页的旧口径收口到新治理结构

- **用户意图**：在治理层已经迁入 `governance/` 之后，继续把 `projects/` 层和直接相关治理页里残留的旧表述收口干净，避免入口页已经切换了，但项目结构页和项目主页还在按旧的根目录治理模型写说明。
- **主题**：
  1. 同步项目层对新治理结构的说明口径。
  2. 继续收紧项目页和治理页中的裸文件名引用。
- **关键动作**：
  1. **主同步**：更新 [[projects/README]] 和 [[projects/STRUCTURE]]，把治理层总边界正式改为指向 [[governance/README]]，并补上项目层如何依赖治理层的新说明。
  2. 把项目主页、项目结构页和 [[WORKFLOW]] 中这轮直接碰到的 [[BRAIN]]、[[POLICY]]、[[projects/decisions]] 等旧文件名字符串继续收成 [[wikilink]]，避免治理迁移后留下半旧半新的表达。
  3. 在项目层的“默认读取顺序”和“依赖关系”里补上新的治理入口，让后续处理项目记忆、规则和状态时，不再默认只按旧根目录路径理解治理页。
- **影响页面**：[[projects/README]]、[[projects/STRUCTURE]]、[[WORKFLOW]]、[[log]]。

### 把治理层正式收口成目录，并明确 `AGENTS` / `POLICY` 边界

- **用户意图**：确认之前关于“入口 / 治理 / 运行 / 沉淀 / 历史”等分层概念其实已经出现，但边界还不够清楚；同时质疑规则长期散落在根目录不合适，希望同时从逻辑结构和物理结构上把治理层收口，并明确 `AGENTS` 和规则层到底怎么分工。
- **主题**：
  1. 正式把文档系统分层明确成可复用的治理模型。
  2. 把治理层从根目录轻量收口到独立目录。
  3. 澄清 `AGENTS`、`POLICY`、`WORKFLOW`、`BRAIN` 的职责边界。
- **关键动作**：
  1. **主收口**：新增 [[governance/README]]，把整套系统正式定义成入口层、治理层、运行层、沉淀层、历史层、证据层六层模型，并把治理层的逻辑结构与物理结构统一写清。
  2. 将 [[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[log-writing-rules]]、[[trace-writing-rules]] 迁入 `governance/`，结束规则与写法指南继续散落在根目录的状态。
  3. 保留 [[AGENTS]] 在根目录作为 agent 的特殊入口，同时在 [[governance/README]] 和 [[AGENTS]] 中明确说明：[[POLICY]] 负责“怎么判”，[[AGENTS]] 负责“怎么执行”，[[WORKFLOW]] 负责“怎么推进”，[[BRAIN]] 负责“默认带什么背景”。
  4. 重写 [[README]] 和 [[INDEX]] 的入口说明，让总入口不再把治理页误写成根目录平铺页面，而是显式指向 [[governance/README]] 和新的治理层组织方式。
- **影响页面**：[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[BRAIN]]、[[POLICY]]、[[log-writing-rules]]、[[trace-writing-rules]]、[[log]]。

### 把 `[[projects/trace]]` 的人员与时间信息下沉到迭代级

- **用户意图**：指出同一个问题在 trace 过程中往往会有不同的人、不同时间参与，因此质疑当前把“记录人”放在主题主链顶层是否合理，希望把这部分设计调整到更贴近真实协作链路的版本。
- **主题**：
  1. 调整 trace 的人员信息落点。
  2. 调整 trace 的时间与角色信息落点。
- **关键动作**：
  1. **主调整**：在 [[trace-writing-rules]] 中把 `记录人` 从主题级默认字段改成迭代级默认字段，并明确主题级默认不写单个 `记录人`。
  2. 在 [[trace-writing-rules]] 和 [[templates/trace-entry-template]] 中补上迭代级 `角色` 字段，用于表达“产品 / 研发 / agent / 用户确认”等参与视角，但保持可选。
  3. 在 [[projects/trace]] 的现有示例中删掉主题级 `记录人`，改为在 `2026-04-12` 迭代块里写 `sunhao` 和 `agent`，让样例和新规则一致。
  4. 在 [[WORKFLOW]] 中同步把执行口径改成“人和更细时间默认落在迭代块”，避免后续写 trace 时再次漂回主题级。
- **影响页面**：[[trace-writing-rules]]、[[templates/trace-entry-template]]、[[projects/trace]]、[[WORKFLOW]]、[[log]]。

### 为 `[[projects/trace]]` 补齐记录人、日期和文字渲染规则

- **用户意图**：指出 trace 目前还缺少像 `[[log]]` 一样可直接执行的细节，包括人员信息记录、必要日期信息和文字渲染方式，希望把这些元信息和排版规则补到足够完善。
- **主题**：
  1. 为 trace 增加记录人与日期规则。
  2. 为 trace 增加和 `[[log]]` 一致的文字渲染约束。
- **关键动作**：
  1. **主补齐**：在 [[trace-writing-rules]] 中新增“记录人与日期怎么写”，明确记录人优先使用 `git user.name`，迭代块必须带日期，默认写到天，同日多次收敛时才升级到分钟。
  2. 在 [[trace-writing-rules]] 中新增“怎么做文字渲染”，把字段名加粗、短标签加粗、正文不整段加粗的约束补成显式规则，并和 `[[log]]` 保持一致。
  3. 在 [[templates/trace-entry-template]] 中补上“记录人”“YYYY-MM-DD 或 YYYY-MM-DD HH:mm”“主收敛 / 主替换 / 主纠偏”等写法，让模板可以直接套用。
  4. 按新规则回写 [[projects/trace]] 的现有示例，把 `sunhao`、字段加粗和重点短标签补齐，形成一个更可复用的样例。
- **影响页面**：[[trace-writing-rules]]、[[templates/trace-entry-template]]、[[projects/trace]]、[[WORKFLOW]]、[[log]]。

### 让 `[[projects/trace]]` 的文件、规则和模板对齐 `[[log]]` 的治理方式

- **用户意图**：要求 trace 的相关设计参考 `[[log]]`，尤其是文件职责、规则主入口和模板格式，不要让 trace 只有主文件，没有像 `[[log]]` 那样清晰的配套治理结构。
- **主题**：
  1. 为 trace 补齐规则主入口和模板入口。
  2. 把 `[[projects/trace]]` 收成“正文 + 跳转”的主文件形态。
- **关键动作**：
  1. **主收口**：新增 [[trace-writing-rules]]，把 `[[projects/trace]]` 的记录单位、续写旧主题与新开主题的边界、以及和 `[[log]]` / [[projects/decisions]] / [[projects/memory/README]] 的分工统一迁过去。
  2. 新增 [[templates/trace-entry-template]]，给需求演进链提供可直接复用的主链模板和迭代块模板，并在 [[templates/README]] 中补入口。
  3. 把 [[projects/trace]] 自身收短成主文件，只保留职责说明、规则跳转、模板跳转和当前主题正文，不再在主文件里重复展开完整写法。
  4. 在 [[README]]、[[INDEX]] 和 [[WORKFLOW]] 中补上 trace 规则入口和模板入口，保持和 `[[log]]` 同样的治理模式。
- **影响页面**：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[projects/trace]]、[[trace-writing-rules]]、[[templates/trace-entry-template]]、[[templates/README]]、[[log]]。

### 为项目层新增 `[[projects/trace]]` 需求演进链

- **用户意图**：确认当前体系可以正式新增 trace 链路，并要求按结构性扩展的标准全面整改，让项目推进里“产品梳理、技术选型、架构设计、功能设计到 agent 开发”的链路有一个明确落点，而不是继续只靠 `[[log]]` 和零散项目页承接。
- **主题**：
  1. 为项目运行层新增需求演进链主入口。
  2. 同步更新规则、流程、入口和项目结构，让 trace 成为正式职责。
- **关键动作**：
  1. **主新增**：新建 [[projects/trace]]，把它定义成项目层里记录原始意图、约束变化、修补性需求、关键决策变化和最终实现口径的主文件。
  2. 在 [[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]] 中同步补上 trace 的职责、边界和路由，明确它不是第二份 `[[log]]`，也不是第二份 `[[projects/decisions]]`。
  3. 在 [[projects/README]]、[[projects/STRUCTURE]]、[[projects/requirements]]、[[projects/design/README]]、[[projects/decisions]]、[[projects/development/README]]、[[projects/development/execution/worklog]] 和 [[projects/memory/README]] 中补上 trace 的入口、依赖关系和读取顺序。
  4. 把当前文档系统项目自身的“从知识库底座到项目运行链路”的收敛过程写成 [[projects/trace]] 的首条主题，给后续使用留一个最小样例。
- **影响页面**：[[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/requirements]]、[[projects/trace]]、[[projects/design/README]]、[[projects/decisions]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/memory/README]]、[[log]]。

### 区分 `[[log]]` 与需求演进 trace，并把收尾模式补成显式协议

- **用户意图**：确认 `[[log]]` 和需求演进 trace 是否其实是同一件事；如果不是，就说明差别在哪里。同时判断现有“收尾”是否已经足够稳，如果还能更稳，就把收尾流程补成更明确的执行协议。
- **主题**：
  1. 说明 `[[log]]` 与需求演进 trace 的职责边界。
  2. 把“收尾”从隐含习惯补成显式模式。
- **关键动作**：
  1. **主澄清**：确认 `[[log]]` 仍然是按对话组织的主题化历史，重点回答“这轮对话在解决什么”；而需求演进 trace 如果将来要加，会更偏向“需求如何从原始意图一路收敛到最终实现”，两者不是同一层信息。
  2. 在 [[AGENTS]] 中新增收尾模式硬约束，明确只有用户明确下达“收尾 / 执行收尾 / finalize”这类执行命令才进入收尾模式，而且进入后不再继续扩需求或顺手开发。
  3. 在 [[WORKFLOW]] 中补一段“收尾怎么执行”，把范围确认、同步、`[[log]]` 补记、一致性检查和提交顺序写成显式步骤。
  4. 同时把“预存脏改动默认不纳入本次收尾”补成执行边界，避免收尾时误把别的主题一起打包提交。
- **影响页面**：[[AGENTS]]、[[WORKFLOW]]、[[log]]。

### 明确 `[[log]]` 单日内部的记录顺序也要按降序维护

- **记录人**：sunhao
- **用户意图**：确认 `[[log]]` 不只是日期分组按降序，同一天内部的多条对话记录也应保持最新在前，避免日期降序了但单日内部仍按正序追加，导致阅读顺序不一致。
- **主题**：
  1. 明确 `[[log]]` 的排序规则需要同时覆盖“日期层”和“单日内部层”。
  2. 把单日内部也按降序维护补成显式规则。
- **关键动作**：
  1. **主澄清**：在 [[log-writing-rules]] 中补上两层排序规则，明确日期按降序，同一天内部的多条记录也按降序，最新完成或最新补写的那条放最前面。
  2. 在 [[WORKFLOW]] 中同步补一句执行口径，明确当天如果新增记录，应直接插到该日期下面最前面。
  3. 在 [[templates/log-entry-template]] 中把说明改成“同一天可以有多条，且当天最新的一条放最前面”，避免模板使用者只看到“同一天可以有多条”，却没看到内部排序要求。
  4. 在 [[AGENTS]] 中把 `[[log]]` 的职责描述也补成同一句话，确保规则层、流程层和模板层口径一致。
- **影响页面**：[[log-writing-rules]]、[[WORKFLOW]]、[[templates/log-entry-template]]、[[AGENTS]]、[[log]]。

### 收紧 `[[log]]` 的文字强调方式，避免加粗过度

- **记录人**：sunhao
- **用户意图**：明确 `[[log]]` 在文字渲染上还能怎么提升，并判断“主题”“关键动作”等字段是否适合加粗；目标是提升扫读效率，但不把页面做成一片高亮噪声。
- **主题**：
  1. 明确哪些位置适合加粗，哪些位置不适合。
  2. 把文字强调方式补成可复用的轻量规则。
- **关键动作**：
  1. **主判断**：确认字段名和关键动作短标签加粗是合适的，因为它们能提升扫描速度，但整句整段加粗不合适，会把真正的重点冲淡。
  2. 在 [[log-writing-rules]] 中新增“怎么做文字强调”，把字段名加粗、短标签加粗、正文不整段加粗写成明确约束。
  3. 在 [[templates/log-entry-template]] 中把“记录人 / 用户意图 / 主题 / 关键动作 / 影响页面”改成加粗字段名，同时把关键动作示例改成加粗短标签。
  4. 在 [[WORKFLOW]] 中同步补一条执行口径，明确 `[[log]]` 只做轻量强调，不做整段粗体。
- **影响页面**：[[log-writing-rules]]、[[templates/log-entry-template]]、[[WORKFLOW]]、[[log]]。

### 增强 `[[log]]` 单条记录内部的重点呈现方式

- **记录人**：sunhao
- **用户意图**：让 `[[log]]` 的每条记录在内部更容易一眼看到重点，而不是字段齐全但读者还要自己再提炼；同时避免为了强调重点而把模板继续写重。
- **主题**：
  1. 明确 `[[log]]` 重点应主要靠顺序和首条信息来突出。
  2. 为模板和流程补上可直接执行的“重点写法”。
- **关键动作**：
  1. **主收口**：在 [[log-writing-rules]] 中新增“怎么把重点写出来”，明确标题写主变化、主题按重要性排序、关键动作第 1 条先写主结果。
  2. 在 [[templates/log-entry-template]] 中把“用户意图”“主题”“关键动作”的默认写法改成更强调重点的版本，要求主题第 1 条先写核心主题、关键动作第 1 条先写主决定 / 主修正 / 主收口。
  3. 在 [[WORKFLOW]] 中同步补一条执行口径，明确写 `[[log]]` 时优先靠顺序来强调重点，而不是再增加一层新字段。
- **影响页面**：[[log-writing-rules]]、[[templates/log-entry-template]]、[[WORKFLOW]]、[[log]]。

### 修正 `[[log]]` 的过度合并，并补上长期防线

- **用户意图**：解决“4 月 12 日被压成单条总记录”的问题，区分“防碎片重复”和“防按天汇总化”这两类约束，让后续写 `[[log]]` 时既不碎，也不把同日多轮对话压扁。
- **主题**：
  1. 明确同一天、同文件、同领域都不是自动合并理由。
  2. 为 `[[log]]` 增加“过度合并”风险信号和新开记录触发条件。
  3. 把 2026-04-12 从单日总记录拆回多条真实对话记录。
- **关键动作**：
  1. **主修正**：在 [[AGENTS]] 中补成硬约束，明确日期只是分组容器，不是合并单位；同一天、同文件、同领域都不能自动合并。
  2. 在 [[AGENTS]] 中新增一条反向检查：如果合并后只能用“完善 `[[log]]`”“继续调整规则”这类宽标题概括，说明已经合并过度，应拆回多条。
  3. 在 [[log-writing-rules]] 中补充“过度合并的风险信号”“同日记录怎么判断”，并明确从“实施改动”切换到“解释为什么前一条写错、为什么会漏、怎样长期避免”时，通常应新开记录。
  4. 在 [[WORKFLOW]] 的 `[[log]]` 写法里补一条执行检查，要求开始解释上一条为什么写错或怎样长期避免时，不再并到旧记录里。
  5. 重写 2026-04-12 的 `[[log]]` 样例，把此前被压成一天一条的总括记录拆回多条按对话组织的记录。
- **影响页面**：[[AGENTS]]、[[log-writing-rules]]、[[WORKFLOW]]、[[log]]。

### 判断最近被拆开的 `[[log]]` 记录其实应当回并，并沉淀“完善优先”规则

- **用户意图**：解决最近两条记录明明在说同一件事，却因为后续补充和命名收口被拆成相邻两条的问题；让 `[[log]]` 在“补旧记录”和“新开记录”之间有更稳定的判断顺序。
- **主题**：
  1. 下游处理“上一条的补完”与“新的独立对话”之间的边界。
  2. 防止相邻两条记录各承接同一意图的不同碎片。
- **关键动作**：
  1. **主回并**：回看最近两条关于“记录人”字段的 `[[log]]` 记录，确认它们本质上属于同一条日志治理意图，于是合并为同一条记录。
  2. 在 [[log-writing-rules]] 中新增“完善优先规则”，要求在新开记录前先判断这次是不是只在纠正、补全、收短、重命名或格式化上一条记录。
  3. 在 [[log-writing-rules]] 中补充“什么时候必须新开记录”和“完整但不重复”，把“记录完善”与“相邻不重复”拆开表述。
  4. 在 [[WORKFLOW]] 中同步收紧执行口径：如果这次只是对上一条相关记录的补完、纠偏、重命名、格式统一或样例同步，优先直接完善旧记录。
- **影响页面**：[[log]]、[[log-writing-rules]]、[[WORKFLOW]]。

### 收紧 `[[log]]` 的编号模式、模板唯一正文和内部链接检查

- **用户意图**：修正 `[[log]]` 写法里仍然存在的格式漂移、模板重复和内部链接失效问题，并把这些问题变成交付前就会被拦下来的硬约束。
- **主题**：
  1. 把主题和关键动作的列表编号模式从示例提升成规则。
  2. 清掉模板正文重复，恢复模板页的单一信息源。
  3. 修正内部页面引用不能点击的问题，并把它升级成检查项。
- **关键动作**：
  1. **主收口**：把“主题”和“关键动作”统一收成编号列表，并同步更新 [[log]]、[[WORKFLOW]] 和 [[templates/log-entry-template]] 的写法。
  2. 删掉 [[log]] 和 [[WORKFLOW]] 中重复展开的模板正文，只保留规则说明和对 [[templates/log-entry-template]] 的跳转。
  3. 把模板入口中那些纯文本文件名或反引号文件名改成真正可点击的 `[[wikilink]]`。
  4. 在 [[AGENTS]] 和 [[WORKFLOW]] 中新增专项检查，明确禁止复制第二份模板正文，并要求凡是语义上在引用本库页面、模板页、入口页或跳转目标，都必须写成 `[[wikilink]]`。
  5. 同时追查最近几轮实际有变更却没同步写入 `[[log]]` 的遗漏，并把“有实际内容或结构变更就必须同步更新 `[[log]]`”明确写进 [[AGENTS]] 与 [[WORKFLOW]]。
- **影响页面**：[[log]]、[[templates/log-entry-template]]、[[WORKFLOW]]、[[AGENTS]]。

### 回填近期 `[[log]]` 历史，并明确跨日期的延续、重开和回填边界

- **用户意图**：解决最近几轮记录漏写、错位到 2026-04-12 名下，以及跨日期时“应该回并旧记录还是新开当天记录”的判断混乱。
- **主题**：
  1. 追补近期漏记和错位的历史记录。
  2. 明确跨日期时的延续、重开和回填边界。
- **关键动作**：
  1. **主回填**：把前几天真实发生的修正按原始对话日期回填，而不是继续误记在 2026-04-12 名下。
  2. 在 [[log-writing-rules]] 中把“延续 / 重开 / 回填”从隐含习惯补成显式边界，明确跨日期默认在当天新增记录。
  3. 只有在纠正旧记录日期归属或补记本来就属于当时那轮对话的遗漏内容时，才按回填处理。
  4. 顺手整合错位、重复和分散的旧记录，减少历史里因为日期判断不清造成的噪声。
- **影响页面**：[[log]]、[[log-writing-rules]]、[[WORKFLOW]]。

### 抽出 `[[log]]` 的完整规则主入口，并补齐合并与拆解标准

- **用户意图**：把 `[[log]]` 从“历史页里夹着规则说明”的状态，收口成“历史页只放历史、规则页专门讲写法”的结构；同时让合并与拆解不再靠临场感觉。
- **主题**：
  1. 为 `[[log]]` 建立唯一规则入口。
  2. 把记录级合并与主题级合并拆成两层判断。
- **关键动作**：
  1. **主建模**：新建 [[log-writing-rules]]，把 `[[log]]` 的记录单位、合并与拆解标准、记录级 / 主题级判断统一迁过去，作为唯一主入口。
  2. 把 [[log]] 顶部从完整规则正文收短成历史页说明，只保留对 [[log-writing-rules]] 和 [[templates/log-entry-template]] 的跳转。
  3. 在 [[log-writing-rules]] 中把判断标准明确成“用户意图、主结果、因果链和回看成本”，不再只靠隐含口径。
  4. 同步收短 [[WORKFLOW]] 与模板入口里的重复展开，让规则、模板、历史三层职责重新归位。
- **影响页面**：[[log]]、[[log-writing-rules]]、[[WORKFLOW]]、[[templates/log-entry-template]]、[[README]]、[[INDEX]]。

### 为 `[[log]]` 增加记录人字段，并统一字段命名

- **记录人**：sunhao
- **用户意图**：让 `[[log]]` 在需要时能标明记录人，但来源要稳定、可迁移，不回退到本机用户名；同时把字段命名收成一个一致版本。
- **主题**：
  1. 为 `[[log]]` 增加“记录人”字段，并把来源收口到 `git user.name`。
  2. 把字段命名从“记录人（可选）”收成“记录人”。
- **关键动作**：
  1. **主收口**：确认当前仓库的 `git user.name` 为 `sunhao`，适合作为 `[[log]]` 中“记录人”字段的默认来源。
  2. 在 [[log-writing-rules]] 中补充记录人规则，明确需要标注时优先写 `git user.name`；如果仓库没有配置，就留空，不回退到本机用户名。
  3. 在 [[templates/log-entry-template]] 中加入“记录人”字段，并补充使用说明。
  4. 把 [[log-writing-rules]]、[[templates/log-entry-template]] 和示例记录里的字段名统一收成“记录人”，不再把“可选”写进正文。
- **影响页面**：[[log-writing-rules]]、[[templates/log-entry-template]]、[[log]]。

### 为批量同类材料增加轻量批处理模式

- **用户意图**：在不降低质量的前提下，减少批量处理同类材料时重复读取同一组入口页的成本，让 agent 能先做一轮全局校准，再在同批材料上复用。
- **主题**：
  1. 为高频同类材料处理增加轻量路径。
  2. 明确什么时候必须退出批处理模式，回到完整上下文判断。
- **关键动作**：
  1. **主新增**：在 [[AGENTS]] 中新增“批处理模式”，明确适用范围、退出条件和禁止场景。
  2. 在 [[WORKFLOW]] 中新增“轻量批处理模式”，把批次级校准、共享读取和升级回默认流程的顺序写清楚。
- **影响页面**：[[AGENTS]]、[[WORKFLOW]]。

## 2026-04-11

### 修正 `[[log]]` 的记录粒度和动作完整度

- **用户意图**：让 `[[log]]` 既能提炼用户真正想解决的问题，又不要因为过度摘要而丢掉关键改动；同时明确每次对话都要有一个主题或多个主题，只是不必把每个问题拆开单记。
- **主题**：
  1. 把 `[[log]]` 的记录单位从“按天压成一个主题”改成“按对话记录”。
  2. 恢复 `[[log]]` 历史条目中过度压缩的修改动作细节。
- **关键动作**：
  1. **主修正**：重写 `[[log]]`、[[WORKFLOW]]、[[POLICY]]、[[AGENTS]]、[[README]]、[[INDEX]]、[[BRAIN]] 和模板文件中关于 `[[log]]` 的定义，明确记录单位是“每次对话”，同一天可以有多条记录，一次对话可以包含一个或多个相关主题。
  2. 补充 [[log]] 和 [[templates/log-entry-template]] 的条目骨架，把“对话”“主题”“用户意图”“关键动作”“影响页面”固定成默认结构。
  3. 回填历史条目时恢复更完整的动作列表，避免只剩笼统摘要。
- **影响页面**：[[log]]、[[WORKFLOW]]、[[POLICY]]、[[AGENTS]]、[[README]]、[[INDEX]]、[[BRAIN]]、[[templates/log-entry-template]]。

### 重构 `[[log]]` 的记录模型

- **用户意图**：让 `[[log]]` 不再只记“改了什么”，而是能回看用户这轮真正想解决的问题；记录顺序改为时间降序；提问内容按主题提炼，不机械抄写所有问句。
- **主题**：
  1. 让 `[[log]]` 从动作流水改成带用户意图的主题化记录。
- **关键动作**：
  1. **主重构**：重写 `[[log]]` 的说明和历史条目结构，把记录口径收成“主题 + 用户意图 + 关键动作 + 受影响页面”。
  2. 同步更新 [[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/README]] 对 `[[log]]` 的职责描述。
  3. 新增 [[templates/log-entry-template]]，并在 [[log]] 与 [[WORKFLOW]] 中补入推荐骨架，方便后续直接套用。
- **影响页面**：[[log]]、[[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/README]]、[[templates/log-entry-template]]。

### 把角色和 memory 的说明上提到根入口

- **用户意图**：纠正角色 / memory 说明的位置，把框架级解释放在最外层，而不是项目层。
- **主题**：
  1. 角色分层和 memory 分层的关系。
  2. 框架级说明的最终落点。
- **关键动作**：
  1. **主上提**：先在项目层尝试承接 role / memory 说明，随后把解释性内容从 `projects/memory/` 和 `projects/design/memory/` 中移出，最终放到根 `README.md`。
  2. 同时在 [[BRAIN]] 和 [[POLICY]] 增加边界说明，让框架级说明、共享背景和规则层各自归位。
  3. 让 `projects/design/memory/README.md` 只保留研究入口，不再承接框架正文。
  4. 把 2026-04-10 的初次讨论和这次最终纠正合并成连续历史，不重复记两套正文。
- **影响页面**：[[README]]、[[BRAIN]]、[[POLICY]]、[[projects/design/memory/README]]。

## 2026-04-10

### 确认 memory 沉淀的边界和从 log 到 memory 的提炼方式

- 用户意图：确认当前版本能否记录每次对话，并经过合适流程沉淀到 memory；进一步确认 memory 是否会自动从 log 抽取信息更新各层记忆。
- 主题：
  1. 多轮对话与 memory 的沉淀边界。
  2. `log -> memory` 是否自动同步。
- 关键动作：
  1. 明确当前体系可以记录对话过程，但长期沉淀只接受被提炼后的稳定背景、规则和项目记忆，不保留逐字聊天全文。
  2. 明确 `log` 只承担过程记录与时间线，不会自动驱动各层 memory 更新；从 `log` 到 `BRAIN`、`POLICY`、`projects/memory` 的迁移需要先判断晋升条件，再回写。
  3. 把“可以从对话里提炼稳定信息沉淀到 memory”与“自动全文抽取并同步”区分开，避免把 `log` 误解为自动同步源。
- 影响页面：[[log]]、[[BRAIN]]、[[POLICY]]、[[projects/memory/README]]。

### 收紧内部页面引用格式并修正 wikilink 渲染与 README 首章结构

- 用户意图：把 Markdown 内部页面引用收紧成真正可执行的硬约束，并修掉规则页和入口页里那些“看起来像链接但实际上不能点”的写法；同时把 README 第一章节里目录层和根目录页面混排的问题整理成统一格式。
- 主题：
  1. 强化内部页面引用格式约束。
  2. 修正 wikilink 被代码化或写成裸文件名导致的渲染问题。
  3. 统一 README 首章的目录层与根目录页面表达。
- 关键动作：
  1. 在 [[AGENTS]]、[[WORKFLOW]] 和 [[POLICY]] 中补强内部页面引用规则，明确本库页面、入口页、模板页和跳转目标必须使用 `[[wikilink]]`，禁止保留内部 `.md` 链接、本机绝对路径、空链接、占位链接和裸文件名。
  2. 补充一条更细的执行约束：如果语义上是在引用本库页面，就不能把 `[[wikilink]]` 再包进反引号；只有把 `[[wikilink]]` 当作语法示例时，才允许保留代码样式。
  3. 修正 [[POLICY]]、[[BRAIN]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/policy-links]]、[[projects/memory/shared]] 和 [[projects/requirements]] 中被反引号包住、导致不渲染的 wikilink，以及写成裸文件名的内部页面引用。
  4. 回看主 [[README]] 的入口说明，把“页面入口”统一改成可点击的 `[[wikilink]]`，让 [[WORKFLOW]]、[[AGENTS]]、[[INDEX]]、[[log]] 等入口的表现与 [[BRAIN]]、[[POLICY]]、[[projects/memory/README]] 保持一致。
  5. 继续收口 [[README]] 第一章节，把“目录层”和“根目录页面”拆成两组，避免在同一列表里混写目录与页面入口，造成格式和语义不统一。
- 影响页面：[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]、[[README]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/policy-links]]、[[projects/memory/shared]]、[[projects/requirements]]。

### 把项目运行层收口到更清晰的状态与功能点模型

- 用户意图：在前一天已经完成首轮 memory 分层的基础上，把“最小改造方案”剩余缺口补齐，让项目状态、功能点推进、角色分层和运行层入口的口径一致，减少“进行中”这类模糊状态在不同页面里互相污染。
- 主题：
  1. 补齐分层 memory 最小改造方案的剩余部分。
  2. 对齐项目状态、功能点推进和角色分层的口径。
  3. 继续收紧运行层入口、规则桥接和写作边界。
- 关键动作：
  1. 对齐最小改造方案的剩余缺口，保留并恢复 `projects/design/memory/` 作为研究层，新增 `projects/status.md` 作为项目状态页，并把“研究层 / 运行层”拆分正式落地到项目结构中。
  2. 给项目主页、需求页、设计入口、决策页、发布页、开发入口、共享记忆页等核心页面补齐可机读的 frontmatter，让 agent 后续可以读 `type / id / status / stage / source_of_truth` 这类字段，而不只是读正文。
  3. 强化 [[POLICY]]，明确默认不自动晋升、晋升条件、只有拍板后才进入 policy，以及冲突不直接覆盖的固定流程。
  4. 在 `projects/memory/` 增加 `policy-links.md` 作为运行层到规则层的桥接页，并同步更新 [[projects/README]]、[[projects/STRUCTURE]] 和 [[README]] 的入口说明。
  5. 强化 Markdown 引用约束，统一 vault 内页面引用必须使用 `[[wikilink]]` 及其变体，禁止继续保留内部 `.md` 链接、本机绝对路径、空链接和占位链接，并把引用校验加入 [[WORKFLOW]] 的交付前必检项。
  6. 把功能点推进流程正式沉淀到项目层，[[WORKFLOW]] 补了功能点状态机，[[projects/development/README]] 和 [[projects/development/execution/worklog]] 补了模板与示例，[[projects/status]] 变成全局状态镜像，`projects/memory/`、[[projects/decisions]] 和 [[projects/README]] 也同步收口了对应入口。
  7. 把开发示例独立成 `projects/development/examples.md`，并把 [[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/STRUCTURE]]、[[projects/README]] 和 [[WORKFLOW]] 的示例入口同步改为指向该文件。
  8. 把功能点管理从单字段 `in_progress` 改成双轴模型，由 `status` 管生命周期、`phase` 管串联步骤；同时把开发入口、示例页、工作日志、状态页、决策页和项目记忆页都同步沉淀，避免设计、实现、验证混写在一个字段里。
  9. 进一步把项目级状态和功能点双轴分开，让项目入口只保留项目级状态词，功能点推进统一用 `status + phase`，避免不同层级的“进行中”概念互相污染。
  10. 明确功能点卡的最小填写要求，每张卡都必须同时写 `status` 和 `phase`，不能只留一个“进行中”的笼统字段；并把这条约束写进项目共享背景。
  11. 把过程记录也同步拆轴，让 [[projects/development/execution/worklog]] 分开记录 `status` 变化和 `phase` 变化，避免把两条线重新揉回 `in_progress`。
  12. 把开发示例进一步显式化，同时展示进行中、完成待发布、已发布三种卡片，并把已发布示例的阶段口径收口到 `release`。
  13. 把开发示例从“同页多卡”进一步拆成真实功能点实体页，新增 `projects/development/feature-points/` 目录，拆出 `README.md` 索引页和 `FP-001.md`、`FP-002.md`、`FP-003.md` 三个实体页；同时把 [[WORKFLOW]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/decisions]]、[[projects/memory/shared]] 和 [[AGENTS]] 的口径一起改成实体页优先。
  14. 进一步把 [[projects/development/README]] 收成研发经理看板，移走状态轴、阶段轴、实体模板和当前实体清单；把这些执行细节集中到 [[projects/development/feature-points/README]]，让开发主入口只负责整体推进、阻塞、下一步和协调。
  15. 把目录入口标题统一收成中文，并补了一条写作约定：正文默认中文，英文只保留文件名、产品名、代码标识和必要术语；继续把说明性英文收口为中文表达，不动历史事实记录。
  16. 把随意中英混排正式沉淀为 [[AGENTS]] 的硬约束，延续同一天前面的正文中文化收口，把规则明确成后续新增或修改内容都要检查的维护约束。
- 影响页面：[[projects/status]]、[[projects/memory/README]]、[[projects/memory/policy-links]]、[[projects/design/memory/README]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/development/feature-points/README]]、[[projects/README]]、[[projects/STRUCTURE]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]、[[AGENTS]]。

## 2026-04-09

### 把文档库从“文件集合”收口成有上下文模型和 memory 分层的系统

- 用户意图：在不推翻现有骨架的前提下，把这套库从“可用的文档系统”进一步收口成未来可自动运行的文档操作系统；后续更新不再只盯着当前文件，而是先判断模式、阶段、主入口、上下游和受影响页面，并把规则、背景、项目记忆分层放稳。
- 主题：
  1. 建立全局背景优先、上下文模型和结构变更同步规则。
  2. 把 memory 路由拆成共享背景、规则层和项目记忆三层。
  3. 用最小改造而非重构的方式，给后续 agent 自动化预留机器可读入口。
- 关键动作：
  1. 增加“全局背景优先”规则，要求更新任何内容时，不只看当前文件，还要先判断它在整个 vault 中的模式、阶段、主入口、影响范围和知识层级。
  2. 将“上下文”进一步定义为主入口、上下游文件、阶段位置、知识层级和受影响页面的组合，并为项目页、需求、设计、决策、知识页、索引页分别补入最小读取集与演进链路。
  3. 增加“结构变更同步”规则，以后只要新增模块、目录、模板、入口页或新的高频文件类型，就必须在同一次变更里同步更新上下文模型、关联关系、最小读取集和日志。
  4. 收紧提交和规则治理，明确 commit 只针对实际内容或结构变更；本地状态和缓存不进正式提交；新增规则时优先修改旧规则，避免继续把系统写重。
  5. 收紧 [[projects/README]] 的表达方式，保留项目运行层定义，不再显式强调是否已进入正式项目阶段，让内容本身决定页面所处状态。
  6. 收口研发阶段说明，把阶段映射、推进方法和从零做系统的详细说明统一收回 [[WORKFLOW]]，让 [[README]] 和 [[projects/README]] 只保留摘要和跳转，避免重复维护。
  7. 清理文档中的本机绝对路径，让仓库内链接统一改为相对路径，环境说明改为“当前工作区 / 当前 vault”，避免换电脑后链接失效。
  8. 增加链接约束，要求同一 vault 内的页面跳转默认使用 `[[wikilink]]`，外部资源继续使用 Markdown 链接，长期文档禁止写死本机绝对路径。
  9. 增加“AI 功能研发工作流”，在 [[WORKFLOW]] 中补入功能从需求到上线的最小闭环，以及“什么时候补文档、什么时候直接写代码”的判断标准。
  10. 将项目层的结构说明单独抽到 [[projects/STRUCTURE]]，把目录、文件职责、依赖关系和默认读取顺序收口成一个主页面，避免继续把结构和流程堆在同一页。
  11. 明确项目层的目录规则，要求现有内容优先保留；已经形成多文件职责的模块继续保留目录；只有一个 `README.md` 的子目录才优先收平成单文件。
  12. 澄清设计层口径，让 `design/README.md` 成为设计主入口，`architecture.md`、`database.md` 成为设计子页，而不是并列的第二份“设计”。
  13. 按统一规则实际创建项目层文件：`requirements.md`、`design/README.md`、`design/architecture.md`、`design/database.md`、`decisions.md`、`development/README.md`、`development/worklog.md`、`releases.md`、`incidents.md`。
  14. 将事故层调整为目录结构，让 `incidents/README.md` 负责总览和整体状态，每一次事故单独成文件，避免把多次事故堆在同一页。
  15. 为设计层补出显式的技术选型文件 `design/tech-selection.md`，避免把技术选型长期埋在设计总览里。
  16. 引入 [[BRAIN]] 作为共享脑，承接跨多轮确认、后续应自动进入思考背景的内容；同时明确 [[AGENTS]]、`workspace-memory`、[[projects/decisions]]、[[log]] 的分工。
  17. 将“分层 memory 研究”先沉淀到项目设计层，新增 `design/memory/README.md` 和 `design/memory/tools.md`，随后又调整其落点，把这部分研究迁移到 `articles/` 和 `concepts/`，并清理 `projects/design/memory/` 空目录。
  18. 将 Obsidian 软件开发文档系统的整体设计沉淀到知识库层，新增 [[articles/2026-04-09-obsidian-doc-system-design]] 和 [[concepts/document-os]]，用于承接整体架构、无账号小团队约束、半自动到自动化路径，以及未来分层 memory 的文档化路线。
  19. 明确采用“最小改造方案”而不是整体重构：保留根层、项目层、知识层和输入层的现有骨架，不把系统推倒重来，而是在既有结构上补出更清晰的职责边界。
  20. 正式把 memory 路由分层，新增 [[POLICY]] 承接规则和优先级，新增 `projects/memory/` 承接项目级稳定记忆，收紧 [[BRAIN]] 只保留共享背景，并同步更新 [[README]]、[[INDEX]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]]、项目主页面、模板页、相关文章和概念页；同时确认 `log` 只保留过程记录，不会自动抽取并同步各层 memory，后续沉淀要先从 `log` / 对话中提炼再回写。
  21. 明确后续自动化真正依赖的是结构化字段而不只是目录名，因此开始把项目主页、需求页、设计入口、决策页、共享记忆页等核心页面补向可机读的 frontmatter 口径，为下一天继续补齐最小改造方案做准备。
- 影响页面：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]]、[[projects/README]]、[[BRAIN]]、[[POLICY]]、[[projects/memory/README]]、[[articles/2026-04-09-obsidian-doc-system-design]]、[[concepts/document-os]]。

## 2026-04-08

### 搭建 `wiki` 文档库底座并补齐最小维护流程

- 用户意图：先把这套库从零搭起来，让资料有入口、有层次、有维护动作，后续不管是知识沉淀还是研发推进都有可落脚的主结构。
- 主题：
  1. 初始化文档库底座和目录层级。
  2. 补齐从入口到流程的最小维护规则。
- 关键动作：
  1. 初始化 `wiki` vault。
  2. 配置 `Obsidian`、`Codex CLI`、`workspace-filesystem`、`workspace-memory`。
  3. 建立 [[README]]、[[WORKFLOW]]、`templates/`、`articles/`、`concepts/`、`indexes/`。
  4. 把后续维护改成 `raw/ -> articles/concepts/indexes -> log.md` 的持续编译流程。
  5. 补充文件与目录操作流程，包括新建目录、新建文件、修改文件、处理已有目录。
  6. 将“新目录 / 新文件 / 修改文件 / 目录复用 / 链接影响 / 记录日志”等关键判断前置到 [[README]] 和 [[INDEX]]，避免总入口过于隐蔽。
  7. 在总入口补充“怎么用这个 vault / 先看什么 / 常见操作对应关系 / 可直接复制的指令模板”，让 [[README]] 真正承担使用说明。
  8. 进一步明确 `raw/` 与 `inbox/` 的边界，补入 `assets/` 与 `archive/` 的生命周期规则，并把 `workspace-memory` 限定为稳定偏好而不是唯一规则源。
  9. 清理根目录两个空的 `canvas` 占位文件，改用 `assets/` 作为支持性可视化文件落点。
  10. 增加 `projects/` 作为活跃软件研发项目层，明确知识库模式是底座、研发模式是叠加层，并补出项目模板与项目运行说明。
  11. 为 `projects/` 补入手动流控、项目主页优先和活跃项目汇总入口的约定。
  12. 进一步收紧为极简小项目模式，默认一页项目主页加总日志，其他项目文件按需添加，不预建空结构。
  13. 把新建目录规则进一步改成“README 先行，模板和索引按需创建”，避免极简模式被默认的重结构约束反向拉重。
  14. 进一步把模板定位为加速器而非门槛，让项目主页可以直接手写，不必先复制模板。
  15. 把“研发推进的关键原则”单独沉淀到 [[projects/README]] 和 [[WORKFLOW]]，强调项目主页、代码仓库、问题定义、过程记录和知识回写这几条最重要的研发约束。
  16. 明确当前建模前提：一个 `wiki` 只对应一个项目，因此项目主页固定为 [[projects/README]]，不再采用 `projects/<项目名>/` 的多项目结构。
  17. 为 `projects/` 层补充“相关文件分别做什么”的说明，明确每个可选文件的职责、拆分时机和不拆分时机。
  18. 提升会话级更新规则，要求复杂问题拆成中间节点推进并分段提交；同类信息只保留一个主入口，禁止多处复制粘贴；修改前后都要按入口、主页面、相关跳转页的顺序读取和回看。
- 影响页面：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[projects/README]]、[[log]]、`templates/`、`articles/`、`concepts/`、`indexes/`。
