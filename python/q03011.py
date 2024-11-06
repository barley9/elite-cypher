"""
3011. Find if Array Can Be Sorted

You are given a 0-indexed array of positive integers `nums`.

In one operation, you can swap any two adjacent elements if they have the same
number of set bits. You are allowed to do this operation any number of times
(including zero).

Return `true` if you can sort the array, else return `false`.
"""

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        """
        O(2 * n) time, O(n) space solution. Partition `nums` into consecutive
        groups where all elements in a group have the same `bit_count()`. As we
        loop through `nums`, keep track of the minimum and maximum values in
        each partition. If the maximum value in a partition is greater than the
        minimum value in the subsequent partition, that means that there is at
        least one element in the first partition that would need to be sorted
        into a position within the second. However, because the two partitions
        have a different `bit_count()`, achieving such a configuration is
        impossible according to the swap rule.
        """
        partitions = []  # O(n) space
        current_bitcount = -1
        for n in nums:  # O(n) time
            bc = n.bit_count()
            # when bit_count changes, make new partition
            if current_bitcount != bc:
                partitions.append([bc, 2**9, -2**9])  # [bit_count, min, max]
                current_bitcount = bc
            # keep track of MAX value in partition
            if n < partitions[-1][1]:
                partitions[-1][1] = n
            # keep track of MIN value in partition
            if n > partitions[-1][2]:
                partitions[-1][2] = n
        
        # make sure all partitions can be sorted
        for i in range(len(partitions) - 1):  # O(n) time
            # if p[i + 1].min < p[i].max, array can't be sorted
            if partitions[i][2] > partitions[i + 1][1]:
                return False
        
        return True
