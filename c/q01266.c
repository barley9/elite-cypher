/*
 * 1266. Minimum Time Visiting All Points
 * 
 * On a 2D plane, there are `n` points with integer coordinates
 * `points[i] = [xi, yi]`. Return the minimum time in seconds to visit all the
 * points in the order given by `points`.
 * 
 * You can move according to these rules:
 *     In `1` second, you can either:
 *         (a) move vertically by one unit,
 *         (b) move horizontally by one unit, or
 *         (c) move diagonally `sqrt(2)` units (in other words, move one unit
 *             vertically then one unit horizontally in `1` second).
 *     You have to visit the points in the same order as they appear in the
 *         array.
 *     You are allowed to pass through points that appear later in the order,
 *         but these do not count as visits.
 */

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize) {
    /* O(n) time, O(1) space solution */
    int total = 0;
    for (int i = 1; i < pointsSize; i++) {
        unsigned dx = abs(points[i][0] - points[i - 1][0]);
        unsigned dy = abs(points[i][1] - points[i - 1][1]);
        total = total + max(dx, dy);
    }
    return total;
}