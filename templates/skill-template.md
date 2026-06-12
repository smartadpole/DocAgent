---
name: <skill-name>
description: <一句话说明触发场景、适用任务、输出结果和关键边界>
maturity: draft
evidence_signals: []
transfer_ready: false
sensor: none
---

# <Skill Name>

## 定位

说明这个技能把哪类高频任务收敛成什么结果。

## 适用场景

- 场景一：
- 场景二：
- 场景三：

## 边界

- 技能只写可复用流程、判断框架、输出格式和回写守卫。
- 如果涉及项目事实，只写读取和回写入口，不复制正式项目页面正文。
- 如果需要改变规则、状态、设计或验收口径，回到对应主入口处理。

## 成熟度与证据信号

- `maturity`：`draft` / `adopted` / `mature` / `leading` / `deprecated`
- `evidence_signals`：`skill` / `README entry` / `template` / `governance` / `sensor` / `TRANSFER` / `view-or-report`
- `transfer_ready`：是否已经写清跨工程吸收边界、目标自检方式和不复制的项目事实。
- `sensor`：可用的检查命令；没有可检查面时写 `none` 并说明原因。
- `evidence boundary`：成熟度只说明本技能的文档和治理信号，不代表运行验收、项目状态或任务关闭。
- 如果 `transfer_ready: true`，同目录必须有 `TRANSFER.md`，至少写清能力目标、可以吸收、只能抽象吸收、禁止复制、目标工程结构自检和验证要求。

## 工作流

1. 先框定输入和目标。
2. 建立上下文和事实源地图。
3. 区分已确认、待确认、推测和阻塞。
4. 输出最小可执行结论。
5. 按影响面回写项目文档、风险、测试报告或日志。

## 输出格式

```markdown
**输入**
- 目标：
- 范围：
- 当前证据：

**分析**
- 权威事实源：
- 关键判断：
- 待确认：

**行动**
- 下一步：
- 回写页面：
```

## 禁止项

- 不把技能写成第二份项目状态页。
- 不复制项目事实、服务实例、数据表、运行 ID 或一次性 handoff。
- 不用技能结论替代正式测试报告、TASK / EP 状态或 Gate 准出证据；TODO 只作轻量兼容视图。
