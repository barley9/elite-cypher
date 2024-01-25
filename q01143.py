"""
1143. Longest Common Subsequence

Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, `"ace"` is a subsequence of `"abcde"`.

A common subsequence of two strings is a subsequence that is common to both strings.
"""


import itertools

class Solution:
    @staticmethod
    def powerset(iterable: Iterable) -> Iterable:
        """
        Example:
            powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

        Taken from https://docs.python.org/3/library/itertools.html#itertools-recipes
        """
        s = list(iterable)
        return itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        This solution is correct, but is O(2^n) which is much too slow.
        """

        # Make sure len(text1) <= len(text2). If not, swap them.
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        # print(list(self.powerset(text1)))
        # print(list(self.powerset(text2)))

        maxlen = 0
        # maxsub = tuple()
        for sub1 in self.powerset(text1):  # NOTE: here's the O(2^n) part
            if len(sub1) > len(text2):
                break

            for sub2 in itertools.combinations(text2, len(sub1)):
                if sub1 == sub2:
                    maxlen = len(sub1)
                    # maxsub = sub1
        
        # print(maxsub, maxlen)

        return maxlen

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Second attempt. Fails on cases such as ('psnw', 'vozsh')"""

        # Make sure `text1` is shorter than `text2`. If not, swap them.
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        i = 0
        j = 0
        current_len = 0
        max_len = 0
        while i < len(text1):
            while j < len(text2):
                if text1[i] == text2[j]:
                    current_len += 1
                    i += 1
                j += 1

            i += 1

            if current_len > max_len:
                max_len = current_len
            
        return max_len