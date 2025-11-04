"""
3318. Find X-Sum of All K-Long Subarrays I

You are given an array `nums` of `n` integers and two integers `k` and `x`.

The x-sum of an array is calculated by the following procedure:
    Count the occurrences of all elements in the array.
    Keep only the occurrences of the top `x` most frequent elements. If two
        elements have the same number of occurrences, the element with the
        bigger value is considered more frequent.
    Calculate the sum of the resulting array.

Note that if an array has less than `x` distinct elements, its x-sum is the
sum of the array.

Return an integer array `answer` of length `n - k + 1` where `answer[i]` is
the x-sum of the subarray `nums[i..i + k - 1]`.
"""

import collections

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """O(n k log k) time, O(n) space solution"""
        result = []
        for i in range(len(nums) - k + 1):
            counts = collections.Counter(sorted(nums[i:i + k], reverse=True))
            # print(nums[i:i + k], counts, counts.most_common(x))
            result.append(sum(
                count * n
                for n, count in counts.most_common(x)
            ))
        return result