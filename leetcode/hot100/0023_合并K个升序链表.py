# 23. 合并K个升序链表 (Merge k Sorted Lists)
# 难度：困难
# 分类：链表
# https://leetcode.cn/problems/merge-k-sorted-lists/

"""
合并 k 个升序链表为一个升序链表。
"""

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """合并 k 个升序链表。"""
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
