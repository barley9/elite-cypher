"""
3583. Count Special Triplets

You are given an integer array `nums`.

A special triplet is defined as a triplet of indices `(i, j, k)` such that:
    `0 <= i < j < k < n`, where `n = nums.length`
    `nums[i] == nums[j] * 2`
    `nums[k] == nums[j] * 2`

Return the total number of special triplets in the array.

Since the answer may be large, return it modulo `10^9 + 7`.
"""

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        """
        O(sodding terrible) time, O(n) space solution
        
        WAAAYY TOO SLOW
        """
        # Count how many doubles of `nums[i]` there are before and after `nums[i]` for all `1 <= i < len(nums) - 1`
        count_multiples = [
            (
                sum(n == nums[i] << 1 for n in nums[:i]),
                sum(n == nums[i] << 1 for n in nums[i + 1:])
            )
            for i in range(1, len(nums) - 1)
        ]

        # print(count_multiples)

        return sum(
            left * right
            for left, right in count_multiples
        ) % (10**9 + 7)