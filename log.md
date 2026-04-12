# 活动记录

> 历史不重写；新记录按时间降序插在前面，并按日期下的对话组织。

## 记录原则

- `[[log]]` 记录的是每次对话在解决什么主题，不是对话逐句转录。
- 记录单位是“每次对话”，不是“每个问题”，也不是“每天只写一个主题”。
- 一次对话至少有一个主题；如果存在多个紧密相关主题，可以合并在同一条对话记录里。
- 记录用户提问时，先提炼用户意图，再记录对应动作和影响。
- 同一轮里多个细碎问题，如果服务同一主题或同一组相关主题，合并成一条记录。
- 关键动作要保留足够完整，不能只剩过度压缩的摘要。
- 每条记录优先回答四件事：主题、用户意图、关键动作、受影响页面。
- 默认条目模板见 `templates/log-entry-template.md`。

## 推荐模板

```md
## YYYY-MM-DD

### 对话：一句话概括这次对话

- 用户意图：这轮真正想解决什么问题，为什么现在要解决。
- 主题：
  1. 主题 A
  2. 主题 B（可选；如果没有就删掉）
- 关键动作：
  1. 这次实际做了什么关键调整、整理或决策。
  2. 如果动作很多，继续补，不要为了简短丢掉关键信息。
- 影响页面：列出被更新的主页面。
```

## 2026-04-12

### 对话：把中英文混排问题沉淀为 `AGENTS` 硬约束

- 用户意图：把已经确认的中英文混排问题正式沉淀成 agent 必须遵守的硬约束，避免后续继续出现。
- 主题：
  1. 将写作约定从“收口”升级为“必须遵守”。
  2. 让规则落点留在 `AGENTS.md`，而不是只停留在临时说明里。
- 关键动作：
  1. 把 `AGENTS.md` 的写作规则改成正文默认中文，除必要专名外不得混排。
  2. 承接 2026-04-10 的正文中文化收口，把这条约束正式升级为硬规则；同时继续把说明性英文收口为中文表达，并把这条约束写进历史记录，方便后续回看它是怎么形成的。
- 影响页面：[[AGENTS]]、[[log]]。

### 对话：回填历史 log 的日期与整合

- 用户意图：按新的 log 规则把历史回填写到当时提问的日期中，而不是留在当前回填动作的日期里。
- 主题：
  1. 把前几轮关于角色、memory 关系和框架级说明落层的内容，回填到实际提问日期。
  2. 把之前日期里已经出现过的相关信息做整合，避免重复和错位。
- 关键动作：
  1. 回看 2026-04-10 和 2026-04-11 中和本话题相关的记录，准备把初次讨论、落层调整和最终边界分别放回对应日期，并把重复信息合并整理。
- 影响页面：[[log]]。

## 2026-04-11

### 对话：修正 `[[log]]` 的记录粒度和动作完整度

- 用户意图：让 `[[log]]` 既能提炼用户真正想解决的问题，又不要因为过度摘要而丢掉关键改动；同时明确每次对话都要有一个主题或多个主题，只是不必把每个问题拆开单记。
- 主题：
  1. 把 `[[log]]` 的记录单位从“按天压成一个主题”改成“按对话记录”。
  2. 恢复 `[[log]]` 历史条目中过度压缩的修改动作细节。
- 关键动作：
  1. 重写 `[[log]]`、[[WORKFLOW]]、[[POLICY]]、[[AGENTS]]、[[README]]、[[INDEX]]、[[BRAIN]] 和模板文件中关于 `[[log]]` 的定义，明确记录单位是“每次对话”，同一天可以有多条记录，一次对话可以包含一个或多个相关主题。
  2. 补充 `[[log]]` 和 `templates/log-entry-template.md` 的条目骨架，把“对话”“主题”“用户意图”“关键动作”“影响页面”固定成默认结构。
  3. 回填历史条目时恢复更完整的动作列表，避免只剩笼统摘要。
- 影响页面：[[log]]、[[WORKFLOW]]、[[POLICY]]、[[AGENTS]]、[[README]]、[[INDEX]]、[[BRAIN]]、`templates/log-entry-template.md`。

### 对话：重构 `[[log]]` 的记录模型

- 用户意图：让 `[[log]]` 不再只记“改了什么”，而是能回看用户这轮真正想解决的问题；记录顺序改为时间降序；提问内容按主题提炼，不机械抄写所有问句。
- 主题：
  1. 让 `[[log]]` 从动作流水改成带用户意图的主题化记录。
- 关键动作：
  1. 重写 `[[log]]` 的说明和历史条目结构，把记录口径收成“主题 + 用户意图 + 关键动作 + 受影响页面”。
  2. 同步更新 [[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/README]] 对 `[[log]]` 的职责描述。
  3. 新增 `templates/log-entry-template.md`，并在 [[log]] 与 [[WORKFLOW]] 中补入推荐骨架，方便后续直接套用。
- 影响页面：[[log]]、[[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/README]]、`templates/log-entry-template.md`。

### 对话：把角色和 memory 的说明上提到根入口

- 用户意图：纠正角色 / memory 说明的位置，把框架级解释放在最外层，而不是项目层。
- 主题：
  1. 角色分层和 memory 分层的关系。
  2. 框架级说明的最终落点。
- 关键动作：
  1. 先在项目层尝试承接 role / memory 说明，随后把解释性内容从 `projects/memory/` 和 `projects/design/memory/` 中移出，最终放到根 `README.md`。
  2. 同时在 `BRAIN.md` 和 `POLICY.md` 增加边界说明，让框架级说明、共享背景和规则层各自归位。
  3. 让 `projects/design/memory/README.md` 只保留研究入口，不再承接框架正文。
  4. 把 2026-04-10 的初次讨论和这次最终纠正合并成连续历史，不重复记两套正文。
- 影响页面：[[README]]、[[BRAIN]]、[[POLICY]]、[[projects/design/memory/README]]。

## 2026-04-10

### 对话：把项目运行层收口到更清晰的状态与功能点模型

- 用户意图：让项目状态、功能点推进、角色分层和运行层入口的口径一致，减少“进行中”这类模糊状态在不同页面里互相污染。
- 主题：
  1. 对齐项目状态、功能点推进和角色分层的口径。
  2. 继续收紧运行层入口、规则桥接和写作边界。
- 关键动作：
  1. 对齐最小改造方案的剩余缺口，保留并恢复 `projects/design/memory/` 作为研究层，新增 `projects/status.md` 作为项目状态页，并为其补充可读字段。
  2. 强化 [[POLICY]]，明确默认不自动晋升、晋升条件、只有拍板后才进入 policy，以及冲突不直接覆盖的固定流程。
  3. 在 `projects/memory/` 增加 `policy-links.md` 作为运行层到规则层的桥接页，并同步更新 [[projects/README]]、[[projects/STRUCTURE]] 和 [[README]] 的入口说明。
  4. 强化 Markdown 引用约束，统一 vault 内页面引用必须使用 `[[wikilink]]` 及其变体，禁止继续保留内部 `.md` 链接、本机绝对路径、空链接和占位链接，并把引用校验加入 [[WORKFLOW]] 的交付前必检项。
  5. 把功能点推进流程正式沉淀到项目层，[[WORKFLOW]] 补了功能点状态机，[[projects/development/README]] 和 [[projects/development/worklog]] 补了模板与示例，[[projects/status]] 变成全局状态镜像，`projects/memory/`、[[projects/decisions]] 和 [[projects/README]] 也同步收口了对应入口。
  6. 把开发示例独立成 `projects/development/examples.md`，并把 [[projects/development/README]]、[[projects/development/worklog]]、[[projects/STRUCTURE]]、[[projects/README]] 和 [[WORKFLOW]] 的示例入口同步改为指向该文件。
  7. 把功能点管理从单字段 `in_progress` 改成双轴模型，由 `status` 管生命周期、`phase` 管串联步骤；同时把开发入口、示例页、工作日志、状态页、决策页和项目记忆页都同步沉淀，避免设计、实现、验证混写在一个字段里。
  8. 进一步把项目级状态和功能点双轴分开，让项目入口只保留项目级状态词，功能点推进统一用 `status + phase`，避免不同层级的“进行中”概念互相污染。
  9. 明确功能点卡的最小填写要求，每张卡都必须同时写 `status` 和 `phase`，不能只留一个“进行中”的笼统字段；并把这条约束写进项目共享背景。
  10. 把过程记录也同步拆轴，让 [[projects/development/worklog]] 分开记录 `status` 变化和 `phase` 变化，避免把两条线重新揉回 `in_progress`。
  11. 把开发示例进一步显式化，同时展示进行中、完成待发布、已发布三种卡片，并把已发布示例的阶段口径收口到 `release`。
  12. 把开发示例从“同页多卡”进一步拆成真实功能点实体页，新增 `projects/development/feature-points/` 目录，拆出 `README.md` 索引页和 `FP-001.md`、`FP-002.md`、`FP-003.md` 三个实体页；同时把 [[WORKFLOW]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/status]]、[[projects/development/README]]、[[projects/development/worklog]]、[[projects/decisions]]、[[projects/memory/shared]] 和 [[AGENTS]] 的口径一起改成实体页优先。
  13. 进一步把 [[projects/development/README]] 收成研发经理看板，移走状态轴、阶段轴、实体模板和当前实体清单；把这些执行细节集中到 [[projects/development/feature-points/README]]，让开发主入口只负责整体推进、阻塞、下一步和协调。
  14. 把目录入口标题统一收成中文，并补了一条写作约定：正文默认中文，英文只保留文件名、产品名、代码标识和必要术语；继续把说明性英文收口为中文表达，不动历史事实记录。
- 影响页面：[[projects/status]]、[[projects/memory/README]]、[[projects/memory/policy-links]]、[[projects/development/README]]、[[projects/development/worklog]]、[[projects/development/feature-points/README]]、[[projects/README]]、[[projects/STRUCTURE]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]、[[AGENTS]]。

## 2026-04-09

### 对话：把文档库从“文件集合”收口成有上下文模型和 memory 分层的系统

- 用户意图：让后续更新不再只盯着当前文件，而是先判断模式、阶段、主入口、上下游和受影响页面，并把规则、背景、项目记忆分层放稳。
- 主题：
  1. 建立全局背景优先、上下文模型和结构变更同步规则。
  2. 把 memory 路由拆成共享背景、规则层和项目记忆三层。
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
  19. 正式把 memory 路由分层，新增 [[POLICY]] 承接规则和优先级，新增 `projects/memory/` 承接项目级稳定记忆，收紧 [[BRAIN]] 只保留共享背景，并同步更新 [[README]]、[[INDEX]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]]、项目主页面、模板页、相关文章和概念页。
- 影响页面：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]]、[[projects/README]]、[[BRAIN]]、[[POLICY]]、[[projects/memory/README]]、[[articles/2026-04-09-obsidian-doc-system-design]]、[[concepts/document-os]]。

## 2026-04-08

### 对话：搭建 `wiki` 文档库底座并补齐最小维护流程

- 用户意图：先把这套库从零搭起来，让资料有入口、有层次、有维护动作，后续不管是知识沉淀还是研发推进都有可落脚的主结构。
- 主题：
  1. 初始化文档库底座和目录层级。
  2. 补齐从入口到流程的最小维护规则。
- 关键动作：
  1. 初始化 `wiki` vault。
  2. 配置 `Obsidian`、`Codex CLI`、`workspace-filesystem`、`workspace-memory`。
  3. 建立 `README.md`、`WORKFLOW.md`、`templates/`、`articles/`、`concepts/`、`indexes/`。
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
