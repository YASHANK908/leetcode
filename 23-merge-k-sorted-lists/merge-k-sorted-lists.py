# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        dummy=ListNode(0)
        tail=dummy
        heap=[]
        for idx,node in enumerate(lists):
            if node:
                heappush(heap,(node.val,idx,node))
        while heap:
            val,idx,node=heappop(heap)
            tail.next=node
            tail=tail.next
            if node.next:
                heappush(heap,(node.next.val,idx,node.next))
        return dummy.next        

