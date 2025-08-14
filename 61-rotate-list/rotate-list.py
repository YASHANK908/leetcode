# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head 
        tail=head
        length=1
        while tail.next:
            tail=tail.next
            length+=1
        tail.next=head    
        k=k%length
        stepstotail=length-k-1
        newtail=head
        for _ in range(stepstotail):
            newtail=newtail.next 
        newhead=newtail.next
        newtail.next=None
        return newhead

          

