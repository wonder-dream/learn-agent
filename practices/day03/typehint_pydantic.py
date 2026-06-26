# -*- coding: utf-8 -*-
# 1
def f1(x: str | None) -> int: ...
def f2(data: str | bytes) -> str: ...
def f3(result: dict | None) -> str | None: ...


# 2
from typing import Literal

# 只是字面量取值范围，但是无法进行运行时操作，比如遍历这三个字面量
Level = Literal["low", "medium", "high"]


# str 注解只是标注，没有实际约束能力，除非使用pydantic或者mypy这种类型约束的库进行动态或者静态的检查
# Level = "medium" 是没有传入 level 这一参数时赋予的默认值，不参与校验，但是这里的 Level 注解和 str 一样
def review(content: str, level: Level = "medium") -> str:
    return content[:10]


# 3（没找到第二个问题）
from enum import Enum
from typing import Literal


# 多余的定义，被使用 Enum 的 Severity 类覆盖
# Severity = Literal["info", "warning", "error", "critical"]
class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


Category = Literal["style", "naming", "logic", "security"]


def tag_issue(sev: Severity, cat: Category) -> str:
    return f"{sev}: {cat}"


# 4, 5, 6
from pydantic import BaseModel, Field, ConfigDict, computed_field


class CodeFile(BaseModel):
    path: str = Field(min_length=1, max_length=256)
    content: str = Field(min_length=1)
    language: str = Field(min_length=1, default="python")
    lines: int = Field(ge=1)
    model_config = ConfigDict(extra="forbid")

    @computed_field
    @property
    def char_count(self) -> int:
        return len(self.content)


d = {"path": "hello.py", "content": "hello", "lines": 1}
print(CodeFile.model_validate(d))


# 7
class BadFields(BaseModel):
    a: str = Field()  # 与没写 Field 一样的效果
    b: str = Field(description="必填")  # description 用于描述字段的业务含义
    c: int = Field(gt=0, default=-1)  # 默认值不符合约束条件
    d: str = Field(min_length=5, max_length=1)  # 最小长度大于最大长度


# 8
class Code(BaseModel):
    status: str = Field(description="只能是 ok 或 fail")


# 会通过校验，因为 description 只是便于开发者来了解字段的业务含义的
code = Code(status="random_garbage")
print(code.model_json_schema())


# 9
class Review(BaseModel):
    file_path: str = Field(min_length=1)
    line_number: int = Field(ge=1)
    severity: str = Field(min_length=1)
    message: str = Field(min_length=1, max_length=200)


from pydantic import ValidationError

try:
    Review(file_path="a.py", line_number=0, severity="1", message="1")
    assert False
except ValidationError as e:
    error = e.errors()
    assert any(e["type"] == "greater_than_equal" for e in error)
    print("通过：line_number=0 正确抛出了 ValidationError")

try:
    Review(file_path="a.py", line_number=2, severity="1", message="")
    assert False
except ValidationError as e:
    error = e.errors()
    assert any(e["type"] == "string_too_short" for e in error)
    print('通过：message="" 正确抛出了 ValidationError')

try:
    Review(line_number=2, severity="1", message="awi")
    assert False
except ValidationError as e:
    error = e.errors()
    assert any(e["type"] == "missing" for e in error)
    print("通过：不传 file_path 正确抛出了 ValidationError")

# 10
review1 = {
    "file_path": "a.py",
    "line_number": 10,
    "severity": "error",
    "message": "bad",
}
review_class = Review.model_validate(review1)
review2 = review_class.model_dump()
assert review1 == review2
print("验证成功")


# 11
class Status(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"


class Message(BaseModel):
    status: Status
    content: str = Field(min_length=1, max_length=100)


message = Message(status="pending", content="hello")
print(type(message.status))


# 12
# A: 只有两个值，并且我们不需要遍历或者使用这两个值在除了传入参数或者判断的其他地方，直接 Literal 就行
# B: 需要遍历也就是有运行时操作，我们需要将其设置为枚举类
# C: 只限制字面量取值，用 Literal 就行

# 13
from pydantic import model_validator
from typing import Self


class ReviewRequest(BaseModel):
    file_path: str = Field(min_length=1)
    file_content: str = Field(min_length=1)
    language: str = "python"
    review_level: Literal["low", "medium", "high"] = "medium"

    @model_validator(mode="after")
    def check_ext(self) -> Self:
        ext_map = {".py": "python", ".js": "javascript"}
        for ext, lang in ext_map.items():
            if self.file_path.endswith(ext) and self.language != lang:
                raise ValueError(
                    f"{self.file_path} 后缀是 {ext}，但 language={self.language}，不匹配"
                )
        return self
