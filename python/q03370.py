"""
3370. Smallest Number With All Set Bits

You are given a positive number `n`.

Return the smallest number `x` greater than or equal to `n`, such that the
binary representation of `x` contains only set bits.
"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        """O(log n) time, O(1) space solution"""
        return (1 << n.bit_length()) - 1