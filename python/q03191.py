"""
3191. Minimum Operations to Make Binary Array Elements Equal to One I

You are given a binary array `nums`.

You can do the following operation on the array any number of times (possibly zero):
    Choose any 3 consecutive elements from the array and flip all of them.

Flipping an element means changing its value from `0` to `1`, and from `1` to `0`.

Return the minimum number of operations required to make all elements in nums
equal to `1`. If it is impossible, return `-1`.
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if nums.count(0) % 3 != 0:
            return -1
        
        steps = 0
        found_zero = False
        ones_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                found_zero = True
                if ones_count % 3 != 0:
                    return -1
                steps += 2 * (ones_count // 3)
                ones_count = 0
            elif found_zero:
                ones_count += 1

        return steps + 1

    def minOperations(self, nums: List[int]) -> int:
        """
        O(n) time, O(1) space solution; INCORRECT
        
        Strategy:
        We want to group the `0`s together, then flip three of them at a time
        to make the array all `1`s. The provided operation essentially amounts
        to percolating `0`s past the other elements in the array. There can
        only be a solution if the number of `0`s in `nums` is a multiple of 3.
        Further, the number of `1`s separating each pair of `0`s must also be
        a multiple of 3. Therefore, use a FSM-like pattern to detect these
        patterns.

        TODO: Fails for inputs like [1,0,0,1,1,0,1,1,1,0,0,0,1,0,1]; returns -1 instead of correct answer 9
        """
        steps, ones_count, zeros_count = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_count += 1
                q, r = divmod(ones_count, 3)
                if r != 0: return -1
                steps += 2 * q
                ones_count = 0
            elif zeros_count:
                ones_count += 1

        return (steps + 1) if (zeros_count % 3 == 0) else -1