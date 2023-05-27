# link   : https://leetcode.com/problems/neighboring-bitwise-xor/description/
# author : Mohamed Ibrahim

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        orignel = [True]*len(derived)
        # derived = [1,1,0]
        for i in range(len(derived)-1):
            if derived[i] == 0 :
                orignel[i+1] = orignel[i]
            else:
                orignel[i+1] = not orignel[i]
        if derived[-1] == 0:
            return orignel[-1] == orignel[0]
        else:
            return orignel[-1] != orignel[0]
          
          
