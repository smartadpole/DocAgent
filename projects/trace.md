---
type: trace
id: TRACE-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-12
tags: [trace, project]
---

# 需求演进链

这页是项目层里“需求如何收敛成当前实现口径”的主入口。

- 详细记录规则见 [[trace-writing-rules]]。
- 默认模板见 [[templates/trace-entry-template]]。

上游：[[projects/README]]、[[projects/requirements]]、[[projects/design/README]]  \
横向：[[projects/decisions]]、[[projects/development/README]]、[[projects/development/worklog]]  \
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

### TRACE-001 文档系统分层与项目运行链路

- 原始意图：
  - 把当前 Obsidian + Codex 文档系统整理成一个可演化的知识库，并能支撑项目推进。
  - 让项目材料从产品梳理、技术选型、架构设计一路支撑到 agent 开发，而不是只停在资料整理。
- 收敛后的可执行需求：
  - 用 `README`、`INDEX`、`BRAIN`、`POLICY`、`projects/` 和 `log` 建立分层清晰的文档系统。
  - 在项目层明确需求、设计、决策、开发、发布、事故和项目记忆的职责边界。
  - 为项目推进补一条“需求如何收敛成实现”的演进链，不让关键约束和范围变化只留在聊天历史里。
- 关键决策变化：
  - 早期重点是把 `[[log]]` 从动作流水改成按对话组织的主题化历史，但后来确认它仍然只回答“这轮对话在解决什么”，不承担完整需求演进链。
  - 在保留现有分层的前提下，新增 [[projects/trace]] 作为项目运行层主文件，而不是把 trace 混进 `[[log]]`、`[[projects/decisions]]` 或 `projects/memory/`。
- 最终范围：
  - `[[log]]` 继续承担对话级主题化历史。
  - [[projects/trace]] 承担需求、约束、修补和最终实现口径之间的结构化串联。
  - 项目层入口、结构说明、流程页和规则页同步承认这条 trace 链路。
- 假设与未决项：
  - 当前先用单文件主链，后续只有在主题明显增多时再拆分子页或模板。
  - 如果未来出现多个并行需求主题，再评估是否需要把每个主题拆成独立 trace 子页。
- 关联页面：
  - [[README]]
  - [[INDEX]]
  - [[AGENTS]]
  - [[WORKFLOW]]
  - [[projects/README]]
  - [[projects/STRUCTURE]]
  - [[projects/requirements]]
  - [[projects/design/README]]
  - [[projects/decisions]]
- 迭代：

#### 2026-04-12

- 本轮变化：
  - 明确区分 `[[log]]` 和需求演进 trace 的职责边界。
  - 把收尾模式补成显式协议，避免收尾时继续扩需求。
  - 正式新增 [[projects/trace]]，补齐项目推进里的需求演进主链。
- 当前实现口径：
  - 新主题先在需求、设计和决策页形成最小可执行内容，再把原始意图、关键变化和最终范围串回这页。
  - 后续每轮进入项目推进的对话，都应判断是否需要续写已有 trace 主题，而不是只补 `[[log]]`。
