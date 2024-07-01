"""
169. Majority Element

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `n // 2` times. You
may assume that the majority element always exists in the array.
"""

import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """O(n) time and O(n) space solution"""
        if len(nums) == 1:
            return nums[0]

        t = len(nums) // 2  # threshold
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
                if counts[n] > t:  # stop early if we found the maj. element
                    return n
            else:
                counts[n] = 1
        
        raise ValueError("no majority element found")

    def majorityElement(self, nums: List[int]) -> int:
        """O(n) time and O(n) space solution using standard library builtins"""
        counts = collections.Counter(nums)
        return counts.most_common(1)[0][0]

    def majorityElement(self, nums: List[int]) -> int:
        """O(n) time and O(1) space solution taken from examples."""
        most_common = nums[0]
        count = 1
        for n in nums[1:]:
            if n == most_common:
                count += 1
            else:
                count -= 1
                # If `count` is ever negative, `n` is a more common element.
                # Store it and reset `count`
                if count < 0:
                    most_common = n
                    count = 1
        return most_common