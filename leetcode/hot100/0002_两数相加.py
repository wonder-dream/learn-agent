# 2. 两数相加 (Add Two Numbers)
# 难度：中等
# 分类：链表
# https://leetcode.cn/problems/add-two-numbers/

"""
两个非空链表表示两个非负整数，每位数字逆序存储。将两数相加并以链表形式返回。
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """返回表示两数之和的链表。"""
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
