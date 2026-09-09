"""
3871. Count Commas in Range II

You are given an integer `n`.

Return the total number of commas used when writing all integers from `[1, n]`
(inclusive) in standard number formatting.

In standard formatting:
    A comma is inserted after every three digits from the right.
    Numbers with fewer than 4 digits contain no commas.
"""

import math

class Solution:
    def countCommas(self, n: int) -> int:
        """O(1) time, O(1) space solution"""
        if n < 1000:
            return 0
        elif n < 1_000_000:
            return n - 999
        elif n < 1_000_000_000:
            return 2 * n - 999 - 999_999
        elif n < 1_000_000_000_000:
            return 3 * n - 999 - 999_999 - 999_999_999
        elif n < 1_000_000_000_000_000:
            return 4 * n - 999 - 999_999 - 999_999_999 - 999_999_999_999
        elif n < 1_000_000_000_000_000_000:
            return 5 * n - 999 - 999_999 - 999_999_999 - 999_999_999_999 - 999_999_999_999_999

    def countCommas(self, n: int) -> int:
        """O(1) time, O(1) space solution; fastest"""
        if n < 1000:
            return 0
        elif n < 1_000_000:
            return n - 999
        elif n < 1_000_000_000:
            return 2 * n - 1_000_998
        elif n < 1_000_000_000_000:
            return 3 * n - 1_001_000_997
        elif n < 1_000_000_000_000_000:
            return 4 * n - 1_001_001_000_996
        elif n < 1_000_000_000_000_000_000:
            return 5 * n - 1_001_001_001_000_995

    def countCommas(self, n: int) -> int:
        """
        O(log n) time, O(log n) space solution
        
        INCORRECT: INSUFFICIENT FLOAT PRECISION
        """
        q = int(math.log10(n) // 3)  # fails for n really close to 10**15
        return q * n - sum(
            int(3 * i * '9')
            for i in range(1, q + 1)
        )

    def countCommas(self, n: int) -> int:
        """O(log n) time, O(1) space solution; slower but correct"""
        m = n

        # Compute log_10(n) // 3 using only integer arithmetic
        lg = -1
        while m:
            lg += 1
            m //= 1000  # TODO: could be done with mult instead of div?

        s = 0
        for _ in range(lg):
            s = 1000 * s + 1000
        
        return lg * n - s + lg