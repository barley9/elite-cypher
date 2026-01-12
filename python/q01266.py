"""
1266. Minimum Time Visiting All Points

On a 2D plane, there are `n` points with integer coordinates
`points[i] = [xi, yi]`. Return the minimum time in seconds to visit all the
points in the order given by `points`.

You can move according to these rules:
    In `1` second, you can either:
        (a) move vertically by one unit,
        (b) move horizontally by one unit, or
        (c) move diagonally `sqrt(2)` units (in other words, move one unit
            vertically then one unit horizontally in `1` second).
    You have to visit the points in the same order as they appear in the array.
    You are allowed to pass through points that appear later in the order, but
        these do not count as visits.
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for i in range(1, len(points)):
            x0, y0 = points[i - 1]
            x1, y1 = points[i]
            dx, dy = abs(x1 - x0), abs(y1 - y0)
            num_diag = min(dx, dy)
            total += (dx - num_diag) + (dy - num_diag) + num_diag
        return total

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """O(n) time, O(1) space solution"""
        return sum(
            max(
                abs(points[i][0] - points[i - 1][0]),  # dx
                abs(points[i][1] - points[i - 1][1])   # dy
            )
            for i in range(1, len(points))
        )