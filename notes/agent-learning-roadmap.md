# AI Agent 开发学习路线

> 目标岗位：Agent 开发岗（2026 秋招）
> 背景：北邮 AI 本科，Java 入门，Python 能看懂但独立开发经验少
> 整理日期：2026-07-01

---

## 学习原则

1. **先跑通再理解** — 每阶段先跟着教程敲出一个能跑的项目，再回头理解原理
2. **一本书+一个项目** — 每阶段只选一本主教材 + 做一个小项目，不贪多
3. **不跳阶段** — 后面的阶段依赖前面的，按顺序走
4. **项目驱动** — 学完立刻做一个"最小可行项目"来巩固

---

## 总览

```
Phase 0: Python 进阶（异步 + Pydantic）         ← 你在这里附近
Phase 1: Web 框架（FastAPI）
Phase 2: 测试（pytest）
Phase 3: LLM 基础 + Prompt 工程
Phase 4: Agent 核心原理（ReAct / Tool Use）
Phase 5: Agent 框架（LangChain + LangGraph）
Phase 6: RAG + 记忆系统
Phase 7: MCP 协议
Phase 8: 多 Agent 协作（CrewAI）
Phase 9: 评估 + 生产部署 + 项目打磨
```

---

## Phase 0：Python 进阶（2-3 周）

### 需要掌握

- `async/await`、事件循环、`asyncio.gather` vs `create_task`
- 装饰器（理解原理，能自己写）
- Pydantic V2（BaseModel、Field、validator、model_config）
- 类型提示（`list[dict]`、`str | None`、`Literal`）

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **书籍** | 《Python asyncio 并发编程》（清华大学出版社，Matthew Fowler 著） | 中文，14 章，从协程到 aiohttp 全链路，实战驱动 |
| **书籍** | 《并发编程图解》（清华大学出版社，2025） | 图解 + Python 代码，零基础友好 |
| **文档** | [Pydantic 中文文档](https://docs.pydantic.org.cn/latest/) | 官方中文，边查边用 |
| **文章** | [Pydantic V2 入门教程（知乎）](https://zhuanlan.zhihu.com/p/2048162968047826094) | 30 分钟快速上手 |

### 小项目：CLI 天气查询工具

```
功能：输入城市名 → 异步请求公开天气 API → Pydantic 校验响应 → 格式化输出
练到：async/await、aiohttp、Pydantic BaseModel、Field 约束
预计：3-4 天
```

---

## Phase 1：Web 框架 FastAPI（2-3 周）

### 需要掌握

- 路由（GET/POST/PUT/DELETE）、路径参数、查询参数、请求体
- 依赖注入（Depends）、依赖链
- 中间件（请求日志、CORS、异常处理）
- 自动文档（Swagger UI / ReDoc）

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **文档** | [FastAPI 官方英文文档](https://fastapi.tiangolo.com/tutorial/) | 最权威，Tutorial - User Guide 从头跟到尾 |
| **文档** | [FastAPI 中文文档](https://cn.fastapi.tiangolo.com/) | 官方中文，术语对照 |
| **参考** | [FastAPI 9 大必知资源（百度开发者）](https://developer.baidu.com/article/detail.html?id=3803773) | |

### 小项目：Code Review Agent API 骨架

```
功能：POST /review 接收代码片段 → 调用 LLM 返回 Review 结果
练到：路由 + Depends + Pydantic Schema + 配置管理 + 中间件日志
预计：5-7 天（你已经在做了）
```

---

## Phase 2：测试 pytest（1 周）

### 需要掌握

- `@pytest.fixture`、`conftest.py`
- `@pytest.mark.parametrize` 参数化测试
- `pytest-cov` 覆盖率报告
- FastAPI 的 `TestClient` 集成测试

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **文档** | [pytest 官方文档](https://docs.pytest.org/) | 英文，但非常清晰 |
| **书籍** | 《自动化测试实战教程（基于Python语言）》（电子工业出版社，2025） | 中文，pytest + Selenium + Appium |
| **文章** | [pytest 入门指南 2025 实战版（CSDN）](https://blog.csdn.net/haolove527/article/details/154786682) | 1 小时快速上手 |

### 小项目：给 Phase 1 的 API 写全套测试

```
功能：用 TestClient + pytest 覆盖 /review 和 /health，参数化测试 + 异常用例
练到：fixture、parametrize、mock LLM 调用、覆盖率 > 80%
预计：3-4 天
```

---

## Phase 3：LLM 基础 + Prompt 工程（2 周）

### 需要掌握

- LLM API 调用（OpenAI / DeepSeek SDK）
- System Prompt vs User Prompt
- Few-shot、Chain-of-Thought（CoT）、结构化输出
- Token 机制、Temperature 调参
- Prompt 迭代与评估

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **课程** | [吴恩达《ChatGPT Prompt Engineering for Developers》](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) | 免费，1.5 小时，Prompt 工程必看 |
| **视频** | [B站吴恩达 Prompt 工程中文字幕](https://www.bilibili.com/) | 搜索"吴恩达 Prompt Engineering 中英双语" |
| **文章** | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | Agent 设计哲学，必读经典 |
| **文档** | [DeepSeek API 文档](https://platform.deepseek.com/api-docs/) | 你项目用的正是 DeepSeek |

### 小项目：Prompt 实验室

```
功能：一个命令行工具，输入任务描述 → 自动尝试 3 种 Prompt 策略（零样本/少样本/CoT）
      → 对比三个输出的质量
练到：API 调用、Prompt 模板、结构化输出解析、迭代调试
预计：4-5 天
```

---

## Phase 4：Agent 核心原理（3 周）

### 需要掌握

- Agent 的定义：LLM + 工具 + 循环决策
- ReAct 模式（Thought → Action → Observation → Thought → ...）
- Function Calling 机制
- Tool 的定义与注册
- Agent 循环的手写实现（不依赖框架）

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **课程** | [吴恩达《Agentic AI》](https://www.deeplearning.ai/short-courses/agentic-ai/) | 2025年新课，4大设计模式，纯 Python 不绑定框架 |
| **视频** | [B站吴恩达 Agentic AI 中英双语](https://www.bilibili.com/video/BV1aaxyz8ELY/) | 有UP主整理了配套代码 |
| **GitHub** | [agentic-engineering-handbook](https://github.com/keyuchen21/agentic-engineering-handbook) | 160+ 篇权威资源索引 |
| **GitHub** | [awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | 240+ 资源 + 三语路线图 |

### 小项目：手写 ReAct Agent

```
功能：不依赖 LangChain，纯 Python 手写 ReAct 循环
      Agent 可调用 2-3 个工具（搜索/计算器/文件读写），自动循环直到给出最终答案
练到：Agent Loop、Tool 注册机制、Stop Condition、System Prompt 设计
预计：7-10 天（这是整个路线中最重要的项目！）
```

---

## Phase 5：Agent 框架 LangChain + LangGraph（3 周）

### 需要掌握

- LangChain：Chain、PromptTemplate、Tool、Memory
- LangGraph：StateGraph、Node、Edge、Conditional Edge、Checkpointer
- Agent 的可观测性（LangSmith 追踪）

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **文档** | [LangChain 中文文档](https://langchain-doc.cn/v1/python/learn.html) | 官方中文 |
| **文档** | [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/) | 英文，核心是 StateGraph 概念 |
| **书籍** | 《LangChain与LangGraph实战》（机械工业出版社，2026） | 中文，徐澄/段毅著，10 章完整覆盖 |
| **文章** | [从零入门Agent开发：LangGraph与LangChain协同（百度开发者）](https://developer.baidu.com/article/detail.html?id=6996635) | 三阶段学习路径 |

### 小项目：用 LangGraph 重写 Phase 4 的 Agent

```
功能：把 Phase 4 的手写 Agent 用 LangGraph 重写
      → Graph 可视化 → 加 CheckPointer（中断恢复）→ 对比手写版和框架版的差异
练到：StateGraph、Node/Edge、条件分支、LangSmith 追踪
预计：7-10 天
```

---

## Phase 6：RAG + 记忆系统（3 周）

### 需要掌握

- Embedding 原理、向量检索
- RAG 完整链路：文档切分 → 向量化 → 存储 → 检索 → 增强生成
- 向量数据库：Chroma（开发）vs Milvus（生产）
- Agent 记忆：短期（上下文窗口）、长期（向量检索）、工作记忆（scratchpad）

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **书籍** | 《大模型应用开发：RAG实战课》（黄佳，2025） | 中文，DeepSeek + LangChain + Milvus，系统拆解十大组件 |
| **文章** | [学习向量数据库与 RAG 架构（腾讯云）](https://cloud.tencent.com/developer/article/2580844) | 含完整 Chroma 代码 |
| **文章** | [RAG 智能问答系统实战（掘金）](https://juejin.cn/post/7610141315292086312) | 2025 实战教程，从零到 Streamlit 界面 |
| **文章** | [Chroma vs Milvus 对比（CSDN）](https://blog.csdn.net/Trb201013/article/details/153831019) | 选型必看 |

### 小项目：个人知识库问答系统

```
功能：把你的 daily/ 和 notes/ 喂入向量数据库 → Agent 根据你的笔记回答问题
练到：文档切分策略、Embedding、Chroma、检索 + 重排序、RAG + Agent 结合
预计：7-10 天
```

---

## Phase 7：MCP 协议（2 周）

### 需要掌握

- MCP 三大组件：Host / Client / Server
- JSON-RPC 2.0 通信
- 用 FastMCP（Python SDK）写自定义 MCP Server
- MCP 的 Tool / Resource / Prompt 三种能力

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **书籍** | 《MCP原理揭秘与开发指南》（严灿平，微信读书，2025） | 中文，构建可扩展 AI 智能体 |
| **书籍** | 《MCP协议与大模型集成实战》（丁志凯，电子工业出版社，2025） | 中文，从协议设计到智能体开发 |
| **文章** | [学习AI Agent编程－MCP基础（阿里云）](https://developer.aliyun.com/article/1736406) | 2026.05 最新，FastMCP + LangGraph 示例 |
| **文章** | [MCP 从入门到实战（阿里云）](https://developer.aliyun.com/article/1738402) | 系统讲解三角色 + Cherry Studio 实战 |
| **GitHub** | [MCP-all-you-need-to-know](https://github.com/bi32/MCP-all-you-need-to-know) | 五章结构化中文教程 |
| **文档** | [MCP 官方文档](https://modelcontextprotocol.io/) | Anthropic 官方，协议规范 + SDK |

### 小项目：给自己的 Agent 写一个 MCP Server

```
功能：写一个 MCP Server 暴露 2-3 个工具（文件系统操作/Git log/天气查询）
      → Claude Desktop 或自己的 Agent 动态加载 → 对话中调用
练到：FastMCP、工具定义、stdio 传输、Host 端配置
预计：5-7 天
```

---

## Phase 8：多 Agent 协作（2 周）

### 需要掌握

- 多 Agent 协作模式：顺序式、层级式、群聊式
- CrewAI：角色定义、任务编排
- Agent 间通信与冲突解决

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **文档** | [CrewAI 官方文档](https://docs.crewai.com/) | 英文，快速上手 |
| **文章** | [AI Agent框架怎么选？LangGraph/AutoGen/CrewAI（CSDN）](https://modelengine.csdn.net/690b1f075511483559e277b6.html) | 三框架深度对比 |
| **文章** | [智能体框架大比拼（阿里云）](https://developer.aliyun.com/article/1678031) | 六大框架横向对比 |

### 小项目：多 Agent 代码审查团队

```
功能：3 个 Agent 协作 —
      Architect Agent（分析代码结构）
      → Reviewer Agent（检查 Bug/风格/安全）
      → Reporter Agent（汇总成 Markdown 报告）
练到：CrewAI Agent/Task/Crew 定义、顺序执行、结果传递
预计：5-7 天
```

---

## Phase 9：评估 + 生产部署 + 面试准备（3-4 周）

### 需要掌握

- Agent 评估：Evals 体系、准确性/延迟/成本
- Docker 容器化部署
- CI/CD（GitHub Actions）
- 简历项目打磨 + 面试八股

### 权威资源

| 类型 | 资源 | 说明 |
|------|------|------|
| **课程** | 吴恩达 Agentic AI 模块4（评估与误差分析） | 同一门课的后半部分 |
| **GitHub** | [Awesome_Agent_Dev](https://github.com/summerjava/Awesome_Agent_Dev) | Agent 面试大全 |
| **GitHub** | [EldonZhao/ai-agent-startup](https://github.com/EldonZhao/ai-agent-startup) | 2026 版系统路线 + 面试准备 |

### 小项目：Code Review Agent 完整版

```
功能：把 Phase 0-8 的东西全部集成 —
      FastAPI + Agent + RAG + MCP + 多Agent + 评估 + Docker 部署
      这是你的秋招核心项目
练到：全栈 Agent 系统、生产部署、简历叙事
预计：2-3 周
```

---

## 学习节奏建议

| 时间段 | 内容 | 强度 |
|--------|------|------|
| 上午 9:00-11:00（黄金期） | 新知识学习 + 写代码 | 高 |
| 下午（嘈杂期） | LeetCode 2 题 + git commit + 笔记整理 + 自检 | 低 |
| 晚上 | 复盘 + 准备明天的学习材料 | 中 |

**时间估算**：完整路线约 5-7 个月，你目前刚完成 Phase 0 的 Pydantic 部分和 Phase 1 的 FastAPI 基础。

---

## 关键项目里程碑

```
Phase 0 ──→ CLI 天气查询       （Python 进阶练习）
Phase 1 ──→ Code Review API    （FastAPI 骨架）  ← 你在这里
Phase 4 ──→ 手写 ReAct Agent   （最重要！核心能力证明）
Phase 6 ──→ 个人知识库问答     （RAG 实践）
Phase 8 ──→ 多 Agent 代码审查  （多 Agent 协作）
Phase 9 ──→ Code Review Agent  （秋招核心项目）
```

---

## 参考链接汇总

- **FastAPI 官方**: https://fastapi.tiangolo.com/tutorial/
- **FastAPI 中文**: https://cn.fastapi.tiangolo.com/
- **Pydantic 中文**: https://docs.pydantic.org.cn/latest/
- **pytest 官方**: https://docs.pytest.org/
- **LangChain 中文**: https://langchain-doc.cn/v1/python/learn.html
- **LangGraph 官方**: https://langchain-ai.github.io/langgraph/
- **MCP 官方**: https://modelcontextprotocol.io/
- **CrewAI 官方**: https://docs.crewai.com/
- **DeepSeek API**: https://platform.deepseek.com/api-docs/
- **吴恩达 Prompt Engineering**: https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
- **吴恩达 Agentic AI**: https://www.deeplearning.ai/short-courses/agentic-ai/
- **Anthropic: Building Effective Agents**: https://www.anthropic.com/engineering/building-effective-agents
- **awesome-agentic-ai-zh**: https://github.com/WenyuChiou/awesome-agentic-ai-zh
- **agentic-engineering-handbook**: https://github.com/keyuchen21/agentic-engineering-handbook
- **Awesome_Agent_Dev**: https://github.com/summerjava/Awesome_Agent_Dev
- **ai-agent-startup**: https://github.com/EldonZhao/ai-agent-startup
