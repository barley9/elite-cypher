"""
20. Valid Parentheses

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """O(n) time, O(n) space solution"""
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif c == ')':
                if stack.pop() != '(':
                    return False
            elif c == ']':
                if stack.pop() != '[':
                    return False
            elif c == '}':
                if stack.pop() != '{':
                    return False
        return True