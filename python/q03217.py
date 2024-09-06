"""
3217. Delete Nodes From Linked List Present in Array

You are given an array of integers `nums` and the `head` of a linked list.
Return the `head` of the modified linked list after removing all nodes from the
linked list that have a value that exists in `nums`.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        current = head
        while current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next
        if head.val in nums:
            head = head.next
        return head
