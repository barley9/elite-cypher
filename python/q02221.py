"""
2221. Find Triangular Sum of an Array

You are given a 0-indexed integer array `nums`, where `nums[i]` is a digit
between `0` and `9` (inclusive).

The triangular sum of `nums` is the value of the only element present in
`nums` after the following process terminates:
    Let `nums` comprise of `n` elements. If `n == 1`, end the process.
        Otherwise, create a new 0-indexed integer array `newNums` of length
        `n - 1`.
    For each index `i`, where `0 <= i < n - 1`, assign the value of
        `newNums[i]` as `(nums[i] + nums[i+1]) % 10`, where `%` denotes modulo
        operator.
    Replace the array `nums` with `newNums`.
    Repeat the entire process starting from step 1.

Return the triangular sum of `nums`.
"""

import functools

class Solution:
    @staticmethod
    @functools.lru_cache(maxsize=None)
    def binomial(n: int, k: int) -> int:
        """
        Computes the binomial coefficient `C(n, k)`
        See <https://en.wikipedia.org/wiki/Binomial_coefficient>
        """
        if k < 1:
            return 1
        elif k > n:
            return 0
        else:
            return Solution.binomial(n - 1, k) + Solution.binomial(n - 1, k - 1)
    
    def triangularSum(self, nums: List[int]) -> int:
        """O(n * ???) time, O(1) space solution"""
        return sum(
            nums[i] * Solution.binomial(len(nums) - 1, i)
            for i in range(len(nums))
        ) % 10