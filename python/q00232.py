"""
232. Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:
    `void push(int x)` Pushes element x to the back of the queue.
    `int pop()` Removes the element from the front of the queue and returns it.
    `int peek()` Returns the element at the front of the queue.
    `boolean empty()` Returns true if the queue is empty, false otherwise.

Notes:
    You must use only standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""

class MyQueue:
    def __init__(self):
        """
        Use two stacks: one to store the queue in forward order and another to
        store reversed. Only one stack will be populated at any time; items
        will "slosh" back and forth between them like pouring water between two
        cups. This implementation performs best when the same operation is
        performed many times in a row.
        """
        self.sfor = []
        self.srev = []

    def push(self, x: int) -> None:
        """
        O(n) worst case but, if the last operation performed was also a push(),
        becomes ~O(1) not accounting for python list resizing
        """
        while self.srev:
            self.sfor.append(self.srev.pop())
        self.sfor.append(x)

    def pop(self) -> int:
        """
        O(n) worst case but, if the last operation performed was also a pop(),
        becomes O(1)
        """
        while self.sfor:
            self.srev.append(self.sfor.pop())
        return self.srev.pop()

    def peek(self) -> int:
        if self.sfor:
            return self.sfor[0]
        elif self.srev:
            return self.srev[-1]
        else:
            raise ValueError("cannot peek empty queue")

    def empty(self) -> bool:
        return not (self.sfor or self.srev)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()