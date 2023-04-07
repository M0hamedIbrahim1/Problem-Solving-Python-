# link   : https://leetcode.com/problems/sort-colors/description/
# author : Mohamed Ibrahim

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(nums)-1
        i = 0

        def swap(l,r):
            nums[l],nums[r] = nums[r],nums[l]
        while i <= r:
            if nums[i] == 0:
                swap(i,l)
                l+=1
            elif nums[i] == 2:
                swap(i,r)
                r-=1
                i-=1
            i+=1
        
        
