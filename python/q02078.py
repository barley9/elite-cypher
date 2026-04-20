"""
2078. Two Furthest Houses With Different Colors

There are `n` houses evenly lined up on the street, and each house is
beautifully painted. You are given a 0-indexed integer array `colors` of
length `n`, where `colors[i]` represents the color of the `i`th house.

Return the maximum distance between two houses with different colors.

The distance between the `i`th and `j`th houses is `abs(i - j)`, where `abs(x)`
is the absolute value of `x`.
"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """O(n^2) time, O(1) space solution"""
        max_dist = 0
        for i in range(len(colors) - 1):
            for j in range(i + 1, len(colors)):
                if (colors[i] != colors[j]) and (j - i > max_dist):
                    max_dist = j - i
        return max_dist

    def maxDistance(self, colors: List[int]) -> int:
        """O(2n) time, O(1) space solution"""
        n = len(colors)
        max_dist = 0
        
        # Search from left
        for i in range(n):
            if colors[i] != colors[-1]:
                max_dist = n - i - 1
                break
        
        # Search from right
        for i in range(n - 1, -1, -1):
            if (colors[0] != colors[i]) and (i > max_dist):
                max_dist = i
                break

        return max_dist