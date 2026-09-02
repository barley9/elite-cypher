"""
3875. Construct Uniform Parity Array I

You are given an array `nums1` of `n` distinct integers.

You want to construct another array `nums2` of length `n` such that the
elements in `nums2` are either all odd or all even.

For each index `i`, you must choose exactly one of the following (in any
order):
    `nums2[i] = nums1[i]`
    `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`

Return `true` if it is possible to construct such an array, otherwise, return
`false`.
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        """
        O(1) time, O(1) space solution
        
        If `nums1[i]` is even for all `i`, or odd for all `i`, we could just
        let `nums2 = nums1`.
        
        If `nums1` is all even except for one odd element at index `j`, then we
        let `nums2[i] = nums1[i] - nums1[j]` for all `i != j`. Finally we let
        `nums2[j] = nums1[j]`. Now, because the difference between an even
        number and an odd number is odd, every element of `nums2` is odd.

        We can use the above strategy (with trivial modification) for any other
        ratio of even/odd elements.

        Therefore, no matter the contents of `nums1`, we can always form a
        `nums2` with the required property.
        """
        return True