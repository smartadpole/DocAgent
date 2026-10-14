---
type: template
id: TEMPLATE-GOAL-CONTRACT-EXTENSIONS-001
status: active
updated: 2026-10-14
tags: [template, goal, conditional]
---

# Goal Contract 条件扩展

入口与最小生效核心见 [[templates/goal-contract-template]]。本页提供专业能力的条件字段，不是每个 Goal 的附加检查单；已有事实只引用 owner。

## 证据与研究

**触发**：需要区分实现 / 研究 / 方法候选、多个验证层级、参数效果或证据冲突。

- **合同类型**：implementation-goal / trace-only / method-candidate / research-decision / orchestrator-acceptance。
- **Source pack**：本次必须读取或引用的事实源，区分一手事实、辅助事实、推论及未读范围。
- **验证面与证据**：按完成判定选择测试、benchmark、报告、artifact、DB readback、日志、UI 或人工确认；逐项记录结果与缺口。
- **证据层级**：仅列相关 code-level / unit、functional / business-flow、service-side、end-to-end、non-default / boundary、related regression、manual-confirmation。缺少必要层级需给出 partial / blocked 边界，不能以删除字段掩盖缺测。
- **参数验收**：涉及参数 / profile / flag 时，用非默认值或边界值证明它真实影响结果，接口回显不算验证。
- **证据审计**：完成证据与辅助证据的区别、冲突裁决、不能从 local 上推到 service-side / end-to-end / Gate 的范围、仍需人工确认的事项。

## 恢复与依赖

**触发**：执行跨 run，或存在必须持久化的依赖、累计预算与探索分支。

- **恢复状态**：迭代编号、已消费输入、已完成 / 待完成动作、依赖 owner 与状态、恢复游标。
- **迭代规则**：每轮检查和记录什么、下一步选择条件、探索分支上限；不重复记录目标正文。
- **累计预算**：适用的时间 / token / 成本 / 命令或远程操作上限、实际消耗、剩余量与耗尽后的 partial / blocked 状态。
- **阻塞回传**：已达到的状态、缺少哪层证据、不能继续的原因、建议 owner / 恢复动作；下一步为 rerun / retry-after / split / escalate / wait-human / stop 中实际适用者。

## 协作与回传

**触发**：用户或适用规则已授权多 agent / 多线程、主控与子工程分工；此条件本身不授权委派或跨仓写入。

- **职责与入口**：主控负责结果、验收口径、关闭条件和风险归口；子工程回传实现范围、本地验证、失败项、limits 和未验证边界；记录主控吸收与子工程回传入口。
- **Pipeline trace**：目标 → 执行 → 验证 → 吸收的实际证据链接；只在需要独立运行身份、恢复游标或跨角色合流时引用 [[templates/run-capsule-template]]。
- **外部仓库与 Worker**：命中时按 [[templates/run-capsule-extensions#外部仓库现场检查]]、[[templates/run-capsule-extensions#多角色合流]] 填写，不另抄同一份 Git / ownership 信息。

## 沉淀

**触发**：稳定背景、可复用方法、用户纠偏 / 重复失守，或用户显式请求复盘。

按 [[templates/run-capsule-extensions#沉淀与复盘]] 选择事实 owner 和抽象层，记录实际落点与复用证据；没有新信号时不输出“未复用理由”或默认 no-op。显式复盘请求不能因自动触发资格不足而降级。
