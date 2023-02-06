# link   : https://leetcode.com/problems/generate-parentheses/description/
# author : Mohamed Ibrahim


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def resc(s,left,right):
            if left == n and right == n:
                res.append(s)
            if left < n:
                resc(s+'(',left+1,right)
            if right < left:
                resc(s+')',left,right+1)
        resc(s = "",left = 0,right = 0)      
        return res
        
        
 using Backtracing : 
 
 class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s=[],left = 0,right = 0):
            if left == n and right == n:
                res.append("".join(s))
            if left < n:
                s.append('(')
                backtrack(s,left+1,right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(s,left,right+1)
                s.pop()
        backtrack() 
        return res
 
 
 
 
 
 
