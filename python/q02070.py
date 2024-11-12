"""
2070. Most Beautiful Item for Each Query

You are given a 2D integer array `items` where `items[i] = [price_i, beauty_i]`
denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array `queries`. For each `queries[j]`,
you want to determine the maximum beauty of an item whose price is less than or
equal to `queries[j]`. If no such item exists, then the answer to this query is
`0`.

Return an array `answer` of the same length as `queries` where `answer[j]` is
the answer to the `j`th query.
"""

class Solution:
    def maximumBeauty(self,
            items: List[List[int]],
            queries: List[int],
    ) -> List[int]:
        """
        O(2*n + m*log n) time, O(n + m) space solution, where n = len(items)
        and m = len(queries).
        """
        items.sort()

        # Pre-process to remove expensive items with low beauty
        to_remove = [False] * len(items)
        max_beauty = 0
        for i in range(len(items)):
            if items[i][1] > max_beauty:
                max_beauty = items[i][1]  # keep item and update max_beauty
            else:
                to_remove[i] = True  # if a cheaper, more beautiful item exists, discard
        for i in range(len(items) - 1, -1, -1):
            if to_remove[i]:
                del items[i]

        results = []
        for q in queries:
            # Perform binary search on sorted `items`
            low, high = -1, len(items)
            while high - low > 1:
                mid = (high + low) >> 1  # divide by 2 by bit-shifting
                if items[mid][0] > q:
                    high = mid
                else:
                    low = mid
            # If we can't buy anything, return 0 beauty
            results.append(items[low][1] if low > -1 else 0)
        return results