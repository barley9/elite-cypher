"""
3223. Minimum Length of String After Operations

You are given a string `s`.

You can perform the following process on `s` any number of times:
    Choose an index `i` in the string such that there is at least one character
        to the left of index `i` that is equal to `s[i]`, and at least one
        character to the right that is also equal to `s[i]`.
    Delete the closest character to the left of index `i` that is equal to
        `s[i]`.
    Delete the closest character to the right of index `i` that is equal to
        `s[i]`.

Return the minimum length of the final string `s` that you can achieve.
"""

import collections

class Solution:
    def minimumLength(self, s: str) -> int:
        """
        O(n + k) time, O(n) space solution, where n = len(s) and
        k = len(set(s)) is the number of unique characters in `s`
        """
        char_counts = collections.Counter(s)
        return sum(2 - (c & 1) for c in char_counts.values())

    def minimumLength(self, s: str) -> int:
        """O(n) time, O(1) space solution"""
        orda = ord('a')
        counter = [0] * 26
        for char in s: counter[ord(char) - orda] += 1
        return sum(2 - (count & 1) for count in counter if count > 0)

    def minimumLength(self, s: str) -> int:
        """O(26 * n) time, O(1) space solution"""
        result = 0
        for c in range(ord('a'), ord('z') + 1):
            count = s.count(chr(c))  # str.count() is crazy fast
            if count & 1: result += 1
            elif count > 0: result += 2
        return result