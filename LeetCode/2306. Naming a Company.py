# link   : https://leetcode.com/problems/naming-a-company/description/
# author : Mohamed ibrahim

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
            dic = defaultdict(set)
            ans = 0
            for i in ideas:
                dic[i[0]].add(i[1:])
            for i in dic.keys():
                for j in dic.keys():
                    if i>=j:
                        continue
                    same = len(dic[i] & dic[j])
                    ans+= (2 * (len(dic[i])-same) * (len(dic[j])-same))
            return ans
            
            
            
