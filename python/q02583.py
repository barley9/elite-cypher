"""
2583. Kth Largest Sum in a Binary Tree

You are given the `root` of a binary tree and a positive integer `k`.

The level sum in the tree is the sum of the values of the nodes that are on the
same level.

Return the `k`th largest level sum in the tree (not necessarily distinct). If
there are fewer than `k` levels in the tree, return `-1`.

Note that two nodes are on the same level if they have the same distance from
the root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def level_sum(self, root, depth=0, depth_sums=[]):
        """
        Helper function. Mutates `depth_sums` list to contain the level sums of
        the binary tree `root`. O(n) time, O(n) space DFS recursive algorithm.
        """
        # Add space to end of `depth_sums` if too short
        if len(depth_sums) < depth + 1:
            depth_sums.extend([0] * (depth - len(depth_sums) + 1))
        
        depth_sums[depth] += root.val
        
        if root.left:
            self.level_sum(root.left,  depth=depth + 1, depth_sums=depth_sums)
        if root.right:
            self.level_sum(root.right, depth=depth + 1, depth_sums=depth_sums)

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """O(n log n) time, O(n) space recursive solution."""
        level_sums = []

        # Mutate list to contain level sums
        self.level_sum(root=root, depth_sums=level_sums)
        
        # Return `k`th largest sum, if possible
        if len(level_sums) < k:
            return -1
        else:
            return sorted(level_sums)[-k]  # O(n log n)