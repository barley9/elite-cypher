"""
739. Daily Temperatures

Given an array of integers `temperatures` represents the daily temperatures,
return an array `answer` such that `answer[i]` is the number of days you have
to wait after the `i`th day to get a warmer temperature. If there is no future
day for which this is possible, keep `answer[i] == 0` instead.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Naive O(n^2) solution; too slow"""
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break
        
        return answer

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """I think this is O(n), but still too slow"""
        answer = [0] * len(temperatures)
        tracking = [0]  # indices to track
        for j in range(1, len(temperatures)):
            for i in range(len(tracking) - 1, -1, -1):
                if temperatures[j] > temperatures[tracking[i]]:
                    answer[tracking[i]] = j - tracking[i]
                    del tracking[i]
            tracking.append(j)
        
        return answer