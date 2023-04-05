# link   : https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        q = deque([root])
        ans = []
        while q:
            l = len(q)
            res = []
            for i in range(l):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                res.append(node.val)
            ans.append(res)
        return ans
      
      
