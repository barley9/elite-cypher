/*
 * 2206. Divide Array Into Equal Pairs
 *
 * You are given an integer array `nums` consisting of `2 * n` integers.
 *
 * You need to divide `nums` into `n` pairs such that:
 *     Each element belongs to exactly one pair.
 *     The elements present in a pair are equal.
 *
 * Return true if `nums` can be divided into `n` pairs, otherwise return `false`.
 */

#define VALUE_RANGE 501

bool divideArray(int* nums, int numsSize) {
    /* Initialize counts array to all zeros */
    int counts[VALUE_RANGE] = {0};
    
    /*
     * For each value `n` in `nums`, toggle value of counts[n] to keep track
     * of whether we've seen `n` an even or odd number of times
     */
    for (int i = 0; i < numsSize; i++) {
        counts[nums[i]] ^= 1;
    }
    
    /* If any appear an odd number of times, it is impossible to divide `nums` */
    for (int j = 0; j < VALUE_RANGE; j++) {
        if (counts[j] == 1) {
            return false;
        }
    }
    return true;
}