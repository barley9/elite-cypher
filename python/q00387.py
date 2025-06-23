"""
387. First Unique Character in a String

Given a string `s`, find the first non-repeating character in it and return
its index. If it does not exist, return `-1`.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}  # dict mapping characters in `s` to list of indices where character appears
        
        # Populate `seen`; O(n)
        for i, c in enumerate(s):
            if c in seen:
                seen[c].append(i)
            else:
                seen[c] = [i]
        
        # Locate and return first character which appears only once in `s`; O(n)
        for idx_list in seen.values():
            if len(idx_list) == 1:
                return idx_list[0]

        return -1  # default return if none exists