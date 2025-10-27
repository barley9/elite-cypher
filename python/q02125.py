"""
2125. Number of Laser Beams in a Bank

Anti-theft security devices are activated inside a bank. You are given a
0-indexed binary string array `bank` representing the floor plan of the bank,
which is an `m x n` 2D matrix. `bank[i]` represents the `i`th row, consisting
of '0's and '1's. '0' means the cell is empty, while '1' means the cell has a
security device.

There is one laser beam between any two security devices if both conditions are
met:
    The two devices are located on two different rows: `r1` and `r2`, where
        `r1 < r2`.
    For each row `i` where `r1 < i < r2`, there are no security devices in the
        `i`th row.

Laser beams are independent, i.e., one beam does not interfere nor join with
another.

Return the total number of laser beams in the bank.
"""

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """O(m * n) time, O(1) space solution"""
        # Remove any empty rows
        for row in range(len(bank) - 1, -1, -1):
            if bank[row].count('1') == 0:
                del bank[row]
        
        # Count lasers
        total_lasers = 0
        for row in range(len(bank) - 1):
            total_lasers += bank[row].count('1') * bank[row + 1].count('1')
        
        return total_lasers

    def numberOfBeams(self, bank: List[str]) -> int:
        """O(m * n) time, O(m) space solution"""
        # Pre-compute counts
        counts = [bank[row].count('1') for row in range(len(bank))]

        i, j, total = 0, 1, 0
        while j < len(bank):
            if counts[j] > 0:
                total += counts[i] * counts[j]
                i += 1
                j = i
            j += 1

        return total

    def numberOfBeams(self, bank: List[str]) -> int:
        """O(m * n) time, O(1) space solution"""
        total_lasers = 0
        prev_devices = bank[0].count('1')
        for row in range(1, len(bank)):
            curr_devices = bank[row].count('1')
            if not curr_devices:
                continue
            total_lasers += prev_devices * curr_devices
            prev_devices = curr_devices
        return total_lasers