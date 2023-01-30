# link   : https://leetcode.com/problems/3sum/description/
# author : Mohamed Ibrahim


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        for i in range(len(nums)-1):
            j = i+1
            k = len(nums)-1
            while j < k:
                summ = nums[i]+nums[j]+nums[k]
                if summ == 0: 
                    s.add((nums[i],nums[j],nums[k]))
                    j+=1; k-=1
                elif summ < 0 : j+=1
                else : k-=1
  
        output = list(s)
        return output
    
    
    
    
