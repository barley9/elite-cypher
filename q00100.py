"""
100. Same Tree

Given the roots of two binary trees `p` and `q`, write a function to check if
they are the same or not.

Two binary trees are considered the same if they are structurally identical, and
the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursively checks sub-trees for equivalence. This solution is `O(n)`
        time, where `n` is the number of nodes in the smaller tree (we only need
        to fully traverse the smaller tree). This solution is `O(h)` space,
        where `h` is the height of the smallest tree (for the same reasons).
        """
        if isinstance(p, TreeNode) and isinstance(q, TreeNode):
            return p.val == q.val and \
                   self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right, q.right)
        else:
            return p is None and q is None