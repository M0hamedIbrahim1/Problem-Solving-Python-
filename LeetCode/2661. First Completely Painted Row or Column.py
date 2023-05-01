# link   : https://leetcode.com/problems/first-completely-painted-row-or-column/description/
# author : Mohmaed Ibrahim

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n,m = len(mat),len(mat[0])
        rows = [0]*n
        cols = [0]*m
        d = {}
        for i in range(n):
            for j in range(m):
                d[mat[i][j]] = [i , j]
        for i in range(len(arr)):
            r,c = d[arr[i]]
            rows[r]+=1
            cols[c]+=1
            if rows[r] == m or cols[c] == n:
                return i
        return -1
