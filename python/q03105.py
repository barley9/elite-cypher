"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray

You are given an array of integers nums. Return the length of the longest
subarray of nums which is either strictly increasing or strictly decreasing.

def "subarray":
    A subarray is a contiguous non-empty sequence of elements within an array.
def "strictly increasing":
    An array is said to be strictly increasing if each element is strictly
    greater than its previous one (if exists).
def "strictly decreasing":
    An array is said to be strictly decreasing if each element is strictly
    smaller than its previous one (if exists).
"""

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """O(n) time, O(1) space solution"""
        inc_len = 1
        dec_len = 1
        inc_maxlen = 1  # length of longest INCreasing subarray
        dec_maxlen = 1  # length of longest DECreasing subarray
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc_len += 1
                if inc_len > inc_maxlen:
                    inc_maxlen = inc_len
                dec_len = 1
            elif nums[i - 1] > nums[i]:
                dec_len += 1
                if dec_len > dec_maxlen:
                    dec_maxlen = dec_len
                inc_len = 1
            else:
                inc_len = 1
                dec_len = 1
        return inc_maxlen if inc_maxlen > dec_maxlen else dec_maxlen