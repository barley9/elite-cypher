"""
717. 1-bit and 2-bit Characters

We have two special characters:
    The first character can be represented by one bit `0`.
    The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last
character must be a one-bit character.
"""

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        O(n) time, O(n) space solution

        Strategy: Represent as two-state FSM
        """
        # States
        ZERO = 0
        ONE  = 1

        state = ZERO  # start in ZERO state
        decoded = []  # decoded characters
        for b in bits:
            if state == ZERO:
                if b == 0:
                    state = ZERO
                    decoded.append('a')
                else:
                    state = ONE
            elif state == ONE:
                if b == 0:
                    state = ZERO
                    decoded.append('b')
                else:
                    state = ZERO
                    decoded.append('c')

        # print(decoded)
        
        return decoded[-1] == 'a'

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        O(n) time, O(1) space solution
        
        optimized version of above strategy
        """
        state = 0
        for i in range(len(bits)):
            if state:
                state = 0
            else:
                if bits[i]:
                    state = 1
                elif i == len(bits) - 1:
                    return True
        return False