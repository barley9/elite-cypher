"""
1701. Average Waiting Time

There is a restaurant with a single chef. You are given an array `customers`,
where `customers[i] = [arrivali, timei]`:
    * `arrival_i` is the arrival time of the `i`th customer. The arrival times
        are sorted in non-decreasing order.
    * `time_i` is the time needed to prepare the order of the `i`th customer.

When a customer arrives, he gives the chef his order, and the chef starts
preparing it once he is idle. The customer waits till the chef finishes
preparing his order. The chef does not prepare food for more than one customer
at a time. The chef prepares food for customers in the order they were given in
the input.

Return the average waiting time of all customers. Solutions within `10^{-5}`
from the actual answer are considered accepted.
"""

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """O(n) time, O(1) space solution"""
        next_idle = customers[0][0]
        total_wait = 0
        for arrive, time in customers:
            if next_idle < arrive:
                total_wait += time
                next_idle = arrive + time
            else:
                total_wait += time + (next_idle - arrive)
                next_idle += time
        return total_wait / len(customers)
            