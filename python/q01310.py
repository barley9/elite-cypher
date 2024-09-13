"""
1310. XOR Queries of a Subarray

You are given an array `arr` of positive integers. You are also given the array
`queries` where `queries[i] = [lefti, righti]`.

For each query `i` compute the XOR of elements from `lefti` to `righti` (that
is, `arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti]`).

Return an array `answer` where `answer[i]` is the answer to the `i`th query.
"""

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """O(m * n) time, O(n) space solution; TOO SLOW"""
        answers = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            for j in range(left, right + 1):
                answers[i] ^= arr[j]
        return answers