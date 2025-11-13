"""
2654. Minimum Number of Operations to Make All Array Elements Equal to 1

You are given a 0-indexed array `nums` consisiting of positive integers. You
can do the following operation on the array any number of times:
    Select an index `i` such that `0 <= i < n - 1` and replace either of
        `nums[i]` or `nums[i+1]` with their gcd value.

Return the minimum number of operations to make all elements of `nums` equal to
`1`. If it is impossible, return `-1`.

The gcd of two integers is the greatest common divisor of the two integers.
"""

import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        INCORRECT
        O(n) time, O(1) space solution

        Strategy:
            Count `1`s; return `len(nums) - num_ones`
            If no `1`s, find `i` s.t. `gcd(nums[i], nums[i+1]) == 1`; return
                `len(nums)`
            If no such `i`, return `-1`
        """
        ones_count = (nums[0] == 1)
        coprime_index = -1
        for i in range(1, len(nums)):
            if nums[i] == 1:
                ones_count += 1
            if math.gcd(nums[i - 1], nums[i]) == 1:
                coprime_index = i
        
        if ones_count > 0:
            return len(nums) - ones_count
        elif coprime_index != -1:
            return len(nums)
        else:
            return -1

    def minOperations(self, nums: List[int]) -> int:
        """INCORRECT"""
        ones_count = sum((n == 1) for n in nums)
        if ones_count > 0:
            return len(nums) - ones_count
        
        g = math.gcd(*nums)
        if g > 1:
            return -1
        
        return len(nums)