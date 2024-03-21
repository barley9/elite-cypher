"""
206. Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return the
reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Extract LL into array
        array = []
        while head.next:
            array.append(head)
            head = head.next
        array.append(head)
        
        # Reassemble LL in reverse order
        array[0].next = None
        for i in range(len(array) - 1):
            array[i + 1].next = array[i]

        return array[-1]