# link   : https://leetcode.com/problems/longest-repeating-character-replacement/description/
# author : Mohamed Ibrahim


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        start,end,mx_freq,longetst_c = 0,0,0,0

        for end in range(len(s)):
            d[s[end]] = d.get(s[end],0)+1
            mx_freq = max(mx_freq,d[s[end]])
            if end+1 - start - mx_freq > k:
                d[s[start]] -=1
                start+=1
            longetst_c = end+1 - start
        return longetst_c



