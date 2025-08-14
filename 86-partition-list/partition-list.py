# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        
        lesshead=ListNode(0)
        greaterhead=ListNode(0)
        less=lesshead
        greater=greaterhead

        current=head
        while current:
            if current.val<x:
                less.next=current
                less=less.next
            else: 
                greater.next=current   
                greater=greater.next
            current=current.next 
        greater.next=None
        less.next=greaterhead.next
        return lesshead.next       

         
        