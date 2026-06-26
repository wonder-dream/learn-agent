# 一、Type Hints

## 1. 为什么需要类型注解

<!-- 解释：动态类型 vs 静态检查，类型注解的三大作用（文档、工具检查、IDE 补全） -->

众所周知，python是一个动态类型的语言，数据类型是不固定的，同一个变量在现在是整型，下一次赋值之后就可以是字符串了。

这种设计虽然提高了开发的效率，让开发者不需要思考这里需要个什么类型的变量，但是在其他人进行 review 或者对于 IDE  的自动补全以及撰写文档的人来说想要分辨出函数参数或者类属性的数据结构带来了不小的麻烦，于是类型注解应运而生。

类型注解通过一种类似注释的方法，不强制性规范参数或属性的数据结构，但是给开发者和 IDE 提供了这里使用的类型的参考，因为参数和属性的类型往往确定之后是不再改变的。

类型注解作为一种非强制的规范，主要是用于提供合适的参考，加速开发效率和审查及文档效率，同时也有很多第三方库使用类型注解的机制来进行数据类型检查，便于接口的实现和安全性的保证，就比如今天学习的 pydantic。

## 2. Python 3.10+ 新写法

<!-- 对比旧写法 Optional/Union 和新写法 str | None、str | bytes -->

```python
# 旧写法
from typing import Optional, Union
some1: Optional[str]
some2: Union[bytes, str]
# 新写法（PEP 604）
some1: str | None
some2: int | str
```

## 3. 常用类型一览

<!-- 列出 str, int, float, bool, list[X], dict[K,V], tuple[X,Y], str | None, Literal["a","b"]，每种给一个简单例子 -->

```python
str: "hello world"
int: 123
float: 1.101
bool: True/False
list[X]: [1, "1", True]
dict[K,V]: {"key": "value", 1: 2}
tuple[X,Y]: (1, "1", True)
str | None: None
Literal["a","b"]: "a" or "b"
```



## 4. 核心认知：注解不影响运行时

<!-- 解释：Python 解释器不检查类型注解，mypy/pyright 做静态检查，pydantic 做运行时校验 -->

如上所述，类型注解在 python 解释中并不是一个强制性的规范，更多的只是一个给开发者提供便利的“注释”，如果要进行类型校验的话，就需要借助外部库的实现。

静态校验：也就是不运行完整脚本，只是通过类型注解和查看属性，参数类型来进行比对的方案，常用库有：mypy/pyright，这种库不能在服务运行时检查参数属性的合法性，只能通过特殊的运行方式进行审查。

动态校验：在脚本运行时进行校验的方案，在解释器运行到相应的部分时进行类型校验，服务上线后如果前端或者服务端传入不合法的数据，就会报错，常用库就比如 pydantic。

---

# 二、pydantic v2

## 1. BaseModel 是什么

<!-- 解释：类型注解 + 运行时校验 + 序列化 -->

BaseModel 是 pydantic 中定义的一种数据类的基类，提供对类中属性的类型注解进行运行时校验的能力，同时也能够对继承 BaseModel 的类进行自动化的序列化与反序列化，是 python 写后端服务中常用于定义数据库表对应类的常用类

## 2. Field 常用约束

| 约束 | 含义 | 例子 |
|------|------|------|
| `ge` | >= | age: int = Field(`ge`=0) |
| `le` | <= | age: int = Field(`le`=200) |
| `gt` | > | line_number: int = Field(`gt`=0) |
| `lt` | < | long: int = Field(`lt`=100) |
| `min_length` | 最小长度 | content: str = Field(min_length=1) |
| `max_length` | 最大长度 | content: str = Field(max_length=200) |
| `default` | 默认值 | language: str = Field(default="python") |
| `description` | 元数据（不校验！） | language: str = Field(description="编程语言") |

## 3. Field 常见陷阱

<!-- 写出今天踩到的坑：Field() 不加 default 只是加约束、description 不校验、min > max 等 -->

Field() 不加 default 表示该属性必须填，加了 default 表示可选了，不填使用默认值；description 的内容不参与校验，只是给人看的用来描述属性的业务含义；注意定义约束时的区间大小，一定要保证最大值大于最小值；le, lt, ge, gt 都是对数值进行的规范，其他可迭代对象都使用 min_length, max_length。

---

# 三、Literal vs Enum

## 1. 区别

| | Literal | Enum |
|---|--------|------|
| 运行时存在？ | 不存在 | 存在 |
| 能遍历？ | 不能遍历 | 能遍历 |
| IDE 补全？ | 不能自动补全 | 可以自动补全 |
| 序列化行为 | 只做字符串的的进出 | 会自动进行类型转换，对应字符串直接变成枚举类 |

## 2. 选型判断

<!-- 什么时候选 Literal，什么时候选 Enum -->

```
当我们只需要对字面值进行约束，同时给只需要做判断相等操作的时候可以使用 Literal；
一旦需要遍历等运行时操作，我们就需要使用 Enum 枚举类来定义。
```

---

# 四、ValidationError

## 1. 捕获方式

```python
from pydantic import ValidationError

try:
    # 构造模型
except ValidationError as e:
    errors = e.errors()  # list[dict]
```

## 2. errors() 返回结构

| 键 | 含义 |
|----|------|
| `"type"` | 错误类型 |
| `"loc"` | 错误位置 |
| `"msg"` | 错误信息 |
| `"input"` | 传入的错误参数 |

---

# 五、model_config（ConfigDict）

<!-- 列出今天学到的常用配置：extra, validate_default, validate_assignment, frozen, str_strip_whitespace -->

```python
extra: 是否接收额外信息（不在类中定义的部分） "forbid": 报错, "ignore": 忽略不保留, "allow": 保留在实例中
validate_default: 对默认值进行合法性校验
validate_assignment: 对每次赋值操作后进行合法性校验
frozen: 类属性不可变
str_strip_whitespace: 对字符串默认进行 strip() 操作
```



---

# 六、model_validator

<!-- 解释 mode="after" 的用法，return self（不是 Self！），raise ValueError（不是 ValidationError！） -->

```python
from pydantic import model_validator
from typing import Self

@model_validator(mode="after")
def check_ext(self) -> Self:
    ext_map = {".py": "python", ".js": "javascript"}
    for ext, lang in ext_map.items():
    	if self.file_path.endswith(ext) and self.language != lang:
            raise ValueError(f"文件拓展名{ext}与设置语言{self.language}不符，应为{lang}")
    return self
           
# model_validator 是进行多字段联合校验使用的装饰器，可以同时对多个字段进行约束
# mode="after": 指的是这个校验操作在实例创建之后，可以直接操作实例对象获取属性，self.something
# mode="before": 指的是在实例创建之前，还是数据字典的时候进行校验，此时我们可以对传入的数据字典进行修改，但是无法使用 self 获取属性
  
```

---

# 七、computed_field

<!-- 解释：派生字段，自动计算，不出现在构造参数中，但 dump 时可见 -->

派生字段是指在数据类中我们可以通过其他属性计算得出的属性字段，为了保证数据一致性，我们一般不会再去单独存储这样的字段，往往是通过计算得出，所以在构造函数中不显式传入，但是我们序列化之后是可以看到这样的派生字段的。

---

# 八、今日踩坑记录

> 以下 5 个错误来自今天的练习题，已给出「错在哪」和「正确做法」。
> 请在每条后面的 `修正：` 行用自己的话总结一遍（加深记忆）。


### 错误 1：`@property` 和 `@computed_field` 装饰器顺序反了

**错在哪**：把 `@property` 放在 `@computed_field` 上面（外层），装饰器从下向上执行，`@computed_field` 先拿到的是已经被 `@property` 处理过的 property descriptor，不是原始函数，导致运行时错误。正确写法是 `@computed_field` 直接装饰方法，不需要 `@property`。
```python
# 错
@property
@computed_field
def char_count(self) -> int: ...

# 对
@computed_field
def char_count(self) -> int: ...
```
修正：装饰器是要注重执行顺序的，执行顺序不同，可能会导致报错，因为每一个装饰器函数的返回类型不同


### 错误 2：`return Self` 写成了类型，不是实例

**错在哪**：`Self`（大写 S）是 `typing.Self`，代表「当前类」这个类型，用于类型注解。`self`（小写 s）才是实例对象。`model_validator` 方法必须返回实例，写 `return Self` 返回的是一个 type 对象，不是数据。
```python
# 错
def check_ext(self) -> Self:
    ...
    return Self

# 对
def check_ext(self) -> Self:
    ...
    return self
```
修正：返回的时候一定要返回的是对象，而不是类型


### 错误 3：`model_validator` 里直接 `raise ValidationError`

**错在哪**：`ValidationError` 是 pydantic 内部构造的错误格式，不接收裸字符串。在 `model_validator` 里应该抛 `ValueError`，pydantic 会自动把它包装成 `ValidationError`。
```python
# 错
raise ValidationError("文件后缀和语言不匹配")

# 对
raise ValueError("文件后缀和语言不匹配")
```
修正：在 model_validator 中抛出错误要抛出 ValueError。


### 错误 4：类型注解少冒号，`=` 当 `:` 用

**错在哪**：类属性声明 `x: str = "a"` 里，`:` 是类型注解，`=` 是默认值，两者作用完全不同。写成 `x = Literal[...] = Field(...)` 会触发 `SyntaxError: cannot assign to function call`，因为链式赋值试图把值赋给 `Literal[...]` 这个函数调用表达式。
```python
# 错
review_level = Literal["low", "medium", "high"] = Field(default="medium")

# 对
review_level: Literal["low", "medium", "high"] = "medium"
```
修正：注意类型注解使用 ":"，不过这个问题一般会被 IDE 直接发现就是了


---

*笔记整理于 2026-06-26*
