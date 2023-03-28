# link   : https://leetcode.com/problems/merge-sorted-array/description/
# author : Mohamed Ibrahim

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = n+m -1
        while n > 0 and m > 0 : 
            if nums2[n-1] > nums1[m-1]:
                nums1[last] = nums2[n-1]
                n-=1
            else:
                nums1[last] = nums1[m-1]
                m-=1
            last-=1

        while n:
            nums1[last] = nums2[n-1]
            n-=1
            last-=1
            
