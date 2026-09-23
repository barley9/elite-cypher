"""
1658. Minimum Operations to Reduce X to Zero

You are given an integer array `nums` and an integer `x`. In one operation, you
can either remove the leftmost or the rightmost element from the array `nums`
and subtract its value from `x`. Note that this modifies the array for future
operations.

Return the minimum number of operations to reduce `x` to exactly `0` if it is
possible, otherwise, return `-1`.
"""

import numpy as np

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        """INCORRECT"""
        # Create grid containing sum for `i` elements taken from front of
        # `nums` and `j` elements taken from back of `nums`
        grid = []
        for i in range(len(nums)):
            s = sum(nums[0:i])
            row = []
            for j in range(len(nums) - 1, -1, -1):
                if j < i:
                    row.append(-1)
                else:
                    s += nums[j]
                    row.append(s)
            grid.append(row)
        
        print(np.array(grid))

        # Walk grid to find first occurance of `x`
        # (0, 0), (0, 1), (1, 0), (2, 0), (1, 1), (0, 2), ...
        for k in range(len(nums)):
            for i in range(k + 1):
                print(grid[i][k - i], k + 1)
                # if grid[i][k - i] == x:
                #     return k + 1
        return -1