"""
396. Rotate Function

You are given an integer array `nums` of length `n`.

Assume `arr_k` to be an array obtained by rotating `nums` by `k` positions
clock-wise. We define the rotation function `F` on `nums` as follows:
    `F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]`.

Return the maximum value of `F(0), F(1), ..., F(n-1)`.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """TOO SLOW"""
        n = len(nums)
        return max(
            sum(
                i * nums[(i + k) % n]
                for i in range(n)
            )
            for k in range(n)
        )

    def maxRotateFunction(self, nums: List[int]) -> int:
        """INCORRECT"""
        # Locate maximum value in `nums`
        k = 0
        mx = 0
        for i in range(len(nums)):
            if nums[i] > mx:
                mx = nums[i]
                k = i
        
        # Rotate `nums` so that maximum value is at the end
        n = len(nums)
        f = sum(i * nums[(i + n - 1 - k) % n] for i in range(n))

        print([nums[(i + n - 1 - k) % n] for i in range(n)])

        return f