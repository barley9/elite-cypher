"""
1051. Height Checker

A school is trying to take an annual photo of all the students. The students are
asked to stand in a single file line in non-decreasing order by height. Let this
ordering be represented by the integer array `expected` where `expected[i]` is
the expected height of the `i`th student in line.

You are given an integer array `heights` representing the current order that the
students are standing in. Each `heights[i]` is the height of the `i`th student
in line (0-indexed).

Return the number of indices where `heights[i] != expected[i]`.
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        return sum(heights[i] != sorted_heights[i] for i in range(len(heights)))

    def heightChecker(self, heights: List[int]) -> int:
        """O(n log n) time, O(n) space solution using builtin `sorted` method"""
        sorted_heights = sorted(heights)
        return sum(h != s for h, s in zip(heights, sorted_heights))

    def quicksort(self, arr: list) -> list:
        """RYO implementation of quicksort algorithm"""
        if len(arr) < 2:
            return arr
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return self.quicksort(left) + [pivot] + self.quicksort(right)

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = self.quicksort(heights)
        return sum(heights[i] != sorted_heights[i] for i in range(len(heights)))