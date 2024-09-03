"""
1945. Sum of Digits of String After Convert

You are given a string `s` consisting of lowercase English letters, and an
integer `k`.

First, convert `s` into an integer by replacing each letter with its position in
the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then,
transform the integer by replacing it with the sum of its digits. Repeat the
transform operation `k` times in total.

For example, if `s = "zbax"` and `k = 2`, then the resulting integer would be
`8` by the following operations:
    Convert: "zbax" -> "(26)(2)(1)(24)" -> "262124" -> 262124
    Transform #1: `262124 -> 2 + 6 + 2 + 1 + 2 + 4 -> 17`
    Transform #2: `17 -> 1 + 7 -> 8`

Return the resulting integer after performing the operations described above.
"""

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        orda = ord('a')
        ord0 = ord('0')
        n = ''.join(str(ord(c) - orda + 1) for c in s)
        for _ in range(k):
            # print(n)
            n = str(sum((ord(d) - ord0) for d in n))
        return int(n)

    def getLucky(self, s: str, k: int) -> int:
        orda = ord('a')
        ord0 = ord('0')
        n = ''.join(str(ord(c) - orda + 1) for c in s)
        for _ in range(k):
            sum_of_digits = sum((ord(d) - ord0) for d in n)
            if sum_of_digits > 9:
                n = str(sum_of_digits)  # str() is slower than chr(), so use sparingly
            else:
                n = chr(sum_of_digits + ord0)
        return int(n)

    def getLucky(self, s: str, k: int) -> int:
        orda = ord('a')
        ord0 = ord('0')
        char_map = {chr(i) : str(i - orda + 1) for i in range(orda, ord('z') + 1)}
        n = ''.join(char_map[c] for c in s)
        for _ in range(k):
            sum_of_digits = sum(ord(d) - ord0 for d in n)
            if sum_of_digits > 9:
                n = str(sum_of_digits)  # str() is slower than chr(), so use sparingly
            else:
                n = chr(sum_of_digits + ord0)
        return int(n)