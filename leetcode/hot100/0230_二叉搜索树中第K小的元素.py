# 230. 二叉搜索树中第K小的元素 (Kth Smallest Element in a BST)
# 难度：中等
# 分类：二叉树
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

"""
查找二叉搜索树中第 k 小的元素（从 1 开始计数）。
"""

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """返回二叉搜索树中第 k 小的元素。"""
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
