# 开发记录

这页是开发层的过程记录页。

主入口：[[projects/development/execution/README]]

上游：[[projects/development/plan/README]]、[[projects/development/execution/todo]]  \
横向：[[projects/development/reports/README]]、[[projects/development/risks/README]]

## 这页负责什么

- 记录复杂排障
- 记录联调过程
- 记录验证过程
- 记录阶段性问题和解决动作
- 记录开发过程里的讨论和临时同步
- 不承接正式会议纪要；正式会议优先写到 [[projects/meetings/worklog]]

## 当前内容

按时间追加：

- 时间
- 做了什么
- 发现了什么
- 如何验证
- 还剩什么问题

## 记录模板

每次写过程，默认复制 [[templates/development-worklog-entry-template]]。

- 状态变化和阶段变化要分开记，不要重新合并成一个 `in_progress`。

## 关联实体

- 功能点实体页看 [[projects/development/feature-points/README]]
- 过程记录里如果提到某个功能点，优先链接到对应实体页
- 如果这条开发记录来源于正式会议，回看 [[projects/meetings/worklog]]
- 如果某次实现改变了范围、口径或修补边界，记得同步回写 [[projects/trace]]
- 如果某次验证影响 TASK / EP / FP / Gate 关闭、Issue 或回归范围，记得同步回写 [[projects/development/reports/README]]
