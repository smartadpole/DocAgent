# 代码工程回传包模板

使用位置：[[projects/development/execution/developer-execution-workflow]]

回传包以当前 owner 的验收条目组织实际交付和证据，仅补本次实现差异。按当前阶段保留适用字段；缺少必要证据时保留缺口和不上推边界。实际启用了独立 Goal Contract、Run Capsule 或 Loop Contract 时，再链接合同并回传该合同要求的结果；启动条件见 [[templates/goal-contract-template]]、[[templates/run-capsule-template]]、[[templates/loop-contract-template]]。

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
- 当前 owner / 上游需求：目标、授权、范围和停止条件所在章节
- 约束保持情况：对照 owner，记录实际偏差
- 关系类型：
- 当前阶段：
- 主责模块：
- 父 EP Done Contract 对齐：
- TASK Done Contract 完成情况：按 owner 验收条目逐项记录通过 / 未通过 / 缺证据及对应证据链接
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
