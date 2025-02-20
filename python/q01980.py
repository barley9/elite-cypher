"""
1980. Find Unique Binary String

Given an array of strings `nums` containing n unique binary strings each of
length `n`, return a binary string of length `n` that does not appear in
`nums`. If there are multiple answers, you may return any of them.
"""

import numpy as np
import ctypes

class Solution:
    """
    All solutions use a diagonalization approach:
        choose 0th bit of `result` to be different from 0th bit of `nums[0]`,
        1st bit of `result` different from 1st bit of `nums[1]`,
        etc.
    Inspired by: <en.wikipedia.org/wiki/Cantor's_diagonal_argument>
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for i in range(len(nums)):
            result.append('0' if nums[i][i] == '1' else '1')
        return ''.join(result)

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """O(n) time, O(n) space solution"""

        # convert python `int`s to numpy ints for easier bitwise manipulation
        arr = np.array(
            [int(n, base = 2) for n in nums],
            dtype=np.uint16
        )

        result = ~np.uint16(0)  # start with all `1`s
        mask = np.uint16(1)
        for n in arr:
            result ^= (n & mask)  # pick opposite bit: 1 ^ 0 = 1, 1 ^ 1 = 0
            mask = mask << 1

        # `result` will be `11...11{answer}`, so slice off leading `1`s and return
        #  fill----------v v----width = 16 = max int size
        return f"{result:016b}"[16 - len(nums):]

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        O(n) time, O(1) space solution; seems like more trouble than it's worth
        """
        nums = [ctypes.c_uint16(int(n, base=2)) for n in nums]
        result = ctypes.c_uint16(0xFFFF)
        mask = ctypes.c_uint16(1)
        # I think any performance benefits are lost from the constant
        # conversion back and forth from C <--> Python integers. I wish there
        # were a way to perform bitwise operations directly on `ctypes` objects
        # but I can't find any on Google. Looks like `numpy` wins this one.
        for n in nums:
            result.value ^= (n.value & mask.value)
            mask.value <<= 1
        return f"{result.value:016b}"[16 - len(nums):]