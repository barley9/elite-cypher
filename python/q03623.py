"""
3623. Count Number of Trapezoids I

You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]`
represents the coordinates of the `i`th point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of
horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and
only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by
choosing any four distinct points from `points`.

Since the answer may be very large, return it modulo `10**9 + 7`.
"""

import math
import collections

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        O(n) time, O(n) space solution
        INCORRECT
        """
        MOD = 10 ** 9 + 7
        
        ycounts = collections.Counter(y for x,y in points)
        if len(ycounts) < 2:
            return 0

        valid = sum(count > 1 for count in ycounts.values())
        if valid < 2:
            return 0
        
        return (((valid * (valid - 1)) >> 1) * math.prod(
            ((count * (count - 1)) >> 1) % MOD
            for count in ycounts.values()
            if count > 1
        )) % MOD

    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        O(n ** 2) time, O(n) space solution
        TOO SLOW
        """
        MOD = 10 ** 9 + 7
        
        ycounts = collections.Counter(y for x,y in points)
        if len(ycounts) < 2:
            return 0

        valid = sum(count > 1 for count in ycounts.values())
        if valid < 2:
            return 0

        combinations = [
            ((count * (count - 1)) >> 1) % MOD
            for count in ycounts.values()
            if count > 1
        ]

        total = 0
        for i in range(len(combinations) - 1):
            for j in range(i + 1, len(combinations)):
                total += (combinations[i] * combinations[j]) % MOD
        return total % MOD
        
        # return (((valid * (valid - 1)) >> 1) * math.prod(
        #     ((count * (count - 1)) >> 1) % MOD
        #     for count in ycounts.values()
        #     if count > 1
        # )) % MOD
        
    def countTrapezoids(self, points: List[List[int]]) -> int:
        pass