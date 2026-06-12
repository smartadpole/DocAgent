---
type: article
date: 2026-06-12
updated: 2026-06-12
tags: [codex, goal, ai-agent, workflow, tutorial]
---

# Codex Goal 模式使用教程

- 来源：
  - 历史沉淀：[[articles/2026-05-25-codex-goals-research]]
  - 概念入口：[[concepts/codex-goals]]
  - 当前模板：[[templates/goal-contract-template]]
  - 治理边界：[[response-mode-routing]]、[[WORKFLOW]]、[[POLICY]]
  - 历史案例：Goal Contract 主控 / 子工程协作、Goal 自动续跑漏 `log.md`、DocCustomeranalysis Goal Contract 防线吸收
  - 外部工程复核：`/Users/hai/Documents/Code/DocCustomeranalysis/articles/2026-06-12-codex-goal-mode-usage-review.md`
- 类型：操作教程
- 适用对象：需要把 Codex 长时任务从“一次提示词”升级成“可审计完成契约”的用户和 agent 维护者。

## 一句话总结

Codex Goal 模式最稳的用法不是让 Codex “一直自动跑”，而是在启动长时任务前先冻结一份线程级完成契约：目标是什么、由什么证据证明、哪些边界不能越、什么时候必须停。

## 这到底是模板、skill、规则还是工作流

Goal Contract 的主体是 [[templates/goal-contract-template]] 里的模板，但它不是孤立模板，也不是普通 skill。

- **作为模板**：它提供长时任务启动前必须填写的字段骨架。
- **作为工作流约束**：[[response-mode-routing]] 和 [[WORKFLOW]] 规定它只在长时任务正式执行前启用，不是每轮默认仪式。
- **作为规则边界**：[[POLICY]] 规定它不能替代验收、状态关闭、memory、`log.md`、检查、提交或 finalizer。
- **作为 skill 关系**：具体 skill 可以引用它来处理长跑任务，但 Goal Contract 本身不是 `skills/` 下的执行技能。

所以在知识库里，它应被维护为“模板化的治理契约”：模板是主正文，规则和工作流提供启用条件与禁止上推边界，skill 只在需要时调用它。

## 先判断要不要用 Goal

适合使用 Goal 的信号：

- 任务终点清楚，但路径需要边做边发现。
- 用户已经在说“继续推进”“一直到完成”“重启 goal”“未完成 issue 继续处理”。
- 完成依赖多轮证据，例如测试、benchmark、报告、DB readback、UI 验证、复现记录或跨工程回传。
- 任务很容易跑偏，需要明确非目标、写入边界、服务边界或验收边界。
- 已经有可承接 Goal 的 owning page，例如 TASK、Issue、AP、测试报告、handoff 或 episode package；如果没有，先创建或指定记录位置。

不适合使用 Goal 的信号：

- 只是解释一个概念、查一个状态、改一行代码或做一次普通整理。
- 目标还没成形，成功标准、预算、权限或 owner 还需要人工裁定。
- 用户明确说“只记录问题，设定好目标，不需要排查”，这时应做 intake / goal freezing，而不是自动进入诊断。
- 当前任务已经进入验收关闭，Goal 只能作为过程契约，不能替代验收结论。

本库的固定口径是：Goal Contract 的切入点在 [[response-mode-routing]] 判断之后、正式长时执行之前。

## 启动前先写完成契约

一个可用 Goal 至少写清六件事：

1. **记录位置**：这个 Goal 实例写在哪个 owning page，后续从哪里回看。
2. **期望最终状态**：完成后世界应该变成什么样。
3. **完成判定**：哪些结果算 done，哪些只能算 partial / review / blocked。
4. **验证面 / 证据边界**：用哪些测试、报告、日志、artifact、人工确认或读回证明；哪些证据不能上推。
5. **验收目标维度**：本轮要关闭哪个维度；上线执行、全量跑批或未来扩展目标是否只是背景目标。
6. **约束和允许边界**：能动哪些文件、仓库、服务、数据、环境；哪些明确不做。
7. **迭代策略**：每轮检查什么、记录什么、下一步怎么选。
8. **停止条件**：权限缺失、证据不足、预算耗尽、目标冲突或需要用户裁决时怎么停。

可复制骨架：

```text
目标：持续推进 <任务>，直到 <期望最终状态> 成立，或被证据证明暂时无法继续。

记录位置：<TASK / Issue / AP / 测试报告 / handoff / episode package / 其他 owning page>

完成判定：
- done：<必须满足的证据>
- partial / review：<只能说明局部成立的证据>
- blocked：<必须停止的条件>

本轮验收维度：
- <本轮要关闭的维度>
- <全量 / 上线 / 未来扩展目标是否不属于本轮关闭条件>

验证面：
- <测试 / benchmark / 报告 / DB readback / UI / 人工确认>
- <哪些证据只能作为辅助输入，不能上推成闭环>

边界：
- 允许：<文件 / 仓库 / 工具 / 环境 / 数据>
- 不做：<非目标 / 禁止操作 / 需用户确认的动作>

迭代：
- 每轮记录：<动作、证据变化、下一步最高价值检查>
- 停止并汇报：<阻塞原因、已有证据、缺少什么、恢复动作>
```

## 实际使用流程

1. **先判模式**：按 [[response-mode-routing]] 确认这是长时任务，不是快速诊断、普通沉淀或一次性改动。
2. **指定 owning page**：把 Goal 实例落到 TASK、Issue、AP、报告、handoff 或 episode package；没有落点的 Goal 很容易变成聊天里的漂浮目标。
3. **冻结契约**：用 [[templates/goal-contract-template]] 写出期望最终状态、完成判定、证据、验收维度、边界和停止条件。
4. **启动 Goal**：如果当前 Codex 界面支持 `/goal`，把契约压缩成一条清晰目标；如果当前界面不暴露 `/goal` 命令，也把这份契约作为线程级执行基准。
5. **每轮回到契约**：每次自动续跑或用户要求继续时，先对照完成判定和证据边界，再决定继续、收尾或停。
6. **收尾做证据审计**：结论只能写 done / partial / review / blocked，不能把预算耗尽、模型自述、health、日志或 handoff 直接写成完成。
7. **发生内容变更就走门禁**：Goal 自动续跑不是跳过 `log.md`、检查、finalizer 或提交闭环的例外。

历史材料中出现过的控制面包括 `/goal`、`/goal pause`、`/goal resume` 和 `/goal clear`。本机当前 `codex-cli 0.130.0` 的顶层帮助不展示交互式 slash command 细节，所以教程中更稳定的知识是“完成契约怎么写、怎么审计”，具体命令面以当前 Codex UI / CLI 为准。

## 三类高频写法

### 性能优化

```text
持续优化 <模块>，直到 <指标> 达到 <阈值>，并由 <benchmark> 证明；同时保持 <正确性测试> 通过。只修改 <允许范围>。每轮记录改动、指标变化和下一步实验。如果 benchmark 无法运行、指标无有效改善路径或正确性回退，停止并报告证据和阻塞点。
```

### Flaky test / 复杂 bug

```text
持续处理 <问题>，直到要么用复现记录和测试结果证明已修复，要么明确说明无法继续的真实原因。允许读取 <日志 / 报告 / 相关代码>，不扩大 <公共 API / 数据写入 / 环境操作>。每轮记录复现条件、假设变化和下一步检查项。无法复现或证据不足时停止。
```

### 主控 / 子工程协作

```text
主控负责定义最终状态、验收口径、关闭条件和风险归口；子工程只执行实现、局部验证和证据回传。子工程 health、日志、自述和 accepted / running 中间态只能作为辅助证据，不能直接关闭主控 TASK / EP / FP / Gate。
```

## 历史经验提炼

1. **Goal 不是自动关闭器**：历史里最稳定的结论是，Goal 是线程级完成契约，不是全局 memory、仓库级规则、项目状态或验收报告。
2. **三条防线最重要**：期望最终状态防跑偏，验证面 / 证据边界防漂移，预算 / 阻塞停止条件防无限探索。
3. **自动续跑不享有豁免权**：Goal 长跑产生内容变更时，仍要同步 `log.md`、运行检查、处理 finalizer、按主题提交。
4. **主控和子工程要分工**：主控定义完成和关闭；子工程生产证据。不要让子工程自述反向覆盖主控验收口径。
5. ** intake 和 diagnosis 要分开**：用户只要求记录问题、设定目标时，先冻结目标和边界，不要因为 Goal 存在就开始排查。
6. **实例必须有落点**：Goal Contract 应进入 owning page；否则后续很难审计哪一轮改变了完成判定或证据边界。
7. **验收维度不要被全量目标污染**：`full`、`all`、全量跑批或上线执行目标可以作为背景，但只有写进本轮完成判定的部分才是本轮关闭条件。

## 常见反模式

- 把 `/goal 继续完善这个系统` 当成有效目标。
- 没写验证面，只写“直到完成”。
- 没写停止条件，导致复杂问题无限扩读。
- 把 budget 用完、服务 health、日志存在、handoff 写了、任务 accepted / running 当成 done。
- 把 Goal 当成规则升级，不经 [[POLICY]] 和 [[agent-governance-strategy]] 判断就扩大成每轮硬约束。
- 用 Goal 掩盖人工未拍板的范围、指标、权限、生产事实或验收标准。
- Goal 只停在聊天里，没有落到 TASK、Issue、AP、报告、handoff 或 episode package。
- 把“最终上线需要全量执行”误写成本轮验收必须完成的阻塞项。

## 最小检查表

启动前问：

- 这是不是终点清楚、路径需要探索的长时任务？
- Goal 实例写在哪个 owning page？
- 完成判定有没有 done / partial / blocked 的区分？
- 验证面能否直接证明最终状态？
- 哪些证据只能作为辅助输入？
- 本轮验收维度和上线 / 全量执行目标有没有分开？
- 写入边界、服务边界、环境边界是否清楚？
- 预算或停止条件是否清楚？

收尾前问：

- 当前证据能证明 Goal 的期望最终状态吗？
- 有没有把中间态上推成闭环？
- 有没有需要 `log.md`、检查、提交或 handoff 的内容变更？
- 如果 blocked，是否写清已尝试路径、已有证据、阻塞点和恢复动作？

## 相关页面

- [[concepts/codex-goals]]
- [[articles/2026-05-25-codex-goals-research]]
- [[templates/goal-contract-template]]
- [[concepts/harness-engineering]]
- [[concepts/agent-governance]]
- [[response-mode-routing]]
- [[WORKFLOW]]
- [[POLICY]]
