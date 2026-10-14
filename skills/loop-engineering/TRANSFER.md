---
type: skill-transfer
skill: loop-engineering
updated: 2026-10-14
---

# Loop Engineering Transfer

## 能力目标

实现跨run持续发现、去重、评价、持久恢复与可停止调度。 运行入口为 [[skills/loop-engineering/SKILL]]；条件参考随入口按触发迁移，不全量注入每次运行。

## 可以吸收

- Discovery source、Run queue、Persistent state、Evaluator oracle、Scheduler/trigger和Budget/stop。
- 缺关键条件只能discovery-only/not-ready，不启动写入型循环。
- 单agent合法；委派已授权且有需要才读Worker参考，Run Capsule按恢复/合流需要建立。
- 消费项、幂等标识、状态转换、证据、next-run decision与失败恢复。
- Loop不授予外部写入、自动发布或父级关闭权限。

## 只能抽象吸收

目标调度系统、状态存储、oracle、业务owner、Git策略与runbook需要本地确定；脚本不自动代表完整循环控制。

## 禁止复制

不复制来源工程身份、私有路径、项目状态、服务实例、业务数据、凭据、历史日志或一次性检查结论。源工程可访问不等于获准修改；目标已有规则和用户授权优先。迁移结果不冒充业务验收或外部评价完成。

## 目标工程结构自检

查找已有等价能力、当前owner、实际发现入口、允许写入范围和验证方法；优先复用，缺项按需要补齐。模板、reference和sensor只迁移当前能力真正消费的部分，不为形式完整预建目录。

## 验证要求

验证重复输入不重复副作用、预算/失败会停、恢复游标有效、Worker局部证据不关整体；确定性oracle可用时不强制另开模型。 运行目标适用检查，说明真实变更、验证和未证明的范围；结构检查不能证明模型行为正确。
