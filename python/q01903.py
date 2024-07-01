"""
1903. Largest Odd Number in String

You are given a string `num`, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of `num`, or an empty string `""` if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    odds = set(chr(i) for i in range(ord('1'), ord('9') + 1, 2))

    def largestOddNumber(self, num: str) -> str:
        """
        O(n) solution making use of observation that a number is odd if its final digit is odd.
        """
        # seek backwards to the last odd number in `num`
        for i in range(len(num) - 1, -1, -1):
            if num[i] in self.odds:
                break
        else:
            return ""
        
        return num[:i + 1]