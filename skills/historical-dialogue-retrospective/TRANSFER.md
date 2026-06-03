---
type: skill-transfer-manifest
skill: historical-dialogue-retrospective
status: active
updated: 2026-06-03
tags: [skill, transfer, retrospective, adoption]
---

# Historical Dialogue Retrospective Transfer Manifest

## 基本信息

- **能力名称**：完整复盘体系与历史对话 / Agent 工作流复盘能力
- **源技能**：[[skills/historical-dialogue-retrospective/SKILL]]
- **适用迁移场景**：目标工程需要建立复盘体系、升级复盘文件落位、引入 Agent 工作复盘、把历史对话复盘做成 skill，或把复盘结论反哺到模板、规则、sensor 和项目记忆。
- **不适用场景**：目标只是写一篇一次性复盘报告，或只需要记录单个 Issue / 事故原始事实。

## 迁移价值

- 把复盘从“总结文件”升级成长期学习工程。
- 同时覆盖项目复盘、软件研发复盘、Agent 工作复盘和历史对话复盘。
- 让复盘结论能回到未来研发实践、方案设计、工程治理、模板、skill、sensor 和记忆路由。
- 防止复盘行动项漂浮在正文里，或和 Issue、事故、log、决策、memory、trace 混用。

## 参考资料路径

### 核心 skill

- `/Users/hai/Documents/Docs/AcknowledgeBase/skills/historical-dialogue-retrospective/SKILL.md`

### 方法论 / concept

- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/project-retrospective.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/software-development-project-retrospective.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/agent-work-retrospective.md`

### 模板

- `/Users/hai/Documents/Docs/AcknowledgeBase/templates/project-retrospective-template.md`

### 规则 / workflow

- `/Users/hai/Documents/Docs/AcknowledgeBase/AGENTS.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/WORKFLOW.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/harness-evolution.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/harness-feedback-ledger.md`

### 档案 / 运行层入口

- `/Users/hai/Documents/Docs/AcknowledgeBase/projects/retrospectives/README.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/projects/incidents/README.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/projects/development/issues/README.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/log.md`

### 检查脚本 / sensor

- `/Users/hai/Documents/Docs/AcknowledgeBase/scripts/check_all.py`
- `/Users/hai/Documents/Docs/AcknowledgeBase/scripts/check_harness_governance.py`

## 可吸收内容

- 复盘作为长期学习工程的价值定义。
- 复盘文件落位、命名、粒度和最小字段。
- 项目复盘、软件研发复盘、Agent 工作复盘和历史对话复盘的分层。
- 历史对话复盘 skill 的触发条件、证据源分层、输出格式和禁止项。
- 复盘行动项分流到既有 owner 页面的规则。
- 复盘结论反哺模板、skill、sensor、规则、memory 和 trace 的路由。

## 只能抽象吸收

- AcknowledgeBase 的目录结构。
- Gate / FP / EP / TASK / risk / issue / AP / report 事项体系。
- Harness ledger、sensor、规则晋升节奏。
- log eligibility 和收尾检查口径。

## 禁止复制

- AcknowledgeBase 的具体 log 条目。
- 本库项目状态、历史案例原文、一次性治理记录。
- 本机服务路径、工程路径、运行 ID、提交历史或用户偏好。
- DocCustomer、wiki 或其他下游工程的业务事实。

## 目标工程落位建议

- **有 projects/ 结构时**：复盘档案默认放 `projects/retrospectives/`，模板放 `templates/`，skill 放 `skills/`。
- **无 projects/ 结构时**：复盘档案默认放 `docs/retrospectives/`，模板放 `docs/templates/` 或目标工程既有模板目录。
- **已有相近模块时**：先复用已有 `retrospective`、`postmortem`、`incidents`、`lessons-learned` 或 `governance` 入口，避免新建平行体系；但要保留 Issue / 事故事实主档案和复盘档案的分工。

## 目标工程应新增或更新

- 方法入口：项目复盘 / 软件研发复盘 / Agent 工作复盘说明。
- 档案入口：`projects/retrospectives/README.md` 或 `docs/retrospectives/README.md`。
- 模板：项目复盘模板。
- skill：历史对话 / Agent 工作流复盘 skill；如果目标工程没有 skills 体系，则写入 AGENTS 或 docs 的可执行流程。
- 规则 / 读取路径：AGENTS、WORKFLOW 或目标工程等价入口。
- sensor / 检查：如果目标工程已有 check 脚本，补入口或后续候选；没有时只写检查要求，不强行造脚本。
- README / INDEX / AGENTS：让人和 agent 都能找到复盘体系入口。

## 行动分流

- bug、偏差、验收失败：Issue。
- 事故事实和修复闭环：incidents。
- 研发交付动作：Gate / FP / EP / TASK / risk / acceptance / report 或目标工程等价事项系统。
- 跨 owner 协调：meetings。
- 关键取舍：decisions。
- 项目长期事实：memory。
- 需求演进：trace。
- 可复用方法：concepts 或 docs 方法页。
- 可复制骨架：templates。
- 高频 agent 流程：skills。
- 重复失守或机制缺口：harness ledger / feedback ledger。
- 可脚本化检查：sensor / check script。
- 执行规则变化：AGENTS / WORKFLOW / POLICY 或目标工程等价规则入口。

## 生成提示词时必须包含

- 明确说明目标是升级完整复盘体系，不只是新增目录或模板。
- 附上本 manifest 中的资料路径。
- 要求目标工程先读取自身结构，再决定落位。
- 要求建立或完善方法入口、档案入口、模板、skill、规则入口和行动分流。
- 要求跑目标工程已有检查并提交。

## 验证要求

- 目标工程入口能找到复盘体系。
- 复盘方法、档案、模板、skill 的职责分清。
- Issue / 事故 / log / 决策 / memory / trace 不被复盘替代。
- 行动项有 owner 落点。
- 检查通过或说明未能运行的原因。

## 最终回复要求

- 复盘体系落在哪里。
- 方法论在哪里。
- 模板在哪里。
- skill 在哪里。
- 行动项如何分流。
- 跑了哪些检查。
- commit hash。
