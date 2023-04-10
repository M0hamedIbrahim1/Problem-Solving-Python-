# link   : https://leetcode.com/problems/merge-intervals/description/
# author : Mohamed Ibrahim

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort() 
        pst_S , pst_E = intervals[0][0],intervals[0][1]
        ans = [[pst_S,pst_E]]
        for i in range(1,len(intervals)):
            start , end = intervals[i]
            if start <= pst_E and end >= pst_S:
                pst_E = max(pst_E,end)
                pst_S = min(pst_S,start)
                ans[-1][1] = pst_E
                ans[-1][0] = pst_S


            else:
                ans.append([start,end])
                pst_S,pst_E = start,end
        return ans
        
