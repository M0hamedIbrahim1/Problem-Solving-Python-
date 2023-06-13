# link : https://leetcode.com/problems/equal-row-and-column-pairs
# author : Mohamed Ibrahim

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n  = len(grid)
        d = defaultdict(list)

        for i in range(n):
            for j in range(n):
                d[i].append(grid[j][i])
        
        cnt = 0
        for row in range(n):
            for col in d:
                if grid[row] == d[col]:cnt+=1 
        return cnt
