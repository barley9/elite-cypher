"""
120. Triangle

Given a `triangle` array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More
formally, if you are on index `i` on the current row, you may move to either
index `i` or index `i + 1` on the next row.
"""

import functools

class Solution:
    triangle = []

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        return self.min_total_rec(0, 0)
        
    @functools.lru_cache
    def min_total_rec(self, row: int, col: int) -> int:
        if row == len(self.triangle):
            return 0
        left = self.min_total_rec(row + 1, col)
        right = self.min_total_rec(row + 1, col + 1)
        return self.triangle[row][col] + min(left, right)

class Solution:
    cache = {}
    triangle = []

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.cache = {}
        self.triangle = triangle
        return self.min_total_rec(0, 0)
        
    def min_total_rec(self, row: int, col: int) -> int:
        if (row, col) in self.cache:
            return self.cache[(row, col)]
        if row == len(self.triangle):
            return 0
        left  = self.min_total_rec(row + 1, col)
        right = self.min_total_rec(row + 1, col + 1)
        result = self.triangle[row][col] + (left if left < right else right)
        self.cache[(row, col)] = result
        return result

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_sums = [[0] * (i + 1) for i in range(len(triangle) - 1)]
        min_sums.append(triangle[-1])
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                left  = min_sums[row + 1][col]
                right = min_sums[row + 1][col + 1]
                min_sums[row][col] = triangle[row][col] + (left if left < right else right)
        return min_sums[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """O(n) time, O(1) space solution"""
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                left  = triangle[row + 1][col]
                right = triangle[row + 1][col + 1]
                triangle[row][col] += (left if left < right else right)
        return triangle[0][0]