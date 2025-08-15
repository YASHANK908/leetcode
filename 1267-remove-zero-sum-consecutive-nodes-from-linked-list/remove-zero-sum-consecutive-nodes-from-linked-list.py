# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        dummy=ListNode(0)
        dummy.next=head
        prefixsum=0
        sumtonodes={}
        curr=dummy
        while curr:
            prefixsum+=curr.val
            sumtonodes[prefixsum]=curr
            curr=curr.next
        prefixsum=0
        curr=dummy
        while curr:
            prefixsum+=curr.val
            curr.next=sumtonodes[prefixsum].next
            curr=curr.next
        return dummy.next         
