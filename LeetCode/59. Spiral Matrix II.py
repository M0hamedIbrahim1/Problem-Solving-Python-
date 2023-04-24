# Link    : https://leetcode.com/problems/spiral-matrix-ii/solutions/
# author : Mohamed Ibrahim

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [ [0]*n for i in range(n)]

        top , bottom = 0 , len(A)
        left , right = 0 , len(A[0])
        
        res,cnt = [],1
        while left < right and top < bottom:
            
            for i in range(left , right):
                A[top][i] = cnt
                cnt+=1
                
            top+=1
            for i in range(top , bottom):
                A[i][right-1] = cnt
                cnt+=1          
            right-=1

            if not(left < right and top < bottom):break
            
            for i in range(right-1 , left-1 , -1):
                A[bottom-1][i] = cnt
                cnt+=1
            bottom-=1
            for i in range(bottom-1 , top -1,-1):
                A[i][left] = cnt
                cnt+=1
            left+=1
        return A
      
