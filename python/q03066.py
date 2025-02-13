"""
3066. Minimum Operations to Exceed Threshold Value II

You are given a 0-indexed integer array `nums`, and an integer `k`.

In one operation, you will:
    Take the two smallest integers `x` and `y` in `nums`.
    Remove `x` and `y` from `nums`.
    Add `2 * min(x, y) + max(x, y)` anywhere in the array.

Note that you can only apply the described operation if `nums` contains at least
two elements.

Return the minimum number of operations needed so that all elements of the array
are greater than or equal to `k`.
"""

import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """O(n * log(n)) time, O(1) space solution using min-heap"""
        heapq.heapify(nums)
        count = 0
        while (len(nums) > 1) and (nums[0] < k or nums[1] < k):
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, (x << 1) + y)
            count += 1
        return count

    def minOperations(self, nums: List[int], k: int) -> int:
        """O(n * log(n)) time, O(1) space solution using min-heap"""
        heapq.heapify(nums)
        count = 0
        while nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, (x << 1) + y)
            count += 1
        return count

    # These last two are of comparable performance
    def minOperations(self, nums: List[int], k: int) -> int:
        """O(n * log(n)) time, O(1) space solution using min-heap"""
        heapq.heapify(nums)
        count = 0
        while nums[0] < k:
            m = heapq.heappop(nums)
            heapq.heapreplace(nums, (m << 1) + nums[0])
            count += 1
        return count

    def minOperations(self, nums: List[int], k: int) -> int:
        """O(n * log(n)) time, O(1) space solution using min-heap"""
        heapq.heapify(nums)  # O(n)
        for count in range(len(nums) - 1):
            if (nums[0] >= k and nums[1] >= k): break
            m = heapq.heappop(nums)  # O(log n)
            heapq.heapreplace(nums, (m << 1) + nums[0])  # O(log n)
        else:
            count += 1
        return count