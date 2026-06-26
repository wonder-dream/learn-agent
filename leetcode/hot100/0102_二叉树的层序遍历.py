# 102. 二叉树的层序遍历 (Binary Tree Level Order Traversal)
# 难度：中等
# 分类：二叉树
# https://leetcode.cn/problems/binary-tree-level-order-traversal/

"""
返回节点值的层序遍历（逐层从左到右）。
"""

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """返回二叉树的层序遍历结果。"""
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
