# link : https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
# author : Mohamed Ibrahim

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        res , vis = collections.defaultdict(list),[[] for i in range(len(nums)+1)]
        for indx,val in enumerate(nums):
            l = len(vis[val])
            res[l].append(val)
            vis[val].append(indx)
        return list(res.values())
        
