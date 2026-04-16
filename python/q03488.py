"""
3488. Closest Equal Element Queries

You are given a circular array `nums` and an array `queries`.

For each query `i`, you have to find the following:

The minimum distance between the element at index `queries[i]` and any other
index `j` in the circular array, where `nums[j] == nums[queries[i]]`. If no
such index exists, the answer for that query should be `-1`.

Return an array `answer` of the same size as `queries`, where `answer[i]`
represents the result for query `i`.
"""

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """INCORRECT"""
        indices = {}
        for i in range(len(nums)):
            if nums[i] in indices:
                indices[nums[i]].add(i)
            else:
                indices[nums[i]] = {i}
        
        # print(indices)

        result = [-1] * len(queries)
        for i in range(len(queries)):
            n = nums[queries[i]]
            if len(indices[n]) <= 1:
                continue
            
            result[i] = min(
                min(
                    abs(queries[i] - j),
                    abs(queries[i] - (j + len(nums)))
                )
                for j in (indices[n] - {queries[i]})
            )

        return result