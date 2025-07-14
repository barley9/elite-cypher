"""
1290. Convert Binary Number in a Linked List to Integer

Given `head` which is a reference node to a singly-linked list. The value of
each node in the linked list is either `0` or `1`. The linked list holds the
binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """INCORRECT; treats value at `head` as LSB"""
        result = head.val
        i = 1
        # print(bin(result))
        while head.next:
            result += head.next.val * (1 << i)
            # print(bin(result))
            head = head.next
            i += 1
        return result

    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = [head.val]
        while head.next:
            result.append(head.next.val)
            head = head.next
        return sum(
            val * 2 ** i
            for i, val in enumerate(reversed(result))
        )
