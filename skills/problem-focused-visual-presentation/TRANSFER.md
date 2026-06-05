# 问题聚焦式图文呈现迁移清单

## 能力目标

让目标工程的 agent 在面对复杂文档、跨文档主题、项目状态、风险、决策、计划、验收或知识材料时，能自动生成带背景框、证据边界和可视结构的图文 lens，而不是只输出长文字摘要。

## 源资料路径

- `/Users/hai/Documents/Docs/AcknowledgeBase/skills/problem-focused-visual-presentation/SKILL.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/problem-focused-information-presentation.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/ai-era-information-presentation.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/response-mode-routing.md`

## 可以吸收

- 触发条件：信息乱、阅读不方便、一图胜千言、图文混排、HTML 呈现、看文档或看主题。
- 工作流：关注合同、source pack、背景框、图文结构选择、证据追溯、持久化判断。
- 输出格式：一眼判断、背景框、图文主体、证据与追溯、未覆盖边界。
- 视觉类型：表格、脑图、框图、流程图、关系图、时间线、状态卡、证据链图。
- 回写守卫：不把 lens 当第二份真相源，不替代验收 / 关闭 / 准出。

## 只能抽象吸收

- AcknowledgeBase 的 `articles/`、`concepts/`、`skills/`、`views/` 命名方式。
- 本库的 `[[wikilink]]`、`log.md` 和 sensor 结构。
- Life、DocCustomeranalysis、prefect、fetch-adapter、DocFilmCommunity 这些样本事实。

## 禁止复制

- 不复制本库具体项目状态、工程路径、服务实例、报告结论、issue 编号或一次性对话记录。
- 不把目标工程不存在的 `views/` 目录硬套进去。
- 不把 HTML 当唯一输出形式；目标工程可按工具栈选择 Mermaid、SVG、Canvas、PDF、slides 或 dashboard。

## 目标工程落地模块

1. 在目标工程技能层新增等价 skill，写明触发条件、工作流、输出格式和禁止项。
2. 在目标工程 agent 入口规则中加入轻量触发：用户要直观看文档 / 主题 / 状态时，调用该 skill。
3. 在响应模式或 workflow 中加入“图文呈现”模式，说明默认读取、默认写入和持久化边界。
4. 如果目标工程有专题目录或视图目录，建立 current / snapshot 或等价呈现层；没有则先只输出聊天图文 lens。
5. 补入口链接，让用户能从技能目录或专题目录找到该能力。

## 验证要求

- 用一份单文档样本验证：输出必须包含一眼判断、背景框、图文主体和追溯入口。
- 用一个跨多文档主题验证：输出必须呈现材料分层、关系 / 冲突 / 时间线或证据链。
- 检查最终结果没有把历史快照当 current，没有把 lens 当验收或关闭结论。
- 跑目标工程既有检查，并提交同一主题改动。
