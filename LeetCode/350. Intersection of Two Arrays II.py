# link   : https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# author : Mohamed Ibrahim

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d1 = Counter(nums1)
        d2 = Counter(nums2)

        for i in d1:
            if d2.get(i,0):
                mn = min(d1[i],d2[i])
                x = mn*[i]
                res.extend(x)
        return res
        
        
