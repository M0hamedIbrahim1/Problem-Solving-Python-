# link   : https://leetcode.com/problems/insert-interval/description/
# author : Mohamed Ibrahim

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            n_x , n_y = newInterval
            
            if n_y < intervals[i][0]:
                res.append([n_x , n_y])
                return res + intervals[i:]
            elif n_x > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(n_x , intervals[i][0]) , max(n_y , intervals[i][1])]
                
        res.append(newInterval)
        return res
      
