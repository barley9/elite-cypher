"""
2486. Append Characters to String to Make Subsequence

You are given two strings `s` and `t` consisting of only lowercase English
letters.

Return the minimum number of characters that need to be appended to the end of
`s` so that `t` becomes a subsequence of `s`.

A subsequence is a string that can be derived from another string by deleting
some or no characters without changing the order of the remaining characters.
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """O(n) time, O(1) space solution."""
        j = 0  # index into `t`
        for c in s:
            if c == t[j]:  # we only need the first match in `s`
                j += 1
                if j >= len(t):
                    return 0  # `t` is already a subsequence of `s`
        return len(t) - j  # number of missing characters from the end of `t`