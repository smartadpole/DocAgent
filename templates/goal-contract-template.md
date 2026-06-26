---
type: template
id: TEMPLATE-GOAL-CONTRACT-001
status: active
updated: 2026-06-22
tags: [template, harness, goal, contract]
---

# Goal Contract 模板

Goal Contract 是长时任务的完成契约，不是全局 memory、仓库级规则、项目状态页，也不是要求每轮都启用的固定模板。它的位置固定在**响应模式判断之后、正式长时执行之前**。只有当任务“终点清楚、路径需要在执行中探索、可能跨多轮迭代”时才使用，例如复杂 bug 复现、性能优化、迁移、跨轮调研、反复验证的修复、主控和子工程之间的长任务回传。

Goal 只解决三件事：

1. **防止任务跑偏**：固定原始目标、期望最终状态和本轮完成判定，跨多轮后先回到这里校准“到底要完成什么”。
2. **防止证据漂移**：固定验证面、可接受证据、不能上推的证据边界，避免把 health、日志、子工程自述或中间态误当成真正闭环。
3. **防止无限探索**：固定预算、停止条件和阻塞汇报格式，避免复杂任务无边界地继续查下去。

## 适用性判断

- **任务 / 事项 ID**：
- **当前响应模式**：
- **当前执行位置**：主控 / 子工程 / Worker / Evaluator / 其他
- **owning page / record landing**：
- **质量门 / sensor**：
- **为什么需要完成契约**：
- **为什么不是普通一次性任务**：
- **不使用 Goal Contract 的理由**：

## 完成契约

- **原始目标 / 用户最新目标**：
- **期望最终状态**：用可观察结果写清完成后应该变成什么样。
- **完成判定**：哪些结果出现才算完成；哪些结果只能算 partial / review / blocked。
- **验证面**：测试 / benchmark / 报告 / artifact / DB readback / 日志 / UI / 人工确认 / 其他
- **合同类型**：implementation-goal / trace-only / method-candidate / research-decision / orchestrator-acceptance
- **证据层级**：code-level / unit、functional / business-flow、service-side、end-to-end、non-default / boundary、manual-confirmation；不适用或缺失时写明 partial / blocked。
- **Source pack**：必须读取或引用的事实源；区分一手事实、辅助事实和推论。
- **Pipeline trace**：本轮从用户目标到执行、验证、沉淀的链路；主控 / 子工程任务要写明 Run Capsule 或 handoff 位置。
- **必须保持的约束**：
- **允许使用的文件 / 工具 / 数据 / 环境**：
- **明确不做项**：

## 迭代和停止

- **每轮检查什么**：
- **每轮记录什么**：
- **下一步选择规则**：
- **预算或时间边界**：时间 / 命令次数 / 读取范围 / 远程操作 / 成本上限。
- **探索分支上限**：最多同时追几条线索；超过后先汇报而不是继续扩散。
- **必须停止并汇报的条件**：权限缺失、证据不足、环境风险、预算耗尽、目标冲突、需要用户裁决。
- **阻塞后汇报格式**：已达到的状态、缺少哪层证据、不能继续的原因、建议 owner / 恢复动作。

## 证据审计

- **完成证据**：能直接证明期望最终状态达成的证据。
- **辅助证据**：health、日志、子工程 handoff、自述、历史报告、中间态等只能作为辅助输入。
- **不能上推的证据边界**：写清哪些证据不能从 local 上推到 service-side / end-to-end / Gate。
- **明确不足以闭环的证据**：例如只跑 health、只看日志、只读 handoff、只看到任务 accepted / running、只拿到子工程口头完成。
- **仍需人工确认的事项**：
- **预算耗尽时的状态**：blocked / partial / review / 其他

## 主控 / 子工程分工

- **主控定义**：结果、验收口径、状态关闭条件、风险归口
- **子工程执行**：实现范围、本地验证、失败项、未验证边界、回传证据
- **主控吸收入口**：
- **子工程回传入口**：
- **Run Capsule**：多 agent / 多线程 / 子工程运行时链接 [[templates/run-capsule-template]] 或实际 Run Capsule。

## 沉淀和复用

- **Method capture decision**：no-op / log / harness ledger / memory / skill / template / sensor / rule / retrospective
- **Persistence landing**：
- **Reuse decision**：本轮是否形成可复用方法；如果不复用，写明理由。
- **Verification-loop**：下一轮是否需要 rerun / retry-after / split / escalate / wait-human / stop。
- **Retrospective trigger decision**：no-op / 轻量复盘 checkpoint / 标准复盘 / 深度复盘。
