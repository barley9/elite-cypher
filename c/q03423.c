/*
 * 3423. Maximum Difference Between Adjacent Elements in a Circular Array
 *
 * Given a circular array `nums`, find the maximum absolute difference between
 * adjacent elements.
 *
 * Note: In a circular array, the first and last elements are adjacent.
 */

int maxAdjacentDistance_(int* nums, int numsSize) {
    /* O(n) time, O(1) space solution */
    
    int max_diff = -1000;  /* negative infinity */
    
    /* Check standard adjacencies */
    int d;
    for (int i = 1; i < numsSize; i++) {
        d = nums[i] - nums[i - 1];  /* difference */
        d = (d < 0) ? -d : d;  /* absolute value */
        if (d > max_diff) {
            max_diff = d;
        }
    }

    /* Check circular adjacency */
    d = nums[0] - nums[numsSize - 1];
    d = (d < 0) ? -d : d;
    if (d > max_diff) {
        max_diff = d;
    }

    return max_diff;
}

int maxAdjacentDistance(int* nums, int numsSize) {
    /* O(n) time, O(1) space solution */
    
    int max_diff = -1000;  /* negative infinity */
    
    /* Check standard adjacencies */
    int d;
    for (int i = 1; i < numsSize; i++) {
        d = (nums[i] < nums[i - 1]) ? (nums[i - 1] - nums[i]) : (nums[i] - nums[i - 1]);
        if (d > max_diff) {
            max_diff = d;
        }
    }

    /* Check circular adjacency */
    d = (nums[0] < nums[numsSize-1]) ? (nums[numsSize-1] - nums[0]) : (nums[0] - nums[numsSize-1]);
    if (d > max_diff) {
        max_diff = d;
    }

    return max_diff;
}