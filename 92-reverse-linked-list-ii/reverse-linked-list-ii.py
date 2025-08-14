# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy=ListNode(0)
        dummy.next=head
        prevm=dummy
        for _ in range(left-1):
            prevm=prevm.next
        prev=None
        curr=prevm.next
        for _ in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        prevm.next.next=curr
        prevm.next=prev
        return dummy.next    

