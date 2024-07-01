"""
1550. Three Consecutive Odds

Given an integer array `arr`, return `true` if there are three consecutive odd
numbers in the array. Otherwise, return `false`.
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """O(n) time, O(1) space solution"""
        count = 0  # number of consecutive odds in current run
        for n in arr:
            if n & 1:  # if `n` is odd...
                count += 1
                if count > 2: return True
            else: count = 0
        return False