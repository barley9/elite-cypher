"""
3532. Path Existence Queries in a Graph I

You are given an integer `n` representing the number of nodes in a graph,
labeled from `0` to `n - 1`.

You are also given an integer array `nums` of length `n` sorted in non-
decreasing order, and an integer `maxDiff`.

An undirected edge exists between nodes `i` and `j` if the absolute difference
between `nums[i]` and `nums[j]` is at most `maxDiff` (i.e.,
`|nums[i] - nums[j]| <= maxDiff`).

You are also given a 2D integer array `queries`. For each
`queries[i] = [u_i, v_i]`, determine whether there exists a path between nodes
`u_i` and `v_i`.

Return a boolean array `answer`, where `answer[i]` is `true` if there exists a
path between `u_i` and `v_i` in the `i`th query and `false` otherwise.
"""

class Solution:
    def pathExistenceQueries(self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:
        diffs = [
            nums[i] - nums[i - 1]
            for i in range(1, len(nums))
        ]

        print(diffs)

        # Locate all "breaks"; i.e. consecutive elements that differ by more than `maxDiff`
        # If the interval `queries[k] = [a, b]` contains a "break", there is no path between `nums[a]` and `nums[b]`

        breaks = [0]
        bk = 0
        for d in diffs:
            if d > maxDiff:
                bk += 1
            breaks.append(bk)

        print(breaks)

        answers = [
            breaks[i] - breaks[j] == 0
            for i, j in queries
        ]

        return answers

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        """
        O(n + m) time, O(n + m) space solution where `n = len(nums)` and
        `m = len(queries)`
        """
        # Locate all "breaks"; i.e. consecutive elements that differ by more
        # than `maxDiff`
        breaks = [0]
        bk = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > maxDiff:
                bk += 1
            breaks.append(bk)
            
        # If the interval `queries[k] = [i, j]` contains a "break", there is no
        # path between `nums[i]` and `nums[j]`
        return [
            breaks[i] - breaks[j] == 0
            for i, j in queries
        ]