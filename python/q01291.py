"""
1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is
one more than the previous digit.

Return a sorted list of all the integers in the range `[low, high]` inclusive
that have sequential digits.
"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """O(1) time, O(1) space solution"""
        digits = '123456789'
        
        seq_nums = [
            int(digits[i:j])
            for i in range(0, len(digits))
            for j in range(i + 2, len(digits) + 1)
        ]

        return sorted(
            n
            for n in seq_nums
            if low <= n <= high
        )

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        N = 123456789

        seq_nums = [
            (N % 10**(start + stride)) // 10**start
            for stride in range(2, 9 + 1)
            for start in range(9 - stride, -1, -1)
        ]

        return [
            n
            for n in seq_nums
            if low <= n <= high
        ]

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """O(1) time, O(1) space solution"""
        N = 123456789
        return [
            (N % 10**(start + stride)) // 10**start
            for stride in range(2, 9 + 1)
            for start in range(9 - stride, -1, -1)
            if low <= (N % 10**(start + stride)) // 10**start <= high
        ]