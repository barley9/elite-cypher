"""
3423. Maximum Difference Between Adjacent Elements in a Circular Array

Given a circular array `nums`, find the maximum absolute difference between
adjacent elements.

Note: In a circular array, the first and last elements are adjacent.
"""

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        """O(n) time, O(1) space solution"""
        max_diff = -10 ** 7  # negative infinity
        for i in range(len(nums)):
            d = abs(nums[i] - nums[i - 1])
            if d > max_diff:
                max_diff = d
        return max_diff