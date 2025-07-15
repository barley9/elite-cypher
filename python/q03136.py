"""
3136. Valid Word

A word is considered valid if:
    It contains a minimum of 3 characters.
    It contains only digits (0-9), and English letters (uppercase and lowercase).
    It includes at least one vowel.
    It includes at least one consonant.

You are given a string `word`.

Return `true` if `word` is valid, otherwise, return `false`.

Notes:
    'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
    A consonant is an English letter that is not a vowel.
"""

class Solution:
    valid = {chr(i) for i in range(ord('0'), ord('9') + 1)} | \
            {chr(i) for i in range(ord('A'), ord('Z') + 1)} | \
            {chr(i) for i in range(ord('a'), ord('z') + 1)}
    vowels = set('aeiouAEIOU')
    consonants = valid - vowels - {chr(i) for i in range(ord('0'), ord('9') + 1)}

    def isValid(self, word: str) -> bool:
        s = set(word)
        return (len(word) >= 3) and \
               (s <= self.valid) and \
               (len(s & self.vowels) > 0) and \
               (len(s & self.consonants) > 0)

class Solution:
    numerals = {chr(i) for i in range(ord('0'), ord('9') + 1)}
    vowels = set('aeiouAEIOU')
    consonants = {chr(i) for i in range(ord('A'), ord('Z') + 1)} | \
                 {chr(i) for i in range(ord('a'), ord('z') + 1)} - \
                 vowels

    def isValid(self, word: str) -> bool:
        """O(n) time, O(1) space solution"""
        if len(word) < 3:
            return False

        vow = False  # flag for 'word contains at least one vowel'
        con = False  # flag for 'word contains at least one consonant'
        for c in word:
            if c in self.vowels:
                vow = True
            elif c in self.consonants:
                con = True
            elif c in self.numerals:
                pass
            else:
                return False
        return vow and con

class Solution:
    ord0, ord9 = ord('0'), ord('9')
    orda, ordz = ord('a'), ord('z')
    ordA, ordZ = ord('A'), ord('Z')
    vowels = {ord(c) for c in 'aeiouAEIOU'}

    def isValid(self, word: str) -> bool:
        """O(n) time, O(1) space solution"""
        if len(word) < 3:
            return False

        vow = False  # flag for 'word contains at least one vowel'
        con = False  # flag for 'word contains at least one consonant'
        for c in word:
            ordc = ord(c)
            if (self.orda <= ordc <= self.ordz) or (self.ordA <= ordc <= self.ordZ):
                if ordc in self.vowels:
                    vow = True
                else:
                    con = True
            elif self.ord0 <= ordc <= self.ord9:
                pass
            else:
                return False
        return vow and con

    def isValid(self, word: str) -> bool:
        """O(n) time, O(1) space solution"""
        if len(word) < 3:
            return False

        vow = False  # flag for 'word contains at least one vowel'
        con = False  # flag for 'word contains at least one consonant'
        for c in word:
            ordc = ord(c)
            if ordc in self.vowels:
                vow = True
            elif (self.orda <= ordc <= self.ordz) or (self.ordA <= ordc <= self.ordZ):
                con = True
            elif self.ord0 <= ordc <= self.ord9:
                pass
            else:
                return False
        return vow and con