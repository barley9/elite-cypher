"""
299. Bulls and Cows

You are playing the [Bulls and Cows](wikipedia.org/wiki/Bulls_and_cows) game
with your friend.

You write down a secret number and ask your friend to guess what the number
is. When your friend makes a guess, you provide a hint with the following info:
    The number of "bulls", which are digits in the guess that are in the
        correct position.
    The number of "cows", which are digits in the guess that are in your
        secret number but are located in the wrong position. Specifically, the
        non-bull digits in the guess that could be rearranged such that they
        become bulls.

Given the secret number `secret` and your friend's guess `guess`, return the
hint for your friend's guess.

The hint should be formatted as "xAyB", where `x` is the number of bulls and
`y` is the number of cows. Note that both `secret` and `guess` may contain
duplicate digits.
"""

import collections

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        counts_g, counts_s = collections.Counter(), collections.Counter()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                counts_g.update(guess[i])
                counts_s.update(secret[i])
        # bulls = sum(
        #     secret[i] == guess[i]
        #     for i in range(len(secret))
        # )

        cows = (counts_g & counts_s).total()

        return f"{bulls}A{cows}B"

    def getHint(self, secret: str, guess: str) -> str:
        """O(n) time, O(1) space solution"""
        ord0 = ord('0')
        bulls, cows = 0, 0
        sct_counts, gss_counts = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                sct_counts[ord(s) - ord0] += 1
                gss_counts[ord(g) - ord0] += 1
        cows = sum(
            min(ds, dg)
            for ds, dg in zip(sct_counts, gss_counts)
        )
        return f"{bulls}A{cows}B"