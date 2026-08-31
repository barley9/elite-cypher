"""
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

A critical point in a linked list is defined as either a local maxima or a
local minima.

A node is a local maxima if the current node has a value strictly greater than
the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than
the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a
previous node and a next node.

Given a linked list `head`, return an array of length 2 containing
`[minDistance, maxDistance]` where `minDistance` is the minimum distance
between any two distinct critical points and `maxDistance` is the maximum
distance between any two distinct critical points. If there are fewer than two
critical points, return `[-1, -1]`.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """O(n) time, O(n) space solution"""
        if (head is None) or (head.next is None) or (head.next.next is None):
            return [-1, -1]

        n0, n1, n2 = head, head.next, head.next.next
        crits = []  # indices of critical points
        idx = 1

        while (n2 is not None):
            if (n0 is not None) and (n1 is not None):
                if ((n1.val > n0.val) and (n1.val > n2.val)):
                    crits.append(idx)
                elif (n1.val < n0.val) and (n1.val < n2.val):
                    crits.append(idx)  # repeated to keep max line length lower
            n0, n1, n2 = n1, n2, n2.next
            idx += 1

        if len(crits) < 2:
            return [-1, -1]
        
        # TODO: We can probably do without this second O(n) itertation
        return [
            min(
                crits[i] - crits[i - 1]
                for i in range(1, len(crits))
            ),
            crits[-1] - crits[0]
        ]