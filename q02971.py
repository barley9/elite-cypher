"""
2971. Find Polygon With the Largest Perimeter

You are given an array of positive integers `nums` of length `n`.

A polygon is a closed plane figure that has at least `3` sides. The longest side
of a polygon is smaller than the sum of its other sides.

Conversely, if you have `k` (`k >= 3`) positive real numbers `a1`, `a2`, `a3`,
..., `ak` where `a1 <= a2 <= a3 <= ... <= ak` and
`a1 + a2 + a3 + ... + ak-1 > ak`, then there always exists a polygon with `k`
sides whose lengths are `a1`, `a2`, `a3`, ..., `ak`.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed
from `nums`, or `-1` if it is not possible to create a polygon.
"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        nums.sort()

        max_perimeter = sum(nums)
        for i in range(len(nums) - 1, 1, -1):  # stop at 3rd element
            if nums[i] < max_perimeter - nums[i]:  # if we found a valid polygon...
                return max_perimeter  # ...return its perimeter
            else:
                max_perimeter -= nums[i]
        
        return -1
