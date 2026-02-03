"""
3637. Trionic Array I

You are given an integer array `nums` of length `n`.

An array is trionic if there exist indices `0 < p < q < n − 1` such that:
    `nums[0...p]` is strictly increasing,
    `nums[p...q]` is strictly decreasing,
    `nums[q...n − 1]` is strictly increasing.

Return `true` if `nums` is trionic, otherwise return `false`.
"""

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        """O(2*n) time, O(n) space solution"""
        diffs = [
            nums[i] - nums[i - 1]
            for i in range(1, len(nums))
        ]

        # print(diffs)

        p = 0
        while p < len(diffs) and diffs[p] > 0:
            p += 1
        if p == 0 or p >= len(diffs):
            return False

        q = p
        while q < len(diffs) and diffs[q] < 0:
            q += 1
        if q == p or q >= len(diffs):
            return False

        r = q
        while r < len(diffs) and diffs[r] > 0:
            r += 1
        if r == q or r < len(diffs):
            return False

        return True

    def isTrionic(self, nums: List[int]) -> bool:
        """O(n) time, O(1) space solution"""
        if len(nums) < 4:
            return False
        if nums[1] - nums[0] <= 0:
            return False
        if nums[-1] - nums[-2] <= 0:
            return False

        mode = 0  # even == increasing, odd == decreasing
        i = 1
        while i < len(nums):
            d = nums[i] - nums[i - 1]
            if (mode & 1 == 0) and (d > 0):
                i += 1
            elif (mode & 1 == 1) and (d < 0):
                i += 1
            elif d == 0:
                return False
            else:
                mode += 1
            # print(i, d, mode)
        
        return mode == 2  # array switches between incr./decr. exactly twice