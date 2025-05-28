"""
2942. Find Words Containing Character

You are given a 0-indexed array of strings `words` and a character `x`.

Return an array of indices representing the words that contain the character `x`.

Note that the returned array may be in any order.
"""

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        words = [set(word) for word in words]
        return [i for i in range(len(words)) if x in words[i]]

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            if x in set(words[i]):
                result.append(i)
        return result

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        O(n * m) time, O(n) space solution, where
        m = max(len(word) for wordin words)
        """
        return [i for i, word in enumerate(words) if x in word]