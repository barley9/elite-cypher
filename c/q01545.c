/*
 * 1545. Find Kth Bit in Nth Binary String
 * 
 * Given two positive integers `n` and `k`, the binary string `S_n` is formed
 * as follows:
 *     `S_1 = "0"`
 *     `S_i = S_i - 1 + "1" + reverse(invert(S_i - 1))` for `i > 1`
 * 
 * Where `+` denotes the concatenation operation, `reverse(x)` returns the
 * reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0`
 * changes to `1` and `1` changes to `0`).
 * 
 * For example, the first four strings in the above sequence are:
 *     `S_1 = "0"`
 *     `S_2 = "011"`
 *     `S_3 = "0111001"`
 *     `S_4 = "011100110110001"`
 * 
 * Return the `k`th bit in `S_n`. It is guaranteed that `k` is valid for the
 * given `n`.
 */

char findKthBit(int n, int k) {
    /* O(n) time, O(1) space solution */
    if (n == 1) {
        return '0';
    }

    int mid = 1 << (n - 1);
    if (k == mid) {
        return '1';
    }

    if (k < mid) {
        return findKthBit(n - 1, k);
    }

    int rev = (1 << n) - 1;
    char bit = findKthBit(n - 1, rev);

    return (bit == '1') ? '0' : '1';
}