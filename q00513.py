"""
513. Find Bottom Left Tree Value

Given the `root` of a binary tree, return the leftmost value in the last row of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bot_left_rec(self, root, depth=0) -> tuple:
        if root.left is None and root.right is None:
            # print("  " * depth, (depth, root.val))
            return (depth, root.val)
        else:
            bleft = bright = (-1, -1)
            if root.left:
                bleft = self.bot_left_rec(root.left, depth + 1)
            if root.right:
                bright = self.bot_left_rec(root.right, depth + 1)
            
            # print("  " * depth, bright if bleft[0] < bright[0] else bleft)
            return bright if bleft[0] < bright[0] else bleft

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.bot_left_rec(root)[1]