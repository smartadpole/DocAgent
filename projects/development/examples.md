---
type: example
id: DEV-EX-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-10
tags: [development, examples]
---

# 开发示例

主入口：[[projects/development/README]]  \
配套：[[projects/development/worklog]]

这页只放可直接复制的示例，不承载真实进度。

## 双轴说明

- 每张示例卡都同时写 `status` 和 `phase`
- `status` 负责生命周期
- `phase` 负责当前步骤
- 下面三张卡分别示范进行中、完成待发布、已发布

## 示例 1：进行中功能点卡片

#### FP-001 | 为项目状态页补功能点状态镜像

- 状态：active
- 阶段：implementation
- 模块：项目运行层
- 目标：把模块 -> 功能点 -> 状态 -> 阶段 -> 记录 -> 发布这条链路固定下来
- 范围：[[projects/status]]、[[projects/development/README]]、[[projects/development/worklog]]
- 验收：读者能按模板登记一个功能点，并知道状态如何推进
- 负责人：team
- 下一步：把活跃页面按模板补齐
- 阻塞：暂无
- 相关设计：[[projects/design/README]]
- 相关决策：[[projects/decisions]]
- 过程日志：[[projects/development/worklog]]
- 发布/事故：视实现结果补到 [[projects/releases]] 或 [[projects/incidents/README]]
- 结果：待完成后补充

## 示例 2：完成但未发布

#### FP-002 | 双轴模型开发完成，等待发布

- 状态：done
- 阶段：release
- 模块：项目运行层
- 目标：开发和验证已经完成，进入发布收口
- 范围：[[projects/development/README]]、[[projects/development/worklog]]、[[projects/releases]]
- 验收：读者能看出这张卡已经开发完成，但还没有进入已发布态
- 负责人：team
- 下一步：确认发布窗口并写入发布页
- 阻塞：暂无
- 相关设计：[[projects/STRUCTURE]]
- 相关决策：[[projects/decisions]]
- 过程日志：[[projects/development/worklog]]
- 发布/事故：视发布结果补到 [[projects/releases]] 或 [[projects/incidents/README]]
- 结果：等待发布收口

## 示例 3：已发布功能点

#### FP-003 | 双轴模型已发布收口

- 状态：released
- 阶段：release
- 模块：项目运行层
- 目标：让已完成的功能点和已经发布的功能点分开管理
- 范围：[[projects/development/README]]、[[projects/development/examples]]、[[projects/releases]]
- 验收：读者能看出这张卡已经上线，不再属于活跃实现对象
- 负责人：team
- 下一步：如有后续修改，重新开修复点或事故记录
- 阻塞：暂无
- 相关设计：[[projects/STRUCTURE]]
- 相关决策：[[projects/decisions]]
- 过程日志：[[projects/development/worklog]]
- 发布/事故：视实现结果补到 [[projects/releases]] 或 [[projects/incidents/README]]
- 结果：已发布并收口

## 示例 4：过程记录

- 2026-04-10 10:30
  - 功能点：FP-001 为项目状态页补功能点状态镜像
  - 模块：项目运行层
  - 状态变化：planned -> active -> done -> released
  - 阶段变化：design -> implementation -> verification -> release
  - 做了什么：补齐开发入口的模板、状态轴、阶段轴和示例
  - 发现了什么：状态和阶段需要分层维护，不能把设计、实现和验证挤在一个 `in_progress` 里
  - 如何验证：读者可以从模板复制一张卡，并知道要同步更新哪些页面
  - 阻塞：暂无
  - 下一步：把活跃页面按模板补齐
  - 关联链接：[[projects/development/README]]、[[projects/status]]
