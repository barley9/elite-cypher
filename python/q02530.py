"""
2530. Maximal Score After Applying K Operations

You are given a 0-indexed integer array `nums` and an integer `k`. You have a
starting score of `0`.

In one operation:
    choose an index `i` such that `0 <= i < nums.length`,
    increase your score by `nums[i]`, and
    replace `nums[i]` with `ceil(nums[i] / 3)`.

Return the maximum possible score you can attain after applying exactly `k`
operations.

The ceiling function `ceil(val)` is the least integer greater than or equal to
`val`.
"""

import heapq


def divceil(a: int, b: int) -> int:
    """
    Returns `ceiling(a / b)` where `ceiling(n)` is the smallest integer
    greater than or equal to `n`. See this StackOverflow thread:
    https://stackoverflow.com/questions/14822184
    """
    return -(a // -b)

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """O(n + k*log n) time, O(1) space solution using heap"""
        nums = [-n for n in nums]  # `heapq` implements a min-heap, but we want a max-heap
        heapq.heapify(nums)  # O(n) time; see https://docs.python.org/3/library/heapq.html
        
        max_score = 0
        for _ in range(k):
            n = heapq.heappop(nums)  # O(log n) time
            max_score -= n  # deduct negative score = add to score
            n = n // 3  # use floor instead of ceiling because n < 0
            heapq.heappush(nums, n)  # O(log n) time

        return max_score

    def maxKelements(self, nums, k):
        nums,max_score=[-n for n in nums],0;heapq.heapify(nums)
        for _ in range(k):n=heapq.heappop(nums);max_score-=n;heapq.heappush(nums,n//3)
        return max_score

    def maxKelements(self, nums: List[int], k: int) -> int:
        """O(n + k*log n) time, O(1) space solution using heap"""
        nums = [-n for n in nums]  # `heapq` implements a min-heap, but we want a max-heap
        heapq.heapify(nums)
        
        max_score = 0
        for _ in range(k):
            # because nums[0] is always the smallest element, collapse into one line
            max_score -= heapq.heapreplace(nums, nums[0] // 3)

        return max_score

    def maxKelements(self, nums, k):
        nums,max_score=[-n for n in nums],0
        heapq.heapify(nums)
        for _ in range(k):max_score-=heapq.heapreplace(nums,nums[0]//3)
        return max_score