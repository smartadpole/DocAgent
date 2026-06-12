---
type: retrospective
project: wiki
status: active
updated: 2026-06-12
tags: [retrospective, agent-work, codex-goal, public-guide, collaboration]
---

# Codex Goal 公开教程长对话协作复盘

上游：[[concepts/agent-work-retrospective]]、[[harness-evolution]]、[[harness-feedback-ledger]]、[[log]]

关联对象：[[articles/2026-06-12-codex-goal-mode-public-guide]]、[[views/current/knowledge/codex-goal-public-guide.html]]、[[views/current/knowledge/codex-goal-public-guide-work-items.html]]、[[concepts/codex-goals]]

沉淀路由：复盘档案 + [[harness-feedback-ledger]] observed episode + [[projects/memory/shared]] 的协作风格背景；暂不直接升级硬规则。

## 复盘对象

- **时间范围**：2026-06-12 Codex Goal 教程沉淀、公开 Markdown、HTML 图文页、案例化修订和工程事项版新增的连续对话。
- **对象类型**：Agent 工作复盘 / 知识产物复盘 / 图文呈现协作复盘。
- **复盘目标**：解释为什么一个本应较快收敛的公开教程主题变成长对话，识别 agent 建设、技能触发、产物预检和用户协作模型中的缺口。
- **不做范围**：不重判 Codex Goal 官方事实；不推翻已完成的 Markdown / HTML 产物；不把单次问题直接升级成硬规则或 sensor。

## 原始目标

- **目标**：输出一份可对外发布的 Codex Goal 使用教程，并用 HTML 简要突出一个核心点。
- **非目标**：不暴露本库内部路径、TASK 编号、项目私有语境或处理痕迹；不把 Goal Contract 误包装成官方能力；不让图文 lens 替代官方文档或具体项目验收标准。
- **约束**：公开表达要专业、简洁、可信；案例可以来自实际开发，但要抽象成可展示场景；多个版本应共存而不是互相覆盖。
- **成功口径**：读者能先通过一个实际场景理解为什么需要 Goal，再掌握“目标状态 + 验证循环 + 停止边界”的写法；不同受众有合适版本。

## 实际结果

- **已完成**：
  - 形成公开 Markdown 教程：[[articles/2026-06-12-codex-goal-mode-public-guide]]。
  - 形成通用 HTML 版：[[views/current/knowledge/codex-goal-public-guide.html]]，用“报告页导出闭环”作为实际开发场景入口。
  - 形成工程事项版：[[views/current/knowledge/codex-goal-public-guide-work-items.html]]，用 EP / TASK / ISSUE / REPORT 展示工程治理受众下的 Goal 价值。
  - 两版 HTML 均生成 ignored PDF / PNG，并通过专项和全量检查。
- **未完成**：
  - 尚未把“可外发教程产物预检”固化成模板或技能字段。
  - 尚未形成针对公开页面内部处理词的自动检查。
- **偏离或降级**：
  - 初版 HTML 口吻偏纠偏，不够专业。
  - 初版缺少真实开发场景，读者代入感不足。
  - 案例加入后曾把“脱敏开发案例”这类幕后处理词放进可展示文案。
  - 第二版工程事项链路是用户后续推动才形成，agent 没有提前主动给出“通用版 / 工程治理版”版本策略。
- **超出预期**：
  - 最终沉淀出两个互补版本：通用开发场景版和工程事项治理版。
  - 复盘触发出对用户思维风格和 agent 协作机制的更明确认识。
- **遗留风险**：
  - 后续类似“对外发布教程 / HTML lens”仍可能先产出抽象方法，而不是案例入口。
  - 当前 sensor 能检查 lens provenance 和导出闭环，但不能判断“外发文案是否暴露内部处理痕迹”。

## 关键事实

### 证据地图

- **当前对话上下文**：用户连续指出文案不专业、目标偏、缺少案例、“脱敏开发案例”不可展示、EP → TASK → ISSUE 可作为第二版本，以及当前长对话暴露 agent 建设不足。
- **log**：[[log]] 已记录公开教程、HTML lens、文案修订、实际开发场景入口、工程事项版等连续主题。
- **harness ledger**：[[harness-feedback-ledger]] 已有 Goal Contract、图文 lens、PNG 预览、sensor 降噪等相关 episode；本轮新增 observed episode。
- **git / commit**：相关提交包括 `6eca01f` 公开 Markdown 教程、`bff4036` 初版 HTML、`62bf677` 文案修订、`b76a094` 实际开发场景入口、`99ab307` 工程事项版 lens。
- **受影响页面**：公开教程文章、两个 HTML lens、views 入口、lens registry、log。
- **检查输出**：多轮通过 `python3 scripts/check_all.py --only problem-focused-visual-presentation`、`python3 scripts/check_all.py --only knowledge-linking`、`python3 scripts/check_all.py` 和 `git diff --check`。
- **原始 session / rollout**：未读取完整原始 session；本复盘以当前对话、log、commit 和文件产物为主要证据，足以支撑本轮协作机制判断。
- **缺口**：缺少一份可外发教程的预检清单，无法在首轮自动覆盖案例入口、受众、版本策略和公开措辞。

| 时间 / 节点 | 事实 | 证据 |
| --- | --- | --- |
| 公开教程阶段 | agent 先输出结构化教程，但仍偏方法论，案例叙事不足 | [[articles/2026-06-12-codex-goal-mode-public-guide]]、[[log]] |
| 初版 HTML 阶段 | agent 按问题聚焦技能生成一页式 HTML，但口吻偏“纠偏提醒” | [[views/current/knowledge/codex-goal-public-guide.html]] 历史 diff、[[log]] |
| 文案纠偏阶段 | 用户指出专业性、目标偏移和多余信息问题，agent 才收窄为正向定义 | commit `62bf677`、[[log]] |
| 案例入口阶段 | 用户指出需要实际开发案例，agent 才把“报告页导出闭环”提到首屏 | commit `b76a094`、[[log]] |
| 展示措辞阶段 | 用户指出“脱敏开发案例”不能外展，agent 才去除处理痕迹 | commit `b76a094` 最终内容、[[log]] |
| 第二版本阶段 | 用户主动提出 EP → TASK → ISSUE 链路，agent 才形成工程事项版 | commit `99ab307`、[[views/current/knowledge/codex-goal-public-guide-work-items.html]] |

## Agent 工作回看

- **目标理解**：初始目标“可对外发布教程”被理解到，但没有立即转成“外发读者体验优先”的产物合同。`confirmed`
- **阶段判断**：能够在用户纠偏后切换到文案修订、案例化、版本共存和复盘，但切换依赖用户逐步推动。`confirmed`
- **上下文读取**：官方事实、已有教程、图文技能和事项模型读取充分；但对“公开传播产物”的受众和首屏叙事读取不足。`likely`
- **工具使用**：HTML、Playwright 导出、PNG 预览、专项检查和提交闭环执行稳定。`confirmed`
- **执行策略**：每次局部修订能闭环，但缺少早期总控策略：先选受众、先定案例、先判是否需要多版本。`confirmed`
- **验证质量**：结构、链接、导出和宽度验证充分；文案专业性、外发语感和内部词泄漏主要靠用户人工发现。`confirmed`
- **沟通节奏**：有持续 commentary 更新，但没有在第一次用户指出“目标偏了”后主动暂停做一次完整重定向提案。`likely`
- **权限和边界控制**：文件落位、ignored exports、提交边界基本符合本库规则。`confirmed`
- **沉淀路由**：log 和 lens registry 已同步；本轮复盘前尚未把长对话本身作为 agent 建设缺口沉淀。`confirmed`
- **收尾和提交质量**：各阶段均有检查和 commit；但多次小改形成长对话，也暴露前置预检不足。`confirmed`

## 用户协作风格观察

这些不是对用户的评价，而是后续 agent 应主动适配的协作背景：

- 用户倾向用连续追问把抽象产物压到真实可用、可展示、可验证的形态。
- 用户对“概念边界”和“受众边界”敏感：官方能力、本库治理、模板、skill、规则、公开表达不能混。
- 用户能快速识别外发表达中的处理痕迹，例如“脱敏”“内部”“调试”“lens meta”等不该面向读者的词。
- 用户偏好从案例进入抽象模型，而不是只看方法论框架。
- 用户希望版本关系清楚：补第二版时应共存、标受众和用途，而不是覆盖前一版。
- 用户会把长对话本身视为系统信号：如果靠大量追问才收敛，说明 agent / harness 需要升级。

## 偏差与原因

| 偏差 | 类型 | 证据等级 | 原因判断 | 影响 |
| --- | --- | --- | --- | --- |
| 可外发教程没有先走“受众 + 案例 + 公开措辞 + 版本策略”预检 | Agent 工作 / 协作治理 | confirmed | 图文呈现技能强调结构、证据和导出；缺少公开教程特有的传播预检字段 | 导致用户多轮纠偏文案、案例和受众 |
| 初版过度强调反模式纠偏 | 目标偏差 | confirmed | agent 把 Goal 教程历史中的“误用防线”当成首屏主叙事 | 页面专业度不足，读者接受度下降 |
| 实际案例没有自动前置 | 设计 / 表达偏差 | confirmed | 公开教程生成时沿用模板化示例，缺少“案例入口优先”启发式 | 教程说服力不足 |
| 内部处理词进入展示文案 | 沟通 / 产物质量 | confirmed | agent 把工作过程中的处理语汇写进最终读者文本 | 影响对外发布可信度 |
| 没有主动提出多版本受众分层 | 执行策略 | likely | agent 先追求单页核心点，没有主动判断工程治理受众需要独立版本 | 第二版依赖用户启发才出现 |
| 长对话中没有早触发复盘或重定向 | Workflow | likely | 当前流程缺少“同一产物连续 3 次用户纠偏后暂停重述完成合同”的触发器 | 让用户承担了过多产品经理 / 编辑 / QA 工作 |

## 效率与质量

- **必要成本**：
  - 核对 Codex Goal 官方事实和本库 Goal Contract 边界。
  - 生成 HTML lens、ignored PDF / PNG、PNG 预览和运行专项检查。
  - 为第二版读取 EP / TASK / ISSUE / report 模型，保证工程事项链路没有乱讲。
- **可优化成本**：
  - 文案专业性、案例入口和版本策略本可在首轮预检中一次覆盖。
  - “公开页面禁用内部处理词”本可通过人工 checklist 或轻量 sensor 提前发现。
  - 同一主题多次小改后，agent 本应主动暂停总结“当前完成合同”和“下一版策略”。
- **应避免成本**：
  - 让用户反复指出同一类表达问题。
  - 把内部处理语汇暴露到可展示产物。
  - 在外发教程上只输出抽象方法，缺少入口案例。
- **质量结论**：最终产物质量可接受，但收敛路径过长。问题不在工具执行，而在前置判断：agent 没有把“可外发教程”识别成需要读者路径、案例入口、措辞审校和版本分层的专门产物类型。

## 保留做法

- 公开产品事实仍先以官方文档校准，不把本库治理包装成官方能力。
- 持久 HTML lens 继续同轮生成 ignored PDF / PNG，并在最终回复展示 PNG。
- 对用户纠偏的处理要落到文件、log、commit，而不是只在对话里解释。
- 多版本共存时，使用独立 HTML 文件、registry 入口和明确受众说明。

## 改进行动

| 行动 | owner | 落点 | 完成口径 | 检查方式 |
| --- | --- | --- | --- | --- |
| 形成“可外发教程预检清单”候选：受众、第一案例、核心句、公开措辞、内部词、版本策略、证据来源 | future agent | 候选更新 [[skills/problem-focused-visual-presentation/SKILL]] 或新增更窄技能 | 下次公开教程 / HTML lens 首轮输出前可见这些判断 | 复盘后续任务或 skill diff |
| 记录“同一产物连续多次用户纠偏后暂停重定向”的 workflow 候选 | future agent | [[harness-feedback-ledger]] observed，后续若重复再进 [[response-mode-routing]] | agent 在继续改文件前先复述目标、受众、版本和完成合同 | 后续同类对话抽样 |
| 评估公开产物内部词检查 | future agent | 可能扩展 `scripts/check_problem_focused_visual_presentation.py` 或新增 public-copy lint | 对 public guide / external lens 检出“脱敏、内部、调试、anonymized”等词，并允许白名单 | sensor 草案 + 误报评估 |
| 将用户协作风格作为项目级背景轻量记录 | current agent | [[projects/memory/shared]] | 后续 agent 在教程、对外展示、治理解释中自动带入“案例入口 + 边界敏感 + 版本共存” | 本轮 diff |

## 沉淀路由

- **项目记忆**：[[projects/memory/shared]] 轻量记录用户在公开教程 / agent 协作中的稳定偏好。
- **trace**：不更新；本轮不是项目需求范围变化。
- **决策**：不更新；没有形成需要人工拍板的项目决策。
- **设计**：不更新；暂未新增正式设计方案。
- **研发事项**：不新增 EP / TASK；这是 agent 协作机制复盘。
- **Issue / 事故**：不新增 issue；这是协作质量偏差，不是已发生产品 bug。
- **会议 / 跨 owner 协调**：不需要。
- **模板 / skill**：本轮暂不直接改 skill，先以复盘和 ledger 观察。
- **治理规则 / sensor**：进入 [[harness-feedback-ledger]] observed episode，后续重复时再判断晋升。
- **暂不落地**：不把一次长对话直接变成硬规则；不立即新增 public-copy sensor，避免误报。

## 治理自演进判断

- **单次表现，继续观察**：文案语气偏差和案例入口缺失可先作为本轮复盘记录。
- **重复失守，进入 harness ledger**：长对话由用户连续纠偏推动，且涉及公开产物、图文 lens 和 agent 协作成本，进入 ledger observed。
- **可模板化**：可能形成“公开教程 / 对外展示”预检清单。
- **可技能化**：如果后续多次出现，可在问题聚焦图文呈现技能下加“public tutorial lens”分支。
- **可脚本化**：内部词检查可能脚本化，但需先评估误报。
- **影响 WORKFLOW**：若再次出现同一产物连续多轮纠偏，考虑补“暂停重定向”触发。
- **影响 AGENTS**：本轮不影响必须 / 禁止行为。
- **影响 POLICY**：本轮不改变自动写入或裁定边界。

## 未验证边界

- 未读取完整原始 session / rollout，无法逐条还原每一个 tool call 和 commentary。
- 没有对所有历史公开教程产物做抽样检查，不能证明这是全局重复问题。
- “用户协作风格观察”来自本轮和本库长期上下文，适用于 AcknowledgeBase 的 agent 协作，不应自动上升为所有场景的全局人格标签。
- “公开产物内部词 sensor”只是候选，尚未评估误报和白名单策略。
