# link   : https://leetcode.com/problems/maximal-network-rank/description/
# author : Mohamed Ibrahim


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:    
        d, c, res = Counter(), Counter(), 0
        for i in roads:
            d[i[0]] += 1
            d[i[1]] += 1
            c[(i[0], i[1])] = True
        
        for i in range(0, n):
            for j in range(i+1, n):
                if c[(i,j)] or c[(j,i)]: curr = d[i] + d[j] - 1
                else: curr = d[i] + d[j]
                res = max(res, curr)              
        return res
