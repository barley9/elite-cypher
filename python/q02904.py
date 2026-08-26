"""
2904. Shortest and Lexicographically Smallest Beautiful String

You are given a binary string `s` and a positive integer `k`.

A substring of `s` is beautiful if the number of `1`'s in it is exactly `k`.

Let `len` be the length of the shortest beautiful substring.

Return the lexicographically smallest beautiful substring of string `s` with
length equal to `len`. If `s` doesn't contain a beautiful substring, return an
empty string.
"""

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        """INCORRECT"""
        left, right = 0, 1
        ones_count = 1 if s[left] == '1' else 0
        subs = []

        while (left < right):
            if ones_count == k:
                if subs:
                    # Overwrite `subs` if we find a shorter string
                    if right - left < len(subs[0]):
                        subs = [s[left:right]]
                    elif right - left == len(subs[0]):
                        subs.append(s[left:right])
                else:
                    subs.append(s[left:right])

            # Sliding window
            if (right < len(s)) and (ones_count <= k):
                ones_count += 1 if s[right] == '1' else 0
                right += 1
            else:
                ones_count -= 1 if s[left] == '1' else 0
                left += 1

            print(left, right, s[left:right], ones_count, subs)
        
        print(subs)

        return sorted(subs)[0] if subs else ''

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        """O(n^2) time, O(n^2) space solution"""
        subs = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub.count('1') == k:
                    subs.append(sub)
        
        if subs:
            min_len = min(len(sub) for sub in subs)
            return sorted(
                sub
                for sub in subs
                if len(sub) == min_len
            )[0]
        else:
            return ''