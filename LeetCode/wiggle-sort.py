# link   : https://leetcode.com/problems/wiggle-sort-ii/
# author : Mohamed Ibrahim

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst = sorted(nums)
        for i in range(1 , len(nums) , 2):
            nums[i] = lst.pop()       
        for i in range(0 , len(nums) , 2):
            nums[i] = lst.pop()
            
            
