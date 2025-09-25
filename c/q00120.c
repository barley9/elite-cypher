/*
 * 120. Triangle
 *
 * Given a `triangle` array, return the minimum path sum from top to bottom.
 * 
 * For each step, you may move to an adjacent number of the row below. More
 * formally, if you are on index `i` on the current row, you may move to
 * either index `i` or index `i + 1` on the next row.
 */

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize) {
    /* O(n) time, O(1) space solution */
    for (int row = triangleSize - 2; row > -1; row--) {
        for (int col = triangleColSize[row] - 1; col > -1; col--) {
            int left  = triangle[row + 1][col];
            int right = triangle[row + 1][col + 1];
            triangle[row][col] = triangle[row][col] + ((left < right) ? left : right);
        }
    }
    return triangle[0][0];
}