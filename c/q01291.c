/*
 * 1291. Sequential Digits
 * 
 * An integer has sequential digits if and only if each digit in the number is
 * one more than the previous digit.
 * 
 * Return a sorted list of all the integers in the range `[low, high]` inclusive
 * that have sequential digits.
 */

int pow_ten(int p) {
    int result = 1;
    for (int i = 0; i < p; i++) {
        result = result * 10;
    }
    return result;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* sequentialDigits(int low, int high, int* returnSize) {
    /* O(1) time, O(1) space solution */

    int* result = malloc(sizeof(int) * 9 * 9);  /* lazy size over-estimate */

    int N = 123456789;
    int i = 0;  /* index into `result` */
    int temp;
    for (int stride = 2; stride < 9 + 1; stride++) {
        for (int start = 9 - stride; start >= 0; start--) {
            temp = (N % pow_ten(start + stride)) / pow_ten(start);
            if ((low <= temp) && (temp <= high)) {
                result[i] = temp;
                i++;
            }
        }
    }

    *returnSize = i;
    return result;
}