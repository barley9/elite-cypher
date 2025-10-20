"""
2011. Final Value of Variable After Performing Operations

There is a programming language with only four operations and one variable `X`:
    `++X` and `X++` increments the value of the variable `X` by `1`.
    `--X` and `X--` decrements the value of the variable `X` by `1`.

Initially, the value of `X` is `0`.

Given an array of strings `operations` containing a list of operations, return
the final value of `X` after performing all the operations.
"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """O(n) time, O(1) space solution"""
        X = 0
        for operation in operations:
            if '+' in operation:
                X += 1
            else:
                X -= 1
        return X