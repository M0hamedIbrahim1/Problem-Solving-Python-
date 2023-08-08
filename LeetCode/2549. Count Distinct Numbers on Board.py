# link   : https://leetcode.com/problems/count-distinct-numbers-on-board/description/
# author : Mohamed Ibrahim

class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n-1 if n > 1 else 1
