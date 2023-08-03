# link   : https://leetcode.com/problems/substring-xor-queries/description/
# author : Mohamed Ibrahim

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        def fun():
            return False
        d=defaultdict(fun)
        for i in range(len(s)):
            for j in range(i,min(len(s),i+32)):
                ss=s[i:j+1]
                if d[ss]:
                    continue               #need to store first occurence, so if already present before, skip
                d[ss]=(i,j)
                
            
        ans=[]
        for a,b in queries:
            xor=a^b
            test=str(bin(xor))[2:]
            print(test)
            if d[test]:
                ans.append(d[test])
            else:
                ans.append((-1,-1))
        return ans
            

