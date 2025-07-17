"""
3202. Find the Maximum Length of Valid Subsequence II

You are given an integer array `nums` and a positive integer `k`.

A subsequence `sub` of `nums` with length `x` is called valid if it satisfies:
    `(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k`.

Return the length of the longest valid subsequence of `nums`.
"""

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        INCORRECT; this feels like it should work, but it doesn't. (I'm just
        trying to generalize the solution from 3201.)
        """
        print('nums:', nums)
        count_r = [1] * k  # length of longest subsequence with remainder `r`
        idx_r   = [0] * k  # index of last valid index in subsequence with remainder `r`
        for i in range(1, len(nums)):
            print('count:', count_r, '| idx:', idx_r)
            for r in range(k):
                if (nums[idx_r[r]] + nums[i]) % k == r:
                    print(f'\t(nums[{idx_r[r]}] + nums[{i}]) % {k} = {(nums[idx_r[r]] + nums[i]) % k}')
                    count_r[r] += 1
                    idx_r[r] = i
        print('count:', count_r, '| idx:', idx_r)
        return max(count_r)