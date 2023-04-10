# link   : https://leetcode.com/problems/find-peak-element/description/
# author : Mohamed Ibrahim

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        mx = 0
        for i in range(len(nums)):
            if i == 0:
                mx = 0
                continue
            if i == len(nums)-1 and nums[i]>nums[i-1]:
                mx = i
                continue
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

        return mx
      
