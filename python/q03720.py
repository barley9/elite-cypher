"""
3720. Lexicographically Smallest Permutation Greater Than Target

You are given two strings `s` and `target`, both having length `n`, consisting
of lowercase English letters.

Return the lexicographically smallest permutation of `s` that is strictly
greater than `target`. If no permutation of `s` is lexicographically strictly
greater than `target`, return an empty string.
"""

import itertools

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        """
        O(n!) time, O(1) space solution
        TOO SLOW
        """
        target = tuple(target)
        for perm in itertools.permutations(sorted(s)):
            if perm > target:
                return ''.join(perm)
        
        return ''

    # def lexGreaterPermutation(self, s: str, target: str) -> str:
    #     orda = ord('a')
        
    #     # Count frequency of all chars in `s`
    #     counts = [0] * 26
    #     for c in s:
    #         counts[ord(c) - orda] += 1
    #     # print(counts)

    #     # While possible, take chars from `s` that are equal to `target[i]`.
    #     # If not possible, take smallest char from `s` that is greater than `target[i]`
    #     # If out of chars from `s`, ???
    #     result = []
    #     for j, c in enumerate(target):
    #         # Find smallest char gr. than or equal to `c`
    #         i = ord(c) - orda
    #         for i in range(ord(c) - orda, len(counts)):
    #             if counts[i] >= 0:
    #                 result.append(c)
    #                 counts[i] -= 1
    #                 break
    #         else:
    #             return ''
                    
    #         if i == ord(c) - orda:
    #             continue  # `result` and `target` match here
    #         elif i > ord(c) - orda:
    #             break