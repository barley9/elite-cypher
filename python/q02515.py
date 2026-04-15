"""
2515. Shortest Distance to Target String in a Circular Array

You are given a 0-indexed circular string array `words` and a string `target`.
A circular array means that the array's end connects to the array's beginning.

Formally, the next element of `words[i]` is `words[(i + 1) % n]` and the
previous element of `words[i]` is `words[(i - 1 + n) % n]`, where `n` is the
length of `words`.

Starting from `startIndex`, you can move to either the next word or the
previous word with 1 step at a time.

Return the shortest distance needed to reach the string `target`. If the string
`target` does not exist in `words`, return -1.
"""

class Solution:
    def closestTarget(self,
        words: List[str],
        target: str,
        startIndex: int
    ) -> int:
        """
        O(n * L) time, O(1) space solution, where n = len(words) and
        L = len(target)
        """
        if words[startIndex] == target:
            return 0

        left  = (startIndex - 1) % len(words)
        right = (startIndex + 1) % len(words)
        # looping over `words`: O(n) time
        for dist in range(1, len(words)):
            # string comparison: O(L) time
            if (words[left] == target) or (words[right] == target):
                return dist
            
            left -= 1
            if left < 0:
                left += len(words)
            
            right += 1
            if right > len(words) - 1:
                right -= len(words)
            
            dist += 1

        return -1