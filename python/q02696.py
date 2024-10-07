"""
2696. Minimum String Length After Removing Substrings

You are given a string `s` consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can
remove any occurrence of one of the substrings "AB" or "CD" from `s`.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could
produce new "AB" or "CD" substrings.
"""

class Solution:
    def minLength(self, s: str) -> int:
        """O(n^2) time, O(n) space solution using string replacement"""
        prev = ''
        while s != prev:  # if no replacements found, exit loop
            prev = s
            s = s.replace('AB', '').replace('CD', '')
        return len(s)

    def minLength(self, s: str) -> int:
        """
        O(n) time, O(n) space solution using a stack. We can think of 'AB' and
        'CD' as if they were matching pairs of brackets. I.e. A->(, B->), C->[,
        D->]. Then, the problem is reduced to the familiar finding matching
        parentheses.
        """
        min_len = len(s)
        stack = []
        for c in s:
            if c == 'A':
                stack.append(c)
            elif c == 'B':
                if stack and stack[-1] == 'A':
                    stack.pop()
                    min_len -= 2
                else:
                    stack.append(c)
            elif c == 'C':
                stack.append(c)
            elif c == 'D':
                if stack and stack[-1] == 'C':
                    stack.pop()
                    min_len -= 2
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return min_len

    # Increasingly golfed (and slower?!?) versions of above
    def minLength(self, s: str) -> int:
        min_len = len(s)
        stack = []
        for c in s:
            if c == 'B':
                if stack and stack[-1] == 'A':
                    stack.pop()
                    min_len -= 2
                else:
                    stack.append(c)
            elif c == 'D':
                if stack and stack[-1] == 'C':
                    stack.pop()
                    min_len -= 2
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return min_len

    def minLength(self, s: str) -> int:
        min_len = len(s)
        stack = []
        for c in s:
            if c == 'B' and stack and stack[-1] == 'A':
                stack.pop()
                min_len -= 2
            elif c == 'D' and stack and stack[-1] == 'C':
                stack.pop()
                min_len -= 2
            else:
                stack.append(c)
        return min_len

    def minLength(self, s: str) -> int:
        min_len = len(s)
        stack = []
        for c in s:
            if c == 'B' and stack and stack[-1] == 'A':del stack[-1];min_len -= 2
            elif c == 'D' and stack and stack[-1] == 'C':del stack[-1];min_len -= 2
            else:stack.append(c)
        return min_len