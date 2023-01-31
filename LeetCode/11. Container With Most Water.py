# link   : https://leetcode.com/problems/container-with-most-water/description/
# author : Mohamed Ibrahim


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j,mx = 0 ,len(height)-1,0
        while i < j:
            mx = max(mx,min(height[j],height[i])*(j-i))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return mx
        
        
