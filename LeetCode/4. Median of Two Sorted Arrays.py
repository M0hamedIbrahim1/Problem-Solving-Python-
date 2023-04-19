# link   : https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# author : Mohamed Ibrahim

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i , j = 0,0
        n , m = len(nums1),len(nums2)
        while i < n and j < m:
            if nums2[j]>nums1[i]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i < n or j < m:
            if  i!= n :
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1

        return res[len(res)//2] if len(res) % 2 else (res[len(res)//2] + res[(len(res)//2)-1] ) /2
        
