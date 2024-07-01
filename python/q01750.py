"""
1750. Minimum Length of String After Deleting Similar Ends

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

    Pick a non-empty prefix from the string `s` where all the characters in the prefix are equal.
    Pick a non-empty suffix from the string `s` where all the characters in this suffix are equal.
    The prefix and the suffix should not intersect at any index.
    The characters from the prefix and suffix must be the same.
    Delete both the prefix and the suffix.

Return the minimum length of `s` after performing the above operation any number of times (possibly zero times).
"""

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while right > left:
            if s[left] != s[right]:
                return right - left + 1

            # print('\n' + (' ' * left) + 'v' + (' ' * (right - left - 1)) + 'v')
            # print(s)
            
            # gobble any  number of identical characters
            # print('\t', end='')
            prev = s[left]
            while left < len(s) and s[left] == prev:
                # print(s[left], end='')
                left += 1
            # print()

            # print('\t', end='')
            prev = s[right]
            while right > -1 and s[right] == prev:
                # print(s[right], end='')
                right -= 1
            # print()

        return int(left == right)