# 概念层

这里放概念页、工具页、方法页。

## 适合放什么

- 工具名，比如 `Claude Code`、`Codex CLI`、`Obsidian`
- 方法名，比如 `LLM 编译`、`双向链接`、`PRD 写作`
- 项目名、栏目名、固定术语

## 每页建议包含

- 定义
- 相关页面
- 常见用法
- 适用场景
- 未解决的问题

## 方法入口

- [[concepts/technical-research-knowledge-asset]]：技术研究型知识资产，把技术专题调研从资料汇总推进成能支撑判断、选型、落地、风险识别和复用的研究包。
- [[concepts/open-source-project-due-diligence]]：开源工程可用性评估，面向具体开源仓库判断能否直接用、封装用、Fork 改造、只参考实现或放弃。
- [[concepts/it-ai-industry-research-asset]]：IT / AI 行业研究资产，面向行业方向、AI 赛道、产品机会、公司群体和落地场景做产业趋势、技术路线、竞争格局、开源生态和治理风险判断。
- [[concepts/ai-era-information-presentation]]：AI 时代信息记录、处理与呈现方式，区分 Markdown 真相源、向量检索索引、超链接关系网、语义 / 动态 HTML 和 PPT / PDF / WARC / MHTML 归档格式。
- [[concepts/problem-focused-information-presentation]]：问题聚焦式信息呈现，按用户当前关注的问题为状态、计划、决策、故障、验收、知识、资源等信息类型选择合适的阅读 lens，并在需要下载、打印或分发时纳入同源 PDF / PNG 导出、A4 / A3 版式和重复渲染物入库边界。
- [[concepts/image-text-layout-system]]：图片与图文排版体系，把图片职能、图文绑定、空间骨架、视觉组织、响应式媒介、可访问语义和 AI 生成治理组织成可复用模型。
- [[concepts/prd-writing]]：PRD 写作方法
- [[concepts/project-retrospective]]：项目复盘专题，承接跨项目可复用的复盘框架；具体复盘档案看 [[projects/retrospectives/README]]
- [[concepts/software-development-project-retrospective]]：软件研发项目复盘子专题
- [[concepts/agent-work-retrospective]]：Agent 工作复盘子专题，承接 agent 的工作方式、效率、质量和 Harness 改进回看
- [[concepts/agent-governance]]：Agent 治理专题，统筹规则、路由、技能、模板、sensor、复盘和 H5 自演进
- [[concepts/agent-skills]]：Agent Skills，把高频流程、事实源、工具边界、输出格式和验证守卫打包成 agent 可发现、可加载、可执行和可审计的能力单元
- [[concepts/agent-instruction-sharing]]：Claude Code 和 Codex 共享同一份 agent 项目规则的方法，推荐根 `AGENTS.md` 作为唯一规则正文，`CLAUDE.md` 和可选 `.codex/AGENTS.md` 只做薄导入入口
- [[concepts/progressive-design-freeze]]：阶段门滚动冻结
- [[concepts/harness-engineering]]：AI Agent 的工程化运行环境方法
- [[concepts/codex-goals]]：Codex 长时任务的线程级完成契约
- [[concepts/software-testing-acceptance-release]]：软件测试、验收和上线的通用概念
- [[concepts/state-constraint-planning]]：把计划问题表示成状态变量、约束关系和可执行性判断的方法

## 工具入口

- [[concepts/openclaw]]：带 workspace memory、active memory 和 compiled knowledge layer 的 agent runtime

## 企业 / 产品入口

- [[concepts/beijing-xinzhi-ruisheng]]：北京芯智睿声科技有限公司，AI + 柔性传感 + 可穿戴智能人工喉方向的早期辅助科技企业实体页。

## 维护原则

- 同一个概念只保留一个主页面。
- 看到新文章提到这个概念，就回连到它。
- 如果某个概念开始频繁出现，再补一页，不要提前铺太多空页。
- 新增或大改概念页时，按 [[knowledge-linking-rules]] 同步入口、上位概念、邻接页面和必要反向承接，并运行 `python3 scripts/check_all.py --only knowledge-linking`。
