"""
3691. Maximum Total Subarray Value II

You are given an integer array `nums` of length `n` and an integer `k`.

You must select exactly `k` distinct `nums[l..r]` of `nums`. Subarrays may
overlap, but the exact same subarray (same `l` and `r`) cannot be chosen more
than once.

The value of a subarray `nums[l..r]` is defined as:
`max(nums[l..r]) - min(nums[l..r])`.

The total value is the sum of the values of all chosen subarrays.

Return the maximum possible total value you can achieve.
"""

import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        """TOO SLOW"""
        values = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                # print(
                #     [i, j],
                #     nums[i:j],
                #     max(nums[i:j]),
                #     min(nums[i:j]),
                #     max(nums[i:j]) - min(nums[i:j])
                # )
                heapq.heappush_max(
                    values,
                    max(nums[i:j]) - min(nums[i:j])
                )
        
        return sum(
            heapq.heappop_max(values)
            for _ in range(k)
        )

    @staticmethod
    def min_max_indices(arr: List[int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        Returns a tuple of tuples containing the minimum and maximum values in
        `arr` as well as their indices: (min_idx, min_val), (max_idx, max_val)
        """
        ni, xi = 0, 0  # min_index, max_index
        nv, xv = arr[ni], arr[xi]  # min_value, max_value
        for i in range(len(arr)):
            if arr[i] < nv:
                ni, nv = i, arr[i]
            if arr[i] > xv:
                xi, xv = i, arr[i]
        return ((ni, nv), (xi, xv))

    def maxTotalValue(self, nums: List[int], k: int) -> int:
        (min_idx, _), (max_idx, _) = self.min_max_indices(nums)

        num_maxval_intervals = (min(min_idx, max_idx) + 1) * (len(nums) - max(min_idx, max_idx))

        print(nums[min_idx], nums[max_idx], num_maxval_intervals)

        if num_maxval_intervals >= k:
            return k * (nums[max_idx] - nums[min_idx])