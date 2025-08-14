# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return head
        slow=fast= head
        while fast and fast.next:
            slow=slow.next
            
            fast=fast.next.next
        prev,curr=None,slow.next
        slow.next=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
         
        
        first,second=head,prev
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2

            

         
        