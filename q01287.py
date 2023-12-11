"""
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
"""


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        threshold = len(arr) // 4
        count = 0
        cur = None
        for i in range(len(arr)):
            if arr[i] == cur:
                count += 1
                if count > threshold:
                    return arr[i]
            else:
                cur = arr[i]
                count = 1