# link   : https://leetcode.com/problems/longest-consecutive-sequence/solutions/
# author : Mohamed Ibrahim

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictt = dict()
        nums.sort()
        for i in nums:
            dictt[i] = dictt.get(i-1,0)+1
        if len(list(dictt.values())) != 0:
          return (max(list(dictt.values())))
        else : return 0 
        
        
