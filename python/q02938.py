"""
2938. Separate Black and White Balls

There are `n` balls on a table, each ball has a color black or white.

You are given a 0-indexed binary string `s` of length `n`, where `1` and `0`
represent black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return the minimum number of steps to group all the black balls to the right
and all the white balls to the left.
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        """INCORRECT"""
        first = 0  # index of left-most '1'
        count = 0  # number of '0's to the right of left-most '1'
        for first in range(len(s)):
            if s[first] == '1':
                break
        for i in range(first + 1, len(s)):
            if s[i] == '0':
                count += 1
        return count

    def minimumSteps(self, s: str) -> int:
        """O(2 * n) time, O(n) space solution"""
        indices = []
        for i in range(len(s)):
            if s[i] == '0':
                indices.append(i - len(indices))
        print(indices)
        return sum(indices)

    def minimumSteps(self, s: str) -> int:
        """O(n) time, O(1) space solution"""
        count = 0  # number of '0's
        moves = 0  # number of swaps necessary
        for i in range(len(s)):
            if s[i] == '0':
                moves += i - count
                count += 1
        return moves

    def minimumSteps(self, s: str) -> int:
        """INCORRECT"""
        for first in range(len(s)):
            if s[first] == '0':
                break
        count = 1
        for i in range(first + 1, len(s)):
            if s[i] == '0':
                count += 1
        return first * count

    def minimumSteps(self,s):
        count = 0  # total number of '1's
        moves = 0  # total number of swaps necessary
        for c in s:
            if c == '0':
                moves += count  # each '0' needs to be swapped with every previous '1'
            else:
                count += 1
        return moves


# Golfed version (beats 100.00%)
def minimumSteps(s):
 count,moves=0,0
 for c in s:
  if c=='0':moves+=count
  else:count+=1
 return moves
results=[minimumSteps(loads(s)) for s in sys.stdin]
with open('user.out','w') as f:f.write(str(results)[1:-1].replace(', ','\n')+'\n')
sys.exit(0)