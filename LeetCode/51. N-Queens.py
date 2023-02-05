# Link   : https://leetcode.com/problems/n-queens/description/
# author : Mohamed Ibrahim


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range(n)]  
        pov = set() 
        neg = set()
        col = set()
        res = []
        def backtrack(r):
            if r == n:
                res.append(["".join(i) for i in board])
            for c in range(n):
                if c in col or (r+c) in pov or (r-c) in neg :
                    continue
                
                col.add(c)
                pov.add(r+c)
                neg.add(r-c)
                board[r][c] = 'Q'
                backtrack(r+1)

                col.remove(c)
                pov.remove(r+c)
                neg.remove(r-c)
                board[r][c] = '.'
        backtrack(0)
        return res




      
