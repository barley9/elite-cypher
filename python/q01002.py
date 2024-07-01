"""
1002. Find Common Characters

Given a string array `words`, return an array of all characters that show up in
all strings within the `words` (including duplicates). You may return the answer
in any order.
"""

import collections
import numpy as np

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        O(n*k) time, O(n*k) space solution, where `n = len(words)` and
        `k = max(len(word) for word in words)`
        """
        result = collections.Counter(''.join(words))
        for word in words:
            result = result & collections.Counter(word)
        return result.elements()

    def commonChars(self, words: List[str]) -> List[str]:
        orda = ord('a')
        arr = np.vstack([[0] * 26 for _ in words])
        for i in range(len(words)):
            for c in words[i]:
                arr[i, ord(c) - orda] += 1
        result = []
        for i, count in enumerate(np.min(arr, axis=0)):
            result.extend([chr(i + orda)] * count)
        return result

    def commonChars(self, words: List[str]) -> List[str]:
        orda = ord('a')
        result = []
        for word in words:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - orda] += 1
            
            if not result:
                result = counts
            else:
                result = [min(result[i], counts[i]) for i in range(len(counts))]
        return [c for i in range(len(result)) for c in [chr(i + orda)] * result[i]]