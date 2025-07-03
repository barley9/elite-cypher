"""
3304. Find the K-th Character in String Game I

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a positive integer `k`.

Now Bob will ask Alice to perform the following operation forever: Generate a
new string by changing each character in `word` to its next character in the
English alphabet, and append it to the original `word`.

For example, performing the operation on "c" generates "cd" and performing the
operation on "zb" generates "zbac".

Return the value of the `k`th character in word, after enough operations have
been done for word to have at least `k` characters.

Note that the character 'z' can be changed to 'a' in the operation.
"""

class Solution:
    def kthCharacter(self, k: int) -> str:
        """O(log(k)) time, O(k) space solution"""
        word = [0]
        # print(''.join(chr(ch + ord('a')) for ch in word))
        # print(word)
        while len(word) < k:
            word.extend([ch + 1 for ch in word])
            # print(''.join(chr(ch + ord('a')) for ch in word))
            # print(word)
        return chr(word[k - 1] + ord('a'))

    def kthCharacter(self, k: int) -> str:
        # what is the largest power of 2 that is less than `k`?