"""
3310. Remove Methods From Project

You are maintaining a project that has `n` methods numbered from `0` to
`n - 1`.

You are given two integers `n` and `k`, and a 2D integer array invocations,
where `invocations[i] = [a_i, b_i]` indicates that method `a_i` invokes method
`b_i`.

There is a known bug in method `k`. Method `k`, along with any method invoked
by it, either directly or indirectly, are considered suspicious and we aim to
remove them.

A group of methods can only be removed if no method outside the group invokes
any methods within it.

Return an array containing all the remaining methods after removing all the
suspicious methods. You may return the answer in any order. If it is not
possible to remove all the suspicious methods, none should be removed.
"""

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        """O(n + m) time, O(n + m) space solution"""
        edges = {i : [] for i in range(n)}
        for a, b in invocations:
            edges[a].append(b)
        
        sus = [False] * n
        sus[k] = True

        stack = [child for child in edges[k]]
        while stack:
            if sus[stack[-1]]:
                stack.pop()
            else:
                q = stack.pop()
                sus[q] = True
                stack.extend(edges[q])

        # If any sus' methods are called by a non-sus' method, don't remove anything
        for i in range(n):
            if not sus[i]:
                for j in edges[i]:
                    if sus[j]:
                        return list(range(n))

        return [i for i,s in enumerate(sus) if not s]