# 141. 环形链表 (Linked List Cycle)
# 难度：简单
# 分类：链表
# https://leetcode.cn/problems/linked-list-cycle/

"""
给你一个链表的头节点 head，判断链表中是否有环。
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
    def hasCycle(self, head: ListNode) -> bool:
        """判断链表中是否有环。"""
        if head is None:            # 空链表直接返回 False
            return False
        fast = head
        slow = head

        while fast and fast.next:   # 如果 fast 是 None 那么就没有 next 这个属性，所以要先判断 fast 防止报错
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            
        return False


if __name__ == "__main__":
    s = Solution()
    # 在此写本地测试用例
    pass
