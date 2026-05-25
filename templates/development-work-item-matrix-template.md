# 研发事项矩阵模板

使用位置：[[projects/development/plan/work-item-system-model]]

主链默认是 `Gate -> FP -> EP -> TASK`。`risk`、`issue`、`test`、`验收` 是关系节点，不是和主链平行的待办池。

```md
| 上游需求 / 目标 | Gate | 功能点 / 候选项 | EP | TASK | 子工程增量 | 关系类型 | 主责模块 | 当前状态 | 输出物 | 关闭证据 | 回归守卫 | 关系节点覆盖 | 反馈回写 | 未确认项 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 例：需求 A | Gate-001 | FP-001 | EP-001 | TASK-001 | 子工程路径 / handoff | decomposes | 模块 A | planned | 文档 / 代码 / 报告 | 测试报告 / 人工确认 | 旧 bug / 相邻功能 / 配置回归 | risk: RISK-001; test: REPORT-001; 验收: local + service-side; issue-trigger: 失败时创建 / 复用 ISSUE | 需求 / 设计 / 决策 / status | owner 待定 |  |
```
