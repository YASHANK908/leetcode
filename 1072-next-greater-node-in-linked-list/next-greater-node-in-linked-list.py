# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        values=[]
        while head:
            values.append(head.val)
            head=head.next
        res=[0]*len(values)
        stack=[]

        for i,val in enumerate(values):
            while stack and values[stack[-1]]< val:
                idx=stack.pop()
                res[idx]=val
            stack.append(i)
        return res            
        