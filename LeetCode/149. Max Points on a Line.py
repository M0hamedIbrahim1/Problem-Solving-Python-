# link   : https://leetcode.com/problems/max-points-on-a-line/description/
# author : Mohamed Ibrahim


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            Dict = collections.defaultdict(int)
            for j in range(i+1 , len(points)):
                if points[i][0] == points[j][0]:
                    slope = float('inf')
                else:
                    slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                Dict[slope]+=1
                res = max(res , Dict[slope])
        return res+1
      
