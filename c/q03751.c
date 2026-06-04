/*
 * 3751. Total Waviness of Numbers in Range I
 * 
 * You are given two integers `num1` and `num2` representing an inclusive range
 * `[num1, num2]`.
 * 
 * The waviness of a number is defined as the total count of its peaks and valleys:
 *     A digit is a peak if it is strictly greater than both of its immediate
 *         neighbors.
 *     A digit is a valley if it is strictly less than both of its immediate
 *         neighbors.
 *     The first and last digits of a number cannot be peaks or valleys.
 *     Any number with fewer than 3 digits has a waviness of 0.
 * 
 * Return the total sum of waviness for all numbers in the range `[num1, num2]`. 
 */

int totalWaviness(int num1, int num2) {
    /* O(n * m) time, O(1) space solution */
    int total = 0;
    for (int num = num1; num <= num2; num++) {
        int n = num;
        while (n >= 100) {
            int d = (n % 10);
            int c = (n % 100) / 10;
            int m = (n % 1000) / 100;

            total += ((m - c) * (c - d) < 0);

            n = n / 10;
        }
    }
    return total;
}