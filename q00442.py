"""
442. Find All Duplicates in an Array

Given an integer array `nums` of length `n` where all the integers of `nums` are
in the range `[1, n]` and each integer appears once or twice, return an array of
all the integers that appears twice.

You must write an algorithm that runs in `O(n)` time and uses only constant
extra space.
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        O(n) time, O(n) space solution using negation to mark previously seen
        indices
        """
        result = []
        for i in nums:
            absi = abs(i)
            if nums[absi - 1] > 0:
                nums[absi - 1] *= -1
            else:
                result.append(absi)
        return result

    def findDuplicates(self, nums: List[int]) -> List[int]:
        """O(n) time, O(n) space solution using builtin collections.Counter"""
        from collections import Counter
        return [n for n, count in Counter(nums).items() if count == 2]