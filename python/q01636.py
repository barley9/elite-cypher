"""
1636. Sort Array by Increasing Frequency

Given an array of integers `nums`, sort the array in increasing order based on
the frequency of the values. If multiple values have the same frequency, sort
them in decreasing order.

Return the sorted array.
"""

import collections

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = collections.Counter(nums)
        return [
            i
            for k, v in sorted(
                counts.items(),
                key=lambda item: (item[1], 100 - item[0])
            )
            for i in [k] * v
        ]