"""
1018. Binary Prefix Divisible By 5

You are given a binary array `nums` (0-indexed).

We define `x_i` as the number whose binary representation is the subarray
`nums[0..i]` (from most-significant-bit to least-significant-bit).

For example, if `nums = [1,0,1]`, then `x_0 = 1`, `x_1 = 2`, and `x_2 = 5`.

Return an array of booleans `answer` where `answer[i]` is `true` if `x_i` is
divisible by 5.
"""

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """O(2 * n) time, O(n) space solution"""
        answer = [0]
        for bit in nums:
            answer.append((answer[-1] << 1) | bit)
        return [
            answer[i] % 5 == 0
            for i in range(1, len(answer))
        ]

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """O(n) time, O(n) space solution"""
        n = nums[0]
        answer = [False] * len(nums)
        answer[0] = (n % 5 == 0)
        for i in range(1, len(nums)):
            n = (n << 1) | nums[i]
            answer[i] = (n % 5 == 0)
        return answer

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """O(n) time, O(1) space solution. Mutates input list."""
        n = nums[0]
        for i in range(1, len(nums)):
            n = (n << 1) | nums[i]
            nums[i] = (n % 5 == 0)
        nums[0] = not bool(nums[0])
        return nums