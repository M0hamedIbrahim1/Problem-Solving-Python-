# link : https://leetcode.com/contest/biweekly-contest-101/problems/find-the-substring-with-maximum-cost/ 
# author : Mohamed Ibrahim


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = defaultdict(int)
        for indx in range(len(chars)):
            d[chars[indx]] = vals[indx]
        
        mx,Sum = 0,0
        for i in range(len(s)):
            if s[i] in d:
                Sum+=d[s[i]]
            else:
                Sum+=(ord(s[i])-97)+1
            if Sum < 0 : Sum = 0
            mx = max(Sum,mx)
        return mx

