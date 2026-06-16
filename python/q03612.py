"""
3612. Process String with Special Operations I

You are given a string `s` consisting of lowercase English letters and the
special characters: `*`, `#`, and `%`.

Build a new string `result` by processing `s` according to the following rules
from left to right:
    If the letter is a lowercase English letter append it to `result`.
    A '*' removes the last character from `result`, if it exists.
    A '#' duplicates the current `result` and appends it to itself.
    A '%' reverses the current `result`.

Return the final string `result` after processing all characters in `s`.
"""

class Solution:
    alpha = set(
        chr(i)
        for i in range(ord('a'), ord('z') + 1)
    )
    
    def processStr(self, s: str) -> str:
        """O(n) time, O(2^n) space solution"""
        result = []  # stack
        for c in s:
            if c in self.alpha:
                result.append(c)
            elif c == '*' and result:
                result.pop()
            elif c == '#':
                result += result
            elif c == '%':
                result = result[::-1]
        
        return ''.join(result)

    def processStr(self, s: str) -> str:
        """O(n) time, O(2^n) space solution"""
        result = []  # stack
        for c in s:
            if c == '*':
                if result: result.pop()
            elif c == '#':
                result += result
            elif c == '%':
                result = result[::-1]
            else:
                result.append(c)
        return ''.join(result)