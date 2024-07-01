"""
201. Bitwise AND of Numbers Range

Given two integers `left` and `right` that represent the range `[left, right]`,
return the bitwise AND of all numbers in this range, inclusive.
"""

import math

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """O(right - left) time and O(1) space solution; much too slow"""
        result = 2 ** 31 - 1
        for i in range(left, right + 1):
            result &= i
        return result

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """incorrect"""
        if left == right:
            return left
        if left.bit_length() != right.bit_length():
            return 0

        result = left & right
        return result & (0xFFFFFFFF << (~result).bit_length() - 1)

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """incorrect"""
        if left == right:
            return left

        shift = max(left.bit_length(), right.bit_length()) - 1
        mask = 1 << shift
        while mask:
            if not (left & right & mask):
                return mask & ((1 << shift + 1) - 1)
            mask = mask >> 1
        
        return left
