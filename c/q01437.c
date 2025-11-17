/*
 * 1437. Check If All 1's Are at Least Length K Places Away
 *
 * Given an binary array `nums` and an integer `k`, return `true` if all `1`'s
 * are at least `k` places away from each other, otherwise return `false`.
 */

bool kLengthApart(int* nums, int numsSize, int k) {
    /* O(n) time, O(1) space solution */
    int index_last_one = -(1 << 17);  /* 2^17 > 10^5 */
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            if (i - index_last_one <= k) {
                return false;
            }
            index_last_one = i;
        }
    }
    return true;
}