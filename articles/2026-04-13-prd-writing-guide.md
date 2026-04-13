---
type: article
date: 2026-04-13
updated: 2026-04-13
---

# PRD 写作指南

- 来源：[[archive/2026-04-13-prd-writing-guide-source|历史草稿]]
- 日期：2026-04-13
- 类型：方法总结

## 一句话总结

PRD 的核心不是堆模板，而是把业务问题翻成可执行需求：先写问题、目标、范围和验收，再补规则、异常、边界和设计约束。

## 关键要点

- PRD 先写问题和目标，不要先写页面
- 用用户任务链组织需求，不用功能清单组织
- 规则要覆盖正常流、异常流和边界流
- 验收要写成可测试语句
- 在本库里，PRD 的落点是 `projects/requirements.md`，设计转译落点是 `projects/design/README.md`

## 相关概念

- [[concepts/prd-writing]]

## 相关项目页

- [[projects/requirements]]
- [[projects/design/README]]
- [[projects/trace]]
- [[projects/decisions]]

## 后续动作

- 需求输入先收敛成问题、目标、范围、规则、验收，再进入设计
- 如果出现多个可选方案，先回到 [[projects/decisions]] 拆清楚
- 如果需求在推进中发生变化，回写 [[projects/trace]]
