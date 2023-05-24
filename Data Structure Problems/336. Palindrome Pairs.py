# link  : https://leetcode.com/problems/palindrome-pairs/
# author : Mohamed Ibrahim
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
            
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])
                
            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])
                
            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[:j] != '':
                    s,l = word[::-1],len(word)
                    if word[j:] == s[ : l-j]:
                        res.append([i , backward[ word[:j] ] ])

                    
        return res
        
