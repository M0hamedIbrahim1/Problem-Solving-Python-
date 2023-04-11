# link   : https://leetcode.com/problems/factorial-trailing-zeroes/
# author : Mohamed Ibrahim


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n // 5
            res += n
        return res
      
