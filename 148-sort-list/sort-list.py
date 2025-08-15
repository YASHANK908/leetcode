# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid= slow.next
        slow.next=None
        first = self.sortList(head)
        second= self.sortList(mid)
        dummy=ListNode(0)
        tail = dummy
        while first and second:
            if first.val<second.val:
                tail.next=first
                first=first.next
            else:
                tail.next=second
                second=second.next
            tail=tail.next
        tail.next=first or second 
        return dummy.next           

        