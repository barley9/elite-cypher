/*
 * 3876. Construct Uniform Parity Array II
 * 
 * You are given an array `nums1` of `n` distinct integers.
 * 
 * You want to construct another array `nums2` of length `n` such that the
 * elements in `nums2` are either all odd or all even.
 * 
 * For each index `i`, you must choose exactly one of the following (in any
 * order):
 *     `nums2[i] = nums1[i]​​​​​​​`
 *     `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`, such that
 *         `nums1[i] - nums1[j] >= 1`
 * 
 * Return `true` if it is possible to construct such an array, otherwise return
 * `false`.
 */

#include <limits.h>

int min(int* arr, int size) {
    int m = INT_MAX;

    for (int i = 0; i < size; i++) {
        if (arr[i] < m) {
            m = arr[i];
        }
    }

    return m;
}

bool uniformArray(int* nums1, int nums1Size) {
    /* O(2n) time, O(1) space solution */
    int m = min(nums1, nums1Size);  /* TODO: could combine loops? */

    if (m & 1) {
        return true;
    }

    for (int i = 0; i < nums1Size; i++) {
        if (nums1[i] & 1) {
            return false;
        }
    }

    return true;
}