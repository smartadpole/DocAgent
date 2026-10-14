---
type: skill-transfer-manifest
skill: historical-dialogue-retrospective
status: active
updated: 2026-10-14
tags: [skill, transfer, retrospective]
---

# Historical Dialogue Retrospective Transfer

## 能力目标

用原始目标、执行记录和纠偏证据解释Agent工作偏差。 运行入口为 [[skills/historical-dialogue-retrospective/SKILL]]；条件参考随入口按触发迁移，不全量注入每次运行。

## 可以吸收

- 当前上下文、session/rollout、diff、测试、log、ledger、owner和memory的证据用途与限制。
- 快诊与深度复盘分开，深度参考按明确请求/机制问题加载。
- 首轮目标、用户纠偏序列、证据时间点、反证和缺失降级。
- 目标/读取/执行/验证等偏差与成本分析用于定位，不作为每轮固定表单。
- 一次偏差不升级硬规则，真实改进进入原owner。

## 只能抽象吸收

session工具、历史记录形式、复盘存放和ledger路由由目标环境决定；无原始记录要明确局限，不补造。

## 禁止复制

不复制来源工程身份、私有路径、项目状态、服务实例、业务数据、凭据、历史日志或一次性检查结论。源工程可访问不等于获准修改；目标已有规则和用户授权优先。迁移结果不冒充业务验收或外部评价完成。

## 目标工程结构自检

查找已有等价能力、当前owner、实际发现入口、允许写入范围和验证方法；优先复用，缺项按需要补齐。模板、reference和sensor只迁移当前能力真正消费的部分，不为形式完整预建目录。

## 验证要求

验证只有摘要时不会声称完整历史；深度请求保留首轮目标和纠偏，普通问因不建立全套档案。 运行目标适用检查，说明真实变更、验证和未证明的范围；结构检查不能证明模型行为正确。
