# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        first=last=head
        for _ in range(k-1):
            first=first.next
        firstnode=first

        while first.next:
            first=first.next
            last=last.next

        firstnode.val,last.val=last.val,firstnode.val

        return head        

