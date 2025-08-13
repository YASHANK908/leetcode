# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        current=head
        while current:
            if  current.next and current.val==current.next.val:
                dup=current.val
                while current and current.val==dup:
                    current=current.next
                prev.next=current    
            else:
                prev=current
                current=current.next
        return dummy.next    
         
        