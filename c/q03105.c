/*
 * 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
 * You are given an array of integers nums. Return the length of the longest
 * subarray of nums which is either strictly increasing or strictly decreasing.
 */

int longestMonotonicSubarray(int* nums, int numsSize) {
    /* O(n) time, O(1) space solution */
    int inc_len = 1;
    int dec_len = 1;
    int inc_maxlen = 1;
    int dec_maxlen = 1;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i - 1] < nums[i]) {
            inc_len++;
            if (inc_len > inc_maxlen) {
                inc_maxlen = inc_len;
            }
            dec_len = 1;
        } else {
            if (nums[i - 1] > nums[i]) {
                dec_len++;
                if (dec_len > dec_maxlen) {
                    dec_maxlen = dec_len;
                }
                inc_len = 1;
            } else {
                inc_len = 1;
                dec_len = 1;
            }
        }
    }
    
    return (inc_maxlen > dec_maxlen) ? inc_maxlen : dec_maxlen;  /* (condition) ? if_TRUE : if_FALSE */
}