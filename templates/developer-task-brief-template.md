# 编码任务执行单模板

使用位置：[[projects/development/execution/developer-execution-workflow]]

执行单引用当前 TASK / 父 EP owner 的目标、范围和验收，仅补本次派发差异与实现输入。按当前阶段保留适用字段，不预填未适用字段。独立 Goal Contract、Run Capsule 或 Loop Contract 只有命中各自启动条件时才链接实际合同，见 [[templates/goal-contract-template]]、[[templates/run-capsule-template]]、[[templates/loop-contract-template]]；普通编码任务不默认建立。

```md
## 编码任务执行单

- 任务 ID：
- 对应 Gate：
- 功能点 / 候选项：
- 父 EP：
- TASK：
- ISSUE / issue-trigger：
- 当前 owner / 上游需求：目标、授权、范围和停止条件所在章节
- 关系类型：
- 主责模块：
- 执行方：
- 协同方 / 上下游：
- 本次派发范围与不做项：仅写相对 owner 的差异
- 必须保持的约束：引用 owner，补充实现环境约束
- 输入：
- 输出：
- 父 EP Done Contract：引用父级完成标准及本 TASK 对应部分
- TASK Done Contract：引用当前验收条目，不另建完成标准
- 接口 / 数据合同：
- 测试方案：
- 核心用例 / 检查点：
- 相关功能回归范围：
- Issue 原始现象 / Bug 反向用例：
- 联调流程：
- 验收流程：
- 服务台账 / UI API / 配置要求：
- 允许 / 禁止的平台增强：
- 需要回传的结果：
- 不上推边界：
- 阻塞和待确认项：
```
