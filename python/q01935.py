"""
1935. Maximum Number of Words You Can Type

There is a malfunctioning keyboard where some letter keys do not work. All
other keys on the keyboard work properly.

Given a string `text` of words separated by a single space (no leading or
trailing spaces) and a string `brokenLetters` of all distinct letter keys that
are broken, return the number of words in `text` you can fully type using this
keyboard.
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        total = 0
        for word in text.split(' '):
            if all(c not in word for c in brokenLetters):
                total += 1
        return total

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cant_type = set(brokenLetters)
        total, fails = 0, 0  # total typable words, num failed keystrokes in current word
        for c in text:
            if c == ' ':
                if fails == 0:
                    total += 1
                fails = 0
            elif c in cant_type:
                fails += 1
        return total + (fails == 0)

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        total, fails = 0, 0  # total typable words, num failed keystrokes in current word
        for c in text:
            if c == ' ':
                if fails == 0:
                    total += 1
                fails = 0
            elif c in brokenLetters:
                fails += 1
        return total + (fails == 0)

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        total = 0
        for word in text.split(' '):
            if not (set(word) & brokenLetters):
                total += 1
        return total

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        failed = 0
        for word in text.split(' '):
            failed += any(c in word for c in brokenLetters)
        return text.count(' ') - failed + 1

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        O(m*n*k) time, O(m*n) space solution where m = len(text.split(' ')),
        n = max(len(word) for word in text.split(' ')), and k = len(brokenLetters)
        """
        failed = 0
        for word in text.split(' '):
            for c in word:
                if c in brokenLetters:
                    failed += 1
                    break
        return text.count(' ') - failed + 1