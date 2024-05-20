"""
1863. Sum of All Subset XOR Totals

The XOR total of an array is defined as the bitwise `XOR` of all its elements,
or `0` if the array is empty.

    For example, the XOR total of the array [2,5,6] is `2 XOR 5 XOR 6 = 1`.

Given an array `nums`, return the sum of all XOR totals for every subset of
`nums`. 

Note: Subsets with the same elements should be counted multiple times.

An array `a` is a subset of an array `b` if `a` can be obtained from `b` by
deleting some (possibly zero) elements of `b`.
"""


import itertools


class Solution:
    @staticmethod
    def powerset(iterable):
        """powerset([1,2,3]) -> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
        s = list(iterable)
        return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for s in self.powerset(nums):  # for every subset...
            x = 0b00000000
            for n in s:  # ...compute XOR total...
                x ^= n
            result += x  # ...and add it to result
        return result

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = sum(nums)
        for s in itertools.chain.from_iterable(itertools.combinations(nums, r) for r in range(2, len(nums) + 1)):
            x = 0
            for n in s:
                x ^= n
            result += x
        return result

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        # Capture each bit that is set in any of the elements
        for num in nums:
            result |= num
        # Multiply by the number of subset XOR totals that will have each bit set
        return result << (len(nums) - 1)