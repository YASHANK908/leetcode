"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head :
            return head
        current = head
        stack=[]
        while current:
            if current.child:
                if current.next:
                    stack.append(current.next)
                current.next=current.child
                current.child.prev=current
                current.child=None
            if not current.next and stack:
                nxt=stack.pop()
                current.next=nxt
                nxt.prev=current
            current=current.next
        return head                
        