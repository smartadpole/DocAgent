---
type: template
id: TEMPLATE-TECHNOLOGY-RESEARCH-ADOPTION-CONTRACT-001
status: active
updated: 2026-07-31
tags: [template, research, technology-research, adoption-contract, research-capability]
---

# Technology Research Adoption Contract Template

本模板用于把 research-capability 的调研结论转成行动等级。它不追求篇幅，而是防止“资料很多”被误读成“可以采用”。

## 行动等级

| 等级 | 允许条件 | 允许说法 | 禁止说法 |
| --- | --- | --- | --- |
| Adopt | L1 证据充分，风险门闭合，PoC 或等价运行证据可复查 | 建议进入设计 / 实施准备 | 已上线 / 已验收 |
| Trial | 方向有价值，但缺目标环境验证或部分风险未闭合 | 建议小范围 PoC | 可生产接入 |
| Assess | 有线索，证据不足或当前事实易变 | 继续观察 / 补证据 | 可以采用 |
| Hold | 明确不匹配或风险不划算 | 暂缓，并写解锁条件 | 永久否定 |
| Blocked | 缺关键来源、权限、样本或 owner | 暂不能判断 | 已通过 / 已否决 |

## 采用前置条件

| 条件 | 当前证据 | 状态 | 不满足时降级 |
| --- | --- | --- | --- |
| 当前版本 / API 已查证 |  | confirmed / likely / blocked | Assess |
| license / 使用条款明确 |  |  | Hold / Blocked |
| 安全和供应链风险检查 |  |  | Trial / Hold |
| 隐私和合规边界明确 |  |  | Hold |
| 成本、限额和退出成本明确 |  |  | Trial / Assess |
| 本地或目标环境 PoC 通过 |  |  | Trial |
| claim scope 对应的 local validation / runtime readback |  |  | Trial / Blocked |
| owner 和维护责任明确 |  |  | Assess |
| 替代方案已比较 |  |  | Trial / Assess |

## 分支口径

- 技术专题：没有 PoC 时，最多建议 Trial / Assess。
- 开源工程：只读 README、Star、下载量，不足以建议 Adopt。
- 行业 / AI：只有趋势材料时，最多给 Assess。
- 产品 / 公司：条款、价格、数据边界不可见时，写 Blocked。
- PoC：成功只证明限定条件下可行，不能上推到生产验收。

## 刷新触发

- release、breaking change、deprecated API。
- pricing、license、服务条款、模型条款变化。
- CVE、安全公告、依赖和供应链变化。
- benchmark、模型、硬件、云平台能力变化。
- 法规、标准、监管和合规要求变化。

## 转接落位

| 结论类型 | 主落位 |
| --- | --- |
| 稳定概念 | `concepts/` |
| 单篇来源摘要 | `articles/` |
| 选型建议 | `projects/design/` 或 `projects/decisions.md` |
| PoC 计划 / 结果 | TASK、acceptance plan 或 report |
| 风险 | risk |
| 可复用方法 | skills / templates / governance |

## 失败判定

出现以下任一情况，不能作为采用依据：

- 没有研究合同、证据等级、风险门、行动等级或刷新触发。
- 把 L4 线索写成 L1 事实。
- 把旧 release、旧价格或旧政策当当前事实。
- 把宣传语、Star、融资额或单个 benchmark 写成采用结论。
- 把 PoC 通过写成生产验收。
- 把 deterministic contract sensor 通过写成真实研究 outcome 通过。
- R2+ 缺 Source Plan / coverage matrix，或补充材料缺 Evidence Delta Re-open。
- 把技术可行写成业务值得做。

## 最终判断块

```markdown
行动等级：
为什么：
必须先做：
不能上推到：
刷新触发：
沉淀入口：
未覆盖边界：
evaluator provenance：
outcome review：passed / failed / unproven
```
