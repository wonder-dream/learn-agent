# 24. 两两交换链表中的节点 (Swap Nodes in Pairs)
# 难度：中等
# 分类：链表
# https://leetcode.cn/problems/swap-nodes-in-pairs/

"""
两两交换其中相邻的节点，并返回交换后链表的头节点。只能进行节点交换。
"""

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        """两两交换相邻节点并返回头节点。"""
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
