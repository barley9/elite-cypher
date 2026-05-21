"""
3043. Find the Length of the Longest Common Prefix

You are given two arrays with positive integers `arr1` and `arr2`.

A prefix of a positive integer is an integer formed by one or more of its
digits, starting from its leftmost digit. For example, `123` is a prefix of the
integer `12345`, while `234` is not.

A common prefix of two integers `a` and `b` is an integer `c`, such that `c` is
a prefix of both `a` and `b`. For example, `5655359` and `56554` have common
prefixes `565` and `5655` while `1223` and `43456` do not have a common prefix.

You need to find the length of the longest common prefix between all pairs of
integers `(x, y)` such that `x` belongs to `arr1` and `y` belongs to `arr2`.

Return the length of the longest common prefix among all pairs. If no common
prefix exists among them, return `0`.
"""


import functools


class TrieNode:
    def __init__(self):
        self.children = [None] * 10
    
    def insert(self, digits: List[int]) -> None:
        if not digits:
            return

        i = digits[0]
        if not self.children[i]:
            self.children[i] = TrieNode()
        self.children[i].insert(digits[1:])
    
    def contains_prefix(self, prefix: List[int]) -> bool:
        if not prefix:
            return True
        
        i = prefix[0]
        return bool(self.children[i]) and self.children[i].contains_prefix(prefix[1:])
    
    def longest_prefix(self, prefix: List[int]) -> int:
        if len(prefix) == 0:
            return 0
        
        i = prefix[0]
        if (self.children[i] is not None):
            return 1 + self.children[i].longest_prefix(prefix[1:])
        else:
            return 0

@functools.lru_cache(maxsize=None)
def digit_list(n: int) -> List[int]:
    """
    Returns a list of the digits of `n` in decending order of place value
    """
    result = []
    while n:
        result.append(n % 10)
        n //= 10
    return result[::-1]

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        O(m * max(len(i)) + n * max(len(j))) time, O(m) space solution where
        `i` is an element of `arr1` and `j` is an element of `arr2`
        """
        t = TrieNode()
        for n in arr1:
            t.insert(digit_list(n))

        max_prefix_len = 0
        for n in arr2:
            p = t.longest_prefix(digit_list(n))
            if p > max_prefix_len:
                max_prefix_len = p
        
        return max_prefix_len