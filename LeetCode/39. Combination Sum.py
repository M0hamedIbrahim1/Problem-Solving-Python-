# Link   : https://leetcode.com/problems/combination-sum/description/
# author : Mohamed Ibrahom



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def resc(lst,target,indx,subset):
            s =  sum(subset)
            if s == target:
                if subset not in res:
                    res.append(subset)
            if indx == len(lst) or s > target:
                return
            resc(lst,target,indx+1,subset)
            resc(lst,target,indx,subset+[lst[indx]])
        resc(candidates,target,0,[])
        return res
        
        
        
        
