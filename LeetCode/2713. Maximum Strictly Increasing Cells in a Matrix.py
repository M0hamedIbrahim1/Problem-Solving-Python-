# link   : https://leetcode.com/contest/weekly-contest-347/problems/maximum-strictly-increasing-cells-in-a-matrix/
# author : Mohamed ibraihm

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n,m= len(mat),len(mat[0])
        d = defaultdict(list)
        rows = [0]*n
        cols = [0]*m
        for i in range(n):
            for j in range(m):
                d[mat[i][j]].append((i,j))
        for val in sorted(d):
            temp = []
            for r,c in d[val]:
                temp.append(max(rows[r],cols[c])+1)
            for pos , v in zip(d[val] , temp):
                i,j = pos
                rows[i] = max(rows[i] , v)
                cols[j] = max(cols[j] ,v)
        return max(rows+cols)
        
