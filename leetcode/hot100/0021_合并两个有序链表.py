# 21. 合并两个有序链表 (Merge Two Sorted Lists)
# 难度：简单
# 分类：链表
# https://leetcode.cn/problems/merge-two-sorted-lists/

"""
将两个升序链表合并为一个新的升序链表并返回。
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
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """合并两个升序链表为一个新的升序链表。"""
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    # 在此写本地测试用例
    pass
