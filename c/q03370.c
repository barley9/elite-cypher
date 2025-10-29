/*
 * 3370. Smallest Number With All Set Bits
 * 
 * You are given a positive number `n`.
 * 
 * Return the smallest number `x` greater than or equal to `n`, such that the
 * binary representation of `x` contains only set bits.
 */

int smallestNumber(int n) {
    /* O(log n) time, O(1) space */
    int bit_length = 0;
    while (n > 0) {
        bit_length++;
        n = n >> 1;
    }

    /* printf("%i\n", bit_length); */

    return (1 << bit_length) - 1;
}