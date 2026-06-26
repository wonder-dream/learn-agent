# 20. 有效的括号 (Valid Parentheses)
# 难度：简单
# 分类：栈
# https://leetcode.cn/problems/valid-parentheses/

"""
判断只包含 '()[]{}' 的字符串是否有效。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """返回括号字符串是否有效。"""
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or stack.pop() != pairs[char]:
                return False

        return not stack


if __name__ == "__main__":
    s = Solution()
    # 在此写本地测试用例
    print(s.isValid("()[]{}"))
