---
type: memory
memory_layer: project
scope: project
project: wiki
status: active
source_of_truth: true
updated: 2026-04-09
---

# 项目记忆

这页是 `projects/` 里的运行层 memory 入口，承接项目级稳定背景。

## 这页负责什么

- 记录当前项目长期有效的背景、路由和模块边界
- 记录“以后做事默认要知道”的项目级前提
- 作为 project-scoped memory 的主入口
- 为后续自动化提供可读的稳定上下文

## 这页不负责什么

- 不放全局规则，那是 `POLICY.md`
- 不放项目拍板，那是 `projects/decisions.md`
- 不放共享背景正文，那是 `BRAIN.md`
- 不放过程流水，那是 `log.md`

## 当前子页

- [[projects/memory/shared]]：项目共享背景和稳定事实

## 当前路由

- session / inbox：临时信息
- `projects/memory/README.md`：项目级稳定背景
- `[[BRAIN]]`：共享背景
- `[[POLICY]]`：规则和优先级
- `[[projects/decisions]]`：项目冲突和拍板
- `articles/`、`concepts/`、`indexes/`：长期知识资产

## 维护说明

- 如果一条信息只对当前项目长期有效，优先放这里
- 如果它会改变后续怎么判断和怎么写，优先放到 `[[POLICY]]`
- 如果它已经变成跨阶段、可复用的稳定知识，再提升到 `articles/` 或 `concepts/`
