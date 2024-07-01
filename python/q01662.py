"""
1662. Check If Two String Arrays are Equivalent

Given two string arrays `word1` and `word2`, return `true` if the two arrays represent the same string, and `false` otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Concatentate-and-compare solution using builtins. Time complexity is O(
            sum(len(w) for w in word1) +
            sum(len(w) for w in word2)
        ). Space complexity is O(
            sum(len(w) for w in word1) +
            sum(len(w) for w in word2)
        ).
        """
        return ''.join(word1) == ''.join(word2)

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        More C-like solution using multiple indices. Time complexity is O(
            sum(len(w) for w in word1) +
            sum(len(w) for w in word2)
        ). Space complexity is O(1).
        """
        p = q = 0  # indices into word1, word2 lists
        i = j = 0  # indices into word1[p], word2[q] strings

        while True:
            if word1[p][i] != word2[q][j]:
                return False

            i += 1
            j += 1

            if i >= len(word1[p]):
                i = 0
                p += 1

            if j >= len(word2[q]):
                j = 0
                q += 1

            if (p >= len(word1)) ^ (q >= len(word2)):
                return False  # we ran out of one list but not the other; they must not have same length; therefore not equal

            if (p >= len(word1)) & (q >= len(word2)):
                return True  # we ran out of both lists at same time without finding discrepancy; therefore must be equal