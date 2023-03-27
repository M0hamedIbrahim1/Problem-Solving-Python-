# link   : https://leetcode.com/problems/palindrome-linked-list/
# author : Mohamed Ibrahim

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return res == res[::-1]
