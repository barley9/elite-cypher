"""
1137. N-th Tribonacci Number

The Tribonacci sequence $T_n$ is defined as follows: 

$T_0 = 0$, $T_1 = 1$, $T_2 = 1$, and $T_{n+3} = T_n + T_{n+1} + T_{n+2}$ for $n >= 0$.

Given `n`, return the value of $T_n$.
"""

import functools

class Solution:
    @functools.lru_cache
    def tribonacci(self, n: int) -> int:
        """Recursive solution using dynamic programming"""
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        return self.tribonacci(n - 3) + \
               self.tribonacci(n - 2) + \
               self.tribonacci(n - 1)
    
    def tribonacci(self, n: int) -> int:
        """Iterative O(n) solution"""
        if n < 2:
            return n

        a, b, c = 0, 1, 1

        for i in range(3, n + 1):
            a, b, c = b, c, a+b+c
        
        return c