"""
539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum
minutes difference between any two time-points in the list. 
"""

class Solution:
    @staticmethod
    def hhmm_to_min(time_hhmm: str) -> int:
        return 60 * int(time_hhmm[:2]) + int(time_hhmm[3:])

    def findMinDifference(self, timePoints: List[str]) -> int:
        """O(n ** 2) time, O(1) space solution. (TOO SLOW)"""
        period = 24 * 60
        min_diff = 10 ** 7  # infinity
        for i in range(len(timePoints) - 1):
            mi = self.hhmm_to_min(timePoints[i])
            for j in range(i + 1, len(timePoints)):
                mj = self.hhmm_to_min(timePoints[j])
                diff = min(
                    (mi - mj + period) % period,
                    (mj - mi + period) % period,
                )
                if diff < min_diff:
                    min_diff = diff
        return min_diff

    def findMinDifference(self, timePoints: List[str]) -> int:
        time_points = [60 * int(t[:2]) + int(t[3:]) for t in timePoints]
        period = 24 * 60
        min_diff = 10 ** 7  # infinity
        for i in range(len(time_points) - 1):
            for j in range(i + 1, len(time_points)):
                diff = min(
                    (time_points[i] - time_points[j] + period) % period,
                    (time_points[j] - time_points[i] + period) % period,
                )
                if diff < min_diff:
                    min_diff = diff
        return min_diff

    def findMinDifference(self, timePoints: List[str]) -> int:
        """O(n log n) time, O(n) space solution by pre-sorting input"""
        period = 24 * 60
        if len(timePoints) >= period:
            return 0  # by the pigeonhole principle
        
        time_points = sorted(60 * int(t[:2]) + int(t[3:]) for t in timePoints)
        min_diff = 10 ** 7  # infinity
        for i in range(-1, len(time_points) - 1):
            diff = min(
                (time_points[i] - time_points[i + 1] + period) % period,
                (time_points[i + 1] - time_points[i] + period) % period,
            )
            if diff < min_diff:
                min_diff = diff
        return min_diff


# You know the drill; beats 100.00%
def findMinDifference(timePoints):
    period,min_diff=1440,1440
    if len(timePoints)>=period:return 0
    time_points=sorted(60*int(t[:2])+int(t[3:]) for t in timePoints)
    for i in range(-1,len(time_points)-1):
        diff=min((time_points[i]-time_points[i+1]+period)%period,(time_points[i+1]-time_points[i]+period)%period)
        if diff<min_diff:min_diff=diff
    return min_diff
results = []
while 1:
    try:results.append(findMinDifference(loads(next(sys.stdin))))
    except StopIteration:break
with open("user.out","w") as f:print(str(results)[1:-1].replace(", ","\n"),file=f)
sys.exit(0)