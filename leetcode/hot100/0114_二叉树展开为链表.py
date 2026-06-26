# 114. 二叉树展开为链表 (Flatten Binary Tree to Linked List)
# 难度：中等
# 分类：二叉树
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

"""
将二叉树展开为单链表（right 指针指向下一个节点，left 设为 null）。
"""

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """原地将二叉树展开为链表。"""
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
