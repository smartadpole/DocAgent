---
type: concept
updated: 2026-04-13
---

# PRD 写作

## 定义

PRD（Product Requirements Document）不是“把想法写得更长”，而是把业务问题翻译成研发、设计和测试都能执行、能验收的需求文档。

一个好的 PRD 至少要回答四件事：

- 为什么做
- 给谁做
- 做什么、不做什么
- 做成什么样算完成

## 核心原则

- 先定义问题，再定义方案
- 先写目标和范围，再写页面和按钮
- 先补规则，再补文案
- 先补验收，再补实现细节

## 推荐结构

不必每次都写成几十页，但一份能落地的 PRD，通常至少要覆盖这些部分：

1. 文档信息
2. 背景与目标
3. 用户与场景
4. 需求范围与非目标
5. 功能方案
6. 业务规则
7. 页面与交互
8. 数据与埋点
9. 验收标准
10. 风险与未决项

## 写作顺序

1. 先把问题写成一句话。
2. 再把目标写成一句话。
3. 再写本期范围和非目标。
4. 再按用户任务链拆主流程。
5. 再找每一步的决策点、异常流和边界流。
6. 再补验收语句，确认能不能被测试。
7. 最后才展开页面、字段、文案和埋点。

## 常见误区

- 只写功能，不写为什么做
- 只写页面，不写用户路径
- 只写正常流，不写异常和边界
- 没有明确非目标，导致范围膨胀
- 概念词没有定义，导致后续扯皮
- 验收标准不可测试，导致上线后争议

## 相关页面

- [[articles/2026-04-13-prd-writing-guide]]
- [[archive/2026-04-13-prd-writing-guide-source|历史草稿]]
- [[projects/README]]
- [[projects/requirements]]
- [[projects/design/README]]
- [[projects/decisions]]
- [[WORKFLOW]]

## 在本库里的落点

- `projects/requirements.md`：把 PRD 翻成项目可执行需求
- `projects/design/README.md`：把需求翻成设计方案
- `projects/trace.md`：记录需求从原始意图到最终口径的收敛过程
- `projects/decisions.md`：收口方案冲突和拍板
- `governance/WORKFLOW.md`：规定 PRD 如何进入项目推进流程

## 使用说明

- 如果输入是一份 PRD 或需求草稿，先按这个方法收成问题、目标、范围、规则和验收，再写进 `projects/requirements.md`
- 如果需求里混了多个候选方案，先在 `projects/decisions.md` 里拆清楚，再回到设计页
- 如果设计会改变实现口径或边界，继续回写 `projects/trace.md`
- PRD 不是设计文档本身，但它应该成为设计和开发的稳定输入
