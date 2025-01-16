/**********
 * 2425. Bitwise XOR of All Pairings
 *
 * You are given two 0-indexed arrays, `nums1` and `nums2`, consisting of non-
 * negative integers. There exists another array, `nums3`, which contains the
 * bitwise XOR of all pairings of integers between `nums1` and `nums2` (every
 * integer in `nums1` is paired with every integer in `nums2` exactly once).
 * 
 * Return the bitwise XOR of all integers in `nums3`.
 **********/

int xorAllNums(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    /* O(m + n) time, O(1) space solution, where m = nums1Size and n = nums2Size */
    unsigned ans = 0;
    if (nums1Size & 1) {
        for (int i = 0; i < nums2Size; i++) {
            ans ^= nums2[i];
        }
    }
    if (nums2Size & 1) {
        for (int i = 0; i < nums1Size; i++) {
            ans ^= nums1[i];
        }
    }
    return ans;
}