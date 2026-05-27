"""
3121. Count the Number of Special Characters II

You are given a string `word`. A letter `c` is called special if it appears
both in lowercase and uppercase in `word`, and every lowercase occurrence of
`c` appears before the first uppercase occurrence of `c`.

Return the number of special letters in `word`.
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """O(n) time, O(1) space solution"""
        inf = 10 ** 7  # infinity
        ordA = ord('A')
        diff = ord('a') - ord('A')
        
        letters = [0] * 128  # use ASCII to index into `letters`

        for c in word:
            ordc = ord(c)
            # if letter is lowercase, and uppercase already exists in `word`, mark as not special
            if (97 <= ordc <= 122) and (letters[ordc - diff] > 0):
                letters[ordc] = -inf
                letters[ordc - 32] = -inf
            else:
                letters[ordc] += 1
        
        return sum(
            (letters[i] > 0) and (letters[i + diff] > 0)
            for i in range(ordA, ordA + 26 + 1)
        )