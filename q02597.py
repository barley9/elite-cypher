"""
2597. The Number of Beautiful Subsets

You are given an array `nums` of positive integers and a positive integer `k`.

A subset of `nums` is beautiful if it does not contain two integers with an
absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array `nums`.

A subset of `nums` is an array that can be obtained by deleting some (possibly
none) elements from `nums`. Two subsets are different if and only if the chosen
indices to delete are different.
"""

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """
        O(2**n) time, O(2**n) space RYO solution; mostly copied from
        Problem 78: Subsets.
        """
        result = []
        for n in range(1, 2 ** len(nums)):  # use `n` as mask for elements in `nums`
            subset = []
            i = 0
            while n > 0:  # for every bit in `n`...
                if n & 1:  # ...add corresponding element to `subset` if LSB = 1
                    subset.append(nums[i])
                i += 1  # increment index into `nums`
                n = n >> 1
            
            # Check if subset is 'beautiful'
            for i in range(len(subset) - 1):
                for j in range(i + 1, len(subset)):
                    if abs(subset[i] - subset[j]) == k:
                        break
                else:
                    continue
                break
            else:
                result.append(subset)  # if we didn't break anywhere
                
        return len(result)

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """
        O(2**n) time, O(2**n) space solution; much too slow.
        """
        # Generate all subsets (except empty set)
        count = 0
        for n in range(1, 2 ** len(nums)):  # use `n` as mask for elements in `nums`
            subset = []
            i = 0
            while n > 0:  # for every bit in `n`...
                if n & 1:  # ...add corresponding element to `subset` if LSB = 1
                    subset.append(nums[i])
                i += 1  # increment index into `nums`
                n = n >> 1
            
            # Check if subset is 'beautiful'
            for i in range(len(subset) - 1):
                for j in range(i + 1, len(subset)):
                    if abs(subset[i] - subset[j]) == k:
                        break
                else:
                    continue
                break
            else:
                count += 1
                
        return count

    ##########################################

    def factorial(n: int) -> int:
        if n < 2:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def combinations(n: int, k: int) -> int:
        return factorial(n) // (factorial(k) * factorial(n - k))

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ugly_pairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    ugly_pairs += 1
        
        2 ** len(nums) - 1  # all non-empty subsets
        
