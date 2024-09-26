"""
729. My Calendar I

You are implementing a program to use as your calendar. We can add a new event
if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection
(i.e., some moment is common to both events.).

The event can be represented as a pair of integers `start` and `end` that
represents a booking on the half-open interval `[start, end)`, the range of
real numbers `x` such that `start <= x < end`.

Implement the MyCalendar class:
    `MyCalendar()` Initializes the calendar object.
    `boolean book(int start, int end)` Returns `true` if the event can be added
        to the calendar successfully without causing a double booking.
        Otherwise, return `false` and do not add the event to the calendar.

"""

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        """O(n) time lookup"""
        for event in self.events:
            if (end > event[0]) and (event[1] > start):
                return False
        # TODO: add some optimization that combines events that abutt one another
        # TODO: actually, scratch that: use binary search instead
        self.events.append((start, end))
        return True