# 98. 验证二叉搜索树 (Validate Binary Search Tree)
# 难度：中等
# 分类：二叉树
# https://leetcode.cn/problems/validate-binary-search-tree/

"""
判断二叉树是否是一个有效的二叉搜索树。
"""

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """返回二叉树是否为有效的二叉搜索树。"""
        pass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    s = Solution()
    # 在此写本地测试用例
    pass
