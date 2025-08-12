# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow=head
        fas=head
        while fas and fas.next:
            slow=slow.next
            fas=fas.next.next
        return slow
        