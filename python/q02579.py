"""
2579. Count Total Number of Colored Cells

There exists an infinitely large two-dimensional grid of uncolored unit cells.
You are given a positive integer `n`, indicating that you must do the
following routine for `n` minutes:
    At the first minute, color any arbitrary unit cell blue.
    Every minute thereafter, color blue every uncolored cell that touches a blue
        cell.

Return the number of colored cells at the end of `n` minutes.
"""

class Solution:
    def coloredCells(self, n: int) -> int:
        """
        O(1) time, O(1) space solution
        
        Strategy:
        Observe the first few terms in the sequence:
            1, 1+4=5, 5+8=13, 13+12=25, 25+16=41, ...
        Guess quadratic model `f(n) = an^2 + bn + c`.
        Build augmented matrix from (1, f(1)), (2, f(2)), (3, f(3)) and convert to RREF:
            [[ 1 1 1 |  1 ]     [[ 1 0 0 |  2 ]
             [ 4 2 1 |  5 ]  =>  [ 0 1 0 | -2 ]
             [ 9 3 1 | 13 ]]     [ 0 0 1 |  1 ]]
        Therefore a=2, b=-2, c=1 and `f(n) = 2n^2 - 2n + 1 = 2n(n - 1) + 1`
        """
        return 2 * n * (n - 1) + 1