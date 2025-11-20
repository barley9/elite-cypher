"""
757. Set Intersection Size At Least Two

You are given a 2D integer array `intervals` where
`intervals[i] = [start_i, end_i]` represents all the integers from `start_i` to
`end_i` inclusively.

A containing set is an array `nums` where each interval from `intervals` has at
least two integers in `nums`.

For example, if `intervals = [[1,3], [3,7], [8,9]]`, then `[1,2,4,7,8,9]` and
`[2,3,4,8,9]` are containing sets.

Return the minimum possible size of a containing set.
"""

import collections

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        """
        O(n * ???) time, O(???) space solution
        
        INCORRECT
        """
        # Count how many times each integer is covered by an interval
        counts = collections.Counter()
        for lower, upper in intervals:
            counts.update(range(lower, upper + 1))
        
        print(counts)

        # Construct a containing set
        containing = set()
        hits = [0] * len(intervals)  # number of times each interval has been "hit" by element
        for elem, _ in counts.most_common():  # start with elements with highest counts
            for i in range(len(intervals)):  # update `hits`
                if intervals[i][0] <= elem <= intervals[i][1]:
                    hits[i] += 1
                    if hits[i] <= 2:
                        containing.add(elem)
            print(elem, hits, containing)

        return len(containing)
