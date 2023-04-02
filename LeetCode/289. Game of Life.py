# link   : https://leetcode.com/problems/game-of-life/description/
# author : Mohmaed ibrahim


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import copy
        n = len(board)
        m = len(board[0])
        ans = copy.deepcopy(board)

        directions = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        for i in range(n):
            for j in range(m):
                
                zero , ones = 0,0
                for d in directions:
                    x = d[0] + i
                    y = d[1] + j

                    if 0 <= x < n and 0 <= y < m  :
                        if ans[x][y]:ones+=1
                        else:zero+=1
                if ans[i][j]==1 and (ones<2 or ones>3):
                    board[i][j]=0
                if ans[i][j]==1 and (ones==2 or ones==3):
                    board[i][j]=1
                if ans[i][j]==0 and (ones==3):
                    board[i][j]=1
                    
