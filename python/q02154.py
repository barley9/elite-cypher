"""
2154. Keep Multiplying Found Values by Two

You are given an array of integers `nums`. You are also given an integer `original` which is the first number that needs to be searched for in `nums`.

You then do the following steps:
    If `original` is found in `nums`, multiply it by two (i.e., set `original = 2 * original`).
    Otherwise, stop the process.
    Repeat this process with the new number as long as you keep finding the number.

Return the final value of `original`.
"""

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        """O(n) time, O(n) space solution"""
        multiples = {
            n
            for n in nums
            if ((n % original == 0) and ((n // original).bit_count() == 1))
        }
        for _ in range(len(multiples)):
            if original in multiples:
                original <<= 1
            else:
                break
        return original

    def findFinalValue(self, nums: List[int], original: int) -> int:
        """O(n) time, O(n) space solution"""
        multiples = set()
        for n in nums:
            q, r = divmod(n, original)
            if q.bit_count() == 1 and r == 0:
                multiples.add(n)
        while True:
            if original in multiples:
                original <<= 1
            else:
                break
        return original

    def findFinalValue(self, nums: List[int], original: int) -> int:
        """O(n) time, O(n) space solution"""
        multiples = {n for n in nums if n % original == 0}
        while True:
            if original in multiples:
                original <<= 1
            else:
                break
        return original

    def findFinalValue(self, nums: List[int], original: int) -> int:
        """O(n^2) time, O(1) space solution"""
        while True:
            if original in nums:
                original <<= 1
            else:
                break
        return original