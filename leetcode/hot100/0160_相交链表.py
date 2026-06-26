# 160. 相交链表 (Intersection of Two Linked Lists)
# 难度：简单
# 分类：链表
# https://leetcode.cn/problems/intersection-of-two-linked-lists/

"""
给你两个单链表的头节点 headA 和 headB，找出并返回两个单链表相交的起始节点。
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """返回两个单链表相交的起始节点，不相交则返回 None。"""
        pass


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


if __name__ == "__main__":
    s = Solution()
    # 在此写本地测试用例
    pass
