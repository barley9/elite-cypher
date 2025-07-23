"""
1717. Maximum Score From Removing Substrings

You are given a string `s` and two integers `x` and `y`. You can perform two
types of operations any number of times.
    Remove substring "ab" and gain `x` points. (E.g. when removing "ab" from
        "cabxbae" it becomes "cxbae".)
    Remove substring "ba" and gain `y` points. (E.g. when removing "ba" from
        "cabxbae" it becomes "cabxe".)

Return the maximum points you can gain after applying the above operations on `s`.
"""

class Solution:
    @staticmethod
    def score(s: str, points: int, substring: str) -> tuple[int, str]:
        """helper method"""
        total = 0

        index = s.find(substring)
        while index != -1:
            total += points
            s = s[:index] + s[index + len(substring):]
            index = s.find(substring)

        return total, s

    def maximumGain(self, s: str, x: int, y: int) -> int:
        """O(n^2) time, O(1) space solution; TOO SLOW"""
        total = 0

        if x > y:
            temp, s = self.score(s, x, 'ab')
            total += temp
            temp, s = self.score(s, y, 'ba')
            total += temp
        else:
            temp, s = self.score(s, y, 'ba')
            total += temp
            temp, s = self.score(s, x, 'ab')
            total += temp
        
        return total

    def maximumGain(self, s: str, x: int, y: int) -> int:
        """INCORRECT"""
        total = 0
        if x > y:
            total += x * s.count('ab')
            print(total)
            total += y * (''.join(s.split('ab')).count('ba'))
            print(
                s.split('ab'),
                ''.join(s.split('ab')),
                ''.join(s.split('ab')).count('ba'),
            )
        else:
            total += y * s.count('ba')
            print(total)
            total += x * (''.join(s.split('ba')).count('ab'))
            print(
                s.split('ba'),
                ''.join(s.split('ba')),
                ''.join(s.split('ba')).count('ab'),
            )
        return total

    def maximumGain(self, s: str, x: int, y: int) -> int:
        """O(n) time, O(n) space solution"""
        total = 0

        used = set()  # indices already "removed" from `s`
        stack = []  # [(char, index), ...]
        if x > y:
            left, right, points = 'a', 'b', x
        else:
            left, right, points = 'b', 'a', y

        # Search `s` for matching `left` `right` pairs
        for i, c in enumerate(s):
            if c == right:
                top = stack[-1] if stack else (-1, '')
                if top[1] == left:
                    stack.pop()
                    total += points
                    used |= {i, top[0]}
            else:
                stack.append((i, c))
            
            # print([c for i, c in stack], used, total)

        # Swap `left` and `right` and search again
        stack = []
        left, right = right, left
        points = x if points == y else y
        # print()
        
        for i, c in enumerate(s):
            if (c == right) and (i not in used):
                top = stack[-1] if stack else (-1, '')
                if top[1] == left:
                    stack.pop()
                    total += points
                    used |= {i, top[0]}
            else:
                if i not in used:
                    stack.append((i, c))
            
            # print([c for i, c in stack], used, total)
        
        return total