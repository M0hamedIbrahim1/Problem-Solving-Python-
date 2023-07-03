# link   : https://leetcode.com/problems/buddy-strings/description/
# author : Mohamed Ibrahim

class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]
