# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow
         
        prev=None
        while(second):
            nxt=second.next
            second.next=prev
            prev=second 
            second=nxt
        first,second=head,prev
        maxsum=0
        while second:
            maxsum=max(maxsum,first.val+second.val)
            first=first.next 
            second=second.next
        return maxsum    