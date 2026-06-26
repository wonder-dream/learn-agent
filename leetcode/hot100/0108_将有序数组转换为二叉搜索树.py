# 108. 将有序数组转换为二叉搜索树 (Convert Sorted Array to BST)
# 难度：简单
# 分类：二叉树
# https://leetcode.cn/problems/convert-sorted-array-to-bst/

"""
将升序数组转换为一棵平衡二叉搜索树。
"""

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        """将有序数组转换为平衡二叉搜索树。"""
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
