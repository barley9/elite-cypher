"""
645. Set Mismatch

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        O(3 * n) solution using some sets and some math
        """
        # find which number was overwritten using set difference
        for missing in set(range(1, len(nums) + 1)) - set(nums):
            break
        
        # find which number was duplicated using modified math trick
        duplicate = sum(nums) + missing - (len(nums) * (len(nums) + 1)) // 2

        return [duplicate, missing]