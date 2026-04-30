"""
3742. Maximum Path Score in a Grid

You are given an `m x n` grid where each cell contains one of the values 0, 1,
or 2. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right
corner `(m - 1, n - 1)` by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according
to their cell values:
    0: adds 0 to your score and costs 0.
    1: adds 1 to your score and costs 1.
    2: adds 2 to your score and costs 1. ​​​​​​​

Return the maximum score achievable without exceeding a total cost of `k`, or
`-1` if no valid path exists.

Note: If you reach the last cell but the total cost exceeds `k`, the path is
invalid.
"""

class Solution:
    cache = {}
    grid = []
    k = None
    
    def max_score_rec(self, pos: tuple[int, int]) -> int:
        """
        This is the right approach I think, but I don't feel like working out
        the details right now.
        """
        if pos in self.cache:
            return self.cache[pos]
        
        result = max(
            self.grid[pos[0]][pos[1]] + \
                self.max_score_rec((pos[0] + 1, pos[1])) if (pos[0] + 1 < len(self.grid)) else -1,
            self.grid[pos[0]][pos[1]] + \
                self.max_score_rec((pos[0], pos[1] + 1)) if (pos[1] + 1 < len(self.grid[0])) else -1,
        )
        
        print(pos, result)

        self.cache[pos] = result
        return result

    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        self.grid = grid
        result = self.max_score_rec((0, 0))
        print(self.cache)