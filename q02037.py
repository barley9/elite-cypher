"""
2037. Minimum Number of Moves to Seat Everyone

There are `n` seats and `n` students in a room. You are given an array `seats` of length `n`, where `seats[i]` is the position of the `i`th seat. You are also given the array `students` of length `n`, where `students[j]` is the position of the `j`th student.

You may perform the following move any number of times:
    Increase or decrease the position of the `i`th student by `1` (i.e., moving the `i`th student from position `x` to `x + 1` or `x - 1`)

Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """O(2 * n log n) time, O(n) space one-liner solution"""
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))