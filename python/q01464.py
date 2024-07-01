"""
1464. Maximum Product of Two Elements in an Array

Given the array of integers `nums`, you will choose two different indices `i` and `j` of that array. Return the maximum value of `(nums[i]-1)*(nums[j]-1)`. 
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Naive O(n^2) algorithm checking every pair"""
        result = -10 ** 7  # -infinity
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                p = (nums[i] - 1) * (nums[j] - 1)
                if p > result:
                    result = p
        return result

    def maxProduct(self, nums: List[int]) -> int:
        """O(n) algorithm keeping track of maximum two elements"""
        maxtwo = [-10 ** 7, -10 ** 7]  # store [biggest, 2nd biggest] elements
        for n in nums:
            if n > maxtwo[0]:
                maxtwo[1] = maxtwo[0]
                maxtwo[0] = n
            elif n > maxtwo[1]:
                maxtwo[1] = n
            
        return (maxtwo[0] - 1) * (maxtwo[1] - 1)