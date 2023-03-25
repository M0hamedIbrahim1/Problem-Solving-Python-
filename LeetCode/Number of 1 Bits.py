# link   : https://leetcode.com/problems/number-of-1-bits/
# author : Mohamed Ibrahim


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n = n & n-1
            cnt+=1
        return cnt 
      
      
