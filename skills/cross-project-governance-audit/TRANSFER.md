# Cross Project Governance Audit Transfer

## 能力目标

对指定工程按证据审计治理机制，输出真实缺口、识别缺口和可执行整改。 运行入口为 [[skills/cross-project-governance-audit/SKILL]]；条件参考随入口按触发迁移，不全量注入每次运行。

## 可以吸收

- 单工程/多工程/本仓审计按用户范围选择；明确全登记工程请求才按注册表全集覆盖。
- source-depth、true-gap / recognition-gap / signal-only-gap、证据强度及 no runtime validation 边界。
- handoff-ready 需有 owner、写入范围、操作、验证与停止条件，不等于整改已完成。
- 对外模板使用 source archetype / capability pack，分开 system-layer capability 与 project-bound fact。

## 只能抽象吸收

目标治理维度、注册表、Git流程与检查入口按目标自身结构映射；不需要多工程审计时不建注册表。

## 禁止复制

不复制来源工程身份、私有路径、项目状态、服务实例、业务数据、凭据、历史日志或一次性检查结论。源工程可访问不等于获准修改；目标已有规则和用户授权优先。迁移结果不冒充业务验收或外部评价完成。

## 目标工程结构自检

查找已有等价能力、当前owner、实际发现入口、允许写入范围和验证方法；优先复用，缺项按需要补齐。模板、reference和sensor只迁移当前能力真正消费的部分，不为形式完整预建目录。

## 验证要求

用一个有等价能力但命名不同的对象检验 recognition-gap；用一个仅文件存在、无运行证据的对象验证不上推。 运行目标适用检查，说明真实变更、验证和未证明的范围；结构检查不能证明模型行为正确。
