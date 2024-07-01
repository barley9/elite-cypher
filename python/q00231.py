"""
231. Power of Two

Given an integer `n`, return `true` if it is a power of two. Otherwise, return
`false`.

An integer `n` is a power of two, if there exists an integer `x` such that
`n == 2 ** x`.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        This solution is O(log n) time because, under the hood, `bit_count` is a
        loop testing each bit of `n`.
        """
        return n > 0 and n.bit_count() == 1

    def isPowerOfTwo(self, n: int) -> bool:
        """This solution is O(1) time and O(1) space."""
        return n > 0 and not n & (n - 1)