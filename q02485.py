"""
2485. Find the Pivot Integer

Given a positive integer `n`, find the pivot integer `x` such that:

    The sum of all elements between `1` and `x` inclusively equals the sum of
    all elements between `x` and `n` inclusively.

Return the pivot integer `x`. If no such integer exists, return `-1`. It is
guaranteed that there will be at most one pivot index for the given input.
"""

# Create square-root lookup table for numbers up to 1000 (because 1 <= n <= 1000)
sqrts = {i ** 2 : i for i in range(1, 1000 + 1)}

class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        O(1) time, O(1) space solution using a lookup table for square roots. It
        turns out (after a bit of arithmetic) that the pivot
        `x = sqrt(n * (n + 1) / 2)` if the root is an integer; if it is not, no
        pivot exists.
        """
        s = n * (n + 1) // 2  # `n`th triangle number
        if s in self.sqrts:
            return self.sqrts[s]
        else:
            return -1

######################################
#### Alternative, Faster Solution ####
######################################

import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        s = math.sqrt(n * (n + 1) / 2)
        if math.isclose(s, round(s)):
            return round(s)
        else:
            return -1