"""
2095. Delete the Middle Node of a Linked List

You are given the `head` of a linked list. Delete the middle node, and return
the `head` of the modified linked list.

The middle node of a linked list of size `n` is the `floor(n / 2)`th node from
the start using 0-based indexing, where `floor(x)` denotes the largest integer
less than or equal to `x`. E.g. for `n` = `1`, `2`, `3`, `4`, and `5`, the
middle nodes are `0`, `1`, `1`, `2`, and `2`, respectively.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(2n) time, O(1) space solution"""
        if (not head) or (not head.next):
            return None

        # Tranverse LL to calculate size; O(n)
        node = head
        length = 1
        while node.next:
            length += 1
            node = node.next
        
        # Seek to middle node; O(n)
        node = head
        for _ in range(length // 2 - 1):
            node = node.next
        
        # Delete middle node
        node.next = node.next.next

        return head

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(n) time, O(1) space solution"""
        if (not head) or (not head.next):
            return None

        # Traverse LL one node at a time (`slow`) and 2 nodes at a time
        # (`fast`). When `fast` reaches the end of the LL, `slow` must be at
        # the middle.
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Delete middle node
        slow.next = slow.next.next

        return head