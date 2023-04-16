# link   : https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
# author : Mohamed Ibrahim

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        sorted_nums = []
        for i in range(len(nums)-1 , -1 , -1):
            indx = bisect_left(sorted_nums , nums[i])
            result.append(indx)
            sorted_nums.insert(indx,nums[i])
        return result[::-1]
        
