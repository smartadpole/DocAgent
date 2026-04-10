# 活动记录

> append-only

## 2026-04-08

- 初始化 `wiki` vault。
- 配置 `Obsidian`、`Codex CLI`、`workspace-filesystem`、`workspace-memory`。
- 建立 `README.md`、`WORKFLOW.md`、`templates/`、`articles/`、`concepts/`、`indexes/`。
- 后续维护改为 `raw/ -> articles/concepts/indexes -> log.md` 的持续编译流程。
- 补充文件与目录操作流程：新建目录、新建文件、修改文件、处理已有目录。
- 将“新目录 / 新文件 / 修改文件 / 目录复用 / 链接影响 / 记录日志”等关键判断前置到 `README.md` 和 `INDEX.md`，避免总入口过于隐蔽。
- 在总入口补充了“怎么用这个 vault / 先看什么 / 常见操作对应关系 / 可直接复制的指令模板”，让 README 真正承担使用说明。
- 进一步明确 `raw/` 与 `inbox/` 的边界，补入 `assets/` 与 `archive/` 的生命周期规则，并把 `workspace-memory` 限定为稳定偏好而不是唯一规则源。
- 清理了根目录两个空的 `canvas` 占位文件，改用 `assets/` 作为支持性可视化文件落点。
- 增加 `projects/` 作为活跃软件研发项目层，明确知识库模式是底座、研发模式是叠加层，并补了项目模板与项目运行说明。
- 为 `projects/` 补了手动流控、项目主页优先和活跃项目汇总入口的约定。
- 进一步收紧为极简小项目模式：默认一页项目主页 + 总日志，其他项目文件按需添加，不预建空结构。
- 把新建目录规则进一步改成“README 先行，模板和索引按需创建”，避免极简模式被默认的重结构约束反向拉重。
- 进一步把模板定位为加速器而非门槛：项目主页可以直接手写，不必先复制模板。
- 把“研发推进的关键原则”单独沉淀到 `projects/README.md` 和 `WORKFLOW.md`，强调项目主页、代码仓库、问题定义、过程记录和知识回写这几条最重要的研发约束。
- 明确当前建模前提：一个 `wiki` 只对应一个项目，因此项目主页固定为 `projects/README.md`，不再采用 `projects/<项目名>/` 的多项目结构。
- 为 `projects/` 层补充“相关文件分别做什么”的说明，明确每个可选文件的职责、拆分时机和不拆分时机。
- 提升会话级更新规则：复杂问题要拆成中间节点推进并分段提交；同类信息只保留一个主入口，禁止多处复制粘贴；修改前后都要按入口、主页面、相关跳转页的顺序读取和回看。

## 2026-04-09

- 增加“全局背景优先”规则：更新任何内容时，不只看当前文件，还要先判断它在整个 vault 中的模式、阶段、主入口、影响范围和知识层级。
- 将“上下文”进一步定义为主入口、上下游文件、阶段位置、知识层级和受影响页面的组合，并为项目页、需求、设计、决策、知识页、索引页分别补入最小读取集与演进链路。
- 增加“结构变更同步”规则：以后只要新增模块、目录、模板、入口页或新的高频文件类型，就必须在同一次变更里同步更新上下文模型、关联关系、最小读取集和日志。
- 收紧提交和规则治理：commit 只针对实际内容或结构变更；本地状态和缓存不进正式提交；新增规则时优先修改旧规则，避免继续把系统写重。
- 收紧 `projects/README.md` 的表达方式：保留项目运行层定义，不再显式强调是否已进入正式项目阶段，让内容本身决定页面所处状态。
- 收口研发阶段说明：把阶段映射、推进方法和从零做系统的详细说明统一收回 `WORKFLOW.md`，`README.md` 和 `projects/README.md` 只保留摘要和跳转，避免重复维护。
- 清理文档中的本机绝对路径：仓库内链接统一改为相对路径，环境说明改为“当前工作区/当前 vault”，避免换电脑后链接失效。
- 增加链接约束：同一 vault 内的页面跳转默认使用 `[[wikilink]]`，外部资源继续使用 Markdown 链接，长期文档禁止写死本机绝对路径。
- 增加“AI 功能研发工作流”：在 `WORKFLOW.md` 中补入功能从需求到上线的最小闭环，以及“什么时候补文档、什么时候直接写代码”的判断标准。
- 将项目层的结构说明单独抽到 `projects/STRUCTURE.md`，把目录、文件职责、依赖关系和默认读取顺序收口成一个主页面，避免继续把结构和流程堆在同一页。
- 明确项目层的目录规则：现有内容优先保留；已经形成多文件职责的模块继续保留目录；只有一个 `README.md` 的子目录才优先收平成单文件。
- 澄清设计层口径：`design/README.md` 是设计主入口，`architecture.md`、`database.md` 是设计子页，不是并列的第二份“设计”。
- 按统一规则实际创建项目层文件：`requirements.md`、`design/README.md`、`design/architecture.md`、`design/database.md`、`decisions.md`、`development/README.md`、`development/worklog.md`、`releases.md`、`incidents.md`。
- 将事故层调整为目录结构：`incidents/README.md` 负责总览和整体状态，每一次事故单独成文件，避免把多次事故堆在同一页。
- 为设计层补出显式的技术选型文件：`design/tech-selection.md`，避免把技术选型长期埋在设计总览里。
- 引入 `BRAIN.md` 作为共享脑：承接跨多轮确认、后续应自动进入思考背景的内容；同时明确 `AGENTS.md`、`workspace-memory`、`projects/decisions.md`、`log.md` 的分工。
- 将“分层 memory 研究”沉淀到项目设计层：新增 `design/memory/README.md` 和 `design/memory/tools.md`，分别承接分层设计稿和开源工具调研。
- 调整“分层 memory 研究”的落点：它属于知识库调研而不是当前项目设计，因此迁移到 `articles/` 和 `concepts/`，并从项目设计入口移除。
- 清理 `projects/design/memory/` 空目录：研究内容已迁回知识库层，项目层不再保留无职责的空壳目录。
- 将 Obsidian 软件开发文档系统的整体设计沉淀到知识库层：新增 `articles/2026-04-09-obsidian-doc-system-design.md` 和 `concepts/document-os.md`，用于承接整体架构、无账号小团队约束、半自动到自动化路径，以及未来分层 memory 的文档化路线。
- 这次把 memory 路由正式分层：新增 `POLICY.md` 承接规则和优先级，新增 `projects/memory/` 承接项目级稳定记忆，收紧 `BRAIN.md` 只保留共享背景，并同步更新 `README.md`、`INDEX.md`、`WORKFLOW.md`、`AGENTS.md`、`projects/STRUCTURE.md`、项目主页面、模板页、相关文章和概念页。

## 2026-04-10

- 对齐最小改造方案的剩余缺口：保留并恢复 `projects/design/memory/` 作为研究层，新增 `projects/status.md` 作为项目状态页，并为其补充可读字段。
- 强化 `POLICY.md`：明确默认不自动晋升、晋升条件、只有拍板后才进入 policy、以及冲突不直接覆盖的固定流程。
- 在 `projects/memory/` 增加 `policy-links.md` 作为运行层到规则层的桥接页，并同步更新 `projects/README.md`、`projects/STRUCTURE.md` 和 `README.md` 的入口说明。
- 强化 Markdown 引用约束：统一 vault 内页面引用必须使用 `[[wikilink]]` 及其变体，禁止继续保留内部 `.md` 链接、本机绝对路径、空链接和占位链接，并把引用校验加入 `WORKFLOW.md` 的交付前必检项。
- 把功能点推进流程正式沉淀到项目层：`WORKFLOW.md` 补了功能点状态机，`projects/development/README.md` 和 `projects/development/worklog.md` 补了模板与示例，`projects/status.md` 变成全局状态镜像，`projects/memory/`、`projects/decisions.md` 和 `projects/README.md` 也同步收口了对应入口。
- 把开发示例独立成文件：新增 `projects/development/examples.md`，并把 `projects/development/README.md`、`projects/development/worklog.md`、`projects/STRUCTURE.md`、`projects/README.md` 和 `WORKFLOW.md` 的示例入口同步改为指向该文件。
- 把功能点管理从单字段 `in_progress` 改成双轴模型：`status` 管生命周期，`phase` 管串联步骤；同时把开发入口、示例页、工作日志、状态页、决策页和项目记忆页都同步沉淀，避免设计、实现、验证混写在一个字段里。
- 进一步把项目级状态和功能点双轴分开：项目入口只保留项目级状态词，功能点推进统一用 `status + phase`，避免不同层级的“进行中”概念互相污染。
- 明确功能点卡的最小填写要求：每张卡都必须同时写 `status` 和 `phase`，不能只留一个“进行中”的笼统字段。
- 把“功能点卡必须同时写 `status` 和 `phase`”写进项目共享背景，后续读入口、模板或示例时都默认按双轴模型理解。
- 把过程记录也同步拆轴：`projects/development/worklog.md` 现在要求分开记录 `status` 变化和 `phase` 变化，避免把两条线重新揉回 `in_progress`。
- 把开发示例进一步显式化：`projects/development/examples.md` 现在同时展示进行中、完成待发布、已发布三种卡片，让 `status` 和 `phase` 的区别一眼可见。
- 把已发布示例的阶段口径收口到 `release`，避免 `released` 功能点还挂着 `verification` 阶段造成误读。
- 把开发示例从“同页多卡”进一步拆成真实功能点实体页：新增 `projects/development/feature-points/` 目录，拆出 `README.md` 索引页和 `FP-001.md` / `FP-002.md` / `FP-003.md` 三个实体页；同时把 `WORKFLOW.md`、`projects/README.md`、`projects/STRUCTURE.md`、`projects/status.md`、`projects/development/README.md`、`projects/development/worklog.md`、`projects/decisions.md`、`projects/memory/shared.md` 和 `AGENTS.md` 的口径一起改成实体页优先。
- 进一步把 `projects/development/README.md` 收成研发经理看板，移走状态轴、阶段轴、实体模板和当前实体清单；把这些执行细节集中到 `projects/development/feature-points/README.md`，让开发主入口只负责整体推进、阻塞、下一步和协调。
- 这次把目录入口标题统一收成中文，并补了一条写作约定：正文默认中文，英文只保留文件名、产品名、代码标识和必要术语；保留技术专名，但降低入口层的混排感。
