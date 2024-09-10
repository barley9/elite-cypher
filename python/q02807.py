"""
2807. Insert Greatest Common Divisors in Linked List

Given the head of a linked list `head`, in which each node contains an integer
value.

Between every pair of adjacent nodes, insert a new node with a value equal to
the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that
evenly divides both numbers.
"""

import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(n) time, O(1) space solution"""
        node = head
        while node.next:
            gcd_node = ListNode(
                val=math.gcd(
                    node.val,
                    node.next.val
                ),
                next=node.next,
            )
            node.next = gcd_node
            node = node.next.next  # skip over new GCD node
        return head

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(n) time, O(1) space solution"""
        node = head
        while node.next:
            node.next = ListNode(
                val=math.gcd(node.val, node.next.val),
                next=node.next,
            )
            node = node.next.next  # skip over new GCD node
        return head