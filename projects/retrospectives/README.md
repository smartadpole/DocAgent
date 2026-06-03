---
type: retrospective-index
project: wiki
status: active
source_of_truth: true
updated: 2026-06-03
tags: [project, retrospective, learning-loop]
---

# 复盘

上游：[[projects/README]]、[[projects/trace]]、[[projects/decisions]]、[[projects/development/README]]、[[projects/incidents/README]]、[[log]]

方法入口：[[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]

模板：[[templates/project-retrospective-template]]

这页是当前项目的复盘档案入口，负责承接具体复盘文件、跨复盘索引和复盘后的经验流向。

复盘不是普通总结，也不是 `[[log]]` 的加厚版。它是项目长期学习工程的一部分：把已经发生的目标偏差、设计取舍、执行成本、验证缺口、协作问题和有效做法，沉淀成未来需求判断、方案设计、研发实践、工程治理和 agent 协作都会用到的资产。

## 这页负责什么

- 汇总当前项目内已经形成的复盘档案。
- 说明复盘文件的命名、粒度和最小字段。
- 保持跨复盘的共性问题、保留做法和改进主题入口。
- 把复盘结论分流到项目记忆、trace、决策、设计、研发事项、Issue / 事故、模板、技能或治理规则。

## 这页不负责什么

- 不替代 [[log]]；`[[log]]` 记录对话主题和关键动作，复盘解释目标、事实、偏差、原因和可复用经验。
- 不替代 Issue 或事故主档案；已发生 bug、验收失败和事故先在 [[projects/development/issues/README]] 或 [[projects/incidents/README]] 保真。
- 不替代 [[projects/decisions]]；复盘可以提出决策候选，但最终拍板仍进决策页。
- 不替代 [[projects/memory/README]]；只有稳定、后续会自动参与判断的结论才回写项目记忆。
- 不新建平行动作看板；复盘行动项必须落到已有 owner 页面和可检查位置。

## 文件落位

具体复盘文件默认放在本目录。

建议命名：

- `YYYY-MM-DD-<topic>.md`
- `<topic>` 使用英文短横线命名，正文标题用中文说明真实对象。

典型对象：

- 阶段复盘：项目阶段、里程碑、发布准备、复杂验收结束后形成的复盘。
- 专题复盘：需求收敛、架构方案、测试体系、agent 协作、治理改动等长期主题。
- 事故后复盘：事故主档案保存在 [[projects/incidents/README]] 下；如果事故经验上升为跨事故、跨阶段学习，再在本目录写专题复盘并回链事故页。
- Issue 后复盘：Issue 主档案保存在 [[projects/development/issues/README]] 下；如果它暴露需求、设计、流程或治理机制缺口，再在本目录写复盘。

## 粒度

不要把所有记录都升成复盘文件。默认按影响面决定：

| 粒度 | 适用场景 | 落位 |
| --- | --- | --- |
| 轻量 checkpoint | 单次小纠偏、无长期影响的小结 | [[log]]、相关工作记录或 owning page |
| 标准复盘 | 阶段、专题、重要交付链、明显返工或验收偏差 | `projects/retrospectives/` |
| 深度复盘 | 跨阶段、重复失守、重大事故、会改变模板 / skill / 规则的经验 | `projects/retrospectives/`，并同步相关治理或项目主页面 |

## 最小字段

每个复盘文件至少包含：

- **复盘对象**：复盘的是哪段时间、哪个阶段、哪条交付链、哪个事故 / issue 或哪个 agent 协作过程。
- **原始目标**：当时真正想达成什么，明确非目标和约束。
- **实际结果**：已经完成、未完成、偏离、降级、超出预期和仍有风险的部分。
- **关键事实**：时间线、证据、报告、diff、会议、决策或用户纠偏。
- **偏差与原因**：区分事实偏差、判断偏差、设计偏差、执行偏差、验证偏差和协作治理偏差。
- **保留做法**：下次应该继续使用的结构、工具、流程、模板、检查或协作方式。
- **改进行动**：每条都写清 owner、落点、完成口径和检查方式。
- **沉淀路由**：写明哪些进入项目记忆、trace、决策、设计、事项、Issue / 事故、模板、skill、治理页或暂不落地。

## 当前索引

暂无独立复盘档案。后续新增复盘文件时按时间降序补到这里。

## 共性主题

按需要维护：

- 需求和 trace 收敛质量。
- 设计方案和工程实现之间的偏差。
- Gate / FP / EP / TASK、risk、issue、AP、report 的事项关系质量。
- 测试、验收、发布和运行证据质量。
- Agent 协作的目标理解、读取预算、工具使用、验证和收尾质量。
- 治理规则、模板、技能和 sensor 的晋升 / 降级效果。

## 维护说明

- 新复盘文件优先从 [[templates/project-retrospective-template]] 复制最小骨架。
- 复盘结论如果会改变需求主题，同轮更新 [[projects/trace]]。
- 复盘结论如果会改变关键取舍，同轮更新 [[projects/decisions]]。
- 复盘结论如果是项目级稳定事实，同轮更新 [[projects/memory/README]]。
- 复盘结论如果是跨项目可复用方法，回写 [[concepts/project-retrospective]]、相关概念页或 `templates/`。
- 复盘结论如果暴露 agent / Harness 缺口，回写 [[harness-feedback-ledger]]，再按 [[harness-evolution]] 判断是否晋升。
