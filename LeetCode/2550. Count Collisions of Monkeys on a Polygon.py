# link   : https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description/
# author : Mohamed Ibrahim

class Solution:    
    def monkeyMove(self, n: int) -> int:
        return (2 ** n - 2) % 1000000007
