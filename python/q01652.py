"""
1652. Defuse the Bomb

You have a bomb to defuse, and your time is running out! Your informer will
provide you with a circular array `code` of length of `n` and a key `k`.

To decrypt the code, you must replace every number. All the numbers are
replaced simultaneously.
    If `k > 0`, replace the `i`th number with the sum of the next `k` numbers.
    If `k < 0`, replace the `i`th number with the sum of the previous `k` numbers.
    If `k == 0`, replace the `i`th number with `0`.

As `code` is circular, the next element of `code[n-1]` is `code[0]`, and the
previous element of `code[0]` is `code[n-1]`.

Given the circular array `code` and an integer key `k`, return the decrypted
code to defuse the bomb!
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        O(2n) time, O(2n) space solution. First, create augmented `code` by
        concatenating two copies together. That way, we don't have to worry
        anymore about its circular nature, index-out-of-bounds errors, or
        modular arithmetic.
        """
        augmented_code = code + code  # O(2n) list concatenation
        if k > 0:
            return [
                sum(augmented_code[i + 1:i + k + 1])
                for i in range(len(code))
            ]
        elif k < 0:
            return [
                sum(augmented_code[len(code) + i + k:len(code) + i])
                for i in range(len(code))
            ]
        else:
            return [0] * len(code)