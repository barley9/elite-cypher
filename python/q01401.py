"""
1401. Circle and Rectangle Overlapping

You are given a circle represented as `(radius, xCenter, yCenter)` and an axis-
aligned rectangle represented as `(x1, y1, x2, y2)`, where `(x1, y1)` are the
coordinates of the bottom-left corner, and `(x2, y2)` are the coordinates of
the top-right corner of the rectangle.

Return `true` if the circle and rectangle are overlapped otherwise return
`false`. In other words, check if there is any point `(xi, yi)` that belongs to
the circle and the rectangle at the same time.
"""

class Solution:
    @staticmethod
    def circle_point_overlap(
        cx: float, cy: float, cr: float,
        px: float, py: float
    ) -> bool:
        return (cx - px)*(cx - px) + (cy - py)*(cy - py) <= (cr * cr)

    @staticmethod
    def rectangle_point_overlap(
        rx1: float, ry1: float, rx2: float, ry2: float,
        px: float, py: float
    ) -> bool:
        return (rx1 <= px <= rx2) and (ry1 <= py <= ry2)
        
    def checkOverlap(self,
        radius: int, xCenter: int, yCenter: int,
        x1: int, y1: int, x2: int, y2: int
    ) -> bool:
        if Solution.rectangle_point_overlap(
            x1 - radius, y1 - radius, x2 + radius, y2 + radius,
            xCenter, yCenter
        ):
            if (x1 <= xCenter <= x2) or (y1 <= yCenter <= y2):
                return True
            else:
                for px, py in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                    if Solution.circle_point_overlap(xCenter, yCenter, radius, px, py):
                        return True
                return False
        else:
            return False

    def checkOverlap(self,
        radius: int, xCenter: int, yCenter: int,
        x1: int, y1: int, x2: int, y2: int
    ) -> bool:
        """O(1) time, O(1) space solution"""
        # Check if circle overlaps "inflated" rectangle
        if (x1 - radius <= xCenter <= x2 + radius) and (y1 - radius <= yCenter <= y2 + radius):
            # Check if circle is NOT in corner regions
            if (x1 <= xCenter <= x2) or (y1 <= yCenter <= y2):
                return True 
            else:
                # Check if circle overlaps any rectangle corner points
                r2 = radius * radius
                return (xCenter - x1)*(xCenter - x1) + (yCenter - y1)*(yCenter - y1) <= r2 or \
                       (xCenter - x1)*(xCenter - x1) + (yCenter - y2)*(yCenter - y2) <= r2 or \
                       (xCenter - x2)*(xCenter - x2) + (yCenter - y1)*(yCenter - y1) <= r2 or \
                       (xCenter - x2)*(xCenter - x2) + (yCenter - y2)*(yCenter - y2) <= r2
        else:
            return False