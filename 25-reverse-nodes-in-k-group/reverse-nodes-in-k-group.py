# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        def reverse(start,end):
            prev=None
            current=start
            while current!=end:
                next=current.next
                current.next=prev
                prev=current
                current=next
            return prev   
        temp=head
        l=0
        while temp:
            l+=1
            temp=temp.next
        dummy=ListNode()
        dummy.next=head
        prevg=dummy
        while l>=k:
            start=prevg.next
            end=start
            for _ in range(k):
                end=end.next
            newhead=reverse(start,end)
            prevg.next=newhead
            start.next=end
            prevg=start
            l-=k
        return dummy.next    
         