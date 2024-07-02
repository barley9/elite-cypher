"""
350. Intersection of Two Arrays II

Given two integer arrays `nums1` and `nums2`, return an array of their
intersection. Each element in the result must appear as many times as it shows
in both arrays and you may return the result in any order.
"""


import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(m + n) time, O(m + n) space solution"""
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        return list((nums1 & nums2).elements())

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(m + n) time, O(1) space solution"""
        counts1 = [0] * 1001  # 0 <= n <= 1000
        for n in nums1:
            counts1[n] += 1

        counts2 = [0] * 1001
        for n in nums2:
            counts2[n] += 1

        return [j for i in range(len(counts1)) for j in [i] * (counts1[i] if counts1[i] < counts2[i] else counts2[i])]

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(m + n) time, O(m) space solution"""
        counts1 = collections.Counter(nums1)

        result = []
        for n in nums2:
            if counts1[n] > 0:
                result.append(n)
                counts1[n] -= 1
        
        return result
        
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(m + n) time, O(min(m, n)) space solution"""
        counts = collections.Counter(nums1) if len(nums1) < len(nums2) else collections.Counter(nums2)

        result = []
        for n in (nums2 if len(nums1) < len(nums2) else nums1):
            if counts[n] > 0:
                result.append(n)
                counts[n] -= 1
        
        return result