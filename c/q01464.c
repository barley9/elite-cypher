/*
 * 1464. Maximum Product of Two Elements in an Array
 * 
 * Given the array of integers `nums`, you will choose two different indices `i`
 * and `j` of that array. Return the maximum value of `(nums[i]-1)*(nums[j]-1)`. 
 */

int maxProduct(int* nums, int numsSize) {
    int i, j, mi, mj;

    /* (I dunno if these multiple-assignments are good style) */
    i = j = -1;    /* indices of largest, 2nd largest value */
    mi = mj = -1;  /* values of largest, 2nd largest value */

    for (int k = 0; k < numsSize; k++) {
        if (nums[k] >= mi) {
            mj = mi;  /* demote largest to 2nd largest */
            j = i;
            mi = nums[k];  /* save new largest */
            i = k;
        } else if (nums[k] >= mj) {
            mj = nums[k];
            j = k;
        }
    }

    return (mi - 1) * (mj - 1);
}