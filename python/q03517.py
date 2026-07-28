"""
3517. Smallest Palindromic Rearrangement I

You are given a palindromic string `s`.

Return the lexicographically smallest palindromic permutation of `s`.
"""

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        """O(n log n) time, O(n) space solution"""
        if len(s) < 2:
            return s

        prefix = s[:len(s) // 2]
        middle = s[len(s) // 2] if (len(s) % 2 == 1) else ''

        prefix = sorted(prefix)

        return ''.join(prefix + [middle] + prefix[::-1])