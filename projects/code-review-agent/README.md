# 代码审查 Agent

> AI-powered code review: AST 静态分析 + LLM 语义判断，LangGraph 编排

## 架构

```
PR Diff → AST 静态筛查 → 候选问题 → LLM 精判 → 结构化 Review → 输出
         (规则引擎)                (DeepSeek-v4-pro)    (JSON/Markdown)
```

## 技术栈

- **编排**: LangGraph StateGraph
- **静态分析**: Python `ast` 模块
- **语义分析**: DeepSeek-v4-pro API
- **服务层**: FastAPI + asyncio
- **测试**: pytest + pytest-asyncio

## 快速开始

```bash
pip install -e ".[dev]"
cp .env.example .env  # 填入 DEEPSEEK_API_KEY
uvicorn src.server:app --reload
```

## 项目结构

```
code-review-agent/
├── pyproject.toml
├── README.md
├── src/
│   ├── server.py          # FastAPI 服务
│   ├── dependencies.py    # 依赖注入
│   ├── config.py          # 配置管理
│   ├── middleware.py       # 中间件
│   ├── schemas.py         # pydantic 数据模型
│   ├── llm_client.py      # DeepSeek API 封装
│   ├── pipeline.py        # 审查流水线
│   ├── graph.py           # LangGraph StateGraph
│   ├── rules/             # 静态规则
│   ├── analyzers/         # LLM 分析器
│   ├── prompts/           # Prompt 模板
│   └── tools/             # Agent 工具
├── tests/
└── cli.py                 # CLI 入口
```

## 检测能力

| 类别 | 方法 | 示例 |
|------|------|------|
| 命名规范 | AST 规则 | 变量/函数命名不符合 PEP 8 |
| 代码风格 | AST 规则 | 函数过长、嵌套过深 |
| 空指针风险 | LLM 精判 | 未检查 None 就访问属性 |
| 资源泄漏 | LLM 精判 | 文件未关闭、连接未释放 |
| 逻辑错误 | LLM 精判 | 条件判断遗漏、边界错误 |

## License

MIT
