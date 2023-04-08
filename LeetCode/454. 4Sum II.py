# link   : https://leetcode.com/problems/4sum-ii/
# author : Mohamed Ibrahim

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = defaultdict(int)
        res = 0
        
        for i in nums1:
            for j in nums2:
                d[i+j]+=1
            
        for i in nums3:
            for j in nums4:
                res+=d[-1 * (i+j)]
        return res
