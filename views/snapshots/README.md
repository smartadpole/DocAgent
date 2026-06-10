# Snapshot Lenses

这里存放需要冻结的历史视图。只有验收、决策、发布、事故、阶段复盘、外部分发或审计证据需要固化时，才从 current lens 冻结 snapshot。

snapshot lens 必须保留 `snapshot_of`、生成时间、source revision、筛选条件、证据边界、回链、导出配置和不可上推边界。普通追问默认刷新 `views/current/` 中的 canonical current lens，不在这里散落新视图。
