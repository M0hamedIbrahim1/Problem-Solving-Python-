# link   : https://leetcode.com/problems/subarray-sum-equals-k/description/
# author : Mohamed Ibrahim

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        SUM,cnt = 0,0
        for i in range(n):
            SUM+=nums[i]
            if d.get(SUM-k , 0):
                cnt+= d[SUM-k]
            d[SUM]+=1
        return cnt
