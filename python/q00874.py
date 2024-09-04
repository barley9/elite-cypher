"""
874. Walking Robot Simulation

A robot on an infinite XY-plane starts at point `(0, 0)` facing north. The robot
can receive a sequence of these three possible types of `commands`:
    `-2`: Turn left `90` degrees.
    `-1`: Turn right `90` degrees.
    `1 <= k <= 9`: Move forward `k` units, one unit at a time.

Some of the grid squares are `obstacles`. The `i`th obstacle is at grid point
`obstacles[i] = (xi, yi)`. If the robot runs into an obstacle, then it will
instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin
squared (i.e. if the distance is `5`, return `25`).

Note:
    North means +Y direction.
    East means +X direction.
    South means -Y direction.
    West means -X direction.
    There can be obstacle in [0,0].
"""

import numpy as np

class Solution:
    mat_left  = np.array([[0, -1], [ 1, 0]])
    mat_right = np.array([[0,  1], [-1, 0]])

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = np.array([0, 0])
        vel = np.array([0, 1])
        obstacles = set(tuple(item) for item in obstacles)
        maxdist = 0

        for c in commands:
            if c > 0:
                for _ in range(c):
                    if tuple(pos + vel) in obstacles:
                        break
                    else:
                        pos += vel
            else:
                if c == -1:
                    vel = self.mat_right.dot(vel)
                else:
                    vel = self.mat_left.dot(vel)
        
            if np.sum(pos ** 2) > maxdist:
                maxdist = np.sum(pos ** 2)

        return maxdist