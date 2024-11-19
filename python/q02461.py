"""
2461. Maximum Sum of Distinct Subarrays With Length K

You are given an integer array `nums` and an integer `k`. Find the maximum
subarray sum of all the subarrays of `nums` that meet the following conditions:
    The length of the subarray is `k`, and
    All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions.
If no subarray meets the conditions, return `0`.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


import collections


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        INFINITY = 10 ** 7
        arr_counts = collections.Counter(nums[:k])
        arr_sum = sum(nums[:k])
        max_sum = arr_sum if arr_counts.most_common()[0][1] <= 1 else -INFINITY
        # print(nums[:k], arr_sum, arr_counts)
        for i in range(1, len(nums) - k + 1):
            arr_sum += nums[i + k - 1] - nums[i - 1]
            try:
                arr_counts[nums[i + k - 1]] += 1
            except KeyError:
                arr_counts[nums[i + k - 1]] = 1
            arr_counts[nums[i - 1]] -= 1
            # print(nums[i:i + k], arr_sum, arr_counts)

            # TODO: Counter().most_common() is too slow
            if arr_sum > max_sum and arr_counts.most_common()[0][1] <= 1:
                max_sum = arr_sum
        
        return max_sum if max_sum > -INFINITY else 0

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        INFINITY = 10 ** 7
        arr_counts = collections.Counter(nums[:k])
        arr_sum = sum(nums[:k])
        max_sum = arr_sum if arr_counts.most_common()[0][1] <= 1 else -INFINITY
        # print(nums[:k], arr_sum, arr_counts, len(arr_counts))
        for i in range(1, len(nums) - k + 1):
            # Slide window right; add next number and subtract first number from sum
            arr_sum += nums[i + k - 1] - nums[i - 1]
            
            # Keep track of duplicates using Counter()
            try:
                arr_counts[nums[i + k - 1]] += 1
            except KeyError:
                arr_counts[nums[i + k - 1]] = 1
            
            if arr_counts[nums[i - 1]] > 1:
                arr_counts[nums[i - 1]] -= 1
            else:
                del arr_counts[nums[i - 1]]

            # print(nums[i:i + k], arr_sum, arr_counts, len(arr_counts))

            if arr_sum > max_sum and len(arr_counts) == k:
                max_sum = arr_sum
        
        return max_sum if max_sum > -INFINITY else 0

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        O(n) time, O(n) space solution using sliding window to keep track of
        sum, and collections.Counter() to keep track of duplicates
        """
        INFINITY = 10 ** 7
        arr_counts = collections.Counter(nums[:k])
        arr_sum = sum(nums[:k])
        max_sum = arr_sum if len(arr_counts) == k else -INFINITY
        for i in range(1, len(nums) - k + 1):
            # Slide window right
            arr_sum += nums[i + k - 1] - nums[i - 1]

            # Update counts
            arr_counts[nums[i + k - 1]] += 1
            arr_counts[nums[i - 1]] -= 1

            # If count drops to zero, remove it
            if arr_counts[nums[i - 1]] == 0:
                del arr_counts[nums[i - 1]]

            # If new maximum found with no duplicates, set maximum sum
            if arr_sum > max_sum and len(arr_counts) == k:
                max_sum = arr_sum
        
        # If no valid sums found, return 0
        return max_sum if max_sum > -INFINITY else 0