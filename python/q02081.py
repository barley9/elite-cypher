"""
2081. Sum of k-Mirror Numbers

A k-mirror number is a positive integer without leading zeros that reads the
same both forward and backward in base-10 as well as in base-k.
    For example, `9` is a 2-mirror number. The representation of 9 in base-10
        and base-2 are `9` and `1001` respectively, which read the same both
        forward and backward.
    On the contrary, `4` is not a 2-mirror number. The representation of `4`
        in base-2 is `100`, which does not read the same both forward and
        backward.

Given the base `k` and the number `n`, return the sum of the `n` smallest
k-mirror numbers.
"""

from typing import List
import itertools

class Solution:
    numerals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def palindromes_even() -> str:
        """
        Infinite generator of base-10 palindromes with *even* length
        """
        for n in itertools.count(1):
            s = str(n)
            yield s + s[::-1]

    @staticmethod
    def palindromes_odd() -> str:
        """
        Infinite generator of base-10 palindromes with *odd* length
        """
        digit_str = tuple(str(i) for i in range(10))

        for n in range(1, 10):  # skip `0`
            yield digit_str[n]

        for n in itertools.count(1):
            s = str(n)
            srev = s[::-1]
            for mid in digit_str:
                yield s + mid + srev

    def palindromes(self) -> str:
        """
        Generates base-10 palindromic integers in order of increasing
        numerical value
        """
        gen_evn = self.palindromes_even()
        gen_odd = self.palindromes_odd()
        
        prev_evn = next(gen_evn)
        prev_odd = next(gen_odd)
        
        length = 1  # number of digits in palindrome
        
        while True:
            # Generate odd-length palindromes while number of digits is constant
            n = prev_odd
            while len(n) == length:
                yield n
                n = next(gen_odd)
            prev_odd = n  # store next number for later
            length += 1

            # Generate even-length palindromes while number of digits is constant
            n = prev_evn
            while len(n) == length:
                yield n
                n = next(gen_evn)
            prev_evn = n
            length += 1

    @staticmethod
    def is_palindrome(seq: List) -> bool:
        """Returns True if `seq` is a palindrome, False otherwise"""
        return all(
            seq[i] == seq[-i - 1]
            for i in range(len(seq) // 2)
        )

    def to_base(self, n: int, b: int=10) -> List[str]:
        """
        Returns the list of numerals in the base-`b` representation of the
        integer `n` in increasing order of place value. If `n` is `0`, returns
        an empty list.
        """
        if b == 10:
            return list(reversed(str(n)))
        elif b == 2:
            return list(reversed(f'{n:b}'))
        elif b == 8:
            return list(reversed(f'{n:o}'))
        elif b == 16:
            return list(reversed(f'{n:X}'))

        result = []
        while n:
            n, r = divmod(n, b)
            result.append(self.numerals[r])
        return result

    def kMirror(self, k: int, n: int) -> int:
        mirror_numbers = []
        for p in self.palindromes():
            if self.is_palindrome(self.to_base(int(p), k)):
                mirror_numbers.append(int(p))
                if len(mirror_numbers) >= n:
                    break
        # print(mirror_numbers)
        return sum(mirror_numbers)

if __name__ == '__main__':
    odd = Solution.palindromes_odd()
    evn = Solution.palindromes_even()
    for _ in range(100):
        print(next(odd))
    print()
    for _ in range(100):
        print(next(evn))
    print()

    g = Solution().palindromes()
    for _ in range(1000):
        print(next(g))
    print()

    print(Solution().to_base(255, 16))
    print()

    print(Solution().kMirror(7, 17))