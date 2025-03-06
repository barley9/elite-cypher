"""
2965. Find Missing and Repeated Values

You are given a 0-indexed 2D integer matrix `grid` of size `n * n` with values
in the range `[1, n**2]`. Each integer appears exactly once except `a` which
appears twice and `b` which is missing. The task is to find the repeating and
missing numbers `a` and `b`.

Return a 0-indexed integer array `ans` of size `2` where `ans[0]` equals `a`
and `ans[1]` equals `b`.
"""

import math
import functools

class Solution:
    @staticmethod
    def factorial(n: int) -> int:
        if n < 2:
            return 1
        result = 2
        for i in range(3, n + 1):
            result *= i
        return result

    # This implementation turns out to be much faster
    @staticmethod
    @functools.lru_cache()
    def factorial(n: int) -> int:
        if n < 2:
            return 1
        else:
            return n * Solution.factorial(n - 1)

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        O(n ** 2) time, O(1) space solution
        
        Strategy:
        Suppose 2x2 grid. Should have elements a,b,c,d. But, suppose `a` is
        repeated and `b` is missing. That is, grid contains a,a,c,d. So, sum
        all elements in grid and subtract from known sum of 1,2,...,n**2.
        Perform analogous operation using products. The difference D = b - a
        and the ratio R = b/a. This gives a system of two equations with two
        unknowns. Solve and return result.
        """
        n = len(grid) * len(grid)  # number of cells in grid

        # Calculate sum and product if all numbers were present and none repeated
        pristine_sum = (n * (n + 1)) // 2
        pristine_prod = self.factorial(n)
        
        # Calculate actual sum and product
        grid_sum = sum(sum(row) for row in grid)
        grid_prod = math.prod(math.prod(row) for row in grid)

        # print(pristine_sum, grid_sum)
        # print(pristine_prod, grid_prod)

        D = pristine_sum - grid_sum
        # q, r = divmod(pristine_prod, grid_prod)  # NOTE: trying to avoid floats
        R = pristine_prod / grid_prod

        # print(D, '|', q, r, R)

        # a = (D - r) // (q - 1)  # NOTE: fails when a > b
        a = round(D / (R - 1))  # repeated number
        b = D + a  # missing number

        return [a, b]