/*
 * 1980. Find Unique Binary String
 * 
 * Given an array of strings `nums` containing `n` unique binary strings each
 * of length `n`, return a binary string of length `n` that does not appear in
 * `nums`. If there are multiple answers, you may return any of them.
 */

char* findDifferentBinaryString(char** nums, int numsSize) {
    /* O(n) time, O(n) space solution */
    unsigned short ans = 0xFFFF;
    unsigned short mask = 1;
    for (int i = 0; i < numsSize; i++) {
        ans ^= (nums[i][0] - 48) & mask;  /* ASCII of '0' is 48 */
        mask <<= 1;
        printf("%b\n", ans);  /* TODO: Why is `ans` not being updated? */
    }

    /* TODO: create and return char* array */
    return "0";
}