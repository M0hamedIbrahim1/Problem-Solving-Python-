# link   : https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
# author : Mohamed Ibrahim

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
      # defaultdict(<class 'list'>, {}) 
      group_dic = defaultdict(list) 

      ans = []

      for idx, size in enumerate(groupSizes):
        group_dic[size].append(idx)
        if(len(group_dic[size]) == size):
          ans.append(group_dic[size])
          del group_dic[size]
      return ans

