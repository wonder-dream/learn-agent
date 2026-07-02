# AI Agent 开发学习路线（2 个月压缩版）

> 目标：2026 秋招 Agent 开发岗，8 周从 FastAPI 基础到完整 Agent 项目
> 背景：北邮 AI 本科，Python 基础语法过关，FastAPI 入门中
> 整理日期：2026-07-01

---

## 核心策略：砍掉一切面试不考的

**什么不学**：Docker 部署、CI/CD、pytest 专题、CrewAI 深度、生产监控

**什么只了解**：MCP 协议（看懂是什么即可）、多 Agent 概念（能聊 2 分钟即可）

**什么死磕**：手写 ReAct Agent → 这是你面试时唯一能证明"我不是只会调 API"的东西

---

## 8 周安排

```
Week 1  ██░░░░░░  FastAPI 收尾 + Pydantic + asyncio 补漏
Week 2  ███░░░░░  LLM API + Prompt 工程
Week 3  ████░░░░  手写 ReAct Agent（上）— Agent Loop + Tool 注册
Week 4  █████░░░  手写 ReAct Agent（下）— 完整项目 + 面试叙事
Week 5  ██████░░  LangChain + LangGraph 入门
Week 6  ███████░  RAG 基础 + 集成到 Agent
Week 7  ████████  MCP 认知 + 多 Agent 概念 + 项目整合
Week 8  ████████  简历打磨 + 面试八股 + 缓冲区
```

---

## Week 1：FastAPI 收尾 + 基础补漏（7/1 - 7/6）

### 目标
- Day 07 内容收尾（Depends + 中间件 + 骨架组装）
- 跑通一个完整的 FastAPI + LLM 调用链路
- asyncio 核心概念补漏（够用就行，不读完整本书）

### 资源

| 用时 | 资源 | 学什么 |
|------|------|--------|
| 3h | [FastAPI 官方 Tutorial](https://fastapi.tiangolo.com/tutorial/) 的 Dependencies + Middleware 章节 | Depends 嵌套、中间件洋葱模型 |
| 2h | [Pydantic V2 中文教程（知乎）](https://zhuanlan.zhihu.com/p/2048162968047826094) | Field、validator、computed_field |
| 2h | asyncio 核心只看三板斧：`async def` / `await` / `asyncio.gather` | 够写 Agent 就行，别深入 |

### 交付物
- `server.py` + `dependencies.py` + `config.py` + `middleware.py` 跑通
- POST `/review` 能调用 DeepSeek 返回结果

### 验收标准
```bash
curl -X POST http://localhost:8000/review \
  -H "Content-Type: application/json" \
  -d '{"file_path":"test.py","file_content":"print(1)","language":"python"}'
# → 返回 ReviewResponse（含 LLM 返回的 review 内容）
```

---

## Week 2：LLM API + Prompt 工程（7/7 - 7/13）

### 目标
- 能用 DeepSeek/OpenAI SDK 调用 LLM
- 能写出结构化 Prompt（System Prompt + User Prompt + 输出格式约束）
- 理解 Token、Temperature、Few-shot、CoT

### 资源

| 用时 | 资源 | 学什么 |
|------|------|--------|
| 2h | [吴恩达 Prompt Engineering 课程（免费）](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) | 两大黄金原则 + 迭代方法 |
| 1h | [DeepSeek API 文档](https://platform.deepseek.com/api-docs/) | Chat Completion 接口 |
| 1h | 读 [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | Agent 设计哲学，反复看 |

### 交付物
- 一个 CLI 脚本 `prompt_lab.py`：输入任务描述 → 用 3 种策略（零样本/少样本/CoT）分别调 LLM → 打印对比结果

### 验收标准
```bash
python prompt_lab.py "判断以下代码是否有 SQL 注入风险: cursor.execute(f'SELECT * FROM users WHERE id={user_id}')"
# → 三个输出并排显示，能明显看出 CoT > Few-shot > 零样本
```

---

## Week 3-4：手写 ReAct Agent（7/14 - 7/27）★ 最重要

### 目标
- 不依赖任何框架，纯 Python 实现 ReAct Agent
- 理解 Agent Loop 的每一行代码
- Agent 能自动调用工具、观察结果、循环决策、输出最终答案

### ReAct 循环（面试必问，你必须能白板画出来）

```
Thought → Action → Observation → Thought → Action → ... → Final Answer
```

### 资源

| 用时 | 资源 | 学什么 |
|------|------|--------|
| 3h | [吴恩达 Agentic AI 课程](https://www.deeplearning.ai/short-courses/agentic-ai/) 模块 1-3 | Reflection、Tool Use、Planning 设计模式 |
| 随时 | [LangChain 中文文档 Agent 概念页](https://langchain-doc.cn/v1/python/learn.html) | 对照理解 Agent/Tool/AgentExecutor |

### 交付物：`handmade_agent/`

```
handmade_agent/
├── agent.py          # Agent 核心循环（Thought → Action → Observation）
├── tools.py          # 工具注册 + 3 个工具（搜索/计算器/文件读写）
├── llm.py            # LLM 调用封装
├── prompt.py         # System Prompt 模板
└── main.py           # 入口：接收用户问题 → Agent 自动解决
```

### 验收标准
```bash
python main.py "北京今天气温多少度？把结果保存到 weather.txt"
# Agent 自动：搜索天气 → 拿到结果 → 写入文件 → 返回"已保存"
# 控制台输出完整的 Thought/Action/Observation 过程
```

**这个项目的面试叙事**：
> "我手写了一个 ReAct Agent，没有用 LangChain。核心是一个 while 循环 —— LLM 输出 Thought 和 Action，我解析后调用对应工具，把 Observation 喂回去，直到 LLM 输出 Final Answer。这让我真正理解了 Agent 不是魔法，就是 LLM + 工具 + 循环。"

---

## Week 5：LangChain + LangGraph 入门（7/28 - 8/3）

### 目标
- 用 LangGraph 重写 Week 3-4 的 Agent（对比手写版）
- 理解 StateGraph / Node / Edge / Conditional Edge
- 体会到框架的价值：Checkpointer（中断恢复）、可视化 Graph

### 资源

| 用时 | 资源 | 学什么 |
|------|------|--------|
| 2h | [LangGraph 官方 Quick Start](https://langchain-ai.github.io/langgraph/tutorials/introduction/) | StateGraph 核心概念 |
| 2h | [LangChain 中文文档](https://langchain-doc.cn/v1/python/learn.html) Agent 章节 | AgentExecutor、create_react_agent |

### 交付物
把 Week 3-4 的 Agent 改用 LangGraph 重写，加一个功能：**中断恢复**（用户可以在 Agent 执行到一半时说"换个工具"）

### 验收标准
- LangGraph 版本和手写版本跑同一个任务，结果一致
- 面试时能说清楚"手写版 vs 框架版的区别"

---

## Week 6：RAG 基础（8/4 - 8/10）

### 目标
- 理解 Embedding + 向量检索原理
- 用 Chroma 搭一个最小 RAG pipeline
- 把 RAG 作为 Tool 集成到自己的 Agent 里

### 资源

| 用时 | 资源 | 学什么 |
|------|------|--------|
| 2h | [RAG 腾讯云教程](https://cloud.tencent.com/developer/article/2580844) | Chroma 完整代码 |
| 1h | Chroma 官方 Quick Start | pip install + 5 行代码跑通 |

### 交付物
Agent 新增一个 `search_knowledge_base` Tool：把 `daily/` 目录喂给 Chroma → Agent 可以用这个 Tool 检索你的笔记回答问题

### 验收标准
```bash
python main.py "我的 Day 02 学了什么？"  # Agent 调 RAG Tool 检索笔记 → 准确回答
```

---

## Week 7：MCP + 多 Agent 概念 + 项目整合（8/11 - 8/17）

### 目标
- **MCP**：知道是什么、能聊 1 分钟，不深入写代码
- **多 Agent**：知道顺序式/层级式/群聊式三种协作模式，能聊 2 分钟
- **项目整合**：把所有东西串成一个项目

### 资源

| 用时 | 资源 | 学什么 |
|------|------|--------|
| 1h | [MCP 阿里云教程](https://developer.aliyun.com/article/1736406) | 看懂概念 + 三大组件 |
| 0.5h | [智能体框架对比（阿里云）](https://developer.aliyun.com/article/1678031) | LangGraph vs AutoGen vs CrewAI 一句话区别 |

### 交付物
`code-review-agent/` 项目完整版：
```
POST /review → Agent Loop → 调用 Tool(分析/检查/搜索) → 返回 ReviewResponse
```
集成了 RAG（检索历史 review 记录）+ LangGraph（流程编排）

---

## Week 8：简历 + 面试准备 + 缓冲（8/18 - 8/24）

### 目标
- 简历上能写出 2 个项目（Code Review Agent 主项目 + Prompt 实验室副项目）
- 面试八股：Agent 定义、ReAct 循环、Function Calling 原理、RAG 链路
- 缓冲区：前 7 周哪掉了补哪

### 资源

| 资源 | 用途 |
|------|------|
| [Awesome_Agent_Dev](https://github.com/summerjava/Awesome_Agent_Dev) | Agent 面试八股合集 |
| [EldonZhao/ai-agent-startup](https://github.com/EldonZhao/ai-agent-startup) | 2026 面试准备指南 |

### 简历项目叙事模板

**项目一：Code Review Agent（主）**
> 基于 FastAPI + LangGraph 的代码审查 Agent 系统。手写 ReAct 循环实现 LLM 自主决策，集成 4 个工具（代码分析/安全检查/风格检查/RAG 知识检索），支持多步骤推理和中断恢复。后端用 Depends 实现依赖注入，Pydantic 做数据校验。

**项目二：Prompt 实验室（副）**
> CLI 工具，对比零样本/少样本/思维链三种 Prompt 策略在同一 LLM 上的输出质量差异。用于验证 Prompt 工程对 Agent 决策质量的影响。

---

## 每周节奏

| 时段 | 周一-周六 | 周日 |
|------|----------|------|
| 9:00-11:00（黄金） | 新知识 + 写代码 | LeetCode 4 题 |
| 14:00-17:00（嘈杂） | LeetCode 2 题 + git commit + 笔记 | 复习本周 |
| 20:00-21:00 | 复盘 + 准备明天材料 | 自由 |

---

## 砍掉的东西（以及为什么）

| 砍掉 | 理由 |
|------|------|
| 《Python asyncio 并发编程》整本书 | 只学够用的：`async def`/`await`/`gather` |
| pytest 专题 | 测试在项目中边写边学 |
| MCP Server 手写 | 面试不考 MCP 实现，知道概念就行 |
| CrewAI 多 Agent 项目 | 初级岗不要求多 Agent 实战经验 |
| Docker/CI/CD | 不是你的卖点，AI 专业不是运维专业 |
| 多模态 Agent | 超纲，实习生才要求这个 |

---

## 不要偏离的几件事

1. **Week 3-4 手写 Agent 是整个路线的灵魂** — 宁可 Week 1-2 压缩，也要保证这两周完整
2. **每天 LeetCode 不停** — Agent 项目再强，算法挂了一面就没了
3. **不要追新框架** — LangChain/LangGraph 就够，不要同时学 CrewAI/AutoGen/Dify
4. **每周末 commit** — 8 周后你的 GitHub 贡献图是面试官看到的第一个东西

---

## 参考链接

- [FastAPI 官方文档](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic 中文文档](https://docs.pydantic.org.cn/latest/)
- [吴恩达 Prompt Engineering（免费）](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [吴恩达 Agentic AI（免费）](https://www.deeplearning.ai/short-courses/agentic-ai/)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [DeepSeek API 文档](https://platform.deepseek.com/api-docs/)
- [LangChain 中文文档](https://langchain-doc.cn/v1/python/learn.html)
- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
- [RAG 腾讯云教程](https://cloud.tencent.com/developer/article/2580844)
- [MCP 阿里云教程](https://developer.aliyun.com/article/1736406)
- [Awesome_Agent_Dev 面试大全](https://github.com/summerjava/Awesome_Agent_Dev)
- [ai-agent-startup 路线](https://github.com/EldonZhao/ai-agent-startup)
