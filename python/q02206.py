"""
2206. Divide Array Into Equal Pairs

You are given an integer array `nums` consisting of `2 * n` integers.

You need to divide `nums` into `n` pairs such that:
    Each element belongs to exactly one pair.
    The elements present in a pair are equal.

Return `true` if nums can be divided into `n` pairs, otherwise return `false`.
"""

import collections

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        O(2*n) time, O(n) space solution
        
        Strategy:
        Keep track of whether we've seen each value an even or odd number of times
        """
        counts = collections.Counter(nums)
        return not any(v & 1 for v in counts.values())

    def divideArray(self, nums: List[int]) -> bool:
        """
        O(2*n) time, O(1) space solution
        
        Strategy:
        Keep track of whether we've seen each value an even or odd number of times
        """
        counts = [0] * 501  # 1 <= nums[i] <= 500
        for n in nums:
            counts[n] ^= 1  # XOR toggles count[n] between 0 (even) and 1 (odd)
        return not any(counts)

    def divideArray(self, nums: List[int]) -> bool:
        counts = [1] * 501
        for n in nums: counts[n] ^= 1
        return all(counts)