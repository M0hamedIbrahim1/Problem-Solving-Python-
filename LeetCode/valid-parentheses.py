# link   : https://leetcode.com/problems/valid-parentheses/description/
# author : Mohamed Ibrahim


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            elif stack:
                p = stack.pop()
                if i == ')' and p =='(':
                    continue
                elif i == ']' and p == '[':
                    continue
                elif i == '}' and p == '{':
                    continue
                else: return False
            else:
                return False
        if not stack:return True
        else:return False
        
        
