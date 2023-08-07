# link   : https://leetcode.com/contest/biweekly-contest-110/problems/account-balance-after-rounded-purchase/
# author : Mohamed Ibrahim

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        n = 100 - purchaseAmount
        lst_n = n % 10 
        
        if lst_n <= 5 and lst_n:
            return n - lst_n 
        elif lst_n > 5 :
            return n + (10 - lst_n)
    
        return 100 - purchaseAmount
