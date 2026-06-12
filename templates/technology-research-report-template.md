---
type: template
id: TEMPLATE-RESEARCH-REPORT-001
status: active
updated: 2026-06-12
tags: [template, research, technology-research, research-capability]
---

# Technology Research Report Template

用于输出 `research-capability` 的正式结果。它不替代项目决策、PoC 验收或合规批准。

## 一句话结论

- 结论：
- 行动等级：Adopt / Trial / Assess / Hold / Blocked
- 置信度：high / medium / low
- 刷新触发：

## 调研合同

- 对象：
- 决策目标：
- 关键问题：
- 不做项：
- 时间锚点：

## 证据摘要

| 证据 | 等级 | 来源 | 支撑的问题 | 局限 |
| --- | --- | --- | --- | --- |
|  | L1 / L2 / L3 / L4 / L5 |  |  |  |

## 分支判断

- 分支：技术专题 / 开源工程 / 行业 AI / 产品公司 / PoC / 源码工程
- 成熟度：
- 替代方案：
- 集成成本：
- 维护成本：
- 主要阻断项：

## 风险门

| 风险 | 状态 | 证据 | 下一步 |
| --- | --- | --- | --- |
| 安全 |  |  |  |
| license |  |  |  |
| 隐私 / 合规 |  |  |  |
| 供应链 |  |  |  |
| 成本 |  |  |  |
| 维护 |  |  |  |

## 建议

- 立即动作：
- PoC 或验证：
- 暂缓原因：
- 需要人工确认：

## 沉淀

- 主落位：
- 入口 / 回链：
- 后续刷新：
- 未覆盖边界：

## 反证与不确定性

| 假设 | 反证来源 | 当前状态 | 影响 |
| --- | --- | --- | --- |
|  |  | confirmed / likely / possible / blocked |  |

## 采用前检查

- 版本和 release 是否当前：
- license 是否允许目标使用：
- 安全公告和 CVE 是否检查：
- 数据、隐私和合规边界是否明确：
- 成本和限额是否当前：
- 关键 API 是否有 breaking change 风险：
- 是否存在退出成本或供应商锁定：
- 是否需要本地 PoC：
- 是否需要人工或业务 owner 拍板：

## 输出降级规则

- 只有资料摘要，没有证据等级：不能给行动等级。
- 只有 L4 / L5：只能写线索和待验证问题。
- 没有当前查证：不能写“最新版支持 / 当前价格 / 当前政策”。
- 没有本地运行：不能写“可接入生产”。
- 没有项目 owner 确认：不能写“已拍板采用”。
- 没有沉淀入口：不能写“已进入知识库”。
