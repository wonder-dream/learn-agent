# Python lambda + 解包 + 迭代 + 装饰器 + 文件IO 练习题

> 共 15 题，涵盖 lambda、解包、enumerate/zip、装饰器、with 文件读写。
> 尽量用一行代码完成每道题。

---

## 一、lambda 与高阶函数

### 题目 1
用 `sorted()` + `lambda` 对以下列表按**年龄**升序排序：

```python
users = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
# 期望结果
[("Charlie", 20), ("Alice", 25), ("Bob", 30)]
```

### 题目 2
用 `sorted()` + `lambda` 对以下字典列表按 `"score"` 降序排序：

```python
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 72},
]
# 期望结果：Bob → Alice → Charlie
```

### 题目 3
用一行 `map()` 将以下列表中的所有整数转为字符串：

```python
nums = [1, 2, 3, 4, 5]
# 期望结果
["1", "2", "3", "4", "5"]
```

---

## 二、解包 unpacking

### 题目 4
用星号解包，将列表的第一个元素赋给 `head`，剩余部分赋给 `tail`：

```python
data = [1, 2, 3, 4, 5]
# head → 1
# tail → [2, 3, 4, 5]
```

### 题目 5
用星号解包，从列表中提取**第一个**、**最后一个**元素，其余放入 `middle`：

```python
data = [10, 20, 30, 40, 50, 60]
# first → 10, last → 60, middle → [20, 30, 40, 50]
```

### 题目 6
定义函数 `merge_configs(*dicts)`，合并多个字典，**后面的覆盖前面的**。然后用 3 个配置字典调用测试：

```python
def merge_configs(*dicts):
    # 你的代码（一行即可，用 {**d1, **d2, ...} 的思路）

# 测试
c1 = {"host": "localhost", "port": 8000}
c2 = {"port": 9000, "debug": True}
c3 = {"debug": False, "workers": 4}
# 期望结果
{"host": "localhost", "port": 9000, "debug": False, "workers": 4}
```

---

## 三、enumerate + zip

### 题目 7
用 `enumerate()` 遍历列表，打印格式 `L{行号}: {内容}`（行号从 1 开始）：

```python
lines = ["def hello():", "    print('hi')", "    return 42"]
# 期望打印
# L1: def hello():
# L2:     print('hi')
# L3:     return 42
```

### 题目 8
用 `zip()` 同时遍历两个列表，打印 `{name} → {score}`：

```python
names = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 72]
# 期望打印
# Alice → 88
# Bob → 95
# Charlie → 72
```

### 题目 9
用 `zip()` 将两个列表合并为字典（一行代码）：

```python
keys = ["name", "age", "city"]
vals = ["Alice", 25, "Beijing"]
# 期望结果
{"name": "Alice", "age": 25, "city": "Beijing"}
```

---

## 四、装饰器

### 题目 10
补全下方装饰器 `@time_it`，使其能在函数调用前后打印执行时间（秒）：

```python
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@time_it
def slow_add(a, b):
    time.sleep(0.5)
    return a + b

slow_add(1, 2)
# 期望打印类似
# slow_add took 0.5001s
```

### 题目 11
写一个装饰器 `@uppercase_result`，将函数的返回值转为大写（假设返回值是字符串）：

```python
def uppercase_result(func):
    # 你的代码

@uppercase_result
def greet(name):
    return f"hello, {name}"

print(greet("Alice"))
# 期望结果: "HELLO, ALICE"
```

---

## 五、with 语句 + 文件读写

### 题目 12
用 `with open()` 读取文件，统计**总行数**。假设文件 `data.txt` 存在：

```python
# 写出完整代码，打印行数
```

### 题目 13
用 `with open()` 将以下内容写入文件 `output.txt`（每行一个元素）：

```python
lines = ["第一行", "第二行", "第三行"]
# 写出完整代码
```

---

## 六、综合题

### 题目 14
写一个 `parse_config(path: str) -> dict`：
- 读取配置文件，每行格式 `key=value`
- 忽略空行和 `#` 开头的注释
- 返回字典
- 要求用 `with` + 列表推导式 + 字典推导式 + 解包

```python
# 示例文件内容
# host=localhost
# port=8000
# debug=true
# # this is a comment
# 
# workers=4

# 期望结果
{"host": "localhost", "port": "8000", "debug": "true", "workers": "4"}
```

### 题目 15
用**一行代码**（使用 lambda + map/filter + 解包）实现：

给定列表 `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`，返回一个字典，键为原数字，值为其平方，但**只保留偶数**。

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 期望结果
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

---

*祝练习愉快！*
