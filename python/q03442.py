"""
3442. Maximum Difference Between Even and Odd Frequency I

You are given a string `s` consisting of lowercase English letters.

Your task is to find the maximum difference `diff = freq(a1) - freq(a2)`
between the frequency of characters `a1` and `a2` in the string such that:
    `a1` has an odd frequency in the string.
    `a2` has an even frequency in the string.

Return this maximum difference.
"""

import collections

class Solution:
    def maxDifference(self, s: str) -> int:
        """O(n log n) time, O(n) space solution"""
        freqs = sorted(
            collections.Counter(s).items(),
            key=lambda elem: elem[1],
        )
        # print(freqs)
        
        j = len(freqs) - 1
        while (freqs[j][1] % 2 == 0):
            j -= 1
        
        i = 0
        while (freqs[i][1] % 2 == 1):
            i += 1
        
        # print(freqs[i], freqs[j])
        return freqs[j][1] - freqs[i][1]

    def maxDifference(self, s: str) -> int:
        max_odd_freq = -1
        min_evn_freq = 1000  # infinity
        freqs = collections.Counter(s)
        for ch in freqs:
            if freqs[ch] & 1:
                if freqs[ch] > max_odd_freq:
                    max_odd_freq = freqs[ch]
            else:
                if freqs[ch] < min_evn_freq:
                    min_evn_freq = freqs[ch]
        return max_odd_freq - min_evn_freq

    def maxDifference(self, s: str) -> int:
        """O(n) time, O(n) space solution"""
        max_odd_freq = -1
        min_evn_freq = 1000  # infinity
        freqs = collections.Counter(s)
        for ch in freqs:
            if (freqs[ch] % 2 == 1) and (freqs[ch] > max_odd_freq):
                max_odd_freq = freqs[ch]
            elif (freqs[ch] % 2 == 0) and (freqs[ch] < min_evn_freq):
                min_evn_freq = freqs[ch]
        return max_odd_freq - min_evn_freq