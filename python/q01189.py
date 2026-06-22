"""
1189. Maximum Number of Balloons

Given a string `text`, you want to use the characters of `text` to form as many
instances of the word "balloon" as possible.

You can use each character in `text` at most once. Return the maximum number of
instances that can be formed.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """O(n) time, O(1) space solution"""
        counts = {c : 0 for c in 'balloon'}

        for c in text:
            if c in counts: # ignore any chars not in 'balloon'
                counts[c] += 1
        
        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,  # we need two 'l' and two 'o' for each 'balloon'
            counts['o'] // 2,
            counts['n'],
        )