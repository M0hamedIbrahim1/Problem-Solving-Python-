# link   : https://leetcode.com/problems/minimum-time-to-complete-all-tasks/description/
# author : Mohamed Ibrahim

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x:x[1])
        used = [0]*2008

        for start , end , dur in tasks:
            cur = sum(used[start : end+1])
            remain = dur - cur  
            if remain <= 0 :
                continue
            else:
                i = end 
                while remain:
                    if used[i]!=1:
                        used[i] = 1
                    else:
                        while used[i]==1:
                            i-=1
                        used[i] = 1
                    remain-=1
        return sum(used)
