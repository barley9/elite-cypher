"""
3876. Construct Uniform Parity Array II

You are given an array `nums1` of `n` distinct integers.

You want to construct another array `nums2` of length `n` such that the
elements in `nums2` are either all odd or all even.

For each index `i`, you must choose exactly one of the following (in any
order):
    `nums2[i] = nums1[i]​​​​​​​`
    `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`, such that
        `nums1[i] - nums1[j] >= 1`

Return `true` if it is possible to construct such an array, otherwise return
`false`.
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        """O(n) time, O(1) space solution"""
        INF = 10 ** 7

        # Find smallest even and odd numbers in array
        min_even = INF
        min_odd  = INF
        for n in nums1:
            if (n & 1):
                if (n < min_odd): min_odd = n
            else:
                if (n < min_even): min_even = n

        # If array is already either all odd or all even, return True
        if (min_odd == INF) or (min_even == INF):
            return True
        
        # If the smallest odd element is bigger than the smallest even element,
        # we can't satisfy the property
        return min_odd < min_even

    def uniformArray(self, nums1: list[int]) -> bool:
        """O(n) time, O(1) space solution"""
        m = min(nums1)  # find minimum value in `nums1`

        # If min is odd, we're done
        if m & 1:
            return True
        
        # If instead the min is even, we know that either the entire array is
        # even (which allows us to satisfy the required property) or there is
        # at least one odd element (which makes satisfying the property
        # impossible)
        for n in nums1:
            if n & 1:
                return False
        
        return True