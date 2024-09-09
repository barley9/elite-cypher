"""
2191. Sort the Jumbled Numbers

You are given a 0-indexed integer array `mapping` which represents the mapping
rule of a shuffled decimal system. `mapping[i] = j` means digit `i` should be
mapped to digit `j` in this system.

The mapped value of an integer is the new integer obtained by replacing each
occurrence of digit `i` in the integer with `mapping[i]` for all `0 <= i <= 9`.

You are also given another integer array `nums`. Return the array `nums` sorted
in non-decreasing order based on the mapped values of its elements.

Notes:
    Elements with the same mapped values should appear in the same relative
        order as in the input.
    The elements of nums should only be sorted based on their mapped values and
        not be replaced by them.
"""

from functools import partial

class Solution:
    @staticmethod
    def map_num(n: int, mapping: dict) -> int:
        if n == 0:
            return mapping[n]
        digits = []
        while n:
            n, d = divmod(n, 10)
            digits.append(mapping[d])
        return sum(digits[k] * (10 ** k) for k in range(len(digits)))

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = {i : mapping[i] for i in range(len(mapping))}
        return sorted(nums, key=functools.partial(self.map_num, mapping=mapping))

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """O(m * n) time, O(1) space, unholy one-liner solution"""
        return sorted(nums, key=lambda n: sum(mapping[ord(d) - 48] * 10 ** k for k, d in enumerate(reversed(str(n)))))

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        O(m * n) time, O(1) space solution using Python string translation
        methods. Further optimized by using chr() instead of str().
        """
        tr = str.maketrans({chr(i + 48) : chr(mapping[i] + 48) for i in range(len(mapping))})  # 48 == ord('0')
        return sorted(nums, key=lambda n: int(str(n).translate(tr)))