"""
3558. Number of Ways to Assign Edge Weights I

There is an undirected tree with `n` nodes labeled from 1 to `n`, rooted at
node 1. The tree is represented by a 2D integer array `edges` of length
`n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between
nodes `u_i` and `v_i`.

Initially, all edges have a weight of 0. You must assign each edge a weight of
either 1 or 2.

The cost of a path between any two nodes `u` and `v` is the total weight of all
edges in the path connecting them.

Select any one node `x` at the maximum depth. Return the number of ways to
assign edge weights in the path from node 1 to `x` such that its total cost is
odd.

Since the answer may be large, return it modulo `10^9 + 7`.

Note: Ignore all edges not in the path from node 1 to `x`.
"""


import dataclasses


@dataclasses.dataclass(slots=True)
class Node():
    index: int
    children: list = dataclasses.field(default_factory=list)


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        """TOO SLOW"""
        # Compute distance of each node from node 1
        # (this is the slow part)
        dists = {
            1 : 0,  # node 1 is a distance of 0 from node 1
        }
        while edges:  # `edges` could be in any order
            for i in range(len(edges) - 1, -1, -1):
                u, v = edges[i]
                if (u in dists) and (v not in dists):
                    dists[v] = dists[u] + 1
                    del edges[i]
                elif (v in dists) and (u not in dists):
                    dists[u] = dists[v] + 1
                    del edges[i]
        
        # Locate a node at maximum depth
        node = -1
        depth = -1
        for k, v in dists.items():
            if v > depth:
                node = k
                depth = v
        
        # Compute number of ways to make total weight odd
        return (2 ** (depth - 1)) % (10 ** 9 + 7)
        
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Compute distance of each node from node 1 (see <https://stackoverflow.com/questions/71478182>)
        node_keys = set(
            node
            for edge in edges
            for node in edge
        )
        nodes = {
            key : Node(key)
            for key in node_keys
        }
        for u, v in edges:
            nodes[u].children.append(nodes[v])
            node_keys.remove(v)
        root = nodes[list(node_keys)[0]]
        print(root)

        return -1
        
        
        # Locate a node at maximum depth
        node = -1
        depth = -1
        for k, v in dists.items():
            if v > depth:
                node = k
                depth = v
        
        # Compute number of ways to make total weight odd
        return (2 ** (depth - 1)) % (10 ** 9 + 7)
        