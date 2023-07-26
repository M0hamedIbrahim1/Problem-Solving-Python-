# Link   : https://leetcode.com/contest/biweekly-contest-100/problems/find-score-of-an-array-after-marking-all-elements/
# author : Mohamed Ibrahim


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [0]*n
        score = 0
        s = sorted(range(n) , key = lambda x:nums[x])
        
        for i in range(n):
            if not visited[s[i]]:
                
                score+= nums[s[i]]
                visited[s[i]] = 1
                
                if s[i] - 1 >= 0 : visited[s[i]-1] = 1
                if s[i] + 1 < n : visited[s[i]+1] = 1
                    
        return score
