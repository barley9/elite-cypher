"""
2894. Divisible and Non-divisible Sums Difference

You are given positive integers `n` and `m`.

Define two integers as follows:
    `num1`: The sum of all integers in the range `[1, n]` (both inclusive)
        that *are not* divisible by `m`.
    `num2`: The sum of all integers in the range `[1, n]` (both inclusive)
        that *are* divisible by `m`.

Return the integer `num1 - num2`.
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """O(2 * n) time, O(n) space solution"""
        num1 = sum(i for i in range(1, n + 1) if i % m != 0)
        num2 = sum(i for i in range(1, n + 1) if i % m == 0)
        return num1 - num2
        
    def differenceOfSums(self, n: int, m: int) -> int:
        """O(n) time, O(1) space solution"""
        return (n * (n + 1) // 2) - 2 * sum(range(m, n + 1, m))
        
    def differenceOfSums(self, n: int, m: int) -> int:
        """O(1) time, O(1) space solution"""
        return (n * (n + 1) // 2) - 2 * m * ((n // m) * ((n // m) + 1) // 2)