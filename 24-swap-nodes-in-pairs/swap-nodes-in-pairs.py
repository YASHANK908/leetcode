# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        while head and head.next:
            first=head
            second=head.next
            prev.next=second
        
            first.next=second.next
            second.next=first
            prev=first
            head=first.next
        return dummy.next    
        