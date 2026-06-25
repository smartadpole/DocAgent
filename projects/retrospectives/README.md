---
type: retrospective_index
id: PROJ-RETROSPECTIVE-INDEX-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-06-25
tags: [project, retrospective, learning-loop]
---

# 复盘档案

上游：[[projects/README]]、[[projects/trace]]、[[projects/decisions]]、[[projects/development/README]]、[[projects/development/issues/README]]、[[projects/incidents/README]]、[[log]]

方法入口：[[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]

模板：[[templates/project-retrospective-template]]

复盘总技能：[[skills/retrospective-capability/SKILL]]

执行子项：[[skills/delivery-retrospective/SKILL]]、[[skills/historical-dialogue-retrospective/SKILL]]

存放结构：[[projects/design/topics/retrospective-archive-storage-structure]]

这页是当前项目的复盘 archive root。它负责说明复盘触发、正文落位、索引维护、文件爆炸控制、行动分流和 Harness 自演进关系；复盘正文只进入年份目录，不在 archive root 平铺。

复盘不是普通总结，也不是 [[log]] 的加厚版。复盘要把原始目标、实际结果、关键事实、偏差原因、保留做法、改进行动和沉淀路由串起来，让下一轮需求判断、方案设计、研发实践、工程治理、测试验收、运行质量和 Agent 工作方式都能复用这次经验。

## 系统运行闭环

当前复盘体系按五层运行：

1. **方法入口**：[[concepts/project-retrospective]] 定义复盘是什么、何时启动、和其他页面如何分工；软件研发和 Agent 工作分别看 [[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]。
2. **档案入口**：本页承接 archive root 规则、年份目录、索引入口、共性主题和沉淀路由；具体正文进入 `projects/retrospectives/<year>/`。
3. **执行骨架**：[[skills/retrospective-capability/SKILL]] 是复盘总技能，承接统一合同、子项路由、证据等级和行动兑现回检；项目交付 / 软件研发链复盘由 [[skills/delivery-retrospective/SKILL]] 执行，历史对话 / Agent 工作流复盘由 [[skills/historical-dialogue-retrospective/SKILL]] 执行。
4. **行动兑现回检**：标准 / 深度复盘开始前，先回检相关上一篇复盘的 open 改进行动是否兑现、是否 stale、证据在哪里、下一步落到哪个 owner 页。
5. **行动分流和自演进**：复盘行动项必须进入已有 owner 页面；重复失守、模板缺口、skill 缺口或可脚本化检查再进入 [[harness-feedback-ledger]] 和 [[harness-evolution]]。

这五层缺一不可：只有方法没有档案会变成口号，只有模板没有行动分流会变成报告存档，只有行动没有回检和自演进会让同类问题反复靠人工提醒。

## 显式复盘请求

用户明确要求“复盘 / 做复盘 / 写复盘 / 沉淀复盘 / 总结教训”时，默认按标准复盘处理，并默认落文件到 `projects/retrospectives/<year>/`。除非用户同时明确说“只口头 / 不写文件 / 先分析 / 只判断原因”，否则不能把显式复盘请求降级成只在回复里解释、只写 [[log]]，或只做轻量 checkpoint。

用户要求“深度复盘 / 完整复盘 / 全面复盘 / 复盘这段对话 / 分析为什么没自动做好 / 举一反三”时，进入显式深度复盘模式：深读历史、首轮目标和用户纠偏优先、产物即档案、上层抽象和举一反三是必做项。无法读取原始 session / rollout 或 memory 线索时，必须写入未验证边界。

如果用户只是问“为什么 / 在哪 / 先分析”，且没有要求复盘，才按 [[response-mode-routing]] 的快速诊断处理；若诊断后用户要求复盘，再回到本节默认落文件。

## 自动触发关系

复盘也不只靠用户显式说“复盘”。长 Goal、Run Capsule、多 agent、Loop iteration 或复杂规则升级收尾时，evaluator 必须按 [[skills/historical-dialogue-retrospective/SKILL#自动触发矩阵]] 判断：

- `no-op`：普通任务顺利完成，无结构性新信息，不新建复盘。
- `轻量复盘 checkpoint`：复杂运行顺利结束，只在 Closeout Proof、[[log]] 或 next-run decision 记录短判断。
- `标准复盘`：出现用户纠偏、返工、漏验证、漏提交、漏沉淀或 Worker 证据被打回，使用复盘技能完整框架。
- `深度复盘`：重复失守、sensor / 模板 / skill / rule 失效或 Loop evaluator 漏停，同步复盘档案、[[harness-feedback-ledger]] 和治理自演进。

自动触发只决定是否调用复盘技能，不自动覆盖显式复盘请求的默认落文件规则，不自动关闭项目事项、不替代 Issue / 事故主档案、不把行动项留在本目录。`no-op / 轻量复盘 checkpoint 只适用于自动触发判断`。

## 这页负责什么

- 汇总当前项目内已经形成的复盘档案。
- 说明复盘文件落位、命名、粒度、索引入口和最小字段。
- 维护跨复盘的共性主题、保留做法、改进方向和文件爆炸控制规则。
- 把复盘行动分流到 Issue、事故、事项、会议、决策、memory、trace、模板、skill、sensor 或治理页。

## 这页不负责什么

- 不替代 [[log]]；log 记录对话主题、用户意图、关键动作和结构变化，复盘解释目标、事实、偏差、原因和可复用经验。
- 不替代 [[projects/development/issues/README]]；已发生 bug、偏差、验收失败先进入 Issue 案件档案。
- 不替代 [[projects/incidents/README]]；事故事实、影响、修复和恢复链先在事故主档案保真。
- 不替代 [[projects/development/reports/README]]；测试报告是验证证据，不是复盘。
- 不替代 [[projects/decisions]]；复盘可以提出决策候选，最终拍板仍进决策页。
- 不替代 handoff；handoff 承接执行交接和临时证据，不能作为复盘正文或行动 owner。
- 不新建平行看板或平行动作看板；复盘行动项必须落到已有 owner 页面和可检查位置。

## 文件落位

Archive root 固定为 `projects/retrospectives/`：

```text
projects/retrospectives/
  README.md
  indexes/
    by-year.md
    by-theme.md
    by-type.md
  2026/
    README.md
    YYYY-MM-DD-topic.md
```

具体复盘正文默认放入对应年份目录，例如 `projects/retrospectives/2026/`。根目录只保留本入口、`indexes/` 和年份目录；不得把复盘正文平铺在 archive root。

建议命名：

- `YYYY-MM-DD-<topic>.md`
- `<topic>` 使用英文短横线命名，正文标题用中文说明真实复盘对象。

典型对象：

- **阶段复盘**：项目阶段、里程碑、发布准备或复杂验收结束后的复盘。
- **专题复盘**：需求收敛、架构方案、测试体系、agent 协作、治理改动等长期主题。
- **交付链复盘**：Gate / FP / EP / TASK、risk、issue、AP、report、发布和运行证据之间出现偏差时形成的复盘。
- **事故后复盘**：事故主档案仍在 [[projects/incidents/README]]；如果事故经验上升为跨事故、跨阶段学习，再在本目录写专题复盘并回链事故页。
- **Issue 后复盘**：Issue 主档案仍在 [[projects/development/issues/README]]；如果它暴露需求、设计、流程或治理机制缺口，再在本目录写复盘。
- **Agent 工作复盘**：当需要回看 agent 如何理解目标、读取上下文、执行、验证、沟通和沉淀时，使用 [[skills/historical-dialogue-retrospective/SKILL]]。

## 复盘粒度

不要把所有记录都升成复盘文件。默认按影响面决定：

| 粒度 | 适用场景 | 落位 |
| --- | --- | --- |
| 轻量 checkpoint | 单次小纠偏、无长期影响的小结 | [[log]]、相关工作记录或 owning page |
| 标准复盘 | 阶段、专题、重要交付链、明显返工或验收偏差 | `projects/retrospectives/<year>/`，并同步索引 |
| 深度复盘 | 跨阶段、重复失守、重大事故、会改变模板 / skill / 规则 / sensor 的经验 | `projects/retrospectives/<year>/`，并同步相关治理或项目主页面 |

## 索引入口

- [[projects/retrospectives/indexes/by-year]]：完整时间索引，按年份和日期列出复盘正文。
- [[projects/retrospectives/indexes/by-theme]]：主题索引，按复盘体系、Harness 治理、交付链、Agent 协作等长期主题组织。
- [[projects/retrospectives/indexes/by-type]]：类型索引，按项目交付、软件研发链、Agent 工作、Harness 自演进、Issue / 事故后专题等对象组织。

Archive root 不维护完整历史长列表。当前没有需要迁移的旧复盘正文；新增标准 / 深度复盘时先进入年份目录，再同步年度索引，必要时同步主题和类型索引。

## 文件爆炸控制

默认落文件不等于“一次信号一个复盘档案”。复盘文件只承接有长期学习价值的标准 / 深度复盘；同类轻量信号先聚合，不为每个纠偏、Issue、agent episode 或检查失败单独新建档案。

- **同源保留**：待复盘信息保留在原 owner 目录，Issue、事故、报告、会议、log、ledger、handoff 和 TASK 不搬进本目录，也不在本目录镜像一套同构子树。
- **聚合优先**：同一机制缺口下的多条信号优先合成一篇专题复盘；只有目标、证据链或 owner 明显不同，才拆成多篇。
- **队列轻量化**：待复盘候选先放在 owner 页、[[harness-feedback-ledger]]、[[log]] 或 Closeout Proof 中；没有形成标准 / 深度复盘合同前，不预建空正文。
- **索引分层**：本页只保留索引入口、当前重点和共性主题；完整清单按年度、主题和类型索引分组，主题 / 类型不做物理目录。
- **容量回检**：当某个年份目录或索引段落明显膨胀时，先回检同类档案是否应合并、索引是否应拆分，不把正文回退成根目录平铺。

## 共性主题

按需要维护：

- 需求和 trace 收敛质量。
- 设计方案和工程实现之间的偏差。
- Gate / FP / EP / TASK、risk、issue、AP、report 的事项关系质量。
- 测试、验收、发布和运行证据质量。
- Agent 协作的目标理解、阶段判断、读取预算、工具使用、验证和收尾质量。
- 治理规则、模板、技能和 sensor 的晋升 / 降级效果。

## 行动项分流

复盘行动项不能只停留在复盘正文里：

新建标准 / 深度复盘时，先用 [[templates/project-retrospective-template]] 的“上轮行动兑现回检”字段检查相关上一篇复盘的 open 行动。回检只记录状态和证据，不把复盘目录变成行动看板；需要继续推进的行动仍分流到下表 owner 页面。

| 行动类型 | 分流落点 |
| --- | --- |
| bug、实施偏差、验收失败 | [[projects/development/issues/README]] |
| 事故事实、修复闭环、恢复和回滚 | [[projects/incidents/README]]、[[projects/releases]] |
| 研发交付动作 | Gate / FP / EP / TASK、[[projects/development/risks/README]]、[[projects/development/acceptance/README]]、[[projects/development/reports/README]] |
| 跨 owner 协调、人工确认 | [[projects/meetings/README]] |
| 关键取舍 | [[projects/decisions]] |
| 项目长期事实 | [[projects/memory/README]] |
| 需求演进 | [[projects/trace]] |
| 可复用方法 | [[concepts/project-retrospective]] 或相关概念页 |
| 可复制骨架 | [[templates/README]] 和对应模板 |
| 高频 agent 流程 | [[skills/README]] 和具体 skill |
| 重复失守或机制缺口 | [[harness-feedback-ledger]] |
| 可脚本化检查 | `scripts/check_all.py` 或专项 sensor |
| 执行规则变化 | [[AGENTS]]、[[WORKFLOW]]、[[POLICY]] 或相关治理页 |

## 沉淀路由

- 项目事实留在项目层，优先回到事实主档案、trace、decisions、memory、reports 或 incidents。
- 可复用方法抽象后进入 `concepts/`、`templates/` 或 `skills/`。
- Agent / Harness 缺口先进入 [[harness-feedback-ledger]]，再按 [[harness-evolution]] 判断是否晋升。
- 规则变化先做冲突和单一信息源检查，必要时再更新 [[WORKFLOW]]、[[AGENTS]] 或 [[POLICY]]。
- 单次表现只记录复盘或 log，继续观察；不要把所有复盘结论都升级成硬规则。

## 治理自演进关系

复盘结论按影响面逐级上推：

- 单次表现：写入复盘或 [[log]]，保留未验证边界，继续观察。
- 重复失守：进入 [[harness-feedback-ledger]]，记录触发信号、成本类型、已采取改动和状态。
- 可模板化：更新 [[templates/project-retrospective-template]] 或相关模板字段。
- 可技能化：更新 [[skills/retrospective-capability/SKILL]]、[[skills/delivery-retrospective/SKILL]]、[[skills/historical-dialogue-retrospective/SKILL]] 或更窄子项技能。
- 可脚本化：新增或扩展 sensor，并接入 `scripts/check_all.py`。
- 影响执行顺序：更新 [[WORKFLOW]] 或 [[response-mode-routing]]。
- 影响必须 / 禁止行为：更新 [[AGENTS]]。
- 影响优先级、自动沉淀边界或裁定规则：更新 [[POLICY]]。

## 维护说明

- 新复盘文件优先复制 [[templates/project-retrospective-template]]，放入 `projects/retrospectives/<year>/`。
- 新标准 / 深度复盘必须同步 [[projects/retrospectives/indexes/by-year]]；如果有稳定主题或类型，同步 [[projects/retrospectives/indexes/by-theme]] 或 [[projects/retrospectives/indexes/by-type]]。
- 新复盘文件不得直接放在 `projects/retrospectives/` 根目录；维护后用 `python3 scripts/check_all.py --only retrospective-system` 检查。
- 复盘结论如果改变需求主题，同轮更新 [[projects/trace]]。
- 复盘结论如果改变关键取舍，同轮更新 [[projects/decisions]]。
- 复盘结论如果是项目级稳定事实，同轮更新 [[projects/memory/README]]。
- 复盘结论如果是跨项目可复用方法，回写 [[concepts/project-retrospective]]、相关概念页或 `templates/`。
- 复盘结论如果暴露 agent / Harness 缺口，回写 [[harness-feedback-ledger]]，再按 [[harness-evolution]] 判断是否晋升。
- 维护本体系后运行 `python3 scripts/check_all.py --only retrospective-system`；提交前运行完整 `python3 scripts/check_all.py`。
