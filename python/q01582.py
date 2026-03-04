"""
1582. Special Positions in a Binary Matrix

Given an `m x n` binary matrix `mat`, return the number of special positions
in `mat`.

A position `(i, j)` is called special if `mat[i][j] == 1` and all other
elements in row `i` and column `j` are `0` (rows and columns are 0-indexed).
"""

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """O(m * n) time, O(m + n) space solution"""
        ROWS = len(mat)
        COLS = len(mat[0])

        row_sums = list(map(sum, mat))
        col_sums = [
            sum(
                mat[i][j]
                for i in range(ROWS)
            )
            for j in range(COLS)
        ]
        
        # print(row_sums, col_sums)

        count = 0
        for i in range(ROWS):
            # If there is exactly one `1` in row...
            if row_sums[i] == 1:
                # Find index in row where `1` appears
                j = 0
                while j < COLS and mat[i][j] == 0:
                    j += 1
                # print(i, j, sep=', ')
                
                # ...and if there is exactly one `1` in column, increment
                if (j < COLS) and (col_sums[j] == 1):
                    count += 1

        return count