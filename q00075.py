"""
75. Sort Colors

Given an array `nums` with `n` objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white,
and blue, respectively.

You must solve this problem without using the library's sort function.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * 3
        for n in nums:
            counts[n] += 1

        for i, j in enumerate(([0] * counts[0]) + ([1] * counts[1]) + ([2] * counts[2])):
            nums[i] = j

    def sortColors(self, nums: List[int]) -> None:
        """
        O(2*n) time, O(1) space solution
        """
        counts = [0] * 3
        for n in nums:
            counts[n] += 1
        
        i = 0  # index into counts
        for j in range(len(nums)):
            while counts[i] <= 0:
                i += 1
            nums[j] = i
            counts[i] -= 1
    
    def sortColors(self, nums: List[int]) -> None:
        """
        O(2*n) time, O(1) space solution. Still not a single pass O(n) though...
        """
        counts = [0] * 3
        for n in nums:
            counts[n] += 1
        
        i = 0  # index into nums
        for j in range(len(counts)):
            for _ in range(counts[j]):
                nums[i] = j
                i += 1