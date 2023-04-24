# link   : https://leetcode.com/problems/diagonal-traverse/description/
# author : Mohamed Ibrahim 

class Solution:
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []
        d = defaultdict(list)
        N, M = len(matrix), len(matrix[0])
        for i in range(N):
            for j in range(M):
                d[i+j].append(matrix[i][j])
        res = []
        for i in range(len(d)):
            if i % 2 == 0:
                d[i] = d[i][::-1]
            res.extend(d[i])
        return res
      
