/*
 * 3754. Concatenate Non-Zero Digits and Multiply by Sum I
 * 
 * You are given an integer `n`.
 * 
 * Form a new integer `x` by concatenating all the non-zero digits of `n` in
 * their original order. If there are no non-zero digits, `x = 0`.
 * 
 * Let `sum` be the sum of digits in `x`.
 * 
 * Return an integer representing the value of `x * sum`.
 */

long long sumAndMultiply(int n) {
    /* O(2 log n) time, O(log n) space solution */

    int digits[10] = {0};  /* `n <= 10**9` so we're safe */
    int i = 0;  /* index into `digits` */
    long long sum = 0;  /* not sure if `long long` necessary? */

    while (n) {
        int q = n / 10;
        int r = n % 10;
        if (r != 0) {
            sum += r;
            digits[i] = r;
            i++;  /* `i` won't overflow `digits` b/c `n <= 10**9` */
        }
        n = q;
    }

    /* Assemble `x` from `digits` */
    long long x = 0;
    while (i > 0) {  /* reuse `i`; it already points to the end of `digits` */
        i--;
        x = 10 * x + digits[i];
    }

    return x * sum;
}