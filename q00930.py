"""
930. Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of non-empty
subarrays with a sum goal.

A subarray is a contiguous part of the array.
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """O(n^3) solution; much too slow"""
        total = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                total += (sum(nums[i:j]) == goal)

        return total

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """O(n^2) solution; still too slow"""
        total = 0
        for i in range(len(nums)):
            s = nums[i]  # keep a running sum of elements
            if s == goal:
                total += 1
            for j in range(i + 1, len(nums)):
                s += nums[j]
                if s == goal:
                    total += 1
                elif s > goal:
                    break
        return total

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # pre-process `nums` list using run-length encoding (RLE)
        rle = []
        run = [nums[0], 0, 0]  # [digit, run start index, run length]
        for i in range(len(nums)):
            if nums[i] == run[0]:
                run[2] += 1
            else:
                rle.append(tuple(run))
                run = [nums[i], i, 1]
        rle.append(tuple(run))

        print(len(nums), len(rle), len(rle) / len(nums))
        for run in rle:
            print('digit: {}, start: {}, length: {}'.format(*run))

        result = 0
        for i in range(len(rle) - 1):
            for j in range(i + 1, len(rle)):
                pass

        return 0