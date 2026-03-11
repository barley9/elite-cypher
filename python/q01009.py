"""
1009. Complement of Base 10 Integer

The complement of an integer is the integer you get when you flip all the 0's
to 1's and all the 1's to 0's in its binary representation.

For example, The integer `5` is "101" in binary and its complement is "010"
which is the integer `2`.

Given an integer `n`, return its complement.
"""

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """WRONG"""
        return ~n

    def bitwiseComplement(self, n: int) -> int:
        """
        O(log n) time, O(1) space solution

        Because Python stores integers in 2's complement, simply taking the
        bitwise `not` will not work. We have to mask off the upper bits to
        keep the output positive.
        """
        # print(bin(n), n.bit_length())
        # print(bin(~0))
        # print(bin(~0 << n.bit_length()))
        if n == 0:
            return 1

        return ~n & ~(~0 << n.bit_length())