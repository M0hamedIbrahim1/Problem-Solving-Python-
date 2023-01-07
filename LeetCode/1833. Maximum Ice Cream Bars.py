# Link   : https://leetcode.com/problems/maximum-ice-cream-bars/description/
# author : Mohamed Ibrahim


class Solution(object):
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = 0
        for i in sorted(costs):
            if i <= coins:
                cnt+=1
                coins-=i
            else: break
        return cnt
            
            
            
