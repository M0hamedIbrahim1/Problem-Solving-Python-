# link   : https://leetcode.com/problems/gas-station/description/
# author : Mohamed Ibrahim

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost) : 
            return -1
        summ = 0
        indx = 0
        for i in range(len(gas)):
            summ+= (gas[i]-cost[i])
            if summ < 0:
                indx = i+1
                summ = 0
        return indx
        
        
