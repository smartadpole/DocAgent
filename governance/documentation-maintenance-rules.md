---
type: governance
id: GOV-DOCUMENTATION-MAINTENANCE-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-12
tags: [governance, documentation-maintenance, sensor]
---

# Documentation Maintenance Rules

本页是 `documentation-maintenance` 的治理接线页。它回答：当代码、目录、规则、模板、sensor、视图、项目状态或公开行为变化时，什么时候必须同步文档，什么时候只记录检查结论，什么时候不能为了“看起来完整”扩写无关说明。

[[skills/documentation-maintenance/SKILL]] 是执行流程；本页是裁定规则。两者共同约束文档维护，避免文档漂移、过度重写和生成物污染。

## 触发条件

出现以下任一情况，必须进入 documentation-maintenance 判断：

- 代码或文档结构改变了读者、维护者或 agent 的入口。
- 新增、删除、重命名了 `governance/`、`skills/`、`templates/`、`projects/`、`views/` 或检查脚本。
- 改动影响公开 API、CLI、配置、环境变量、默认值、运行命令、验收方式、提交方式或浏览器 / 服务启动规则。
- 改动影响执行合同、响应模式、规则晋升、知识落位、模板反哺、skill maturity、Goal Contract、Issue 分析或 Harness 治理。
- 本轮发现文档中的路径、命令、状态、边界、链接、owner、目录职责或测试命令已经过期。
- 用户指出“你没按规则做”“wiki 不够成熟”“已有规则但没有执行”。

只要触发条件成立，先判定需要读哪些入口，再决定是否编辑。documentation-maintenance 不等于必然大改；它先证明有没有漂移。

## 证据顺序

文档维护必须从事实变化反推文档，不从想写的文档反推事实：

1. 真实 diff、用户指定文件、诊断矩阵、检查失败或运行证据。
2. 受影响主入口，例如 [[README]]、[[INDEX]]、[[AGENTS]]、[[governance/README]]、[[skills/README]]、[[templates/README]]、[[views/README]]。
3. owning page，例如某个 skill、template、governance rule、project page、service registry 或 report。
4. 关联 sensor，例如 `python3 scripts/check_all.py --only skill-maturity`、`documentation-maintenance`、`knowledge-linking`、`topic-visual-presentation`。
5. [[log]]，只记录本轮真实用户意图、关键动作和结构变化，不作为主动背景入口。

如果证据和文档冲突，先标注冲突层级。不要用最新回复、旧日志或记忆覆盖正式主入口。

## 必须同步的页面类型

| 改动类型 | 至少检查 | 常见同步 |
| --- | --- | --- |
| 新增技能 | [[skills/README]]、[[INDEX]]、技能页、TRANSFER、skill-maturity sensor | [[log]]、必要治理页 |
| 新增模板 | [[templates/README]]、使用它的 skill / governance | [[INDEX]]、sensor |
| 新增治理规则 | [[governance/README]]、[[AGENTS]] 或 [[WORKFLOW]] 的短引用 | [[POLICY]] 或 [[response-mode-routing]] |
| 新增 views/lens | [[views/README]]、[[views/lens-registry]]、对应 skill / template | `.gitignore`、导出边界 |
| 新增检查脚本 | `scripts/check_all.py`、owning skill / governance | [[AGENTS]] 或 [[WORKFLOW]] 的专项 sensor 提示 |
| 项目状态变化 | `projects/README.md` 或 owning project page | report / issue / risk / trace |
| 规则执行失守 | [[instruction-adherence]]、[[harness-feedback-ledger]] | sensor、模板字段或最终证明 |

同步的目标是消除漂移，不是把同一段正文复制到所有入口。入口页只放导航和最小语义，正文留在单一信息源。

## 保守编辑原则

- 先更新已有页，再考虑新建页。
- 新建页必须说明它承接的单一问题，以及不能替代哪些页面。
- 入口页用一句话加链接，避免复制正文。
- 规则页写裁定条件和边界，技能页写执行流程，模板页写字段骨架，sensor 写可机器检查的最小门禁。
- `views/` 只承接呈现层；PDF、PNG、SVG 导出件默认是缓存，不成为文档事实源。
- `log.md` 只写本轮主题化过程记录，不替代技能、规则、模板或项目状态。
- 不能因为矩阵缺 `large-body` 就堆无意义文字；正文厚度必须来自真实操作规则、反模式、示例、检查点或迁移边界。

## 不需要同步的情况

以下情况可以记录“检查后无需文档改动”：

- 纯内部重构没有改变读者可见行为、命令、入口或 agent 规则。
- 格式化、排序、注释微调没有改变合同。
- 临时运行输出、缓存、导出截图或本地预览没有进入长期结构。
- 用户明确只要快速诊断，并且没有形成长期项目事实或规则变化。
- 子工程内部文件变化没有授权回写本库，且本库只作为只读上下文源。

无需改动也要在最终回复写明已检查的边界；若本轮本库有内容或结构变化，仍按会话规则更新 [[log]] 并提交。

## sensor 要求

`documentation-maintenance` 的 sensor 只检查 wiring，不替代人工语义判断。它至少覆盖：

- [[skills/documentation-maintenance/SKILL]] 和 TRANSFER 是否存在。
- 本治理页是否存在并包含触发、证据、同步、保守编辑和禁止项。
- [[skills/README]]、[[INDEX]] 是否有技能入口。
- `scripts/check_all.py` 是否接入 `documentation-maintenance`。
- 技能页是否声明 `sensor` 和 `evidence boundary`。

如果 sensor 通过但文档语义仍漂移，按 [[instruction-adherence]] 判断是否需要补模板字段、触发器或更具体的检查。

## 输出合同

执行 documentation-maintenance 后，最终说明至少包含：

- 本轮触发原因。
- 已检查的事实源和入口。
- 已修改的页面或确认无需修改的页面。
- 运行的检查命令。
- 未覆盖边界。

禁止只说“已同步文档”。必须让后续 agent 看得出这次同步解决了哪个漂移问题。
