"""
2657. Find the Prefix Common Array of Two Arrays

You are given two 0-indexed integer permutations `A` and `B` of length `n`.

A prefix common array of `A` and `B` is an array `C` such that `C[i]` is equal
to the count of numbers that are present at or before the index `i` in both `A`
and `B`.

Return the prefix common array of `A` and `B`.

A sequence of `n` integers is called a permutation if it contains all integers
from `1` to `n` exactly once.
"""

import collections

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """O(n ** 2) time, O(3 * n) space solution"""
        counta = [0] * (len(A) + 1)
        countb = [0] * (len(B) + 1)
        result = []
        for a, b in zip(A, B):
            counta[a] += 1
            countb[b] += 1
            result.append(sum(
                (ca > 0 and cb > 0 and ca == cb)
                for ca, cb in zip(counta, countb)
            ))
        return result

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """O(n ** 2) time, O(3 * n) space solution"""
        counta = collections.Counter()
        countb = collections.Counter()
        result = []
        common = 0
        for i in range(len(A)):
            counta.update(A[i:i + 1])
            countb.update(B[i:i + 1])
            result.append((counta & countb).total())
        return result