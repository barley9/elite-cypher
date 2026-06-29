"""
1967. Number of Strings That Appear as Substrings in Word

Given an array of strings `patterns` and a string `word`, return the number of
strings in `patterns` that exist as a substring in `word`.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """O(m*n) time, O(1) space solution"""
        return sum(
            pattern in word  # built-in substring search is extremely optimized
            for pattern in patterns
        )