"""
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    - `countAndSay(1) = "1"`
    - `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
"""


import functools

class Solution:
    @functools.lru_cache
    def countAndSay(self, n: int) -> str:
        """
        This is sequence A005150 in the OEIS.
        """
        if n == 1:
            return '1'
        
        s = self.countAndSay(n - 1)
        groups = []
        i = 0
        for j in range(1, len(s)):
            if s[i] != s[j]:
                groups.append(s[i:j])
                i = j
        groups.append(s[i:])

        return ''.join(str(len(g)) + g[0] for g in groups)