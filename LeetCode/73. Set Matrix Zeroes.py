# link : https://leetcode.com/problems/set-matrix-zeroes/
# author : Mohamed Ibrahim


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows , cols = len(matrix),len(matrix[0])
        s = set()
        
        def func(i,j):
            for r in range(rows):
                matrix[r][j] = 0
            for c in range(cols):
                matrix[i][c] = 0    
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0 :
                    s.add((i,j))
                    

        for i in range(rows):
            for j in range(cols):
                if (i,j) in s:
                    func(i,j)
                        
