# link   : https://leetcode.com/problems/sum-of-matrix-after-queries/description/
# author : Mohamed Ibrahim

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        queries.reverse()
        rows,cols = set(),set()
        res = 0
        
        for Type , index , val in (queries):
            
            if Type == 0:
                if index not in rows:
                    res+= val*(n - len(cols))
                    rows.add(index)
            else:
                if index not in cols:
                    res+= val*(n-len(rows))
                    cols.add(index)
        return res
        
