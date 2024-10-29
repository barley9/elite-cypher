"""
2684. Maximum Number of Moves in a Grid

You are given a 0-indexed `m x n` matrix `grid` consisting of positive
integers.

You can start at any cell in the first column of the matrix, and traverse the
grid in the following way:

From a cell `(row, col)`, you can move to any of the cells:
    `(row - 1, col + 1)`,
    `(row    , col + 1)`, and
    `(row + 1, col + 1)`
such that the value of the cell you move to, should be strictly bigger than the
value of the current cell.

Return the maximum number of moves that you can perform.
"""

import functools

class Solution:
    @functools.lru_cache
    def max_moves_rec(self, pos: Tuple[int, int]) -> int:
        global arr

        if pos[1] == len(arr[0]) - 1:
            return 0  # base case; we have reached right-most column
        
        moves = []
        for i in (-1, 0, +1):
            print(
                pos,
                arr[pos[0]][pos[1]],
                (pos[0] + i, pos[1] + 1),
                arr[pos[0] + i][pos[1] + 1] if (0 <= pos[0] + i < len(arr)) else None,
            )
            if (0 <= pos[0] + i < len(arr)) and (arr[pos[0] + i][pos[1] + 1] > arr[pos[0]][pos[1]]):
                moves.append(1 + self.max_moves_rec((pos[0] + i, pos[1] + 1)))
        return max(moves) if moves else 0

    def maxMoves(self, grid: List[List[int]]) -> int:
        global arr
        arr = grid
        return max(
            self.max_moves_rec((i, 0))
            for i in range(len(arr))
        )

# no faster than previous solution :(
class Solution:
    @functools.lru_cache
    def max_moves_rec(self, pos: Tuple[int, int]) -> int:
        global arr

        if pos[1] == len(arr[0]) - 1:
            return 0  # base case; we have reached right-most column
        
        result = 0
        for i in range(-1, 2):  # (-1, 0, +1)
            if not (0 <= pos[0] + i < len(arr)):
                continue
            m = arr[pos[0]][pos[1]]
            n = arr[pos[0] + i][pos[1] + 1]
            if m >= n:
                continue
            moves = self.max_moves_rec((pos[0] + i, pos[1] + 1)) + 1
            if moves > result:
                result = moves
        return result

    def maxMoves(self, grid: List[List[int]]) -> int:
        global arr
        arr = grid
        return max(
            self.max_moves_rec((i, 0))
            for i in range(len(arr))
        )