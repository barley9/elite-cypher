"""
3751. Total Waviness of Numbers in Range I

You are given two integers `num1` and `num2` representing an inclusive range
`[num1, num2]`.

The waviness of a number is defined as the total count of its peaks and valleys:
    A digit is a peak if it is strictly greater than both of its immediate
        neighbors.
    A digit is a valley if it is strictly less than both of its immediate
        neighbors.
    The first and last digits of a number cannot be peaks or valleys.
    Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range `[num1, num2]`. 
"""

class Solution:
    def waviness(self, n: int) -> int:
        ord0 = ord('0')
        digits = [ord(d) - ord0 for d in str(n)]
        
        if len(digits) < 3:
            return 0
        
        diffs = [
            digits[i] - digits[i - 1]
            for i in range(1, len(digits))
        ]
        return sum(
            (diffs[i] * diffs[i - 1]) < 0
            for i in range(1, len(diffs))
        )

    def totalWaviness(self, num1: int, num2: int) -> int:
        """
        O(n * m) time, O(m) space solution where
        `m = max(len(str(num)) for num in range(num1, num2 + 1))`
        """
        return sum(
            self.waviness(n)
            for n in range(num1, num2 + 1)
        )

    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for n in range(num1, num2 + 1):
            digits = [ord(d) for d in str(n)]
            total += sum(
                (digits[i] - digits[i - 1]) * (digits[i + 1] - digits[i]) < 0
                for i in range(1, len(digits) - 1)
            )
        return total

    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for n in range(num1, num2 + 1):
            while n >= 100:
                d = (n % 10)
                c = (n % 100) // 10
                m = (n % 1000) // 100

                total += ((m - c) * (c - d) < 0)

                n //= 10
        return total