"""
1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of characters `a`, `b` and `c`.

Return the number of substrings containing at least one occurrence of all
these characters `a`, `b` and `c`.

A substring is a contiguous subsequence of a string.
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """O(n**2) time, O(1) space solution; TOO SLOW"""
        orda = ord('a')
        result = 0
        for start in range(len(s) - 2):
            counts = [
                s.count('a', start, start + 2),
                s.count('b', start, start + 2),
                s.count('c', start, start + 2)
            ]
            for end in range(start + 3, len(s) + 1):
                counts[ord(s[end - 1]) - orda] += 1
                if all(counts[i] > 0 for i in range(len(counts))):
                    # If we already have a substring `p` that satisfies
                    # all(...), all other substrings `q` that contain `p`
                    # will also satisfy all(...).
                    result += len(s) - end + 1
                    break
        return result

    def numberOfSubstrings(self, s: str) -> int:
        """O(n) time, O(1) space solution; WORK IN PROGRESS"""
        orda = ord('a')
        result = 0
        start, end = 0, 3
        counts = [
            s.count('a', start, start + 2),
            s.count('b', start, start + 2),
            s.count('c', start, start + 2)
        ]
        while start < len(s) - 2:
            counts[ord(s[end - 1]) - orda] += 1
            if all(counts[i] > 0 for i in range(len(counts))):
                # If we already have a substring `p` that satisfies
                # all(...), all other substrings `q` that contain `p`
                # will also satisfy all(...).
                result += len(s) - end + 1
            else:
                end += 1
            counts[ord(s[start]) - orda] -= 1
            start += 1
        return result