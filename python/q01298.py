"""
1298. Maximum Candies You Can Get from Boxes

You have `n` boxes labeled from `0` to `n - 1`. You are given four arrays:
`status`, `candies`, `keys`, and `containedBoxes` where:
    `status[i]` is `1` if the `i`th box is open and `0` if the `i`th box is
        closed,
    `candies[i]` is the number of candies in the `i`th box,
    `keys[i]` is a list of the labels of the boxes you can open after opening
        the `i`th box.
    `containedBoxes[i]` is a list of the boxes you found inside the `i`th box.

You are given an integer array `initialBoxes` that contains the labels of the
boxes you initially have. You can take all the candies in any open box and you
can use the keys in it to open new boxes and you also can use the boxes you
find in it.

Return the maximum number of candies you can get following the rules above.
"""

import collections
import copy

class Solution:
    def maxCandies(self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:
        """O(n) time, O(n) space solution using double-ended queue"""
        total_candies = 0
        boxes = collections.deque(initialBoxes)
        was_locked = set()

        while boxes:
            box = boxes.popleft()
            
            # If box is locked, put back into queue and skip
            if not status[box]:
                if box in was_locked:  # box is still locked ==> we're stuck
                    break
                else:
                    was_locked.add(box)
                boxes.append(box)
                continue
            
            # Empty the candies from the box
            total_candies += candies[box]
            candies[box] = 0

            # Unlock all possible boxes
            for key in keys[box]:
                status[key] = 1
                if key in was_locked:
                    was_locked.remove(key)
            keys[box] = []

            # Add newly found boxes to queue
            boxes.extend(containedBoxes[box])
            containedBoxes[box] = []

        return total_candies