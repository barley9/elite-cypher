"""
2264. Largest 3-Same-Digit Number in String

You are given a string `num` representing a large integer. An integer is good if it meets the following conditions:
 * It is a substring of `num` with length `3`.
 * It consists of only one unique digit.

Return the maximum good integer as a string or an empty string `""` if no such integer exists.

Note:
 * A substring is a contiguous sequence of characters within a string.
 * There may be leading zeroes in `num` or a good integer.
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_ints = set()
        i = 0
        j = 1
        while j < len(num):
            if num[i] == num[j]:
                if j - i >= 2:
                    good_ints.add(int(num[i:j + 1]))
                    i = j
            else:
                i = j
            j += 1

        return f"{max(good_ints):03}" if good_ints else ""

    def largestGoodInteger(self, num: str) -> str:
        max_int = -1
        i = 0
        j = 1
        while j < len(num):
            if num[i] == num[j]:
                if j - i >= 2:
                    n = int(num[i:j + 1])
                    if n > max_int:
                        max_int = n
                    i = j
            else:
                i = j
            j += 1

        return f"{max_int:03}" if max_int > -1 else ""