"""
826. Most Profit Assigning Work

You have `n` jobs and `m` workers. You are given three arrays: `difficulty`,
`profit`, and `worker` where:
    `difficulty[i]` and `profit[i]` are the difficulty and the profit of the
        `i`th job, and
    `worker[j]` is the ability of `j`th worker (i.e., the `j`th worker can only
        complete a job with difficulty at most `worker[j]`).

Every worker can be assigned at most one job, but one job can be completed
multiple times.
    For example, if three workers attempt the same job that pays $1, then the
        total profit will be $3. If a worker cannot complete any job, their
        profit is $0.

Return the maximum profit we can achieve after assigning the workers to the
jobs.
"""

class Solution:
    def maxProfitAssignment(self,
            difficulty: List[int],
            profit: List[int],
            worker: List[int]) -> int:
        """
        O(m * n) time, O(1) space solution assuming `profit` is sorted
        (INCORRECT ASSUMPTION)
        """
        total_profit = 0
        for i in range(len(worker)):
            for j in range(len(difficulty) - 1, -1, -1):
                if difficulty[j] <= worker[i]:
                    total_profit += profit[j]
                    break
        return total_profit

    def maxProfitAssignment(self,
            difficulty: List[int],
            profit: List[int],
            worker: List[int]) -> int:
        """
        O(n log n + n * m) time, O(2 * n) space solution where m = len(worker)
        and n = len(profit) = len(difficulty)
        """
        tasks = sorted(
            zip(difficulty, profit),
            key=lambda task: task[1],
            reverse=True,
        )
        # print(tasks)
        total_profit = 0
        for w in worker:
            for i in range(len(tasks)):
                if tasks[i][0] <= w:
                    total_profit += tasks[i][1]
                    break
        return total_profit