"""
1464. Maximum Product of Two Elements in an Array

Given the array of integers `nums`, you will choose two different indices `i`
and `j` of that array. Return the maximum value of `(nums[i]-1)*(nums[j]-1)`. 
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

    def maxProduct(self, nums: List[int]) -> int:
        """INCORRECT; fails when max is at `nums[0]`"""
        i, j = 0, 0  # indices of largest, 2nd largest element
        
        for k in range(len(nums)):
            if nums[k] >= nums[i]:
                j = i  # demote previous largest to 2nd largest
                i = k  # save new largest
            elif nums[k] >= nums[j]:
                j = k

        print(nums[i], nums[j])

        return (nums[i] - 1) * (nums[j] - 1)

    def maxProduct(self, nums: List[int]) -> int:
        """O(n) time, O(1) space solution"""
        i, j = None, None  # indices of largest, 2nd largest element
        mi, mj = -1, -1  # values of largest, 2nd largest element
        
        for k, n in enumerate(nums):
            if n >= mi:
                mj, j = mi, i  # demote previous largest to 2nd largest
                mi, i = n, k  # save new largest
            elif n >= mj:
                mj, j = n, k
            # print(f"\tnums[{i}] = {mi}, nums[{j}] = {mj}")

        # print(mi, mj)
        
        return (mi - 1) * (mj - 1)