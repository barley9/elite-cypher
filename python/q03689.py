"""
3689. Maximum Total Subarray Value I

You are given an integer array `nums` of length `n` and an integer `k`.

You need to choose exactly `k` non-empty subarrays `nums[l..r]` of nums.
Subarrays may overlap, and the exact same subarray (same l and r) can be chosen
more than once.

The value of a subarray `nums[l..r]` is defined as:
`max(nums[l..r]) - min(nums[l..r])`.

The total value is the sum of the values of all chosen subarrays.

Return the maximum possible total value you can achieve.
"""

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        """O(2n) time, O(1) space solution"""
        return k * (max(nums) - min(nums))

    def maxTotalValue(self, nums: List[int], k: int) -> int:
        """O(n) time, O(1) space solution"""
        minimum = 10 ** 10
        maximum = -1
        for n in nums:
            if n > maximum:
                maximum = n
            if n < minimum:
                minimum = n
        return k * (maximum - minimum)