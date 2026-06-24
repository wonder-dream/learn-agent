# 1
print([x ** 2 for x in range(1, 21) if x % 2 == 0])

# 2(不知道capitalize()的用法)
# words = ["apple", "Banana", "cherry", "Date"]
# print([(word.upper(), len(word)) for word in words])

# 2
words = ["apple", "Banana", "cherry", "Date"]
print([(word.capitalize(), len(word)) for word in words])

# 3
nums = [12, 5, 8, 130, 25, 44, 3, 77]
print([x for x in nums if x % 4 == 0 and x % 8 != 0])

# 4
s = "a1b2c3d4e5"
print([x for x in s if x.isdigit()])

# 5
print([[(x + y) for x in range(5)] for y in range(5)])

# 6(二维数组是[x][y]不是[x, y])
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([[x for x in matrix[y, range(3)]] for y in range(3)])

# 6
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([[matrix[x][y] for x in range(3)] for y in range(3)])

# 7
keys = ["a", "b", "c", "d"]
vals = [1, 2, 3, 4]
print({keys[v-1]:v for v in vals if v > 2})

# 8(不知道还有split()可以做到分割单词)
# text = "hello world hello python"
# print({word for word in text})

# 8
text = "hello world hello python"
print({word for word in text.split() if len(word) > 4})

# 9
s = "PythonProgramming"
print(s[-5:-1])

# 10
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::-1])

# 11(数组拼接使用+运算符)
nums = [1, 2, 3, 4, 5, 6]
print(nums[::2] + nums[1::2])

# 12
words = ["hello", "world", "python", "list", "comprehension"]
print([word.upper()[0:3] for word in words if len(word) >= 5])

# def chunk_list(lst, n):
#     start = 0
#     end = start + n
#     ans = []
#     while(start < len(lst)):
#         ans.append(lst[start:end])
#         start = end
#         end = start + n
#     return ans

def chunk_list(lst, n):
    # lst[i:i+n]表示从索引i开始，取n个元素，如果超出范围自动截断到列表末尾
    # range(0, len(lst), n)表示i的取值范围从0开始最大到lst的长度-1(因为range函数前闭后开)步长为n，也就是中间跳过n个取下一个i
    # 列表推导式是更加简洁和Pythonic的方法
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))

def filter_and_map(lst):
    return [word.upper() for word in lst.split()]

print(filter_and_map("hello world hello python 123"))

# def count_words(text: str) -> dict[str, int]:
#     words = text.split()
#     ans = {}
#     for word in words:
#         if ans.get(word, 0) == 0:
#             ans[word] = 1
#         else:
#             ans[word] += 1
#     return ans

# def count_words(text: str) -> dict[str, int]:
#     words = text.split()
#     ans = {}
#     for word in words:
#         ans[word] = ans.get(word, 0) + 1
#     return ans

import collections
def count_words(text: str) -> dict[str, int]:
    return dict(collections.Counter(text.split()))

print(count_words("hello world hello python"))
    
    
def process_logs(logs: list[str]) -> dict:
    ans = {}
    levels = [log.split(" ")[1] for log in logs]
    ans["error_count"] = levels.count("ERROR")
    ans["info_count"] = levels.count("INFO")
    ans["errors"] = [{"date": log.split(" ")[0], "message": log.split(" ", 2)[2]} for log in logs if log.split(" ")[1] == "ERROR"]
    ans["first_error_time"] = ans["errors"][0]["date"] if ans["error_count"] > 0 else None
    return ans

print(process_logs(["2024-06-23 ERROR connection timeout",
                    "2024-06-24 INFO request processed",
                    "2024-06-25 ERROR disk full"]))

print([[x for x in range(10)] for y in range(10)])

d = {"a": 1, "b": 2}
print(list(d))