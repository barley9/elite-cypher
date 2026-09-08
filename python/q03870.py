"""
3870. Count Commas in Range

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
        if math.log10(n) // 3 == 0.0:
            return 0
        else:
            return n - 999  # we don't need any more cases b/c n <= 10**5

    def countCommas(self, n: int) -> int:
        """O(1) time, O(1) space solution"""
        if n < 1000:
            return 0
        else:
            return n - 999  # we don't need any more cases b/c n <= 10**5