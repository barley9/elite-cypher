"""
401. Binary Watch

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs
on the bottom to represent the minutes (0-59). Each LED represents a zero or
one, with the least significant bit on the right.

[The watch face looks like this when off:
+---------------------+
| H  8  4  2  1   PM  |
| M  32  16  8  2  1  |
+---------------------+]

For example, the below binary watch reads "4:51 PM":
+---------------------+
| H  8 {4} 2  1  {PM} |
| M {32}{16} 8 {2}{1} |
+---------------------+
[Numbers surrounded by curly braces are illuminated.]

Given an integer `turnedOn` which represents the number of LEDs that are
currently on (ignoring the PM), return all possible times the watch could
represent. You may return the answer in any order.

The hour must not contain a leading zero. For example, "01:00" is not valid.
It should be "1:00".

The minute must consist of two digits and may contain a leading zero. For
example, "10:2" is not valid. It should be "10:02".
"""


import itertools

class Solution:
    LED_COUNT = 4 + 6

    def bin_sequence_to_time(self, sequence: tuple[int]) -> str:
        """O(len(sequence)) time, O(1) space helper function"""
        assert len(sequence) == self.LED_COUNT

        hour   = int(''.join(sequence[:4]), 2)
        minute = int(''.join(sequence[4:]), 2)

        if (0 <= hour < 12) and (0 <= minute < 60):
            return f"{hour}:{minute:0>2}"
        else:
            return ""

    def readBinaryWatch(self, num_lit: int) -> List[str]:
        """O(n!) time, O(n!) space solution"""
        seqs = set(itertools.permutations(
            '1' * num_lit + \
            '0' * (self.LED_COUNT - num_lit)
        ))

        return [
            str_time
            for str_time in map(
                self.bin_sequence_to_time,
                seqs
            )
            if str_time
        ]