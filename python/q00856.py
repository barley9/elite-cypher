"""
856. Score of Parentheses

Given a balanced parentheses string `s`, return the score of the string.

The score of a balanced parentheses string is based on the following rule:
    "()" has score `1`.
    `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.
    `(A)` has score `2 * A`, where `A` is a balanced parentheses string.
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """O(3n) time, O(n) space solution"""
        s = s.replace(")(", ")+(")
        s = s.replace("()","1")
        s = s.replace("(", "2*(")
        # print(s)
        return eval(s)

    def scoreOfParentheses(self, s: str) -> int:
        """O(n) time, O(n) space solution"""
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                # Add up everything inside pair of parens
                total = 0
                while stack[-1] != "(":
                    total += stack.pop()
                stack.pop()
                # If nothing inside parens, push `1`; else, push double
                if total == 0:
                    stack.append(1)
                else:
                    stack.append(2 * total)
            # print(stack)
        
        return sum(stack)