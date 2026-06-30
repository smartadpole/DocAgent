# 研发事项矩阵模板

使用位置：[[projects/development/plan/work-item-system-model]]

主链默认是 `Gate -> FP -> EP -> TASK`。`risk`、`issue`、`test`、`验收` 是关系节点，不是和主链平行的待办池。

```md
| 树状编号 | 上游需求 / 目标 | Gate | 功能点 / 候选项 | EP | TASK | 子工程增量 | 关系类型 | 主责模块 | 当前状态 | 输出物 | 关闭证据 | 回归守卫 | 关系节点覆盖 | 反馈回写 | 未确认项 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-EP-FP-M3-005-02-03 | 例：需求 A | GATE-M3 | FP-M3-005 | EP-FP-M3-005-02 | TASK-EP-FP-M3-005-02-03 | 子工程路径 / handoff | decomposes | 模块 A | planned | 文档 / 代码 / 报告 | 测试报告 / 人工确认 | 旧 bug / 相邻功能 / 配置回归 | risk: RISK-FP-M3-005-01; test: REPORT-001; 验收: local + service-side; issue-trigger: 失败时创建 / 复用 ISSUE-TASK-EP-FP-M3-005-02-03-01 | 需求 / 设计 / 决策 / status | owner 待定 |  |
```

`树状编号` 必须能读回父级上下文；没有父 EP 的 TASK 只能作为待关系校准候选，不能直接派发为正式编码任务。
