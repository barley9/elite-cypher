"""
1669. Merge In Between Linked Lists

You are given two linked lists: `list1` and `list2` of sizes `n` and `m`
respectively.

Remove `list1`'s nodes from the `a`th node to the `b`th node, and put `list2`
in their place.

Build the result list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self,
            list1: ListNode,
            a: int,
            b: int,
            list2: ListNode) -> ListNode:
        """
        This solution is O(m + n) time and O(1) space because we have to
        traverse all of `list2` and, in the worst case [i.e. when
        `b == len(list1) - 1`], we have to traverse all of `list1` as well.
        """
        # seek to node at index `a`
        node_a = list1
        for _ in range(a - 1):
            node_a = node_a.next
        
        # seek to node at index `b`
        node_b = node_a
        for _ in range(b - a + 2):
            node_b = node_b.next

        # seek to final node of `list2`
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        
        # stitch together the final modified `list1`
        node_a.next = list2
        tail2.next = node_b
        return list1