# link : https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
# author : Mohamed Ibrahim

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter(nums)
        d = defaultdict(int)
        
        for i in range(len(nums)):
            d[nums[i]]+=1
            if (cnt[nums[i]] - d[nums[i]]) * 2 > n-(i+1) and d[nums[i]]*2 > i+1:
                return i
        return -1
