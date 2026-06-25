"""
3737. Count Subarrays With Majority Element I

You are given an integer array `nums` and an integer `target`.

Return the number of of `nums` in which `target` is the majority element.

The majority element of a subarray is the element that appears strictly more
than half of the times in that subarray.
"""

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """SCRATCH-WORK"""
        # The other values in `nums` don't matter, only the positions of `target`
        target_positions = []
        for i, n in enumerate(nums):
            if n == target:
                target_positions.append(i)

        targets_running_total = [0]
        running_total = 0
        for i in range(len(nums)):
            if nums[i] == target:
                running_total += 1
            targets_running_total.append(running_total)

        print(targets_running_total)

        if len(target_positions) == 0:
            return 0
        
        # print(target_positions)
        # How many subarrays contain 1 target value?
        # How many subarrays contain 2 target values?
        # How many subarrays contain n target values?

        # Generate all subarrays in increasing order of length
        # Subarray must be less than twice the number of `target` values in `nums` so that `target` can be a majority element
        result = 0
        for stride in range(1, 2 * len(target_positions)):
            for start in range(len(nums) - stride + 1):
                # Check how many `target` values are in range
                print(start, stride, nums[start:start + stride])
                if (targets_running_total[start + stride] - targets_running_total[start]) > (stride // 2):
                    result += 1

        return result

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """O(n^2) time, O(n) space solution"""
        # The other values in `nums` don't matter, only the positions of `target`
        # We want to be able to quickly calculate how many `target` lie within an interval
        counts = [0]  # running total at each index
        count = 0  # running total of number of occurances of `target`
        for n in nums:
            if n == target:
                count += 1
            counts.append(count)
        
        # Generate all subarrays in increasing order of length, and not longer
        # than 2 * (total occurances of `target`) - 1
        result = 0
        for stride in range(1, 2 * counts[-1]):
            for start in range(len(nums) - stride + 1):
                # Check how many `target` values are in range
                if (counts[start + stride] - counts[start]) > (stride // 2):
                    result += 1

        return result