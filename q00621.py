"""
621. Task Scheduler

You are given an array of CPU `tasks`, each represented by letters A to Z, and
a cooling time, `n`. Each cycle or interval allows the completion of one task.
Tasks can be completed in any order, but there's a constraint: identical tasks
must be separated by at least `n` intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.
"""

import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """INCORRECT"""
        counts = collections.Counter(tasks)
        if len(counts) > n:
            return counts.total()
        
        mode = counts.most_common(1)[0]
        num_modes = sum(item[1] == mode[1] for item in counts.items())
        
        return (mode[1] - 1) * (n + 1) + num_modes

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """INCORRECT"""
        # Get list of [task, frequency] in descending order of frequency
        counts = [list(item) for item in reversed(collections.Counter(tasks).most_common())]
        last_seen = {item[0] : 10 ** 7 for item in counts}

        result = 0
        i = len(counts) - 1
        while counts:
            count = counts[i % len(counts)]
            # print(i, count, last_seen)
            if last_seen[count[0]] - i > n:
                sequence.append(count[0])
                last_seen[count[0]] = i
                count[1] -= 1
                if count[1] <= 0:
                    del counts[i % len(counts)]
            result += 1
            i -= 1
            
        return result

def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get list of [task, frequency] in descending order of frequency
        counts = [list(item) for item in reversed(collections.Counter(tasks).most_common())]
        last_seen = {item[0] : 10 ** 7 for item in counts}

        sequence = []

        result = 0
        i = len(counts) - 1
        while counts:
            count = counts[i % len(counts)]
            print(i, count, last_seen)
            if last_seen[count[0]] - i > n:
                sequence.append(count[0])
                last_seen[count[0]] = i
                count[1] -= 1
                if count[1] <= 0:
                    del counts[i % len(counts)]
            else:
                sequence.append('idle')
            result += 1
            i -= 1

        print(sequence)
            
        return result
