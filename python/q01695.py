"""
1695. Maximum Erasure Value

You are given an array of positive integers `nums` and want to erase a
subarray containing unique elements. The score you get by erasing the subarray
is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array `b` is called to be a subarray of `a` if it forms a contiguous
subsequence of `a`, that is, if it is equal to `a[l], a[l+1], ..., a[r]` for
some `(l, r)`.
"""

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cur_sum = nums[0]  # sum of subarray so far
        max_sum = cur_sum
        unique = {nums[0] : 0}  # {val : index, ...} lookup table for values in subarray
        left = 0
        right = 1
        while right < len(nums):
            # print((left, right), nums[left:right + 1], unique)
            if nums[right] not in unique:
                cur_sum += nums[right]
                if cur_sum > max_sum:
                    max_sum = cur_sum
                unique[nums[right]] = right
            else:
                temp = unique[nums[right]] + 1
                for i in range(left, unique[nums[right]] + 1):
                    cur_sum -= nums[i]
                    del unique[nums[i]]
                left = temp
                cur_sum += nums[right]
                if cur_sum > max_sum:
                    max_sum = cur_sum
                unique[nums[right]] = right
            right += 1
        return max_sum

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """O(n) time, O(n) space solution using sliding window"""
        current_sum = max_sum = nums[0]  # keep track of subarray sum
        index_of = {nums[0] : 0}  # {val : index, ...} to keep track of elements we've encountered
        left = 0  # left index of sliding window
        for right in range(1, len(nums)):
            if nums[right] in index_of:
                # We HAVE seen nums[right] before
                # Move `left` just after index of last encountered instance of `nums[right]`
                new_left = index_of[nums[right]] + 1
                # Remove elements from running total and hash table
                for i in range(left, new_left - 1):
                    current_sum -= nums[i]
                    del index_of[nums[i]]
                left = new_left
                index_of[nums[right]] = right  # update index
            else:
                # We haven't seen `nums[right]` before
                # Add it to running total and to hash table
                current_sum += nums[right]
                if current_sum > max_sum:
                    max_sum = current_sum
                index_of[nums[right]] = right
        return max_sum