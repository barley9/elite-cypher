/*
 * 3689. Maximum Total Subarray Value I
 * 
 * You are given an integer array `nums` of length `n` and an integer `k`.
 * 
 * You need to choose exactly `k` non-empty subarrays `nums[l..r]` of nums.
 * Subarrays may overlap, and the exact same subarray (same l and r) can be chosen
 * more than once.
 * 
 * The value of a subarray `nums[l..r]` is defined as:
 * `max(nums[l..r]) - min(nums[l..r])`.
 * 
 * The total value is the sum of the values of all chosen subarrays.
 * 
 * Return the maximum possible total value you can achieve.
 */

#include <limits.h>

long long min(int* nums, int numsSize) {
    /* Returns the MINimum value in `nums` */
    long long minimum = LLONG_MAX;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < minimum) {
            minimum = nums[i];
        }
    }
    return minimum;
}

long long max(int* nums, int numsSize) {
    /* Returns the MAXimum value in `nums` */
    long long maximum = LLONG_MIN;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maximum) {
            maximum = nums[i];
        }
    }
    return maximum;
}

long long maxTotalValue(int* nums, int numsSize, int k) {
    /* O(2n) time, O(1) space solution */
    return k * (max(nums, numsSize) - min(nums, numsSize));
}