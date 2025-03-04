"""
1780. Check if Number is a Sum of Powers of Three

Given an integer `n`, return `true` if it is possible to represent `n` as the
sum of distinct powers of three. Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that
`y == 3 ** x`.
"""

class Solution:
    @staticmethod
    def ternary(n: int) -> list[int]:
        """
        converts integer `n` into array of ternary (aka base 3) digits
        """
        if n == 0:
            return [0]
        q = n
        result = []
        while q != 0:
            q, r = divmod(q, 3)
            result.append(r)
        return result

    def checkPowersOfThree(self, n: int) -> bool:
        return 2 not in self.ternary(n)

    def checkPowersOfThree(self, n: int) -> bool:
        """O(log_3(n)) time, O(1) space solution"""
        while n != 0:
            n, r = divmod(n, 3)
            if r == 2: return False
        return True
