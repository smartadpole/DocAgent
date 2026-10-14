---
name: cross-project-governance-audit
description: 审计指定工程的 Agent 治理、技能、检查与协作边界，区分真实缺口和识别缺口；不因普通修改或泛化建议自动扫描所有工程。
maturity: mature
evidence_signals: [skill, README entry, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only harness-governance,skill-maturity
---

# Cross-Project Governance Audit

围绕用户指定的工程和审计问题，判断机制是否存在、是否有真实证据、缺口应由谁处理。审计本身不授权改目标工程。

## 范围与证据

单工程只检查该工程；多工程比较保持同一基线。用户明确要求全登记工程时，以 source registry 或等价登记面为全集，逐工程记录覆盖和不可读原因；“举一反三”本身不扩大工程范围。只需本工程自查时不新建注册表。

先读目标入口与当前 owner，再按缺口查看相关治理、skill、模板、sensor、运行证据或历史变更。Git 同步状态影响判断时检查 branch、remotes、dirty、fetch 与 ahead/behind；纯文档审计不为仪式执行 fetch。说明实际 source-depth，不能以只读根入口冒充完整审计。

按问题选取执行约束、响应分流、反馈纠偏、自动检查、技能模板、跨工程权限等维度。对每项给出证据、缺口和影响：

- `true-gap`：缺失必要能力或实现。
- `recognition-gap`：等价能力已有，入口或识别方式缺失。
- `signal-only-gap`：只缺词语、篇幅等弱信号，不值得补噪声。

文件存在、矩阵分数、sensor 通过只证明相应结构；不能证明模型行为、runtime validation、业务质量或验收完成。未运行验证时如实标明。

## 交付与后续

交付结论、逐项证据、真实缺口及 owner。需要可执行移交时使用 [[templates/cross-project-governance-audit-contract-template]] 的适用字段，说明写入范围、操作、验证、停止条件与剩余边界；`handoff-ready` 表示可以执行，不表示已修复。

跨工程吸收只提炼 system-layer capability；project-bound fact、排行、运行状态、真实路径和一次性报告不进入通用规则。公开模板使用 source archetype / capability pack 等角色描述。规则升级回到 [[template-feedback-rules]]，迁移边界见 [[skills/cross-project-governance-audit/TRANSFER]]。

相关验证：`python3 scripts/check_all.py --only cross-project-governance-audit`。专项检查证明接线，独立审计判断仍需对应证据。
