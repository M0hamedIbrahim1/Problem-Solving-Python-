# link   : https://leetcode.com/problems/top-k-frequent-elements/description/
# author : Mohamed Ibrahim


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        l = []
        for i in nums:
            d[i] = d.get(i,0)+1
        lst = sorted(d.items(),key = lambda d:d[1],reverse= True)   
        for j in range(k):
            l.append(lst[j][0])
        return l
        
        
        
        
