"""
2425. Bitwise XOR of All Pairings

You are given two 0-indexed arrays, `nums1` and `nums2`, consisting of non-
negative integers. There exists another array, `nums3`, which contains the
bitwise XOR of all pairings of integers between `nums1` and `nums2` (every
integer in `nums1` is paired with every integer in `nums2` exactly once).

Return the bitwise XOR of all integers in `nums3`.
"""

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Naive O(m * n) time, O(1) space solution, where m = len(nums1) and
        n = len(nums2); TOO SLOW
        """
        result = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                result ^= nums1[i] ^ nums2[j]
        return result

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        O(m + n) time, O(1) space solution, where m = len(nums1) and n = len(nums2)
        
        Strategy:
        We want to first compute nums3 = [
            a_0 ^ b_0, a_0 ^ b_1, ...,
            a_1 ^ b_0, a_1 ^ b_1, ...,
                .          .       .
        ] where a_i, b_j = nums1[i], nums2[j]. Then, we take all of the
        elements of nums3 and XOR them together. Since XOR is commutative, it
        only matters how many of each number are in the final calculation.
        There will be len(nums2) occurrences of nums1[0], len(nums2) of
        nums1[1], etc. Likewise, there will be len(nums1) occurences of
        nums2[0], etc. Lastly, XOR is its own inverse; that is, z ^ z = 0 for
        all z. Therefore, if there are an even number of occurrences of any
        number, its contribution to the final result will be zero.
        """
        result = 0  # 0 is the identity element for XOR
        if len(nums1) & 1:  # if len(nums1) is odd...
            for n in nums2:
                result ^= n  # ...XOR all elements of `nums2` (NOT `nums1`!) into `result`
        if len(nums2) & 1:
            for n in nums1:
                result ^= n
        return result