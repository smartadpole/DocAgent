---
type: template
id: TEMPLATE-TECHNOLOGY-RESEARCH-EVIDENCE-MATRIX-001
status: active
updated: 2026-07-31
tags: [template, research, technology-research, evidence-matrix, research-capability]
---

# Technology Research Evidence Matrix Template

本模板用于 `research-capability` 的证据矩阵。它帮助 agent 把资料、事实、推论、风险、行动等级和沉淀落位分开。

## 1. 研究问题矩阵

| 问题 | 决策影响 | 必需证据等级 | 当前证据 | 状态 | 下一步 |
| --- | --- | --- | --- | --- | --- |
|  | high / medium / low | L1 / L2 / L3 / L4 |  | confirmed / likely / possible / blocked |  |

R2+ 必须给出 Source Plan checkpoint、coverage target 和停止条件；每个关键问题的覆盖状态只能是 `covered / partial / blocked`，不能用来源数量代替问题覆盖。

## 2. 来源矩阵

| 来源 | 类型 | 等级 | 当前性 | 可信度 | 用途 | 局限 |
| --- | --- | --- | --- | --- | --- | --- |
| 官方文档 | docs | L1 | current / stale / unknown | high / medium / low | API / pricing / policy / setup |  |
| 论文 / 标准 | paper / standard | L1 / L2 |  |  | mechanism / benchmark |  |
| repo / release | code | L1 |  |  | implementation / license / health |  |
| 本地运行 | local evidence | L1 |  |  | PoC / performance / compatibility |  |
| 行业报告 | report | L2 |  |  | market / trend |  |
| 媒体 / 博客 | article | L4 |  |  | clue only |  |

## 3. 分支矩阵

| 分支 | 必查事实 | 推荐证据 | 强结论前置条件 |
| --- | --- | --- | --- |
| 技术专题 | 概念边界、核心机制、生态、替代路线 | 官方文档、论文、标准、成熟实现 | 至少一个 L1 来源，风险和适用场景清楚 |
| 开源工程 | license、release、维护活跃、issue、运行方式、供应链 | repo、release、license、CVE、本地运行 | license 清楚，最小运行或代码审计完成 |
| 行业 / AI | 价值链、产品化路径、公司信号、监管、数据 | 官方产品、行业报告、论文、客户案例 | 多来源交叉，明确不确定性 |
| 产品 / 公司 | 能力、价格、SLA、数据处理、退出成本 | 官方文档、价格页、状态页、合同资料 | 当前价格和数据边界确认 |
| PoC | 成功标准、样本、指标、失败退出 | 本地命令、日志、结果、截图 | 可重复运行，失败边界记录 |
| 源码工程 | 真实实现、入口、依赖、测试、部署 | 本地代码、测试、运行、架构 | 完成指定审计等级 |

## 4. 风险矩阵

| 风险 | 触发条件 | 当前状态 | 阻断级别 | 缓解 / 下一步 |
| --- | --- | --- | --- | --- |
| security | CVE、权限、数据泄露、模型安全 |  | blocker / watch / none |  |
| license | 商用限制、copyleft、模型 license |  |  |  |
| privacy | 数据出境、训练数据、日志保留 |  |  |  |
| compliance | 法规、行业规范、审计 |  |  |  |
| supply-chain | 维护者、依赖、构建、镜像 |  |  |  |
| cost | 价格、限额、硬件、云资源 |  |  |  |
| operations | 监控、回滚、SLA、on-call |  |  |  |
| integration | API 稳定性、SDK、迁移成本 |  |  |  |

## 5. 行动等级矩阵

| 等级 | 条件 | 允许说法 | 禁止说法 |
| --- | --- | --- | --- |
| Adopt | L1 充分、风险可控、PoC 或约束验证完成 | 建议采用 / 进入设计或实施 | 已上线 / 已验收 |
| Trial | 价值明确，但缺本地验证或部分风险未清 | 建议 PoC / 小范围试用 | 可生产接入 |
| Assess | 线索有价值，证据不足 | 继续观察 / 补证据 | 值得投入实施 |
| Hold | 风险或收益不匹配 | 暂缓 | 永久不做 |
| Blocked | 缺关键权限、来源、样本或 owner | 暂不能判断 | 已否决 / 已通过 |

## 6. 结论生成器

```markdown
一句话结论：
证据等级：
行动等级：
主要依据：
主要风险：
下一步：
刷新触发：
沉淀落位：
未覆盖边界：
```

## 7. 降级检查

- 没有 L1：降级到 Trial / Assess / Hold。
- 没有当前查证：不要写“当前支持 / 当前价格 / 最新政策”。
- 没有本地运行：不要写“可生产接入”。
- 没有 license 检查：不要建议商用采用。
- 没有安全 / 隐私检查：不要建议处理敏感数据。
- 没有项目 owner：不要写“已拍板”。
- 没有 knowledge-linking：不要写“已沉淀完整”。
- 没有 counter-evidence：不要写“替代路线已经排除”。
- R2+ 没有 Source Plan checkpoint：不要写“系统性研究已完成”。
- 新材料没有 Evidence Delta Re-open：不要写“最新证据已吸收”。
- 没有与 claim scope 对应的 local validation：不要给 Adopt。
