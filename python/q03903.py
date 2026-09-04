"""
3903. Smallest Stable Index I

You are given an integer array `nums` of length `n` and an integer `k`.

For each index `i`, define its instability score as
`max(nums[0..i]) - min(nums[i..n - 1])`.

In other words:
    `max(nums[0..i])` is the largest value among the elements from index `0` to
        index `i`.
    `min(nums[i..n - 1])` is the smallest value among the elements from index
        `i` to index `n - 1`.

An index `i` is called stable if its instability score is less than or equal to
`k`.

Return the smallest stable index. If no such index exists, return `-1`.
"""

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        """O(3n) time, O(2n) space solution"""
        INF = 10 ** 10  # infinity

        # Pre-compute prefix/postfix maximum/minimum value arrays
        max_so_far = -INF
        post_max = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > max_so_far:
                max_so_far = nums[i]
            post_max[i] = max_so_far
        
        min_so_far = INF
        pre_min = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < min_so_far:
                min_so_far = nums[i]
            pre_min[i] = min_so_far

        # Search for first "stable" array index
        for i in range(len(nums)):
            if post_max[i] - pre_min[i] <= k:
                return i
        
        return -1