"""
1609. Even Odd Tree

A binary tree is named Even-Odd if it meets the following conditions:

    The root of the binary tree is at level index `0`, its children are at level index `1`, their children are at level index `2`, etc.
    For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
    For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

Given the `root` of a binary tree, return `true` if the binary tree is Even-Odd, otherwise return `false`.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeRows(self, root: Optional[TreeNode], rows: list, depth: int=0) -> None:
        """mutates `rows` to contain list of values in each row of tree"""
        if len(rows) <= depth:
            rows.append([])
        
        rows[depth].append(root.val)
        
        if root.left:
            self.treeRows(root.left, rows, depth + 1)
        if root.right:
            self.treeRows(root.right, rows, depth + 1)

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        rows = []
        self.treeRows(root, rows)
        
        for i, row in enumerate(rows):
            odd = bool(i % 2)
            prev = 10 ** 6 + 1 if odd else -(10 ** 6 + 1)
            # print(odd, prev)
            for val in row:
                # odd rows must have even values, and vice versa
                if val % 2 == odd:
                    # print(f"value {val} in row {i} is wrong parity")
                    return False

                if odd:
                    # odd rows must be strictly decreasing
                    if val >= prev:
                        # print(f"value {val} >= {prev} in row {i}")
                        return False
                else:
                    # even rows must be strictly increasing
                    if val <= prev:
                        # print(f"value {val} <= {prev} in row {i}")
                        return False
                
                prev = val
                
        return True