"""
1758. Minimum Changes To Make Alternating Binary String

You are given a string `s` consisting only of the characters '0' and '1'. In
one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For
example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""

class Solution:
    def minOperations(self, s: str) -> int:
        """WRONG"""
        ord0 = ord('0')

        digits = [ord(d) - ord0 for d in s]
        print(digits)

        count = 0
        for i in range(1, len(digits)):
            if digits[i - 1] == digits[i]:
                digits[i] ^= 1  # if adjacent digits are the same, toggle
                count += 1
        print(digits)

        return count

    def minOperations(self, s: str) -> int:
        ord0 = ord('0')

        digits = [ord(d) - ord0 for d in s]
        diffs = [
            digits[i] - digits[i - 1]
            for i in range(1, len(digits))
        ]

        print(digits)
        print(diffs)