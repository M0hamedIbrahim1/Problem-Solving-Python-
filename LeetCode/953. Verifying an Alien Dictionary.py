# Link   : https://leetcode.com/problems/verifying-an-alien-dictionary
# author : Mohamed ibrahim



class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i = 0
        while i < len(words)-1:
            i_1,i_2 = 0,0
            while i_1 < len(words[i]) and i_1 < len(words[i+1]):
                if order.index(words[i][i_1]) > order.index(words[i+1][i_1]):
                    return False
                elif order.index(words[i][i_1]) < order.index(words[i+1][i_1]):
                    break
                i_1+=1
            if len(words[i+1]) < len(words[i]) and words[i+1] == words[i][:len(words[i+1])]:
                return False
            i+=1
        return True
        
        
