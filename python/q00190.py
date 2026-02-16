"""
190. Reverse Bits

Reverse bits of a given 32 bits signed integer.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        """O(log n) time, O(log n) space solution"""
        return int(
            f'{n:0>32b}'[::-1],
            2
        )