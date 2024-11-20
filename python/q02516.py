"""
2516. Take K of Each Character From Left and Right

You are given a string `s` consisting of the characters 'a', 'b', and 'c' and a
non-negative integer `k`. Each minute, you may take either the leftmost
character of `s`, or the rightmost character of `s`.

Return the minimum number of minutes needed for you to take at least `k` of
each character, or return `-1` if it is not possible to take `k` of each
character.
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        O(n) time, O(1) space solution using sliding window to find largest
        subsequence NOT to take
        """
        # If `s` isn't long enough to contain enough chars, return -1
        if len(s) < 3 * k:
            return -1
        
        # Calculate number of occurrences of each char
        orda = ord('a')
        counts = [0] * 3
        for c in s:
            counts[ord(c) - orda] += 1

        # If there aren't enough of some char, return -1
        if any(c < k for c in counts):
            return -1

        # Initialize char counts inside window
        cur_window = [0] * 3
        max_window = 0

        left = 0
        for right in range(len(s)):
            cur_window[ord(s[right]) - orda] += 1
            while left <= right and any(counts[i] - cur_window[i] < k for i in range(len(counts))):
                cur_window[ord(s[left]) - orda] -= 1
                left += 1
            if right - left + 1 > max_window:
                max_window = right - left + 1
        
        return len(s) - max_window