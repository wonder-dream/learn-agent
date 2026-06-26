# 105. 从前序与中序遍历序列构造二叉树 (Construct Binary Tree)
# 难度：中等
# 分类：二叉树
# https://leetcode.cn/problems/construct-binary-tree/

"""
给定前序遍历和中序遍历，构造二叉树并返回其根节点。
"""

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """从前序和中序遍历序列构造二叉树。"""
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
