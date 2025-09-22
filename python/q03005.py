"""
3005. Count Elements With Maximum Frequency

You are given an array `nums` consisting of positive integers.

Return the total frequencies of elements in `nums` such that those elements
all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in
the array.
"""

import collections

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        """O(n) time, O(1) space solution"""
        counts = [0] * 101  # 1 <= nums[i] <= 100
        for n in nums:
            counts[n] += 1
        
        max_count = -1
        elems = 0
        for i in range(len(counts)):
            if counts[i] > max_count:
                max_count = counts[i]
                elems = 1
            elif counts[i] == max_count:
                elems += 1
        
        return max_count * elems

    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)
        max_freq = max(freqs.values())
        return sum(f for f in freqs.values() if f == max_freq)