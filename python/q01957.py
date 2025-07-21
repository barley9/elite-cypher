"""
1957. Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.

Given a string `s`, delete the minimum possible number of characters from `s`
to make it fancy.

Return the final string after the deletion. It can be shown that the answer
will always be unique.
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        s = list(s)
        count = 0
        char = ''
        for i in range(len(s) - 1, -1, -1):
            if s[i] == char:
                count += 1
                if count > 2:
                    del s[i]
            else:
                char = s[i]
                count = 1
        return ''.join(s)

    def makeFancyString(self, s: str) -> str:
        rle = []  # run-length encoding [['c', count], ...]
        for c in s:
            if rle and (rle[-1][0] == c):
                rle[-1][1] += 1
            else:
                rle.append([c, 1])
        return ''.join(char * min(count, 2) for char, count in rle)

    def makeFancyString(self, s: str) -> str:
        stack = []
        count = 0
        for c in s:
            if stack and (stack[-1] == c):
                count += 1
                if count < 3:
                    stack.append(c)
            else:
                count = 1
                stack.append(c)
        return ''.join(stack)

    def makeFancyString(self, s: str) -> str:
        """O(2*n) time, O(n) space solution"""
        stack = [s[0]]
        count = 1
        for c in s[1:]:
            if stack[-1] == c:
                count += 1
                if count < 3:
                    stack.append(c)
            else:
                count = 1
                stack.append(c)
        return ''.join(stack)