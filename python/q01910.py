"""
1910. Remove All Occurrences of a Substring

Given two strings `s` and `part`, perform the following operation on `s` until
        all occurrences of the substring `part` are removed:
    Find the leftmost occurrence of the substring `part` and remove it from `s`.

Return `s` after removing all occurrences of `part`.

A substring is a contiguous sequence of characters in a string.
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """Alternative solution (happens to be slower)"""
        stack = []
        part = list(reversed(part))
        for c in s:
            stack.append(c)
            if len(stack) >= len(part) and all(stack[len(stack) - i - 1] == part[i] for i in range(len(part))):
                stack = stack[:len(stack) - len(part)]
        return ''.join(stack)

    def removeOccurrences(self, s: str, part: str) -> str:
        """Another alternative slower solution"""
        stack = []
        part = list(part)  # convert to list so we can test equality simply
        for c in s:
            stack.append(c)
            # If trailing slice of `stack` is equal to `part`...
            if len(stack) >= len(part) and stack[len(stack) - len(part):] == part:
                for _ in range(len(part)): del stack[-1]
        return ''.join(stack)

    def removeOccurrences(self, s: str, part: str) -> str:
        """O(2 * n) time, O(n) space solution using a stack"""
        stack = []
        part = list(part)  # convert to list so we can test equality simply
        for c in s:
            stack.append(c)
            # If trailing slice of `stack` is equal to `part`...
            if len(stack) >= len(part) and stack[len(stack) - len(part):] == part:
                stack = stack[:len(stack) - len(part)]  # 'pop' slice from `stack`
        return ''.join(stack)

    def removeOccurrences(self, s: str, part: str) -> str:
        """I always forget how fast 'find in string' operation is in Python..."""
        while part in s: s=s.replace(part,'',1)
        return s