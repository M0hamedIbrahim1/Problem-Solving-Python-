# link   : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# author : Mohameed Ibrahim 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left , right,mx = 0 , 1 ,0
        while right < len(prices):
            m = prices[right] - prices[left]
            if prices[right] > prices[left]:
             mx = max(mx,m)
            else:
              left = right
            right+=1
        return mx
      
      
      
