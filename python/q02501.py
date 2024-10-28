"""
2501. Longest Square Streak in an Array

You are given an integer array `nums`. A subsequence of `nums` is called a
square streak if:
    The length of the subsequence is at least `2`, and
    after sorting the subsequence, each element (except the first element) is
        the square of the previous number.

Return the length of the longest square streak in `nums`, or return `-1` if
there is no square streak.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.
"""

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        max_streak = 0
        for n in nums:
            streak = 1
            while n * n in nums:
                streak += 1
                n = n * n
            if streak > max_streak:
                max_streak = streak
        return max_streak if max_streak > 1 else -1

# Direct output file writing is now slower?!?
def longestSquareStreak(nums):
    nums,max_streak=set(nums),0
    for n in nums:
        streak = 1
        while n*n in nums:streak+=1;n=n*n
        if streak>max_streak:max_streak=streak
    return max_streak if max_streak>1 else -1
results=[longestSquareStreak(loads(arr)) for arr in sys.stdin]
with open('user.out','w') as f:f.write(str(results)[1:-1].replace(', ','\n')+'\n')
sys.exit(0)