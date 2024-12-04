"""
2825. Make String a Subsequence Using Cyclic Increments

You are given two 0-indexed strings `str1` and `str2`.

In an operation, you select a set of indices in `str1`, and for each index `i`
in the set, increment `str1[i]` to the next character cyclically. That is 'a'
becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

Return `true` if it is possible to make `str2` a subsequence of `str1` by
performing the operation at most once, and `false` otherwise.

Note: A subsequence of a string is a new string that is formed from the
original string by deleting some (possibly none) of the characters without
disturbing the relative positions of the remaining characters.
"""

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """INCORRECT due to misreading the problem"""
        orda = ord('a')
        s1 = [ord(c) - orda for c in str1]
        s2 = [ord(c) - orda for c in str2]
        
        i = 0
        j = 0
        while i < len(s1):
            d = (s1[i] - s2[j] + 26) % 26
            m = min(d, 26 - d)
            print(f"s1[{i}] = {chr(s1[i] + orda)} is distance {m} from s2[{j}] = {chr(s2[j] + orda)}")
            if m < 2:  # if we can match by rotating at most once...
                print(f"\t{m} <= 1, so move on to next char in s2")
                j += 1  # move on to next char in `s2`
                if j >= len(s2):
                    return True  # if we've matched all of `s2`, return True
            else:
                print(f"\t{m} > 1, so DON'T move on to next char in s2")
            i += 1

        return False

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        O(m) time, O(m + n) space solution, where m = len(str1) and
        n = len(str2).
        """
        orda = ord('a')
        s1 = [ord(c) - orda for c in str1]
        s2 = [ord(c) - orda for c in str2]
        
        i = 0
        j = 0
        while i < len(s1):
            d = (s2[j] - s1[i] + 26) % 26
            print(f"s1[{i}] = {chr(s1[i] + orda)} is distance {d} from s2[{j}] = {chr(s2[j] + orda)}")
            if d < 2:  # if we can match by rotating at most once...
                print(f"\t{d} <= 1, so move on to next char in s2")
                j += 1  # move on to next char in `s2`
                if j >= len(s2):
                    print("\ts2 is expended, return True")
                    return True  # if we've matched all of `s2`, return True
            else:
                print(f"\t{d} > 1, so DON'T move on to next char in s2")
            i += 1

        print("s1 is expended, return False")
        return False

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        O(m) time, O(m + n) space solution, where m = len(str1) and
        n = len(str2).
        """
        orda = ord('a')
        s1 = [ord(c) - orda for c in str1]
        s2 = [ord(c) - orda for c in str2]
        
        j = 0
        for i in range(len(s1)):
            d = (s2[j] - s1[i] + 26) % 26
            # print(f"s1[{i}] = {chr(s1[i] + orda)} is distance {d} from s2[{j}] = {chr(s2[j] + orda)}")
            if d < 2:  # if we can match by incrementing at most once...
                j += 1  # move on to next char in `s2`
                if j >= len(s2):
                    return True  # we've matched all of `s2`
        # we ran out of `s1` before matching all of `s2`
        return False

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """O(m) time, O(1) space solution, where m = len(str1)."""
        orda = ord('a')  # pre-compute for performance
        j = 0  # index into `str2`
        c2 = ord(str2[j]) - orda
        for i in range(len(str1)):
            c1 = ord(str1[i]) - orda
            d = (c2 - c1 + 26) % 26  # circular distance between `c1` and `c2`
            if d < 2:
                j += 1
                if j >= len(str2):
                    return True
                c2 = ord(str2[j]) - orda
        return False