# link   : https://leetcode.com/problems/pascals-triangle/description/
# author : Mohamed Ibrahim



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [1]*numRows
        for i in range(numRows):
            lst[i] = [1]*(i+1)

            for j in range(1,i):
                lst[i][j] = lst[i-1][j-1]+lst[i-1][j]
        return lst
        
        
