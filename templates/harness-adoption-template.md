---
type: template
id: TEMPLATE-HARNESS-ADOPTION-001
status: active
updated: 2026-10-14
tags: [template, harness, agent]
---

# Harness 接入模板

## 基本信息

- **系统 / 仓库**：
- **系统类型**：主控文档库 / 子工程 / 服务运行仓库 / 数据工程 / 其他
- **主控关系**：谁定义需求、状态、验收和关闭口径
- **当前阶段**：探索 / 设计 / 实现 / 验收 / 发布 / 运维

## 单一信息源

- **入口页**：
- **需求 / 范围**：
- **设计 / 合同**：
- **状态 / 任务**：
- **验证 / 报告**：
- **服务实例 / 运行事实**：
- **日志 / 过程记录**：

## 写权限和边界

- **可自动写入**：
- **只读上下文**：
- **需要用户授权**：
- **必须人工确认**：
- **禁止动作**：

## 响应模式路由

- **默认模式**：
- **快速诊断事实源**：
- **引导式设计触发条件**：
- **进入沉淀的触发条件**：
- **进入验收关闭的触发条件**：
- **进入规则升级的触发条件**：
- **进入收尾模式的触发条件**：
- **首次 checkpoint 目标**：

## Agent Harness Core

- **根规则入口**：root AGENTS / thin adapter / project-specific adapter。
- **治理分级**：P0 hard constraint / P1 semantic gate / P2 workflow default / P3 backlog。
- **状态约束**：权限、remote、dirty / diverged / local-only、预算、外部服务、人工确认。
- **当前 owner 入口**：引用需求、授权、验收和停止条件的单一信息源；接入模板只声明本地接线。
- **最终交付合同**：修改位置、检查结果、commit hash、未验证边界和不能上推的证据。

## 条件合同接入

默认沿用当前 owner 推进。接入时只为实际需要的能力声明本地 owner / 落点；长时执行、复杂排障或多轮验证本身不触发独立合同，也不生成未启用表单。

- **Goal Contract**：用户明确要求独立完成契约，或持久恢复、依赖控制、累计预算确需独立记录且原 owner 无法承接时，按 [[templates/goal-contract-template]] 引用实际合同。Goal 工具仅在用户明确要求 Goal 时使用。
- **Run Capsule / 编排**：需要独立运行身份、恢复游标或跨角色合流时使用 [[templates/run-capsule-template]]；已授权协作再声明 Orchestrator、Worker、Evaluator、allowed writes、required evidence 和 Subproject Git Preflight。
- **Loop Contract**：需要跨 run 发现源、去重持久队列与调度恢复时使用 [[templates/loop-contract-template]]；合同承接 discovery source、run queue、scheduler、state store、evaluator oracle、budget / stop 和 next-run decision。

目标、完成判定和完成证据回写到原 owner；health、日志、handoff、自述和中间态只能作为辅助证据。各合同只补独立运行需要，不建立平行状态源。

## 验证层级

- **local validation**：
- **service-side validation**：
- **end-to-end validation**：
- **非默认值 / 边界值**：
- **人工确认边界**：

## Handoff 和回写

- **子工程交付物**：
- **主控吸收入口**：
- **状态关闭条件**：
- **风险 / 会议归口**：
- **提交 / 推送要求**：
- **Worker 不能宣布整体闭环**：
- **Evaluator 合流规则**：

## Feedback Sensors

- **已有检查**：
- **缺失检查**：
- **可脚本化规则**：
- **需要保留为人工判断的事项**：
- **sensor 边界**：只证明结构 wiring，不证明真实运行质量。

## 规则反哺

- **可复用系统层信息**：
- **必须剥离的项目事实**：
- **候选落点**：[[WORKFLOW]] / [[AGENTS]] / [[POLICY]] / [[agent-governance-strategy]] / [[state-constraint-reasoning]] / [[agent-orchestration]] / [[skills/README]] / [[templates/README]] / [[BRAIN]]
- **冲突或待拍板**：
