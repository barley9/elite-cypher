"""
3754. Concatenate Non-Zero Digits and Multiply by Sum I

You are given an integer `n`.

Form a new integer `x` by concatenating all the non-zero digits of `n` in
their original order. If there are no non-zero digits, `x = 0`.

Let `sum` be the sum of digits in `x`.

Return an integer representing the value of `x * sum`.
"""

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        """O(2 log n) time, O(log n) space solution"""
        ord0 = ord('0')
        nzdig = [
            d
            for d in str(n)
            if d != '0'
        ]
        s = sum(
            ord(d) - ord0
            for d in nzdig
        )
        return int(''.join(nzdig)) * s if nzdig else 0

    def sumAndMultiply(self, n: int) -> int:
        """INCORRECT: REVERSED DIGIT ORDER"""
        x = 0
        s = 0
        while n:
            q, r = divmod(n, 10)
            if r != 0:
                s += r  # add right-most digit to sum
                x = 10 * x + r  # append right-most digit to `x`
            n = q
        return x * s

    def sumAndMultiply(self, n: int) -> int:
        """O(2 log n) time, O(log n) space solution"""
        x = []  # list of digits, in increasing order of place value
        s = 0  # sum of nonzero digits
        while n:
            q, r = divmod(n, 10)
            if r != 0:
                s += r  # add right-most digit to sum
                x.append(r)  # append right-most digit to `x`
            n = q
        return s * sum(
            d * 10**p
            for p, d in enumerate(x)
        )