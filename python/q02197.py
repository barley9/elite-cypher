"""
2197. Replace Non-Coprime Numbers in Array

You are given an array of integers `nums`. Perform the following steps:
    Find any two adjacent numbers in `nums` that are non-coprime.
    If no such numbers are found, stop the process.
    Otherwise, delete the two numbers and replace them with their LCM (Least
        Common Multiple).
    Repeat this process as long as you keep finding two adjacent non-coprime
        numbers.

Return the final modified array. It can be shown that replacing adjacent non-
coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less
than or equal to `10^8`.

Two values `x` and `y` are non-coprime if `GCD(x, y) > 1` where `GCD(x, y)` is
the Greatest Common Divisor of `x` and `y`.
"""

import math

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        result = []
        left = 0
        right = 1
        
        while right < len(nums):
            print(nums, (nums[left], nums[right]), math.gcd(nums[left], nums[right]))
            if math.gcd(nums[left], nums[right]) > 1:
                g = math.gcd(nums[left], nums[right])
                nums[right] = nums[left] * nums[right] // g
                left = right
                right += 1
            else:
                result.append(nums[left])
                left += 1
                right = left + 1
        result.append(nums[left])
        
        return result