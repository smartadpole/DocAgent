---
type: memory
id: MEM-PROJ-001
memory_layer: shared
scope: project
project: PROJ-WIKI-001
status: confirmed
source_of_truth: true
updated: 2026-04-10
tags: [memory, shared]
---

# 项目共享背景

## 当前稳定事实

- 当前 vault 的用途是一个面向软件研发的文档系统。
- 当前运行模式是单库、单项目。
- 当前项目就是这个 wiki 系统本身。
- 现阶段仍然是半自动：人决定做哪一项，agent 按规则辅助执行。
- Git 负责变更审计和回滚，Obsidian 负责阅读和组织，Codex 负责读写与编排。
- 共享背景、项目记忆和规则已经分层：
  - [[BRAIN]] 放共享背景
  - [[projects/memory/README]] 放项目级稳定记忆
  - [[POLICY]] 放规则和优先级
  - [[projects/decisions]] 放项目拍板
- 项目主页固定为 [[projects/README]]
- 项目层结构和读取顺序固定看 [[projects/STRUCTURE]]
- 角色分层固定为：[[projects/README]] 偏 CTO / 项目负责人视角，[[projects/development/README]] 偏研发经理视角，[[projects/development/feature-points/README]] 和其下实体页偏工程师视角
- 设计拆模块后，执行粒度以功能点实体页为准；状态镜像看 [[projects/status]]，过程流水看 [[projects/development/worklog]]
- 功能点用 `status` + `phase` 双轴管理：`status` 看生命周期，`phase` 看串联步骤；每个功能点实体页都要同时写这两个字段；功能点实体页一页一个功能点；旧 `in_progress` 口径已拆开

## 需要持续带入的前提

- 不需要账号系统才能协作
- 不需要先推翻目录重来
- 先保留现有骨架，再逐步把 memory 路由和 policy 规则机器可读化
- 任何冲突先升级到决策页，再同步回写共享背景或 policy
