"""
1545. Find Kth Bit in Nth Binary String

Given two positive integers `n` and `k`, the binary string `S_n` is formed as
follows:
    `S_1 = "0"`
    `S_i = S_i - 1 + "1" + reverse(invert(S_i - 1))` for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the
reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes
to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:
    `S_1 = "0"`
    `S_2 = "011"`
    `S_3 = "0111001"`
    `S_4 = "011100110110001"`

Return the `k`th bit in `S_n`. It is guaranteed that `k` is valid for the given
`n`.
"""


import functools

class Solution:
    @staticmethod
    @functools.lru_cache(maxsize=None)
    def seq(n: int) -> str:
        """O(n * 2^n) time, O(n * 2^n) space helper function"""
        if n == 1:
            return "0"

        return Solution.seq(n - 1) + "1" + ''.join(map(
            lambda digit: "1" if digit == "0" else "0",
            reversed(Solution.seq(n - 1)),
        ))

    def findKthBit(self, n: int, k: int) -> str:
        for i in range(1, n + 1):
            print(
                Solution.seq(i),
                int(self.seq(i), 2),
                sep=", "
            )

        print(Solution.seq.cache_info())

        return Solution.seq(n)[k - 1]


    @staticmethod
    @functools.lru_cache(maxsize=None)
    def seq(n: int) -> list[int]:
        """O(n * 2^n) time, O(n * 2^n) space helper function"""
        if n == 1:
            return [0]

        return Solution.seq(n - 1) + [1] + list(map(
            lambda digit: digit ^ 1,
            reversed(Solution.seq(n - 1)),
        ))

    def findKthBit(self, n: int, k: int) -> str:
        for i in range(1, n + 1):
            print(
                Solution.seq(i),
                int(''.join(
                    chr(d + ord('0'))
                    for d in Solution.seq(i)
                ), 2),
                sep=", "
            )

        print(Solution.seq.cache_info())

        return str(Solution.seq(n)[k - 1])


    def findKthBit(self, n: int, k: int) -> str:
        """O(n) time, O(1) space solution"""
        if n == 1:
            return "0"

        # Because a '1' is always inserted between the sequence and the
        # reversed sequence, the middle bit will always be a '1'
        middle = 1 << (n - 1)
        if k == middle:
            return "1"
        
        # First half of previous sequence is not reversed, so search there for
        # `k`th digit
        if k < middle:
            return self.findKthBit(n - 1, k)
        
        # Second half of sequence is reversed, so mirror `k` and search there
        mirrored = (1 << n) - k
        kthbit = self.findKthBit(n - 1, mirrored)

        # Invert bit and return
        return "1" if kthbit == "0" else "0"