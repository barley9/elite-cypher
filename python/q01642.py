"""
1642. Furthest Building You Can Reach

You are given an integer array `heights` representing the heights of buildings,
some `bricks`, and some `ladders`.

You start your journey from building `0` and move to the next building by
possibly using bricks or ladders.

While moving from building `i` to building `i+1` (0-indexed),

    If the current building's height is greater than or equal to the next
    building's height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height,
    you can either use one ladder or `h[i+1] - h[i]` bricks.

Return the furthest building index (0-indexed) you can reach if you use the
given ladders and bricks optimally.
"""

import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) < 2:
            return len(heights) - 1

        cost_heap = []  # maxheap to store brick costs

        for i in range(len(heights) - 1):
            print(i)
            if heights[i + 1] > heights[i]:  # only jumps cost resources; falls are free!
                diff = heights[i + 1] - heights[i]
                heapq.heappush(cost_heap, -diff)  # heapq implements minheap, so invert value
                bricks -= diff
                print(f'\tdiff: {diff}')
                if bricks >= 0:
                    print(f'\tused {diff} bricks; {bricks} bricks remaining')
                else:
                    print('\tinsufficient bricks...')
                    if ladders > 0:
                        maxjump = -heapq.heappop(cost_heap)  # heapq implements minheap, so invert value
                        bricks += maxjump
                        ladders -= 1
                        print(f'\tused 1 ladder; refunded {maxjump} bricks; {ladders} ladders remaining')
                    else:
                        print('\tinsufficient ladders...')
                        break
        else:
            return i + 1
        
        return i

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        In the worst case for time-complexity `heights` is strictly increasing
        and we have only ladders and no bricks. So, each loop we push onto heap
        and pop from heap. Both of these are `O(log n)` time, so in total this
        solution is `O(n log n)` time.
        In the worst case for space-complexity `heights` is strictly increasing
        and we have unlimited bricks. So, we store `n - 1` jumps onto the heap
        requiring `O(n)` extra space.
        """
        if len(heights) < 2:
            return len(heights) - 1

        cost_heap = []  # maxheap to store brick costs

        for i in range(len(heights) - 1):
            if heights[i + 1] > heights[i]:  # only jumps cost resources; falls are free!
                diff = heights[i + 1] - heights[i]
                heapq.heappush(cost_heap, -diff)  # heapq implements minheap, so invert value
                bricks -= diff
                if bricks < 0:  # if we don't have enough bricks, try using ladders
                    if ladders > 0:
                        maxjump = -heapq.heappop(cost_heap)  # heapq implements minheap, so invert value
                        bricks += maxjump  # refund bricks replaced by ladder
                        ladders -= 1
                    else:
                        break  # we're out of resources
        else:
            return i + 1  # we made it to the last building
        
        return i  # we ran out of resources at some point