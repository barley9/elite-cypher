"""
2265. Count Nodes Equal to Average of Subtree

Given the `root` of a binary tree, return the number of nodes where the value
of the node is equal to the average of the values in its subtree.

Note:
    The average of `n` elements is the sum of the `n` elements divided by `n`
        and rounded down to the nearest integer.
    A subtree of `root` is a tree consisting of `root` and all of its
        descendants.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    @staticmethod
    def dfs_count(root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + Solution.dfs_count(root.left) + Solution.dfs_count(root.right)

    @staticmethod
    def dfs_sum(root: TreeNode) -> int:
        if root is None:
            return 0

        return root.val + Solution.dfs_sum(root.left) + Solution.dfs_sum(root.right)

    @staticmethod
    def dfs_count_equal(root: TreeNode) -> Tuple[int, int, int]:
        """Returns (population, sum, count_equal) for subtree"""
        if root is None:
            return (0, 0, 0)

        left  = Solution.dfs_count_equal(root.left)
        right = Solution.dfs_count_equal(root.right)

        pop = 1 + left[0] + right[0]
        tot = root.val + left[1] + right[1]
        eq = ((tot // pop) == root.val)

        return (
            pop,
            tot,
            eq + left[2] + right[2]
        )

    def averageOfSubtree(self, root: TreeNode) -> int:
        """scratchwork"""
        # count number of nodes in subtree
        print(self.dfs_count(root))

        # compute sum of values in subtree
        print(self.dfs_sum(root))

        # compute average value of subtree
        print(self.dfs_sum(root) // self.dfs_count(root), root.val)

        # check if equal to root node value
        # total up all truthy nodes
        print(self.dfs_count_equal(root))

        return self.dfs_count_equal(root)[2]

    def averageOfSubtree(self, root: TreeNode) -> int:
        """O(n) time, O(n) space solution"""
        return self.dfs_count_equal(root)[2]

    def averageOfSubtree(self, root: TreeNode) -> int:
        """O(n) time, O(n) space solution"""
        global result
        result = 0  # value will be mutated by recursive dfs() calls
        
        def dfs(root: TreeNode) -> Tuple[int, int]:
            global result

            if root is None:
                return (0, 0)
            
            left  = dfs(root.left)
            right = dfs(root.right)

            pop = 1 + left[0] + right[0]
            tot = root.val + left[1] + right[1]
            result += ((tot // pop) == root.val)

            return (pop, tot)

        dfs(root)
        return result