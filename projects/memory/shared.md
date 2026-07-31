---
type: memory
id: MEM-PROJ-001
memory_layer: shared
scope: project
project: PROJ-WIKI-001
status: confirmed
source_of_truth: true
updated: 2026-07-31
tags: [memory, shared]
---

# 项目共享背景

## 当前稳定事实

- 当前 vault 的用途是一个面向软件研发的文档系统。
- 当前 wiki 的目标角色已经升级为所有实现类工程的合集与模板，但不再把自己定义成某一种工程模板；稳定口径是 Template Kernel + Project Profile Overlay + Capability Pack 的模板母体工程。
- 调研能力属于 Template Kernel 的 `strong-template-kernel` 基线：wiki 完整承接可迁移的 Research Contract、R2+ Source Plan、coverage、Evidence Delta、验证阶梯、修订循环和 evaluator；AcknowledgeBase 保留上游设计与领域知识 owner，wiki 不复制领域正文或项目事实。
- 主控、子工程、runtime service、数据 / 模型工程、知识库 / 文档治理工程、运维 agent 和 hybrid 工程接入时，都应先声明 project_role、primary / secondary profiles、required / optional / forbidden packs、project_bound_facts，再从本仓找到本地 profile、agent system 七层、control plane、implementation boundaries、evidence contract、template adoption 和 closeout proof。
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
- 设计拆模块后，执行粒度以功能点实体页为准；状态镜像看 [[projects/status]]，过程流水看 [[projects/development/execution/worklog]]
- 功能点用 `status` + `phase` 双轴管理：`status` 看生命周期，`phase` 看串联步骤；每个功能点实体页都要同时写这两个字段；功能点实体页一页一个功能点；旧 `in_progress` 口径已拆开
- 实现类工程接入先看 [[projects/design/topics/implementation-engineering-template-system]] 和 [[templates/implementation-project-profile-template]]；AcknowledgeBase source topic 中的通用方案按 [[acknowledgebase-topic-system-adoption.v1]] 逐 topic 落到 agent、workflow、memory、harness、skill、evaluation、governance、template、topic 和 migration 层，不复制源工程事实。
- wiki 治理体系全面整改的完成定义以 [[wiki-governance-system-contract.v1]] 为准：只新增 manifest、摘要矩阵、入口链接或 sensor 只能算 `partial / review`，必须实际写入 owner、模板、memory、harness、skill、sensor 和 closeout proof 后才能说 complete。

## 需要持续带入的前提

- 不需要账号系统才能协作
- 不需要先推翻目录重来
- 先保留现有骨架，再逐步把 memory 路由和 policy 规则机器可读化
- 任何冲突先升级到决策页，再同步回写共享背景或 policy
- sensor 通过只能证明结构接线；没有 runtime / live readback / end-to-end / 人工确认时，任何实现类工程接入都只能报 `partial / review / blocked`，不能上推为已上线、已验收或行为智能达标。
