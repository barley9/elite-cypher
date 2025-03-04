/*
 * 1780. Check if Number is a Sum of Powers of Three
 *
 * Given an integer `n`, return `true` if it is possible to represent `n` as
 * the sum of distinct powers of three. Otherwise, return `false`.
 *
 * An integer `y` is a power of three if there exists an integer `x` such that
 * `y == 3 ** x`.
 */

bool checkPowersOfThree(int n) {
    /* O(log_3(n)) time, O(1) space solution */
    int q = n;
    int r = 0;
    while (q != 0) {
        r = q % 3;
        q = q / 3;
        if (r == 2) {
            return false;
        }
    }
    return true;
}