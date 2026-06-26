# 25. K个一组翻转链表 (Reverse Nodes in k-Group)
# 难度：困难
# 分类：链表
# https://leetcode.cn/problems/reverse-nodes-in-k-group/

"""
每 k 个节点一组进行翻转，返回修改后的链表。不足 k 个保持原有顺序。
"""

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """每 k 个节点一组进行翻转。"""
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
