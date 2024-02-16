"""
1481. Least Number of Unique Integers after K Removals

Given an array of integers `arr` and an integer `k`. Find the least number of
unique integers after removing exactly `k` elements.
"""

import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        Because of sort by frequency, this solution is O(n log n) in time.
        Creating the `Counter()` object and iterating over it are both O(n)
        operations. The creation of a `Counter()` object makes this O(n) in
        space.
        """
        # Create a dict of element frequencies, convert to list of tuples
        # (elem, freq), and sort descending by frequency
        counts = collections.Counter(arr).most_common()
        
        # Look at least-common elements first
        for i in range(len(counts) - 1, -1, -1):
            # If we can remove all copies of an element from `arr` using our
            # remaining allowed removals `k`, do so and continue. If we've run
            # out of `k`, return the remaining number of unique elements.
            if counts[i][1] <= k:
                k -= counts[i][1]
            else:
                return i + 1

        return 0