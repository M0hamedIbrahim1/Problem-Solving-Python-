# link   : https://leetcode.com/problems/contiguous-array/description/
# author : Mohamed Ibrahim 

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = 0
        max_length = 0
        d = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt-=1
            else:
                cnt+=1
            if cnt in d:
                max_length = max(max_length , i - d[cnt])
            else:
                d[cnt] = i
        return max_length
        
