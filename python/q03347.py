"""
3347. Maximum Frequency of an Element After Performing Operations II

You are given an integer array `nums` and two integers `k` and `numOperations`.

You *must* perform an operation `numOperations` times on `nums`, where in each
operation you:
    Select an index `i` that was not selected in any previous operations.
    Add an integer in the range `[-k, k]` to `nums[i]`.

Return the maximum possible frequency of any element in `nums` after performing
the operations.
"""

import collections

class Solution:
    def maxFrequency(self,
            nums: List[int],
            k: int,
            numOperations: int) -> int:
        """INCORRECT; doesn't take into account `numOperations`"""
        freqs = collections.Counter()
        for n in nums:
            # print(list(range(n - k, n + k + 1)))
            freqs.update(range(n - k, n + k + 1))
        return freqs.most_common(1)[0][1]