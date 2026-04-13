---
type: requirement
id: REQ-001
project: PROJ-WIKI-001
status: active
stage: design
depends_on: []
updated: 2026-04-13
tags: [requirement]
---

# 需求

这页是需求主文件。

上游：[[projects/README]]  \
下游：[[projects/trace]]、[[projects/design/README]]、[[projects/decisions]]

## 这页负责什么

- 说明为什么做
- 说明做给谁
- 说明范围是什么
- 说明验收怎么算通过
- 作为 PRD 在项目层的落点，把问题、目标、范围、规则和验收收成可执行需求
- 说明如果需求涉及 memory 或 policy，哪些边界必须先说清
- 为需求演进链提供原始目标、范围和验收锚点

相关方法：[[concepts/prd-writing]]

## 当前内容

按需要补充：

- 问题定义
- 用户场景
- 目标
- 非目标
- 约束
- 验收标准

## 维护说明

- 如果输入材料是一份 PRD 或需求草稿，先按 [[concepts/prd-writing]] 收敛成问题、目标、范围、规则和验收，再写到这里
- 如果一个需求会改变项目记忆、规则路由或阶段判断，先在这里写清楚，再同步到 [[POLICY]]、[[projects/memory/README]] 和 [[projects/decisions]]
- 如果需求已经进入设计、实现或修补阶段，记得同步到 [[projects/trace]]，不要让范围变化只留在对话里
- 需求页只保留需求本身，不写实现细节
