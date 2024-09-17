"""
884. Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists
only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does
not appear in the other sentence.

Given two sentences `s1` and `s2`, return a list of all the uncommon words. You
may return the answer in any order.
"""

import collections

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """INCORRECT; doesn't handle duplicate words in one string"""
        s1 = set(s1.split(" "))
        s2 = set(s2.split(" "))
        return (s1 - s2) | (s2 - s1)

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        seen = set()
        result = set()
        for word in s1.split(" ") + s2.split(" "):
            if word in seen:
                try:
                    result.remove(word)
                except KeyError:
                    pass
            else:
                result.add(word)
            seen.add(word)
        return result

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = collections.Counter(s1.split() + s2.split())
        return [word for word in words if words[word] == 1]

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        O(n ** 2) time, O(n) space solution, where n is the total number of
        words in s1 and s2. (WHY IS THIS SO FAST?!?)
        """
        words = s1.split() + s2.split()
        return [word for word in words if words.count(word) == 1]