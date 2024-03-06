"""
451. Sort Characters By Frequency

Given a string `s`, sort it in decreasing order based on the frequency of the
characters. The frequency of a character is the number of times it appears in
the string.

Return the sorted string. If there are multiple answers, return any of them.
"""

import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        # get `Counter()` of character frequencies
        freq = collections.Counter(s)

        # sort descending by frequency
        sorted_freq = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # join frequency-length runs of each character and return
        return ''.join(item[0] * item[1] for item in sorted_freq)
        
    def frequencySort(self, s: str) -> str:
        """
        One-liner solution using `collections.Counter`. Because of sorting,
        O(n log n).
        """
        # Get `Counter()` of character frequencies, sort descending by
        # frequency, then join frequency-length runs of each character
        return ''.join(item[0] * item[1] for item in sorted(
            collections.Counter(s).items(),
            key=lambda item: item[1],
            reverse=True))