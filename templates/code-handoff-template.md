# 代码工程回传包模板

使用位置：[[projects/development/execution/developer-execution-workflow]]

推荐存放在实现工程内：

```text
docs/handoffs/<work-id>/README.md
```

轻量或历史兼容任务可以使用：

```text
docs/handoffs/<work-id>-<short-topic>.md
```

```md
# <work-id> | 回传包标题

- 任务 ID：
- 对应 Gate：
- 对应 FP / 候选 ID：
- 对应 EP：
- 对应 TASK：
- 对应 ISSUE / issue-trigger：
- 对应 TODO（轻量 / 兼容）：
- 上游需求 / 目标：
- Goal Contract：
- 期望最终状态：
- 验证面：
- 约束保持情况：
- 阻塞停止条件：
- 关系类型：
- 当前阶段：
- 主责模块：
- 父 EP Done Contract 对齐：
- TASK Done Contract 完成情况：
- 交付物类型：
- 读取输入：
- 实现范围：
- 不做项：
- 验证证据：
- 测试方案和用例执行情况：
- 相关功能回归范围：
- Issue 原始现象保真：
- Bug 反向复验：
- 参数生效证据：
- local validation：
- service-side validation：
- end-to-end validation：
- 服务台账 / UI API / 配置回写：
- Goal 完成判断：
- 独立抽插证据：
- 失败项：
- 未验证项：
- 关闭判断和不上推边界：
- 反馈回写：
- 偏差和风险：
- 提问 / 需交流事项：
- 文档建议：
- 下一步：
```

回传包不是第二份设计正文，也不是把本库页面复制进代码工程。实现工程只能证明本次代码、配置、测试和运行证据；EP / TASK / FP / Gate / Issue 是否关闭，由主控侧按报告、台账和人工确认边界裁决。
