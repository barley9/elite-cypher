"""
2161. Partition Array According to Given Pivot

You are given a 0-indexed integer array `nums` and an integer `pivot`.
Rearrange `nums` such that the following conditions are satisfied:
    Every element less than `pivot` appears before every element greater than
        `pivot`.
    Every element equal to `pivot` appears in between the elements less than
        and greater than `pivot`.
    The relative order of the elements less than `pivot` and the elements
        greater than `pivot` is maintained. More formally, consider every
        `p_i`, `p_j` where `p_i` is the new position of the `i`th element and
        `p_j` is the new position of the `j`th element. If `i < j` and both
        elements are smaller (or larger) than pivot, then `p_i < p_j`.
Return `nums` after the rearrangement.
"""

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """O(n) time, O(n) space solution"""
        left = []  # elements less than `pivot`
        right = []  # elements greater than `pivot`
        pcount = 0  # count the number of times `pivot` occurs in `nums`
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                pcount += 1
        return left + ([pivot] * pcount) + right