# link :  https://leetcode.com/contest/weekly-contest-329/problems/sort-the-students-by-their-kth-score/ 
# author : Mohamed Ibrahim

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key = lambda x:x[k],reverse = True)
        return score
      
