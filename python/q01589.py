"""
1598. Crawler Log Folder

The Leetcode file system keeps a log each time some user performs a change
folder operation.

The operations are described below:
    "../" : Move to the parent folder of the current folder. (If you are already
        in the main folder, remain in the same folder).
    "./" : Remain in the same folder.
    "x/" : Move to the child folder named `x` (This folder is guaranteed to
        always exist).

You are given a list of strings `logs` where `logs[i]` is the operation
performed by the user at the `i`th step.

The file system starts in the main folder, then the operations in `logs` are
performed.

Return the minimum number of operations needed to go back to the main folder
after the change folder operations.
"""

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """O(n) time, O(1) space naive solution"""
        depth = 0
        for d in logs:
            if d == "../":
                if depth > 0:
                    depth -= 1
            elif d == "./":
                pass
            else:
                depth += 1
        return depth

    def minOperations(self, logs: List[str]) -> int:
        """wrong"""
        return sum((1 - 2 * (d == "../")) * (d != "./") for d in logs)

    def minOperations(self, logs: List[str]) -> int:
        """O(n) time, O(1) space solution, optimized"""
        depth = 0
        for d in logs:
            if d[0] != '.': depth += 1
            elif d == '../' and depth > 0: depth -= 1
        return depth