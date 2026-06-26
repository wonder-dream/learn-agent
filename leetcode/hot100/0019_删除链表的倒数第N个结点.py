# 19. 删除链表的倒数第N个结点 (Remove Nth Node From End of List)
# 难度：中等
# 分类：链表
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

"""
删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """删除链表的倒数第 n 个结点并返回头结点。"""
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
