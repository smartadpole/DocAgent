---
type: design
id: DES-MEM-001
project: PROJ-WIKI-001
status: active
stage: design
updated: 2026-04-10
tags: [design, memory]
---

# Memory 研究

这里是 memory 设计研究层，不是正式生效的 memory 存储位。

## 这页负责什么

- 承接 memory 分层方案讨论
- 承接 memory 工具调研
- 承接未来 memory 运行层的设计草稿

## 这页不负责什么

- 不承接正式生效的项目 memory，那是 [[projects/memory/README]]
- 不承接共享背景，那是 [[BRAIN]]
- 不承接正式规则，那是 [[POLICY]]
- 不承接角色专属 memory；角色分层是项目稳定事实，统一记在 [[projects/memory/shared]]

## 角色和 memory 的关系

- 这里讨论的是设计判断，不是正式运行层的数据。
- 角色是职责视角，memory 是上下文视角。
- 当前设计不打算给每个角色单独一套 memory，而是让共享背景、项目记忆和规则层按作用域服务不同角色。
- 如果未来要做角色专属 memory，需要额外补 ownership 和 routing 设计。

## 当前入口

- [[articles/2026-04-09-layered-memory-research]]
- [[concepts/layered-memory]]
- [[projects/memory/README]]
- [[projects/decisions]]

## 当前子页

- [[projects/design/memory/tools]]
