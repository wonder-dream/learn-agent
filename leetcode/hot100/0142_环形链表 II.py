# 142. 环形链表 II (Linked List Cycle II)
# 难度：中等
# 分类：链表
# https://leetcode.cn/problems/linked-list-cycle-ii/

"""
返回链表开始入环的第一个节点。如果链表无环，则返回 null。
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode | None:
        """返回链表开始入环的第一个节点，无环返回 None。"""
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
