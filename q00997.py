"""
997. Find the Town Judge

In a town, there are `n` people labeled from `1` to `n`. There is a rumor that
one of these people is secretly the town judge.

If the town judge exists, then:

    1. The town judge trusts nobody.
    2. Everybody (except for the town judge) trusts the town judge.
    3. There is exactly one person that satisfies properties 1 and 2.

You are given an array `trust` where `trust[i] = [a_i, b_i]` representing that
the person labeled `a_i` trusts the person labeled `b_i`. If a trust
relationship does not exist in `trust` array, then such a trust relationship
does not exist.

Return the label of the town judge if the town judge exists and can be
identified, or return `-1` otherwise.
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # set of possible judges
        judges = set(i for i in range(1, n + 1))
        # list of sets of people who trust person `i`
        trusted = [set() for _ in range(n)]
        for a, b in trust:
            judges -= {a}  # if `a` trusts `b`, `a` cannot be judge
            trusted[b - 1].add(a)  # `b` is trusted by `a`

        allset = set(i for i in range(1, n + 1))
        for j in judges:
            # if `j` is trusted by everyone (except `j`), they must be judge
            if trusted[j - 1] == allset - {j}:
                return j
        
        return -1

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        O(n) time, O(n) space solution using graph theory. Treat each person as
        node in graph, with directed connections representing trust
        relationships. The judge's node has indegree == n - 1 (everybody else
        trusts them) and outdegree == 0 (they trust nobody).
        """
        indegree = [0] * n
        for a, b in trust:
            indegree[a - 1] -= 1
            indegree[b - 1] += 1

        for i in range(1, len(indegree)):
            if indegree[i] == n - 1:
                return i + 1
        
        return -1

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)  # small optimization to simplify index lookup
        for a, b in trust:
            indegree[a] -= 1
            indegree[b] += 1
        for i in range(1, len(indegree)):
            if indegree[i] == n - 1:
                return i
        return -1