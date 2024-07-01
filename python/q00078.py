"""
78. Subsets

Given an integer array `nums` of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any
order.
"""

import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        O(2 ** n) space, O(2 ** n) time solution taken from
        https://docs.python.org/3/library/itertools.html
        """
        return itertools.chain.from_iterable(
            itertools.combinations(nums, r) for r in range(len(nums) + 1)
        )

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        O(2**n) time, O(2**n) space RYO solution using loops and element
        masking. Actually faster than using `itertools` recipe.
        """
        result = []
        for n in range(2 ** len(nums)):  # use `n` as mask for elements in `nums`
            subset = []
            i = 0
            while n > 0:  # for every bit in `n`...
                if n & 1:  # ...add corresponding element to `subset` if LSB = 1
                    subset.append(nums[i])
                i += 1  # increment index into `nums`
                n = n >> 1
            result.append(subset)
        return result