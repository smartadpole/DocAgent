---
type: concept
updated: 2026-05-28
---

# OpenClaw

## 定义

OpenClaw 是一个以本地 agent workspace 为核心的 AI agent runtime / gateway 系统。它把规则、人格、工具说明、长期记忆、每日记忆、技能和插件能力组织在同一套工作区与运行时里。

如果只看当前文档库最相关的部分，它最值得关注的是一套 file-first、layered、retrieval-aware 的 memory 设计，而不是单纯“会调用工具的 agent”。

## 相关页面

- [[articles/2026-05-28-openclaw-memory-system-research]]
- [[articles/2026-04-09-layered-memory-research]]
- [[concepts/layered-memory]]
- [[concepts/harness-engineering]]

## 常见用法

- 研究长期运行 agent 的 workspace 组织方式
- 研究 file-backed memory 与检索增强如何结合
- 研究 active recall、memory consolidation 和 compiled knowledge layer
- 研究 agent 工作区如何同时承接规则、记忆和技能

## 维护说明

- 这是 OpenClaw 的概念入口页，只保留定义和跳转。
- 详细调研统一收在 [[articles/2026-05-28-openclaw-memory-system-research]]。
