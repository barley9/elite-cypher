"""
670. Maximum Swap

You are given an integer `num`. You can swap two digits at most once to get the
maximum valued number.

Return the maximum valued number you can get.
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        """INCORRECT"""
        # Sort list of digits in descending and reconstruct integer
        ord0 = ord('0')
        return sum(
            d * 10 ** k
            for k, d in enumerate(sorted(
                ord(d) - ord0
                for d in str(num)
            ))
        )

    def maximumSwap(self, num: int) -> int:
        """INCORRECT"""
        # Split `nums` into list of digits
        ord0 = ord('0')
        digits = [ord(d) - ord0 for d in reversed(str(num))]

        # Find largest digit
        argmax = 0
        for i in range(len(digits)):
            if digits[i] > digits[argmax]:
                argmax = i

        # Swap so that largest digit is in highest place value
        swap = digits[argmax]
        digits[argmax] = digits[-1]
        digits[-1] = swap

        # Re-construct integer and return
        return sum(d * 10 ** k for k, d in enumerate(digits))

    def maximumSwap(self, num: int) -> int:
        """INCORRECT"""
        # Split `nums` into list of digits
        ord0 = ord('0')
        digits = [ord(d) - ord0 for d in reversed(str(num))]

        for start in range(len(digits) - 1, 0, -1):
            # Find largest digit
            argmax = start
            for i in range(start, -1, -1):
                if digits[i] > digits[argmax]:
                    argmax = i

            print(digits, start, argmax)

            if argmax != start:
                # Swap so that largest digit is in highest place value
                swap = digits[argmax]
                digits[argmax] = digits[start]
                digits[start] = swap
                break
            else:
                # Restart but skip first digit because it's already largest
                start -= 1

        # Re-construct integer and return
        return sum(d * 10 ** k for k, d in enumerate(digits))

    def maximumSwap(self, num: int) -> int:
        """
        INCORRECT
        Fails for `num = 1993` -> 9913; instead outputs 9193 (WRONG)
        """
        digits = sorted(
            (list(elem) for elem in enumerate(reversed(str(num)))),
            key=lambda elem: elem[1],
        )
        
        for i in range(len(digits) - 1, -1, -1):
            # If digit is not in the position that would maximize result...
            if digits[i][0] != i:
                # ...locate digit currently occupying place value...
                for j in range(i - 1, -1, -1):
                    if digits[j][0] == i:
                        # ...and swap the two digits' place values
                        digits[i][0], digits[j][0] = digits[j][0], digits[i][0]
                        break
                break

        # Reconstruct resulting integer from list of digits
        return int(''.join(
            elem[1]
            for elem in sorted(
                digits,
                key=lambda elem: elem[0],
                reverse=True,
            )
        ))