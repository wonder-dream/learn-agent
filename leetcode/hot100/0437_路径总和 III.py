# 437. 路径总和 III (Path Sum III)
# 难度：中等
# 分类：二叉树
# https://leetcode.cn/problems/path-sum-iii/

"""
求二叉树里节点值之和等于 targetSum 的路径的数目。路径方向必须向下。
"""

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        """返回路径和等于 targetSum 的路径数目。"""
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
