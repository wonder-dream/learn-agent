# 50 天任务总览

## M1：基础筑基（Day 1-15）

| Day | 主题 | 产出 | 依赖 |
|-----|------|------|------|
| 01 | Python 语法糖一：列表/字典/集合/字符串 | `notes/engineering/python-syntax-1.md` | — |
| 02 | Python 语法糖二：lambda/解包/装饰器/文件IO | `notes/engineering/python-syntax-2.md` | Day 01 |
| 03 | 类型注解 + pydantic v2 → 定义项目 Schema | `projects/code-review-agent/src/schemas.py` | Day 01-02 |
| 04 | asyncio 异步编程 + httpx 并发请求 | `notes/engineering/python-asyncio.md` | Day 02 |
| 05 | pytest 基础 + 项目 Schema 测试 | `projects/code-review-agent/tests/test_schemas.py` | Day 03 |
| 06 | FastAPI 基础：路由 + 请求/响应模型 | `notes/engineering/fastapi-basics.md` | Day 03 |
| 07 | FastAPI 进阶：依赖注入 + 中间件 + server 骨架 | `projects/code-review-agent/src/server.py` | Day 06 |
| 08 | LLM API 调通：DeepSeek-v4-pro | `projects/code-review-agent/src/llm_client.py` | — |
| 09 | Tool Calling / Function Calling 原理 | `notes/agent/function-calling.md` | Day 08 |
| 10 | Prompt 工程：System Prompt + CoT | `projects/code-review-agent/src/prompts/` | Day 08 |
| 11 | 手写最简 Agent 循环（原生 Python） | `projects/code-review-agent/src/simple_agent.py` | Day 09-10 |
| 12 | LangGraph 入门：StateGraph + Node + Edge | `notes/agent/langgraph-basics.md` | Day 11 |
| 13 | LangGraph 进阶：条件路由 + Checkpoint | `notes/agent/langgraph-advanced.md` | Day 12 |
| 14 | Python AST 模块：代码结构提取 | `notes/engineering/python-ast.md` | — |
| 15 | M1 复盘 + 查漏补缺 | `daily/15.md` 含 M1 总结 | Day 01-14 |

## M2：项目实战（Day 16-35）

### 阶段 A：静态分析层（Day 16-18）

| Day | 主题 | 产出 | 依赖 |
|-----|------|------|------|
| 16 | 风格规则引擎 | `src/rules/style_rules.py` | Day 14 |
| 17 | 命名规范 + 复杂度检查 | `src/rules/naming_rules.py` + 规则引擎整合 | Day 16 |
| 18 | 静态层测试 + 输出格式对齐 Schema | `tests/test_rules.py` + 静态层跑通 | Day 17 |

### 阶段 B：LLM 精判层（Day 19-20）

| Day | 主题 | 产出 | 依赖 |
|-----|------|------|------|
| 19 | 逻辑 Bug 检测 Prompt 调优 | `src/analyzers/logic_analyzer.py` | Day 10, 18 |
| 20 | 混合流水线 v1：静态筛候选 → LLM 精判 → 汇总 | `src/pipeline.py` | Day 19 |

### 阶段 C：LangGraph 编排 + 工具化（Day 21-24）

| Day | 主题 | 产出 | 依赖 |
|-----|------|------|------|
| 21 | LangGraph 编排：StateGraph 审查流水线 | `src/graph.py`（替换 pipeline.py 的 if-else） | Day 13, 20 |
| 22 | 工具节点封装 + 错误处理 + 重试 | `src/tools/` + 完善异常处理 | Day 21 |
| 23 | CLI 工具：命令行一键审查 | `cli.py` | Day 22 |
| 24 | FastAPI 对接完整流水线 | `src/server.py`（接入 graph.run） | Day 07, 23 |

### 阶段 D：测试 + 数据 + 展示（Day 25-29）

| Day | 主题 | 产出 | 依赖 |
|-----|------|------|------|
| 25 | 单元测试 + 集成测试 + mock LLM | `tests/` 完整测试套件 | Day 24 |
| 26 | 真实数据测试：10 个开源文件 → 量化指标 | 准确率/召回率/成本数据 | Day 25 |
| 27 | 打磨：日志 + 超时 + 限流 + 配置管理 | 生产级完善 | Day 26 |
| 28 | Demo 录制 + GIF + 项目 README | 项目对外展示完成 | Day 27 |
| 29 | 技术博客：代码审查 Agent 架构设计 | 知乎/掘金发布 | Day 28 |

### 阶段 E：扩展能力（Day 30-34）

| Day | 主题 | 产出 | 依赖 |
|-----|------|------|------|
| 30 | MCP 实践：给项目加 MCP Server 接口 | `src/mcp_server.py` + `notes/agent/mcp-basics.md` | Day 24 |
| 31 | RAG 微项目：代码文档检索问答 | `projects/rag-doc-search/` 快速原型 | — |
| 32 | RAG 微项目：混合检索 + Rerank + 评估 | 完善 + `notes/rag/rag-notes.md` | Day 31 |
| 33 | Agent 可观测性：日志追踪 + Token 成本统计 | `src/observability.py` + 仪表数据 | Day 27 |
| 34 | 项目最终打磨：代码整理 + 量化指标汇总 | 仓库 README 更新 | Day 28-33 |
| 35 | M2 复盘 + 查漏补缺 | `daily/35.md` 含 M2 总结 | Day 16-34 |

## M3：面试冲刺（Day 36-50）

### 算法专项（Day 36-40）

| Day | 主题 | 题量 | 产出 |
|-----|------|------|------|
| 36 | 链表 + 栈/队列 | 10 题 | `leetcode/hot100/` 题解 |
| 37 | 二叉树 + DFS/BFS | 10 题 | 同上 |
| 38 | 动态规划 | 8 题 | 同上 |
| 39 | 哈希表 + 双指针 + 滑动窗口 | 10 题 | 同上 |
| 40 | 排序 + 二分 + 回溯 | 10 题 | 同上 |

### 八股整理（Day 41-45）

| Day | 主题 | 产出 |
|-----|------|------|
| 41 | Transformer + Attention 原理 + 位置编码 + Tokenization | `interview/ai-basics.md` |
| 42 | Agent 范式（ReAct/PlanExecute/Reflexion）+ RAG 全链路 | `interview/agent-rag.md` |
| 43 | Python 高频（GIL/装饰器/生成器/asyncio）+ 操作系统 | `interview/cs-basics.md` |
| 44 | 数据库（索引/事务/分库分表）+ 网络（TCP/HTTP/DNS） | `interview/db-network.md` |
| 45 | 项目深挖话术：技术选型→架构→优化→量化指标 | `interview/project-qna.md` |

### 模拟面试 + 收尾（Day 46-50）

| Day | 主题 | 产出 |
|-----|------|------|
| 46 | 简历撰写 + 修改 + 投递列表 | 简历定稿 + 目标公司清单 |
| 47 | 模拟面试 Day1：技术面（八股 + 算法） | 录音复盘 |
| 48 | 模拟面试 Day2：项目面（项目深挖 + 场景设计） | 录音复盘 |
| 49 | 查漏补缺 + 仓库 README 最终打磨 | 仓库收尾 |
| 50 | 终盘：50 天总结 + 秋招投递启动 | `daily/50.md` 终章 |

---

## 每日必做

- [ ] 完成当日主线产出（见上表）
- [ ] LeetCode × 1-2 题（M1 入门题 + M2 中等题穿插）
- [ ] Git commit + push（绿点）
- [ ] 填写 `daily/XX.md` 打卡

## 每日 LeetCode 节奏

| 阶段 | 难度 | 节奏 |
|------|------|------|
| M1 Day 1-2 | — | 不刷，专心 Python |
| M1 Day 3-10 | Easy | 每天 2 道 Hot 100 Easy |
| M1 Day 11-15 | Easy + 少量 Medium | 每天 2 道 |
| M2 Day 16-35 | Medium 为主 | 每天 3 道，穿插复习 |
| M3 Day 36-40 | 专项突击 | 每天 8-10 道 |

## 变更记录

v2 (2024-06-21):
- Transformer 移出 M1 → 移到 M3 八股（学了不用会忘）
- Day 03 Schema 只写一次，M2 直接复用不复写
- Day 10 Prompt 只写一次，M2 只做"调优"不复写
- LangGraph 学完立即在项目中使用（Day 12-13 学 → Day 21 用）
- Day 06-07 FastAPI 建骨架 → Day 24 对接完整流水线（明确分工）
- MCP 改成工程实践（给项目加 MCP Server，不只看文档）
- RAG 改成微项目（2 天快速原型 + 评估，有代码产出）
- 新增 Day 33 Agent 可观测性（面试亮点话题）
