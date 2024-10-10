"""
962. Maximum Width Ramp

A ramp in an integer array `nums` is a pair `(i, j)` for which `i < j` and
`nums[i] <= nums[j]`. The width of such a ramp is `j - i`.

Given an integer array `nums`, return the maximum width of a ramp in `nums`. If
there is no `ramp` in nums, return `0`.
"""

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """O(n^2) time, O(1) space solution by iterating over all pairs; way too slow"""
        max_width = 0
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1, i, -1):
                if (j - i > max_width) and (nums[i] <= nums[j]):
                    max_width = j - i
        return max_width

    def maxWidthRamp(self, nums: List[int]) -> int:
        """O(n^2) time, O(1) space solution with early stopping; still too slow"""
        for width in range(len(nums) - 1, 0, -1):
            for i in range(0, len(nums) - width):
                if nums[i] <= nums[i + width]:
                    return width
        return 0

    def maxWidthRamp(self, nums: List[int]) -> int:
        """O(n log n) time, O(n) space solution using sorted list of indices"""
        indices = sorted(range(len(nums)), key=lambda i: nums[i])
        min_index = len(nums)
        max_width = 0
        for i in indices:
            if i - min_index > max_width:
                max_width = i - min_index
            if i < min_index:
                min_index = i
        return max_width

    def maxWidthRamp(self, nums: List[int]) -> int:
        """O(n) time, O(n) space solution using stack"""
        stack = []
        for i in range(len(nums)):
            if (not stack) or (nums[i] <= nums[stack[-1]]):
                stack.append(i)
        
        max_width = 0

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                if i - stack[-1] > max_width:
                    max_width = i - stack[-1]
                del stack[-1]
        
        return max_width