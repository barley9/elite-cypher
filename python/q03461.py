"""
3461. Check If Digits Are Equal in String After Operations I

You are given a string `s` consisting of digits. Perform the following
operation repeatedly until the string has exactly two digits:
    For each pair of consecutive digits in `s`, starting from the first digit,
        calculate a new digit as the sum of the two digits modulo 10.
    Replace `s` with the sequence of newly calculated digits, maintaining the
        order in which they are computed.

Return `true` if the final two digits in `s` are the same; otherwise, return
`false`.
"""

class Solution:
    ord0 = ord('0')

    @staticmethod
    @functools.lru_cache
    def binomial(n: int, k: int) -> int:
        """
        Computes the binomial coefficient `C(n, k)`
        See <https://en.wikipedia.org/wiki/Binomial_coefficient>
        """
        if k < 1:
            return 1
        elif k > n:
            return 0
        else:
            return Solution.binomial(n - 1, k) + Solution.binomial(n - 1, k - 1)

    def hasSameDigits(self, s: str) -> bool:
        """O(???) time, O(n) space solution"""
        return (sum(
            (ord(d) - self.ord0) * Solution.binomial(len(s) - 2, i)
            for i, d in enumerate(s[:len(s) - 1])
        ) - sum(
            (ord(d) - self.ord0) * Solution.binomial(len(s) - 2, i)
            for i, d in enumerate(s[1:])
        )) % 10 == 0

    def hasSameDigits(self, s: str) -> bool:
        digits = [ord(d) - self.ord0 for d in s]
        binoms = [
            Solution.binomial(len(s) - 2, i)
            for i in range(len(s) - 1)
        ]
        return sum(
            digits[i] * binoms[i]
            for i in range(0, len(digits) - 1)
        ) % 10 == sum(
            digits[i] * binoms[i - 1]
            for i in range(1, len(digits))
        ) % 10