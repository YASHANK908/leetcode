# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        first=headA
        sec=headB
        while first!=sec:
            first= first.next if first else headB
            sec=sec.next if sec else headA
        return sec    
         
        