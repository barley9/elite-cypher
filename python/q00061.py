"""
61. Rotate List

Given the `head` of a linked list, rotate the list to the right by `k` places.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_length(self, head: Optional[ListNode]) -> int:
        """Returns the number of nodes in a linked list"""
        if not head:
            return 0

        result = 1
        while head.next:
            result += 1
            head = head.next
        return result

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """O(2n) time, O(1) space solution"""

        # If LL is empty, or has size 1, or rotated by 0 places, return LL unchanged
        if (not head) or (not head.next) or (k == 0):
            return head

        # Locate tail node and compute LL length (first pass)
        tail = head
        llen = 1
        while tail.next:
            tail = tail.next
            llen += 1
        
        # Locate node at which to cut LL (second pass)
        cut_after = head
        for _ in range(llen - (k % llen) - 1):
            cut_after = cut_after.next
        
        # Stitch LL pieces back together
        tail.next = head
        head = cut_after.next
        cut_after.next = None

        return head