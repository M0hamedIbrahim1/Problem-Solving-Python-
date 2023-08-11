# link   : https://leetcode.com/contest/biweekly-contest-96/problems/minimum-operations-to-make-array-equal-ii/
# author : Mohamed Ibrahim

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        if k == 0:
            if nums1 == nums2 : return 0
            else:return -1
        
        
        plus , minus = 0,0
        for i in range(len(nums1)):
            if (nums1[i] - nums2[i]) % k != 0 : return -1
            
            if nums1[i] > nums2[i]:
                minus+=(nums1[i] - nums2[i])
            else:
                plus+=(nums2[i] - nums1[i])
            
        if plus != minus:return -1
        return plus//k
