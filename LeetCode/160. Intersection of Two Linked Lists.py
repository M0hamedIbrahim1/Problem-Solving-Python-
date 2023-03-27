# link   : https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# author : Mohamed Ibrahim

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA,curB = headA,headB
        LenA,LenB = 0,0
        while curA is not None:
            curA = curA.next
            LenA+=1
        while curB is not None:
            curB = curB.next
            LenB+=1 

        curA,curB = headA,headB

        if LenA > LenB:
            for i in range(LenA-LenB):
                curA = curA.next
        elif LenB > LenA:
            for i in range(LenB-LenA):
                curB = curB.next
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA
        
        
