"""
1726. Tuple with Same Product

Given an array `nums` of distinct positive integers, return the number of
tuples `(a, b, c, d)` such that `a * b = c * d` where `a`, `b`, `c`, and `d`
are elements of `nums`, and `a != b != c != d`.
"""

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        O(n**4) time, O(1) space solution; TOO SLOW. (I kinda hate combinatorics problems.)
        """
        result = 0
        for i in range(0, len(nums) - 3):
            a = nums[i]
            for j in range(i + 1, len(nums) - 2):
                b = nums[j]
                for k in range(j + 1, len(nums) - 1):
                    c = nums[k]
                    for m in range(k + 1, len(nums)):
                        d = nums[m]
                        # print(a, b, c, d)
                        result += 8 * (a * b == c * d) + \
                                  8 * (a * c == b * d) + \
                                  8 * (a * d == b * c)
        return result