# 199. 二叉树的右视图 (Binary Tree Right Side View)
# 难度：中等
# 分类：二叉树
# https://leetcode.cn/problems/binary-tree-right-side-view/

"""
返回从右侧所能看到的节点值（从顶到底）。
"""

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """返回二叉树的右视图。"""
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
