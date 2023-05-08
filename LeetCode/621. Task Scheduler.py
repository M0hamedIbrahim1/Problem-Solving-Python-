# link   : https://leetcode.com/problems/task-scheduler/description/
# author : Mohamed Ibrahim

class Solution:
    def leastInterval(self, tasks, N):
        task_counts = list(collections.Counter(tasks).values())
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)
