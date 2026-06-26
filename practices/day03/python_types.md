# Python 类型注解 + pydantic 练习题

> 共 15 题，涵盖 type hints、Literal vs Enum、pydantic BaseModel、Field 约束、ValidationError、model_validator、往返测试。
> 练习文件写在 `practices/day03/type_answer.py`，每个题用 `# === 题 N ===` 分隔。

---

## 一、Type Hints 基础（改错 + 翻译）

### 题目 1
把下面三个旧式类型注解翻译成 Python 3.10+ 的新写法（不允许出现 `Optional`、`Union`）：

```python
from typing import Optional, Union

def f1(x: Optional[str]) -> int: ...
def f2(data: Union[str, bytes]) -> str: ...
def f3(result: Optional[dict]) -> Union[str, None]: ...
```

写出翻译后的版本。

### 题目 2
下面有三处类型注解，哪些是「真正的运行时约束」，哪些只是「标注而已」？分别说明原因。

```python
from typing import Literal

Level = Literal["low", "medium", "high"]

def review(content: str, level: Level = "medium") -> str:
    return content[:10]
```

- A. `str` 注解
- B. `Literal["low", "medium", "high"]` 注解
- C. `=` 默认值 `"medium"`

### 题目 3
下面代码中有两个问题，找出来并改正（不允许用 `Literal` 替代 `Enum`，也不允许反过来——两个都保留，修正其他问题）：

```python
from enum import Enum
from typing import Literal

Severity = Literal["info", "warning", "error", "critical"]

class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

Category = Literal["style", "naming", "logic", "security"]

def tag_issue(sev: Severity, cat: Category) -> str:
    return f"{sev}: {cat}"
```

---

## 二、pydantic 模型定义

### 题目 4
定义一个 `CodeFile` pydantic 模型，包含以下字段和约束：

| 字段 | 类型 | 约束 |
|------|------|------|
| `path` | `str` | 必填，长度 1~256 |
| `content` | `str` | 必填，长度 ≥ 1 |
| `language` | `str` | 默认 `"python"`，长度 ≥ 1 |
| `lines` | `int` | 必填，≥ 1 |

写出完整模型定义，并用 `model_validate()` 测试：
- 合法数据能正常解析
- `path=""` 抛出 `ValidationError`

### 题目 5
给题目 4 的 `CodeFile` 增加一个 `model_config`，要求：

- **拒绝多余字段**（传入模型没定义的字段就报错）

写出配置后的模型，然后测试：传入 `{"path": "a.py", "content": "x=1", "lines": 1, "author": "bob"}` 是否报错？

### 题目 6
给题目 4 的 `CodeFile` 增加一个 `computed_field`（派生字段）：

- `char_count: int` — 自动等于 `len(content)`
- 这个字段不出现在构造参数里，但 `model_dump()` 时能看到

写出完整实现。

---

## 三、Field 约束细节

### 题目 7
下面每个字段定义都存在一个「约束无效」或「约束意图与写法不匹配」的问题，找出来并改正：

```python
from pydantic import BaseModel, Field

class BadFields(BaseModel):
    a: str = Field()                          # 问题？
    b: str = Field(description="必填")         # 问题？
    c: int = Field(gt=0, default=-1)          # 问题？
    d: str = Field(min_length=5, max_length=1) # 问题？
```

### 题目 8
`Field(description=...)` 在 pydantic 中**不做任何校验**。请验证这一点：

- 定义一个模型，字段 `status: str = Field(description="只能是 ok 或 fail")`
- 写入测试：传入 `status="random_garbage"`，看是否会通过校验
- 说明被校验的行为是什么（引用 `.model_json_schema()` 输出中 description 的位置作为证据）

---

## 四、ValidationError 实战

### 题目 9
定义模型：

```python
from pydantic import BaseModel, Field

class Review(BaseModel):
    file_path: str = Field(min_length=1)
    line_number: int = Field(ge=1)
    severity: str = Field(min_length=1)
    message: str = Field(min_length=1, max_length=200)
```

写测试代码，用 `try/except` + `assert` 验证以下场景（不用 pytest）：

| 场景 | 预期失败的字段 | 预期错误类型 |
|------|----------------|-------------|
| `line_number=0` | `line_number` | `greater_than_equal` |
| `message=""` | `message` | `string_too_short` |
| 不传 `file_path` | `file_path` | `missing` |

示例写法参考（你按自己的理解写，这只是示意格式）：

```python
from pydantic import ValidationError

try:
    Review(line_number=0, file_path="a.py", severity="error", message="bad")
    assert False, "应该抛 ValidationError 但没抛"
except ValidationError as e:
    errors = e.errors()
    # errors 是一个 list[dict]，每个 dict 有 "loc"（字段路径）和 "type"（错误类型）
    # 你的断言写在这里
    print("通过：line_number=0 正确抛出了 ValidationError")
```

要求：用 `e.errors()` 断言出错的**字段名**（`loc`）和**错误类型**（`type`），分别对应表中三行。

### 题目 10
用题目 9 的 `Review`，测试 `model_validate()` → `model_dump()` 往返：

- 输入合法 dict → `model_validate()` 得到对象 → `model_dump()` 回 dict
- 断言：回字典的值与原始输入一致
- 额外测试：`model_dump(exclude_none=True)` 对 `Optional` 字段的行为（需给 Review 加一个 `suggestion: str | None = None`）

---

## 五、Enum 实战

### 题目 11
用 `str, Enum` 定义一个 `Status` 枚举：

```python
Status.PENDING    → "pending"
Status.RUNNING    → "running"
Status.SUCCESS    → "success"
Status.FAILED     → "failed"
```

然后在 pydantic 模型中使用它，验证：

- 传入 `"pending"` 能自动转成 `Status.PENDING`
- `model_dump()` 时自动转回 `"pending"`
- 传入 `"unknown"` 抛出 ValidationError

### 题目 12
以下场景应该选 `Literal` 还是 `Enum`？各写一句话理由：

- **A**: API 的排序方向，只有 `"asc"` 和 `"desc"` 两个值
- **B**: 代码审查的严重级别，4 个值，前端要遍历生成下拉框，后端要按级别排序
- **C**: HTTP 方法，只是用来限制函数参数不传错

---

## 六、model_validator 跨字段校验

### 题目 13
定义 `ReviewRequest` 模型：

```python
class ReviewRequest(BaseModel):
    file_path: str = Field(min_length=1)
    file_content: str = Field(min_length=1)
    language: str = "python"
    review_level: Literal["low", "medium", "high"] = "medium"
```

增加一个 `@model_validator(mode="after")`：

- 如果 `language == "python"`，但 `file_path` 不以 `.py` 结尾 → 报错
- 如果 `language == "javascript"`，但 `file_path` 不以 `.js` 结尾 → 报错

写测试验证两种错误情况都能被正确捕获。

---

## 七、综合题

### 题目 14
把 day03 daily 中定义的三个模型整合到一个完整的 `schemas.py` 风格文件里（写在 `practices/day03/type_answer.py` 中，单独用一个 section）：

- `Severity(str, Enum)`
- `ReviewComment`
- `ReviewRequest` 
- `ReviewResponse`

要求：
- 修复 daily 中原有的问题（`category` 从 `str + description` 改为 `Enum` 或 `Literal`，`total_issues` 改为 `computed_field`）
- 所有 `Field()` 约束齐全
- 添加合适的 `model_config`
- 新写法优先（`str | None` 替代 `Optional`）

### 题目 15
基于题目 14 的模型，写一个**独立的测试函数** `test_full_roundtrip()`：

1. 构造一个合法的 `ReviewRequest` dict
2. 构造一个合法的 `ReviewResponse` dict（包含 2 条 `ReviewComment`）
3. 分别做 `model_validate()` → `model_dump()` 往返
4. 故意传入一条非法 `ReviewComment`（`line_number=0`），断言抛出 `ValidationError`
5. 检查 `ValidationError.errors()` 中错误数量 ≥ 1，且包含 `line_number` 字段的错误

---

*祝练习愉快！*
