"""
1437. Check If All 1's Are at Least Length K Places Away

Given an binary array `nums` and an integer `k`, return `true` if all `1`'s are
at least `k` places away from each other, otherwise return `false`.
"""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """O(n) time, O(1) space solution"""
        index_last_one = -(10**5 + 1)  # negative infinity
        for i in range(len(nums)):
            if nums[i] == 1:
                # print(index_last_one, i)
                if (i - index_last_one) <= k:
                    return False
                index_last_one = i
        return True