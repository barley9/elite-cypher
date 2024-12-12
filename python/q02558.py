"""
2558. Take Gifts From the Richest Pile

You are given an integer array `gifts` denoting the number of gifts in various
piles. Every second, you do the following:
    Choose the pile with the maximum number of gifts.
    If there is more than one pile with the maximum number of gifts, choose any.
    Leave behind the floor of the square root of the number of gifts in the
        pile. Take the rest of the gifts.

Return the number of gifts remaining after `k` seconds.
"""

import math
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        O(n + k*log(n)) time, O(1) space solution using max-heap
        """
        
        # `heapq` implements a min-heap, but we want a max-heap
        gifts = [-n for n in gifts]  # O(n) time

        heapq.heapify(gifts)  # O(n) time
        
        for _ in range(k):
            heapq.heapreplace(
                gifts,
                -int(math.sqrt(-gifts[0]))
            )
        
        return -sum(gifts)  # O(n) time