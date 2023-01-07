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
            
            
            
            
            
other Soluation ( RECURSION )

class Solution(object):
    def resc(self,lst,n,sum):
        if sum == 0 or n == 0:
            return 0
        if lst[n-1] <= sum:
            return max(1+self.resc(lst,n-1,sum-lst[n-1]),self.resc(lst,n-1,sum))
        else:
            return self.resc(lst,n-1,sum)

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return self.resc(costs,len(costs),coins)
    
    
    
    
