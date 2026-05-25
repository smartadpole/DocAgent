---
type: article
date: 2026-05-25
updated: 2026-05-25
tags: [ai-agent, harness-engineering, software-engineering]
---

# Harness Engineering 深度调研

- 来源：
  - 本地归档：[[raw/harness-engineering/2026-05-25-ren-x-harness-engineering.html]]、[[raw/harness-engineering/2026-05-25-wechat-harness-engineering.html]]
  - 外部参考：[Martin Fowler - Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html)、[OpenAI - Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)、[LangChain - Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)、[Vercel - We removed 80% of our agent's tools](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)、[arXiv:2605.13357](https://arxiv.org/abs/2605.13357)、[arXiv:2604.25850](https://arxiv.org/abs/2604.25850)
- 类型：专题调研
- 关联概念：[[concepts/harness-engineering]]

## 一句话总结

Harness Engineering 不是给 AI 多写几句提示词，而是把模型之外的上下文、工具、规则、权限、工作流、验证、日志、记忆和人类决策做成一套可约束、可观测、可校验、可持续演化的工程系统。

## 核心判断

当前这个概念的共识可以压成一句话：

`Agent = Model + Harness`

这里的 `Model` 是推理能力本身，`Harness` 是模型之外所有让它能稳定完成工程任务的结构。它包括：

- `上下文`：AGENTS / CLAUDE 文件、架构文档、dev-map、任务看板、接口文档、设计约束、代码索引。
- `工具`：终端、文件系统、浏览器、MCP、CI、日志系统、发布系统、数据库只读查询能力。
- `规则与技能`：必须遵守的底线、固定任务的 SOP、模型调用前应读什么、交付前应跑什么。
- `工作流`：任务拆分、计划、实现、验证、审查、打回、重跑、提交和发布的接力规则。
- `反馈传感器`：lint、测试、覆盖率、静态分析、架构检查、AI review、人工 review、运行日志、trace、SLO。
- `权限与门禁`：哪些动作能自动做，哪些只能建议，哪些必须人工确认。
- `记录与演化`：失败归因、干预记录、回写文档、脚本化旧错误、删除过期规则。

这意味着：Harness 的目标不是“让模型看起来更聪明”，而是把模型放进一个能稳定收敛到正确结果的工程闭环。

## 和 Prompt / Context Engineering 的关系

Prompt Engineering 主要处理“怎么表达当前请求”。Context Engineering 主要处理“当前请求要给模型哪些信息”。Harness Engineering 的范围更大：它把 prompt 和 context 放进一套执行系统里，还要回答工具怎么接、反馈怎么收、失败怎么归因、权限怎么控、文档怎么回写、旧规则怎么淘汰。

Martin Fowler 的文章把 Harness 拆成 `feedforward guides` 和 `feedback sensors` 很有用：

- `Feedforward` 是行动前约束：架构说明、AGENTS、how-to-test skill、API 文档、MCP 暴露的知识库。
- `Feedback` 是行动后校验：eslint、semgrep、coverage、dependency cruiser、代码审查、架构审查、mutation testing、运行时 SLO 和日志异常采样。

所以 Context Engineering 更像 Harness 的一个子能力；Harness Engineering 还负责把这些上下文和反馈安排到完整的软件变更生命周期里。

## 为什么会在 2026 年变成显性主题

### 1. 模型能力已经跨过“能写代码”的门槛

当模型还很弱时，主要问题是它不会写。模型变强后，瓶颈变成：它会写，但不一定在正确上下文里写；会修，但不一定修到真实根因；会交付，但不一定知道什么叫完成。

### 2. 人类注意力成为稀缺资源

OpenAI 的 Codex 实验把工程师角色重新定义为“设计环境、表达意图、构造反馈循环”。它不是让人消失，而是把人的主要精力从手写代码上移到系统设计、规格裁定、反馈闭环和熵管理。

### 3. 真实工程不能只靠一次性输出

真实工程里有旧代码、约束、测试、兼容、部署、数据迁移、权限、发布和回滚。一次性生成很容易成功，持续迭代才会暴露规则腐烂、上下文膨胀、验证缺口和职责不清。

### 4. “更多工具”不等于“更强 Agent”

Vercel 的案例很有代表性：删除 80% 工具，改用文件系统和更好的数据 / 文档结构，反而让执行时间、token、步骤数和成功率都改善。它说明 Harness 的价值不是堆能力，而是让模型面前的选择空间更可理解。

## 组件地图

### 1. 规格层：先定义要做什么

规格层回答：任务目标、边界、验收标准、非目标、兼容要求、人工确认点是什么。

本地微信长文里的 JK Launcher 案例强调，第一步不是写 Rule、拆 Agent 或上脚本，而是先把 SPEC 和 AI 反复磨透。这个判断是对的：如果规格不清，后面的规则和脚本只会把模糊目标包装得更复杂。

### 2. 上下文层：给 AI 地图，不给百科全书

OpenAI 的做法是把 `AGENTS.md` 当目录，而不是百科全书；真正的知识放在结构化 `docs/` 中。这个原则可以概括为：

- 根入口短，负责指路。
- 正文分层，负责事实。
- 文档可链接、可校验、可维护。
- 上下文按阶段提供，不一次性塞满窗口。

这和本库的七层模型高度一致：[[README]] / [[INDEX]] 是入口，[[AGENTS]] 是执行约束，[[BRAIN]] / [[POLICY]] / [[WORKFLOW]] 是治理层，`projects/` 是项目运行层，`articles/` / `concepts/` 是知识沉淀层。

### 3. 规则层：减少低级错误，但不迷信软约束

Rule 的价值是告诉 AI 什么不能乱来，例如必须编译、必须测试、不能改某些路径、不能把真实密钥写进文档。但 Rule 是软约束，会忘、会误判相关性，也会被解释性执行。

成熟 Harness 会把 Rule 当起点，而不是终点。能机器判定的规则，应逐步下沉成脚本、CI、lint、schema、类型系统或权限门禁。

### 4. Skill 层：高频动作标准化

Skill 解决的是“同一类动作不要每次临场发挥”。例如：

- 编译怎么找环境、怎么收日志、怎么判断失败。
- 测试怎么选范围、怎么处理 flaky、怎么给出未验证边界。
- 代码审查怎么按风险排序、怎么区分 bug / 风格 / 残余风险。
- 源码审计怎么定义深度等级、证据矩阵和未读清单。

Skill 不是项目事实单一信息源，它是可复用流程和判断框架。

### 5. Workflow / Sub-agent 层：把复杂任务拆成接力

多 Agent 的重点不是“角色名好看”，而是防止一个模型自己写需求、自己设计、自己实现、自己审自己。有效拆分要写清：

- 每个阶段读什么。
- 每个阶段产出什么。
- 谁能接下一棒。
- 什么情况必须打回。
- 打回后回到哪一阶段重跑。
- 交接记录写在哪里。

没有 Workflow 的 Sub-agent 只是多人格；有 Workflow 的 Sub-agent 才是工程接力。

### 6. Scripts / Sensors 层：用可执行反馈定义完成

本地微信长文和 Martin Fowler 都把反馈层放在核心位置。它的本质是：不接受“我觉得好了”，只接受证据。

常见反馈传感器可以分层：

- 快速本地层：格式化、lint、类型检查、单元测试、最小 smoke。
- 变更审查层：AI review、人工 review、架构规则、依赖边界、死代码、覆盖率质量。
- 集成层：CI、端到端测试、迁移检查、回归套件、安全扫描。
- 运行层：日志异常、SLO、错误率、成本、延迟、用户路径采样。

越早能发现的问题，越应该往左移动；越昂贵、越全局的检查，越适合放在集成或持续监控层。

### 7. MCP / 外部系统层：把 AI 接进工程系统

MCP 不等于 Harness 主体，它是外接能力层。它适合承接：

- CI 构建触发和日志读取。
- 制品上传、签名、发布、灰度状态读取。
- 设计系统、知识库、表格、Issue、PR、日历等外部事实读取。
- Unity / IDE / 浏览器 / 运行时宿主的受控操作。

关键不是“能接”，而是接入能力要被权限、日志和门禁约束。凭据、真实发布、数据库写入、外部状态回写不能散落在 prompt 和临时命令里。

### 8. Memory 层：团队真相源优先文件化

微信长文的第十章判断也很重要：团队级 Harness 的主场不是隐藏 memory，而是仓库里可审计、可交接、可链接的资产。

Memory 可以辅助个人偏好、会话延续和检索，但团队共识应优先进入：

- SPEC
- AGENTS / Rule
- Skill
- Scripts
- dev-map
- 任务看板
- 设计 / 决策 / 测试报告

隐藏 memory 如果没有回写机制，很容易变成不可审计的第二真相源。

## 案例信号

### OpenAI Codex：仓库知识是系统记录

OpenAI 的案例不是“模型替代工程师”，而是“工程师设计代理可工作的环境”。几个信号很关键：

- 空仓库起步，初始脚手架、CI、格式化、包管理和 AGENTS 都由 Codex 生成。
- 五个月后约百万行代码、约 1500 个 PR，由小团队驱动。
- 人类不直接写代码，而是定义任务、审查反馈、构建环境和反馈闭环。
- `AGENTS.md` 被控制成短入口，深层知识进入结构化 `docs/`。

对本库的启发：根级 [[AGENTS]] 适合做执行入口和路由，不适合无限膨胀成百科全书。

### LangChain Deep Agents：只改 Harness 也能显著涨分

LangChain 在 Terminal Bench 2.0 上固定模型 `gpt-5.2-codex`，通过迭代 harness 把 deepagents-cli 从 52.8 提到 66.5。它的关键不是某句提示词，而是：

- 用 trace 分析失败模式。
- 把 trace 分析做成可重复 Skill。
- 聚焦 system prompt、tools、middleware 这几个可控旋钮。
- 强化自验证和推理预算安排。
- 防止对单个任务过拟合。

这说明 Harness 是可实验、可度量、可迭代的工程对象。

### Vercel：工具越少，选择空间可能越好

Vercel 删除大量自定义工具后，用文件系统作为主抽象，结果在代表性查询上更快、更少 token、更少步骤且成功率更高。它的边界同样明确：这能成立，是因为语义层本身已经有清晰文档、命名和结构。

启发：别急着给 Agent 包装一堆工具。先检查文件、文档、数据、命名和搜索路径是否足够清楚。工具是在弥补真实行为缺口，不是为了看起来完整。

### JK Launcher：从 SPEC 到脚本门禁再到 dev-map

本地长文最有价值的是落地顺序：

1. 先磨规格设计文档。
2. 再补 Rule，约束底线。
3. 把编译、测试、验证做成 Skill。
4. 引入 Sub Agent 和 Workflow，把复杂任务拆成接力。
5. 把可判定约束下沉成总验证脚本。
6. 持续迭代后再补 dev-map 和任务看板。
7. 外部构建、签名、制品、发布、回写再考虑 MCP。

这个顺序比“一上来全套多 Agent + MCP”更稳。

### X 图文：三条反直觉原则

本地 X 图文把 Harness 压成几个直观判断：

- 工具不是越多越好。每接一个工具，先问它补哪个行为缺口。
- 上下文不是越长越好。关键信息应放在头尾，并按频率分层。
- Harness 不是越厚越安全。模型变强后，要删掉过期补丁，保持刚刚够用。

这可以作为 Harness 体检的轻量准则：少一点堆料，多一点工程判断。

### 学术化趋势：Harness 正在变成运行时研究对象

arXiv:2605.13357 把 Harness 形式化为运行时基底，列出任务规格、上下文选择、工具访问、项目记忆、任务状态、可观测性、失败归因、验证、权限、熵审计和干预记录等职责，并提出 H0-H3 阶梯和 episode package。

arXiv:2604.25850 则把 Harness 演化本身做成闭环，强调组件可观测、经验可观测和决策可观测；它的结论倾向于：收益主要来自工具、middleware 和长期 memory 等结构性组件，而不只是 system prompt。

这些论文还需要继续验证，但方向很明确：Harness 不再只是经验手册，而会逐渐变成可观测、可比较、可自动演化的运行时系统。

## 成熟度模型

### H0：裸模型 / 裸对话

- 只有 prompt，没有项目结构入口。
- 验收靠模型自报。
- 适合一次性小任务，不适合长期工程。

### H1：轻量规则和上下文

- 有 AGENTS / CLAUDE / README。
- 有最小测试命令和目录约定。
- 仍然主要靠人提醒和人工验收。

### H2：可执行反馈闭环

- 有统一 lint / test / smoke / link check。
- 有清晰的完成定义。
- 失败能形成可回看的日志和修复动作。

### H3：流程化接力

- 有 SPEC、任务状态、计划、实现、审查、测试和回写规则。
- Skill 处理高频动作。
- Sub Agent 或角色分工开始有明确交接材料。

### H4：工程交付闭环

- 接入 CI、制品、签名、部署、发布、回滚、运行观测。
- MCP 或等价工具层受到权限和审计约束。
- 每次交付不只证明代码对，还证明工程动作闭环。

### H5：可观测自进化

- Trace、episode package、失败归因和 harness 变更形成闭环。
- Harness 改动有预测、有验证、有回滚。
- 人类负责方向、边界和最终责任，AI 在既定规则中高密度落地。

## 落地顺序建议

### 1. 从最痛的重复失败开始

不要为了“搭 Harness”而搭。先列出 AI 反复犯的 5 到 10 类错误：

- 总忘记跑测试。
- 总改错目录。
- 总覆盖用户已有改动。
- 总把日志现象当根因。
- 总把局部验证写成完整通过。
- 总把临时聊天结论留在最终回复里，不回写文件。

每个错误先判断：该进 Rule、Skill、Script、Workflow、MCP，还是该改文档入口。

### 2. 先做最小可用 Harness

一个小项目的最低可用版本可以只有：

- 根级 `AGENTS.md`：短入口、边界、必读页。
- `docs/` 或项目内 README：真实知识单一信息源。
- `scripts/check`：最小验证入口。
- `log` 或 worklog：记录关键动作和残余风险。
- PR / handoff 模板：固定交付输出。

### 3. 把软规则逐步脚本化

Rule 先覆盖不可遗漏的底线；一旦同类错误重复出现，就问：

- 能不能用脚本检查？
- 能不能用类型系统 / schema / lint 表达？
- 能不能放进 CI？
- 能不能在提交前自动跑？
- 能不能在失败时输出可读修复建议？

### 4. 等任务复杂后再拆多 Agent

多 Agent 的引入条件不是“想高级”，而是出现：

- 一个任务跨需求、设计、实现、验证多个角色。
- 自我审查不可靠。
- 阶段交接材料开始变多。
- 失败需要回退到特定阶段，而不是让同一个 Agent 继续圆。

### 5. 外部系统最后接，并带权限设计

CI、发布、签名、数据库写入、工单状态回写都不该一开始暴露给 AI。先让本地开发闭环可验证，再逐步接外部系统，并写清：

- 谁允许调用。
- 哪些参数可变。
- 哪些动作只读。
- 哪些动作必须人工确认。
- 结果写回哪里。

## 常见反模式

- `一个巨大的 AGENTS.md`：短期方便，长期腐烂，且挤占上下文。
- `只有 Rule 没有检查`：看似有制度，实际仍靠模型自觉。
- `工具堆叠`：每个工具都是选择压力，过多工具会让模型迷路。
- `隐藏 memory 当真相源`：团队无法审计，交接时失效。
- `多 Agent 没有 Workflow`：只是多角色聊天，没有接棒条件。
- `CI 只做事后判死刑`：反馈太晚，修复成本高。
- `文档不回写`：Harness 只在一次会话里生效，下一轮重新犯错。
- `过期规则不删除`：模型变强或项目变化后，旧补丁会变成噪声。

## 对当前文档库的启发

当前 wiki 本身已经很像一个文档型 Harness：

- [[AGENTS]] 是 agent 执行约束和入口。
- [[WORKFLOW]] 是流程编排。
- [[POLICY]] 是自动沉淀和冲突裁定。
- [[BRAIN]] 是共享背景。
- `projects/` 是项目运行层。
- `skills/` 是可复用 agent 动作。
- `templates/` 是交付骨架。
- [[log]] 是过程记录和干预记录。

可以考虑的后续增强，不必本轮立刻做：

- 增加 Markdown 链接 / wikilink 检查脚本，作为知识库 feedback sensor。
- 增加 frontmatter schema 检查，减少页面类型漂移。
- 增加 source-to-article 模板，把 `raw -> articles -> concepts -> indexes -> log` 的链路变成可复用动作。
- 给 `skills/` 增加验证清单：触发条件、事实源、禁止项、输出格式、回写边界是否齐全。

## 未解决问题

- Harness 应该做到多厚：太薄靠运气，太厚会干扰模型。
- 哪些 harness 组件能跨模型迁移，哪些必须按模型重新调优。
- Self-improving harness 如何避免过拟合、刷榜和错误归因。
- 团队级 memory 如何与文件化真相源共存。
- 代理执行权限如何在效率、审计和安全之间平衡。
- 如何把 Harness ROI 从“感觉更稳”变成可度量指标。

## 后续动作

- 如果后续要把这个概念用于当前 wiki 本体演进，优先从 `feedback sensor` 入手，而不是新增规则正文。
- 如果用于具体代码仓库，先按“重复错误清单 -> 最小 Harness -> 脚本化 -> 多 Agent -> MCP”的顺序推进。
- 如果继续调研，应优先补：LangChain trace 分析方法、OpenAI docs-as-system-of-record 结构、Martin Fowler 的 regulation categories、AHE 的可观测演化框架。
