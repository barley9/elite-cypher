"""
3867. Sum of GCD of Formed Pairs

You are given an integer array `nums` of length `n`.

Construct an array `prefixGcd` where for each index `i`:
    Let `mx_i = max(nums[0], nums[1], ..., nums[i])`.
    `prefixGcd[i] = gcd(nums[i], mx_i)`.

After constructing `prefixGcd`:
    Sort `prefixGcd` in non-decreasing order.
    Form pairs by taking the smallest unpaired element and the largest unpaired
        element.
    Repeat this process until no more pairs can be formed.
    For each formed pair, compute the GCD of the two elements.
    If `n` is odd, the middle element in the `prefixGcd` array remains unpaired
        and should be ignored.

Return an integer denoting the sum of the GCD values of all formed pairs.
The term `gcd(a, b)` denotes the greatest common divisor of `a` and `b`. 
"""

import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        """O(n log n + 2n) time, O(n) space solution"""
        prefixGcd = []
        mx = 0
        for n in nums:
            if n > mx:
                mx = n
            prefixGcd.append(math.gcd(mx, n))
        
        prefixGcd.sort()

        return sum(
            math.gcd(prefixGcd[i], prefixGcd[-(1 + i)])
            for i in range(len(prefixGcd) // 2)
        )