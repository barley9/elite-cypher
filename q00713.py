"""
713. Subarray Product Less Than K

Given an array of integers `nums` and an integer `k`, return the number of
contiguous subarrays where the product of all the elements in the subarray is
strictly less than `k`.
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """O(n^3) time, O(n) space solution. Much too slow."""
        from math import prod

        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if prod(nums[i:j]) < k:
                    result += 1

        return result

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """O(n^2) time, O(1) space solution. Still much too slow."""
        result = 0
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                if prod < k:
                    result += 1
                else:
                    break
        return result

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """Sliding window implementation"""
        pass