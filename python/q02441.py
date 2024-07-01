"""
2441. Largest Positive Integer That Exists With Its Negative

Given an integer array `nums` that does not contain any zeros, find the largest
positive integer `k` such that `-k` also exists in the array.

Return the positive integer `k`. If there is no such integer, return `-1`.
"""

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """O(2N) time, O(N) space solution using set()"""
        nums = set(nums)  # O(N) time to construct set()
        maxn = -1
        for n in nums:
            if -n in nums and abs(n) > maxn:
                maxn = abs(n)
        return maxn
