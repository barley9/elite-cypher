"""
3042. Count Prefix and Suffix Pairs I

You are given a 0-indexed string array `words`.

Let's define a boolean function `isPrefixAndSuffix` that takes two strings, `str1` and `str2`:

    'isPrefixAndSuffix(str1, str2)' returns true if `str1` is both a prefix and a suffix of `str2`, and false otherwise.

For example, `isPrefixAndSuffix("aba", "ababa")` is `true` because "aba" is a prefix of "ababa" and also a suffix, but `isPrefixAndSuffix("abc", "abcd")` is `false`.

Return an integer denoting the number of index pairs `(i, j)` such that `i < j`, and `isPrefixAndSuffix(words[i], words[j])` is `true`.
"""


class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        """
        Returns True if `str1` is both a prefix and a suffix of `str2`; False otherwise.
        This is O(len(str1)) time and O(1) space.
        """
        if len(str2) < len(str1):
            return False

        for i in range(len(str1)):
            if str1[i] != str2[i] or str1[-(i + 1)] != str2[-(i + 1)]:
                return False
        return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Returns the number of pairs of strings in `words` such that `isPrefixAndSuffix()` is True.

        Because of the nested loop, this is O(len(words) ** 2) time and O(1) space.
        """
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                count += self.isPrefixAndSuffix(words[i], words[j])
        return count

    # More optimized (?) solution with the same time complexity
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                count += words[j][:len(words[i])] == words[i] and words[j][len(words[j]) - len(words[i]):len(words[j])] == words[i]
        return count