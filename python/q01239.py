"""
1239. Maximum Length of a Concatenated String with Unique Characters

You are given an array of strings `arr`. A string `s` is formed by the concatenation of a subsequence of `arr` that has unique characters.

Return the maximum possible length of `s`.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
"""


from typing import List, Iterable
import itertools

def powerset(iterable: Iterable) -> Iterable:
    """
    Example:
        powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    Taken from https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )

def maxLength(self, arr: List[str]) -> int:
    charsets = [set(s) for s in arr]
    arrset = set(c for s in arr for c in s)
    # print(charsets)
    # print(arrset)
    maxlen = 0

    for subset in powerset(charsets):
        print(subset, arrset.intersection(*subset))

        overlap = arrset.intersection(*subset)
        if not overlap and sum(len(s) for s in subset) > maxlen:
            maxlen = sum(len(s) for s in subset)

    return maxlen

if __name__ == '__main__':
    tests = [
        ["un","iq","ue"],
        ["cha","r","act","ers"],
        ["abcdefghijklmnopqrstuvwxyz"],
    ]

    for test in tests:
        print(maxLength(None, test), end='\n\n')