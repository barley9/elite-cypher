"""
2429. Minimize XOR

Given two positive integers `num1` and `num2`, find the positive integer `x`
        such that:
    `x` has the same number of set bits as `num2`, and
    The value `x XOR num1` is minimal.

Note that XOR is the bitwise XOR operation.

Return the integer `x`. The test cases are generated such that `x` is uniquely
determined.

The number of set bits of an integer is the number of `1`'s in its binary
representation.
"""

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        print(f"{num1:08b}", f"{num2:08b}", end=' ')
        x = 0
        bits = num2.bit_count()  # number of bits of `x` we are allowed to set
        # We want `x ^ num1` to be minimal, so use available bits zero out MSBs of `num1`
        for i in range(num1.bit_length() - 1, -1, -1):
            if ((1 << i) & num1):
                x |= 1 << i
                bits -= 1
                if bits <= 0:
                    break
            i -= 1
        
        # If we haven't set enough bits, start setting LSBs in `x` until we run out
        i = 0
        while bits > 0:
            if ~x & (1 << i):
                x |= 1 << i
                bits -= 1
            i += 1

        print(f"{x:08b}")
        return x

    def minimizeXor(self, num1: int, num2: int) -> int:
        """O(log(num1) + log(num2)) time, O(1) space solution"""
        # print(f"{num1:08b}", f"{num2:08b}")
        x = 0
        bits = num2.bit_count()
        msb = num1.bit_length() - 1
        for i in range(max(bits, msb), -1, -1):
            # Set bit if
            #   EITHER the corresponding bit of `num1` is set,
            #   OR if we would have too many bits to pack into the remaining positions
            if (1 << i) & num1 or i < bits:
                x |= 1 << i
                bits -= 1
                if bits <= 0:  # if we've run out of bits, exit
                    break
        
            # print(f"{x:08b}")
        return x