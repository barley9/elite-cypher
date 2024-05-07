"""
2816. Double a Number Represented as a Linked List

You are given the `head` of a non-empty linked list representing a non-negative
integer without leading zeroes.

Return the `head` of the linked list after doubling it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _doubleItRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(n) time, O(n) space (because of stack space) recursive solution"""
        if head.next:
            carry = self._doubleItRec(head.next)
        else:
            carry = ListNode(val=0)
        q, r = divmod(2 * head.val + carry.val, 10)
        head.val = r
        return ListNode(val=q, next=head)

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = self._doubleItRec(head)  # all the real work happens here

        # Post-processing to remove leading zeros (TODO: find a way to avoid this?)
        while result.val == 0 and result.next:
            result = result.next
        return result

class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            q, r = divmod(2 * curr.val, 10)
            
            if not q:
                curr.val = r
            elif prev:
                curr.val = r
                prev.val += q
            else:
                head = ListNode(val=q, next=head)
                curr.val = r

            prev = curr
            curr = curr.next

        return head