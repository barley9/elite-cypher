"""
279. Perfect Squares

Given an integer `n`, return the least number of perfect square numbers that
sum to `n`.

A perfect square is an integer that is the square of an integer; in other
words, it is the product of some integer with itself. For example, `1`, `4`,
`9`, and `16` are perfect squares while `3` and `11` are not.
"""

import math
import functools

class Solution:
    def numSquares(self, n: int) -> int:
        """Greedy algorithm; incorrect"""

        i = math.ceil(math.sqrt(n))  # check for squares up to i**2
        
        print(n, i)

        count = 0
        while i > 0:
            if n - i * i >= 0:
                n = n - i * i
                print('\t', i*i, n)
                count += 1

                if n == 0:
                    break
            else:
                i -= 1

        return count

    def numSquares(self, n: int) -> int:
        """Still greedy, just one exhaustive step; still incorrect"""
        N = n
        min_count = 10 ** 7  # +INF
        for i in range(math.ceil(math.sqrt(n)), 0, -1):  # check for squares up to i**2
            print("i",  i)
            n = N  # reset n back to original value
            count = 0
            while i > 0:
                if n - i * i >= 0:
                    n = n - i * i
                    print('\t', i*i, n)
                    count += 1

                    if n == 0:
                        break
                else:
                    i -= 1
            
            print("count", count)
            
            if 0 < count < min_count:
                min_count = count
        
        return min_count

    @functools.lru_cache
    def numSquares(self, n: int) -> int:
        """Dynamic programming solution; believed correct, but too slow"""
        if n == 1:
            return 1

        m = math.ceil(math.sqrt(n))  # m * m = smallest square less than or equal to n
        counts = []
        for i in range(m, 0, -1):
            print(n, i * i)
            if n - i * i > 0:
                counts.append(self.numSquares(n - i * i) + 1)
            elif n - i * i == 0:
                counts.append(1)
        print(counts)
        print()
        return min(counts)