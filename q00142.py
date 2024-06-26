"""
142. Linked List Cycle II

Given the `head` of a linked list, return the node where the cycle begins. If
there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the `next` pointer. Internally, `pos` is
used to denote the index of the node that tail's `next` pointer is connected to
(0-indexed). It is `-1` if there is no cycle. Note that pos is not passed as a
parameter.

Do not modify the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(n) time, O(n) space solution using hash table to store nodes already
        encountered.
        """
        if not head:
            return None

        seen = set()
        while head.next:
            if head.next in seen:
                return head.next
            seen.add(head)
            head = head.next