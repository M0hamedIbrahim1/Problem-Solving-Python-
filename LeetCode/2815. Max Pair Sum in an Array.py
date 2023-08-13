# link : https://leetcode.com/problems/max-pair-sum-in-an-array/description/
# author : Mohamed ibrahim

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort()
        d = defaultdict(list)
        for i in range(len(nums)):
            s = int(max(str(nums[i])))
            d[s].append(nums[i])
        
        mx = 0
        for k in d:
            if len(d[k]) > 1 :
                mx = max(mx , d[k][-1] + d[k][-2])
        
        return -1 if mx == 0 else mx
      
