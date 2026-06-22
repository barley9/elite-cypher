"""
1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string `s` that consists of lower case English letters and
brackets.

Reverse the strings in each pair of matching parentheses, starting from the
innermost one.

Your result should not contain any brackets.
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        """O(n) time, O(n) space solution"""
        stack = []
        for c in s:
            if c == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # pop open paren
                stack.extend(temp)
            else:
                stack.append(c)
            # print(c, stack, '', sep='\n')
        return ''.join(stack)