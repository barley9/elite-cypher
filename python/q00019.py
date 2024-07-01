"""
19. Remove Nth Node From End of List

Given the `head` of a linked list, remove the `n`th node from the end of the list and return its head.

Definition for singly-linked list.
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Add sentinel to reduce edge cases
        sentinel = ListNode(next=head)

        # Compute length of list
        size = 0
        node = sentinel
        while node.next:
            size += 1
            node = node.next

        # Seek to `n`th element from end...
        node = sentinel
        for _ in range(size - n):
            node = node.next
        
        node.next = node.next.next if node.next else None
        
        return sentinel.next