/*
 * 3201. Find the Maximum Length of Valid Subsequence I
 * 
 * You are given an integer array `nums`. A subsequence `sub` of `nums` with
 * length `x` is called valid if it satisfies:
 *     `(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2`.
 * 
 * Return the length of the longest valid subsequence of `nums`.
 * 
 * (A subsequence is an array that can be derived from another array by deleting
 * some or no elements without changing the order of the remaining elements.)
 */

int max3(int a, int b, int c) {
    if (a > b) {
        if (a > c) {
            return a;
        } else {
            return c;
        }
    } else {
        if (b > c) {
            return b;
        } else {
            return c;
        }
    }
}

int maximumLength(int* nums, int numsSize) {
    /* O(n) time, O(1) space solution */
    int num_odd = nums[0] & 1;
    int num_alt = 1;
    int i = 0;
    for (int j = 1; j < numsSize; j++) {
        num_odd = num_odd + (nums[j] & 1);
        if ((nums[i] ^ nums[j]) & 1) {
            num_alt++;
            i = j;
        }
    }
    return max3(num_odd, numsSize - num_odd, num_alt);
}