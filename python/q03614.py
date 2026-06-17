"""
3614. Process String with Special Operations II

You are given a string `s` consisting of lowercase English letters and the
special characters: '*', '#', and '%'.

You are also given an integer `k`.

Build a new string result by processing `s` according to the following rules
from left to right:
    If the letter is a lowercase English letter append it to result.
    A '*' removes the last character from result, if it exists.
    A '#' duplicates the current result and appends it to itself.
    A '%' reverses the current result.

Return the `k`th character of the final string `result`. If `k` is out of the
bounds of `result`, return '.'.
"""

class Solution:
    def processStr(self, s: str, k: int) -> str:
        """MEMORY LIMIT EXCEEDED"""
        stack = []
        for c in s:
            if c == '*':
                if stack: stack.pop()
            elif c == '#':
                stack += stack  # append `stack` to itself recursively?
            elif c == '%':
                stack = stack[::-1]  # set flag to append to front instead?
            else:
                stack.append(c)
        return stack[k] if k < len(stack) else '.'