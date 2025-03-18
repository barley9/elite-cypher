"""
2401. Longest Nice Subarray

You are given an array `nums` consisting of positive integers.

We call a subarray of `nums` nice if the bitwise AND of every pair of elements
that are in different positions in the subarray is equal to `0`.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length `1` are always considered nice.
"""

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        O(n ** 2) time, O(1) space solution
        
        Strategy:
        For each new candidate, check its bitwise AND against every element
        already in window. If any are nonzero, slide window over.
        """
        left = 0
        right = 1
        max_len = 0
        while right < len(nums):
            # Check new candidate `nums[right]` against all elements in current window
            for i in range(left, right):
                if nums[i] & nums[right]:
                    left += 1
                    break
            else:
                # We made it all the way through the window
                if right - left > max_len:
                    max_len = right - left
                right += 1
        
        return max_len + 1

    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        O(n ** 2) time, O(1) space alternative solution.

        Strategy:
        If any of the set bits in next candidate share a position with any of
        the set bits in any of the elements already in window, at least one of
        the bitwise AND's between the candidate and the elements in the window
        will be nonzero. So, keep track of all the occupied positions in a
        variable called `window_mask`.
        """
        left, right = 0, 1
        window_mask = nums[left]
        max_len = 0
        while right < len(nums):
            if (left < right) and (nums[right] & window_mask):
                left += 1
                # Re-generate window_mask
                window_mask = nums[left]
                for i in range(left, right):
                    window_mask |= nums[i]
            else:
                if right - left > max_len:
                    max_len = right - left
                window_mask |= nums[right]  # add `nums[right]` to window
                right += 1
        return max_len + 1

    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        O(n ** 2) time, O(1) space solution
        
        Strategy:
        Since we increment `left` each time a candidate fails to be "nice",
        just check against `nums[left]` instead of the whole window. Though,
        if this passes, we still have to check the rest of the elements.

        How is this faster than solution #1?
        """
        left, right = 0, 1
        max_len = 0
        while right < len(nums):
            if (left < right) and (nums[left] & nums[right]):
                left += 1  # remove `nums[left]` from window
            else:
                for i in range(left, right):
                    if nums[i] & nums[right]:  # check the rest of the elements in window
                        break
                else:
                    # We made it all the way through
                    if right - left > max_len:
                        max_len = right - left
                    right += 1  # add `nums[right]` to window
                    continue
                # We found a nonzero AND somewhere inside window; remove `nums[left]`
                left += 1
        return max_len + 1
        
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        O(n ** 2) time, O(1) space solution
        
        NOTE:
        Stolen from LeetCode code examples
        https://leetcode.cn/problems/longest-nice-subarray/solutions/1799426/bao-li-mei-ju-pythonjavacgo-by-endlessch-z6t6/
        """
        max_len = 1
        for i, window_mask in enumerate(nums):
            j = i - 1
            while (j >= 0) and (window_mask & nums[j] == 0):
                window_mask |= nums[j]
                j -= 1
            if i - j > max_len:
                max_len = i - j
        return max_len