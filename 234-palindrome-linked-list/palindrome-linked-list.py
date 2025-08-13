# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        def reverse(head):
            prev=None
            current=head
            while current:
                next=current.next
                current.next=prev
                prev=current
                current=next
            return prev    
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        secondhalf= reverse(slow)
     
        firsthalf=head
        while secondhalf:
            if firsthalf.val!=secondhalf.val:
                return False
            firsthalf=firsthalf.next
            secondhalf=secondhalf.next
        return True        
    