# 50 天任务总览

## M1：基础筑基（Day 1-15）

| Day | 主题 | 产出 |
|-----|------|------|
| 01 | Python 语法糖一：列表/字典/集合/字符串 | `notes/engineering/python-syntax-1.md` |
| 02 | Python 语法糖二：lambda/解包/装饰器/文件IO | `notes/engineering/python-syntax-2.md` |
| 03 | 类型注解 + pydantic v2 | `notes/engineering/python-types.md` |
| 04 | asyncio 异步编程 + httpx | `notes/engineering/python-asyncio.md` |
| 05 | pytest + 项目骨架测试 | `projects/code-review-agent/tests/test_schemas.py` |
| 06 | FastAPI 基础：路由 + 请求/响应 | `notes/engineering/fastapi-basics.md` |
| 07 | FastAPI 进阶：依赖注入 + 中间件 | `notes/engineering/fastapi-advanced.md` |
| 08 | LLM API 调通：DeepSeek-v4-pro | `projects/code-review-agent/src/llm_client.py` |
| 09 | Tool Calling + Function Calling 原理 | `notes/agent/function-calling.md` |
| 10 | Prompt 工程：System Prompt + CoT | `notes/prompt/prompt-engineering.md` |
| 11 | Transformer 一：Attention | `notes/transformer/attention.md` |
| 12 | Transformer 二：架构 + 位置编码 | `notes/transformer/architecture.md` |
| 13 | 手写最简 Agent 循环 | `projects/code-review-agent/src/simple_agent.py` |
| 14 | LangGraph：StateGraph + 条件路由 | `notes/agent/langgraph-basics.md` |
| 15 | M1 复盘 + 查漏补缺 | `daily/15.md` 含 M1 总结 |

## M2：项目实战（Day 16-35）

| Day | 主题 | 产出 |
|-----|------|------|
| 16 | Python AST 模块学习 | `notes/engineering/python-ast.md` |
| 17 | 静态分析：风格规则引擎 | `projects/code-review-agent/src/rules/style_rules.py` |
| 18 | 静态分析：命名规范 + 复杂度检查 | `projects/code-review-agent/src/rules/naming_rules.py` |
| 19 | 结构化输出设计：ReviewResult Schema | `projects/code-review-agent/src/schemas.py` |
| 20 | LLM 精判：Prompt 模板设计 | `projects/code-review-agent/src/prompts/` |
| 21 | LLM 精判：逻辑 Bug 检测实现 | `projects/code-review-agent/src/analyzers/logic_analyzer.py` |
| 22 | 混合流水线：静态筛候选 + LLM 精判 | `projects/code-review-agent/src/pipeline.py` |
| 23 | LangGraph 集成：StateGraph 审查流水线 | `projects/code-review-agent/src/graph.py` |
| 24 | 工具节点：AST 解析工具 + LLM 调用工具 | `projects/code-review-agent/src/tools/` |
| 25 | 错误处理 + 重试机制 + 超时控制 | 完善异常处理 |
| 26 | CLI 工具：命令行接口 | `projects/code-review-agent/cli.py` |
| 27 | FastAPI 服务：POST /review 端点 | `projects/code-review-agent/src/server.py` |
| 28 | 测试：pytest 单元测试 + 集成测试 | `projects/code-review-agent/tests/` |
| 29 | 真实数据测试：找 10 个开源 PR 跑结果 | 量化指标收集 |
| 30 | Demo 录制 + GIF 制作 | 项目 README 完善 |
| 31 | 博客：代码审查 Agent 技术方案 | 发布到知乎/掘金 |
| 32 | MCP 协议入门 + Server 构建 | `notes/agent/mcp-basics.md` |
| 33 | RAG 基础：Embedding + 向量数据库 | `notes/rag/rag-basics.md` |
| 34 | RAG 进阶：混合检索 + Rerank | `notes/rag/rag-advanced.md` |
| 35 | M2 复盘 + 查漏补缺 | `daily/35.md` 含 M2 总结 |

## M3：面试冲刺（Day 36-50）

| Day | 主题 | 产出 |
|-----|------|------|
| 36 | LeetCode 专项：链表 + 栈/队列 | 10 题 + 笔记 |
| 37 | LeetCode 专项：二叉树 + DFS/BFS | 10 题 + 笔记 |
| 38 | LeetCode 专项：动态规划 | 8 题 + 笔记 |
| 39 | LeetCode 专项：哈希表 + 双指针 + 滑动窗口 | 10 题 + 笔记 |
| 40 | LeetCode 专项：排序 + 二分 + 回溯 | 10 题 + 笔记 |
| 41 | 八股：Transformer + Attention 原理 | `interview/ai-basics.md` |
| 42 | 八股：Agent 范式 + RAG 全链路 | `interview/agent-rag.md` |
| 43 | 八股：Python 高频题 + 操作系统 | `interview/cs-basics.md` |
| 44 | 八股：数据库 + 网络 | `interview/db-network.md` |
| 45 | 项目深挖话术准备 | `interview/project-qna.md` |
| 46 | 简历撰写 + 修改 | 简历定稿 |
| 47 | 模拟面试 Day1：技术面 | 录音复盘 |
| 48 | 模拟面试 Day2：项目面 | 录音复盘 |
| 49 | 查漏补缺 + 项目 README 最终打磨 | 仓库收尾 |
| 50 | 终盘：50 天总结 + 秋招投递计划 | `daily/50.md` 终章 |

---

## 每日算法穿插

每天额外刷 1-2 道 LeetCode Hot 100，记录在 `leetcode/hot100/` 下。

## 每日必做

- [ ] 完成当日主线产出（见上表）
- [ ] LeetCode × 1-2 题
- [ ] Git commit + push（绿点）
- [ ] 填写 `daily/XX.md` 打卡
