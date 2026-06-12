---
type: template
id: TEMPLATE-PROBLEM-FOCUSED-LENS-REVIEW-CONTRACT-001
status: active
updated: 2026-06-12
tags: [template, lens, problem-focused-lens, review-contract, problem-focused-visual-presentation]
---

# Problem-Focused Lens Review Contract

本模板用于审核 problem-focused lens 是否值得交付。它不是为了增加正文体量，而是为了确认 lens 没有替代真相源、没有误报导出、没有把局部证据上推成项目裁决。

## 审核优先级

1. 证据合同：source pack、evidence boundary、source revision、refresh trigger。
2. 使用边界：current / snapshot、not source of truth for、不能上推到哪里。
3. 持久化合同：canonical path、registry、导出缓存和检查状态。
4. 可读性：首屏判断、视觉结构、颜色 / 排序 / 分组口径。

如果证据不清，停止交付；视觉风格不能弥补证据缺口。

## 核心审核表

| 检查项 | 通过标准 | 失败处理 |
| --- | --- | --- |
| 关注问题 | 首屏能看出 lens 回答什么 | 回到关注合同 |
| source pack | 关键判断都有来源 | 补来源或降级 |
| evidence boundary | confirmed / likely / possible / blocked 分开 | 重写证据段 |
| current / snapshot | 时间、revision、刷新触发清楚 | 补 metadata |
| registry | 持久 lens 已登记 | 先补 [[views/lens-registry]] |
| 导出 | PNG / PDF / print view 状态真实 | 改写导出声明 |
| 不上推 | 写清不能替代状态、验收、规则或任务 | 补边界说明 |

## 典型误用

- 把矩阵颜色当成能力事实，忽略诊断里的 missing signals。
- 把 HTML 当成项目状态源。
- 把 PNG / PDF 当成 canonical source。
- 把未读来源写成 confirmed。
- 把候选根因写成已确认根因。
- 把 research 线索写成采用建议。
- 把子工程 handoff 写成主控吸收完成。
- 把 lens 里的行动项当成正式 TASK。

## 完成判定

- `ready for reading`：source pack、证据边界、首屏判断完整。
- `ready for sharing`：在 `ready for reading` 基础上完成视觉和导出检查。
- `ready for decision support`：行动等级、风险、owner 和不上推边界都清楚。
- `needs-work`：缺来源、缺 registry、导出未验证或读者仍需追问关键证据。

## 最终回复片段

```markdown
- lens:
- source pack:
- registry:
- exports:
- verified:
- not source of truth for:
- remaining boundary:
```
