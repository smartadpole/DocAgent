# Performance Bandwidth Analysis Transfer

## 能力目标

以可比较的分层测量支持性能归因，限制容量外推。 运行入口为 [[skills/performance-bandwidth-analysis/SKILL]]；条件参考随入口按触发迁移，不全量注入每次运行。

## 可以吸收

- entrypoint、business denominator、timing ledger、重叠耗时与残差。
- client wall、service-side timing、trace artifact、API/DB/readback等证据分离。
- coverage matrix覆盖相关payload、并发单位、配置、revision与失败样本。
- 局部直接证据可确认局部瓶颈；生产容量需要代表性完整链路。

## 只能抽象吸收

生产拓扑、模型、样本、阈值、容量目标与环境配置属于目标工程，不作为通用默认值。

## 禁止复制

不复制来源工程身份、私有路径、项目状态、服务实例、业务数据、凭据、历史日志或一次性检查结论。源工程可访问不等于获准修改；目标已有规则和用户授权优先。迁移结果不冒充业务验收或外部评价完成。

## 目标工程结构自检

查找已有等价能力、当前owner、实际发现入口、允许写入范围和验证方法；优先复用，缺项按需要补齐。模板、reference和sensor只迁移当前能力真正消费的部分，不为形式完整预建目录。

## 验证要求

验证upload-only不推端到端、单请求不推容量、缺全链路不否定已确认局部等待；对比条件变化要声明不可直接比较。 运行目标适用检查，说明真实变更、验证和未证明的范围；结构检查不能证明模型行为正确。
