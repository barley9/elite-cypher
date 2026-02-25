"""
1356. Sort Integers by The Number of 1 Bits

You are given an integer array `arr`. Sort the integers in the array in
ascending order by the number of `1`'s in their binary representation and in
case of two or more integers have the same number of `1`'s you have to sort
them in ascending order.

Return the array after sorting it.
"""

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        O(n log n) time, O(n) space solution

        Thanks to <https://stackoverflow.com/a/4233482> for multi-key sorting
        """
        return sorted(
            arr,
            key=lambda n: (n.bit_count(), n)
        )
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        """O(n log n) time, O(1) space solution"""
        arr.sort(key=lambda n: (n.bit_count(), n))
        return arr