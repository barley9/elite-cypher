"""
1578. Minimum Time to Make Rope Colorful

Alice has `n` balloons arranged on a rope. You are given a 0-indexed string
`colors` where `colors[i]` is the color of the `i`th balloon.

Alice wants the rope to be colorful. She does not want two consecutive
balloons to be of the same color, so she asks Bob for help. Bob can remove
some balloons from the rope to make it colorful. You are given a 0-indexed
integer array `neededTime` where `neededTime[i]` is the time (in seconds) that
Bob needs to remove the `i`th balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
"""

# Cheating by modifying results to display 0ms runtime:
# __import__('atexit').register(lambda:open("display_runtime.txt","w").write("0"))


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        O(n) time, O(n) space solution

        Find runs of colors. Within each run, find the highest cost balloon.
        Remove all others in run and add their times to `total_cost`. This
        will guarantee that no consecutive balloons share the same color and
        only the minimum amount of time-cost is incurred to satisfy this
        condition.
        """
        runs = []  # list of runs, where each run is a list of time-costs
        run_color = ''
        for i in range(len(colors)):
            if colors[i] == run_color:
                runs[-1].append(neededTime[i])
            else:
                runs.append([neededTime[i]])
                run_color = colors[i]
        
        total_cost = 0
        for run in runs:
            if len(run) < 2:  # no cost for runs containing one balloon
                continue
            total_cost += sum(run) - max(run)  # remove all but most costly
        
        return total_cost

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """O(n) time, O(1) solution"""
        total_cost = 0

        run_color = ''
        run_length = 1
        run_total_cost = 0
        run_max_cost = 0
        for i in range(len(colors)):
            if colors[i] == run_color:
                run_length += 1
                run_total_cost += neededTime[i]
                if neededTime[i] > run_max_cost:
                    run_max_cost = neededTime[i]
            else:
                if run_length > 1:  # no cost for runs with single balloon
                    total_cost += run_total_cost - run_max_cost
                run_color = colors[i]
                run_length = 1
                run_total_cost = neededTime[i]
                run_max_cost = neededTime[i]
        if run_length > 1:
            total_cost += run_total_cost - run_max_cost
        
        return total_cost