"""
1963. Minimum Number of Swaps to Make the String Balanced

You are given a 0-indexed string `s` of even length `n`. The string consists of
exactly `n / 2` opening brackets '[' and `n / 2` closing brackets ']'.

A string is called balanced if and only if:
    It is the empty string, or
    It can be written as `AB`, where both `A` and `B` are balanced strings, or
    It can be written as `[C]`, where `C` is a balanced string.

You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make `s` balanced.
"""

class Solution:
    @staticmethod
    def ceildiv(a: int, b: int) -> int:
        """ceiling division returns ceiling(a / b), complementary to floor division"""
        return -(a // -b)

    def minSwaps(self, s: str) -> int:
        """O(n) time, O(1) space solution"""
        ordbks = ord('\\')  # ASCII: ..., Z, [, \, ], ...
        kilter = 0  # i dunno what to call this: balance? kilter? right-heaviness?
        max_kilter = 0
        for c in s:
            kilter += ord(c) - ordbks
            if kilter > max_kilter:
                max_kilter = kilter
        return self.ceildiv(max_kilter, 2)

    def minSwaps(self,s):
        kilter,max_kilter=0,0
        for c in s:
            kilter+=1 if c==']' else -1
            if kilter>max_kilter:max_kilter=kilter
        return -(max_kilter // -2)

    def minSwaps(self,s):
        kilter,max_kilter=0,0
        for c in s:
            if c == ']':
                kilter += 1
                if kilter > max_kilter:max_kilter = kilter
            else:kilter -= 1
        return -(max_kilter // -2)