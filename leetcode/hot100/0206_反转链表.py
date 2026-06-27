# 206. 反转链表 (Reverse Linked List)
# 难度：简单
# 分类：链表
# https://leetcode.cn/problems/reverse-linked-list/

"""
给你单链表的头节点 head，请你反转链表，并返回反转后的链表。
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
    def reverseList(self, head: ListNode) -> ListNode | None:
        """反转链表并返回反转后的链表。"""
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return ListNode.to_list(prev)


if __name__ == "__main__":
    s = Solution()
    # 在此写本地测试用例
    print(s.reverseList(ListNode.from_list([1, 2, 3, 4, 5])))
