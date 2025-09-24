"""
166. Fraction to Recurring Decimal

Given two integers representing the `numerator` and `denominator` of a
fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than `10^4` for
all the given inputs.
"""

class Solution:
    ord0 = ord('0')

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        O(??) time, O(??) space solution

        (I have no idea how the length of the decimal expansion of a rational
        number depends on its numerator and denominator)
        """
        neg_flag = ((numerator < 0) ^ (denominator < 0)) & (numerator != 0)
        n, d = abs(numerator), abs(denominator)
        
        seen = {}
        paren_idx = None
        digits = []
        for i in range(10 ** 4):  # output is guaranteed less than 10^4
            q, r = divmod(n, d)
            if (q, r) in seen:
                paren_idx = seen[(q, r)]  # we found a cycle
                break
            digits.append(q)
            if r == 0:
                break  # the decimal expansion terminated
            
            # Store indices of previously encountered (quotient, remainder)
            if i > 0:
                seen[(q, r)] = i  # do not count whole part when finding cycle
            
            n = 10 * r

        # print(seen)
        # print(digits)

        result = ('-' if neg_flag else '') + \
                 str(digits[0]) + \
                 ('.' if len(digits) > 1 else '')
        if paren_idx is None:
            result += ''.join(chr(digit + self.ord0) for digit in digits[1:])
        else:
            result += ''.join(chr(digit + self.ord0) for digit in digits[1:paren_idx]) + \
                      '(' + \
                      ''.join(chr(digit + self.ord0) for digit in digits[paren_idx:]) + \
                      ')'
        
        return result