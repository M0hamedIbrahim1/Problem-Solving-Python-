# link   : https://leetcode.com/problems/shuffle-the-array/description/
# Author : Mohamed ibrahim



class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst = []
        l = nums[:n]
        r = nums[n:]
        i = 0
        while i < n:
            lst.append(l[i])
            lst.append(r[i])
            i+=1
        return lst
      
      
      
