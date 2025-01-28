"""
2658. Maximum Number of Fish in a Grid

You are given a 0-indexed 2D matrix `grid` of size `m x n`, where `(r, c)`
        represents:
    A land cell if `grid[r][c] = 0`, or
    A water cell containing `grid[r][c]` fish, if `grid[r][c] > 0`.

A fisher can start at any water cell `(r, c)` and can do the following
        operations any number of times:
    Catch all the fish at cell `(r, c)`, or
    Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his
starting cell optimally, or `0` if no water cell exists.

An adjacent cell of the cell `(r, c)`, is one of the cells `(r, c + 1)`,
`(r, c - 1)`, `(r + 1, c)`, or `(r - 1, c)` if it exists.
"""

import collections

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """O(m * n) time, O(m * n) space solution"""
        NROWS = len(grid)
        NCOLS = len(grid[0])

        # Find all euclidean-connected 'pools' of fish
        cell_pools = {}  # {(r, c) : pool_index, ...}
        pool_cells = {}  # {pool_index : [(r, c), (r, c), ...], ...}
        pool_index = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0 and (i, j) not in cell_pools:
                    cell_pools[(i, j)] = pool_index
                    pool_cells[pool_index] = [(i, j)]
                    neighbors = collections.deque([
                        (i + 1, j),
                        (i - 1, j),
                        (i, j + 1),
                        (i, j - 1),
                    ])
                    seen = {(i, j)}
                    while neighbors:
                        r, c = neighbors.popleft()
                        if ((r, c) not in seen) and (0 <= r < NROWS) and (0 <= c < NCOLS) and (grid[r][c] > 0):
                            cell_pools[(r, c)] = pool_index
                            pool_cells[pool_index].append((r, c))
                            seen.add((r, c))
                            neighbors.extend([
                                (r + 1, c),
                                (r - 1, c),
                                (r, c + 1),
                                (r, c - 1),
                            ])

                    pool_index += 1

        # print(pool_cells)
        # print(cell_pools)

        return max(
            sum(grid[r][c] for r, c in pool)
            for pool in pool_cells.values()
        ) if pool_cells else 0

    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        """
        Helper function. Returns the sum of all cells in grid adjacent to
        (i, j) using depth-first search
        """
        if not (0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] > 0):
            return 0
        temp = grid[i][j]
        grid[i][j] = 0  # to avoid double-counting
        return temp + \
               self.dfs(grid, i + 1, j) + \
               self.dfs(grid, i - 1, j) + \
               self.dfs(grid, i, j + 1) + \
               self.dfs(grid, i, j - 1)

    def findMaxFish(self, grid: List[List[int]]) -> int:
        NROWS = len(grid)
        NCOLS = len(grid[0])
        max_fish = 0
        for i in range(NROWS):
            for j in range(NCOLS):
                if grid[i][j] > 0:
                    fish = self.dfs(grid, i, j)
                    if fish > max_fish:
                        max_fish = fish
        return max_fish