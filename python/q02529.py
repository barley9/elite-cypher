"""
2529. Maximum Count of Positive Integer and Negative Integer

Given an array `nums` sorted in non-decreasing order, return the maximum
between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in `nums` is `pos` and the
number of negative integers is `neg`, then return the maximum of `pos` and
`neg`.

Note that `0` is neither positive nor negative.
"""

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """O(n) time, O(1) space solution"""
        pos_count = 0
        neg_count = 0
        for n in nums:
            if n > 0:
                pos_count += 1
            elif n < 0:
                neg_count += 1
        return pos_count if pos_count > neg_count else neg_count

    # Alternatively, we could use a binary search strategy to find the index
    # dividing the negative values from the positive, but it would likely
    # require some recursion and I'm not sure that it would end up being faster.