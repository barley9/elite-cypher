"""
1267. Count Servers that Communicate

You are given a map of a server center, represented as a `m * n` integer
matrix grid, where `1` means that on that cell there is a server and `0` means
that it is no server. Two servers are said to communicate if they are on the
same row or on the same column.

Return the number of servers that communicate with any other server.
"""

import numpy as np

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        grid = np.asarray(grid)
        print(np.sum(grid, axis=0))
        print(np.sum(grid, axis=1))

        # This could work, if it weren't for double-counting issues...

        return 0