"""
2452. Words Within Two Edits of Dictionary

You are given two string arrays, `queries` and `dictionary`. All words in each
array comprise of lowercase English letters and have the same length.

In one edit you can take a word from `queries`, and change any letter in it to
any other letter. Find all words from `queries` that, after a maximum of two
edits, equal some word from `dictionary`.

Return a list of all words from `queries`, that match with some word from
`dictionary` after a maximum of two edits. Return the words in the same order
they appear in `queries`.
"""

class Solution:
    @staticmethod
    def hamming_distance(s1: str, s2: str) -> int:
        # return sum(c1 != c2 for c1, c2 in zip(s1, s2))
        return sum(s1[i] != s2[i] for i in range(len(s1)))

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        """
        O(m * n * l) time, O(m) space solution where m = len(queries),
        n = len(dictionary), and l = len(queries[0])
        """
        result = []
        for q in queries:
            for d in dictionary:
                if self.hamming_distance(q, d) <= 2:
                    result.append(q)
                    break
        return result