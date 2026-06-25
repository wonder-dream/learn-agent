import os


# lst = [
#     {"name": "Alice", "age": 30, "city": "New York"},
#     {"name": "Bob", "age": 25, "city": "Los Angeles"},
#     {"name": "Charlie", "age": 35, "city": "Chicago"},
#     {"name": "David", "age": 40, "city": "Houston"}
# ]

# print(sorted(lst, key=lambda p: p["age"]))

# def merge_configs(*dicts) -> dict:
#     merged = {}
#     for dict in dicts:
#         merged = {**merged, **dict}
#     return merged


# def merge_configs(*dicts) -> dict:
#     merged = {}
#     for dict in dicts:
#         merged = merged | dict
#     return merged

# def merge_configs(*dicts) -> dict:
#     return {k: v for d in dicts for k, v in d.items()}

# with open("./data.txt", "r", encoding="utf-8") as f:
#     print(f.read())
    
# with open("./data.txt", "w", encoding="utf-8") as f:
#     f.write("hello world!\n")

# def process(line):
#     print(line.strip())
    
# with open("./data.txt") as f:
#     for line in f:
#         process(line)

config_dir = os.path.dirname(__file__)

# def parse_config(path: str) -> dict:
#     config = {}
#     with open(os.path.join(config_dir, path), "r", encoding="utf-8") as f:
#         for line in f:
#             line = line.strip()
#             if line and not line.startswith("#"):
#                 config[line.split("=", 1)[0]] = line.split("=", 1)[1]
#     return config
        
# print(parse_config("config.txt"))

# 1
users = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
print(sorted(users, key=lambda u: u[1]))

# 2
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 72},
]
print(sorted(students, key=lambda s: s["score"], reverse=True))

# 3
nums = [1, 2, 3, 4, 5]
print(list(map(str, nums)))

# 4
data = [1, 2, 3, 4, 5]
head, *tail = data
print(head, tail)

# 5
data = [10, 20, 30, 40, 50, 60]
first, *middle, last = data
print(first, middle, last)

# 6
def merge_configs(*dicts):
    return {k: v for d in dicts for k, v in d.items()}
c1 = {"host": "localhost", "port": 8000}
c2 = {"port": 9000, "debug": True}
c3 = {"debug": False, "workers": 4}
print(merge_configs(c1, c2, c3))

# 7
lines = ["def hello():", "    print('hi')", "    return 42"]
for index, line in enumerate(lines):
    print(f"L{index+1}: {line}")
    
# 8
names = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 72]
for name, score in zip(names, scores):
    print(f"{name} -> {score}")

# 9
keys = ["name", "age", "city"]
vals = ["Alice", 25, "Beijing"]
print({k: v for k, v in zip(keys, vals)})

# 10
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

# 11
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@uppercase_result
def greet(name):
    return f"hello {name}"
print(greet("Alice"))

# 12
with open("./data.txt") as f:
    line_number = 0
    for line in f:
        line_number += 1
    print(line_number)
    
# 13
lines = ["第1行", "第2行", "第三行"]
with open("./output.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
        f.flush()
        
# 14
def parse_config(path: str) -> dict:
    config = {}
    with open(os.path.join(config_dir, path), "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                config[line.split("=", 1)[0]] = line.split("=", 1)[1]
    return config

# 15
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(dict(map(lambda x: (x, x**2), filter(lambda x: x % 2 == 0, nums))))