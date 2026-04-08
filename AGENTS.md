# AGENTS

这份文件是给 Codex 和其他 agent 的维护约束。目标不是写说明书，而是把这套 vault 持续维护成一个可演化的知识库。

## 角色分工

- `raw/`：原始资料层。优先保持原样，少改动。
- `inbox/`：临时收口区。来源还没完全处理完时先放这里。
- `assets/`：支持性附件层。图片、截图、导图、导出物和 canvas 放这里。
- `projects/`：活跃研发项目层。需求、设计、任务、决策、发布和复盘放这里。
- `articles/`：摘要卡片层。每篇材料一张主卡。
- `concepts/`：概念和实体层。工具、项目、术语都放这里。
- `indexes/`：导航层。只负责入口、分类和检索。
- `archive/`：退役和历史层。保留旧页面、合并结果和历史版本。
- `log.md`：append-only 活动记录。

## 维护规则

- 先读 `INDEX.md` 和相关页面，再决定是否新建页面。
- 优先更新已有页，不要无脑新建重复页。
- 新页面先写最小可用版本，再补链接。
- 所有重要概念都要双向链接，避免孤岛页。
- 有长期价值的结论要回写到 vault，而不是只留在对话里。
- 过程性决定和修复动作要写进 `log.md`。
- `workspace-memory` 只记稳定偏好和重复习惯，不作为唯一规则源。
- 研发项目的阶段和状态由人读项目主页手动推进，不做隐藏自动流控。
- 活跃研发项目先读项目主页，再改需求、设计、决策或运行记录。
- 极简小项目默认只保留一个项目主页，除非内容明显变多，否则不要先建空的 `requirements.md`、`design.md`、`releases.md` 之类文件。

## 会话级规则

- 复杂问题不要一次改完，先拆成几个中间节点，再逐步推进。
- 每个中间节点都要形成一个可理解、可回看、可提交的结果。
- 只要这次对话产生了实际文件变更，保底在对话结束前做一次 commit。
- 如果问题明显复杂，中间节点完成后就提交，不要把多个大变化混成一个 commit。
- commit 只包含同一主题的改动，不把无关内容打包进去。

## 单一信息源

- 同一类信息只保留一个主入口，不允许在多个页面复制粘贴同一段正文。
- 状态类信息以 `projects/README.md` 为主，其他页面引用或链接它，不重复维护第二份状态说明。
- 概念类信息以 `concepts/` 主页面为主，项目页只写与当前项目直接相关的上下文。
- 导航类信息放 `indexes/`，不要在多个说明页里重复堆导航列表。
- 需要在别处提及时，优先链接、摘一句、或写简短引用说明，不复制整段内容。

## 上下文模型

- 这里的“上下文”，不是当前文件附近几段话，而是为了正确更新目标内容，必须一起判断的最小相关信息集合。
- 每次更新都要先判断目标内容属于哪一层：证据层、项目运行层、知识沉淀层、导航层、历史层。
- 证据层是 `raw/`、`inbox/`、`assets/`，回答“信息从哪里来”。
- 项目运行层是 `projects/README.md`、`requirements.md`、`design.md`、`decisions.md`、`worklog.md`、`releases.md`、`incidents.md`，回答“当前项目正在做什么、为什么这样做、做到哪里了”。
- 知识沉淀层是 `articles/`、`concepts/`、`indexes/`，回答“哪些结论已经稳定、哪些概念可以复用、入口如何组织”。
- 历史层是 `archive/` 和 `log.md`，回答“它以前怎么演进、哪些内容已退役、这次结构调整从何时开始生效”。
- 同一段内容至少同时拥有四个属性：所属模式、所属阶段、主入口、受影响页面。

## 关联关系

- `projects/README.md` 是项目运行层主入口，连接 `requirements.md`、`design.md`、`decisions.md`、`worklog.md`、`releases.md`、`incidents.md`。
- `requirements.md` 上连项目主页，下连 `design.md` 和 `decisions.md`，外连相关 `raw/` 来源。
- `design.md` 上连项目主页和需求，横向连接 `decisions.md`，必要时连到相关 `concepts/`。
- `decisions.md` 要能回溯到需求、设计和当时约束，必要时连到 `worklog.md`、`releases.md` 或 `incidents.md`。
- `worklog.md` 连接项目主页、决策和实际推进记录，是过程上下文，不是长期知识主入口。
- `releases.md` 连接项目主页、设计、决策和验证结果；`incidents.md` 连接发布、运行现象、根因和修复动作。
- `articles/` 连接原始来源和稳定结论；`concepts/` 连接多个文章页和项目页；`indexes/` 只负责把这些主页面串起来。
- `archive/` 只承接退役内容，不承担当前主入口职责。

## 演进关系

- 默认演进链路是：`raw/inbox -> projects -> articles/concepts/indexes -> archive/log.md`。
- 新信息先作为来源进入 `raw/` 或 `inbox/`。
- 当信息开始参与当前项目判断和推进时，进入 `projects/`。
- 当项目里的某些结论已经脱离当前阶段、可以跨阶段或跨问题复用时，提升到 `articles/` 或 `concepts/`。
- 当一个主题需要长期导航、分类和检索时，再由 `indexes/` 收口。
- 当页面不再承担当前入口职责但仍有历史价值时，转入 `archive/`，同时在 `log.md` 留痕。

## 读取顺序

- 写任何内容时都要先建立全局背景，不允许只盯着当前文件局部改写。
- 先判断这段内容在整个 vault 里的位置：它服务哪个主题、哪个阶段、哪个主入口、哪类读者。
- 任何一段内容都不是孤立的，修改前必须先判断它的上游、下游和主入口。
- 默认先读 `README.md`、`INDEX.md`、相关目录的 `README.md`，再读目标文件本身。
- 如果目标在 `projects/`，先读 `projects/README.md`，再读相关的 `requirements.md`、`design.md`、`decisions.md`、`worklog.md`。
- 如果目标在知识库层，先找对应的主摘要页、概念页和索引页，确认哪一页才是单一信息源。
- 如果这次改动会影响阶段判断、导航结构、概念定义或项目状态，就必须额外回看相关入口页和主页面。
- 改动后要回看相关入口页和链接页，确认结构、跳转和职责没有被破坏。

## 目标文件的最小读取集

- 改 `projects/README.md` 时，至少读：`README.md`、`INDEX.md`、相关 `requirements.md`、`design.md`、`decisions.md`、`worklog.md`。
- 改 `requirements.md` 时，至少读：`projects/README.md`、相关 `raw/` 来源、已有 `design.md`、已有 `decisions.md`。
- 改 `design.md` 时，至少读：`projects/README.md`、`requirements.md`、已有 `decisions.md`、相关 `concepts/`。
- 改 `decisions.md` 时，至少读：`projects/README.md`、`requirements.md`、`design.md`、相关 `worklog.md` 或 `incidents.md`。
- 改 `worklog.md` 时，至少读：`projects/README.md`、当前相关 `decisions.md`、必要时读 `releases.md` 或 `incidents.md`。
- 改 `releases.md` 时，至少读：`projects/README.md`、`design.md`、`decisions.md`、相关验证记录。
- 改 `incidents.md` 时，至少读：`projects/README.md`、`releases.md`、相关 `worklog.md`、相关决策和原始证据。
- 改 `articles/` 时，至少读：对应 `raw/` 来源、相关 `concepts/`、必要时读相关项目页。
- 改 `concepts/` 时，至少读：相关 `articles/`、相关项目页、相关 `indexes/`。
- 改 `indexes/` 时，至少读：它要导航到的主页面，不允许只看索引本身闭门重排。

## 文件与目录操作

- 新建目录前先确认是不是已有目录的子集。
- 新建目录后先补 `README.md`；模板和索引按需补，不要为了完整性先铺满。
- 新建文件先确认它属于 `raw/`、`inbox/`、`articles/`、`concepts/` 还是 `indexes/`。
- 如果是支持性附件，优先放 `assets/`；如果是退役页面，优先放 `archive/`。
- 如果是活跃研发项目的文档，优先放 `projects/`。
- 对单一小项目，优先一页到底，拆分目录和子文件必须有明确理由。
- 修改文件前先读现有内容，只改必要部分。
- 重命名文件或目录时，优先保持内部链接同步更新。
- 处理已有目录时，先扩展再拆分，尽量不要平行复制一套新结构。
- 原始来源不要回写成整理稿，整理稿也不要再塞回 `raw/`。
- 合并、归档、删除都要同步更新 `INDEX.md` 和 `log.md`。
- 研发项目结束后，把稳定结论回收到知识库层，把项目特有上下文保留在 `projects/` 或 `archive/`。
- 结构性变更要写进 `log.md`。

## 写作规则

- 优先短页、强链接、可检索。
- 把事实、解释、推测分开写。
- 不确定时明确标注不确定。
- 名词尽量稳定，避免同义词泛滥。

## 新文档处理

1. 新材料先进入 `inbox/` 或 `raw/`。
2. 生成或更新摘要卡。
3. 回链到相关概念页。
4. 更新索引页。
5. 追加一条 `log.md` 记录。

## 定期检查

- 找断链。
- 找孤儿页。
- 找过时结论。
- 找没有实体页的重要概念。
- 找适合拆分成新页面的高频主题。
