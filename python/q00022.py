"""
22. Generate Parentheses

Given `n` pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.
"""

import functools

class Solution:
    @functools.lru_cache(maxsize=None)
    def generateParenthesis(self, n: int) -> list[str]:
        """
        O(3^n) time, O(3^n) space solution
        
        INCORRECT: does not generate ALL answers
        """
        if n == 1:
            return ["()"]

        p1 = self.generateParenthesis(n - 1)
        result = list(set(
            s
            for i in range(len(p1))
            for s in [
                f"({p1[i]})",
                f"(){p1[i]}",
                f"{p1[i]}()"
            ]
        ))

    @functools.lru_cache(maxsize=None)
    def generateParenthesis(self, n: int) -> list[str]:
        # State machine?
        state = 0
        elem = ""
        if state == 0:
            elem += "("
            state += 1
        elif state < n:
            pass
        else:
            elem += ")"
            state -= 1