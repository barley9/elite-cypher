"""
1404. Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string `s`, return the number
of steps to reduce it to `1` under the following rules:

    If the current number is even, you have to divide it by `2`.

    If the current number is odd, you have to add `1` to it.

It is guaranteed that you can always reach one for all test cases.
"""


import functools


class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        n = int(s, 2)
        print(s, n)
        while n != 1:
            if n & 1:  # if n is odd...
                n += 1  # ...add 1
            else:
                n = n >> 1  # ...divide by 2
            count += 1
        return count


    def numSteps(self, s: str) -> int:
        return self.rec_numSteps(int(s, 2))
    
    @functools.lru_cache
    def rec_numSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        if n & 1:
            return 1 + self.rec_numSteps(n + 1)
        else:
            return 1 + self.rec_numSteps(n >> 1)
