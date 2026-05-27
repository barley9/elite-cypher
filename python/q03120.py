"""
3120. Count the Number of Special Characters I

You are given a string `word`. A letter is called special if it appears both in
lowercase and uppercase in `word`.

Return the number of special letters in `word`.
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """O(n) time, O(1) space solution"""
        ordA = ord('A')
        letters = [0] * (ord('z') - ord('A') + 1)

        for c in word:
            letters[ord(c) - ordA] += 1
        
        diff = ord('a') - ord('A')
        return sum(
            (letters[i] > 0) and (letters[i + diff] > 0)
            for i in range(26)
        )

    def numberOfSpecialChars(self, word: str) -> int:
        upper = ''.join(chr(i) for i in range(ord('A'), ord('A') + 26))
        lower = ''.join(chr(i) for i in range(ord('a'), ord('a') + 26))

        return sum(
            (word.count(upper[i]) > 0) and (word.count(lower[i]) > 0)
            for i in range(len(upper))
        )

    def numberOfSpecialChars(self, word: str) -> int:
        """O(2n) time, O(1) space solution"""
        ordA = ord('A')
        diff = ord('a') - ord('A')

        return sum(
            (word.count(chr(i)) > 0) and (word.count(chr(i + diff)) > 0)
            for i in range(ordA, ordA + 26)
        )