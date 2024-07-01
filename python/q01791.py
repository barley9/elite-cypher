"""
1791. Find Center of Star Graph

There is an undirected star graph consisting of `n` nodes labeled from `1` to 
`n`. A star graph is a graph where there is one center node and exactly `n - 1`
edges that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [u_i, v_i]`
indicates that there is an edge between the nodes `u_i` and `v_i`. Return the
center of the given star graph.
"""


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """O(n) time, O(1) space solution"""
        for i in set.intersection(*(set(edge) for edge in edges)):
            return i

    def findCenter(self, edges: List[List[int]]) -> int:
        """O(1) time, O(1) space solution"""
        for i in set(edges[0]) & set(edges[1]):  # only need to check first two
            return i