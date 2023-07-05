# link   : https://leetcode.com/contest/biweekly-contest-98/problems/maximum-difference-by-remapping-a-digit/
# author : Mohamed Ibrahim

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        
        maxx = list(num)
        minn = list(num)
        
        M = num[0]
        x = num[0]
        flag = True
        for i in range(len(num)):
            if maxx[i] == '9':continue
            if flag : 
                M = maxx[i]
                flag = False
                
            if maxx[i] == M:
                print(maxx[i])
                maxx[i] = '9'
        maxx = ''.join(maxx)
                
            
        for i in range(len(num)):
            if minn[i] == x:
                minn[i] = '0'
                
        minn = ''.join(minn)
        
        print(maxx,minn)
        return int(maxx)-int(minn)
