"""一次性生成 Hot 100 所有题目的模板文件"""
import os

# 格式: (题号, 中文名, 英文名, 难度, 分类, 描述文本, 方法体, 是否需要链表类, 是否需要树类)
# 描述文本: 题目说明的 docstring
# 方法体: 放在 class Solution 里的代码（包含方法签名和 docstring）

HOT100 = []

def add(num, cn, en, diff, cat, desc, method, link=False, tree=False):
    HOT100.append((num, cn, en, diff, cat, desc, method, link, tree))

# === 哈希 (3) ===
add(1, "两数之和", "Two Sum", "简单", "哈希",
    "给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。",
    '''    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """{}"""
        pass'''.format("给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。"))

add(49, "字母异位词分组", "Group Anagrams", "中等", "哈希",
    "给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。",
    '''    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """给你一个字符串数组，请你将字母异位词组合在一起。"""
        pass''')

add(128, "最长连续序列", "Longest Consecutive Sequence", "中等", "哈希",
    "给定一个未排序的整数数组 nums，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。要求 O(n)。",
    '''    def longestConsecutive(self, nums: list[int]) -> int:
        """给定一个未排序的整数数组 nums，找出数字连续的最长序列的长度。"""
        pass''')

# === 双指针 (4) ===
add(283, "移动零", "Move Zeroes", "简单", "双指针",
    "给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。必须原地操作。",
    '''    def moveZeroes(self, nums: list[int]) -> None:
        """将所有 0 移动到数组的末尾，保持非零元素的相对顺序。"""
        pass''')

add(11, "盛最多水的容器", "Container With Most Water", "中等", "双指针",
    "给定一个长度为 n 的整数数组 height。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。",
    '''    def maxArea(self, height: list[int]) -> int:
        """返回容器可以储存的最大水量。"""
        pass''')

add(15, "三数之和", "3Sum", "中等", "双指针",
    "给你一个整数数组 nums，返回所有和为 0 且不重复的三元组。",
    '''    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """返回所有和为 0 且不重复的三元组。"""
        pass''')

add(42, "接雨水", "Trapping Rain Water", "困难", "双指针",
    "给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。",
    '''    def trap(self, height: list[int]) -> int:
        """返回能接的雨水总量。"""
        pass''')

# === 滑动窗口 (5) ===
add(3, "无重复字符的最长子串", "Longest Substring Without Repeating Characters", "中等", "滑动窗口",
    "给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。",
    '''    def lengthOfLongestSubstring(self, s: str) -> int:
        """返回不含有重复字符的最长子串的长度。"""
        pass''')

add(438, "找到字符串中所有字母异位词", "Find All Anagrams in a String", "中等", "滑动窗口",
    "给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。",
    '''    def findAnagrams(self, s: str, p: str) -> list[int]:
        """返回 s 中所有 p 的异位词的子串的起始索引。"""
        pass''')

add(560, "和为 K 的子数组", "Subarray Sum Equals K", "中等", "滑动窗口",
    "给你一个整数数组 nums 和一个整数 k，请你统计并返回该数组中和为 k 的子数组的个数。",
    '''    def subarraySum(self, nums: list[int], k: int) -> int:
        """返回和为 k 的子数组的个数。"""
        pass''')

add(239, "滑动窗口最大值", "Sliding Window Maximum", "困难", "滑动窗口",
    "给你一个整数数组 nums，有一个大小为 k 的滑动窗口。返回滑动窗口中的最大值。",
    '''    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """返回滑动窗口中的最大值。"""
        pass''')

add(76, "最小覆盖子串", "Minimum Window Substring", "困难", "滑动窗口",
    "给你一个字符串 s、一个字符串 t。返回 s 中涵盖 t 所有字符的最小子串。如果不存在则返回空字符串。",
    '''    def minWindow(self, s: str, t: str) -> str:
        """返回 s 中涵盖 t 所有字符的最小子串。"""
        pass''')

# === 普通数组 (5) ===
add(53, "最大子数组和", "Maximum Subarray", "中等", "普通数组",
    "给你一个整数数组 nums，请你找出一个具有最大和的连续子数组，返回其最大和。",
    '''    def maxSubArray(self, nums: list[int]) -> int:
        """返回最大子数组和。"""
        pass''')

add(56, "合并区间", "Merge Intervals", "中等", "普通数组",
    "以数组 intervals 表示若干个区间的集合，请你合并所有重叠的区间，并返回一个不重叠的区间数组。",
    '''    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """合并所有重叠的区间并返回。"""
        pass''')

add(189, "轮转数组", "Rotate Array", "中等", "普通数组",
    "给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置。",
    '''    def rotate(self, nums: list[int], k: int) -> None:
        """将数组中的元素向右轮转 k 个位置。"""
        pass''')

add(238, "除自身以外数组的乘积", "Product of Array Except Self", "中等", "普通数组",
    "返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。不要使用除法，O(n)。",
    '''    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """返回除自身以外数组的乘积。"""
        pass''')

add(41, "缺失的第一个正数", "First Missing Positive", "困难", "普通数组",
    "给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数。O(n) 且常数空间。",
    '''    def firstMissingPositive(self, nums: list[int]) -> int:
        """返回没有出现的最小的正整数。"""
        pass''')

# === 矩阵 (4) ===
add(73, "矩阵置零", "Set Matrix Zeroes", "中等", "矩阵",
    "给定一个矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。",
    '''    def setZeroes(self, matrix: list[list[int]]) -> None:
        """原地将矩阵中 0 所在行和列的所有元素都设为 0。"""
        pass''')

add(54, "螺旋矩阵", "Spiral Matrix", "中等", "矩阵",
    "给你一个 m 行 n 列的矩阵 matrix，请按照顺时针螺旋顺序，返回矩阵中的所有元素。",
    '''    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """返回顺时针螺旋顺序的矩阵元素。"""
        pass''')

add(48, "旋转图像", "Rotate Image", "中等", "矩阵",
    "给定一个 n×n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。必须原地旋转。",
    '''    def rotate(self, matrix: list[list[int]]) -> None:
        """原地将矩阵顺时针旋转 90 度。"""
        pass''')

add(240, "搜索二维矩阵 II", "Search a 2D Matrix II", "中等", "矩阵",
    "搜索 m×n 矩阵中的目标值。每行从左到右升序，每列从上到下升序。",
    '''    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """返回矩阵中是否存在目标值。"""
        pass''')

# === 链表 (13+1) ===
add(160, "相交链表", "Intersection of Two Linked Lists", "简单", "链表",
    "给你两个单链表的头节点 headA 和 headB，找出并返回两个单链表相交的起始节点。",
    '''    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """返回两个单链表相交的起始节点，不相交则返回 None。"""
        pass''', link=True)

add(206, "反转链表", "Reverse Linked List", "简单", "链表",
    "给你单链表的头节点 head，请你反转链表，并返回反转后的链表。",
    '''    def reverseList(self, head: ListNode) -> ListNode | None:
        """反转链表并返回反转后的链表。"""
        pass''', link=True)

add(234, "回文链表", "Palindrome Linked List", "简单", "链表",
    "给你一个单链表的头节点 head，请你判断该链表是否为回文链表。",
    '''    def isPalindrome(self, head: ListNode) -> bool:
        """判断链表是否为回文链表。"""
        pass''', link=True)

add(141, "环形链表", "Linked List Cycle", "简单", "链表",
    "给你一个链表的头节点 head，判断链表中是否有环。",
    '''    def hasCycle(self, head: ListNode) -> bool:
        """判断链表中是否有环。"""
        pass''', link=True)

add(142, "环形链表 II", "Linked List Cycle II", "中等", "链表",
    "返回链表开始入环的第一个节点。如果链表无环，则返回 null。",
    '''    def detectCycle(self, head: ListNode) -> ListNode | None:
        """返回链表开始入环的第一个节点，无环返回 None。"""
        pass''', link=True)

add(21, "合并两个有序链表", "Merge Two Sorted Lists", "简单", "链表",
    "将两个升序链表合并为一个新的升序链表并返回。",
    '''    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """合并两个升序链表为一个新的升序链表。"""
        pass''', link=True)

add(2, "两数相加", "Add Two Numbers", "中等", "链表",
    "两个非空链表表示两个非负整数，每位数字逆序存储。将两数相加并以链表形式返回。",
    '''    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """返回表示两数之和的链表。"""
        pass''', link=True)

add(19, "删除链表的倒数第N个结点", "Remove Nth Node From End of List", "中等", "链表",
    "删除链表的倒数第 n 个结点，并且返回链表的头结点。",
    '''    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """删除链表的倒数第 n 个结点并返回头结点。"""
        pass''', link=True)

add(24, "两两交换链表中的节点", "Swap Nodes in Pairs", "中等", "链表",
    "两两交换其中相邻的节点，并返回交换后链表的头节点。只能进行节点交换。",
    '''    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        """两两交换相邻节点并返回头节点。"""
        pass''', link=True)

add(25, "K个一组翻转链表", "Reverse Nodes in k-Group", "困难", "链表",
    "每 k 个节点一组进行翻转，返回修改后的链表。不足 k 个保持原有顺序。",
    '''    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """每 k 个节点一组进行翻转。"""
        pass''', link=True)

add(138, "随机链表的复制", "Copy List with Random Pointer", "中等", "链表",
    "每个节点包含一个随机指针 random。构造这个链表的深拷贝。",
    '''    def copyRandomList(self, head: 'Node | None') -> 'Node | None':
        """深拷贝带随机指针的链表。"""
        pass''')

add(148, "排序链表", "Sort List", "中等", "链表",
    "给你链表的头结点 head，请将其按升序排列并返回排序后的链表。",
    '''    def sortList(self, head: ListNode | None) -> ListNode | None:
        """返回升序排列后的链表。"""
        pass''', link=True)

add(23, "合并K个升序链表", "Merge k Sorted Lists", "困难", "链表",
    "合并 k 个升序链表为一个升序链表。",
    '''    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """合并 k 个升序链表。"""
        pass''', link=True)

add(146, "LRU缓存", "LRU Cache", "中等", "链表",
    "实现 LRUCache 类：get(key) 和 put(key, value)，O(1) 时间复杂度。",
    '''    # LRU Cache 是设计题，请在 __main__ 中实现 LRUCache 类
    pass''')

# === 二叉树 (15) ===
add(94, "二叉树的中序遍历", "Binary Tree Inorder Traversal", "简单", "二叉树",
    "给定一个二叉树的根节点 root，返回它的中序遍历。",
    '''    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """返回二叉树的中序遍历结果。"""
        pass''', tree=True)

add(104, "二叉树的最大深度", "Maximum Depth of Binary Tree", "简单", "二叉树",
    "给定一个二叉树 root，返回其最大深度。",
    '''    def maxDepth(self, root: TreeNode | None) -> int:
        """返回二叉树的最大深度。"""
        pass''', tree=True)

add(226, "翻转二叉树", "Invert Binary Tree", "简单", "二叉树",
    "翻转这棵二叉树，并返回其根节点。",
    '''    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """翻转二叉树并返回根节点。"""
        pass''', tree=True)

add(101, "对称二叉树", "Symmetric Tree", "简单", "二叉树",
    "检查二叉树是否轴对称。",
    '''    def isSymmetric(self, root: TreeNode | None) -> bool:
        """返回二叉树是否轴对称。"""
        pass''', tree=True)

add(543, "二叉树的直径", "Diameter of Binary Tree", "简单", "二叉树",
    "返回该树的直径（任意两个节点之间最长路径的长度）。",
    '''    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """返回二叉树的直径。"""
        pass''', tree=True)

add(102, "二叉树的层序遍历", "Binary Tree Level Order Traversal", "中等", "二叉树",
    "返回节点值的层序遍历（逐层从左到右）。",
    '''    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """返回二叉树的层序遍历结果。"""
        pass''', tree=True)

add(108, "将有序数组转换为二叉搜索树", "Convert Sorted Array to BST", "简单", "二叉树",
    "将升序数组转换为一棵平衡二叉搜索树。",
    '''    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        """将有序数组转换为平衡二叉搜索树。"""
        pass''', tree=True)

add(98, "验证二叉搜索树", "Validate Binary Search Tree", "中等", "二叉树",
    "判断二叉树是否是一个有效的二叉搜索树。",
    '''    def isValidBST(self, root: TreeNode | None) -> bool:
        """返回二叉树是否为有效的二叉搜索树。"""
        pass''', tree=True)

add(230, "二叉搜索树中第K小的元素", "Kth Smallest Element in a BST", "中等", "二叉树",
    "查找二叉搜索树中第 k 小的元素（从 1 开始计数）。",
    '''    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """返回二叉搜索树中第 k 小的元素。"""
        pass''', tree=True)

add(199, "二叉树的右视图", "Binary Tree Right Side View", "中等", "二叉树",
    "返回从右侧所能看到的节点值（从顶到底）。",
    '''    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """返回二叉树的右视图。"""
        pass''', tree=True)

add(114, "二叉树展开为链表", "Flatten Binary Tree to Linked List", "中等", "二叉树",
    "将二叉树展开为单链表（right 指针指向下一个节点，left 设为 null）。",
    '''    def flatten(self, root: TreeNode | None) -> None:
        """原地将二叉树展开为链表。"""
        pass''', tree=True)

add(105, "从前序与中序遍历序列构造二叉树", "Construct Binary Tree", "中等", "二叉树",
    "给定前序遍历和中序遍历，构造二叉树并返回其根节点。",
    '''    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """从前序和中序遍历序列构造二叉树。"""
        pass''', tree=True)

add(437, "路径总和 III", "Path Sum III", "中等", "二叉树",
    "求二叉树里节点值之和等于 targetSum 的路径的数目。路径方向必须向下。",
    '''    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        """返回路径和等于 targetSum 的路径数目。"""
        pass''', tree=True)

add(236, "二叉树的最近公共祖先", "Lowest Common Ancestor", "中等", "二叉树",
    "找到该树中两个指定节点的最近公共祖先。",
    '''    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """返回两个指定节点的最近公共祖先。"""
        pass''', tree=True)

add(124, "二叉树中的最大路径和", "Binary Tree Maximum Path Sum", "困难", "二叉树",
    "返回二叉树中的最大路径和。路径至少包含一个节点。",
    '''    def maxPathSum(self, root: TreeNode | None) -> int:
        """返回二叉树中的最大路径和。"""
        pass''', tree=True)

# === 图论 (4) ===
add(200, "岛屿数量", "Number of Islands", "中等", "图论",
    "计算由 '1'（陆地）和 '0'（水）组成的二维网格中岛屿的数量。",
    '''    def numIslands(self, grid: list[list[str]]) -> int:
        """返回岛屿数量。"""
        pass''')

add(994, "腐烂的橘子", "Rotting Oranges", "中等", "图论",
    "每分钟腐烂橘子会感染周围新鲜橘子。返回全部腐烂所需最小分钟数，不可能则返回 -1。",
    '''    def orangesRotting(self, grid: list[list[int]]) -> int:
        """返回全部腐烂所需最小分钟数。"""
        pass''')

add(207, "课程表", "Course Schedule", "中等", "图论",
    "给定课程数和先修条件，判断是否可能完成所有课程。",
    '''    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """返回是否可能完成所有课程。"""
        pass''')

add(208, "实现 Trie (前缀树)", "Implement Trie", "中等", "图论",
    "实现 Trie 类：insert(word), search(word), startsWith(prefix)。",
    '''    # Trie 是设计题，请在 __main__ 中实现 Trie 类
    pass''')

# === 回溯 (8) ===
add(46, "全排列", "Permutations", "中等", "回溯",
    "给定一个不含重复数字的数组 nums，返回其所有可能的全排列。",
    '''    def permute(self, nums: list[int]) -> list[list[int]]:
        """返回所有可能的全排列。"""
        pass''')

add(78, "子集", "Subsets", "中等", "回溯",
    "返回数组所有可能的子集（幂集）。解集不能包含重复的子集。",
    '''    def subsets(self, nums: list[int]) -> list[list[int]]:
        """返回所有可能的子集。"""
        pass''')

add(17, "电话号码的字母组合", "Letter Combinations", "中等", "回溯",
    "给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。",
    '''    def letterCombinations(self, digits: str) -> list[str]:
        """返回所有可能的字母组合。"""
        pass''')

add(39, "组合总和", "Combination Sum", "中等", "回溯",
    "找出 candidates 中可以使数字和为目标数 target 的所有不同组合。同一数字可无限重复。",
    '''    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """返回所有和为 target 的组合。"""
        pass''')

add(22, "括号生成", "Generate Parentheses", "中等", "回溯",
    "生成所有可能的并且有效的括号组合。",
    '''    def generateParenthesis(self, n: int) -> list[str]:
        """返回所有可能的有效括号组合。"""
        pass''')

add(79, "单词搜索", "Word Search", "中等", "回溯",
    "给定二维字符网格和一个单词，判断单词是否存在于网格中。",
    '''    def exist(self, board: list[list[str]], word: str) -> bool:
        """返回单词是否存在于网格中。"""
        pass''')

add(131, "分割回文串", "Palindrome Partitioning", "中等", "回溯",
    "将字符串 s 分割成一些子串，使每个子串都是回文串。返回所有可能的分割方案。",
    '''    def partition(self, s: str) -> list[list[str]]:
        """返回所有可能的分割方案。"""
        pass''')

add(51, "N皇后", "N-Queens", "困难", "回溯",
    "返回所有不同的 n 皇后问题的解决方案。",
    '''    def solveNQueens(self, n: int) -> list[list[str]]:
        """返回所有不同的 n 皇后问题的解决方案。"""
        pass''')

# === 二分查找 (6) ===
add(35, "搜索插入位置", "Search Insert Position", "简单", "二分查找",
    "给定排序数组和目标值，返回目标值索引或应插入的位置。",
    '''    def searchInsert(self, nums: list[int], target: int) -> int:
        """返回目标值索引或应插入的位置。"""
        pass''')

add(74, "搜索二维矩阵", "Search a 2D Matrix", "中等", "二分查找",
    "每行升序，每行第一个大于前一行最后一个。判断目标值是否在矩阵中。",
    '''    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """返回目标值是否在矩阵中。"""
        pass''')

add(34, "在排序数组中查找元素的第一个和最后一个位置", "Find First and Last", "中等", "二分查找",
    "找出目标值在排序数组中的开始位置和结束位置。不存在返回 [-1, -1]。",
    '''    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """返回目标值的开始和结束位置。"""
        pass''')

add(33, "搜索旋转排序数组", "Search in Rotated Sorted Array", "中等", "二分查找",
    "在旋转后的升序数组中搜索目标值，返回索引，否则返回 -1。",
    '''    def search(self, nums: list[int], target: int) -> int:
        """返回目标值的索引，不存在返回 -1。"""
        pass''')

add(153, "寻找旋转排序数组中的最小值", "Find Minimum in Rotated Sorted Array", "中等", "二分查找",
    "找出旋转后的升序数组中的最小元素。",
    '''    def findMin(self, nums: list[int]) -> int:
        """返回数组中的最小元素。"""
        pass''')

add(4, "寻找两个正序数组的中位数", "Median of Two Sorted Arrays", "困难", "二分查找",
    "找出两个正序数组的中位数。O(log(m+n))。",
    '''    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """返回两个正序数组的中位数。"""
        pass''')

# === 栈 (5) ===
add(20, "有效的括号", "Valid Parentheses", "简单", "栈",
    "判断只包含 '()[]{}' 的字符串是否有效。",
    '''    def isValid(self, s: str) -> bool:
        """返回括号字符串是否有效。"""
        pass''')

add(155, "最小栈", "Min Stack", "中等", "栈",
    "实现 MinStack 类：push, pop, top, getMin（常数时间）。",
    '''    # MinStack 是设计题，请在 __main__ 中实现 MinStack 类
    pass''')

add(394, "字符串解码", "Decode String", "中等", "栈",
    "编码规则: k[encoded_string]，解码字符串。",
    '''    def decodeString(self, s: str) -> str:
        """返回解码后的字符串。"""
        pass''')

add(739, "每日温度", "Daily Temperatures", "中等", "栈",
    "返回数组 answer，answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。",
    '''    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """返回每天之后出现更高温度的天数。"""
        pass''')

add(84, "柱状图中最大的矩形", "Largest Rectangle in Histogram", "困难", "栈",
    "求在柱状图中能够勾勒出来的矩形的最大面积。",
    '''    def largestRectangleArea(self, heights: list[int]) -> int:
        """返回柱状图中最大矩形面积。"""
        pass''')

# === 堆 (3) ===
add(215, "数组中的第K个最大元素", "Kth Largest Element", "中等", "堆",
    "返回数组中第 k 个最大的元素。",
    '''    def findKthLargest(self, nums: list[int], k: int) -> int:
        """返回第 k 个最大的元素。"""
        pass''')

add(347, "前 K 个高频元素", "Top K Frequent Elements", "中等", "堆",
    "返回其中出现频率前 k 高的元素。",
    '''    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """返回出现频率前 k 高的元素。"""
        pass''')

add(295, "数据流的中位数", "Find Median from Data Stream", "困难", "堆",
    "实现 MedianFinder 类：addNum(num), findMedian()。",
    '''    # MedianFinder 是设计题，请在 __main__ 中实现 MedianFinder 类
    pass''')

# === 贪心 (4) ===
add(121, "买卖股票的最佳时机", "Best Time to Buy and Sell Stock", "简单", "贪心",
    "选择某一天买入，未来某一天卖出。返回最大利润。",
    '''    def maxProfit(self, prices: list[int]) -> int:
        """返回可以获取的最大利润。"""
        pass''')

add(55, "跳跃游戏", "Jump Game", "中等", "贪心",
    "每个元素代表可跳跃的最大长度。判断是否能够到达最后一个下标。",
    '''    def canJump(self, nums: list[int]) -> bool:
        """返回是否能够到达最后一个下标。"""
        pass''')

add(45, "跳跃游戏 II", "Jump Game II", "中等", "贪心",
    "返回到达最后一个位置的最小跳跃次数。",
    '''    def jump(self, nums: list[int]) -> int:
        """返回到达最后位置的最小跳跃次数。"""
        pass''')

add(763, "划分字母区间", "Partition Labels", "中等", "贪心",
    "划分字符串为尽可能多的片段，同一字母最多出现在一个片段中。返回每个片段的长度列表。",
    '''    def partitionLabels(self, s: str) -> list[str]:
        """返回每个片段的长度列表。"""
        pass''')

# === 动态规划 (15) ===
add(70, "爬楼梯", "Climbing Stairs", "简单", "动态规划",
    "每次爬 1 或 2 个台阶。返回爬到楼顶的方法数。",
    '''    def climbStairs(self, n: int) -> int:
        """返回爬到楼顶的方法数。"""
        pass''')

add(118, "杨辉三角", "Pascal's Triangle", "简单", "动态规划",
    "生成杨辉三角的前 numRows 行。",
    '''    def generate(self, numRows: int) -> list[list[int]]:
        """返回杨辉三角的前 numRows 行。"""
        pass''')

add(198, "打家劫舍", "House Robber", "中等", "动态规划",
    "相邻房屋不能同时偷。返回能偷到的最高金额。",
    '''    def rob(self, nums: list[int]) -> int:
        """返回能偷到的最高金额。"""
        pass''')

add(279, "完全平方数", "Perfect Squares", "中等", "动态规划",
    "返回和为 n 的完全平方数的最少数量。",
    '''    def numSquares(self, n: int) -> int:
        """返回和为 n 的完全平方数的最少数量。"""
        pass''')

add(322, "零钱兑换", "Coin Change", "中等", "动态规划",
    "返回可以凑成总金额所需的最少的硬币个数。无法凑成返回 -1。",
    '''    def coinChange(self, coins: list[int], amount: int) -> int:
        """返回凑成总金额的最少硬币数。"""
        pass''')

add(139, "单词拆分", "Word Break", "中等", "动态规划",
    "判断是否可以利用字典中的单词拼接出字符串 s。",
    '''    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """返回是否可以用字典中的单词拼接出 s。"""
        pass''')

add(300, "最长递增子序列", "Longest Increasing Subsequence", "中等", "动态规划",
    "找到其中最长严格递增子序列的长度。",
    '''    def lengthOfLIS(self, nums: list[int]) -> int:
        """返回最长严格递增子序列的长度。"""
        pass''')

add(152, "乘积最大子数组", "Maximum Product Subarray", "中等", "动态规划",
    "找出数组中乘积最大的非空连续子数组，返回其乘积。",
    '''    def maxProduct(self, nums: list[int]) -> int:
        """返回乘积最大子数组的乘积。"""
        pass''')

add(416, "分割等和子集", "Partition Equal Subset Sum", "中等", "动态规划",
    "判断是否可以将数组分割成两个元素和相等的子集。",
    '''    def canPartition(self, nums: list[int]) -> bool:
        """返回是否可以分割成等和子集。"""
        pass''')

add(32, "最长有效括号", "Longest Valid Parentheses", "困难", "动态规划",
    "找出最长有效（格式正确且连续）括号子串的长度。",
    '''    def longestValidParentheses(self, s: str) -> int:
        """返回最长有效括号子串的长度。"""
        pass''')

add(62, "不同路径", "Unique Paths", "中等", "动态规划",
    "机器人位于 m×n 网格左上角，只能向右或向下移动。返回不同路径数。",
    '''    def uniquePaths(self, m: int, n: int) -> int:
        """返回不同的路径数。"""
        pass''')

add(64, "最小路径和", "Minimum Path Sum", "中等", "动态规划",
    "找从网格左上角到右下角的最小路径和。只能向右或向下。",
    '''    def minPathSum(self, grid: list[list[int]]) -> int:
        """返回最小路径和。"""
        pass''')

add(5, "最长回文子串", "Longest Palindromic Substring", "中等", "动态规划",
    "找到字符串 s 中最长的回文子串。",
    '''    def longestPalindrome(self, s: str) -> str:
        """返回最长的回文子串。"""
        pass''')

add(1143, "最长公共子序列", "Longest Common Subsequence", "中等", "动态规划",
    "返回两个字符串的最长公共子序列的长度。",
    '''    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """返回最长公共子序列的长度。"""
        pass''')

add(72, "编辑距离", "Edit Distance", "中等", "动态规划",
    "返回将 word1 转换成 word2 所使用的最少操作数（插入、删除、替换）。",
    '''    def minDistance(self, word1: str, word2: str) -> int:
        """返回编辑距离。"""
        pass''')

# === 技巧 (5) ===
add(136, "只出现一次的数字", "Single Number", "简单", "技巧",
    "除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个元素。线性时间，常数空间。",
    '''    def singleNumber(self, nums: list[int]) -> int:
        """返回只出现一次的数字。"""
        pass''')

add(169, "多数元素", "Majority Element", "简单", "技巧",
    "返回数组中出现次数大于 ⌊n/2⌋ 的元素。",
    '''    def majorityElement(self, nums: list[int]) -> int:
        """返回多数元素。"""
        pass''')

add(75, "颜色分类", "Sort Colors", "中等", "技巧",
    "原地对 0/1/2 排序。不使用库 sort。",
    '''    def sortColors(self, nums: list[int]) -> None:
        """原地对数组按 0/1/2 排序。"""
        pass''')

add(31, "下一个排列", "Next Permutation", "中等", "技巧",
    "原地将数组重新排列为下一个字典序更大的排列。不存在则排为升序。",
    '''    def nextPermutation(self, nums: list[int]) -> None:
        """原地修改为下一个排列。"""
        pass''')

add(287, "寻找重复数", "Find the Duplicate Number", "中等", "技巧",
    "数组有 n+1 个整数，范围 [1, n]。找出唯一的重复数。不修改数组，O(1) 空间。",
    '''    def findDuplicate(self, nums: list[int]) -> int:
        """返回重复的数。"""
        pass''')


LINKED_LIST_CODE = '''
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

    @staticmethod
    def from_list(arr: list) -> "ListNode | None":
        dummy = ListNode()
        cur = dummy
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    @staticmethod
    def to_list(head: "ListNode | None") -> list:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
'''

TREE_CODE = '''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

os.makedirs("leetcode/hot100", exist_ok=True)

for num, cn, en, diff, cat, desc, method, link, tree in HOT100:
    slug = en.lower().replace(" ", "-").replace("'", "").replace("(", "").replace(")", "").replace(",", "")

    lines = [
        f"# {num}. {cn} ({en})",
        f"# 难度：{diff}",
        f"# 分类：{cat}",
        f"# https://leetcode.cn/problems/{slug}/",
        "",
        f'"""',
        f"{desc}",
        f'"""',
        "",
        "class Solution:",
        method,
        "",
    ]
    if link:
        lines.append(LINKED_LIST_CODE)
    if tree:
        lines.append(TREE_CODE)
    lines += [
        "",
        'if __name__ == "__main__":',
        "    s = Solution()",
        "    # 在此写本地测试用例",
        "    pass",
        "",
    ]

    fname = f"leetcode/hot100/{num:04d}_{cn}.py"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

print(f"已生成 {len(HOT100)} 个文件到 leetcode/hot100/")
