"""
2999. Count the Number of Powerful Integers

You are given three integers `start`, `finish`, and `limit`. You are also
given a 0-indexed string `s` representing a positive integer.

A positive integer `x` is called powerful if it ends with `s` (in other words,
`s` is a suffix of `x`) and each digit in `x` is at most `limit`.

Return the total number of powerful integers in the range `[start...finish]`.

A string `x` is a suffix of a string `y` if and only if `x` is a substring of
`y` that starts from some index (including 0) in `y` and extends to the index
`y.length - 1`. For example, `25` is a suffix of `5125` whereas `512` is not.
"""

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        """Annoying case-hunting problem"""
        ord0 = ord('0')  # we'll use this in a loop, so store an alias for faster execution

        # Strip off prefixes
        start_pref, finish_pref = list(str(start)[:-len(s)]), list(str(finish)[:-len(s)])
        
        if len(start_pref) == 0:
            start_pref = 0
        else:
            # Loop over digits in the prefix of `start`. If an invalid digit
            # is encountered (i.e. a digit that is greater than `limit`),
            # overwrite the previous digit with `limit` and the rest of the
            # prefix with zeros. That is, 'round' up to smallest valid integer.
            i = len(start_pref)  # infinity
            for i in range(len(start_pref)):
                print('\t', ord(start_pref[i]) - ord0)
                if ord(start_pref[i]) - ord0 > limit:
                    break
            print('start_pref: "' + ''.join(start_pref[:i - 1]) + chr(limit + ord0) + '0' * (len(start_pref) - i) + '"')
            start_pref = int(
                ''.join(start_pref[:i - 1]) + chr(limit + ord0) + '0' * (len(start_pref) - i),
                base=limit + 1
            )

        if len(finish_pref) == 0:
            if finish < int(s):
                return 0
            else:
                finish_pref = 1
        else:
            # Loop over digits in the prefix of `finish`. If an invalid digit is
            # encountered (i.e. a digit greater than `limit`), overwrite the rest
            # of the digits in `finish_pref` with `str(limit)`. That is, 'round'
            # down to largest valid integer.
            i = len(finish_pref)
            valid = True
            for i in range(len(finish_pref)):
                print('\t', ord(finish_pref[i]) - ord0)
                if ord(finish_pref[i]) - ord0 > limit:
                    valid = False
                    break
            print('finish_pref: "' + ''.join(finish_pref[:i]) + chr(limit + ord0) * (len(finish_pref) - i) + '"')
            if valid:
                finish_pref = int(''.join(finish_pref))
            else:
                finish_pref = int(
                    ''.join(finish_pref[:i]) + chr(limit + ord0) * (len(finish_pref) - i),
                    base=limit + 1
                )
        
        print(start_pref, finish_pref)

        return finish_pref - start_pref + 1