"""
2375. Construct Smallest Number From DI String

You are given a 0-indexed string `pattern` of length `n` consisting of the
characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string `num` of length `n + 1` is created using the following
        conditions:
    `num` consists of the digits '1' to '9', where each digit is used at most
        once.
    If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.
    If `pattern[i] == 'D'`, then `num[i] > num[i + 1]`.

Return the lexicographically smallest possible string `num` that meets the
conditions.
"""

import itertools

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """First stab at a stack-based solution"""
        n = 1
        stack = []
        for c in pattern:
            if c == 'I':
                stack.append(n)
                n += 1
            else:
                stack.append(n)
                n -= 1
                if n < 1:
                    stack[-1] += 1
                    n += 1
        stack.append(n)

        # for i in range(len(stack) - 1):
        #     stack[i + 1] - stack[i]

        return ''.join(str(i) for i in stack)

    # Pre-generate all possible solutions (technically still O(1) space!)
    perms = list(itertools.permutations("123456789"))
    ord0 = ord('0')

    def smallestNumber(self, pattern: str) -> str:
        """O(9! * 9 * len(pattern)) time, O(9!) space brute force solution."""
        for i in range(len(self.perms)):
            n = [ord(d) - self.ord0 for d in self.perms[i]]
            if all(
                    (pattern[j] == 'I' and n[j] < n[j + 1]) or (pattern[j] == 'D' and n[j] > n[j + 1])
                    for j in range(len(pattern))
                ):
                print(f"count: {count}")
                return ''.join(self.perms[i][:len(pattern) + 1])

    def factorial(self, n: int) -> int:
        if n < 2:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def smallestNumber(self, pattern: str) -> str:
        """
        O(9! * 9 * len(pattern)) time, O(9!) space brute force solution.
        Optimized to skip over candidates which cannot be solutions.
        Because `self.perms` is generated in lexicographic order, the first
        candidate which matches `pattern` is guaranteed to be the
        lexicographically smallest.
        """
        i = 0
        j = 9
        while i < len(self.perms):
            n = [ord(d) - self.ord0 for d in self.perms[i]]
            # Use `for...break...else`` instead of `all(...)` because namespace inside `all()` is inaccessible outside
            for j in range(len(pattern)):
                if not ((pattern[j] == 'I' and n[j] < n[j + 1]) or (pattern[j] == 'D' and n[j] > n[j + 1])):
                    break
            else:
                return ''.join(self.perms[i][:len(pattern) + 1])
            
            # Skip over elements that cannot possibly be solutions
            # If the pattern fails at index `j`, then any candidates that have the same value n[j] are also excluded.
            # Because `self.perms` is generated in lexicographic order, there are (8 - j)! elements that we can immediately eliminate.
            i += self.factorial(8 - j)