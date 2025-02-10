"""
3174. Clear Digits

You are given a string `s`.

Your task is to remove all digits by doing this operation repeatedly:
    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.
"""

class Solution:
    digits = set(chr(i) for i in range(ord('0'), ord('9') + 1))

    def clearDigits(self, s: str) -> str:
        """INCORRECT"""
        stripped = ''.join(c for c in s if c not in self.digits)
        # print(digits)
        # print(s, stripped)
        return stripped[:2*len(stripped) - len(s)]

    def clearDigits(self, s: str) -> str:
        """
        O(2 * n) time, O(n) space solution. This is just like checking for
        matching parentheses (use a stack!).
        """
        stack = []
        for c in s:
            if c in self.digits:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)