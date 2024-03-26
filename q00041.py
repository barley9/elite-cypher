"""
41. First Missing Positive

Given an unsorted integer array `nums`. Return the smallest positive integer
that is not present in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)`
auxiliary space.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """O(n) time, O(n) space solution"""
        s = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in s: return i

    def firstMissingPositive(self, nums: List[int]) -> int:
        """Another O(n) time, O(n) space solution"""
        seen = [False] * (len(nums) + 2)
        for n in nums:
            if n > 0 and n < len(seen):
                seen[n] = True
        for i in range(1, len(seen)):
            if i < len(seen) and not seen[i]:
                return i

    def firstMissingPositive(self, nums: List[int]) -> int:
        """implement cycle sort"""
        pass