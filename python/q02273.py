"""
2273. Find Resultant Array After Removing Anagrams

You are given a 0-indexed string array `words`, where `words[i]` consists of
lowercase English letters.

In one operation, select any index `i` such that `0 < i < words.length` and
`words[i - 1]` and `words[i]` are anagrams, and delete `words[i]` from words.
Keep performing this operation as long as you can select an index that
satisfies the conditions.

Return `words` after performing all operations. It can be shown that selecting
the indices for each operation in any arbitrary order will lead to the same
result.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase using all the original letters exactly once. For example, "dacb"
is an anagram of "abdc".
"""

import collections
import itertools

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """INCORRECT"""
        words = list(reversed(words))
        orda = ord('a')
        counters = set()
        for i in range(len(words) - 1, -1, -1):
            counter = [0] * 26
            for c in words[i]:
                counter[ord(c) - orda] += 1
            counter = tuple(counter)
            if counter in counters:
                del words[i]
            else:
                counters.add(counter)
        return list(reversed(words))

    def removeAnagrams(self, words: List[str]) -> List[str]:
        """O(n) time, O(n) space solution"""
        orda = ord('a')
        result = []
        current_counter = collections.Counter({'a' : -1})
        for word in words:
            counter = collections.Counter(word)
            if current_counter != counter:
                result.append(word)
                current_counter = counter
        return result

    def removeAnagrams(self, words: List[str]) -> List[str]:
        """O(n) time, O(n) space solution"""
        orda = ord('a')  # alias to save repeated calculation
        result = []
        current_counter = [-1] * 26
        for word in words:
            # Count each character in `word`
            counter = [0] * 26
            for c in word:
                counter[ord(c) - orda] += 1
            # Compare to `current_counter`; if new anagram found, add to `result`
            if counter != current_counter:
                result.append(word)
                current_counter = counter
        return result

    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        O(n k log k) time, O(n) space solution, where
        `k = max(len(word) for word in words)`
        """
        result = [words[0]]  # `words[0]` will always be in output
        for i in range(1, len(words)):
            # Every word is sorted twice! I hate that this is faster.
            if sorted(words[i - 1]) != sorted(words[i]):
                result.append(words[i])
        return result

    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        O(n) time, O(n) space solution. Divides `words` into groups whose
        elements are all identical after applying `sorted()`. Then, choose the
        first element of each group and add it to result.
        """
        return [
            next(g) # first element of group `g`
            for _, g in itertools.groupby(words, sorted)
        ]