# link   : https://leetcode.com/problems/merge-two-sorted-lists/description/
# author : Mohamed Ibrahim

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ref = Node = ListNode()
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                Node.next = list1
                list1 = list1.next
            else:
                Node.next = list2
                list2 = list2.next  
            Node = Node.next
        Node.next = list1 or list2  
        return ref.next
        
