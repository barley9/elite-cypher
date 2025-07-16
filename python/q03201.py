"""
3201. Find the Maximum Length of Valid Subsequence I

You are given an integer array `nums`. A subsequence `sub` of `nums` with
length `x` is called valid if it satisfies:
    `(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2`.

Return the length of the longest valid subsequence of `nums`.

(A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.)
"""

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [n & 1 for n in nums]
        num_odd = sum(nums)
        num_evn = len(nums) - num_odd
        print(num_odd, num_evn)

        num_alt = 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                num_alt += 1
                i = j
            j += 1
        print(num_alt)

        return max(num_odd, num_evn, num_alt)

    @staticmethod
    def max3(a: int, b: int, c: int) -> int:
        if a > b:
            if a > c: return a
            else: return c
        else:
            if b > c: return b
            else: return c

    def maximumLength(self, nums: List[int]) -> int:
        num_odd = sum(n & 1 for n in nums)
        num_evn = len(nums) - num_odd
        num_alt = 1
        i = 0
        for j in range(1, len(nums)):
            if (nums[i] ^ nums[j]) & 1:
                num_alt += 1
                i = j
        return self.max3(num_odd, num_evn, num_alt)
        
    def maximumLength(self, nums: List[int]) -> int:
        """
        O(n) time, O(1) space solution
        
        Observations:
            Subsequence must either be all even, all odd, or alternating even-odd
            Could represent `nums` as sequence of bits
        """
        num_odd = nums[0] & 1
        num_alt = 1
        i = 0
        for j in range(1, len(nums)):
            num_odd += nums[j] & 1
            if (nums[i] ^ nums[j]) & 1:
                num_alt += 1
                i = j
        num_evn = len(nums) - num_odd
        return self.max3(num_odd, num_evn, num_alt)