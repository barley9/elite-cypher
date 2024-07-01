import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        O(n) time, O(n) space solution. Uses the fact that all characters in a
        palindrom must appear an even number of times, except the middle
        character.
        
        Approach:
        First, pre-compute the frequencies of every character. For each
        character, find largest even number less than or equal to its frequency.
        We can do this by masking off the 1s digit in the binary expansion. Sum
        all these masked frequencies. Lastly, if at least one character had an
        odd frequency, add 1 to total.
        """
        s = collections.Counter(s)
        return sum(v & 0b11111111110 for v in s.values()) + \
               any(v & 1 for v in s.values())
    

    def longestPalindrome(self, s: str) -> int:
        orda = ord('A')
        parity = [False] * (ord('z') - orda + 1)
        for c in s:
            parity[ord(c) - orda] ^= True  # flip parity of character
        return len(s) - sum(parity) + any(p for p in parity)
    

    def longestPalindrome(self, s: str) -> int:
        parity = set()
        for c in s:
            if c in parity:
                parity.remove(c)
            else:
                parity.add(c)
        return len(s) - len(parity) + (len(parity) > 0)
    

    def longestPalindrome(self, s: str) -> int:
        """O(n) time, O(1) space solution. (Fastest so far)"""
        parity = [False] * (ord('z') + 1)
        for c in s:
            parity[ord(c)] ^= True  # flip parity of character
        return len(s) - sum(parity) + any(p for p in parity)