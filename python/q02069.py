"""
2069. Walking Robot Simulation II

A `width` x `height` grid is on an XY-plane with the bottom-left cell at
`(0, 0)` and the top-right cell at `(width - 1, height - 1)`. The grid is
aligned with the four cardinal directions ("North", "East", "South", and
"West"). A robot is initially at cell `(0, 0)` facing direction "East".

The robot can be instructed to move for a specific number of steps. For each
step, it does the following.
    Attempts to move forward one cell in the direction it is facing.
    If the cell the robot is moving to is out of bounds, the robot instead
        turns 90 degrees counterclockwise and retries the step.

After the robot finishes moving the number of steps required, it stops and
awaits the next instruction.

Implement the Robot class:
    `Robot(int width, int height)` Initializes the `width` x `height` grid
        with the robot at `(0, 0)` facing "East".
    `void step(int num)` Instructs the robot to move forward `num` steps.
    `int[] getPos()` Returns the current cell the robot is at, as an array of
        length 2, [x, y].
    `String getDir()` Returns the current direction of the robot, "North",
        "East", "South", or "West".
"""


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

class Robot:
    """TOO SLOW"""
    cardinal_lookup = {
        ( 0,  1): "North",
        ( 0, -1): "South",
        ( 1,  0): "East",
        (-1,  0): "West",
    }

    def __init__(self, width: int, height: int):
        self.grid = [width, height]
        self.pos = [0, 0]
        self.dir = [1, 0]

    def step(self, num: int) -> None:
        # print(f"step({num})")
        while num > 0:
            # Attempt to move to position...
            next_cell = [
                self.pos[0] + self.dir[0],
                self.pos[1] + self.dir[1]
            ]
            # print("\t", num, self.pos, self.dir, next_cell, self.getDir())
            
            # If candidate position is inside grid...
            if (0 <= next_cell[0] < self.grid[0]) and (0 <= next_cell[1] < self.grid[1]):
                self.pos[0] += self.dir[0]
                self.pos[1] += self.dir[1]
                num -= 1
            else:
                # Rotate counter-clockwise
                self.dir = [
                    -self.dir[1],
                    self.dir[0]
                ]
                # print("\tget rotated, idiot")

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.cardinal_lookup[tuple(self.dir)]


class Robot:
    """
    Attempt #2: Try to make multiple steps at once

    UNFINISHED
    """
    cardinal_lookup = {
        ( 0,  1): "North",
        ( 0, -1): "South",
        ( 1,  0): "East",
        (-1,  0): "West",
    }

    def __init__(self, width: int, height: int):
        self.grid = [width, height]
        self.pos = [0, 0]
        self.dir = [1, 0]

    def _rotate(self) -> None:
        self.dir = [
            -self.dir[1],
            self.dir[0]
        ]

    def step(self, num: int) -> None:
        # If on edge and moving clockwise... mod out perimeter of grid
        # If on edge and NOT moving clockwise...
        # If not on edge and can reach edge...
        # If not on edge and CAN'T reach edge...

        gx, gy = self.grid
        while num > 0:
            px, py = self.pos

            # If on edge...
            if (px == 0) or (px == gx - 1) or (py == 0) or (py == gy - 1):
                # If moving clockwise...
                if px == 0:
                    if py == 0:
                        pass
                    else:
                        pass
                else:
                    if py == 0:
                        pass
                    else:
                        pass


        print(f"step({num})")
        perimeter = 2 * (self.grid[0] - 1) + 2 * (self.grid[1] - 1)
        while num > 0:
            # If on edge, modulo out perimeter from `num`
            q, r = divmod(num, perimeter)
            if (q > 0) and \
                    (self.pos[0] == 0 or self.pos[0] == self.grid[0] - 1) and \
                    (self.pos[1] == 0 or self.pos[1] == self.grid[1] - 1):
                num = r
                continue
            
            # Candidate cell
            cell = [
                self.pos[0] + num * self.dir[0],
                self.pos[1] + num * self.dir[1]
            ]
            if (0 <= cell[0] < self.grid[0]) and (0 <= cell[1] < self.grid[1]):
                self.pos = cell
                num = 0
            else:
                if cell[0] >= self.grid[0]:
                    num -= self.grid[0] - self.pos[0]
                    self.pos[0] = self.grid[0]
                elif cell[0] < 0:
                    num -= self.pos[0]
                    self.pos[0] = 0
                elif cell[1] >= self.grid[1]:
                    num -= self.grid[1] - self.pos[1]
                    self.pos[1] = self.grid[1]
                elif cell[1] < 0:
                    num -= self.pos[1]
                    self.pos[1] = 0
                self._rotate()
            
            print("\t", num, self.pos, self.dir, self.getDir())

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.cardinal_lookup[tuple(self.dir)]