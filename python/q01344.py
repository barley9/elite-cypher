"""
1344. Angle Between Hands of a Clock

Given two numbers, `hour` and `minutes`, return the smaller angle (in degrees)
formed between the hour and the minute hand.

Answers within `10^-5` of the actual value will be accepted as correct.
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """O(1) time, O(1) space solution"""
        t = hour + (minutes / 60)  # elapsed time
        theta_m = (360 * t) / 1  # angle of minute hand
        theta_h = (360 * t) / 12  # angle of hour hand
        dtheta = (theta_m - theta_h) % 360
        return min(dtheta, 360 - dtheta)

    def angleClock(self, hour: int, minutes: int) -> float:
        dt = (360 * (1/12 - 1) * (hour + minutes / 60)) % 360
        return min(dt, 360 - dt)