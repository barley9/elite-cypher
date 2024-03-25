"""
448. Find All Numbers Disappeared in an Array

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`,
return an array of all the integers in the range `[1, n]` that do not appear in
`nums`.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in s:
                result.append(i)
        return result

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """O(n) time, O(n) space solution using python sets"""
        return list(set(range(1, len(nums) + 1)) - set(nums))