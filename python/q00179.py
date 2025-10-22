"""
179. Largest Number

Given a list of non-negative integers `nums`, arrange them such that they form
the largest number and return it.

Since the result may be very large, so you need to return a string instead of
an integer.
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        O(n log n) time, O(n) space partial solution. It would work as-is, but
        I'd need to sort '3' after '30' without altering any other ordering
        property. Can't figure out how to do that yet.
        """
        nums = [str(n) for n in nums]
        return ''.join(sorted(nums, reverse=True))