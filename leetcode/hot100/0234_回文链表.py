# 234. 回文链表 (Palindrome Linked List)
# 难度：简单
# 分类：链表
# https://leetcode.cn/problems/palindrome-linked-list/

"""
给你一个单链表的头节点 head，请你判断该链表是否为回文链表。
"""


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


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """判断链表是否为回文链表。"""
        if head is None:
            return False

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        midd = self.reverse_linked(slow)

        while midd and head:
            if midd.val != head.val:
                return False
            midd = midd.next
            head = head.next

        return True


if __name__ == "__main__":
    s = Solution()
    # 在此写本地测试用例
    pass
