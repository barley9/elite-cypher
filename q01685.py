"""
1685. Sum of Absolute Differences in a Sorted Array

You are given an integer array `nums` sorted in non-decreasing order.

Build and return an integer array `result` with the same length as `nums` such
that `result[i]` is equal to the summation of absolute differences between
`nums[i]` and all the other elements in the array.

In other words, `result[i]` is equal to `sum(|nums[i]-nums[j]|)` where
`0 <= j < nums.length` and `j != i` (0-indexed).
"""

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """Naive O(n^2) reference solution"""
        return [sum(abs(nums[i] - nums[j]) for j in range(len(nums)) if i != j) for i in range(len(nums))]

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        O(n) time, O(n) space solution by first computing array of cumulative
        sums.

        Suppose `nums = [1,3,4,4,6,7,8]`:
                     _
                   _| |
                 _| | |
                | | | |
             _ _| | | |
           _| | | | | |
          | | | | | | |
         _| | | | | | |
        |_|_|_|_|_|_|_|
         0 1 2 3 4 5 6 
        
        For example, if `i = 3`, the sum we want is
                     _
                   _|#|
                 _|#|#|
                |#|#|#|
             _ _|#|#|#|
         # #| | | | | |
         #| | | | | | |
         #| | | | | | |
        |_|_|_|_|_|_|_|
         0 1 2 3 4 5 6 
               ^
               i

        With some algebra, we can derive an expression for this area as a
        function of `i` (and `nums` of course).
        """
        # Pre-compute list of partial sums of `nums`
        cumsum = [0] * len(nums)
        s = 0
        for i in range(len(cumsum)):
            s += nums[i]
            cumsum[i] = s

        # Create result array
        result = [0] * len(nums)
        for i in range(len(result)):
            result[i] = nums[i] * i + cumsum[-1] - cumsum[i] - nums[i] * (len(nums) - 1 - i)
            if i > 0:
                result[i] -= cumsum[i - 1]
        
        return result

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """Optimized version of above function"""
        numslen = len(nums)
        total = sum(nums)
        s = 0
        result = [0] * numslen
        for i in range(numslen):
            result[i] = total - 2 * s + nums[i] * (2 * i - numslen)
            s += nums[i]
        
        return result
