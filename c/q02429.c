/**********
2429. Minimize XOR

Given two positive integers `num1` and `num2`, find the positive integer `x`
        such that:
    `x` has the same number of set bits as `num2`, and
    The value `x XOR num1` is minimal.

Note that XOR is the bitwise XOR operation.

Return the integer `x`. The test cases are generated such that `x` is uniquely
determined.

The number of set bits of an integer is the number of `1`'s in its binary
representation.
**********/

int pop_count(int n) {
    /* 
     * Helper function to count and return the number of non-zero bits in `n`
     * O(log(n)) time, O(1) space
     */
    int ans = 0;
    while (n) {
        if (n & 1) {
            ans++;
        }
        n = n >> 1;
    }
    return ans;
}

int msb(unsigned int n) {
    /*
     * Helper function to calculate the index of the most significant non-zero bit of `n`
     * See <https://stackoverflow.com/questions/671815>
     * O(log(n)) time, O(1) space
     */
    unsigned int ans = 0;
    while (n >>= 1) {
        ans++;  // bit-shift right until n = 0; the number of iterations this took is the answer
    }
    return ans;
}

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

unsigned int minimizeXor(int num1, int num2) {
    /* O(log(num1) + log(num2)) time, O(1) space solution */
    unsigned int x = 0;
    unsigned int bits = pop_count(num2);  // O(log(num2))
    unsigned int high = msb(num1);  // O(log(num1))
    for (int i = max(bits, high); i >= 0; i--) {
        if (((1 << i) & num1) || (i < bits)) {
            x |= 1 << i;
            bits--;
            if (bits <= 0) {
                break;
            }
        }
    }
    return x;
}