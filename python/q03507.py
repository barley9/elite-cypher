"""
3507. Minimum Pair Removal to Sort Array I

Given an array `nums`, you can perform the following operation any number of
times:
    Select the adjacent pair with the minimum sum in `nums`. If multiple such
        pairs exist, choose the leftmost one.
    Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-
decreasing.

An array is said to be non-decreasing if each element is greater than or equal
to its previous element (if it exists).
"""

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """O(n^2) time, O(1) space solution"""
        for steps in range(len(nums)):
            # Search for decreasing pair of elements
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    break
            else:
                return steps

            # Locate minimum pair sum
            min_idx = None
            min_sum = 10 ** 7
            for i in range(1, len(nums)):
                if nums[i - 1] + nums[i] < min_sum:
                    min_sum = nums[i - 1] + nums[i]
                    min_idx = i
            
            # Remove pair; replace with sum
            nums[min_idx - 1] += nums[min_idx]
            del nums[min_idx]
        
        return -1