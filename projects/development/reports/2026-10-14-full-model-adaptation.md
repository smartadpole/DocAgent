---
type: test-report
id: REPORT-FULL-MODEL-ADAPTATION-20261014
project: PROJ-WIKI-001
status: verified-local
updated: 2026-10-14
tags: [agent, skills, model, template, validation]
---

# 完整模型适配整改与验证

设计 owner：[[projects/design/topics/agent-workflow-memory-harness-skill-landing]]。验证对象是本仓 Agent 指令、技能、模板及检查器实现，不是业务服务或发布 Gate。用户要求按同等完整范围处理剩余 Skills、长模板、真实模型验证，并直接切换新流程、检查和提交。

## 范围与设计取舍

前一轮报告只证明入口、发现、触发和阶段合同，本轮接续其未完成范围。实际覆盖 18 个技能、17 份可迁移清单、6 份新条件参考和既有研究方法图；三份核心长模板改为最小合同加条件扩展，并同步五份采纳 / 执行 / 回传模板、技能模板、导航与实际消费者。

保留原生中文融合问候、知识深度、单一信息源、事项父级、原始现象、权限和公开安全。没有引入业务模型迁移、用户级配置修改、生产操作或新旧双入口。历史报告与未修改的历史呈现仍保存当时证据，不成为当前运行入口。

| 技能 | 处理与特色承接 |
| --- | --- |
| cross-project-governance-audit | 指定范围取证，明确全工程请求才展开注册全集；保留 source-depth 与三类缺口 |
| cross-project-skill-adoption-prompt | 授权内直接适配、验证与提交；仅委托执行 / 只要提示词时加载任务书参考；golden 按语义比较 |
| delivery-retrospective | 保留需求到发布交付链，证据地图按受影响环节读取，保留上轮行动兑现 |
| documentation-maintenance | diff 驱动，同步授权内必要文档；保留 generated 源、thin adapter 与方案裁决边界 |
| goal-contract | 复用 owner；独立文档与 Goal 工具授权分别判断；保留证据层、预算、停止 |
| historical-dialogue-retrospective | 普通问因短路；深度参考保留原始 session、目标、纠偏、效率与行动归口 |
| issue-analysis | 最小可区分验证；条件参考承接跨工程事实层、责任与联测；原始现象不改写 |
| knowledge-linking | 保留非 log 稳定入口与有意义关系，不为数量制造邻接 |
| loop-engineering | 单 agent 合法；委派细节按条件读取；发现、去重、持久恢复、oracle、预算与停止完整保留 |
| performance-bandwidth-analysis | 局部直接证据可支持局部结论；保留业务分母、重叠耗时、残差、覆盖矩阵与容量边界 |
| public-html-publish | 生成 HTML 不触发发布；publication profile 唯一承接现场状态；保留 allowlist、隔离及 live / denial |
| research-capability | 公共研究合同唯一 owner；R0–R4、L1–L6、R2+ 覆盖、反证、修订、停止及专业方法可达 |
| retrospective-capability | 真实学习信号或显式请求触发；保留年度档案、索引、上轮行动回检与原 owner |
| runtime-config-switch | 保留来源优先级、活动任务、reload、default path proof、合成数据清理和回滚 |
| technology-research | 公共方法复用总技能；保留机制、开源健康 / license、行业生态、成本、PoC 与源码验证 |
| topic-visual-presentation | 默认有组织 HTML；正式导出和 v2 bundle 按条件启用，保留语义绑定、页面树、渲染与独立评价边界 |
| transferable-skill-governance | 能力与风险优先，分数仅作线索；保留原生适配、项目事实隔离与外部评价边界 |
| work-item-auto-decomposition | 保持项目绑定；按阶段补关系，父 EP、原始 Issue 和父级关闭守卫不削弱 |

三份核心模板不再要求未触发字段、空 no-op 或全角色表。`conditional_sources` 是离线检查依赖清单；每条都有真实链接和正文触发，模型按任务读取，检查器不会把所有参考注入运行上下文。断链、目录逃逸、重复、循环和格式错误均拒绝。

旧的固定标题、篇幅、装饰性 marker 检查改为能力接线检查，保留研究合同正反 fixture、事项语义、发布安全和正式 v2 验证。独立审查发现研究治理页仍强制统一技术行动枚举与逐 owner no-op；已同步唯一治理 owner，避免旧默认从其他入口恢复。

## 真实模型方法与结果

官方基线核对 [GPT-6 Astra Skills 指导](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) 与 [模型使用指南](https://developers.openai.com/api/docs/guides/latest-model)。当日官方解析器返回 gpt-6-astra，本机原生 model/list 默认模型为 gpt-6.1-sol，两者分别验证，未改变用户模型配置。

使用显式 opt-in 的 `scripts/run_model_adaptation.py` 和 `scripts/fixtures/model_adaptation/cases.json`。每次复制输入及相对技能链接到独立数据目录，固定模型与 medium 推理；只读场景用 read-only sandbox，文件修复用 workspace-write。保留逐文件指纹、提示词、事件、原始回答、用量和退出码；oracle 不发送给被测模型。独立评审读原始输出与工具证据，不采用作者自评分。

| 验证组 | 观察与结论 |
| --- | --- |
| Astra 基线与候选同题六场景 | 授权采纳、复用 TASK、语义 golden、临时 HTML、独立 Goal、持久 Loop；候选六项通过。基线多数也能正确裁决，但需解释旧条款冲突或裁剪默认，不能把基线伪称全面失败 |
| Astra 专业三场景 | accepted / UI / DB 事实归一与最小读回；营销与实验分层、反证及 PoC 停止；原始 session 与纠偏 / owner 复盘。三项通过；首次 429 无回答，完整保留，原输入重跑成功 |
| Astra 运行边界三场景 | override 不证明默认切换、样本等待不证明生产容量、他仓 200 不证明本仓发布。关键边界通过；原短答对完整恢复 / 清理的覆盖不足，保留 partial，不追改成全通过 |
| Astra 完整运行交接方案 | 新的明确完整方案请求覆盖来源、授权、非默认效果、无 override 默认路径、业务分母、清理读回、失败回滚与缺测；只证明方案能力，不冒充实际服务切换 |
| Astra 隔离文件任务 | 实际修复唯一授权链接，领域例外逐字保留；checker 退出 0，外部指纹确认只改目标文件，无新增提交 |
| Sol 融合冷启动 | 原定问候逐字匹配，四项编号与推荐第一步保留；事件仅最终回答，零工具、零修改 |
| Sol 隔离文件任务 | 同一真实修复四项 oracle 全部通过；只改授权链接，checker 成功，提交计数仍为初始一条 |

六场景同题单次测量：基线输入 259035 tokens、183.54 秒；候选输入 117588 tokens、87.53 秒。缓存、服务状态和单样本差异存在，只作为本次观测，不宣称普遍节省率或稳定收益。

## 静态、加载与呈现验证

- 入口 9 项、阶段合同 23 项、显式条件依赖 8 项回归通过；冻结本批变更后完整 `python3 scripts/check_all.py` 的 31 项门禁全部通过。
- Codex 原生 skills/list 强制刷新：18 个 repo 技能全部 enabled，errors=[]。真实测试轨迹实际读取了技能及研究 / 复盘深度参考；发现通过不等于所有模型必然正确调用。
- v2 正式呈现 portable、negative-suite 和 regenerated runtime-artifact-readback 通过。原 golden 的源片段按新默认更新，inventory 及 active profile 同步；旧 writer 仍禁写，没有双写。该检查证明结构及生成产物读回，不冒充新的 reader utility 或独立视觉评分。
- 公开安全、Markdown、技能与原生事项检查保留；公共报告不包含私有源工程、运行身份、本机路径、凭据或原始事件。

## 收尾、回退与结论边界

本仓起始干净，本轮只提交直接相关差异，不推送。提交身份由包含本报告的 Git commit 给出，避免自引用 hash；提交后重新核对 staged 与剩余 dirty。

回退应整体 revert 本批提交，连同技能、条件参考、模板、实际消费者、检查器和正式呈现 inventory 一起恢复，不能只恢复旧入口或旧字面 sensor。原始模型证据保存在维护端数据目录；复跑需要本地 Codex 可用和模型权限，完整静态检查不自动消耗模型调用。

本轮可证明本仓上述完整整改范围及有限真实场景结果。未开展真实生产服务切换、业务模型迁移、生产容量测试、公开发布或长期统计评估；这些没有被纳入本次授权目标，也不借结构、一次成功或文档压缩宣称完成。上游仅吸收条件加载与证据分层的系统增量，不搬运本仓项目事实。
