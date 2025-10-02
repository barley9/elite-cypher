"""
1518. Water Bottles

There are `numBottles` water bottles that are initially full of water. You can
exchange `numExchange` empty water bottles from the market with one full water
bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers `numBottles` and `numExchange`, return the maximum
number of water bottles you can drink.
"""

import math

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """O(log_numExchange(numBottles)) time, O(1) space solution"""
        total = 0
        numEmpty = 0
        while numBottles > 0:
            # Drink
            total += numBottles
            numEmpty += numBottles
            numBottles = 0

            # Exchange
            numBottles, numEmpty = divmod(numEmpty, numExchange)
        
        return total

    # def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    #     return math.log(numBottles, numExchange)