---
type: template
id: TEMPLATE-GOAL-CONTRACT-001
status: active
updated: 2026-10-14
tags: [template, harness, goal, contract]
conditional_sources: [templates/goal-contract-extensions.md]
---

# Goal Contract 模板

先复用当前 owner 的目标、授权、验收和停止条件。只有用户明确要求独立完成契约，或持久恢复、依赖控制、累计预算确需独立记录且原 owner 无法承接时，才建立 Goal Contract。普通持续执行、复杂排障、跨多轮验证或区分证据层级，本身均不构成启动条件。

Goal 工具仅在用户明确要求 Goal 时调用；需要文档合同不等于获准创建 Goal 工具对象。仅“持续做到完成”时直接继续已有任务，不生成未启用合同或适用性表单。

## 最小生效核心

以下信息可以链接已有 owner 的精确章节，不复写第二份目标或状态。

- **Owner 与独立记录原因**：事项 / owning page；原 owner 无法承接的恢复、依赖或累计预算需要。
- **目标与完成判定**：用户最新目标、期望最终状态、可观察的验收结果和明确不做项。
- **授权与约束**：允许写入的文件 / 环境、工具 / 数据权限、必须保持的边界。
- **验证合同**：直接完成证据、必要验证面、证据来源及不能上推的层级。
- **预算与停止条件**：适用的时间 / 成本 / 读取或探索上限；权限、风险、目标冲突、证据或预算触发的停止点。
- **当前进展与恢复点**：已达到状态、完成证据 / 缺口、下一步动作与 owner；恢复时读回真实状态。

health、日志、handoff / 自述、accepted / running 等中间态不能代替功能、service-side、end-to-end 或正式准出证据。必要证据缺失只能判 partial / review / blocked；预算耗尽不代表完成，局部通过不能关闭父事项。

## 条件扩展

只在命中条件时读取 [[templates/goal-contract-extensions]] 对应章节并补入当前 owner，不复制整份扩展。涉及分层验收、参数或研究裁决时用“证据与研究”；需要多轮恢复或依赖调度时用“恢复与依赖”；已授权跨角色 / 跨仓工作时用“协作与回传”；形成可复用教训或显式复盘请求时用“沉淀”。没有触发的章节不写空表、no-op 或不适用声明。
