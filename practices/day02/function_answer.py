# ==========================================
# Day02 练习题参考答案
# ==========================================

# 题目 1：sorted + lambda 按年龄排序
users = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
print(sorted(users, key=lambda u: u[1]))

# 题目 2：sorted 按 score 降序
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 72},
]
print(sorted(students, key=lambda s: s["score"], reverse=True))

# 题目 3：map 转字符串
nums = [1, 2, 3, 4, 5]
print(list(map(str, nums)))

# 题目 4：head, *tail 解包
data = [1, 2, 3, 4, 5]
head, *tail = data
print(f"head={head}, tail={tail}")

# 题目 5：first, *middle, last 解包
data = [10, 20, 30, 40, 50, 60]
first, *middle, last = data
print(f"first={first}, last={last}, middle={middle}")

# 题目 6：merge_configs(*dicts)
def merge_configs(*dicts):
    result = {}
    for d in dicts:
        result |= d  # Python 3.9+ 合并运算符
    return result

c1 = {"host": "localhost", "port": 8000}
c2 = {"port": 9000, "debug": True}
c3 = {"debug": False, "workers": 4}
print(merge_configs(c1, c2, c3))

# 一行写法（解包展开到字面量合并）
def merge_configs_oneline(*dicts):
    return {k: v for d in dicts for k, v in d.items()}

print(merge_configs_oneline(c1, c2, c3))

# 题目 7：enumerate 打印行号
lines = ["def hello():", "    print('hi')", "    return 42"]
for i, line in enumerate(lines, start=1):
    print(f"L{i}: {line}")

# 题目 8：zip 同时遍历
names = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 72]
for name, score in zip(names, scores):
    print(f"{name} → {score}")

# 题目 9：zip 合并为字典（一行）
keys = ["name", "age", "city"]
vals = ["Alice", 25, "Beijing"]
print(dict(zip(keys, vals)))

# 题目 10：@time_it 装饰器（已给出，验证运行）
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

print(slow_add(1, 2))

# 题目 11：@uppercase_result 装饰器
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase_result
def greet(name):
    return f"hello, {name}"

print(greet("Alice"))

# 题目 12：统计文件行数
# 先创建一个测试文件
with open("practices/day02/data.txt", "w", encoding="utf-8") as f:
    f.write("line1\nline2\nline3\n")

with open("practices/day02/data.txt", "r", encoding="utf-8") as f:
    line_count = sum(1 for _ in f)
print(f"总行数: {line_count}")

# 题目 13：写入文件
lines = ["第一行", "第二行", "第三行"]
with open("practices/day02/output.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
# 验证写入
with open("practices/day02/output.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 题目 14：parse_config 函数
# 创建示例配置文件
with open("practices/day02/config.txt", "w", encoding="utf-8") as f:
    f.write("host=localhost\n")
    f.write("port=8000\n")
    f.write("debug=true\n")
    f.write("# this is a comment\n")
    f.write("\n")
    f.write("workers=4\n")

def parse_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return dict(line.split("=", 1) for line in lines)

print(parse_config("practices/day02/config.txt"))

# 题目 15：一行代码 — 过滤偶数并生成平方字典
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print({x: x**2 for x in filter(lambda x: x % 2 == 0, nums)})
# 或纯推导式（更推荐）
print({x: x**2 for x in nums if x % 2 == 0})
