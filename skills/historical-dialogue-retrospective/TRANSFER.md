---
type: skill-transfer-manifest
skill: historical-dialogue-retrospective
status: active
updated: 2026-06-03
tags: [skill, transfer, retrospective, adoption]
---

# Historical Dialogue Retrospective Transfer Manifest

## 基本信息

- **能力名称**：完整复盘体系与历史对话 / Agent 工作流复盘能力
- **源技能**：[[skills/historical-dialogue-retrospective/SKILL]]
- **适用迁移场景**：目标工程需要建立复盘体系、升级复盘文件落位、引入 Agent 工作复盘、把历史对话复盘做成 skill，或把复盘结论反哺到模板、规则、sensor 和项目记忆。
- **不适用场景**：目标只是写一篇一次性复盘报告，或只需要记录单个 Issue / 事故原始事实。

## 迁移价值

- 把复盘从“总结文件”升级成长期学习工程。
- 同时覆盖项目复盘、软件研发复盘、Agent 工作复盘和历史对话复盘。
- 让复盘结论能回到未来研发实践、方案设计、工程治理、模板、skill、sensor 和记忆路由。
- 防止复盘行动项漂浮在正文里，或和 Issue、事故、log、决策、memory、trace 混用。

## 参考资料路径

### 核心 skill

- `/Users/hai/Documents/Docs/AcknowledgeBase/skills/historical-dialogue-retrospective/SKILL.md`

### 方法论 / concept

- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/project-retrospective.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/software-development-project-retrospective.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/concepts/agent-work-retrospective.md`

### 模板

- `/Users/hai/Documents/Docs/AcknowledgeBase/templates/project-retrospective-template.md`

### 规则 / workflow

- `/Users/hai/Documents/Docs/AcknowledgeBase/AGENTS.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/WORKFLOW.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/harness-evolution.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/governance/harness-feedback-ledger.md`

### 档案 / 运行层入口

- `/Users/hai/Documents/Docs/AcknowledgeBase/projects/retrospectives/README.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/projects/incidents/README.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/projects/development/issues/README.md`
- `/Users/hai/Documents/Docs/AcknowledgeBase/log.md`

### 检查脚本 / sensor

- `/Users/hai/Documents/Docs/AcknowledgeBase/scripts/check_all.py`
- `/Users/hai/Documents/Docs/AcknowledgeBase/scripts/check_harness_governance.py`

## 可吸收内容

- 复盘作为长期学习工程的价值定义。
- 复盘文件落位、命名、粒度和最小字段。
- 项目复盘、软件研发复盘、Agent 工作复盘和历史对话复盘的分层。
- 历史对话复盘 skill 的触发条件、证据源分层、输出格式和禁止项。
- 复盘行动项分流到既有 owner 页面的规则。
- 复盘结论反哺模板、skill、sensor、规则、memory 和 trace 的路由。

## 只能抽象吸收

- AcknowledgeBase 的目录结构。
- Gate / FP / EP / TASK / risk / issue / AP / report 事项体系。
- Harness ledger、sensor、规则晋升节奏。
- log eligibility 和收尾检查口径。

## 禁止复制

- AcknowledgeBase 的具体 log 条目。
- 本库项目状态、历史案例原文、一次性治理记录。
- 本机服务路径、工程路径、运行 ID、提交历史或用户偏好。
- DocCustomer、wiki 或其他下游工程的业务事实。

## 目标工程结构自检与落位建议

- **有 projects/ 结构时**：复盘档案默认放 `projects/retrospectives/`，模板放 `templates/`，skill 放 `skills/`。
- **无 projects/ 结构时**：复盘档案默认放 `docs/retrospectives/`，模板放 `docs/templates/` 或目标工程既有模板目录。
- **已有相近模块时**：先复用已有 `retrospective`、`postmortem`、`incidents`、`lessons-learned` 或 `governance` 入口，避免新建平行体系；但要保留 Issue / 事故事实主档案和复盘档案的分工。
- **同名目录职责冲突时**：不要只看目录名。若目标工程的 `templates/` 是前端 / 服务端渲染模板、生成物模板或业务运行资产，复盘模板应改落 `docs/templates/`、`.codex/agents/templates/` 或目标工程明确的文档模板目录。

## 目标工程应新增或更新

- 方法入口：项目复盘 / 软件研发复盘 / Agent 工作复盘说明。
- 档案入口：`projects/retrospectives/README.md` 或 `docs/retrospectives/README.md`。
- 模板：项目复盘模板。
- skill：历史对话 / Agent 工作流复盘 skill；如果目标工程没有 skills 体系，则写入 AGENTS 或 docs 的可执行流程。
- 规则 / 读取路径：AGENTS、WORKFLOW 或目标工程等价入口。
- sensor / 检查：如果目标工程已有 check 脚本，补入口或后续候选；没有时只写检查要求，不强行造脚本。
- README / INDEX / AGENTS：让人和 agent 都能找到复盘体系入口。

## 复盘体系迁移的最小模块清单

生成目标工程提示词时，必须保留下面这组模块；不能只写成“新增复盘目录和模板”。

1. **复盘方法入口**
   - 说明复盘是什么、什么时候启动、和 log / Issue / 事故 / 决策 / memory / trace 的区别。
   - 说明复盘如何服务未来研发实践、方案设计、工程治理、测试验收、运行质量和 Agent 工作方式。
2. **复盘档案入口**
   - 说明这页负责什么、不负责什么、复盘文件放哪里、命名规则、轻量 checkpoint / 标准复盘 / 深度复盘粒度、当前索引、共性主题、维护说明和沉淀路由。
3. **复盘模板**
   - 至少包含复盘对象、原始目标、实际结果、关键事实、偏差与原因、保留做法、改进行动、沉淀路由和未验证边界。
   - Agent 深度参与时还要保留 Agent 工作维度；软件研发项目还要保留交付链维度。
4. **软件研发项目复盘维度**
   - 覆盖需求、设计、事项关系、实现合同、测试验收、发布证据、运行质量、事故 / 回滚、协作治理和单一信息源。
   - 明确测试报告不是复盘，Issue 关闭不是复盘完成，单次事故不能直接泛化成全项目结论。
5. **Agent 工作复盘维度**
   - 覆盖目标理解、阶段判断、上下文读取、工具使用、执行策略、验证质量、沟通节奏、权限边界、沉淀路由、收尾和提交质量。
   - 明确 Agent 工作复盘评价的是 agent 如何工作，不替代项目结果复盘。
6. **历史对话 / Agent 工作流复盘 skill**
   - 定义触发场景、响应模式、证据源分层、对象框定、工作链还原、Agent 偏差分类、效率质量判断、workflow 改进路由、输出格式和禁止项。
   - 证据源至少区分当前上下文、log、harness ledger、原始 session / rollout、git diff / commit、受影响主页面、检查 / 测试输出、memory、最终回复 / handoff。
   - 禁止只凭 log 或当前上下文判断完整历史，禁止把一次偏差直接升级成硬规则。
7. **行动分流机制**
   - 复盘行动项必须分流到 Issue、incidents、研发事项、meetings、decisions、memory、trace、concepts、templates、skills、ledger、sensor 或规则入口，不在复盘正文里形成平行看板。
8. **治理自演进关系**
   - 单次表现进入复盘或 log；重复失守进入 feedback ledger / harness ledger；可模板化更新模板；可技能化更新 skill；可脚本化进入 sensor；影响执行顺序更新 WORKFLOW；影响必须 / 禁止行为更新 AGENTS；影响优先级或自动沉淀边界更新 POLICY 或目标工程等价规则页。
   - 不把所有复盘结论升级成硬规则，不为了完整复盘无限扩读，不让复盘体系变成新的治理噪音。
9. **入口同步**
   - 按目标工程实际结构更新 README、INDEX、AGENTS、WORKFLOW、docs / projects 入口、skills 入口和 templates 入口中的相关位置。
   - 入口同步只做导航和短说明，不复制复盘正文。

## 行动分流

- bug、偏差、验收失败：Issue。
- 事故事实和修复闭环：incidents。
- 研发交付动作：Gate / FP / EP / TASK / risk / acceptance / report 或目标工程等价事项系统。
- 跨 owner 协调：meetings。
- 关键取舍：decisions。
- 项目长期事实：memory。
- 需求演进：trace。
- 可复用方法：concepts 或 docs 方法页。
- 可复制骨架：templates。
- 高频 agent 流程：skills。
- 重复失守或机制缺口：harness ledger / feedback ledger。
- 可脚本化检查：sensor / check script。
- 执行规则变化：AGENTS / WORKFLOW / POLICY 或目标工程等价规则入口。

## 生成提示词时必须包含

- 明确说明目标是升级完整复盘体系，不只是新增目录或模板。
- 附上本 manifest 中的资料路径。
- 要求目标工程 agent 先读取自身结构，再决定落位；通用提示词生成端不必预读目标工程。
- 要求建立或完善方法入口、档案入口、模板、软件研发复盘维度、Agent 工作复盘维度、历史对话复盘 skill、规则入口、行动分流和治理自演进。
- 要求跑目标工程已有检查并提交。
- 如果已经读取目标工程结构，提示词必须写每个目标工程的差异化落位建议；如果没有读取，只要求目标工程 agent 自行判断，不编造。

## 推荐提示词骨架

复盘体系迁移提示词优先写成目标工程可执行任务书，不要写成迁移说明书。推荐骨架如下：

1. 开头直接写：`请升级本工程的完整复盘体系。目标不是只新增一个复盘目录，也不是只写一篇复盘模板，而是建立一套可持续运行的复盘系统。`
2. 写清复盘体系目标：复盘是长期学习工程，覆盖项目、阶段、事故、Issue、交付链偏差、Agent 协作偏差和治理缺口，并反哺未来研发实践、方案设计、工程治理、测试验收、运行质量和 Agent 工作方式。
3. 列 `复盘体系参考资料`：按档案层、模板、通用项目复盘、软件研发复盘、Agent 工作复盘、历史对话 skill、维护规则 / workflow 分组列绝对路径；如用户指定参考提交或版本锚点，应写入这一节。
4. 写 `吸收边界`：不要整库复制；只吸收系统层信息；禁止复制项目事实、log 历史、当前状态、案例原文或一次性治理记录。
5. 写 `目标工程中完成的设计`：要求先读取目标工程 README、AGENTS、docs、projects、issues、incidents、tasks、decisions、memory、trace、skills 等已有结构，再决定落位；有 `projects/` 优先 `projects/retrospectives/`，没有则优先 `docs/retrospectives/`，已有相近目录时优先复用。
6. 写 `需要建立的复盘体系模块`：逐项展开方法入口、档案入口、模板、软件研发项目复盘维度、Agent 工作复盘维度、历史对话 / Agent 工作流复盘 skill、行动分流机制、治理自演进关系。
7. 写 `需要更新的入口`：按目标工程实际结构选择 README、INDEX、AGENTS、WORKFLOW、docs/README、projects/STRUCTURE、projects/README、skills/README、templates/README，不机械照搬。
8. 写 `最终交付`：读取目标结构、说明推荐落位、新增或完善方法入口 / 档案入口 / 模板 / skill、同步入口、跑检查、提交 commit，并在最终回复说明落位、方法论、模板、skill、行动分流、检查和 commit hash。

这个骨架是复盘迁移的默认任务书形态。跨工程 meta-skill 的覆盖矩阵、目标差异化说明和验证要求只能补强它，不能替代它。

如果用户点名多个目标工程，最终提示词仍应先保留这份完整通用任务书，再追加每个目标工程的差异化落位说明。不要把多工程差异提前写成主叙事，导致“复盘体系目标、参考资料、模块清单、入口同步、最终交付”被压缩。差异化说明重点写结构事实、应复用入口、禁止误用目录、需要覆盖的默认落位和各仓库的检查 / 提交边界。

## 验证要求

- 目标工程入口能找到复盘体系。
- 复盘方法、档案、模板、skill 的职责分清。
- Issue / 事故 / log / 决策 / memory / trace 不被复盘替代。
- 行动项有 owner 落点。
- 检查通过或说明未能运行的原因。

## 最终回复要求

- 复盘体系落在哪里。
- 方法论在哪里。
- 模板在哪里。
- skill 在哪里。
- 行动项如何分流。
- 跑了哪些检查。
- commit hash。
