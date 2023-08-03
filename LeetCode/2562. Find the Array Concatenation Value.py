# link   : https://leetcode.com/problems/find-the-array-concatenation-value/description/
# author : Mohamed Ibrahim

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        x = len(nums)
        while x >=2:
            res+= int(str(nums[0])+str(nums[-1]))
            nums.pop(0)
            nums.pop(x-2)
            x-=2
        if x:res+=nums[0]
        return res
