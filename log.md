# 活动记录

> 历史不重写；新记录按时间降序插在前面，并按日期下的对话组织。

`[[log]]` 只负责承接历史记录。

- 详细记录规则见 [[log-writing-rules]]。
- 默认模板见 [[templates/log-entry-template]]。

## 2026-06-05

### 同步 PDF 导出能力到专题方案页

- **记录人**：sunhao
- **用户意图**：用户指出 PDF / A4 / A3 / 打印导出不应只进入技能说明，专题知识库里的相关方案也应吸纳进去。
- **主题**：
  1. 将 PDF / print view 从技能执行细节同步为问题聚焦式信息呈现专题方案的一部分。
  2. 把 `export_profile` / `print_profile` 纳入跨工程校准的 lens 运行机制，明确导出版式不是收尾截图，而是设计期约束。
  3. 更新上位调研和入口摘要，让用户从调研文章、专题方案、INDEX 和 articles 入口都能发现导出打印能力。
- **关键动作**：
  1. 更新 [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]，补充用户目的、方案修正、运行流程和方案边界中的 PDF / A4 / A3 / 打印导出要求。
  2. 更新 [[articles/2026-06-05-ai-era-information-presentation-research]]，在问题视角选择矩阵、本库启发、PPT / PDF 边界和常见误区中补入导出打印策略。
  3. 更新 [[INDEX]] 和 [[articles/README]]，把专题能力摘要扩展为 current / snapshot / source refresh / background frame / user entry / PDF export。
- **结论**：导出打印现在属于专题方案，而不只是 agent 技能实现细节。后续设计图文 lens 时，只要存在下载、打印、线下批注或分发需求，就要在方案层同步考虑 A4 / A3、横竖版、分页、页眉页脚、来源页脚、图表裁切和 PDF / snapshot 边界。
- **影响页面**：[[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]、[[articles/2026-06-05-ai-era-information-presentation-research]]、[[INDEX]]、[[articles/README]]、[[log]]。

### 升级图文 lens 的 PDF 导出和打印版式能力

- **记录人**：sunhao
- **用户意图**：用户要求继续升级问题聚焦式图文呈现技能，使其支持导出；如果采用 HTML 样式，应支持导出 PDF，并且在设计阶段就适配 A4、A3 等页面大小，横排竖排不限制，便于下载和打印。
- **主题**：
  1. 将“导出 / 打印”从事后附加能力提升为图文 lens 的设计期能力。
  2. 明确 HTML current lens、PDF export 和 snapshot 的分工：HTML 负责交互和当前视图，PDF 负责下载、打印、线下批注和分发，关键节点 PDF 才作为 snapshot 固化。
  3. 补齐 `export_profile` 和 `print_profile`：页面尺寸、横竖版、边距、分页、页眉页脚、图表裁切、重复表头、来源和证据边界。
  4. 强化迁移边界：目标工程迁移该技能时也要迁走 PDF / print view 能力，不能只迁走 lens 结构。
- **关键动作**：
  1. 更新 [[skills/problem-focused-visual-presentation/SKILL]]，把 PDF 导出、A4 / A3、横竖版、分页策略、print CSS 和 PDF 检查加入触发描述、关注合同、输出模板、持久化判断和自检。
  2. 更新 [[concepts/problem-focused-information-presentation]]，把导出 / 打印加入最终呈现层级，并补充 `export_profile`、`print_profile` 和常见误区。
  3. 更新 `skills/problem-focused-visual-presentation/TRANSFER.md`，要求跨工程迁移时同步吸收 HTML print view、PDF export、页面规格和打印验证。
- **结论**：问题聚焦式图文呈现不应只停在“好看的 HTML 页面”。当用户可能下载、打印或线下流转时，agent 必须在设计阶段考虑 PDF 导出和页面版式；A4、A3、横排、竖排、边距、分页和图表裁切都是 lens 设计的一部分。PDF 是从 HTML / 图文 lens 派生的打印和分发产物，不替代 Markdown 真相源。
- **影响页面**：[[skills/problem-focused-visual-presentation/SKILL]]、[[concepts/problem-focused-information-presentation]]、`skills/problem-focused-visual-presentation/TRANSFER.md`、[[log]]。

### 校准信息呈现趋势为页面化 lens

- **记录人**：sunhao
- **用户意图**：用户指出“HTML 本身成为趋势”这个说法不够准确，真正趋势是信息呈现从长 Markdown / 长文档转向可交互、可视化、可追溯的页面化 lens；用户要求判断这段内容是否有价值，并补充到知识库。
- **主题**：
  1. 把 HTML、OpenAI Canvas、Notebook、dashboard、Artifact、Mermaid、ECharts / D3、SVG 和 Canvas 图形统一归为呈现层输出家族，而不是新的信息架构本身。
  2. 明确“真相源结构化，呈现层按问题生成”：Markdown / YAML / issue / log / report / code / data snapshot 保持事实和审计，图文 lens 负责当前阅读和决策。
  3. 补齐输出形态选择矩阵：简单问答用短 Markdown，状态 / 风险 / 计划 / 验收用 lens 页面和矩阵，故障用时间线和证据链，决策用 decision matrix，数据探索用 HTML report / Notebook / dashboard，说明文档仍用 Markdown。
  4. 强化 canonical current lens 与 snapshot 的分工，并要求 lens 带 `source`、`generated_at`、`evidence_boundary`、`context_frame` 和 `refresh_trigger`。
- **关键动作**：
  1. 更新 [[articles/2026-06-05-ai-era-information-presentation-research]]，把原先偏“HTML 化”的表述校准为页面化 lens，并补入 Streamlit、ECharts 和问题视角的呈现选择矩阵。
  2. 更新 [[concepts/ai-era-information-presentation]]，把“页面化 lens 不是所有内容 HTML 化”写入基本原则和常见误区。
  3. 更新 [[concepts/problem-focused-information-presentation]]，补充最终呈现形态的趋势定义和输出形态选择表。
  4. 更新 [[skills/problem-focused-visual-presentation/SKILL]]，让 agent 在执行图文呈现前先判断短答、Markdown 真相源、页面化 lens、交互报告或归档快照。
- **结论**：这段内容有高价值，因为它把本专题从“HTML 是更好的阅读格式”继续校准为“问题聚焦式呈现层”。后续本库和 agent 体系应避免把 HTML 当成目标本身；真正目标是每次围绕当前关注对象生成合适的图文 lens，并始终回链真相源和证据。
- **影响页面**：[[articles/2026-06-05-ai-era-information-presentation-research]]、[[concepts/ai-era-information-presentation]]、[[concepts/problem-focused-information-presentation]]、[[skills/problem-focused-visual-presentation/SKILL]]、[[log]]。

### 升级问题聚焦式图文呈现为 agent 技能

- **记录人**：sunhao
- **用户意图**：用户要求升级当前 agent 体系，使其真正具备“问题聚焦式图文呈现”能力，而不是只在知识库里保存专题概念。
- **主题**：
  1. 将 [[concepts/problem-focused-information-presentation]] 从知识库专题进一步接入 agent 执行体系。
  2. 新增可触发技能，使 agent 在用户要看文档、主题、状态、风险、决策、计划、验收或知识材料，并强调直观、图文混排、一图胜千言、HTML 呈现或阅读不方便时，自动进入图文呈现流程。
  3. 把图文呈现作为独立响应模式接入 [[response-mode-routing]] 和 [[WORKFLOW]]，明确默认读取、默认写入、持久化边界和检查要求。
  4. 将根 [[AGENTS]] 的会话级规则更新为识别图文呈现模式，避免以后仍把长文字摘要当作最终体验。
- **关键动作**：
  1. 新增 [[skills/problem-focused-visual-presentation/SKILL]]，定义关注合同、source pack、背景框、图文结构选择、输出 lens、持久化判断和自检。
  2. 新增 `skills/problem-focused-visual-presentation/TRANSFER.md`，为后续迁移到其他工程提供资料路径、吸收边界、禁止复制项、落地模块和验证要求。
  3. 更新 [[skills/README]] 和 [[INDEX]]，把该能力加入技能入口和总入口。
  4. 更新 [[response-mode-routing]]、[[WORKFLOW]] 和 [[AGENTS]]，把“图文呈现”变成 agent 可识别、可执行的响应模式。
  5. 更新 [[concepts/problem-focused-information-presentation]]，反向链接到新技能，保持概念层和技能层分工清楚。
- **结论**：问题聚焦式图文呈现现在已从专题方案升级为 agent 可执行技能。后续用户要求“看一份文档 / 一个主题 / 当前状态 / 风险 / 验收 / 知识”，且目标是直观展示时，agent 应先生成带一眼判断、背景框、图文主体、证据追溯和未覆盖边界的 lens；只有用户要求持久视图或已有呈现层时，才写入 HTML / 图文文件。
- **影响页面**：[[skills/problem-focused-visual-presentation/SKILL]]、`skills/problem-focused-visual-presentation/TRANSFER.md`、[[skills/README]]、[[INDEX]]、[[response-mode-routing]]、[[WORKFLOW]]、[[AGENTS]]、[[concepts/problem-focused-information-presentation]]、[[log]]。

### 设计问题聚焦式信息呈现专题

- **记录人**：sunhao
- **用户意图**：用户指出复杂系统的信息展示不应是一次性 dashboard，而是在每次关注某个问题时都有合适展示；随后进一步校准本轮是知识库专题和方案设计，不是开发，并强调 Life / DocCustomer 只是复杂度参考，目标应覆盖所有信息类型。用户继续追问“关注对象 / 展示视角 / 信息分层”是否完整，要求检查风险、验收、知识等对象覆盖是否充分；随后纠正最终阅读体验不应默认停在 Markdown，复杂信息应优先采用 HTML 呈现。用户进一步追问多次对话问到同一问题时 HTML 文件应更新还是新增、HTML 文件放在哪里、HTML 是否应形成面向用户的体系；随后要求多看 Life、DocCustomeranalysis、prefect、fetch-adapter、DocFilmCommunity 等工程样本，结合工程重新分析用户目的并完善方案；最后进一步校准主要目的其实是“一图胜千言”，复杂文字信息需要表格、脑图、框图等图文混排，HTML 只是优先承载方式，若 HTML 不足应另想办法，并强调展示对象既可能是单文档也可能是跨文档主题，必须呈现其所处背景。
- **主题**：
  1. 将本轮从软件开发或固定 dashboard 方案，校准为知识库专题设计。
  2. 复用 [[articles/2026-06-05-ai-era-information-presentation-research]] 中“源、索引、关系、界面、归档”五层模型，进一步补出面向当前关注问题的阅读 lens 层。
  3. 把 Life / DocCustomer 从目标对象降为参考样本，抽象出状态、计划、决策、故障、验收、知识、资源、owner、时间线等通用信息类型的展示协议。
  4. 对照用户列出的关注对象、展示视角和三层信息分层，补齐独立的关注对象分类，并把风险从信息类型提升为可选主 lens。
  5. 区分 Markdown 真相源 / 生成输入和 HTML 最终阅读界面，避免把可维护格式误当作复杂信息的最佳呈现格式。
  6. 设计图文 lens 的生命周期和存放体系：当前视图与历史快照分工、统一呈现层目录、lens registry、按用户关注对象组织入口。
  7. 用 Life、DocCustomeranalysis、prefect、fetch-adapter 和 DocFilmCommunity 做只读横向校准，把方案从信息类型分类推进到 current / snapshot、源刷新、证据上推和用户入口体系。
  8. 将“HTML lens”校准为“图文混排 lens”：HTML 是默认容器，不是能力上限；当表格、脑图、框图、流程图、时间线或关系图更能降低认知成本时，应优先可视化。
  9. 补出单文档 lens 和跨文档主题 lens 的对象粒度，并要求每个 lens 呈现上位背景、来源背景、历史背景、关系背景和使用边界。
- **关键动作**：
  1. 新增并校准 [[concepts/problem-focused-information-presentation]]，定义问题聚焦式信息呈现的目标、基本模型、最终呈现形态、图文 lens 生命周期、存放体系、用户视角体系、关注对象分类、通用 lens、信息类型视角、设计原则、常见误区和后续演进方向。
  2. 更新 [[concepts/ai-era-information-presentation]] 和 [[articles/2026-06-05-ai-era-information-presentation-research]]，说明问题聚焦式 lens 是原有记录 / 组织 / 处理 / 呈现 / 归档模型的方案化延伸。
  3. 新增并继续校准 [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]，记录跨工程样本、用户目的判断、方案修正和图文 lens 运行流程。
  4. 更新 [[INDEX]] 和 [[articles/README]]，并沿用 [[concepts/README]] 中已有的概念入口，让该概念和横向校准文章能从设计思路、摘要卡片层和概念层入口被发现。
- **结论**：复杂系统的直观展示应以“当前关注问题”而不是“固定总览页”为中心；每次先定关注对象和判断目的，再选择状态卡、证据链、决策矩阵、行动地图、时间线、关系图或专题卡等 lens，并明确一眼判断层、证据解释层和原始追溯层。关注对象主类至少覆盖状态、问题 / 故障 / 异常、决策、计划、风险、验收 / 关闭、知识、资源 / 资产、关系 / owner 和时间线 / 演进。Markdown 负责真相源和生成输入，复杂信息的最终阅读体验应优先走图文混排 lens；HTML 是默认容器，但如果 HTML 排版不能充分表达，应补充 SVG、Canvas、Mermaid、ECharts / D3、Excalidraw 导出图、PDF / slide、独立图片或 HTML + assets 组合包。同一个稳定关注对象默认维护一个 canonical lens；只有验收、决策、发布、事故、阶段复盘、外部分发或证据固化时，才生成 snapshot。展示对象既可以是一份文档，也可以是跨多文档主题；每个 lens 都必须呈现上位背景、来源背景、历史背景、关系背景和使用边界。跨工程校准进一步确认：同一问题再次出现时应先解析 lens id、刷新最小 source pack、更新 current，再判断是否需要 snapshot；不同工程可以声明自己的高频 lens pack，但通用层只定义关注对象、证据边界、刷新流程、registry、背景框和 provenance。
- **影响页面**：[[concepts/problem-focused-information-presentation]]、[[concepts/ai-era-information-presentation]]、[[articles/2026-06-05-ai-era-information-presentation-research]]、[[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]、[[INDEX]]、[[articles/README]]、[[concepts/README]]、[[log]]。

### 调研 AI 时代信息记录、处理与呈现方式

- **记录人**：sunhao
- **用户意图**：用户要求完整调研 AI 时代信息呈现方式的演进，从文档 chunk 化和向量检索，到 Karpathy 带动的 Markdown + 超链接关系网，再到用 HTML 实时呈现信息结果、弱化 PPT 默认地位。
- **主题**：
  1. 将本轮判定为知识沉淀 / 调研沉淀模式，落位到 `articles/` 摘要卡片和 `concepts/` 概念页，而不是项目运行链路。
  2. 外部核验 RAG / chunking、Karpathy Software 3.0、`llms.txt`、MCP、Claude Artifacts、ChatGPT Canvas、Quarto 和 Observable 等来源。
  3. 将结论收口为“Markdown 真相源、向量索引、超链接关系网、HTML 交互呈现、PPT / PDF 分发归档”的分层模型。
  4. 用户进一步指出“信息记录 / 信息处理 / 信息呈现”需要分开，并追问 HTML 是否也会成为记录形式；据此补查 HTML、W3C Web Standards、HtmlRAG、WARC 和 MHTML 等来源，重构为三职能模型。
  5. 用户要求进一步做全面深入调研，补入历史信息和最新技术，并参考专业知名网站及名人主页；据此扩展 Bush、Engelbart、Nelson、Berners-Lee、Ward Cunningham、Gruber / Swartz、Tufte、Bret Victor、Karpathy、Jeremy Howard、Anthropic、OpenAI、Observable 和 Quarto 等来源。
- **关键动作**：
  1. 新增并校准 [[articles/2026-06-05-ai-era-information-presentation-research]]，梳理文件记录、chunk / vector 处理、Markdown 记录 + 处理、HTML 实时呈现、HTML 记录边界、历史谱系、名人和专业网站观点地图、最新技术谱系、对比矩阵、场景选择矩阵、推荐架构和本库启发。
  2. 新增并校准 [[concepts/ai-era-information-presentation]]，作为后续判断信息记录、组织、处理、呈现和归档形态的概念入口，并补充可读性、可寻址性、可关系化、可计算性、可呈现性、可复现性、可归档性和可治理性八类 guarantee。
  3. 更新 [[INDEX]]、[[articles/README]] 和 [[concepts/README]]，让新调研能从入口和上位概念被发现。
- **结论**：AI 时代信息结构不是单一工具替代，而是记录、组织、处理、呈现和归档的职责分离；向量库负责处理层召回，Markdown 同时承担轻量记录和模型处理主链，语义静态 HTML 可成为记录格式，动态 HTML / Artifact / Notebook 默认是实时呈现和探索界面，PPT / PDF / WARC / MHTML 保留分发或归档边界。最终判断不看文件后缀，而看格式是否提供可读、可寻址、可关系化、可计算、可呈现、可复现、可归档和可治理的保证。
- **影响页面**：[[articles/2026-06-05-ai-era-information-presentation-research]]、[[concepts/ai-era-information-presentation]]、[[INDEX]]、[[articles/README]]、[[concepts/README]]、[[log]]。

## 2026-06-04

### Agent 指令共享的 Codex thin adapter 口径校准

- **记录人**：sunhao
- **用户意图**：用户追问 DocCustomeranalysis 中“`.codex/AGENTS.md` 也仿照 `CLAUDE.md` 导入根 `AGENTS.md`”的新设计是否已经沉淀到本库 `concepts/agent-instruction-sharing.md` 及相关文档中。
- **主题**：
  1. 确认 [[concepts/agent-instruction-sharing]]、[[AGENTS]]、[[README]]、[[INDEX]]、[[governance/README]]、[[governance/platform-standards]]、[[projects/decisions]]、[[harness-feedback-ledger]] 和 `scripts/check_harness_governance.py` 仍残留“删除 / 不维护 `.codex/AGENTS.md`”的旧口径。
  2. 将概念页更新为“根 `AGENTS.md` 是唯一规则正文；`CLAUDE.md` 和可选 `.codex/AGENTS.md` 是工具入口壳；`.codex/AGENTS.md` 如存在必须通过 `@../AGENTS.md` 指回根规则，不能复制共享治理正文”。
  3. 同步入口页、治理页、平台标准、决策记录、Harness ledger 和检查脚本，改为允许 thin Codex adapter、禁止重复规则正文。
- **关键动作**：
  1. 更新 [[concepts/agent-instruction-sharing]] 的推荐结构、Codex 适配入口处理、最小实现、判断规则和常见误区。
  2. 更新 [[AGENTS]]、[[README]]、[[INDEX]]、[[concepts/README]] 和 [[governance/README]]，把“唯一入口”改为“唯一规则正文 + 工具薄入口”。
  3. 更新 [[governance/platform-standards]]、[[projects/decisions]]、[[harness-feedback-ledger]] 和 `scripts/check_harness_governance.py`，使 sensor 检查词覆盖 `thin Codex adapter` 和 `@../AGENTS.md`。
- **结论**：Agent 指令共享知识已从“删除 `.codex/AGENTS.md`”校准为“规则正文唯一 + 工具入口薄适配”。后续跨工程采纳时，应先把 `.codex/AGENTS.md` 的有效规则并入根 [[AGENTS]]，再按项目需要删除旧文件或改成 `@../AGENTS.md` thin adapter。
- **影响页面**：[[concepts/agent-instruction-sharing]]、[[AGENTS]]、[[README]]、[[INDEX]]、[[concepts/README]]、[[governance/README]]、[[governance/platform-standards]]、[[projects/decisions]]、[[harness-feedback-ledger]]、`scripts/check_harness_governance.py`、[[log]]。

### 统一项目级 Agent 规则入口

- **记录人**：sunhao
- **用户意图**：用户指出当前方案仍可能让其他工程同时维护根 `AGENTS.md` 和 `.codex/AGENTS.md` 两份项目规则，要求只保留根目录 `AGENTS.md`，把 `.codex/AGENTS.md` 的有效内容归入根入口。
- **主题**：
  1. 确认 `.codex/AGENTS.md` 虽然是 Codex 适配壳，但仍会形成第二份项目级规则入口，和刚建立的 Claude / Codex 共享规则目标冲突。
  2. 将项目级 agent 规则收口为唯一根 `AGENTS.md`；`CLAUDE.md` 只做 Claude Code import 壳，`.codex/` 只做 Codex 专用配置或 subagent 外壳。
  3. 将本轮纠偏升级为设计裁决和 sensor：以后发现 `.codex/AGENTS.md`，应合并回根 `AGENTS.md`，而不是继续维护两份规则。
- **关键动作**：
  1. 删除 `.codex/AGENTS.md`，把其中有效启动、检查和写入边界规则并入 [[AGENTS]] 的“工具入口统一”段。
  2. 更新 [[README]]、[[INDEX]]、[[governance/README]]、[[concepts/agent-instruction-sharing]]、[[governance/platform-standards]]、[[projects/decisions]]、[[harness-feedback-ledger]]、[[skills/cross-project-governance-audit/SKILL]] 和 [[skills/issue-analysis/SKILL]]，统一根 `AGENTS.md` 单一入口口径。
  3. 更新 `scripts/check_harness_governance.py`，不再要求 `.codex/AGENTS.md` 存在，反而把它作为重复项目级规则入口报错。
- **验证**：`python3 scripts/check_all.py --only harness-governance` 通过；`python3 scripts/check_all.py` 通过；`git diff --check` 通过。
- **二阶反思**：工具适配壳也会变成规则漂移源。共享 agent 体系应区分“项目级规则单一入口”和“工具专用配置 / subagent 外壳”，不能因为 Codex 或 Claude 各有目录就复制项目规则。
- **影响页面**：[[AGENTS]]、`CLAUDE.md`、[[README]]、[[INDEX]]、[[governance/README]]、[[concepts/agent-instruction-sharing]]、[[governance/platform-standards]]、[[projects/decisions]]、[[harness-feedback-ledger]]、[[skills/cross-project-governance-audit/SKILL]]、[[skills/issue-analysis/SKILL]]、`scripts/check_harness_governance.py`、[[log]]。

### 接入 Claude Code 共享规则入口

- **记录人**：sunhao
- **用户意图**：用户确认当前工程是否已经能适配 Claude，并要求直接处理，让 Claude Code 与 Codex 共享本工程 agent 规则。
- **主题**：
  1. 确认当前工程已有根 [[AGENTS]] 和 `.codex/AGENTS.md`，但缺少 `CLAUDE.md`，Claude Code 还不能自动通过 `@AGENTS.md` 加载共享主规则。
  2. 按 [[concepts/agent-instruction-sharing]] 的最小稳态方案，将 `CLAUDE.md` 做成薄适配入口，只导入 [[AGENTS]]，不复制第二份规则正文。
  3. 同步根入口和治理入口中的物理结构表述，明确 `CLAUDE.md` 是 Claude Code adapter，不是新的治理单一信息源。
- **关键动作**：
  1. 新增 `CLAUDE.md`，通过 `@AGENTS.md` 导入共享主规则，并只保留 Claude Code 专用补充区。
  2. 更新 `.gitignore`，加入 `CLAUDE.local.md`，防止本机私有 Claude 记忆误提交。
  3. 更新 [[README]]、[[INDEX]]、[[governance/README]] 和 [[AGENTS]]，把 Claude 适配壳与共享规则入口的边界写清楚。
- **验证**：`python3 scripts/check_all.py --only harness-governance` 通过；`python3 scripts/check_all.py` 通过；`git diff --check` 通过。
- **二阶反思**：跨工具 agent 共享不应复制多份规则正文；正确结构是共享 `AGENTS.md` 作为规则单一信息源，工具专用入口只做 import 和薄补充。
- **影响页面**：`CLAUDE.md`、`.gitignore`、[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[log]]。

### 为迁移 meta-skill 增加产物级回归和分阶段思考循环

- **记录人**：sunhao
- **用户意图**：用户追问为什么跨工程迁移 meta-skill 升级十几次仍做不好，并指出根本可能在 meta skill 设计，以及更深层如何让 skill 在每个环节做好思考、不遗漏且翔实。
- **主题**：
  1. 确认历史失败不是单条规则缺失，而是只检查规则文本、不检查生成产物质量；此前多轮提交持续补自然语言质量门，但没有固定回归样例证明输出像任务书。
  2. 将 meta skill 的执行过程拆成执行合同判定、源能力抽取、模块展开、任务书成稿、失败模式审查和 golden regression 对照六个思考检查点。
  3. 为“生成一段提示词，把复盘体系迁移到其他工程”建立 golden taskbook 样例，并将基准校准为用户确认更好的任务书形态，而不是 agent 自己生成的压缩版。
- **关键动作**：
  1. 新增并校准 `skills/cross-project-skill-adoption-prompt/examples/retrospective-transfer-taskbook-golden.md`，保存复盘迁移任务书 golden 样例和 regression requirements。
  2. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，新增“生成思考循环”，要求每一环先做中间判断，再进入最终提示词。
  3. 更新 `skills/historical-dialogue-retrospective/TRANSFER.md` 和 [[templates/skill-transfer-manifest-template]]，加入 golden regression 样例字段。
  4. 更新 [[harness-feedback-ledger]] 和 `scripts/check_harness_governance.py`，把 golden 样例作为必需文件，并检查任务书章节、字段级模块和关键禁止项。
- **验证**：本轮收尾时运行专项和全量检查。
- **二阶反思**：skill 的翔实性不能只靠“写得更严格”的自然语言保证。高风险技能需要把思考链路拆成检查点，并保存至少一个产物级 golden 样例；sensor 要检查样例结构，而不只检查规则页关键词。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/cross-project-skill-adoption-prompt/examples/retrospective-transfer-taskbook-golden.md`、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[templates/skill-transfer-manifest-template]]、[[harness-feedback-ledger]]、`scripts/check_harness_governance.py`、[[log]]。

### 补齐复盘迁移提示词的字段级任务书要求

- **记录人**：sunhao
- **用户意图**：用户指出“生成一段提示词，把复盘体系迁移到其他工程”的输出仍像迁移说明，不像目标工程 agent 可照着执行的任务书，尤其缺少每个模块的字段级展开、明确落位和具体禁止项。
- **主题**：
  1. 确认上一版虽然列出了复盘模块，但没有强制每个模块写清目标工程应写入的字段、判断项、反模式和验证点。
  2. 将通用 meta skill 的模块展开要求抽象为“目标 / 字段或判断项 / 落位 / 禁止项 / 验证点”，适用于所有技能迁移。
  3. 将复盘体系迁移的专属字段级要求写入 `historical-dialogue-retrospective/TRANSFER.md`，覆盖方法入口、档案入口、模板、软件研发复盘、Agent 工作复盘、历史对话 skill、行动分流和治理自演进。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，要求生成稿不能只列模块标题，必须展开每个模块的字段、判断项、禁止项和验证点。
  2. 更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，新增“字段级任务书展开要求”，把测试报告不是复盘、Issue 关闭不是复盘完成、不能只凭 log 做历史复盘等禁止项固化到复盘迁移任务书质量门。
- **验证**：本轮收尾时运行专项和全量检查。
- **二阶反思**：任务书质量不只取决于模块是否完整，还取决于目标 agent 是否知道每个模块里具体要写什么、不能用什么替代、如何验证。以后跨工程迁移提示词必须同时守住模块完整和字段级可执行性。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[log]]。

### 修正迁移 meta-skill 的全主题适用边界

- **记录人**：sunhao
- **用户意图**：用户纠正跨工程技能迁移 meta-skill 不是只针对某一个主题，而是要服务所有已沉淀 skill / 能力主题，不能被复盘样例绑定。
- **主题**：
  1. 明确复盘只是首个高价值样板，不是 meta-skill 的通用字段来源；Issue 分析、验收、代码基线审计等技能迁移应使用各自 `TRANSFER.md` 的主题模块。
  2. 将 Baseline 对比评分改成“任意技能主题通用字段 + 当前源 skill / `TRANSFER.md` 的主题专属模块”，避免把复盘档案入口、复盘维度等字段套到所有技能上。
  3. 将生成质量门拆成“通用任务书完整性 + 主题覆盖完整性”两层：高抽象只定义迁移不变量，具体待迁移内容必须由源 skill / `TRANSFER.md` 提供。
  4. 为以后新增技能迁移 manifest 补出“源能力覆盖矩阵”和“主题专属任务书基线”，让每个技能自己声明可执行任务书主干、模块清单、条件适用项和最终交付要求。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，加入“迁移任务书生成器”的抽象层级说明，并泛化 baseline rubric、有效增益、两层质量门和模式污染防线。
  2. 更新 [[templates/skill-transfer-manifest-template]]，新增源能力覆盖矩阵、主题专属模块清单、条件适用 / 不适用模块和最终交付要求，承接开头命令、目标定义、结构自检重点、主题模块和最终交付。
  3. 更新 [[harness-feedback-ledger]] 和 `scripts/check_harness_governance.py`，把“复盘样例绑定 meta-skill”记录为 episode，并用 sensor 检查全主题适用和主题专属模块。
- **验证**：`python3 scripts/check_all.py --only harness-governance` 通过；完整 `python3 scripts/check_all.py` 通过。
- **二阶反思**：样板可以帮助校准任务书质量，但不能上升为所有主题的字段模型。以后 meta-skill 从某个强样例吸收优点时，必须先抽象通用任务书结构，再把主题字段留在对应 `TRANSFER.md`。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、[[templates/skill-transfer-manifest-template]]、[[harness-feedback-ledger]]、`scripts/check_harness_governance.py`、[[log]]。

### 固化迁移提示词任务书基线的收尾细节

- **记录人**：sunhao
- **用户意图**：用户提供多段对比结论，要求升级跨工程技能迁移 meta-skill，吸收更强任务书样稿的优点，让通用提示词生成技能更可执行、更稳。
- **主题**：
  1. 确认复合能力迁移提示词应继续以完整任务书为主干，meta-skill 只做补丁式增强，不重新压缩成迁移说明。
  2. 补齐两个容易漏掉的收尾细节：参考提交 / 版本锚点必须先确认再写成事实，样稿末尾重复命令应删除或移到开头，避免目标 agent 误读。
  3. 强化最终回复要求：目标工程 agent 不只汇报改了哪些文件和 commit hash，还要说明未验证边界和后续建议。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，在 Golden Baseline、Baseline 对比评分和输出前自检中加入重复命令清理、版本锚点确认和未验证边界要求。
  2. 更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，把这些收尾细节写入复盘体系迁移默认任务书骨架和最终回复要求。
- **验证**：`python3 scripts/check_all.py --only harness-governance` 通过；`git diff --check` 通过。
- **二阶反思**：这轮不是新增一个复盘模块，而是把用户已确认的强样稿差异变成生成质量门。以后 meta-skill 处理 golden baseline 时，应该优先保留任务书执行粒度，再做锚点、边界和最终交付的窄补强。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[log]]。

### 建立新增知识的网状关联自检机制

- **记录人**：sunhao
- **用户意图**：用户追问新增知识与既有知识库的关联是否自动生成，并要求设计和落实一个机制，分析历史知识库、做测试；随后追问这个能力是否已经落实为别人可学习使用的技能，以及是否按调研、沉淀知识、总结方案的链路完成。
- **主题**：
  1. 明确当前状态：Obsidian 可以自动展示 `[[wikilink]]` 图谱，但语义关联选择不是自动生成；此前主要靠 agent 手动判断入口、上位概念和回链。
  2. 设计最小可执行机制：新增知识仍由 agent 做语义判断，但必须通过 sensor 检查结构性信号，包括页面出链、非 `[[log]]` 入链、入口 / 上位知识页回链。
  3. 用历史 `concepts/` 和 `articles/` 页面校准阈值，确认现有知识库已有入口和非 log 入链网络，再用临时孤岛页做负向测试，证明 sensor 能抓出新增孤岛。
  4. 补齐调研和技能层：用 Obsidian、Evergreen notes、Zettelkasten 等外部资料校准“自动展示图谱”和“自动生成语义关联”的边界，并把流程写成可复用技能。
- **关键动作**：
  1. 新增 [[knowledge-linking-rules]]，定义新增知识关联自检、概念页 / 摘要卡片最小通过标准、自动检查边界和禁止项。
  2. 新增 `scripts/check_knowledge_linking.py` 并接入 `scripts/check_all.py --only knowledge-linking`，把知识关联检查变成可运行 sensor。
  3. 新增 [[skills/knowledge-linking/SKILL]]，把调研、沉淀知识、总结方案、关系画像、入口回链和验证命令写成别人可学习使用的 agent 技能。
  4. 新增 [[articles/2026-06-04-knowledge-linking-mechanism-research]]，沉淀外部调研来源、关键结论、历史知识库分析、机制方案和边界。
  5. 更新 [[WORKFLOW]]、[[POLICY]]、[[governance/README]]、[[INDEX]]、[[README]]、[[concepts/README]]、[[articles/README]]、[[skills/README]] 和概念 / 文章模板，让规则、入口、技能、模板和检查命令形成闭环。
  6. 更新 [[harness-feedback-ledger]]，把“新增知识关联依赖人工补链”记录为已晋升 episode，并把知识关联检查加入 active sensor backlog。
- **验证**：`python3 scripts/check_all.py --only knowledge-linking` 通过；临时创建 `concepts/__tmp_orphan_check.md` 时检查会失败并指出缺出链、缺非 log 入链、缺入口 / 知识页回链，删除测试文件后再次通过。
- **二阶反思**：这轮暴露的是“图谱可视化自动”和“知识关联生成自动”之间的边界。未来新增知识不能只靠 agent 口头说已关联，也不能只靠 `[[log]]` 被发现；必须有可检查的入口、上位概念和邻接回链。
- **影响页面**：[[knowledge-linking-rules]]、[[skills/knowledge-linking/SKILL]]、[[articles/2026-06-04-knowledge-linking-mechanism-research]]、[[WORKFLOW]]、[[POLICY]]、[[governance/README]]、[[INDEX]]、[[README]]、[[concepts/README]]、[[articles/README]]、[[skills/README]]、[[templates/concept-template]]、[[templates/article-template]]、[[harness-feedback-ledger]]、`scripts/check_knowledge_linking.py`、`scripts/check_all.py`、[[log]]。

### 收敛迁移 meta-skill 为单一通用提示词生成器

- **记录人**：sunhao
- **用户意图**：用户指出不需要“通用提示词、定制提示词、直接执行迁移、元技能维护”等多模式分类，只要 meta-skill 生成一个通用提示词。
- **主题**：
  1. 明确前次修复过度模式化：为了避免误路由，反而把跨工程迁移 meta-skill 做成了多模式路由器，偏离了用户想要的单一产物。
  2. 将 meta-skill 职责收敛为只生成通用迁移提示词：不预读目标工程、不输出具体工程小节、不做定制落位、不执行迁移。
  3. 保留 baseline 对比、Golden Baseline、任务书粒度和结构自检规则，但把它们全部服务于唯一通用提示词产物。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，删除定制、直接执行和元技能维护模式表述，改为“只有一个产物：通用迁移提示词”。
  2. 更新 [[harness-feedback-ledger]]，新增“跨工程迁移 meta-skill 过度模式化” episode，并把 active sensor 从四选一模式检查改成唯一通用产物检查。
  3. 更新 `scripts/check_harness_governance.py`，检查 `通用迁移提示词` 和 `只有一个产物`，不再要求四选一和元技能维护模式。
- **二阶反思**：修路由问题不一定要增加路由分支；当用户要的是一个稳定产物时，最好的治理是减少模式数量，让所有防线服务同一个输出。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、[[harness-feedback-ledger]]、`scripts/check_harness_governance.py`、[[log]]。

### 修正 meta-skill 维护请求的路由失守

- **记录人**：sunhao
- **用户意图**：用户纠正前一轮不是要单次生成通用提示词，而是要重启 goal 并修改 meta-skill，处理现有 meta-skill 导致生成提示词不合理的问题。
- **主题**：
  1. 明确这轮缺口不是“生成稿是否足够通用”，而是任务模式路由错误：当用户要求升级 meta-skill 本身时，agent 必须进入元技能维护模式，不能用候选提示词替代技能文件修改。
  2. 将跨工程迁移 meta-skill 的模式裁决从通用 / 定制 / 直接执行扩展为通用提示词、定制提示词、直接执行迁移、元技能维护四选一，并要求最新用户指令优先。
  3. 把“不是单次生成 / 重启 goal / 修改 meta skill / 修生成机制”写成显式触发信号，要求同步技能、sensor、ledger、log 和 commit。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，新增元技能维护模式、四选一任务裁决、维护请求优先路由和禁止用单次提示词替代维护闭环。
  2. 更新 [[harness-feedback-ledger]]，新增 “Meta-skill 维护请求被降级成单次生成” episode，并把通用模式 sensor 从三选一校准为四选一。
  3. 更新 `scripts/check_harness_governance.py`，将元技能维护模式、四选一和禁止单次提示词替代纳入 harness-governance 检查。
- **二阶反思**：候选提示词可以用作验证样本，但不能成为 meta-skill 维护请求的主交付。以后用户说“修技能 / 修生成机制 / 重启 goal”时，先改机制，再用样本验证机制是否有效。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、[[harness-feedback-ledger]]、`scripts/check_harness_governance.py`、[[log]]。

### 建立迁移提示词的示例基准比较门

- **记录人**：sunhao
- **用户意图**：用户要求设置目标并升级跨工程迁移 meta-skill，直到它针对“生成一段提示词，把复盘体系迁移到其他工程”产出的通用提示词，比用户提供的强示例更优秀。
- **主题**：
  1. 明确这轮缺口不是继续补某个章节，而是 meta-skill 缺少“用户示例 -> baseline rubric -> generated >= baseline”的比较门，导致生成稿可能在有强示例时仍然重写、压缩或混入旧上下文。
  2. 将复盘迁移提示词的质量标准改成：先完整覆盖示例的目标、资料、边界、结构自检、八类模块、入口同步和最终交付，再通过 `TRANSFER.md`、通用模式、同名目录防误用、未验证边界和检查替代方案实现增益。
  3. 明确“通用版”不是短版，也不是不适配目标结构；它应保留完整任务书粒度，只把具体工程定制改成结构自检条件。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，新增 Baseline 对比评分、`generated >= baseline` 输出前裁决、通用模式锁定、Golden Baseline 补丁原则和模式污染防线。
  2. 更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，新增通用版生成规则和“优于示例的判定标准”。
  3. 更新 [[harness-feedback-ledger]] 和 `scripts/check_harness_governance.py`，把示例基准比较做成 active sensor 检查项。
- **二阶反思**：当用户已经给出强示例时，meta-skill 的任务不是“重新创作一份看起来更规整的提示词”，而是先证明没有损失示例的执行力，再做明确增益。之后同类 meta-skill 都应优先引入 baseline 比较，而不是反复追加自然语言提醒。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[harness-feedback-ledger]]、`scripts/check_harness_governance.py`、[[log]]。

### 收紧复盘迁移提示词的任务书粒度和目录误用防线

- **记录人**：sunhao
- **用户意图**：用户对比 agent 生成的复盘体系迁移提示词和一份更完整的手写任务书，要求判断哪个更好，并把本工程复盘体系继续升级到能生成更可执行的迁移提示词。
- **主题**：
  1. 确认手写任务书整体更好，因为它保留了目标、资料、边界、落位、模块、入口和最终交付的完整执行顺序；原生成稿的优势只在于对 `prefect` 和 `customeranalysis` 的目标工程差异化落位更具体。
  2. 将生成规则收紧为“完整任务书主干 + 目标工程差异化补强”，避免多工程定制时把通用复盘体系模块压缩成短清单。
  3. 补上同名目录职责冲突防线，要求识别业务 `templates/`、handoff、log、issue、incident 等相近目录，不能只按目录名机械落位。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，要求复合能力迁移保留完整编号任务书，并在对照样稿质量门中保留同等执行粒度。
  2. 更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，补充同名目录职责冲突处理和多目标工程提示词的“通用任务书先行、差异化说明后置”规则。
- **二阶反思**：这轮不是新增复盘体系模块，而是修正复盘体系外迁时的生成质量门。未来判断迁移提示词优劣时，要同时看执行粒度和目标工程适配；两者不能互相替代。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[log]]。

### 沉淀 Claude Code 与 Codex 共享 agent 规则的方法

- **记录人**：sunhao
- **用户意图**：用户提供一套“让 Claude 和 Codex 共享同一份 agent 信息”的实践方案，要求沉淀成知识库内容，避免以后在多个工具入口之间复制规则并产生漂移。
- **主题**：
  1. 将该内容定位为跨项目可复用的 Agent 指令共享方法，而不是当前本库的新硬约束或项目运行状态。
  2. 确认最小稳态方案：`AGENTS.md` 作为共享主规则，Codex 直接读取，Claude Code 通过 `CLAUDE.md` 的 `@AGENTS.md` 导入并追加 Claude 专用规则。
  3. 区分共享“项目规则”和共享“自定义子 agent”：前者适合单一主文件，后者因 Claude / Codex 格式不同，应共享核心 prompt 文案，再生成各自包装文件。
- **关键动作**：
  1. 新增 [[concepts/agent-instruction-sharing]]，沉淀目录结构、最小实现、全局共享、子 agent 边界、判断规则、常见误区和验证方式。
  2. 更新 [[concepts/README]]、[[concepts/agent-governance]]、[[concepts/harness-engineering]] 和 [[INDEX]]，把该方法挂到 Agent 治理、Harness 组件和方法入口下。
- **二阶反思**：这轮是可复用知识沉淀，不是规则升级。正确做法是把“多工具共享同一份项目规则”的方法放进概念层，供未来项目采用；不要把当前库 `AGENTS.md` 继续扩成工具配置百科。
- **影响页面**：[[concepts/agent-instruction-sharing]]、[[concepts/README]]、[[concepts/agent-governance]]、[[concepts/harness-engineering]]、[[INDEX]]、[[log]]。

## 2026-06-03

### 修正跨工程迁移提示词的任务书形态缺口

- **记录人**：sunhao
- **用户意图**：用户追问跨工程迁移 meta-skill 已经升级过一次，为什么生成的复盘体系迁移提示词仍弱于手写任务书，并要求判断是否还有办法解决。
- **主题**：
  1. 明确上次升级解决的是“源能力覆盖度不足”，这次暴露的是“最终提示词形态不足”：生成稿虽然有路径、边界、覆盖矩阵和差异化落位，但没有强制保留目标工程 agent 可逐项执行的任务书主干。
  2. 将跨工程迁移提示词的质量门从“模块覆盖完整”继续升级为“任务书优先”：先让目标 agent 知道要做什么、按什么资料读、在哪些模块落地、如何验证提交，再把迁移边界和目标差异化作为防护层补进去。
  3. 把复盘体系迁移的手写强结构沉淀为 `TRANSFER.md` 的推荐提示词骨架，避免下一次只靠临场比较发现同类缺口。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，新增可执行任务书要求、任务书优先顺序、对照样稿质量门和输出前自检。
  2. 更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，新增复盘体系迁移的推荐提示词骨架，覆盖参考资料、吸收边界、目标结构自检、模块落地、入口同步和最终交付。
  3. 更新 [[harness-feedback-ledger]] 和 `scripts/check_harness_governance.py`，把“任务书形态缺口”作为独立 episode 和 active sensor 检查项。
- **二阶反思**：覆盖矩阵只能证明“没少模块”，不能证明“目标 agent 拿到就能执行”。以后跨工程迁移类 meta-skill 必须同时守住两层质量：源能力覆盖完整，以及最终提示词像任务书而不是迁移说明书。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[harness-feedback-ledger]]、`scripts/check_harness_governance.py`、[[log]]。

### 修正跨工程迁移提示词覆盖度不足

- **记录人**：sunhao
- **用户意图**：用户对比 agent 生成的复盘体系迁移提示词和手写版提示词，指出手写版更完整，追问是否说明跨工程迁移技能提示词设计不够完善，以及能否解决。
- **主题**：
  1. 确认问题不只是单次生成表达偏短，而是 meta-skill 缺少“源能力覆盖矩阵”和“目标工程差异化说明”的强制质量门。
  2. 将复合能力迁移提示词的最低要求从“列路径、边界和落位”升级为“保留方法、档案、模板、skill、行动分流、治理自演进、验证和入口同步的完整模块拆解”。
  3. 把复盘体系迁移里更完整的手写结构吸收到 `TRANSFER.md`，避免后续再依赖临场对比才能发现缺口。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，补充源能力覆盖矩阵、复合能力压缩防线、定制提示词目标工程差异化说明和输出前自检。
  2. 更新 `skills/historical-dialogue-retrospective/TRANSFER.md`，新增复盘体系迁移的最小模块清单，覆盖方法入口、档案入口、模板、软件研发复盘、Agent 工作复盘、历史对话 skill、行动分流、治理自演进和入口同步。
  3. 更新 [[harness-feedback-ledger]]，把这次“迁移提示词覆盖度不足”记录为已晋升的 Harness episode，并留下后续 sensor 候选。
- **二阶反思**：这轮暴露的是 meta-skill 生成质量门缺口。之后生成跨工程迁移提示词时，不能只证明“有路径、有边界、有落位”，还要证明源能力的关键模块没有被摘要压掉；定制提示词若已读取目标工程结构，也必须给出目标工程差异化落位建议。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[harness-feedback-ledger]]、[[log]]。

### 校准跨工程技能提示词的目标结构读取边界

- **记录人**：sunhao
- **用户意图**：用户指出“判断目标工程结构”这个环节不应让提示词生成端变重；目标工程 agent 拿到提示词后本来会自己读取和判断结构，要求校准跨工程技能升级提示词生成能力。
- **主题**：
  1. 明确通用提示词生成时不需要预读目标工程结构，只需要在提示词中要求目标工程 agent 先做结构自检。
  2. 将目标工程结构处理分成三种模式：通用提示词、定制提示词、直接执行迁移。
  3. 保留“目标工程必须自适配落位”的要求，防止目标工程无脑照搬 AcknowledgeBase 目录。
- **关键动作**：
  1. 更新 [[skills/cross-project-skill-adoption-prompt/SKILL]]，把“目标工程信息”改成模式分级，并补充通用提示词不预读目标工程的禁止项。
  2. 更新 `skills/historical-dialogue-retrospective/TRANSFER.md` 和 [[templates/skill-transfer-manifest-template]]，把“目标工程落位建议”改为“目标工程结构自检与落位建议”。
- **二阶反思**：这轮校准说明 meta-skill 不能因为追求准确而默认变重。通用提示词负责把结构自检责任交给目标工程 agent；只有定制或直接执行时，当前 agent 才读取目标工程结构。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[templates/skill-transfer-manifest-template]]、[[log]]。

### 建立跨工程技能升级提示词生成能力

- **记录人**：sunhao
- **用户意图**：用户指出刚才为复盘生成目标工程升级提示词的方式，以后会扩展到其他技能；要求判断是沉淀每个技能的提示词，还是形成一个特定技能，之后按需生成合格提示词，并落实这个能力。
- **主题**：
  1. 明确长期主资产不应是每个技能的一份固定完整提示词，而应是一个 meta-skill 加每个具体技能的迁移资料清单。
  2. 将“跨工程技能升级”建模为：源技能本体、`TRANSFER.md` 迁移清单、相关 concept / template / governance / sensor 资料、目标工程自适配提示词。
  3. 以复盘体系作为首个样板，为历史对话复盘技能补充迁移资料清单，后续 Issue、验收、代码基线审计等能力可按同一模式扩展。
- **关键动作**：
  1. 新增 [[skills/cross-project-skill-adoption-prompt/SKILL]]，定义生成跨工程技能升级提示词的触发场景、读取顺序、输出结构、自检和禁止项。
  2. 新增 [[templates/skill-transfer-manifest-template]]，作为具体技能维护迁移资料清单的模板。
  3. 新增 `skills/historical-dialogue-retrospective/TRANSFER.md`，把完整复盘体系迁移需要的资料路径、吸收边界、目标工程落位、行动分流和验证要求结构化。
  4. 更新 [[skills/README]]、[[templates/README]]、[[README]]、[[INDEX]]、[[AGENTS]] 和 [[WORKFLOW]]，让 meta-skill 和 transfer manifest 模式进入入口、技能维护原则和目录归类规则。
- **二阶反思**：这轮暴露的是“能力外迁”本身也是一种高频能力。以后不应把每次给目标工程的提示词当长期资产，而应让提示词按需生成；长期维护的是技能本体、迁移清单和生成器。
- **影响页面**：[[skills/cross-project-skill-adoption-prompt/SKILL]]、`skills/historical-dialogue-retrospective/TRANSFER.md`、[[templates/skill-transfer-manifest-template]]、[[skills/README]]、[[templates/README]]、[[README]]、[[INDEX]]、[[AGENTS]]、[[WORKFLOW]]、[[log]]。

### 升级复盘体系为可持续运行系统

- **记录人**：sunhao
- **用户意图**：用户要求不要只新增复盘目录或模板，而是把本工程自身复盘体系升级为能长期运行的系统，覆盖项目、阶段、事故、Issue、交付链偏差、Agent 协作偏差和治理缺口，并接入模板、skill、行动分流、Harness 自演进和检查。
- **主题**：
  1. 明确本工程已有 `projects/` 结构，复盘档案继续落在 [[projects/retrospectives/README]]，方法论保留在 [[concepts/project-retrospective]] 及子专题，模板在 [[templates/project-retrospective-template]]，执行 skill 在 [[skills/historical-dialogue-retrospective/SKILL]]。
  2. 把复盘体系补成方法入口、档案入口、执行骨架、行动分流和治理自演进四层闭环，避免只有概念或模板、没有可持续 owner 和检查。
  3. 补齐软件研发交付链和 Agent 工作复盘维度，明确测试报告、Issue 关闭、事故主档案、log、decision、memory、trace 和复盘之间的边界。
- **关键动作**：
  1. 更新 [[projects/retrospectives/README]]，新增系统运行闭环、行动分流和治理自演进关系。
  2. 更新 [[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]，补齐复盘系统组成、页面分工、交付链检查点和 Agent 工作边界。
  3. 更新 [[templates/project-retrospective-template]] 和 [[skills/historical-dialogue-retrospective/SKILL]]，补证据地图、交付链、Agent 工作回看、治理自演进判断和质量自检。
  4. 更新 [[AGENTS]]、[[WORKFLOW]]、[[README]]、[[INDEX]]、[[skills/README]]、[[templates/README]] 和 `scripts/check_harness_governance.py`，让复盘系统从入口和 sensor 都能被发现。
- **二阶反思**：这轮暴露的是“复盘能力”需要工程化闭环，而不是再加自然语言说明。以后新增长期学习类能力时，应同步定义方法、档案、模板 / skill、行动 owner、自演进路由和最小检查，防止能力停留在文档愿望。
- **影响页面**：[[projects/retrospectives/README]]、[[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]、[[templates/project-retrospective-template]]、[[skills/historical-dialogue-retrospective/SKILL]]、[[AGENTS]]、[[WORKFLOW]]、[[README]]、[[INDEX]]、[[skills/README]]、[[templates/README]]、`scripts/check_harness_governance.py`、[[log]]。

### 明确复盘档案作为长期学习工程的落位

- **记录人**：sunhao
- **用户意图**：用户指出复盘是长期工程，不只是总结文件；它应总结问题、沉淀经验，并实质帮助未来项目研发实践、方案设计和工程本身，要求检查现有复盘方案是否明确了复盘文件放在哪里，并完善知识库设计。
- **主题**：
  1. 明确用户判断成立：现有复盘专题已经有方法、触发和行动分流，但缺少“具体复盘档案”的主入口和目录落位。
  2. 将具体复盘文件落到 `projects/retrospectives/` 运行层，保持 `concepts/` 只承接方法论、`templates/` 只承接可复制页面骨架、`log` 只承接主题化历史。
  3. 明确复盘行动项不形成新平行看板，仍回到 Issue / 事故、事项链、会议 / 决策、项目记忆、trace、模板、skill 或治理页。
- **关键动作**：
  1. 新增 [[projects/retrospectives/README]]，定义复盘档案入口、文件命名、粒度、最小字段、当前索引和沉淀路由。
  2. 新增 [[templates/project-retrospective-template]]，提供具体复盘档案的最小骨架。
  3. 更新 [[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]、[[projects/STRUCTURE]]、[[projects/README]]、[[projects/status]]、[[README]]、[[INDEX]]、[[templates/README]]、[[concepts/README]]、[[AGENTS]] 和 [[WORKFLOW]]，补齐复盘文件落位、上下文模型和入口链接。
- **二阶反思**：这轮暴露的是复盘体系的承载层缺口，而不是复盘触发条件缺口。以后设计“长期学习工程”类能力时，应同时定义方法页、实例档案入口、行动分流和模板骨架，避免只有概念没有可持续存放位置。
- **影响页面**：[[projects/retrospectives/README]]、[[templates/project-retrospective-template]]、[[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]、[[projects/STRUCTURE]]、[[projects/README]]、[[projects/status]]、[[README]]、[[INDEX]]、[[templates/README]]、[[concepts/README]]、[[AGENTS]]、[[WORKFLOW]]、[[log]]。

## 2026-06-02

### 沉淀 Issue 截图原始证据入库缺口分析

- **记录人**：sunhao
- **用户意图**：用户指出上传截图和问题描述后，issue 没有沉淀原始图片证据，要求分析为什么总出现此类问题，并把调研结果和完善高效方案沉淀为知识库内容。
- **主题**：
  1. 明确这不是“旧 skill 没有规则”，一级根因是场景分流错误：`用户上传图 + 创建 issue` 没有被识别为独立场景，导致旧规则没有进入 issue 创建阶段的第一执行槽位。
  2. 结合 OpenAI 图片 / 文件输入文档和 Codex skill / AGENTS.md 官方手册，确认“模型能理解图片”与“仓库已保存原图”之间必须有显式归档桥接。
  3. 提出 issue 创建的最小执行合同：先保存用户截图到 `assets/issues/<issue-id>/`，再在 issue 文档中用标准 Markdown 图片语法引用；截图、入口和期望行为已足够时不需要浏览器复现。
- **关键动作**：
  1. 新增并修正 [[articles/2026-06-02-issue-original-evidence-asset-intake]]，沉淀旧 issue skill / AGENTS / issue README 已有截图保存规则却未在 issue 创建阶段生效的失效链。
  2. 更新 [[articles/README]] 和 [[concepts/agent-governance]]，把该案例作为 Agent / Harness 证据保真案例入口。
- **二阶反思**：这轮暴露的是场景分流能力不足，而不只是“快路径优化”和“证据资产化”之间的设计断层。后续处理用户截图类 issue 时，必须先识别 `用户上传图 + 创建 issue` 组合场景，再执行截图保存和 Markdown embed；不能只问是否需要复现，也不能用图片摘要替代原图。
- **影响页面**：[[articles/2026-06-02-issue-original-evidence-asset-intake]]、[[articles/README]]、[[concepts/agent-governance]]、[[log]]。

## 2026-05-31

### 收口项目复盘触发、粒度和行动跟踪口径

- **记录人**：sunhao
- **用户意图**：用户追问项目复盘后续会形成 skill 时，概念页里的复盘触发是否仍有必要，并要求把这轮判断沉淀到对应知识库。
- **主题**：
  1. 明确概念页只保留“是否启动复盘、启动到哪里”的粗路由，不承接完整执行流程，避免和未来 skill 维护两份触发逻辑。
  2. 把项目复盘分成轻量 checkpoint、标准复盘和深度复盘，防止小事过度治理、大事复盘过浅。
  3. 明确复盘改进行动必须落到 Issue、事故、事项、会议 / 决策、项目记忆、模板 / 规则 / skill 或 Harness ledger 等可跟踪单一信息源。
  4. 补齐软件研发复盘里的协作治理主线，把信息流、事项关系、证据边界和沉淀路由纳入复盘检查。
- **关键动作**：
  1. 更新 [[concepts/project-retrospective]]，新增启动判断与路由、复盘粒度、改进行动跟踪三节。
  2. 更新 [[concepts/software-development-project-retrospective]]，新增协作治理回看，并把推荐输出结构补上协作治理项。
  3. 更新 [[concepts/agent-work-retrospective]]，把适用触发收口为启动判断与技能边界，明确详细流程由历史对话复盘 skill 承接。
- **二阶反思**：这轮暴露的是概念页和 skill 的职责边界问题。概念页应该给入口判断、语义边界和沉淀路由；skill 才负责具体执行步骤、证据读取和输出模板。后续新增方法类页面时，也应先区分“概念边界”和“可执行技能”，避免同一判断逻辑在两层漂移。
- **影响页面**：[[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/agent-work-retrospective]]、[[log]]。

## 2026-05-30

### 修正 Agent 治理设计里的过度缩减风险

- **记录人**：sunhao
- **用户意图**：用户明确要求直接审查并整改知识库中关于 Agent / Harness 治理设计方案的材料，尤其纠正“信息过度缩减”风险，并强调 Gate / FP / EP / TASK / risk / issue / AP / report 体系绝对不能被简化。
- **主题**：
  1. 修正 DocCustomer 治理反思中的过度缩减建议：不再写固定压缩 AGENTS 行数、默认只走快速诊断、工作项简化为三层、`log` 只留三条硬约束等容易误删能力的口径。
  2. 明确研发事项体系不可简化：Gate / FP / EP / TASK / risk / issue / AP / report 是不同语义节点，只能补权限矩阵、状态传播矩阵和证据不上推边界。
  3. 把“减负”限定为减少入口噪音、重复规则和无条件仪式，不压缩分层验收、写入边界、原始事实保真和人工确认边界。
- **关键动作**：
  1. **修正案例文章**：更新 [[articles/2026-05-30-agent-governance-reflection-doccustomer]]，把“精简层次”改成“明确状态传播边界”，新增“防止信息过度缩减”小节。
  2. **同步治理专题**：更新 [[concepts/agent-governance]]，把“降低读取成本误写成删除信息结构”列为反模式。
  3. **同步 Harness 降级边界**：更新 [[harness-evolution]]，明确降级 / 删除只针对噪音和重复说明，不用于删除 P0 防线或压缩核心事项体系。
- **二阶反思**：这轮暴露的是“反臃肿”本身也会走偏：如果只盯着字数和层级数量，容易把真正需要保留的信息结构删掉。后续治理瘦身必须先区分入口噪音、流程仪式和核心语义节点，不能用压缩指标替代职责边界设计。
- **影响页面**：[[articles/2026-05-30-agent-governance-reflection-doccustomer]]、[[concepts/agent-governance]]、[[harness-evolution]]、[[log]]。

### 收窄 Agent 治理硬性条目

- **记录人**：sunhao
- **用户意图**：用户追问当前 agent 治理方案是否合理，特别是入口缩减是否会导致能力下降、`log` 硬性条目是否不合理，并要求检查其他设计里的同类问题，完成治理策略整改。
- **主题**：
  1. 横向识别类似过硬点：`[[log]]`、响应模式、引导式设计产物化、二阶反思、完整检查、模板反哺、Goal Contract、入口同步和事项链路都存在被写成无条件仪式的风险。
  2. 明确整改策略：入口缩减不等于能力下降，能力应下沉到 owning page、技能、模板和 sensor；根入口只保留 P0 防线、路由和短触发。
  3. 把 `[[log]]` 从“文件变更必写”改成 log eligibility：必须判断是否影响未来理解，再决定必写、合并写或免写。
- **关键动作**：
  1. **新增策略入口**：新增 [[agent-governance-strategy]]，定义 P0 硬约束、P1 语义门、P2 流程和 P3 backlog，并列出 Log / Artifactization / Check / Rule Upgrade 四个关键语义门。
  2. **收窄执行规则**：更新 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[instruction-adherence]]、[[log-writing-rules]] 和 `.codex/AGENTS.md`，把 `[[log]]`、产物化、完整检查和二阶反思改成资格判断，不再作为每轮硬性仪式。
  3. **接入治理入口和 sensor**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[concepts/agent-governance]]、[[harness-feedback-ledger]] 和 `scripts/check_harness_governance.py`，让策略页成为可检查的治理接线。
- **二阶反思**：这轮暴露的不是单个 `log` 规则问题，而是 Harness 把防漏动作持续硬化的系统倾向。后续新增任何规则、模板字段或 sensor 时，都要先问它是 P0 guard 还是 P1/P2/P3；如果不是 P0，就必须保留免做条件和降级出口。
- **影响页面**：[[agent-governance-strategy]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[instruction-adherence]]、[[log-writing-rules]]、[[response-mode-routing]]、[[harness-feedback-ledger]]、[[concepts/agent-governance]]、[[README]]、[[INDEX]]、[[governance/README]]、`.codex/AGENTS.md`、`scripts/check_harness_governance.py`、[[log]]。

### 跨工程治理中控基础设施落地

- **记录人**：sunhao
- **用户意图**：把 AcknowledgeBase 从"能做治理"的设计态，推进到"可定期自动执行治理"的运行态；要求统一标准、逐工程推进、handoff 包模式（中控只写建议，用户手动执行）。
- **主题**：新增四个组件——平台级治理标准（L1-L4 成熟度矩阵）、工程注册表（8 工程、治理阶段、路径）、跨工程审计技能（全量/单工程两种模式）、每周一 9:00 定期调度任务。
- **关键动作**：
  - 新增 [[governance/platform-standards]]：5 维度、L1-L4 成熟度标准，基于 AcknowledgeBase 自身体系
  - 新增 `projects/governance/`：含 [[projects/governance/registry]]（工程注册表）和 README
  - 新增 [[skills/cross-project-governance-audit/SKILL]]：审计技能，输出漂移报告 + handoff 包
  - 新增定期调度任务 `cross-project-governance-audit`，每周一 9:00 自动跑全量审计
  - 更新 [[skills/README]]、[[governance/README]] 加入新文件入口
- **待补充**：注册表中 7 个工程路径标注"待补充"，需要用户补全后首次审计才能完整运行

### AcknowledgeBase 治理中控设计

- **记录人**：sunhao
- **用户意图**：用户提出以 AcknowledgeBase 为中控，定期对各工程做针对性治理，解决模板传播和跨工程治理问题。
- **主题**：设计 AcknowledgeBase 中控的四类治理动作（漂移检查、episode 对比、规则健康度、handoff 包生成）、调度频率（主控月度/子工程季度）、职责边界（只读+建议，不直接写入其他工程）、起步路径（WORKFLOW 模式 → 技能化 → 调度化）、wiki 最小改动（只需加 template-changelog.md）。
- **关键动作**：新增 [[articles/2026-05-30-acknowledgebase-governance-hub-design]]，校准前两篇文章的拓扑描述，在 [[INDEX]] 中补入口。

### Agent 体系深度分析：前沿理论与工程现实对照

- **记录人**：sunhao
- **用户意图**：用户补充工程拓扑说明（wiki 是模板、AcknowledgeBase 是知识库兼管理层、各主控-子工程归属），并要求结合 Karpathy 设计、OpenClaw memory、harness 和分流设计做前沿调研，依据调研结果深度分析现有 agent 设计问题，沉淀结果。
- **主题**：
  1. WebSearch 调研 Karpathy Software 3.0 / Agentic Engineering、多 agent 路由架构（hub-and-spoke/hierarchical）、CoALA memory 四类型、AHE 三可观测性支柱、agent 权限边界安全数据。
  2. 结合知识库已有 harness/openclaw/codex-goals 文章，做五层对照分析：Karpathy 框架、多 agent 拓扑、OpenClaw memory、AHE 成熟度、权限边界安全现实。
  3. 诊断六大根本性设计缺陷：规则当程序用、容错设计缺失、memory 未分层、orchestrator 层缺失、episode 无闭环、wiki 模板地位未落地。
  4. 提出三阶演进路径（Phase 0/1/2）。
- **关键动作**：新增 [[articles/2026-05-30-agent-system-deep-analysis]]，在 [[INDEX]] 中补入口。

### Agent 治理跨工程横向分析与方案探索

- **记录人**：sunhao
- **用户意图**：用户要求横向对比主控工程（DocCustomeranalysis、wiki、DocFilmCommunity）、子工程（fetch-adapter、customeranalysis、prefect、train_platform）和 AcknowledgeBase，综合分析共性问题并探索可行方案，结果沉淀到文档。
- **主题**：
  1. 跨 8 工程读取 AGENTS.md、harness-feedback-ledger、governance/ 核心文件和 sensor 脚本清单。
  2. 发现 8 类共性问题：独立重发明同一治理轮子、episode 永久 active、边界靠自然语言声明、分流在每工程独立实现、commit closure 高频失守、协调协议不统一、中英文双语概念漂移、治理演进机制只在主控完整。
  3. 提出四条可行方案：共享治理内核仓库（核心方向）、写入边界字段化（scope 声明前置）、AGENTS.md 三档精简（P0/P1/P2）、跨工程 Episode 注册表。
  4. 建议优先序：先做 AGENTS.md 精简和 scope 声明字段化，再建跨工程注册表，最后规划共享内核。
- **关键动作**：新增 [[articles/2026-05-30-agent-governance-cross-project-synthesis]]，在 [[INDEX]] 中补入口。

### Agent 治理整体反思（DocCustomer 案例）

- **记录人**：sunhao
- **用户意图**：用户要求以 DocCustomer 为例反思 agent 治理体系，归纳结构性问题并沉淀到文档中。
- **主题**：
  1. 规则只增不减的正反馈陷阱：Rule Prune Queue 停留在 backlog，无硬性触发机制。
  2. 角色边界模糊：agent 同时指模型、Harness 和 sensor，缺少授权层级矩阵。
  3. 响应模式分流过重：单次任务需跨 5+ 文件推导当前模式。
  4. 状态层次过多（7 层工作项），缺少写入权限矩阵，导致 agent 频繁误写。
  5. Finalizer 例外参数膨胀，说明前置流程不可靠。
  6. 子工程写入边界靠自然语言声明，应升级为系统层硬隔离。
  7. log.md 治理规则精力投入与实际价值不对等。
  8. 治理层自参照无独立人工审核卡口。
- **关键动作**：新增 [[articles/2026-05-30-agent-governance-reflection-doccustomer]]，在 [[INDEX]] 中补入口。

## 2026-05-29

### 沉淀 finalizer 写入范围失守案例

- **记录人**：sunhao
- **用户意图**：用户指出某次 agent 收尾中，明明已经要求“只提交相关内容”，agent 仍沿 ISSUE / TASK / EP / FP 归属链继续同步，要求把这类 agent 系统问题作为专题案例沉淀，分析它属于什么问题以及怎么解决。
- **主题**：
  1. 这不是业务 issue，而是 Agent / Harness 的写入范围和最终证明缺口。
  2. finalizer 只证明 working tree clean、`log.md` 纳入提交或 external residual 已明示，不等于证明本轮 diff 符合用户最新允许范围。
  3. 用户即时收窄指令应触发 Scope Lock；后续发现的级联同步候选只能列为待确认，不应继续自动追平。
- **关键动作**：
  1. **新增案例文章**：新增 [[articles/2026-05-29-finalizer-write-scope-case]]，还原 `659a27d` 之后继续提交归属同步的工作链，分析 clean proof 与 scope proof 混淆。
  2. **记录 Harness episode**：更新 [[harness-feedback-ledger]]，把该问题记为 `Finalizer 写入范围证明缺口` observed episode，并补写 Scope Proof sensor backlog 和晋升候选。
  3. **补入口回链**：更新 [[concepts/agent-governance]]、[[articles/README]] 和 [[INDEX]]，让这个案例能从 Agent 治理和文章层被找到。
- **二阶反思**：这轮暴露的是收尾证明维度不足：提交闭环不能只证明“干净”，还要在用户收窄范围后证明“没有越界”。后续如果同类问题重复出现，应优先补 finalizer scope manifest 或 `--allowed-path` 类 sensor，而不是继续增加自然语言提醒。
- **影响页面**：[[articles/2026-05-29-finalizer-write-scope-case]]、[[harness-feedback-ledger]]、[[concepts/agent-governance]]、[[articles/README]]、[[INDEX]]、[[log]]。

### 沉淀历史对话与 Agent 工作流复盘技能

- **记录人**：sunhao
- **用户意图**：在已有项目复盘、软件研发复盘和 Agent 工作复盘专题之上，进一步把历史对话复盘做成可启动技能，用来检查 agent 工作是否有偏差，并发现整个深度 agent 工作流协作的可改进点。
- **主题**：
  1. 历史对话复盘不能只看单一材料；需要同时区分 [[harness-feedback-ledger]] 的结构性 episode、[[log]] 的主题化历史、当前对话上下文、原始 session / rollout、git diff / commit、检查输出和受影响页面。
  2. 复盘目标不仅是总结历史，还要判断 agent 的目标理解、路由、读取、执行、验证、沟通、沉淀和收尾是否偏离。
  3. workflow 改进不能直接一律升级硬规则，应按单次表现、episode、模板、sensor、技能、[[WORKFLOW]]、[[AGENTS]]、[[POLICY]] 和 memory 路由分流。
- **关键动作**：
  1. **新增技能**：新增 [[skills/historical-dialogue-retrospective/SKILL]]，定义历史对话与 Agent 工作流复盘的触发场景、证据源分层、复盘框架、偏差分类、效率质量判断、改进路由和输出格式。
  2. **接入复盘专题**：更新 [[concepts/agent-work-retrospective]] 和 [[concepts/project-retrospective]]，把历史对话、当前上下文、log、Harness episode、git 和检查证据纳入 Agent 工作复盘体系。
  3. **接入 Harness 与技能入口**：更新 [[concepts/harness-engineering]]、[[concepts/agent-governance]]、[[skills/README]] 和 [[INDEX]]，让该技能能从 Harness、Agent 治理、复盘专题和技能层入口被发现。
- **二阶反思**：这轮补上的不是一张报告模板，而是一条复盘执行流程。历史对话复盘的难点在证据分层和改进路由：只看 log 会丢过程，只看当前上下文会丢历史，只看 ledger 会忽略普通执行流水。后续如果该技能使用中反复暴露字段缺口，再考虑升级模板或 sensor。
- **影响页面**：[[skills/historical-dialogue-retrospective/SKILL]]、[[skills/README]]、[[concepts/agent-work-retrospective]]、[[concepts/project-retrospective]]、[[concepts/harness-engineering]]、[[concepts/agent-governance]]、[[INDEX]]、[[log]]。

## 2026-05-28

### 开启 Agent 治理专题

- **记录人**：sunhao
- **用户意图**：开启一个专门承接 agent 治理能力演进的专题，让现有 Harness、规则、技能、模板、sensor 和复盘机制有统一议题入口。
- **主题**：
  1. Agent 治理属于知识库方法专题，不是项目开发专题，不能落到 `projects/design/topics/` 或续写项目开发 trace。
  2. Agent 治理不是再堆一层硬规则，而是把响应路由、主动对话、指令遵循、执行合同、H5 自演进和工作复盘放到同一张知识库专题地图里。
  3. 后续 agent 能力升级应先判断属于硬约束、执行路由、任务语义、能力复用还是反馈学习，再决定回写位置。
- **关键动作**：
  1. **新增知识库专题**：新增 [[concepts/agent-governance]]，定义 Agent 治理的核心问题、治理对象、分层模型、当前基线、使用口径和反模式。
  2. **撤回错误落位**：撤回 `projects/design/topics/` 和 [[projects/trace]] 中的项目开发链路改动，保留知识库层沉淀。
  3. **补入口回链**：更新 [[concepts/README]]、[[INDEX]] 和 [[governance/README]]，让概念入口、总索引和治理入口都能找到 Agent 治理专题。
  4. **记录纠偏 episode**：更新 [[harness-feedback-ledger]]，把“知识库专题误落项目开发层”的路由偏差记为 observed episode。
- **二阶反思**：这轮暴露的是专题落位路由缺口：不能只看到“专题”就进入项目设计专题；应先判断它是知识库方法、系统治理、项目运行还是研发开发。后续同类内容要先按知识库 / 项目开发分层判断，再决定是否进入 `projects/`。
- **影响页面**：[[concepts/agent-governance]]、[[concepts/README]]、[[INDEX]]、[[governance/README]]、[[harness-feedback-ledger]]、[[log]]。

### 区分知识库模板和系统治理模板

- **记录人**：sunhao
- **用户意图**：纠正“只要一说模板就沉淀到 `templates/`”的落位偏差，要求先判断这是知识库模板还是系统治理模板。
- **主题**：
  1. 知识库模板属于专题成果，承接方法框架、报告结构、分析维度或内容骨架，优先落在 owning topic、`articles/`、`concepts/` 或项目专题页。
  2. 系统治理模板属于 `templates/`，只承接跨项目、跨页面类型复用的可复制页面骨架、字段、证据边界和检查口径。
  3. “模板化”不是自动新建模板文件的理由，必须先过模板分类、单一信息源和规则体积检查。
- **关键动作**：
  1. **升级裁定页**：更新 [[template-feedback-rules]]，新增知识库模板 / 系统治理模板二分、落位规则、进入 `templates/` 的最低条件和反哺分类标签。
  2. **同步执行约束**：更新 [[AGENTS]]、`.codex/AGENTS.md`、[[POLICY]] 和 [[WORKFLOW]]，把“先分类再落位”写入 agent 执行、自动写入边界和反哺流程。
  3. **收窄模板目录职责**：更新 [[templates/README]]，明确本目录只放系统治理可复制骨架，不承接所有专题模板化成果。
  4. **补入口和 episode**：更新 [[README]]、[[INDEX]] 和 [[harness-feedback-ledger]]，让入口能指向这次二分规则，并把用户纠偏记录为 promoted episode。
- **二阶反思**：这轮暴露的是术语路由缺口：同一个“模板”词在知识沉淀和治理骨架里含义不同。后续同类纠偏应优先补分类触发和路由，而不是继续新增模板文件。
- **影响页面**：[[template-feedback-rules]]、[[AGENTS]]、`.codex/AGENTS.md`、[[POLICY]]、[[WORKFLOW]]、[[templates/README]]、[[README]]、[[INDEX]]、[[harness-feedback-ledger]]、[[log]]。

### 补充 Agent 工作复盘子专题

- **记录人**：sunhao
- **用户意图**：指出当前项目复盘还漏了“agent 在工作”这个执行主体视角，需要把 agent 的工作方式、效率、质量和改进也纳入复盘体系。
- **主题**：
  1. 当执行主体是 agent 时，复盘不能只看项目产物，还要看目标理解、阶段判断、上下文读取、工具使用、验证质量、沟通节奏和边界控制。
  2. Agent 工作复盘应和 Harness 自演进分工：单次表现先复盘，重复失守或机制缺口再进入 episode、sensor、模板、技能或规则升级。
  3. 软件研发项目复盘在 agent 参与执行时，需要显式补看 agent 工作质量，而不是把它隐含在协作治理里。
- **关键动作**：
  1. **新增子专题**：新增 [[concepts/agent-work-retrospective]]，定义 Agent 工作复盘的维度、触发场景、推荐输出、Harness 分工、沉淀路由和反模式。
  2. **同步专题关系**：更新 [[concepts/project-retrospective]] 和 [[concepts/software-development-project-retrospective]]，把 agent 作为执行主体和软件研发交付链中的复盘对象接入。
  3. **补入口链接**：更新 [[INDEX]]、[[concepts/README]] 和 [[concepts/harness-engineering]]，让 Agent 工作复盘同时能从复盘专题和 Harness Engineering 入口找到。
- **二阶反思**：这次暴露的是复盘对象建模缺口：在 agent 协作越来越常见的工作里，只复盘项目结果会漏掉执行主体本身的质量反馈。后续如果 Agent 工作复盘被反复使用，再考虑补模板或 sensor，不在本轮提前扩成硬规则。
- **影响页面**：[[concepts/agent-work-retrospective]]、[[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/harness-engineering]]、[[concepts/README]]、[[INDEX]]、[[log]]。

### 把状态与约束推演模板拆成多维报告资产

- **记录人**：sunhao
- **用户意图**：把已经形成的方法模板继续沉淀成资产库，不只保留一张总模板，而是能按不同分析维度复用出多种报告资产。
- **主题**：
  1. 模板不是一次性回答的附属物，而应作为可复用资产沉淀下来。
  2. 状态与约束推演类问题不适合永远只用一张大模板；应按总览、可执行性、依赖传播、时间资源、阻塞不确定等维度拆成资产族。
  3. 报告资产需要接回治理入口和模板入口，避免新增模板很快变成孤岛。
- **关键动作**：
  1. **主尝试**：先把状态与约束推演按总览、可执行性、依赖传播、时间资源、阻塞不确定几类维度拆成资产族，验证这种拆法是否比一张万能模板更稳。
  2. **补治理说明**：更新 [[state-constraint-reasoning]] 和 [[concepts/state-constraint-planning]]，先把“报告资产化”写成这套方法的落地方向。
  3. **补项目主链**：续写 [[projects/trace]]，把这次从“单模板”升级到“多维资产族”的变化纳入当前方法主题的迭代链。
- **二阶反思**：这轮说明真正可复用的方法论，通常不会停在一张万能模板；更稳定的做法是保留一个统一总模型，再围绕高频判断维度沉淀一组报告资产。后续若某类计划报告继续高频出现，应优先判断是否再拆成独立资产，而不是继续把总模板越写越厚。
- **影响页面**：[[templates/README]]、[[state-constraint-reasoning]]、[[concepts/state-constraint-planning]]、[[projects/trace]]、[[log]]。

### 纠正状态推演模板的归属边界并补齐三类专题样式

- **记录人**：sunhao
- **用户意图**：纠正“状态推演模板已经进入系统模板层”的归属错误，明确它们只是知识库专题成果，并确认是否已经覆盖超简版、生活版和工程版三类模板。
- **主题**：
  1. 这组模板写法当前属于专题成果，不应直接放进 `templates/` 作为系统模板。
  2. 用户点名要求覆盖三类版本：超简版、生活版、工程版。
  3. 治理页和概念页可以引用专题成果，但不应把它误写成已经晋升为正式系统模板。
- **关键动作**：
  1. **新增专题样式包**：新增 [[articles/2026-05-28-state-constraint-template-pack]]，统一收口超简版、生活版和工程版三类模板样式。
  2. **撤回系统模板归属**：删除 `templates/` 下那组状态推演报告资产文件，并更新 [[templates/README]]、[[state-constraint-reasoning]]、[[concepts/state-constraint-planning]] 和研究卡片的相关表述。
  3. **补主链纠偏**：续写 [[projects/trace]]，明确这次是“专题成果 / 系统模板”边界纠偏，而不是继续扩大系统模板层。
- **二阶反思**：这轮说明“有价值的写法”不自动等于“应进入系统模板层”。更稳的顺序应该是：先作为知识库专题成果沉淀，等跨场景复用稳定后，再决定是否晋升为正式模板。
- **影响页面**：[[articles/2026-05-28-state-constraint-template-pack]]、[[articles/2026-05-28-state-constraint-planning-research]]、[[concepts/state-constraint-planning]]、[[state-constraint-reasoning]]、[[templates/README]]、[[projects/trace]]、[[log]]。

### 把计划型问题升级为状态与约束推演方法

- **记录人**：sunhao
- **用户意图**：把“我缺的是把信息放进系统约束里推演的能力”这件事做成正式知识沉淀和专业方法，而不是停留在一次搬家反思或口头提醒。
- **主题**：
  1. 这次真正缺的不是“前置条件意识”本身，而是先做系统状态建模、约束传播、未知变量标注和可执行性判断，再更新计划的能力。
  2. 这类问题横跨搬家、旅行、办证、采购、部署、上线、签合同等计划型场景，不能只用生活经验表述，需要把自动规划、时间约束网络、约束规划、项目调度、MBSE / Statecharts 和系统思维组合起来。
  3. 如果只写研究卡片和概念页，方法仍可能停留在“知道了”；需要同步进入治理入口和 discovery 模板，改变默认执行。
- **关键动作**：
  1. **新增研究卡片**：新增 [[articles/2026-05-28-state-constraint-planning-research]]，系统整理自动规划、时间约束网络、约束规划 / 调度、项目调度、MBSE / Statecharts 和系统思维各自能解决什么，以及它们对当前问题的组合价值。
  2. **新增概念与治理入口**：新增 [[concepts/state-constraint-planning]] 和 [[state-constraint-reasoning]]，把“新信息进入 -> 状态更新 -> 约束传播 -> 可执行性判断 -> 计划更新”升级为当前库的正式方法。
  3. **同步默认执行**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[response-mode-routing]]、[[proactive-dialogue-system]] 和 [[templates/guided-discovery-session-template]]，让计划型问题默认先判状态与约束，不直接写动作安排。
  4. **补项目主链**：更新 [[projects/trace]] 和 [[projects/decisions]]，把这次方法升级纳入当前 wiki 项目的正式演进和决策链。
- **二阶反思**：这轮说明“更成熟的计划能力”不能只靠多写几个 TODO 字段，而要把意图、事实、约束、假设、阻塞和外部不确定拆开，再让约束传播进入默认执行。后续如果还出现“意图直接写成计划”的失守，应优先补检查或更强模板字段，而不是只重复提醒。
- **影响页面**：[[articles/2026-05-28-state-constraint-planning-research]]、[[concepts/state-constraint-planning]]、[[state-constraint-reasoning]]、[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[templates/guided-discovery-session-template]]、[[projects/trace]]、[[projects/decisions]]、[[log]]。

### 建立项目复盘专题和软件研发项目复盘子专题

- **记录人**：sunhao
- **用户意图**：在知识库中建立一个可长期复用的项目复盘专题，并下设软件研发项目复盘子专题，让后续项目、阶段、发布或事故结束后有统一的复盘入口和沉淀路由。
- **主题**：
  1. 项目复盘应作为概念 / 方法层专题，承接跨项目可复用框架，不替代具体项目、事故、决策或测试报告。
  2. 软件研发项目复盘需要把需求、设计、拆解、实现、测试验收、发布运行和协作治理放在一条交付链里回看。
  3. 复盘沉淀必须区分项目事实、可复用方法、模板候选、规则变化和技能候选，避免把一次性项目事实直接写成通用规则。
- **关键动作**：
  1. **新增主专题**：新增 [[concepts/project-retrospective]]，定义项目复盘的层级、对象、最小产出、页面分工和常见反模式。
  2. **新增子专题**：新增 [[concepts/software-development-project-retrospective]]，定义软件研发项目复盘的主线、推荐输出结构、证据读取顺序和沉淀路由。
  3. **补入口链接**：更新 [[INDEX]] 和 [[concepts/README]]，把复盘专题接入研发方法和概念方法入口。
- **二阶反思**：复盘类内容很容易在项目事实、事故报告和通用方法之间漂移；本轮先用主专题和子专题分层，后续只有当复盘骨架被反复使用时，再考虑新增模板或技能，不提前铺空结构。
- **影响页面**：[[concepts/project-retrospective]]、[[concepts/software-development-project-retrospective]]、[[concepts/README]]、[[INDEX]]、[[log]]。

### 调研 OpenClaw 的记忆系统并沉淀为知识卡片

- **记录人**：sunhao
- **用户意图**：调研 `OpenClaw`，重点理解它的记忆系统如何组织、检索、晋升和编译，并把高价值结论沉淀到当前文档库，而不是只在对话里口头总结。
- **主题**：
  1. OpenClaw 的 memory 核心不是单独向量库，而是以 workspace Markdown 为真相源的分层记忆体系。
  2. 它把长期记忆、每日工作记忆、active recall、dreaming consolidation 和 wiki compilation 拆成不同职责层。
  3. 当前 wiki 最值得借鉴的是 file-first truth、daily -> curated 提纯链、action-sensitive memory 和 compiled knowledge layer，而不是直接照搬具体插件。
- **关键动作**：
  1. **新增研究卡片**：新增 [[articles/2026-05-28-openclaw-memory-system-research]]，整理 `MEMORY.md`、`memory/YYYY-MM-DD.md`、`DREAMS.md`、builtin / QMD search、active memory、memory flush、dreaming 和 `memory-wiki` 的结构与判断。
  2. **新增概念入口**：新增 [[concepts/openclaw]]，作为工具级概念页，承接后续关于 OpenClaw workspace / memory / runtime 的统一跳转入口。
  3. **补导航入口**：更新 [[INDEX]] 和 [[concepts/README]]，把专题与概念接到当前知识沉淀层入口，避免新卡片成为孤岛页。
  4. **保留边界**：本轮属于知识沉淀，不直接修改 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]] 或项目运行层状态。
- **二阶反思**：这轮再次说明“记忆系统”不能只看 embedding 或向量检索；真正可长期工作的 memory 需要同时处理真相源、分层、召回、提纯、预算和可审阅中间层。后续若要吸收到当前 wiki，应优先补 action-sensitive memory 和 compiled knowledge layer 的抽象设计。
- **影响页面**：[[articles/2026-05-28-openclaw-memory-system-research]]、[[concepts/openclaw]]、[[concepts/README]]、[[INDEX]]、[[log]]。

### 校准 Harness 调研的完整性、前沿性和深入度

- **记录人**：sunhao
- **用户意图**：检查当前知识库里关于 Harness 的专题沉淀是否已经真的做到“完整、前沿、深入”，并把判断本身回写进知识库，而不是只在对话里口头回应。
- **主题**：
  1. 研究页不能因为已经存在就默认等于“调研完成”；需要显式写出当前覆盖边界、前沿缺口和截至日期。
  2. `Harness Engineering` 当前库里已经形成基础骨架，但仍缺少对 2026-05-21/2026-05-27 runtime adaptation 和 2026-05-26 governed evolution 这批新材料的系统吸收。
  3. 需要把“稳定共识 / 前沿增量 / 当前库已吸收 / 待吸收”区分开，避免旧研究页看起来像已经封口。
- **关键动作**：
  1. **升级专题卡片**：更新 [[articles/2026-05-25-harness-engineering-research]]，新增“截至 2026-05-28 的当前评估”和“2026-05-28 前沿增量”，补入 Martin Fowler、LangChain、OpenAI、Vercel、`arXiv:2605.22166`、`arXiv:2605.27328` 的增量判断。
  2. **升级概念页**：更新 [[concepts/harness-engineering]]，补写当前研究状态和未解决问题，明确当前结论是“基础完整，但还不能宣称完全前沿深入”。
  3. **保留诚实边界**：这轮没有把新研究直接伪装成已经落地的治理规则、sensor 或模板，而是先把知识层的 currentness 和 gap 写清楚。
- **二阶反思**：这轮暴露的是专题研究页常见的结构性风险：材料一旦沉淀成文章，维护者容易把“已有页面”误读成“最新且封口”。后续同类专题应显式标注评估日期、前沿增量和待吸收缺口。
- **影响页面**：[[articles/2026-05-25-harness-engineering-research]]、[[concepts/harness-engineering]]、[[log]]。

### 升级主动对话和性能预算 Harness

- **记录人**：sunhao
- **用户意图**：把当前 wiki 的智能体系统升级得更前沿、更智能，同时注意性能，避免只堆规则或照搬 `DocCustomeranalysis` 的业务事实。
- **主题**：
  1. 智能化升级应落到主动对话、场景自动判定、带假设推进和每轮产物化，而不是只增加说明文字。
  2. 性能优化应落到读取预算、问题预算、检查预算和产物大小预算，避免为了“智能”无限扩读、长问卷或铺满项目结构。
  3. 下游工程的成熟经验只抽象为模板级 Harness 能力，不复制具体业务状态、环境语义或一次性证据。
- **关键动作**：
  1. **新增治理页**：新增 [[proactive-dialogue-system]]，定义通用主动对话内核、场景化问题包、上下文自动判定、无感交流等级、性能预算和每轮产物化落地判定。
  2. **新增模板**：新增 [[templates/guided-discovery-session-template]]，承接场景包、置信度、关键假设、对话所得、agent 思考结果、性能预算、路由和提交闭环。
  3. **同步入口和路由**：更新 [[AGENTS]]、[[response-mode-routing]]、[[WORKFLOW]]、[[POLICY]]、[[governance/README]]、[[INDEX]]、`.codex/AGENTS.md` 和 [[templates/README]]，把“引导式设计”加入默认响应模式。
  4. **升级 sensor**：扩展 `scripts/check_harness_governance.py`，检查主动对话页、引导式模板、入口 wiring、性能预算和产物化字段。
  5. **记录 H5 episode**：更新 [[harness-feedback-ledger]]，把本轮作为“主动对话和性能预算升级”的 promoted episode。
- **不反哺边界**：没有复制 `DocCustomeranalysis` 的业务 issue、141 / 149 环境语义、服务实例、项目状态或具体报告；只吸收抽象后的主动对话、引导式设计、产物化闭环和性能预算。
- **二阶反思**：这轮说明“更智能”必须变成可触发、可模板化、可检查的机制；否则会退化成聊天风格偏好。后续同类升级应继续按“场景判断 -> 产物落地 -> sensor 守卫 -> 性能预算”的顺序推进。
- **影响页面**：[[proactive-dialogue-system]]、[[templates/guided-discovery-session-template]]、[[AGENTS]]、[[response-mode-routing]]、[[WORKFLOW]]、[[POLICY]]、[[governance/README]]、[[INDEX]]、[[templates/README]]、[[harness-feedback-ledger]]、[[log]]、`.codex/AGENTS.md`、`scripts/check_harness_governance.py`。

## 2026-05-26

### 吸收 DocCustomeranalysis 的测试成熟度和口径漂移治理

- **记录人**：sunhao
- **用户意图**：从 `/Users/hai/Documents/Code/DocCustomeranalysis` 最近完善的 harness 设计、测试环节规则和口径漂移治理中抽象可复用系统层信息，回写到当前 wiki 模板库，不复制下游项目事实。
- **主题**：
  1. 规则已有但执行失守时，优先升级为触发矩阵、模板字段、sensor、门禁或最终证明，而不是继续堆自然语言规则。
  2. 执行类页面必须保持当前裁决单值，防止参考规则、非目标、条件路由或上层证据漂成隐形待办。
  3. 测试、验收和上线需要分层：测试计划 / AP 先于测试报告，环境是证据面不是荣誉阶梯。
- **关键动作**：
  1. **新增治理页**：新增 [[instruction-adherence]] 和 [[execution-contract-semantics]]，分别承接规则执行覆盖和执行合同语义防漂移。
  2. **新增测试概念和计划层**：新增 [[concepts/software-testing-acceptance-release]]、[[projects/development/plan/test-acceptance-planning-model]]、[[projects/development/acceptance/README]] 和 [[projects/development/acceptance/plans/README]]。
  3. **补模板和报告字段**：新增 [[templates/development-acceptance-plan-template]]，升级 [[templates/development-test-report-template]]，让报告记录计划来源、AP、fixture / oracle 和不上推边界。
  4. **同步入口和研发链路**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[projects/STRUCTURE]]、[[projects/development/README]]、研发总控、事项模型、TASK 模型和报告入口。
  5. **新增 sensor**：新增 `scripts/check_testing_system_maturity.py` 和 `scripts/check_execution_contract_semantics.py`，并接入 `scripts/check_all.py` 和 `scripts/check_harness_governance.py`。
- **不反哺边界**：没有复制 `DocCustomeranalysis` 的业务 issue、服务器编号、项目状态、具体测试报告、服务实例、灰度 / 生产事实或一次性任务结论；只吸收抽象后的规则覆盖层、执行合同语义、测试成熟度模型、AP 计划层和可检查 sensor。
- **二阶反思**：这轮说明“测试规则更完善”不能只写进报告模板；如果没有前置 AP / 计划来源和执行合同语义检查，后续仍会把报告当计划、把高环境当阶梯、把非目标写成隐形待办。后续同类吸收应继续按“抽象候选 -> 入口/模板 -> sensor -> log/commit”的闭环执行。
- **影响页面**：[[instruction-adherence]]、[[execution-contract-semantics]]、[[concepts/software-testing-acceptance-release]]、[[projects/development/plan/test-acceptance-planning-model]]、[[projects/development/acceptance/README]]、[[projects/development/acceptance/plans/README]]、[[templates/development-acceptance-plan-template]]、[[templates/development-test-report-template]]、[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[harness-feedback-ledger]]、[[projects/STRUCTURE]]、[[projects/development/README]]、[[projects/development/plan/README]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/plan/task-design-model]]、[[projects/development/reports/README]]、[[templates/README]]、[[concepts/README]]、[[log]]、`scripts/check_all.py`、`scripts/check_harness_governance.py`、`scripts/check_testing_system_maturity.py`、`scripts/check_execution_contract_semantics.py`。

## 2026-05-25

### 继续吸收 DocCustomeranalysis 的 Goal Contract 防线设计

- **记录人**：sunhao
- **用户意图**：从 `DocCustomeranalysis` 读取新补强的 goal 设计，把其中可复用的系统层规则吸收到当前 wiki 模板库，而不是复制下游项目事实。
- **主题**：
  1. Goal Contract 的切入点应固定在响应模式判断之后、正式长时执行之前。
  2. Goal Contract 只解决防跑偏、防证据漂移和防无限探索，不替代项目状态、验收报告、规则层或 memory。
  3. `health`、日志、子工程自述、handoff 和任务中间态只能作为辅助证据，不能因为写进 Goal 就上推为真正闭环。
- **关键动作**：
  1. **升级模板正文**：重写 [[templates/goal-contract-template]]，补齐适用性判断、原始目标 / 用户最新目标、完成判定、探索分支上限、阻塞后汇报格式、证据审计和辅助证据边界。
  2. **同步路由和规则**：更新 [[response-mode-routing]]、[[WORKFLOW]] 和 [[POLICY]]，把 Goal Contract 的切入位置、三条防线和不上推边界写入当前治理链。
  3. **同步协作模板**：更新 [[templates/developer-task-brief-template]]、[[templates/code-handoff-template]]、[[templates/harness-episode-package-template]] 和 [[templates/harness-adoption-template]]，让主控下发、子工程回传和 episode 复盘都能记录完成判定与证据边界。
  4. **同步概念和入口**：更新 [[concepts/codex-goals]]、[[concepts/harness-engineering]]、[[INDEX]] 和 [[templates/README]]，避免入口仍停留在旧版“最终状态 + 验证面 + 阻塞条件”的粗口径。
  5. **升级 sensor**：更新 `scripts/check_harness_governance.py`，把 Goal Contract 新字段和关键防线纳入 Harness 检查。
- **不反哺边界**：本轮没有复制 `DocCustomeranalysis` 的业务事项、141 / 149 环境语义、具体 issue、服务实例或项目状态；只吸收抽象后的 Goal Contract 触发位置、字段结构、证据审计和 sensor 要求。
- **二阶反思**：这轮说明“吸收 goal 设计”不能只改模板正文；长时任务契约如果不进入路由、协作模板和 sensor，很快会退回成一段可选提示词。后续同类反哺应继续遵守“先分类候选、剥离项目事实、同步可检查入口”的顺序。
- **影响页面**：[[templates/goal-contract-template]]、[[response-mode-routing]]、[[WORKFLOW]]、[[POLICY]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]]、[[templates/harness-episode-package-template]]、[[templates/harness-adoption-template]]、[[concepts/codex-goals]]、[[concepts/harness-engineering]]、[[INDEX]]、[[templates/README]]、[[log]]、`scripts/check_harness_governance.py`。

### 完整吸收 Gate / FP / EP / TASK 研发事项体系

- **记录人**：sunhao
- **用户意图**：在前一轮吸收 H5 Harness 后，继续完整吸收 `DocCustomeranalysis` 中更成熟的 Gate、FP、EP、TASK、Issue、risk、test、项目验收、测试、服务台账和子工程沟通规则，并固化为当前 wiki 的默认工程设计。
- **主题**：
  1. 正式研发事项主链升级为 `Gate -> FP -> EP -> TASK`，不再只靠 FP / TODO / 报告表达执行闭环。
  2. risk、Issue、test、验收、报告和服务台账作为关系节点和关闭守卫，而不是平行堆放的清单。
  3. Issue 是案件档案，报告是每次验证记录，服务台账是运行实例事实单一信息源。
  4. 子工程只读上下文、受控回写和无写权限回传都必须按 EP / TASK / Issue / 报告 / 服务台账边界沟通。
- **关键动作**：
  1. **补事项模型**：更新 [[projects/development/plan/work-item-system-model]]，新增 [[projects/development/plan/task-design-model]]、[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]] 和 [[projects/development/issues/README]]。
  2. **补模板**：新增 [[templates/development-execution-package-template]]、[[templates/development-task-template]] 和 [[templates/development-issue-template]]，升级 [[templates/development-work-item-matrix-template]]、[[templates/development-test-report-template]] 和 [[templates/service-registry-template]]。
  3. **同步入口和治理**：更新 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[README]]、[[INDEX]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/development/README]]、[[projects/development/plan/README]]、[[projects/development/execution/README]]、Gate、FP、risk、报告和台账入口。
  4. **补子工程沟通**：升级 [[projects/development/execution/developer-execution-workflow]]、[[templates/developer-task-brief-template]] 和 [[templates/code-handoff-template]]，让任务下发、代码回传、验收评审和受控回写都使用 EP / TASK 主链。
  5. **收口维护入口**：在 [[projects/development/plan/README]] 新增维护者入口顺序，让日常研发事项维护先走总控页，只有改默认规则时才回到治理层。
  6. **统一旧口径**：清理 [[projects/development/execution/engineering-feedback-loop]]、[[response-mode-routing]]、[[POLICY]]、[[AGENTS]] 和相关模板里的旧 TODO / FP 主闭环表述，统一为 TASK / EP / FP / Gate 主链，TODO 只作轻量兼容视图。
  7. **新增 sensor**：新增并扩展 `scripts/check_work_item_matrix.py`，接入 `scripts/check_all.py`，让事项矩阵、模板、入口和子工程回传 wiring 可检查；后续又从关键词检查升级为文件、章节、表头、模板字段和入口链接检查。
- **二阶反思**：这轮说明“完整吸收”不能只靠口头记忆；高价值工程设计必须同时落到模型、模板、入口、治理规则、子工程协作契约和本地 sensor，后续才能在新任务中自然执行。对于分布式规则，必须给维护者一个日常入口顺序；对于 sensor，优先检查结构和字段，不继续堆脆弱关键词；对于升级后的术语，必须清理旧主闭环表达，只保留明确标注的轻量兼容 TODO。
- **影响页面**：[[projects/development/plan/work-item-system-model]]、[[projects/development/plan/task-design-model]]、[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/issues/README]]、[[projects/development/reports/README]]、[[projects/service-registry]]、[[templates/development-work-item-matrix-template]]、[[templates/development-execution-package-template]]、[[templates/development-task-template]]、[[templates/development-issue-template]]、[[templates/development-test-report-template]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]]、[[templates/service-registry-template]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[README]]、[[INDEX]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/trace]]、[[projects/decisions]]、[[log]]、`scripts/check_work_item_matrix.py`、`scripts/check_all.py`。

### 将 Codex Goals 转成主控和子工程协作契约

- **记录人**：sunhao
- **用户意图**：基于刚沉淀的 Codex Goals 专题，判断自有主控工程和子工程是否有升级建议，并把可执行的部分直接落实到当前模板库。
- **主题**：
  1. 长时任务升级点不是让 agent 无限后台运行，而是先写清线程级完成契约。
  2. 主控侧负责定义最终状态、验证面、约束、状态关闭条件和人工确认边界。
  3. 子工程侧负责按主控契约执行实现、本地验证、失败项、未验证边界和可吸收回传。
- **关键动作**：
  1. **新增模板**：新增 [[templates/goal-contract-template]]，把最终状态、验证面、约束、迭代策略、阻塞停止条件和主控 / 子工程分工收成可复制骨架。
  2. **升级协作模板**：更新 [[templates/harness-adoption-template]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]] 和 [[templates/harness-episode-package-template]]，加入 Goal Contract 字段和完成判断。
  3. **同步规则和入口**：更新 [[response-mode-routing]]、[[WORKFLOW]]、[[AGENTS]]、[[POLICY]]、[[README]]、[[INDEX]]、[[templates/README]] 和 [[concepts/harness-engineering]]，明确 Goal Contract 不替代验收关闭。
  4. **补 sensor 和 ledger**：更新 `scripts/check_harness_governance.py` 和 [[harness-feedback-ledger]]，让 Goal Contract 的关键入口和模板字段进入 Harness 检查。
- **二阶反思**：这轮说明 Goals 最适合先转成模板字段和 sensor，而不是直接新增一组重规则；主控和子工程之间真正需要固化的是“谁定义完成、谁生产证据、谁关闭状态”。
- **影响页面**：[[templates/goal-contract-template]]、[[templates/harness-adoption-template]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]]、[[templates/harness-episode-package-template]]、[[response-mode-routing]]、[[WORKFLOW]]、[[AGENTS]]、[[POLICY]]、[[README]]、[[INDEX]]、[[templates/README]]、[[concepts/harness-engineering]]、[[harness-feedback-ledger]]、[[log]]。

### 吸收 DocCustomeranalysis 的 H5 Harness 与本地门禁

- **记录人**：sunhao
- **用户意图**：把 `DocCustomeranalysis` 中更健全的 Harness 设计和整体系统流程抽象吸收到当前 wiki 模板库里，因为两者定位一致，但不能复制下游项目事实。
- **主题**：
  1. 当前 wiki 已有响应模式路由，但缺少 H5 自演进、episode ledger 和可执行 sensor 闭环。
  2. 可复用的是系统层能力：episode 数据、晋升 / 降级机制、统一本地门禁、工作阶段专项检查、Codex 本地入口和复盘模板。
  3. 不反哺的是下游项目业务 issue、运行环境、具体测试报告、141 / 149 边界、GitLab 平台假设和一次性状态。
- **关键动作**：
  1. **新增 H5 治理入口**：新增 [[harness-evolution]] 和 [[harness-feedback-ledger]]，让用户纠偏、检查失败、模式切换和重复失守先沉淀为 episode，再决定是否晋升规则。
  2. **新增模板和本地适配**：新增 [[templates/harness-episode-package-template]]、[[templates/harness-evolution-review-template]] 和 `.codex/AGENTS.md`。
  3. **新增统一门禁**：新增 `scripts/check_all.py` 和 `scripts/check_harness_governance.py`，先覆盖 Harness wiring、模板、入口链接和 H5 ledger。
  4. **同步入口和项目链路**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[concepts/harness-engineering]]、[[templates/README]]、[[skills/README]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/decisions]] 和 [[projects/trace]]。
- **二阶反思**：这轮说明“更健全”不是继续堆自然语言规则，而是把规则的生命线做出来：episode -> ledger -> sensor / template / skill -> 必要时再升规则；后续要优先扩展 Markdown / wikilink、frontmatter、技能质量和模板完整性 sensor。
- **影响页面**：[[harness-evolution]]、[[harness-feedback-ledger]]、[[response-mode-routing]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[README]]、[[INDEX]]、[[governance/README]]、[[concepts/harness-engineering]]、[[skills/README]]、[[templates/README]]、[[templates/harness-episode-package-template]]、[[templates/harness-evolution-review-template]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/decisions]]、[[projects/trace]]、[[log]]、`.codex/AGENTS.md`、`scripts/check_all.py`、`scripts/check_harness_governance.py`。

### 调研 Codex Goals 并沉淀为长时任务完成契约专题

- **记录人**：sunhao
- **用户意图**：围绕用户提供的本地译文材料，调研 Codex Goals 这个专题，并把它整理成可回看的知识沉淀，而不是只停留在一次对话解释。
- **主题**：
  1. Codex Goals 的本质是线程级持久目标和完成契约，不是全局 memory，也不是仓库级规则。
  2. 强 Goal 的关键在于把结果、证据、约束、边界、迭代策略和阻塞停止条件写清楚。
  3. Goals 对性能调优、flaky test 调查、复杂迁移和研究复现这类“终点明确、路径不明确”的长时任务特别有价值。
- **关键动作**：
  1. **归档来源**：把用户提供的微信 HTML 和资源目录归档到 `raw/codex-goals/`，保留本地原始材料，避免后续结论失去证据源。
  2. **新增专题卡片**：新增 [[articles/2026-05-25-codex-goals-research]]，整理 Goals 的定义、适用场景、强弱写法、生命周期控制、和 Agent Harness 的关系，以及可直接复用的 Goal 模板。
  3. **新增概念页**：新增 [[concepts/codex-goals]]，把 Codex Goals 收口为线程级完成契约的概念单一信息源。
  4. **补入口链接**：更新 [[INDEX]] 和 [[concepts/README]]，把 Codex Goals 纳入研发方法和概念入口，方便后续回链。
- **二阶反思**：这轮沉淀说明“长期委托给 Agent 的任务”不能只靠更长 prompt；后续如果要把这类能力进一步制度化，重点应放在可审计完成条件和证据检查，而不是再叠一层模糊规则。
- **影响页面**：[[articles/2026-05-25-codex-goals-research]]、[[concepts/codex-goals]]、[[INDEX]]、[[concepts/README]]、[[log]]、`raw/codex-goals/`。

### 将响应模式路由升级为 wiki Harness 默认机制

- **记录人**：sunhao
- **用户意图**：综合 Harness 设计，对当前 wiki 做一轮正式升级，让它更智能、更高效，并且至少把 agent 响应效率治理问题处理成可执行规则，而不是继续停留在候选反思。
- **主题**：
  1. 响应效率治理的关键是先判模式、先给 checkpoint，再决定是否进入沉淀、验收、规则升级或实现回传。
  2. [[AGENTS]] 继续保持短入口和硬约束，详细模式表、读取预算和切换规则由 [[response-mode-routing]] 做单一信息源。
  3. 快速诊断不能替代验收关闭，重治理闭环也不能伪装成仍在分析。
  4. 新系统接入 Agent Harness 需要模板化主控关系、单一信息源、写权限、验证层级、handoff 和 feedback sensor。
- **关键动作**：
  1. **新增治理入口**：新增 [[response-mode-routing]]，正式定义快速诊断、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传和批处理模式。
  2. **同步硬规则和流程**：更新 [[AGENTS]]、[[WORKFLOW]] 和 [[POLICY]]，让每轮先判响应模式，并明确快速诊断默认不写状态、不关闭 TODO / FP / Gate、不替代验收。
  3. **升级技能与模板**：更新 [[skills/issue-analysis/SKILL]]，增加快速根因链和完整沉淀链分支；新增 [[templates/harness-adoption-template]] 并挂入 [[templates/README]]。
  4. **同步入口和项目链路**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[concepts/harness-engineering]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/trace]] 和 [[projects/decisions]]。
  5. **更新来源分析边界**：把 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]] 从候选反思更新为来源分析和升级参考，生效入口改指 [[response-mode-routing]]。
- **二阶反思**：这轮暴露的不是缺少更多规则，而是需要把规则变成 Harness 里的路由器和反馈传感器；下一步不应继续堆入口正文，应优先补 wikilink、frontmatter、技能质量和模板完整性检查。
- **影响页面**：[[response-mode-routing]]、[[templates/harness-adoption-template]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[README]]、[[INDEX]]、[[governance/README]]、[[skills/README]]、[[skills/issue-analysis/SKILL]]、[[templates/README]]、[[concepts/harness-engineering]]、[[articles/2026-05-25-agent-response-efficiency-governance-reflection]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/trace]]、[[projects/decisions]]、[[log]]。

### 沉淀 Agent 系统升级参考方案

- **记录人**：sunhao
- **用户意图**：把关于 wiki、重治理主控工程和子工程如何升级为健全且高效的 Agent Harness 的综合判断沉淀到文档中，作为后续升级参考方案，而不是只留在对话里。
- **主题**：
  1. 后续升级关键不是继续加规则，而是建立可路由、可验证、可观测、可减载的 Agent Harness。
  2. wiki 应作为模板级 Harness，优先沉淀模式路由、系统接入模板和 feedback sensor，而不是扩写成厚重规则库。
  3. 重治理主控工程应保留治理完整性，但把快速根因链、完整沉淀链和验收关闭链显式分层。
  4. 子工程应作为实现和证据生产者，按主控裁决读取、局部实现、分层验证和 handoff 回传，不越权关闭主控状态。
- **关键动作**：
  1. **扩展升级参考**：更新 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]，新增“系统升级参考方案”，写入总目标、统一执行路由、wiki / 重治理主控工程 / 子工程分系统建议、黄金准则和三步落地顺序。
  2. **保持候选边界**：明确该方案当前仍是知识沉淀和规则候选，不直接修改 [[WORKFLOW]]、[[AGENTS]]、[[POLICY]] 或技能页。
  3. **补后续动作**：在同页后续动作中加入系统接入模板和 feedback sensor 优先级，避免后续只继续堆自然语言规则。
- **二阶反思**：这次沉淀再次确认效率治理的关键不是削弱主控证据闭环，而是把“先快后重”写成可执行路由；下一步如果要真正生效，应进入规则升级模式并同步入口、技能、模板和检查脚本。
- **影响页面**：[[articles/2026-05-25-agent-response-efficiency-governance-reflection]]、[[log]]。

### 调研 Harness Engineering 并沉淀为知识库专题

- **记录人**：sunhao
- **用户意图**：围绕用户提供的两份 Harness Engineering 本地材料做全面深入调研，形成可回看的专题沉淀，而不是只在对话里给出概念解释。
- **主题**：
  1. Harness Engineering 的核心不是提示词，而是 `Agent = Model + Harness` 这一工程系统视角。
  2. 有效 Harness 由规格、上下文、规则、Skill、Workflow、Sub Agent、脚本反馈、MCP / 工具、Memory 和可观测演化共同组成。
  3. OpenAI、LangChain、Vercel、本地 JK Launcher 案例和 X 图文都指向同一条实践线：少堆料，多用工程判断，把可判定约束下沉成脚本或反馈传感器。
- **关键动作**：
  1. **归档来源**：把用户提供的两份 HTML 归档到 `raw/harness-engineering/`，并把 X 图文里的关键图片归档到 `assets/harness-engineering/`。
  2. **新增专题卡片**：新增 [[articles/2026-05-25-harness-engineering-research]]，系统整理定义、组件地图、案例信号、成熟度模型、落地顺序、反模式和对当前文档库的启发。
  3. **新增概念页**：新增 [[concepts/harness-engineering]]，作为 Harness Engineering 的概念单一信息源。
  4. **补入口链接**：更新 [[INDEX]] 和 [[concepts/README]]，把专题和概念纳入研发方法入口。
- **二阶反思**：这次专题与当前文档库已有七层模型高度相关，但本轮仍属于知识沉淀，不直接改 [[AGENTS]]、[[WORKFLOW]] 或 [[POLICY]]；后续若要吸收为执行机制，应优先补链接检查、frontmatter 检查等 feedback sensor，而不是继续加规则正文。
- **影响页面**：[[articles/2026-05-25-harness-engineering-research]]、[[concepts/harness-engineering]]、[[INDEX]]、[[concepts/README]]、[[log]]、`raw/harness-engineering/`、`assets/harness-engineering/`。

### 纠正 agent 响应效率治理反思的层级归属

- **记录人**：sunhao
- **用户意图**：指出前一轮把 agent 响应效率治理反思放进 `projects/development/plan/` 是错误归类，并继续要求对重治理主控工程慢的问题做全面、客观分析，目标是功能完善且高效，而不是简单把治理闭环砍掉。
- **主题**：
  1. 重治理主控工程的慢主要来自主控治理链路过重，不是默认检查脚本本身慢。
  2. 当前模板库缺少针对单个简单问题的“快速诊断模式”，只有批量材料处理的轻量模式。
  3. issue 分析 + 沉淀本身是合理需求；真正要拆分的是必要成本、可优化成本和应避免成本。
  4. 该结论当前只应进入知识沉淀层，不能伪装成项目研发待办或已生效硬规则。
- **关键动作**：
  1. **迁移沉淀页**：把原 `projects/development/plan/agent-response-efficiency-upgrade-plan` 改迁到 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]，作为知识沉淀和规则候选。
  2. **撤回项目化挂载**：清理 [[projects/development/plan/README]]、[[projects/development/execution/todo]] 和 [[projects/status]] 中关于该事项的项目计划、待办和状态入口。
  3. **保留知识入口**：更新 [[INDEX]]，把该反思挂到设计思路 / 知识沉淀入口，而不是研发方法入口。
  4. **补全面分析**：扩展 [[articles/2026-05-25-agent-response-efficiency-governance-reflection]]，加入必要成本、可优化成本、应避免成本、五类响应模式、判定表和阶段性反馈目标，明确“慢的核心工作有必要，但当前慢法仍可优化”。
- **当前边界**：本轮仍没有修改 [[AGENTS]]、[[WORKFLOW]] 或 [[POLICY]] 的硬规则；如果后续要正式引入快速诊断模式，需要另起规则升级流程。
- **影响页面**：[[articles/2026-05-25-agent-response-efficiency-governance-reflection]]、[[projects/development/plan/README]]、[[projects/development/execution/todo]]、[[projects/status]]、[[INDEX]]、[[log]]。

## 2026-05-12

### 从重治理主控工程抽象吸收技能层和 issue-analysis 技能

- **记录人**：sunhao
- **用户意图**：继续检查重治理主控工程中可反哺当前模板库的技能和规则，吸收项目内 agent 技能层与问题分析方法，同时避免把下游项目事实、运行状态和业务链路带入模板库。
- **主题**：
  1. 下游项目新增的 `skills/` 层属于可复用系统结构，适合进入模板库，作为项目内 agent 分析流程、判断框架和输出格式的主入口。
  2. `issue-analysis` 技能中的事实源分层、最小根因链、计数 / 状态单位归一、跨工程分工、三层验证和回写守卫具备通用性。
  3. 下游项目里的具体业务 pipeline、服务实例、表名、运行 ID、handoff 路径和一次性事故材料属于项目材料，不进入模板技能正文。
- **关键动作**：
  1. **新增技能层**：新增 [[skills/README]]，把项目内 agent 技能和 [[templates/README]]、治理层、项目事实源区分开。
  2. **新增问题分析技能**：新增 [[skills/issue-analysis/SKILL]]，抽象沉淀主控侧 issue / incident 分析流程，覆盖问题框、上下文读取、事实源地图、状态单位归一、最小根因链、责任边界、跨工程分工、联测方案、回写守卫和禁止项。
  3. **补技能模板**：新增 [[templates/skill-template]] 并挂入 [[templates/README]]，让后续项目内技能有可复制骨架，避免每次从空白页起步。
  4. **同步入口和规则**：更新 [[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[BRAIN]]、[[POLICY]] 和 [[template-feedback-rules]]，把技能层纳入七层模型、读取顺序、路由规则、反哺范围和项目材料红线。
- **不反哺内容**：具体业务链路、服务名、数据表、运行 ID、服务实例、生产状态、TODO / Gate / 测试结论、本地路径和一次性 handoff 不进入当前模板库。
- **模板检查结果**：新增 [[templates/skill-template]]；技能正文只保留可复用流程和回写守卫，未复制第二份项目状态、TODO、测试报告或服务台账正文。
- **协作契约检查结果**：技能层仍遵守主控文档库与子工程的只读上下文和受控回写边界；技能可指导读取子工程 `AGENTS.md`、技能和 handoff，但默认不直接修改子工程。
- **影响页面**：[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[BRAIN]]、[[POLICY]]、[[template-feedback-rules]]、[[skills/README]]、[[skills/issue-analysis/SKILL]]、[[templates/README]]、[[templates/skill-template]]、[[log]]。

## 2026-05-09

### 从重治理主控工程抽象吸收研发治理规则

- **记录人**：sunhao
- **用户意图**：检查重治理主控工程中是否存在可反哺当前模板库的规则，并只吸收抽象后的系统层信息，不带入下游项目事实。
- **主题**：
  1. 下游项目暴露出运行服务治理、源码审计、跨工程 handoff 和验收证据分层四类可复用规则。
  2. 服务 IP、端口、代码提交、业务 TODO、具体测试报告和项目状态属于下游项目材料，不进入当前模板库。
  3. 反哺时优先更新既有主入口、规则页和模板页，避免复制第二份正文。
- **关键动作**：
  1. **运行治理**：新增 [[projects/service-registry]] 和 [[templates/service-registry-template]]，把服务实例台账、服务组 / 组件层级、健康检查、配置 profile、数据目录和脱敏字段口径抽象为可选项目层结构。
  2. **源码审计**：新增 [[projects/codebase/source-code-audit-workflow]] 和 [[templates/source-code-audit-report-template]]，固化 L0 到 L3 的源码工程解读等级、证据矩阵、自动推进和终态自审边界。
  3. **验收规则**：更新 [[POLICY]]、[[projects/development/reports/README]] 和 [[templates/development-test-report-template]]，吸收验收对象分层、`local validation` / `service-side validation` / `end-to-end validation`、非默认参数验证、人工确认项和报告双向关联规则。
  4. **跨工程协作**：更新 [[projects/development/execution/developer-execution-workflow]]、[[templates/code-handoff-template]] 和 [[templates/developer-task-brief-template]]，强化只读上下文、受控回写、handoff 入库、独立抽插和下游吸收边界。
  5. **入口同步**：更新 [[README]]、[[INDEX]]、[[AGENTS]]、[[WORKFLOW]]、[[BRAIN]]、[[template-feedback-rules]]、[[projects/README]]、[[projects/STRUCTURE]] 和 [[projects/codebase/README]]，补齐新页面类型的主入口、上下游关系、读取顺序和反哺边界。
- **不反哺内容**：下游项目中的具体服务实例、IP / 端口、进程、提交号、业务 TODO、测试结论、灰度状态、项目技术拍板和一次性排障过程均保留在下游项目，不写入当前模板库。
- **模板检查结果**：新增服务实例台账条目模板和源码审计报告模板；既有测试报告、编码任务执行单和代码工程回传包模板已同步扩展，项目页只链接模板，不维护第二份模板正文。
- **协作契约检查结果**：主控文档库与实现工程仍按“只读上下文 + 代码工程回传包 + 本库侧吸收”作为默认模式；直接回写本库或修改子工程都必须有明确授权。
- **影响页面**：[[README]]、[[INDEX]]、[[AGENTS]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[template-feedback-rules]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/service-registry]]、[[projects/codebase/README]]、[[projects/codebase/source-code-audit-workflow]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/reports/README]]、[[templates/README]]、[[templates/service-registry-template]]、[[templates/source-code-audit-report-template]]、[[templates/code-handoff-template]]、[[templates/developer-task-brief-template]]、[[templates/development-test-report-template]]、[[log]]。

## 2026-05-07

### 固化新应用探索从调研到研发的轻量路径

- **记录人**：sunhao
- **用户意图**：把“探索全新桌面端 / web / app 时，先轻量调研和收敛，再进入项目研发结构”的判断沉淀下来，并尽量固化成后续可复用的 agent 能力。
- **主题**：
  1. 全新应用探索不应一开始就铺满完整 `projects/`、设计包和研发拆解。
  2. 多个候选方向应先走证据层和知识沉淀层，用材料、摘要、概念和候选比较验证问题。
  3. 只有某个方向明确成为当前要推进的应用，才进入项目层并逐步补需求、trace、设计专题、决策、架构包和研发事项。
- **关键动作**：
  1. **主流程**：在 [[WORKFLOW]] 中新增 `1.9.0 新应用探索模式`，明确 discovery、轻量项目、完整研发三种交付状态和推荐演进链。
  2. **主入口**：更新 [[README]]、[[INDEX]]、[[projects/README]] 和 [[projects/STRUCTURE]]，把新应用探索路径挂到入口、项目极简模式和结构说明里。
  3. **主路由**：更新 [[BRAIN]]、[[POLICY]] 和 [[AGENTS]]，把“多方向探索先轻量路由，选定当前项目后再进项目层”固化成共享背景、路由规则和 agent 执行约束。
  4. **本地技能**：新增本地 Codex skill `app-discovery`，只保留触发条件、轻量工作流和输出形态，详细流程仍以当前文档库为单一信息源。
- **影响页面**：[[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[log]]。

## 2026-05-06

### 纠正模板库和具体工程之间的吸收方向

- **记录人**：sunhao
- **用户意图**：纠正前一轮把“模板到项目吸收边界”写成当前模板库主流程的视角错误，明确当前库是上游模板库，未来吸收应当是从具体工程中抽象系统层信息回到模板库。
- **主题**：
  1. 当前库是上游模板，不是具体项目；下游项目的不吸收清单只能作为反哺边界参考。
  2. 吸收方向固定为“具体工程 / 下游项目 -> 抽象系统层信息 -> 模板库”。
  3. 模板库不维护下游项目已吸收到哪个上游 commit、项目侧同步状态或项目侧不吸收决定。
- **关键动作**：
  1. **主纠偏**：从 [[WORKFLOW]] 中移除“模板到项目吸收模式”，回到模板反哺模式的单一方向。
  2. **主边界**：更新 [[template-feedback-rules]]，把下游非吸收清单定位为下游处理项目材料边界的参考，而不是模板库主流程。
  3. **主约束**：更新 [[AGENTS]]，要求具体工程提供的不吸收清单只用于辅助判断反哺边界，不在当前库维护项目侧同步记录。
- **影响页面**：[[WORKFLOW]]、[[template-feedback-rules]]、[[AGENTS]]、[[log]]。

### 补清模板到具体项目的吸收边界

- **记录人**：sunhao
- **用户意图**：确认从上游模板库吸收内容时，哪些内容不适合进入当前具体项目，并检查当前工程是否存在把模板示例或上游项目事实误当成项目事实的问题。
- **主题**：
  1. 从模板库吸收更新时，也要区分系统能力和模板 / 项目事实。
  2. 占位项目、示例功能点、示例 TODO、示例 Gate、示例报告、示例风险和示例执行数据不能成为目标项目事实。
  3. 目标项目应记录已吸收到的上游 commit 或版本，后续只比较新变化，避免重复吸收。
- **关键动作**：
  1. **主边界**：更新 [[template-feedback-rules]]，新增模板到项目的吸收边界，明确只吸收结构、规则、流程、模板骨架和协作契约。
  2. **主约束**：更新 [[AGENTS]]，要求具体项目吸收上游模板库时也要执行模板到项目的边界判断。
  3. **主流程**：更新 [[WORKFLOW]]，新增模板到项目吸收模式，要求记录上游 commit / 版本、吸收项和不吸收项。
- **影响页面**：[[template-feedback-rules]]、[[AGENTS]]、[[WORKFLOW]]、[[log]]。

### 把每轮结束前的二阶反思固化成学习机制

- **记录人**：sunhao
- **用户意图**：要求 agent 具备举一反三能力，能够在每次对话结束时主动反思当前问题、抽象到更高层面，并从多轮对话中持续完善系统，而不是同类问题反复等用户提醒。
- **主题**：
  1. 对话收尾不应只做结果提交，还要判断本轮暴露的是单点问题还是同类流程缺口。
  2. 可复用教训应主动回写到规则、流程、模板、协作边界或共享背景，不应只留在会话里。
  3. 二阶反思要受 [[POLICY]] 约束：可自动改既有流程和执行约束，但新增高优先级规则或改变自动写入边界时必须升级。
- **关键动作**：
  1. **主背景**：更新 [[BRAIN]]，把“系统应从每轮对话中持续学习并做二阶反思”写入共同工作方式。
  2. **主边界**：更新 [[POLICY]]，允许 agent 在收尾或被指出重复 / 同类问题时自动做二阶反思并更新既有流程、执行约束、模板入口或 [[log]]，同时保留高优先级规则的冲突升级边界。
  3. **主执行**：更新 [[AGENTS]] 和 [[WORKFLOW]]，把二阶反思加入会话级规则和收尾顺序，要求检查同类漏检、流程缺口、模板缺口、协作契约缺口和记忆路由缺口。
- **影响页面**：[[BRAIN]]、[[POLICY]]、[[AGENTS]]、[[WORKFLOW]]、[[log]]。

### 把模板和跨工程协作漏检沉淀为结构变更必检项

- **记录人**：sunhao
- **用户意图**：追问为什么相关模板和主控 / 实现工程协作边界要等用户指出后才补，要求把这类漏检转成以后不会再发生的机制。
- **主题**：
  1. 前一轮采纳项目层规则时只检查了目录和规则正文，没有把可复制模板和跨工程协作契约当成同级必检项。
  2. 新增项目层结构、事项类型、执行流程或报告类型时，必须同轮检查 `templates/` 和模板入口。
  3. 只要规则涉及当前文档库和实现工程 / 子模块协作，必须同轮写清任务下发、证据回传、写权限、状态关闭和冲突升级。
- **关键动作**：
  1. **主约束**：更新 [[AGENTS]]，把项目层结构变更时的模板完整性检查、跨工程协作边界检查写成 agent 必须遵守的硬约束。
  2. **主流程**：更新 [[WORKFLOW]]，把模板检查和主控 / 实现工程协作契约检查加入新增模块、目录和高频文件类型的固定步骤。
  3. **主反哺**：更新 [[template-feedback-rules]]，要求跨项目反哺时记录模板检查结果和协作契约检查结果，不能只写结构和规则。
- **影响页面**：[[AGENTS]]、[[WORKFLOW]]、[[template-feedback-rules]]、[[log]]。

### 补齐研发协作模板并明确主控与实现工程边界

- **记录人**：sunhao
- **用户意图**：检查项目层规则采纳后，相关模板目录和模板文件是否齐全，以及现有规则是否覆盖当前文档主控系统和实现工程子模块之间的协作。
- **主题**：
  1. 研发层新增结构已经有目录和入口，但模板层没有同步补齐，且部分模板正文散在开发页里。
  2. 主控系统和实现工程之间已有回传包、写权限模式和反馈闭环，但需要把协作边界显式写清。
  3. 模板正文应回到 [[templates/README]] 及其模板页，项目页只保留入口链接，避免两份正文漂移。
- **关键动作**：
  1. **主模板**：新增功能点、事项矩阵、TODO、Gate、测试报告、风险、开发过程记录、编码任务执行单、代码工程回传包和工程反馈模板，并统一挂到 [[templates/README]]。
  2. **主收口**：把 [[projects/development/feature-points/README]]、[[projects/development/execution/todo]]、[[projects/development/gates/README]]、[[projects/development/reports/README]]、[[projects/development/risks/README]]、[[projects/development/execution/worklog]]、[[projects/development/execution/developer-execution-workflow]] 和 [[projects/development/execution/engineering-feedback-loop]] 里的内联模板正文收回成模板链接。
  3. **主协作**：在 [[projects/development/execution/developer-execution-workflow]] 中补清主控系统和实现工程的任务下发、开发执行、测试反馈、回传吸收和冲突升级边界。
  4. **主入口**：更新 [[README]]、[[INDEX]]、[[WORKFLOW]]、[[projects/status]] 和 [[projects/memory/policy-links]]，让模板入口和功能点模板口径回到单一信息源。
- **影响页面**：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[templates/README]]、[[templates/development-feature-point-template]]、[[templates/development-work-item-matrix-template]]、[[templates/development-todo-template]]、[[templates/development-gate-template]]、[[templates/development-test-report-template]]、[[templates/development-risk-template]]、[[templates/development-worklog-entry-template]]、[[templates/developer-task-brief-template]]、[[templates/code-handoff-template]]、[[templates/engineering-feedback-template]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/execution/todo]]、[[projects/development/execution/worklog]]、[[projects/development/feature-points/README]]、[[projects/development/gates/README]]、[[projects/development/reports/README]]、[[projects/development/risks/README]]、[[projects/status]]、[[projects/memory/policy-links]]、[[log]]。

### 抽象采纳项目层研发规则而不同步项目事实

- **记录人**：sunhao
- **用户意图**：在已经沉淀跨项目反哺红线后，重新处理“从下游项目采纳新设计”的任务，重点采纳项目层面的通用规则更新，同时避免再次把具体项目事实同步进模板库。
- **主题**：
  1. 只把研发计划、执行、阶段门、实现、报告和风险这些可复用项目层结构抽象回模板。
  2. 把需求、目标、功能点、TODO、反馈、证据、风险和 Gate 准出的关系沉淀成通用事项模型。
  3. 明确不采纳下游项目里的具体业务范围、结果表、字段、运行证据、具体 Gate 内容和测试结论。
- **关键动作**：
  1. **主结构**：把开发层扩展为 [[projects/development/plan/README]]、[[projects/development/execution/README]]、[[projects/development/gates/README]]、[[projects/development/implementation/README]]、[[projects/development/reports/README]] 和 [[projects/development/risks/README]]，并把原开发流水迁到 [[projects/development/execution/worklog]]。
  2. **主模型**：新增 [[projects/development/plan/work-item-system-model]]、[[projects/development/execution/todo]]、[[projects/development/execution/developer-execution-workflow]] 和 [[projects/development/execution/engineering-feedback-loop]]，收口研发事项关系、TODO 关闭守卫、工程协作回传和反馈纠偏。
  3. **主方法**：新增 [[concepts/progressive-design-freeze]]，只保留阶段门滚动冻结的方法定义、冻结节奏和候选功能点提升标准，不带入下游项目应用页。
  4. **主同步**：更新 [[README]]、[[INDEX]]、[[AGENTS]]、[[WORKFLOW]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]] 和 [[projects/development/feature-points/README]]，让新项目层结构进入入口、读取顺序、同步规则和交付检查。
- **影响页面**：[[README]]、[[INDEX]]、[[AGENTS]]、[[WORKFLOW]]、[[concepts/README]]、[[concepts/progressive-design-freeze]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/development/README]]、[[projects/development/plan/README]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/execution/README]]、[[projects/development/execution/todo]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/execution/worklog]]、[[projects/development/gates/README]]、[[projects/development/implementation/README]]、[[projects/development/reports/README]]、[[projects/development/risks/README]]、[[projects/development/feature-points/README]]、[[log]]。

### 把跨项目误同步教训沉淀成反哺红线

- **记录人**：sunhao
- **用户意图**：在完全删除错误同步提交后，要求把这次误把具体项目事实同步进模板库的教训沉淀成规则，避免以后再次发生。
- **主题**：
  1. “采纳某项目设计”不能再被默认执行成整库同步或原样搬运项目设计页。
  2. 跨项目反哺必须先列候选分类和不反哺边界，再写入抽象后的系统层信息。
  3. 结果表、字段、灰度范围、项目 TODO、Gate、测试报告和代码审计结论这类内容默认属于项目材料，不进入模板库。
- **关键动作**：
  1. **主红线**：更新 [[template-feedback-rules]]，新增跨项目采纳红线，禁止整库同步、整目录复制、先写入再筛选。
  2. **主边界**：更新 [[POLICY]]，把跨项目采纳的自动写入边界收紧为先列候选、先做事实剥离。
  3. **主约束**：更新 [[AGENTS]]，把禁止原样同步下游项目设计写成 agent 执行约束。
- **影响页面**：[[template-feedback-rules]]、[[POLICY]]、[[AGENTS]]、[[log]]。

## 2026-04-25

### 重新定义模板反哺的系统层范围并补齐规则类反哺

- **记录人**：sunhao
- **用户意图**：纠正前一次反哺时对“可复用系统层信息”的定义过窄问题，明确只要是规则就默认进入反哺候选并必须判断，并把 DocFilmCommunity 中遗漏的规则、流程、写法和记忆路由抽象回模板库。
- **主题**：
  1. 重新定义模板反哺的系统层范围。
  2. 区分可复用系统信息和具体项目材料。
  3. 补齐 DocFilmCommunity 中已经验证的规则类反哺。
- **关键动作**：
  1. **主规则**：更新 [[template-feedback-rules]]，把可反哺系统层信息扩展为结构、流程、规则、记忆系统、写法格式、模板、自动化契约和治理说明，并明确“只要它是规则，就默认进入反哺候选”。
  2. **主边界**：在 [[template-feedback-rules]] 中补清项目材料范围，要求抽掉项目事实、业务状态、技术拍板和一次性结论，只保留可跨项目复用的系统规则。
  3. **主回填**：把 DocFilmCommunity 中关于 [[log]] 标题、同日记录复核、并列项编号、[[projects/trace]] 同轮同步和来源材料格式转换不进 trace 的规则，回写到 [[log-writing-rules]]、[[trace-writing-rules]]、[[templates/log-entry-template]]、[[templates/trace-entry-template]]、[[AGENTS]]、[[POLICY]] 和 [[WORKFLOW]]。
  4. **主同步**：补回“标签：内容”默认加粗、决策标题保持稳定、决策摘要不引入复杂 block id，以及完整架构包到研发拆解时的回链、验证、发布和交付前检查规则。
  5. **主防线**：补清“规则默认反哺”只是默认进入候选，不代表原样写入；写入前必须通过抽象、事实剥离、冲突、单一信息源和规则体积检查，后续证明不通用时要收窄、降级或退役。
  6. **主入口**：同步更新 [[README]]、[[INDEX]] 和 [[governance/README]] 中的模板反哺入口描述，避免入口页继续把反哺范围收窄成结构和模板。
- **影响页面**：
  1. [[template-feedback-rules]]
  2. [[log-writing-rules]]
  3. [[trace-writing-rules]]
  4. [[templates/log-entry-template]]
  5. [[templates/trace-entry-template]]
  6. [[AGENTS]]
  7. [[POLICY]]
  8. [[WORKFLOW]]
  9. [[README]]
  10. [[INDEX]]
  11. [[governance/README]]
  12. [[log]]

### 移除 `[[log]]` 记录标题里的旧固定前缀

- **记录人**：sunhao
- **用户意图**：检查模板库里是否仍然遗漏旧版 `[[log]]` 标题前缀，并按最新设计移除这段固定前缀。
- **主题**：
  1. 清理 `[[log]]` 历史记录标题里的旧前缀。
  2. 同步日志模板和日志写法规则。
- **关键动作**：
  1. **主修正**：批量移除 [[log]] 中所有三级标题开头的旧固定前缀，保留原本标题内容。
  2. **主同步**：更新 [[templates/log-entry-template]] 和 [[log-writing-rules]]，明确三级标题直接写一句话标题，不再加旧版固定前缀。
- **影响页面**：[[log]]、[[templates/log-entry-template]]、[[log-writing-rules]]。

### 把 DocFilmCommunity 的系统级进化反哺回 wiki 模板

- **记录人**：sunhao
- **用户意图**：解决不同项目各自演化后如何反哺模板库的问题，并把 DocFilmCommunity 中已经验证过的系统性规则、结构和模板抽象回当前 wiki 模板，但不带入具体项目事实。
- **主题**：
  1. 建立跨项目模板反哺机制。
  2. 抽象 DocFilmCommunity 的结构性演进。
  3. 同步项目层、设计层、会议层、决策写法和研发拆解流程。
- **关键动作**：
  1. **主机制**：新增 [[template-feedback-rules]]，明确下游项目反哺模板时要先区分项目事实和系统能力，再按结构、流程、规则、模板和知识沉淀分流。
  2. **主结构**：新增 [[projects/codebase/README]] 与代码基线子页，补入现实实现审计、冲突收口和复用边界；新增 [[projects/design/topics/README]]，承接未拍板设计专题和后续储备。
  3. **主设计包**：把设计层扩展成完整架构包，补齐 [[projects/design/backend-frontend-structure]]、[[projects/design/permission-boundary]]、[[projects/design/write-boundary]]、[[projects/design/deployment]] 和 [[projects/design/runtime-quality]]。
  4. **主流程**：更新 [[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]] 和项目入口，补上模板反哺模式、代码基线读取顺序、设计专题路由、完整架构包到功能点拆解、会议去重和决策写法骨架。
  5. **主模板**：新增 [[templates/decision-entry-template]]，并收紧 [[templates/meeting-entry-template]] 中会议行动项、会后回写和单条记录内去重的写法。
- **影响页面**：
  1. [[template-feedback-rules]]
  2. [[README]]
  3. [[INDEX]]
  4. [[governance/README]]
  5. [[BRAIN]]
  6. [[POLICY]]
  7. [[WORKFLOW]]
  8. [[AGENTS]]
  9. [[projects/README]]
  10. [[projects/STRUCTURE]]
  11. [[projects/status]]
  12. [[projects/codebase/README]]
  13. [[projects/design/README]]
  14. [[projects/design/topics/README]]
  15. [[projects/decisions]]
  16. [[projects/development/README]]
  17. [[projects/development/feature-points/README]]
  18. [[projects/meetings/README]]
  19. [[templates/decision-entry-template]]
  20. [[templates/meeting-entry-template]]
  21. [[log]]

## 2026-04-14
## 2026-04-13
### 确认会议记录默认是一会一条，预读材料则单独成页

- **记录人**：sunhao
- **用户意图**：确认正式会议到底是按“每个会议一个文件”组织，还是默认在同一个会议时间线里按条目记录，并厘清准备、会议记录和结论是否放在一起；同时确认如果明天要把会议问题发给对方提前看，该怎么组织。
- **主题**：
  1. 明确正式会议的默认承载方式。
  2. 明确单场会议内部的内容组织方式。
  3. 明确会前需要对外共享时的材料落点。
- **关键动作**：
  1. **主澄清**：在 [[projects/meetings/README]] 里补充规则，明确默认一场会不单独生成一个文件，而是在 [[projects/meetings/worklog]] 里写成一条记录。
  2. **主收口**：确认准备材料、会议纪要、结论和行动项默认放在同一条会议记录里，只有特别大的会议才再单独拆页。
  3. **主分流**：如果会前要发给对方提前看，优先单独开一页可分享的会前材料 / 议程页，不把预读材料只埋在 [[projects/meetings/worklog]] 的长时间线里。
- **影响页面**：[[projects/meetings/README]]、[[projects/meetings/worklog]]、[[templates/meeting-entry-template]]、[[log]]。

## 2026-04-13
### 把会议记录骨架提炼成可复用模板页

- **记录人**：sunhao
- **用户意图**：在已经拆出会议主入口和会议记录页之后，希望把单场会议的记录骨架再提炼成模板页，后续新增正式会议时可以直接复制使用。
- **主题**：
  1. 把会议记录骨架抽成模板。
  2. 让会议记录入口和模板互相可达。
- **关键动作**：
  1. **主新增**：新增 [[templates/meeting-entry-template]]，把正式会议记录的字段骨架、分流口径和使用说明沉淀成可复制模板。
  2. **主联通**：更新 [[templates/README]]、[[projects/meetings/worklog]] 和 [[governance/WORKFLOW]]，让模板从模板入口、会议记录页和治理流程里都能直接找到。
- **影响页面**：[[templates/meeting-entry-template]]、[[templates/README]]、[[projects/meetings/worklog]]、[[governance/WORKFLOW]]、[[log]]。

### 把正式会议从开发 worklog 拆出到专门会议入口

- **记录人**：sunhao
- **用户意图**：项目管理期间会议会很多，希望把正式会议材料、会议纪要和行动项单独收口，不再和开发过程流水混在一起，同时把会议管理的规则和流程沉淀成稳定入口。
- **主题**：
  1. 把正式会议从开发 worklog 中拆出独立层。
  2. 给会议材料、纪要、行动项和会后分流建立固定入口。
  3. 把会议组织规则和流程写进治理层与项目层。
- **关键动作**：
  1. **主新增**：创建 [[projects/meetings/README]] 和 [[projects/meetings/worklog]]，把正式会议入口、记录模板和时间线记录单独收口。
  2. **主同步**：更新 [[projects/README]]、[[projects/STRUCTURE]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/status]]、[[projects/memory/README]]、[[INDEX]] 和 [[README]]，让项目主入口、结构页和常用入口都能直接找到会议层。
  3. **主治理**：在 [[governance/WORKFLOW]] 和 [[AGENTS]] 里补上会议材料的收集、记录、分流和阅读顺序，并用 [[projects/decisions]]、[[projects/trace]] 记录这次结构拆分。
- **影响页面**：[[projects/meetings/README]]、[[projects/meetings/worklog]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/status]]、[[projects/memory/README]]、[[governance/README]]、[[governance/WORKFLOW]]、[[AGENTS]]、[[projects/decisions]]、[[projects/trace]]、[[INDEX]]、[[README]]、[[log]]。

### 把 Obsidian 的依赖说明写清楚

- **记录人**：sunhao
- **用户意图**：确认这套文档库是否能脱离 Obsidian 使用，避免把 `[[wikilink]]` 体系误写成可选功能。
- **主题**：
  1. 澄清 Obsidian 对内部导航的实际作用。
  2. 让入口页把“正文可读”和“链接可用”分开说清。
- **关键动作**：
  1. **主修正**：更新 [[README]] 和 [[INDEX]]，把 Obsidian 描述为这套库的原生阅读 / 编辑入口，并明确不用 Obsidian 时 `[[wikilink]]` 导航不能完整生效。
  2. **主收口**：把“普通 Markdown 阅读器也能读正文”与“完整链接网络依赖 Obsidian”分开表述，避免使用者误解为只是体验差异。
- **影响页面**：[[README]]、[[INDEX]]、[[log]]。

## 2026-04-13
### 把 commit message 的语言规则写进维护约束

- **用户意图**：明确协作时的提交信息规范，正文内容可以继续用中文，但 commit message 必须统一用英文。
- **主题**：
  1. 把 commit message 语言要求提升为维护约束。
  2. 保留正文和说明可中文的现有写作习惯。
- **关键动作**：
  1. **主更新**：在 [[AGENTS]] 的会话级规则里补充 commit message 必须使用英文的约束。
  2. **主澄清**：说明正文、说明和文档内容仍然可以使用中文，不影响既有写作习惯。
- **影响页面**：[[AGENTS]]、[[log]]。

## 2026-04-13
### 把已经处理过的 PRD 源稿从 `raw` 迁出，明确处理后内容只留在知识库层

- **用户意图**：确认 PRD 教程在经过整理后不应继续占用 `raw/`，而应该回到知识库层；只有还没处理的原始材料才继续留在 `raw/`。
- **主题**：
  1. 纠正 PRD 教程的分层归属。
  2. 强化 `raw/` 与知识库层的边界。
- **关键动作**：
  1. **主迁出**：把 [[archive/2026-04-13-prd-writing-guide-source]] 从 `raw/` 迁出，让这份已经处理过的源稿不再占用 `raw/`。
  2. **主对齐**：同步更新 [[concepts/prd-writing]] 和 [[articles/2026-04-13-prd-writing-guide]] 的来源链接，改指向历史草稿而不是 `raw/`。
  3. **主收紧**：在 [[raw/README]] 里补一句更明确的维护原则，说明已经整理成摘要、概念页、索引页或历史版本的内容，不应继续留在 `raw/`。
- **影响页面**：[[archive/2026-04-13-prd-writing-guide-source]]、[[concepts/prd-writing]]、[[articles/2026-04-13-prd-writing-guide]]、[[raw/README]]、[[log]]。

## 2026-04-13
### 把 PRD 指导重排成可复用的方法入口，并接入项目需求和设计流程

- **用户意图**：把新增加的 PRD 指导从一篇偏长的原始材料整理成可复用的方法入口，让它不只“能看”，还要能反向指导项目层的需求、设计和开发。
- **主题**：
  1. 重排 PRD 原始稿并去重。
  2. 抽出 PRD 写作方法页和摘要卡片。
  3. 把 PRD 方法接到项目需求、设计和 workflow。
- **关键动作**：
  1. **主整理**：重写 [[archive/2026-04-13-prd-writing-guide-source]]，按定义、常见误区、标准结构、思考顺序、专业细节、模板、自检和落库路径重新组织，删掉原稿里重复铺陈和来回兜圈的部分。
  2. **主沉淀**：新增 [[concepts/prd-writing]] 和 [[articles/2026-04-13-prd-writing-guide]]，把 PRD 写作方法沉淀成稳定概念页和摘要卡片。
  3. **主接线**：在 [[projects/README]]、[[projects/requirements]]、[[projects/design/README]]、[[WORKFLOW]] 和 [[INDEX]] 中补上 PRD 方法入口与项目落点，让需求页和设计页可以直接引用。
- **影响页面**：[[archive/2026-04-13-prd-writing-guide-source]]、[[concepts/prd-writing]]、[[articles/2026-04-13-prd-writing-guide]]、[[projects/README]]、[[projects/requirements]]、[[projects/design/README]]、[[WORKFLOW]]、[[INDEX]]、[[concepts/README]]、[[log]]。

## 2026-04-12
### 继续把项目层和治理页的旧口径收口到新治理结构

- **用户意图**：在治理层已经迁入 `governance/` 之后，继续把 `projects/` 层和直接相关治理页里残留的旧表述收口干净，避免入口页已经切换了，但项目结构页和项目主页还在按旧的根目录治理模型写说明。
- **主题**：
  1. 同步项目层对新治理结构的说明口径。
  2. 继续收紧项目页和治理页中的裸文件名引用。
- **关键动作**：
  1. **主同步**：更新 [[projects/README]] 和 [[projects/STRUCTURE]]，把治理层总边界正式改为指向 [[governance/README]]，并补上项目层如何依赖治理层的新说明。
  2. 把项目主页、项目结构页和 [[WORKFLOW]] 中这轮直接碰到的 [[BRAIN]]、[[POLICY]]、[[projects/decisions]] 等旧文件名字符串继续收成 [[wikilink]]，避免治理迁移后留下半旧半新的表达。
  3. 在项目层的“默认读取顺序”和“依赖关系”里补上新的治理入口，让后续处理项目记忆、规则和状态时，不再默认只按旧根目录路径理解治理页。
- **影响页面**：[[projects/README]]、[[projects/STRUCTURE]]、[[WORKFLOW]]、[[log]]。

### 把治理层正式收口成目录，并明确 `AGENTS` / `POLICY` 边界

- **用户意图**：确认之前关于“入口 / 治理 / 运行 / 沉淀 / 历史”等分层概念其实已经出现，但边界还不够清楚；同时质疑规则长期散落在根目录不合适，希望同时从逻辑结构和物理结构上把治理层收口，并明确 `AGENTS` 和规则层到底怎么分工。
- **主题**：
  1. 正式把文档系统分层明确成可复用的治理模型。
  2. 把治理层从根目录轻量收口到独立目录。
  3. 澄清 `AGENTS`、`POLICY`、`WORKFLOW`、`BRAIN` 的职责边界。
- **关键动作**：
  1. **主收口**：新增 [[governance/README]]，把整套系统正式定义成入口层、治理层、运行层、沉淀层、历史层、证据层六层模型，并把治理层的逻辑结构与物理结构统一写清。
  2. 将 [[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[log-writing-rules]]、[[trace-writing-rules]] 迁入 `governance/`，结束规则与写法指南继续散落在根目录的状态。
  3. 保留 [[AGENTS]] 在根目录作为 agent 的特殊入口，同时在 [[governance/README]] 和 [[AGENTS]] 中明确说明：[[POLICY]] 负责“怎么判”，[[AGENTS]] 负责“怎么执行”，[[WORKFLOW]] 负责“怎么推进”，[[BRAIN]] 负责“默认带什么背景”。
  4. 重写 [[README]] 和 [[INDEX]] 的入口说明，让总入口不再把治理页误写成根目录平铺页面，而是显式指向 [[governance/README]] 和新的治理层组织方式。
- **影响页面**：[[README]]、[[INDEX]]、[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[BRAIN]]、[[POLICY]]、[[log-writing-rules]]、[[trace-writing-rules]]、[[log]]。

### 把 `[[projects/trace]]` 的人员与时间信息下沉到迭代级

- **用户意图**：指出同一个问题在 trace 过程中往往会有不同的人、不同时间参与，因此质疑当前把“记录人”放在主题主链顶层是否合理，希望把这部分设计调整到更贴近真实协作链路的版本。
- **主题**：
  1. 调整 trace 的人员信息落点。
  2. 调整 trace 的时间与角色信息落点。
- **关键动作**：
  1. **主调整**：在 [[trace-writing-rules]] 中把 `记录人` 从主题级默认字段改成迭代级默认字段，并明确主题级默认不写单个 `记录人`。
  2. 在 [[trace-writing-rules]] 和 [[templates/trace-entry-template]] 中补上迭代级 `角色` 字段，用于表达“产品 / 研发 / agent / 用户确认”等参与视角，但保持可选。
  3. 在 [[projects/trace]] 的现有示例中删掉主题级 `记录人`，改为在 `2026-04-12` 迭代块里写 `sunhao` 和 `agent`，让样例和新规则一致。
  4. 在 [[WORKFLOW]] 中同步把执行口径改成“人和更细时间默认落在迭代块”，避免后续写 trace 时再次漂回主题级。
- **影响页面**：[[trace-writing-rules]]、[[templates/trace-entry-template]]、[[projects/trace]]、[[WORKFLOW]]、[[log]]。

### 为 `[[projects/trace]]` 补齐记录人、日期和文字渲染规则

- **用户意图**：指出 trace 目前还缺少像 `[[log]]` 一样可直接执行的细节，包括人员信息记录、必要日期信息和文字渲染方式，希望把这些元信息和排版规则补到足够完善。
- **主题**：
  1. 为 trace 增加记录人与日期规则。
  2. 为 trace 增加和 `[[log]]` 一致的文字渲染约束。
- **关键动作**：
  1. **主补齐**：在 [[trace-writing-rules]] 中新增“记录人与日期怎么写”，明确记录人优先使用 `git user.name`，迭代块必须带日期，默认写到天，同日多次收敛时才升级到分钟。
  2. 在 [[trace-writing-rules]] 中新增“怎么做文字渲染”，把字段名加粗、短标签加粗、正文不整段加粗的约束补成显式规则，并和 `[[log]]` 保持一致。
  3. 在 [[templates/trace-entry-template]] 中补上“记录人”“YYYY-MM-DD 或 YYYY-MM-DD HH:mm”“主收敛 / 主替换 / 主纠偏”等写法，让模板可以直接套用。
  4. 按新规则回写 [[projects/trace]] 的现有示例，把 `sunhao`、字段加粗和重点短标签补齐，形成一个更可复用的样例。
- **影响页面**：[[trace-writing-rules]]、[[templates/trace-entry-template]]、[[projects/trace]]、[[WORKFLOW]]、[[log]]。

### 让 `[[projects/trace]]` 的文件、规则和模板对齐 `[[log]]` 的治理方式

- **用户意图**：要求 trace 的相关设计参考 `[[log]]`，尤其是文件职责、规则主入口和模板格式，不要让 trace 只有主文件，没有像 `[[log]]` 那样清晰的配套治理结构。
- **主题**：
  1. 为 trace 补齐规则主入口和模板入口。
  2. 把 `[[projects/trace]]` 收成“正文 + 跳转”的主文件形态。
- **关键动作**：
  1. **主收口**：新增 [[trace-writing-rules]]，把 `[[projects/trace]]` 的记录单位、续写旧主题与新开主题的边界、以及和 `[[log]]` / [[projects/decisions]] / [[projects/memory/README]] 的分工统一迁过去。
  2. 新增 [[templates/trace-entry-template]]，给需求演进链提供可直接复用的主链模板和迭代块模板，并在 [[templates/README]] 中补入口。
  3. 把 [[projects/trace]] 自身收短成主文件，只保留职责说明、规则跳转、模板跳转和当前主题正文，不再在主文件里重复展开完整写法。
  4. 在 [[README]]、[[INDEX]] 和 [[WORKFLOW]] 中补上 trace 规则入口和模板入口，保持和 `[[log]]` 同样的治理模式。
- **影响页面**：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[projects/trace]]、[[trace-writing-rules]]、[[templates/trace-entry-template]]、[[templates/README]]、[[log]]。

### 为项目层新增 `[[projects/trace]]` 需求演进链

- **用户意图**：确认当前体系可以正式新增 trace 链路，并要求按结构性扩展的标准全面整改，让项目推进里“产品梳理、技术选型、架构设计、功能设计到 agent 开发”的链路有一个明确落点，而不是继续只靠 `[[log]]` 和零散项目页承接。
- **主题**：
  1. 为项目运行层新增需求演进链主入口。
  2. 同步更新规则、流程、入口和项目结构，让 trace 成为正式职责。
- **关键动作**：
  1. **主新增**：新建 [[projects/trace]]，把它定义成项目层里记录原始意图、约束变化、修补性需求、关键决策变化和最终实现口径的主文件。
  2. 在 [[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]] 中同步补上 trace 的职责、边界和路由，明确它不是第二份 `[[log]]`，也不是第二份 `[[projects/decisions]]`。
  3. 在 [[projects/README]]、[[projects/STRUCTURE]]、[[projects/requirements]]、[[projects/design/README]]、[[projects/decisions]]、[[projects/development/README]]、[[projects/development/execution/worklog]] 和 [[projects/memory/README]] 中补上 trace 的入口、依赖关系和读取顺序。
  4. 把当前文档系统项目自身的“从知识库底座到项目运行链路”的收敛过程写成 [[projects/trace]] 的首条主题，给后续使用留一个最小样例。
- **影响页面**：[[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/requirements]]、[[projects/trace]]、[[projects/design/README]]、[[projects/decisions]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/memory/README]]、[[log]]。

### 区分 `[[log]]` 与需求演进 trace，并把收尾模式补成显式协议

- **用户意图**：确认 `[[log]]` 和需求演进 trace 是否其实是同一件事；如果不是，就说明差别在哪里。同时判断现有“收尾”是否已经足够稳，如果还能更稳，就把收尾流程补成更明确的执行协议。
- **主题**：
  1. 说明 `[[log]]` 与需求演进 trace 的职责边界。
  2. 把“收尾”从隐含习惯补成显式模式。
- **关键动作**：
  1. **主澄清**：确认 `[[log]]` 仍然是按对话组织的主题化历史，重点回答“这轮对话在解决什么”；而需求演进 trace 如果将来要加，会更偏向“需求如何从原始意图一路收敛到最终实现”，两者不是同一层信息。
  2. 在 [[AGENTS]] 中新增收尾模式硬约束，明确只有用户明确下达“收尾 / 执行收尾 / finalize”这类执行命令才进入收尾模式，而且进入后不再继续扩需求或顺手开发。
  3. 在 [[WORKFLOW]] 中补一段“收尾怎么执行”，把范围确认、同步、`[[log]]` 补记、一致性检查和提交顺序写成显式步骤。
  4. 同时把“预存脏改动默认不纳入本次收尾”补成执行边界，避免收尾时误把别的主题一起打包提交。
- **影响页面**：[[AGENTS]]、[[WORKFLOW]]、[[log]]。

### 明确 `[[log]]` 单日内部的记录顺序也要按降序维护

- **记录人**：sunhao
- **用户意图**：确认 `[[log]]` 不只是日期分组按降序，同一天内部的多条对话记录也应保持最新在前，避免日期降序了但单日内部仍按正序追加，导致阅读顺序不一致。
- **主题**：
  1. 明确 `[[log]]` 的排序规则需要同时覆盖“日期层”和“单日内部层”。
  2. 把单日内部也按降序维护补成显式规则。
- **关键动作**：
  1. **主澄清**：在 [[log-writing-rules]] 中补上两层排序规则，明确日期按降序，同一天内部的多条记录也按降序，最新完成或最新补写的那条放最前面。
  2. 在 [[WORKFLOW]] 中同步补一句执行口径，明确当天如果新增记录，应直接插到该日期下面最前面。
  3. 在 [[templates/log-entry-template]] 中把说明改成“同一天可以有多条，且当天最新的一条放最前面”，避免模板使用者只看到“同一天可以有多条”，却没看到内部排序要求。
  4. 在 [[AGENTS]] 中把 `[[log]]` 的职责描述也补成同一句话，确保规则层、流程层和模板层口径一致。
- **影响页面**：[[log-writing-rules]]、[[WORKFLOW]]、[[templates/log-entry-template]]、[[AGENTS]]、[[log]]。

### 收紧 `[[log]]` 的文字强调方式，避免加粗过度

- **记录人**：sunhao
- **用户意图**：明确 `[[log]]` 在文字渲染上还能怎么提升，并判断“主题”“关键动作”等字段是否适合加粗；目标是提升扫读效率，但不把页面做成一片高亮噪声。
- **主题**：
  1. 明确哪些位置适合加粗，哪些位置不适合。
  2. 把文字强调方式补成可复用的轻量规则。
- **关键动作**：
  1. **主判断**：确认字段名和关键动作短标签加粗是合适的，因为它们能提升扫描速度，但整句整段加粗不合适，会把真正的重点冲淡。
  2. 在 [[log-writing-rules]] 中新增“怎么做文字强调”，把字段名加粗、短标签加粗、正文不整段加粗写成明确约束。
  3. 在 [[templates/log-entry-template]] 中把“记录人 / 用户意图 / 主题 / 关键动作 / 影响页面”改成加粗字段名，同时把关键动作示例改成加粗短标签。
  4. 在 [[WORKFLOW]] 中同步补一条执行口径，明确 `[[log]]` 只做轻量强调，不做整段粗体。
- **影响页面**：[[log-writing-rules]]、[[templates/log-entry-template]]、[[WORKFLOW]]、[[log]]。

### 增强 `[[log]]` 单条记录内部的重点呈现方式

- **记录人**：sunhao
- **用户意图**：让 `[[log]]` 的每条记录在内部更容易一眼看到重点，而不是字段齐全但读者还要自己再提炼；同时避免为了强调重点而把模板继续写重。
- **主题**：
  1. 明确 `[[log]]` 重点应主要靠顺序和首条信息来突出。
  2. 为模板和流程补上可直接执行的“重点写法”。
- **关键动作**：
  1. **主收口**：在 [[log-writing-rules]] 中新增“怎么把重点写出来”，明确标题写主变化、主题按重要性排序、关键动作第 1 条先写主结果。
  2. 在 [[templates/log-entry-template]] 中把“用户意图”“主题”“关键动作”的默认写法改成更强调重点的版本，要求主题第 1 条先写核心主题、关键动作第 1 条先写主决定 / 主修正 / 主收口。
  3. 在 [[WORKFLOW]] 中同步补一条执行口径，明确写 `[[log]]` 时优先靠顺序来强调重点，而不是再增加一层新字段。
- **影响页面**：[[log-writing-rules]]、[[templates/log-entry-template]]、[[WORKFLOW]]、[[log]]。

### 修正 `[[log]]` 的过度合并，并补上长期防线

- **用户意图**：解决“4 月 12 日被压成单条总记录”的问题，区分“防碎片重复”和“防按天汇总化”这两类约束，让后续写 `[[log]]` 时既不碎，也不把同日多轮对话压扁。
- **主题**：
  1. 明确同一天、同文件、同领域都不是自动合并理由。
  2. 为 `[[log]]` 增加“过度合并”风险信号和新开记录触发条件。
  3. 把 2026-04-12 从单日总记录拆回多条真实对话记录。
- **关键动作**：
  1. **主修正**：在 [[AGENTS]] 中补成硬约束，明确日期只是分组容器，不是合并单位；同一天、同文件、同领域都不能自动合并。
  2. 在 [[AGENTS]] 中新增一条反向检查：如果合并后只能用“完善 `[[log]]`”“继续调整规则”这类宽标题概括，说明已经合并过度，应拆回多条。
  3. 在 [[log-writing-rules]] 中补充“过度合并的风险信号”“同日记录怎么判断”，并明确从“实施改动”切换到“解释为什么前一条写错、为什么会漏、怎样长期避免”时，通常应新开记录。
  4. 在 [[WORKFLOW]] 的 `[[log]]` 写法里补一条执行检查，要求开始解释上一条为什么写错或怎样长期避免时，不再并到旧记录里。
  5. 重写 2026-04-12 的 `[[log]]` 样例，把此前被压成一天一条的总括记录拆回多条按对话组织的记录。
- **影响页面**：[[AGENTS]]、[[log-writing-rules]]、[[WORKFLOW]]、[[log]]。

### 判断最近被拆开的 `[[log]]` 记录其实应当回并，并沉淀“完善优先”规则

- **用户意图**：解决最近两条记录明明在说同一件事，却因为后续补充和命名收口被拆成相邻两条的问题；让 `[[log]]` 在“补旧记录”和“新开记录”之间有更稳定的判断顺序。
- **主题**：
  1. 下游处理“上一条的补完”与“新的独立对话”之间的边界。
  2. 防止相邻两条记录各承接同一意图的不同碎片。
- **关键动作**：
  1. **主回并**：回看最近两条关于“记录人”字段的 `[[log]]` 记录，确认它们本质上属于同一条日志治理意图，于是合并为同一条记录。
  2. 在 [[log-writing-rules]] 中新增“完善优先规则”，要求在新开记录前先判断这次是不是只在纠正、补全、收短、重命名或格式化上一条记录。
  3. 在 [[log-writing-rules]] 中补充“什么时候必须新开记录”和“完整但不重复”，把“记录完善”与“相邻不重复”拆开表述。
  4. 在 [[WORKFLOW]] 中同步收紧执行口径：如果这次只是对上一条相关记录的补完、纠偏、重命名、格式统一或样例同步，优先直接完善旧记录。
- **影响页面**：[[log]]、[[log-writing-rules]]、[[WORKFLOW]]。

### 收紧 `[[log]]` 的编号模式、模板唯一正文和内部链接检查

- **用户意图**：修正 `[[log]]` 写法里仍然存在的格式漂移、模板重复和内部链接失效问题，并把这些问题变成交付前就会被拦下来的硬约束。
- **主题**：
  1. 把主题和关键动作的列表编号模式从示例提升成规则。
  2. 清掉模板正文重复，恢复模板页的单一信息源。
  3. 修正内部页面引用不能点击的问题，并把它升级成检查项。
- **关键动作**：
  1. **主收口**：把“主题”和“关键动作”统一收成编号列表，并同步更新 [[log]]、[[WORKFLOW]] 和 [[templates/log-entry-template]] 的写法。
  2. 删掉 [[log]] 和 [[WORKFLOW]] 中重复展开的模板正文，只保留规则说明和对 [[templates/log-entry-template]] 的跳转。
  3. 把模板入口中那些纯文本文件名或反引号文件名改成真正可点击的 `[[wikilink]]`。
  4. 在 [[AGENTS]] 和 [[WORKFLOW]] 中新增专项检查，明确禁止复制第二份模板正文，并要求凡是语义上在引用本库页面、模板页、入口页或跳转目标，都必须写成 `[[wikilink]]`。
  5. 同时追查最近几轮实际有变更却没同步写入 `[[log]]` 的遗漏，并把“有实际内容或结构变更就必须同步更新 `[[log]]`”明确写进 [[AGENTS]] 与 [[WORKFLOW]]。
- **影响页面**：[[log]]、[[templates/log-entry-template]]、[[WORKFLOW]]、[[AGENTS]]。

### 回填近期 `[[log]]` 历史，并明确跨日期的延续、重开和回填边界

- **用户意图**：解决最近几轮记录漏写、错位到 2026-04-12 名下，以及跨日期时“应该回并旧记录还是新开当天记录”的判断混乱。
- **主题**：
  1. 追补近期漏记和错位的历史记录。
  2. 明确跨日期时的延续、重开和回填边界。
- **关键动作**：
  1. **主回填**：把前几天真实发生的修正按原始对话日期回填，而不是继续误记在 2026-04-12 名下。
  2. 在 [[log-writing-rules]] 中把“延续 / 重开 / 回填”从隐含习惯补成显式边界，明确跨日期默认在当天新增记录。
  3. 只有在纠正旧记录日期归属或补记本来就属于当时那轮对话的遗漏内容时，才按回填处理。
  4. 顺手整合错位、重复和分散的旧记录，减少历史里因为日期判断不清造成的噪声。
- **影响页面**：[[log]]、[[log-writing-rules]]、[[WORKFLOW]]。

### 抽出 `[[log]]` 的完整规则主入口，并补齐合并与拆解标准

- **用户意图**：把 `[[log]]` 从“历史页里夹着规则说明”的状态，收口成“历史页只放历史、规则页专门讲写法”的结构；同时让合并与拆解不再靠临场感觉。
- **主题**：
  1. 为 `[[log]]` 建立唯一规则入口。
  2. 把记录级合并与主题级合并拆成两层判断。
- **关键动作**：
  1. **主建模**：新建 [[log-writing-rules]]，把 `[[log]]` 的记录单位、合并与拆解标准、记录级 / 主题级判断统一迁过去，作为唯一主入口。
  2. 把 [[log]] 顶部从完整规则正文收短成历史页说明，只保留对 [[log-writing-rules]] 和 [[templates/log-entry-template]] 的跳转。
  3. 在 [[log-writing-rules]] 中把判断标准明确成“用户意图、主结果、因果链和回看成本”，不再只靠隐含口径。
  4. 同步收短 [[WORKFLOW]] 与模板入口里的重复展开，让规则、模板、历史三层职责重新归位。
- **影响页面**：[[log]]、[[log-writing-rules]]、[[WORKFLOW]]、[[templates/log-entry-template]]、[[README]]、[[INDEX]]。

### 为 `[[log]]` 增加记录人字段，并统一字段命名

- **记录人**：sunhao
- **用户意图**：让 `[[log]]` 在需要时能标明记录人，但来源要稳定、可迁移，不回退到本机用户名；同时把字段命名收成一个一致版本。
- **主题**：
  1. 为 `[[log]]` 增加“记录人”字段，并把来源收口到 `git user.name`。
  2. 把字段命名从“记录人（可选）”收成“记录人”。
- **关键动作**：
  1. **主收口**：确认当前仓库的 `git user.name` 为 `sunhao`，适合作为 `[[log]]` 中“记录人”字段的默认来源。
  2. 在 [[log-writing-rules]] 中补充记录人规则，明确需要标注时优先写 `git user.name`；如果仓库没有配置，就留空，不回退到本机用户名。
  3. 在 [[templates/log-entry-template]] 中加入“记录人”字段，并补充使用说明。
  4. 把 [[log-writing-rules]]、[[templates/log-entry-template]] 和示例记录里的字段名统一收成“记录人”，不再把“可选”写进正文。
- **影响页面**：[[log-writing-rules]]、[[templates/log-entry-template]]、[[log]]。

### 为批量同类材料增加轻量批处理模式

- **用户意图**：在不降低质量的前提下，减少批量处理同类材料时重复读取同一组入口页的成本，让 agent 能先做一轮全局校准，再在同批材料上复用。
- **主题**：
  1. 为高频同类材料处理增加轻量路径。
  2. 明确什么时候必须退出批处理模式，回到完整上下文判断。
- **关键动作**：
  1. **主新增**：在 [[AGENTS]] 中新增“批处理模式”，明确适用范围、退出条件和禁止场景。
  2. 在 [[WORKFLOW]] 中新增“轻量批处理模式”，把批次级校准、共享读取和升级回默认流程的顺序写清楚。
- **影响页面**：[[AGENTS]]、[[WORKFLOW]]。

## 2026-04-11

### 修正 `[[log]]` 的记录粒度和动作完整度

- **用户意图**：让 `[[log]]` 既能提炼用户真正想解决的问题，又不要因为过度摘要而丢掉关键改动；同时明确每次对话都要有一个主题或多个主题，只是不必把每个问题拆开单记。
- **主题**：
  1. 把 `[[log]]` 的记录单位从“按天压成一个主题”改成“按对话记录”。
  2. 恢复 `[[log]]` 历史条目中过度压缩的修改动作细节。
- **关键动作**：
  1. **主修正**：重写 `[[log]]`、[[WORKFLOW]]、[[POLICY]]、[[AGENTS]]、[[README]]、[[INDEX]]、[[BRAIN]] 和模板文件中关于 `[[log]]` 的定义，明确记录单位是“每次对话”，同一天可以有多条记录，一次对话可以包含一个或多个相关主题。
  2. 补充 [[log]] 和 [[templates/log-entry-template]] 的条目骨架，把“对话”“主题”“用户意图”“关键动作”“影响页面”固定成默认结构。
  3. 回填历史条目时恢复更完整的动作列表，避免只剩笼统摘要。
- **影响页面**：[[log]]、[[WORKFLOW]]、[[POLICY]]、[[AGENTS]]、[[README]]、[[INDEX]]、[[BRAIN]]、[[templates/log-entry-template]]。

### 重构 `[[log]]` 的记录模型

- **用户意图**：让 `[[log]]` 不再只记“改了什么”，而是能回看用户这轮真正想解决的问题；记录顺序改为时间降序；提问内容按主题提炼，不机械抄写所有问句。
- **主题**：
  1. 让 `[[log]]` 从动作流水改成带用户意图的主题化记录。
- **关键动作**：
  1. **主重构**：重写 `[[log]]` 的说明和历史条目结构，把记录口径收成“主题 + 用户意图 + 关键动作 + 受影响页面”。
  2. 同步更新 [[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/README]] 对 `[[log]]` 的职责描述。
  3. 新增 [[templates/log-entry-template]]，并在 [[log]] 与 [[WORKFLOW]] 中补入推荐骨架，方便后续直接套用。
- **影响页面**：[[log]]、[[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/README]]、[[templates/log-entry-template]]。

### 把角色和 memory 的说明上提到根入口

- **用户意图**：纠正角色 / memory 说明的位置，把框架级解释放在最外层，而不是项目层。
- **主题**：
  1. 角色分层和 memory 分层的关系。
  2. 框架级说明的最终落点。
- **关键动作**：
  1. **主上提**：先在项目层尝试承接 role / memory 说明，随后把解释性内容从 `projects/memory/` 和 `projects/design/memory/` 中移出，最终放到根 `README.md`。
  2. 同时在 [[BRAIN]] 和 [[POLICY]] 增加边界说明，让框架级说明、共享背景和规则层各自归位。
  3. 让 `projects/design/memory/README.md` 只保留研究入口，不再承接框架正文。
  4. 把 2026-04-10 的初次讨论和这次最终纠正合并成连续历史，不重复记两套正文。
- **影响页面**：[[README]]、[[BRAIN]]、[[POLICY]]、[[projects/design/memory/README]]。

## 2026-04-10

### 确认 memory 沉淀的边界和从 log 到 memory 的提炼方式

- 用户意图：确认当前版本能否记录每次对话，并经过合适流程沉淀到 memory；进一步确认 memory 是否会自动从 log 抽取信息更新各层记忆。
- 主题：
  1. 多轮对话与 memory 的沉淀边界。
  2. `log -> memory` 是否自动同步。
- 关键动作：
  1. 明确当前体系可以记录对话过程，但长期沉淀只接受被提炼后的稳定背景、规则和项目记忆，不保留逐字聊天全文。
  2. 明确 `log` 只承担过程记录与时间线，不会自动驱动各层 memory 更新；从 `log` 到 `BRAIN`、`POLICY`、`projects/memory` 的迁移需要先判断晋升条件，再回写。
  3. 把“可以从对话里提炼稳定信息沉淀到 memory”与“自动全文抽取并同步”区分开，避免把 `log` 误解为自动同步源。
- 影响页面：[[log]]、[[BRAIN]]、[[POLICY]]、[[projects/memory/README]]。

### 收紧内部页面引用格式并修正 wikilink 渲染与 README 首章结构

- 用户意图：把 Markdown 内部页面引用收紧成真正可执行的硬约束，并修掉规则页和入口页里那些“看起来像链接但实际上不能点”的写法；同时把 README 第一章节里目录层和根目录页面混排的问题整理成统一格式。
- 主题：
  1. 强化内部页面引用格式约束。
  2. 修正 wikilink 被代码化或写成裸文件名导致的渲染问题。
  3. 统一 README 首章的目录层与根目录页面表达。
- 关键动作：
  1. 在 [[AGENTS]]、[[WORKFLOW]] 和 [[POLICY]] 中补强内部页面引用规则，明确本库页面、入口页、模板页和跳转目标必须使用 `[[wikilink]]`，禁止保留内部 `.md` 链接、本机绝对路径、空链接、占位链接和裸文件名。
  2. 补充一条更细的执行约束：如果语义上是在引用本库页面，就不能把 `[[wikilink]]` 再包进反引号；只有把 `[[wikilink]]` 当作语法示例时，才允许保留代码样式。
  3. 修正 [[POLICY]]、[[BRAIN]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/policy-links]]、[[projects/memory/shared]] 和 [[projects/requirements]] 中被反引号包住、导致不渲染的 wikilink，以及写成裸文件名的内部页面引用。
  4. 回看主 [[README]] 的入口说明，把“页面入口”统一改成可点击的 `[[wikilink]]`，让 [[WORKFLOW]]、[[AGENTS]]、[[INDEX]]、[[log]] 等入口的表现与 [[BRAIN]]、[[POLICY]]、[[projects/memory/README]] 保持一致。
  5. 继续收口 [[README]] 第一章节，把“目录层”和“根目录页面”拆成两组，避免在同一列表里混写目录与页面入口，造成格式和语义不统一。
- 影响页面：[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]、[[README]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/policy-links]]、[[projects/memory/shared]]、[[projects/requirements]]。

### 把项目运行层收口到更清晰的状态与功能点模型

- 用户意图：在前一天已经完成首轮 memory 分层的基础上，把“最小改造方案”剩余缺口补齐，让项目状态、功能点推进、角色分层和运行层入口的口径一致，减少“进行中”这类模糊状态在不同页面里互相污染。
- 主题：
  1. 补齐分层 memory 最小改造方案的剩余部分。
  2. 对齐项目状态、功能点推进和角色分层的口径。
  3. 继续收紧运行层入口、规则桥接和写作边界。
- 关键动作：
  1. 对齐最小改造方案的剩余缺口，保留并恢复 `projects/design/memory/` 作为研究层，新增 `projects/status.md` 作为项目状态页，并把“研究层 / 运行层”拆分正式落地到项目结构中。
  2. 给项目主页、需求页、设计入口、决策页、发布页、开发入口、共享记忆页等核心页面补齐可机读的 frontmatter，让 agent 后续可以读 `type / id / status / stage / source_of_truth` 这类字段，而不只是读正文。
  3. 强化 [[POLICY]]，明确默认不自动晋升、晋升条件、只有拍板后才进入 policy，以及冲突不直接覆盖的固定流程。
  4. 在 `projects/memory/` 增加 `policy-links.md` 作为运行层到规则层的桥接页，并同步更新 [[projects/README]]、[[projects/STRUCTURE]] 和 [[README]] 的入口说明。
  5. 强化 Markdown 引用约束，统一 vault 内页面引用必须使用 `[[wikilink]]` 及其变体，禁止继续保留内部 `.md` 链接、本机绝对路径、空链接和占位链接，并把引用校验加入 [[WORKFLOW]] 的交付前必检项。
  6. 把功能点推进流程正式沉淀到项目层，[[WORKFLOW]] 补了功能点状态机，[[projects/development/README]] 和 [[projects/development/execution/worklog]] 补了模板与示例，[[projects/status]] 变成全局状态镜像，`projects/memory/`、[[projects/decisions]] 和 [[projects/README]] 也同步收口了对应入口。
  7. 把开发示例独立成 `projects/development/examples.md`，并把 [[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/STRUCTURE]]、[[projects/README]] 和 [[WORKFLOW]] 的示例入口同步改为指向该文件。
  8. 把功能点管理从单字段 `in_progress` 改成双轴模型，由 `status` 管生命周期、`phase` 管串联步骤；同时把开发入口、示例页、工作日志、状态页、决策页和项目记忆页都同步沉淀，避免设计、实现、验证混写在一个字段里。
  9. 进一步把项目级状态和功能点双轴分开，让项目入口只保留项目级状态词，功能点推进统一用 `status + phase`，避免不同层级的“进行中”概念互相污染。
  10. 明确功能点卡的最小填写要求，每张卡都必须同时写 `status` 和 `phase`，不能只留一个“进行中”的笼统字段；并把这条约束写进项目共享背景。
  11. 把过程记录也同步拆轴，让 [[projects/development/execution/worklog]] 分开记录 `status` 变化和 `phase` 变化，避免把两条线重新揉回 `in_progress`。
  12. 把开发示例进一步显式化，同时展示进行中、完成待发布、已发布三种卡片，并把已发布示例的阶段口径收口到 `release`。
  13. 把开发示例从“同页多卡”进一步拆成真实功能点实体页，新增 `projects/development/feature-points/` 目录，拆出 `README.md` 索引页和 `FP-001.md`、`FP-002.md`、`FP-003.md` 三个实体页；同时把 [[WORKFLOW]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/decisions]]、[[projects/memory/shared]] 和 [[AGENTS]] 的口径一起改成实体页优先。
  14. 进一步把 [[projects/development/README]] 收成研发经理看板，移走状态轴、阶段轴、实体模板和当前实体清单；把这些执行细节集中到 [[projects/development/feature-points/README]]，让开发主入口只负责整体推进、阻塞、下一步和协调。
  15. 把目录入口标题统一收成中文，并补了一条写作约定：正文默认中文，英文只保留文件名、产品名、代码标识和必要术语；继续把说明性英文收口为中文表达，不动历史事实记录。
  16. 把随意中英混排正式沉淀为 [[AGENTS]] 的硬约束，延续同一天前面的正文中文化收口，把规则明确成后续新增或修改内容都要检查的维护约束。
- 影响页面：[[projects/status]]、[[projects/memory/README]]、[[projects/memory/policy-links]]、[[projects/design/memory/README]]、[[projects/development/README]]、[[projects/development/execution/worklog]]、[[projects/development/feature-points/README]]、[[projects/README]]、[[projects/STRUCTURE]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]、[[AGENTS]]。

## 2026-04-09

### 把文档库从“文件集合”收口成有上下文模型和 memory 分层的系统

- 用户意图：在不推翻现有骨架的前提下，把这套库从“可用的文档系统”进一步收口成未来可自动运行的文档操作系统；后续更新不再只盯着当前文件，而是先判断模式、阶段、主入口、上下游和受影响页面，并把规则、背景、项目记忆分层放稳。
- 主题：
  1. 建立全局背景优先、上下文模型和结构变更同步规则。
  2. 把 memory 路由拆成共享背景、规则层和项目记忆三层。
  3. 用最小改造而非重构的方式，给后续 agent 自动化预留机器可读入口。
- 关键动作：
  1. 增加“全局背景优先”规则，要求更新任何内容时，不只看当前文件，还要先判断它在整个 vault 中的模式、阶段、主入口、影响范围和知识层级。
  2. 将“上下文”进一步定义为主入口、上下游文件、阶段位置、知识层级和受影响页面的组合，并为项目页、需求、设计、决策、知识页、索引页分别补入最小读取集与演进链路。
  3. 增加“结构变更同步”规则，以后只要新增模块、目录、模板、入口页或新的高频文件类型，就必须在同一次变更里同步更新上下文模型、关联关系、最小读取集和日志。
  4. 收紧提交和规则治理，明确 commit 只针对实际内容或结构变更；本地状态和缓存不进正式提交；新增规则时优先修改旧规则，避免继续把系统写重。
  5. 收紧 [[projects/README]] 的表达方式，保留项目运行层定义，不再显式强调是否已进入正式项目阶段，让内容本身决定页面所处状态。
  6. 收口研发阶段说明，把阶段映射、推进方法和从零做系统的详细说明统一收回 [[WORKFLOW]]，让 [[README]] 和 [[projects/README]] 只保留摘要和跳转，避免重复维护。
  7. 清理文档中的本机绝对路径，让仓库内链接统一改为相对路径，环境说明改为“当前工作区 / 当前 vault”，避免换电脑后链接失效。
  8. 增加链接约束，要求同一 vault 内的页面跳转默认使用 `[[wikilink]]`，外部资源继续使用 Markdown 链接，长期文档禁止写死本机绝对路径。
  9. 增加“AI 功能研发工作流”，在 [[WORKFLOW]] 中补入功能从需求到上线的最小闭环，以及“什么时候补文档、什么时候直接写代码”的判断标准。
  10. 将项目层的结构说明单独抽到 [[projects/STRUCTURE]]，把目录、文件职责、依赖关系和默认读取顺序收口成一个主页面，避免继续把结构和流程堆在同一页。
  11. 明确项目层的目录规则，要求现有内容优先保留；已经形成多文件职责的模块继续保留目录；只有一个 `README.md` 的子目录才优先收平成单文件。
  12. 澄清设计层口径，让 `design/README.md` 成为设计主入口，`architecture.md`、`database.md` 成为设计子页，而不是并列的第二份“设计”。
  13. 按统一规则实际创建项目层文件：`requirements.md`、`design/README.md`、`design/architecture.md`、`design/database.md`、`decisions.md`、`development/README.md`、`development/worklog.md`、`releases.md`、`incidents.md`。
  14. 将事故层调整为目录结构，让 `incidents/README.md` 负责总览和整体状态，每一次事故单独成文件，避免把多次事故堆在同一页。
  15. 为设计层补出显式的技术选型文件 `design/tech-selection.md`，避免把技术选型长期埋在设计总览里。
  16. 引入 [[BRAIN]] 作为共享脑，承接跨多轮确认、后续应自动进入思考背景的内容；同时明确 [[AGENTS]]、`workspace-memory`、[[projects/decisions]]、[[log]] 的分工。
  17. 将“分层 memory 研究”先沉淀到项目设计层，新增 `design/memory/README.md` 和 `design/memory/tools.md`，随后又调整其落点，把这部分研究迁移到 `articles/` 和 `concepts/`，并清理 `projects/design/memory/` 空目录。
  18. 将 Obsidian 软件开发文档系统的整体设计沉淀到知识库层，新增 [[articles/2026-04-09-obsidian-doc-system-design]] 和 [[concepts/document-os]]，用于承接整体架构、无账号小团队约束、半自动到自动化路径，以及未来分层 memory 的文档化路线。
  19. 明确采用“最小改造方案”而不是整体重构：保留根层、项目层、知识层和输入层的现有骨架，不把系统推倒重来，而是在既有结构上补出更清晰的职责边界。
  20. 正式把 memory 路由分层，新增 [[POLICY]] 承接规则和优先级，新增 `projects/memory/` 承接项目级稳定记忆，收紧 [[BRAIN]] 只保留共享背景，并同步更新 [[README]]、[[INDEX]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]]、项目主页面、模板页、相关文章和概念页；同时确认 `log` 只保留过程记录，不会自动抽取并同步各层 memory，后续沉淀要先从 `log` / 对话中提炼再回写。
  21. 明确后续自动化真正依赖的是结构化字段而不只是目录名，因此开始把项目主页、需求页、设计入口、决策页、共享记忆页等核心页面补向可机读的 frontmatter 口径，为下一天继续补齐最小改造方案做准备。
- 影响页面：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]]、[[projects/README]]、[[BRAIN]]、[[POLICY]]、[[projects/memory/README]]、[[articles/2026-04-09-obsidian-doc-system-design]]、[[concepts/document-os]]。

## 2026-04-08

### 搭建 `wiki` 文档库底座并补齐最小维护流程

- 用户意图：先把这套库从零搭起来，让资料有入口、有层次、有维护动作，后续不管是知识沉淀还是研发推进都有可落脚的主结构。
- 主题：
  1. 初始化文档库底座和目录层级。
  2. 补齐从入口到流程的最小维护规则。
- 关键动作：
  1. 初始化 `wiki` vault。
  2. 配置 `Obsidian`、`Codex CLI`、`workspace-filesystem`、`workspace-memory`。
  3. 建立 [[README]]、[[WORKFLOW]]、`templates/`、`articles/`、`concepts/`、`indexes/`。
  4. 把后续维护改成 `raw/ -> articles/concepts/indexes -> log.md` 的持续编译流程。
  5. 补充文件与目录操作流程，包括新建目录、新建文件、修改文件、处理已有目录。
  6. 将“新目录 / 新文件 / 修改文件 / 目录复用 / 链接影响 / 记录日志”等关键判断前置到 [[README]] 和 [[INDEX]]，避免总入口过于隐蔽。
  7. 在总入口补充“怎么用这个 vault / 先看什么 / 常见操作对应关系 / 可直接复制的指令模板”，让 [[README]] 真正承担使用说明。
  8. 进一步明确 `raw/` 与 `inbox/` 的边界，补入 `assets/` 与 `archive/` 的生命周期规则，并把 `workspace-memory` 限定为稳定偏好而不是唯一规则源。
  9. 清理根目录两个空的 `canvas` 占位文件，改用 `assets/` 作为支持性可视化文件落点。
  10. 增加 `projects/` 作为活跃软件研发项目层，明确知识库模式是底座、研发模式是叠加层，并补出项目模板与项目运行说明。
  11. 为 `projects/` 补入手动流控、项目主页优先和活跃项目汇总入口的约定。
  12. 进一步收紧为极简小项目模式，默认一页项目主页加总日志，其他项目文件按需添加，不预建空结构。
  13. 把新建目录规则进一步改成“README 先行，模板和索引按需创建”，避免极简模式被默认的重结构约束反向拉重。
  14. 进一步把模板定位为加速器而非门槛，让项目主页可以直接手写，不必先复制模板。
  15. 把“研发推进的关键原则”单独沉淀到 [[projects/README]] 和 [[WORKFLOW]]，强调项目主页、代码仓库、问题定义、过程记录和知识回写这几条最重要的研发约束。
  16. 明确当前建模前提：一个 `wiki` 只对应一个项目，因此项目主页固定为 [[projects/README]]，不再采用 `projects/<项目名>/` 的多项目结构。
  17. 为 `projects/` 层补充“相关文件分别做什么”的说明，明确每个可选文件的职责、拆分时机和不拆分时机。
  18. 提升会话级更新规则，要求复杂问题拆成中间节点推进并分段提交；同类信息只保留一个主入口，禁止多处复制粘贴；修改前后都要按入口、主页面、相关跳转页的顺序读取和回看。
- 影响页面：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[projects/README]]、[[log]]、`templates/`、`articles/`、`concepts/`、`indexes/`。
