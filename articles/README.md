# 摘要卡片层

这里放每篇材料的一张摘要卡片。

## 建议命名

- `YYYY-MM-DD-标题.md`

## 每页建议包含

- 来源
- 一句话总结
- 关键观点
- 相关工具
- 关联概念
- 待办或后续动作

## 维护原则

- 尽量只写一次摘要，不重复抄原文。
- 如果文章涉及很多工具，优先加链接，不要堆长段解释。
- 新增或大改摘要卡片时，按 [[knowledge-linking-rules]] 同步相关概念、入口回链和必要的案例 / 上位页承接，并运行 `python3 scripts/check_all.py --only knowledge-linking`。

## 信息架构 / 知识呈现

- [[articles/2026-06-10-color-aesthetic-system-research]]：配色与审美体系调研，把颜色从“好看”校准为信息层级、行动语义、状态语义、品牌气质、数据编码和可访问性共同组成的视觉系统。
- [[articles/2026-06-09-technology-research-capability-system]]：技术调研能力体系补全，说明技术调研需要先做对象路由，再按证据等级、成熟度、经济性、安全合规、AI 评测和更新机制形成可持续研究能力。
- [[articles/2026-06-09-technical-topic-research-methodology]]：技术专题调研方法论，说明技术类专题 / 概念调研的目标不是搜全资料，而是形成支撑判断、选型、PoC、风险识别和复用的技术研究型知识资产。
- [[articles/2026-06-09-open-source-project-due-diligence-methodology]]：开源工程调研方法论，说明具体开源仓库调研应按项目画像、健康度、跑通验证、代码结构、效果性能、集成成本、风险和使用策略形成工程尽调资产。
- [[articles/2026-06-09-it-ai-industry-research-methodology]]：IT / AI 行业调研方法论，说明行业和 AI 领域调研应按宏观趋势、技术路线、产品应用、公司竞争、开源生态和落地治理形成机会与行动判断。
- [[articles/2026-06-08-image-text-layout-system-research]]：图片与图文排版体系调研，从现代主义排版、瑞士网格、Gestalt、Material / Carbon、CSS Grid、响应式图片、可访问图注和 AI layout generation 中抽象出意图、素材、空间骨架、视觉组织、图文绑定、媒介适配和治理生成七层模型。
- [[articles/2026-06-05-ai-era-information-presentation-research]]：AI 时代信息记录、处理与呈现方式调研，梳理文件记录、chunk / vector 处理、Markdown 记录 + 处理、页面化 lens、HTML 实时呈现、同源导出和 HTML 记录边界。
- [[articles/2026-06-05-problem-focused-information-presentation-cross-project-calibration]]：用 Life、DocCustomeranalysis、prefect、fetch-adapter 和 DocFilmCommunity 只读样本校准问题聚焦式图文 lens 的 current / snapshot、源刷新、背景框、用户入口、同源导出和重复渲染物边界。
- [[articles/2026-06-04-knowledge-linking-mechanism-research]]：新增知识关联机制调研，校准 Obsidian 图谱、Evergreen notes 和 Zettelkasten 方法论，说明本库采用“agent 语义判断 + sensor 结构检查”的知识网络机制。

## Agent / Harness 案例

- [[articles/2026-06-12-codex-goal-mode-public-guide]]：可对外发布的 Codex Goal 模式使用教程，独立说明适用场景、命令、Goal Contract 写法、示例、运行管理和误用边界。
- [[articles/2026-06-12-codex-goal-mode-usage-guide]]：Codex Goal 模式使用教程，从历史 Goal Contract、主控 / 子工程协作和自动续跑漏 `log.md` 案例中提炼何时用、怎么写、怎么迭代和怎么收尾。
- [[articles/2026-06-09-scientific-agent-skills-research]]：Scientific Agent Skills 调研，说明科研 Agent Skill 库的价值在于把工具链、数据库、实验流程、方法规范和输出模板变成 agent 可加载的流程资产，并提醒不要无脑全装 community skill。
- [[articles/2026-06-02-issue-original-evidence-asset-intake]]：Issue 原始图片证据未入库案例，分析模型可见图片与本地证据资产之间的断层，并提出高效的证据资产门方案。
- [[articles/2026-05-29-finalizer-write-scope-case]]：finalizer 写入范围失守案例，分析 clean proof 与 scope proof 混淆的问题。

## 企业 / 产品调研

- [[articles/2026-06-09-xinzhi-ruisheng-company-research]]：芯智睿声企业调研，把北京芯智睿声科技有限公司校准为 AI + 柔性传感 + 可穿戴智能人工喉的早期辅助科技企业，并标出医疗器械注册、临床验证、数据隐私和商业化阶段的待核验边界。
