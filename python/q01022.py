"""
1022. Sum of Root To Leaf Binary Numbers

You are given the `root` of a binary tree where each node has a value `0` or
`1`. Each root-to-leaf path represents a binary number starting with the most
significant bit.

For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent
`01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from
the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ord0 = ord('0')

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        O(n) time, O(n * 2^n) space solution
        
        Since there's no penalty for destroying the tree, mutate `val` to be
        a list of all values in node's parents.
        """
        if isinstance(root.val, int):
            root.val = [root.val]
            
        total = 0

        if root.left:
            root.left.val = root.val + [root.left.val]
            total += self.sumRootToLeaf(root.left)

        if root.right:
            root.right.val = root.val + [root.right.val]
            total += self.sumRootToLeaf(root.right)

        if (not root.left) and (not root.right):
            total += int(''.join(
                chr(v + self.ord0)
                for v in root.val
            ), 2)

            # total += sum(
            #     d << k
            #     for k, d in enumerate(reversed(root.val))
            # )

            # total += sum(
            #     d << (len(root.val) - k - 1)
            #     for k, d in enumerate(root.val)
            # )
        
        return total