# link   : https://leetcode.com/problems/majority-element/description/
# author : Mohamed ibrahim

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
       
        # res = {}
        # mx,ans = -1,-1
        # for i in nums:
        #     res[i] = res.get(i,0)+1
        #     if res[i] > mx:
        #         mx = res[i]
        #         ans = i
        # return ans
