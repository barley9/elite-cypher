"""
3375. Minimum Operations to Make Array Values Equal to K

You are given an integer array `nums` and an integer `k`.

An integer `h` is called valid if all values in the array that are strictly
greater than `h` are identical.

For example, if `nums = [10, 8, 10, 8]`, a valid integer is `h = 9` because
all `nums[i] > 9` are equal to `10`, but `5` is not a valid integer.

You are allowed to perform the following operation on `nums`:
    Select an integer `h` that is valid for the current values in `nums`.
    For each index `i` where `nums[i] > h`, set `nums[i] to h`.

Return the minimum number of operations required to make every element in
`nums` equal to `k`. If it is impossible to make all elements equal to `k`,
return `-1`.
"""

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """O(n) time, O(1) space solution"""
        # It doesn't matter how many values are in `nums`, only whether or not
        # a value is present
        contains = [False] * 101  # 1 <= nums[i] <= 100
        for n in nums:
            contains[n] = True

        # If `k != 1` and there's a `1` in `nums`, it's impossible to convert
        # that `1` into `k` because `h` can't go lower than `1`
        if contains[1] and k > 1:
            return -1

        if any(contains[i] for i in range(k)):
            # if any values are smaller than `k` they can never get larger, so
            # converting all elements into `k` is impossible
            return -1
        else:
            # Every value in `nums` that is greater than `k` must be
            # converted. Each conversion costs one operation, so the total
            # number of operations is just the count of how many values are
            # above `k`
            return sum(contains[i] for i in range(k + 1, len(contains)))

    def minOperations(self, nums: List[int], k: int) -> int:
        """O(n) time, O(1) space solution"""
        seen = [False] * 101
        total = 0
        for n in nums:
            if n == 1 and k != 1:
                return -1
            elif n < k:
                return -1
            elif not seen[n] and n != k:
                total += 1
                seen[n] = True
        return total

    def minOperations(self, nums: List[int], k: int) -> int:
        """O(n) time, O(n) space solution"""
        nums = set(nums)
        if any(n < k for n in nums):
            return -1
        else:
            return len(nums) - (k in nums)