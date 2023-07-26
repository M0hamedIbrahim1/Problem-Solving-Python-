# link   : https://leetcode.com/problems/distribute-money-to-maximum-children/description/
# author : Mohamed Ibrahim

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children : return -1
        
        n =  8*children - money
        if n <= 0 : return children -( n < 0)
        
        res , rem = divmod(money - children , 7)
        
        if rem == 3 and res == children-1:return res-1
        return res
