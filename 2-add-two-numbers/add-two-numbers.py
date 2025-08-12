# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode( )
        current=dummy
        carry=0
        total=0
        while l1 or l2 or carry:
            val1= l1.val if l1 else 0 
            val2= l2.val if l2 else 0
            total=val1+val2+carry
            carry=total//10
            dig=total%10
            current.next=ListNode(dig )
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next    
        return dummy.next        

l1 = ListNode(5)
l1.next = ListNode(6)
l1.next.next = ListNode(7)

l2 = ListNode(7)
l2.next =ListNode(0)
l2.next.next = ListNode(8)
 
        