"""
2017. Grid Game

You are given a 0-indexed 2D array `grid` of size `2 x n`, where `grid[r][c]`
represents the number of points at position `(r, c)` on the matrix. Two robots
are playing a game on this matrix.

Both robots initially start at `(0, 0)` and want to reach `(1, n-1)`. Each
robot may only move to the right (`(r, c)` to `(r, c + 1)`) or down (`(r, c)`
to `(r + 1, c)`).

At the start of the game, the first robot moves from `(0, 0)` to `(1, n-1)`,
collecting all the points from the cells on its path. For all cells `(r, c)`
traversed on the path, `grid[r][c]` is set to `0`. Then, the second robot
moves from `(0, 0)` to `(1, n-1)`, collecting the points on its path. Note
that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second
robot. In contrast, the second robot wants to maximize the number of points it
collects. If both robots play optimally, return the number of points collected
by the second robot.
"""

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        """INCORRECT"""
        # Determine the optimal path for 1st robot
        # Because there are only two rows, the 1st robot can move down exactly once
        # The question is where it should use it to get the most points
        # (Is this question practically different from "minimize the score of the second robot"?)
        nrows = len(grid)
        ncols = len(grid[0])

        max_score = 0
        down_index = 0
        for i in range(ncols):
            score = sum(grid[0][:i + 1]) + sum(grid[1][i:])
            print(grid[0][:i + 1], grid[1][i:], score)
            if score > max_score:
                max_score = score
                down_index = i

        print(max_score, down_index)

        # Remove points collected by first robot from grid
        for i in range(down_index + 1):
            grid[0][i] = 0
        for i in range(down_index, ncols):
            grid[1][i] = 0

        print(grid[0])
        print(grid[1])

        # Determine maximum possible score for the second robot
        max_score = 0
        for i in range(ncols):
            score = sum(grid[0][:i + 1]) + sum(grid[1][i:])
            print(grid[0][:i + 1], grid[1][i:], score)
            if score > max_score:
                max_score = score

        return max_score

    def gridGame(self, grid: List[List[int]]) -> int:
        """O(n ** 2) time, O(1) space solution; TOO SLOW"""
        NROWS = len(grid)
        NCOLS = len(grid[0])
        INFINITY = 10 ** 10

        min_score = INFINITY
        for i in range(NCOLS):
            score = max(sum(grid[0][i + 1:]), sum(grid[1][0:i]))
            # print(grid[0][i + 1:], grid[1][0:i], score)
            if score < min_score:
                min_score = score
        
        return min_score

    def gridGame(self, grid: List[List[int]]) -> int:
        """
        O(n) time, O(1) space solution
        
        Because the grid has only two rows and the robots can only move either
        down or right, the first robot can move down exactly once. The
        question is then where it should make this move to optimize its goal.
        Once the first robot takes its turn, the grid will be essentially cut
        in half. Because of the 'diagonal' arrangement of zeros in the grid,
        the second robot cannot benefit from making its 'down' move anywhere
        but either at the very beginning or at the very end. Therefore, it
        will have to choose to take the top row or the bottom row to optimize
        its points. 
        """
        NROWS = len(grid)
        NCOLS = len(grid[0])
        INFINITY = 10 ** 10

        min_score = INFINITY  # minimum possible score
        top = sum(grid[0][1:])  # score if top row is taken
        bot = 0  # score if bottom row is taken
        for i in range(NCOLS - 1):
            score = top if top > bot else bot
            # print(grid[0][i + 1:], top, grid[1][0:i], bot, score)
            if score < min_score:
                min_score = score
            top -= grid[0][i + 1]
            bot += grid[1][i]

        score = top if top > bot else bot        
        return min_score if min_score < score else score