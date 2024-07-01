"""
1913. Maximum Product Difference Between Two Pairs

The product difference between two pairs `(a, b)` and `(c, d)` is defined as `(a * b) - (c * d)`.

For example, the product difference between `(5, 6)` and `(2, 7)` is `(5 * 6) - (2 * 7) = 16`.

Given an integer array nums, choose four distinct indices `w`, `x`, `y`, and `z` such that the product difference between pairs `(nums[w], nums[x])` and `(nums[y], nums[z])` is maximized.

Return the maximum such product difference.
"""

class Solution:
    INFINITY = 10 ** 7

    def maxProductDifference(self, nums: List[int]) -> int:
        two_max = [-self.INFINITY, -self.INFINITY]
        two_min = [+self.INFINITY, +self.INFINITY]

        for n in nums:
            if n > two_max[0]:
                two_max[1] = two_max[0]
                two_max[0] = n
            elif n > two_max[1]:
                two_max[1] = n

            if n < two_min[0]:
                two_min[1] = two_min[0]
                two_min[0] = n
            elif n < two_min[1]:
                two_min[1] = n
        
        return (two_max[0] * two_max[1]) - (two_min[0] * two_min[1])