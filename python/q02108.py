"""
2108. Find First Palindromic String in the Array

Given an array of strings `words`, return the first palindromic string in the
array. If there is no such string, return an empty string `""`.

A string is palindromic if it reads the same forward and backward.
"""

class Solution:
    def isPalindrome(self, word: str) -> bool:
        """
        Returns True if word is a palindromic string, False otherwise
        If n = len(word), this function is O(n / 2) time and O(1) space
        """
        for i in range(len(word) // 2):
            if word[i] != word[-(i + 1)]:
                return False
        return True

    def isPalindrome(self, word: str) -> bool:
        """
        Returns True if word is a palindromic string, False otherwise.
        If n = len(word), this function is O(n) time and O(n) space because
        python string slicing creates a copy.
        """
        return word == word[::-1]

    def firstPalindrome(self, words: List[str]) -> str:
        """
        This solution is O(m * n), where m = len(words) and n = max(len(w) for
        w in words)
        """
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
    
    # Most optimized version
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]: return word
        return ""