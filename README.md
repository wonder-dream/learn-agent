# learn-agent

> 2026 秋招 Agent 开发方向学习仓库 | 北邮 AI 本科
>
> 50 天计划 · 每日打卡 · 从零到 Agent 工程师

---

## 进度

```
M1 ████████░░░░░░░░ Day  1-15   Python 工程化 + LLM API + Agent 基础
M2 ████████████░░░░ Day 16-35   RAG + 代码审查 Agent 项目
M3 ████████████████ Day 36-50   Agent 范式 + 算法 + 面试
```

| 里程碑 | 时间 | 状态 |
|--------|------|------|
| M1 基础筑基 | Day 1-15 | 📋 任务就绪，6/24 启动 |
| M2 项目实战 | Day 16-35 | 📋 任务就绪 |
| M3 面试冲刺 | Day 36-50 | 📋 任务就绪 |

---

## 目录

```
learn-agent/
├── daily/          # 每日打卡记录（核心）
├── notes/          # 学习笔记
│   ├── transformer/
│   ├── prompt/
│   ├── rag/
│   ├── agent/
│   └── engineering/
├── projects/       # 实战项目
│   └── code-review-agent/
├── leetcode/       # 算法刷题
│   └── hot100/
└── interview/      # 八股 + 面经
```

---

## 每日打卡规则

1. 每天产出对应 `daily/XX.md` 文件
2. 文件内容：今日目标 → 完成情况 → 遇到问题 → 明天计划
3. 当天 23:59 前 commit 到 GitHub
4. 断签不补，空文件不删（公开耻辱驱动）

---

## 技术栈

- **语言**: Python (asyncio / pydantic / pytest / FastAPI)
- **框架**: LangGraph / LangChain
- **模型**: DeepSeek-v4-pro
- **工具**: Git / Docker / GitHub Actions

---

## 项目：代码审查 Agent

> 混合架构：AST 静态分析 + LLM 语义判断，LangGraph 状态机编排

- [ ] S1 静态分析层 — 风格检查 + 命名规范
- [ ] S2 语义分析层 — 逻辑 Bug 检测 + LLM 精判
- [ ] S3 集成层 — GitHub Webhook / CLI + 结构化 Review 报告

---

## LeetCode 进度

| 难度 | 目标 | 完成 |
|------|------|------|
| Easy | 40 | 0 |
| Medium | 50 | 0 |
| Hard | 10 | 0 |

---

*Start: 2026-06-24 | End: 2026-08-12 | 50 days*
