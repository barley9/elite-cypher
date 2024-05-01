"""
2001. Number of Pairs of Interchangeable Rectangles

You are given `n` rectangles represented by a 0-indexed 2D integer array
`rectangles`, where `rectangles[i] = [width_i, height_i]` denotes the width and
height of the `i`th rectangle.

Two rectangles `i` and `j` (`i < j`) are considered interchangeable if they have
the same width-to-height ratio. More formally, two rectangles are
interchangeable if `width_i / height_i == width_j / height_j` (using decimal
division, not integer division).

Return the number of pairs of interchangeable rectangles in `rectangles`.
"""

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        """O(n) time, O(n) space solution"""
        ratios = {}  # store hash table of ratios r : [rectangles with ratio r]
        for i, rect in enumerate(rectangles):
            r = rect[0] / rect[1]
            if r in ratios:
                ratios[r].append(i)
            else:
                ratios[r] = [i]
        
        total = 0
        for k, v in ratios.items():
            total += (len(v) * (len(v) - 1)) // 2  # triangle number
        
        return total

    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        """O(n) time, O(n) space solution"""
        ratios = {}
        total = 0
        for rect in rectangles:  # optimized into one loop
            r = rect[0] / rect[1]  # width / height
            if r in ratios:
                total += ratios[r]
                ratios[r] += 1
            else:
                ratios[r] = 1
                
        return total