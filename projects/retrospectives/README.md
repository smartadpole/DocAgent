---
type: retrospective_index
id: PROJ-RETROSPECTIVE-INDEX-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-06-03
tags: [project, retrospective, learning-loop]
---

# 复盘档案

上游：[[projects/README]]、[[projects/trace]]、[[projects/decisions]]、[[projects/development/README]]、[[projects/development/issues/README]]、[[projects/incidents/README]]、[[log]]

方法入口：[[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]

模板：[[templates/project-retrospective-template]]

执行技能：[[skills/historical-dialogue-retrospective/SKILL]]

这页是当前项目的复盘档案入口。它负责把阶段、专题、事故后、Issue 后、交付链偏差和 Agent 协作偏差沉淀成可回看的学习资产，并把复盘结论分流到已有单一信息源。

复盘不是普通总结，也不是 [[log]] 的加厚版。复盘要把原始目标、实际结果、关键事实、偏差原因、保留做法、改进行动和沉淀路由串起来，让下一轮需求判断、方案设计、研发实践、工程治理、测试验收、运行质量和 Agent 工作方式都能复用这次经验。

## 这页负责什么

- 汇总当前项目内已经形成的复盘档案。
- 说明复盘文件落位、命名、粒度和最小字段。
- 维护跨复盘的共性主题、保留做法和改进方向。
- 把复盘行动分流到 Issue、事故、事项、会议、决策、memory、trace、模板、skill、sensor 或治理页。

## 这页不负责什么

- 不替代 [[log]]；log 记录对话主题、用户意图、关键动作和结构变化，复盘解释目标、事实、偏差、原因和可复用经验。
- 不替代 [[projects/development/issues/README]]；已发生 bug、偏差、验收失败先进入 Issue 案件档案。
- 不替代 [[projects/incidents/README]]；事故事实、影响、修复和恢复链先在事故主档案保真。
- 不替代 [[projects/development/reports/README]]；测试报告是验证证据，不是复盘。
- 不替代 [[projects/decisions]]；复盘可以提出决策候选，最终拍板仍进决策页。
- 不新建平行看板或平行动作看板；复盘行动项必须落到已有 owner 页面和可检查位置。

## 文件落位

具体复盘文件默认放在本目录。

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
| 标准复盘 | 阶段、专题、重要交付链、明显返工或验收偏差 | `projects/retrospectives/` |
| 深度复盘 | 跨阶段、重复失守、重大事故、会改变模板 / skill / 规则 / sensor 的经验 | `projects/retrospectives/`，并同步相关治理或项目主页面 |

## 当前复盘索引

暂无独立复盘档案。后续新增复盘文件时按时间降序补到这里。

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

## 维护说明

- 新复盘文件优先复制 [[templates/project-retrospective-template]]。
- 复盘结论如果改变需求主题，同轮更新 [[projects/trace]]。
- 复盘结论如果改变关键取舍，同轮更新 [[projects/decisions]]。
- 复盘结论如果是项目级稳定事实，同轮更新 [[projects/memory/README]]。
- 复盘结论如果是跨项目可复用方法，回写 [[concepts/project-retrospective]]、相关概念页或 `templates/`。
- 复盘结论如果暴露 agent / Harness 缺口，回写 [[harness-feedback-ledger]]，再按 [[harness-evolution]] 判断是否晋升。
- 维护本体系后运行 `python3 scripts/check_all.py --only retrospective-system`；提交前运行完整 `python3 scripts/check_all.py`。
