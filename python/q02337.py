"""
2337. Move Pieces to Obtain a String

You are given two strings `start` and `target`, both of length `n`. Each string
consists only of the characters 'L', 'R', and '_' where:
    The characters 'L' and 'R' represent pieces, where a piece 'L' can move to
        the left only if there is a blank space directly to its left, and a
        piece 'R' can move to the right only if there is a blank space directly
        to its right.
    The character '_' represents a blank space that can be occupied by any of
        the 'L' or 'R' pieces.

Return `true` if it is possible to obtain the string `target` by moving the
pieces of the string `start` any number of times. Otherwise, return `false`.
"""

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """INCORRECT"""
        if [c for c in start if c != '_'] != [c for c in target if c != '_']:
            return False
        
        L = 0b10
        R = 0b01
        configs = [0] * len(start)
        for i in range(len(start)):
            if start[i] == 'L':
                configs[i] |= L
                for j in range(i - 1, -1, -1):
                    if start[j] != '_':
                        break
                    configs[j] |= L
            elif start[i] == 'R':
                configs[i] |= R
                for j in range(i + 1, len(start)):
                    if start[j] != '_':
                        break
                    configs[j] |= R
        print([f"{n:>02b}" for n in configs])
        
        targ = [L if c == 'L' else (R if c == 'R' else 0) for c in target]
        print([f"{n:>02b}" for n in targ])

        for m, n in zip(configs, targ):
            if n == 0:
                continue
            if not (m & n):
                return False
        
        return True

    def canChange(self, start: str, target: str) -> bool:
        """
        O(4 * n) time, O(n) space solution
        """
        if [c for c in start if c != '_'] != [c for c in target if c != '_']:
            return False

        positions = [(start[i], i) for i in range(len(start)) if start[i] != '_']

        j = 0  # index into `positions`
        for i in range(len(target)):
            if target[i] == '_':
                continue
            
            if target[i] != positions[j][0]:
                return False
            if target[i] == 'L' and i > positions[j][1]:
                return False
            if target[i] == 'R' and i < positions[j][1]:
                return False

            j += 1

        return True

    def canChange(self, start: str, target: str) -> bool:
        """
        O(4 * n) time, O(n) space solution
        """
        if [c for c in start if c != '_'] != [c for c in target if c != '_']:
            return False

        positions = [(start[i], i) for i in range(len(start)) if start[i] != '_']

        j = 0  # index into `positions`
        for i in range(len(target)):
            if target[i] == '_':
                continue
            
            if target[i] != positions[j][0]:
                return False
            if target[i] == 'L' and i > positions[j][1]:
                return False
            if target[i] == 'R' and i < positions[j][1]:
                return False

            j += 1

        return True

    def canChange(self, start: str, target: str) -> bool:
        start_pos  = [(start[i], i) for i in range(len(start)) if start[i] != '_']
        target_pos = [(target[i], i) for i in range(len(target)) if target[i] != '_']
        
        if len(start_pos) != len(target_pos):
            return False
        
        for s, t in zip(start_pos, target_pos):
            if s[0] != t[0] or (t[0] == 'L' and s[1] < t[1]) or (t[0] == 'R' and s[1] > t[1]):
                return False
        
        return True