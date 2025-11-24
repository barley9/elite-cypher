/*
 * 1018. Binary Prefix Divisible By 5
 * 
 * You are given a binary array `nums` (0-indexed).
 * 
 * We define `x_i` as the number whose binary representation is the subarray
 * `nums[0..i]` (from most-significant-bit to least-significant-bit).
 * 
 * For example, if `nums = [1,0,1]`, then `x_0 = 1`, `x_1 = 2`, and `x_2 = 5`.
 * 
 * Return an array of booleans `answer` where `answer[i]` is `true` if `x_i` is
 * divisible by 5.
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    /* O(n) time, O(n) space solution */
    bool* answer = malloc(numsSize * sizeof(bool));
    *(returnSize) = numsSize;
    
    int n = nums[0];
    answer[0] = (n % 5 == 0);
    for (int i = 1; i < numsSize; i++) {
        n = ((n << 1) | nums[i]) % 5;
        answer[i] = (n == 0);
    }

    return answer;
}